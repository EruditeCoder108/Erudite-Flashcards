(function () {
  let api = window.eruditeFlashcards || window.eruditeMobileFlashcards || null;

  function getNativeApi() {
    api = window.eruditeFlashcards || window.eruditeMobileFlashcards || api || null;
    return api;
  }
  const mirroredStateKeys = new Set([
    'flashcardSetDraft',
    'currentStudyProgress',
    'srsModeEnabled',
    'customCursorEnabled',
    'cursorStyle'
  ]);
  const legacyDurableKeys = [
    'flashcardSets',
    'flashcardClasses',
    'flashcardSetDraft',
    'currentStudyProgress',
    'srsModeEnabled',
    'studyProgress'
  ];
  let isHydrating = false;
  let isWritingStateMirror = false;

  function readLocal(key, fallback) {
    try {
      const raw = localStorage.getItem(key);
      return raw ? JSON.parse(raw) : fallback;
    } catch (error) {
      return fallback;
    }
  }

  function writeLocal(key, value) {
    localStorage.setItem(key, JSON.stringify(value));
    return value;
  }

  function parseMirroredStateValue(key, raw) {
    if (raw === null || raw === undefined) return null;
    if (key === 'srsModeEnabled') return raw === true || raw === 'true';
    try {
      return JSON.parse(raw);
    } catch (_error) {
      return raw;
    }
  }

  function writeStateMirror(key, value) {
    if (!mirroredStateKeys.has(key)) return;
    isWritingStateMirror = true;
    try {
      const serialized = key === 'srsModeEnabled'
        ? String(Boolean(value))
        : JSON.stringify(value);
      localStorage.setItem(key, serialized);
    } finally {
      isWritingStateMirror = false;
    }
  }

  function removeStateMirror(key) {
    if (!mirroredStateKeys.has(key)) return;
    isWritingStateMirror = true;
    try {
      localStorage.removeItem(key);
    } finally {
      isWritingStateMirror = false;
    }
  }

  function readFileAsDataUrl(file) {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = () => resolve(reader.result);
      reader.onerror = () => reject(reader.error);
      reader.readAsDataURL(file);
    });
  }

  function normalizeSrsState(value) {
    if (typeof value === 'number') return ['New', 'Learning', 'Review', 'Relearning'][value] || 'New';
    return value || 'New';
  }

  function normalizeTagList(value) {
    if (Array.isArray(value)) return value.map(item => String(item).trim()).filter(Boolean);
    return String(value || '').split(',').map(item => item.trim()).filter(Boolean);
  }

  function timeValue(value) {
    if (!value) return null;
    const time = new Date(value).getTime();
    return Number.isFinite(time) ? time : null;
  }

  function dayKey(value) {
    const time = timeValue(value);
    if (!time) return '';
    const date = new Date(time);
    date.setHours(0, 0, 0, 0);
    return String(date.getTime());
  }

  function srsDayKey(value, rolloverHour = 4) {
    const date = new Date(value || Date.now());
    date.setHours(date.getHours() - rolloverHour, 0, 0, 0);
    return date.toISOString().slice(0, 10);
  }

  function isBuried(buriedUntil, nowMs = Date.now()) {
    const until = timeValue(buriedUntil);
    return Boolean(until && until > nowMs);
  }

  function isSrsDue(srs, nowMs = Date.now()) {
    if (!srs || !srs.due) return false;
    const state = normalizeSrsState(srs.state);
    const due = timeValue(srs.due);
    if (!due) return true;
    if (state === 'Learning' || state === 'Relearning') return due <= nowMs;
    return srsDayKey(due) <= srsDayKey(nowMs);
  }

  function normalizedRatingName(value) {
    const rating = String(value || '').trim().toLowerCase();
    if (rating === 'again' || rating === '1') return 'Again';
    if (rating === 'hard' || rating === '2') return 'Hard';
    if (rating === 'good' || rating === '3') return 'Good';
    if (rating === 'easy' || rating === '4') return 'Easy';
    return '';
  }

  function emptyRatingCounts() {
    return { Again: 0, Hard: 0, Good: 0, Easy: 0 };
  }

  function createRatingWindows() {
    return {
      '7': emptyRatingCounts(),
      '30': emptyRatingCounts(),
      '90': emptyRatingCounts(),
      all: emptyRatingCounts()
    };
  }

  function browserReviewStats(history, nowMs = Date.now()) {
    const todayKey = dayKey(nowMs);
    const sevenDaysAgo = nowMs - (7 * 24 * 60 * 60 * 1000);
    const thirtyDaysAgo = nowMs - (30 * 24 * 60 * 60 * 1000);
    const ninetyDaysAgo = nowMs - (90 * 24 * 60 * 60 * 1000);
    let lastReviewedAt = null;
    let againCount = 0;
    let failedRecently = false;
    let failedToday = false;
    const ratingCounts = emptyRatingCounts();
    const ratingWindows = createRatingWindows();
    for (const review of Array.isArray(history) ? history : []) {
      const rating = normalizedRatingName(review?.rating || review?.grade);
      const reviewedAt = timeValue(review?.reviewedAt || review?.time || review?.date);
      if (reviewedAt && (!lastReviewedAt || reviewedAt > lastReviewedAt)) lastReviewedAt = reviewedAt;
      if (rating) {
        ratingCounts[rating] += 1;
        ratingWindows.all[rating] += 1;
        if (reviewedAt >= sevenDaysAgo) ratingWindows['7'][rating] += 1;
        if (reviewedAt >= thirtyDaysAgo) ratingWindows['30'][rating] += 1;
        if (reviewedAt >= ninetyDaysAgo) ratingWindows['90'][rating] += 1;
      }
      if (rating === 'Again') {
        againCount += 1;
        if (reviewedAt && reviewedAt >= sevenDaysAgo) failedRecently = true;
        if (reviewedAt && dayKey(reviewedAt) === todayKey) failedToday = true;
      }
    }
    return { againCount, failedRecently, failedToday, lastReviewedAt, ratingCounts, ratingWindows };
  }

  function hasCardMedia(card, kind) {
    if (kind === 'image' && (card.termImage || card.definitionImage)) return true;
    const media = card.media || {};
    const items = [
      ...(Array.isArray(media.term) ? media.term : []),
      ...(Array.isArray(media.definition) ? media.definition : [])
    ];
    return items.some(item => {
      const itemKind = String(item?.kind || item?.mediaType || '').toLowerCase();
      const mime = String(item?.mime || item?.type || '').toLowerCase();
      if (kind === 'audio') return itemKind === 'audio' || mime.startsWith('audio/');
      if (kind === 'image') return itemKind === 'image' || mime.startsWith('image/');
      return false;
    });
  }

  function normalizeBulkDueIso(value) {
    const raw = String(value || '').trim();
    if (!raw) return null;
    const date = /^\d{4}-\d{2}-\d{2}$/.test(raw)
      ? new Date(`${raw}T04:00:00`)
      : new Date(raw);
    return Number.isFinite(date.getTime()) ? date.toISOString() : null;
  }

  async function listSets() {
    const nativeApi = getNativeApi();
    if (nativeApi) return nativeApi.listSets();
    return readLocal('flashcardSets', []);
  }

  async function listSetsMeta(options = {}) {
    const nativeApi = getNativeApi();
    if (nativeApi?.listSetsMeta) return nativeApi.listSetsMeta(options);
    return listSets(); // fallback: load full sets
  }

  async function getSetStatsMeta(setIds = []) {
    const nativeApi = getNativeApi();
    if (nativeApi?.getSetStatsMeta) return nativeApi.getSetStatsMeta(setIds);
    return [];
  }

  async function getSet(id) {
    const nativeApi = getNativeApi();
    if (nativeApi) return nativeApi.getSet(id);
    const sets = await listSets();
    return sets.find((set) => String(set.id) === String(id)) || null;
  }

  async function listCardsForBrowser() {
    const nativeApi = getNativeApi();
    if (nativeApi?.listCardsForBrowser) return nativeApi.listCardsForBrowser();
    const sets = await listSets();
    const classes = await listClasses();
    const classLookup = new Map((classes || []).map(item => [String(item.id), item]));
    const nowMs = Date.now();
    const cards = [];
    (sets || []).forEach(set => {
      const className = set.classId ? classLookup.get(String(set.classId))?.name : 'General';
      (set.cards || []).forEach((card, index) => {
        const srs = card.srs || null;
        const state = normalizeSrsState(srs?.state);
        const dueTime = timeValue(srs?.due);
        const suspended = Boolean(card.suspended);
        const buried = isBuried(card.buriedUntil, nowMs);
        const reviews = browserReviewStats(card.reviewHistory || [], nowMs);
        const tags = Array.isArray(card.tags) ? card.tags : [];
        cards.push({
          id: card.id,
          setId: set.id,
          noteId: card.noteId || null,
          noteType: card.noteType || 'basic',
          cardTemplate: card.cardTemplate || 'front-back',
          clozeIndex: card.clozeIndex || null,
          deck: set.name || 'Untitled Set',
          classId: set.classId || null,
          className: className || 'General',
          position: index,
          term: card.term || '',
          definition: card.definition || '',
          tags,
          srsState: state,
          due: srs?.due || null,
          dueTime,
          isDue: !suspended && !buried && Boolean(srs && state !== 'New' && isSrsDue(srs, nowMs)),
          isOverdue: !suspended && !buried && Boolean(srs && state !== 'New' && dueTime && srsDayKey(dueTime) < srsDayKey(nowMs)),
          suspended,
          buriedUntil: card.buriedUntil || null,
          buried,
          failedRecently: reviews.failedRecently,
          failedToday: reviews.failedToday,
          leech: reviews.againCount >= 8 || Number(srs?.lapses || 0) >= 8,
          noTags: !tags.length,
          hasImage: hasCardMedia(card, 'image'),
          hasAudio: hasCardMedia(card, 'audio'),
          reviewCount: Array.isArray(card.reviewHistory) ? card.reviewHistory.length : 0,
          againCount: reviews.againCount,
          ratingCounts: reviews.ratingCounts,
          ratingWindows: reviews.ratingWindows,
          reps: Number(srs?.reps || 0),
          lapses: Number(srs?.lapses || 0),
          intervalDays: Number(srs?.scheduled_days || srs?.elapsed_days || 0),
          lastReviewedAt: reviews.lastReviewedAt,
          lastModified: Number(card.lastModified || set.lastModified || 0)
        });
      });
    });
    return cards;
  }

  async function bulkUpdateCards(cardIds = [], action = '', options = {}) {
    const nativeApi = getNativeApi();
    if (nativeApi?.bulkUpdateCards) return nativeApi.bulkUpdateCards(cardIds, action, options);

    const ids = new Set((Array.isArray(cardIds) ? cardIds : []).map(value => String(value)));
    if (!ids.size) return { updated: 0, deleted: 0, moved: 0, touchedSetIds: [] };

    const normalizedAction = String(action || '').trim().toLowerCase();
    const allowedActions = new Set(['suspend', 'unsuspend', 'reset-srs', 'delete', 'move', 'set-due', 'add-tag', 'remove-tag']);
    if (!allowedActions.has(normalizedAction)) {
      throw new Error(`Unsupported bulk card action: ${action}`);
    }
    const sets = await listSets();
    const now = Date.now();
    const touchedSetIds = new Set();
    const movedCards = [];
    let updated = 0;
    let deleted = 0;
    let moved = 0;
    const dueIso = normalizedAction === 'set-due' ? normalizeBulkDueIso(options.due || options.dueDate) : null;
    const tagList = normalizedAction === 'add-tag' || normalizedAction === 'remove-tag'
      ? normalizeTagList(options.tags || options.tag)
      : [];
    const targetSetId = String(options.targetSetId || '');
    const targetSet = normalizedAction === 'move'
      ? sets.find(set => String(set.id) === targetSetId)
      : null;

    if (normalizedAction === 'set-due' && !dueIso) throw new Error('Choose a valid due date.');
    if ((normalizedAction === 'add-tag' || normalizedAction === 'remove-tag') && !tagList.length) throw new Error('Enter at least one tag.');
    if (normalizedAction === 'move' && !targetSet) throw new Error('Destination deck was not found.');

    const nextSets = sets.map(set => {
      const nextCards = [];
      let touched = false;
      for (const card of set.cards || []) {
        if (!ids.has(String(card.id))) {
          nextCards.push(card);
          continue;
        }

        touched = true;
        touchedSetIds.add(String(set.id));
        if (normalizedAction === 'delete') {
          deleted += 1;
          continue;
        }

        const nextCard = { ...card, lastModified: now };
        if (normalizedAction === 'suspend') {
          nextCard.suspended = true;
        } else if (normalizedAction === 'unsuspend') {
          nextCard.suspended = false;
        } else if (normalizedAction === 'reset-srs') {
          delete nextCard.srs;
          if (options.deleteHistory) nextCard.reviewHistory = [];
        } else if (normalizedAction === 'set-due') {
          const baseSrs = nextCard.srs || {};
          nextCard.srs = {
            ...baseSrs,
            state: baseSrs.state && normalizeSrsState(baseSrs.state) !== 'New' ? baseSrs.state : 'Review',
            due: dueIso,
            elapsed_days: Number(baseSrs.elapsed_days || 0),
            scheduled_days: Number(baseSrs.scheduled_days || 0),
            reps: Number(baseSrs.reps || 0),
            lapses: Number(baseSrs.lapses || 0),
            stability: Number(baseSrs.stability || 0),
            difficulty: Number(baseSrs.difficulty || 0)
          };
        } else if (normalizedAction === 'add-tag') {
          const currentTags = normalizeTagList(nextCard.tags || []);
          const lower = new Set(currentTags.map(tag => tag.toLowerCase()));
          nextCard.tags = [...currentTags, ...tagList.filter(tag => !lower.has(tag.toLowerCase()))];
        } else if (normalizedAction === 'remove-tag') {
          const remove = new Set(tagList.map(tag => tag.toLowerCase()));
          nextCard.tags = normalizeTagList(nextCard.tags || []).filter(tag => !remove.has(tag.toLowerCase()));
        } else if (normalizedAction === 'move') {
          movedCards.push(nextCard);
          moved += 1;
          continue;
        }

        nextCards.push(nextCard);
        updated += 1;
      }
      return touched
        ? { ...set, cards: nextCards, lastModified: now }
        : set;
    });

    if (normalizedAction === 'move' && movedCards.length) {
      touchedSetIds.add(targetSetId);
      const target = nextSets.find(set => String(set.id) === targetSetId);
      if (target) {
        target.cards = [...(target.cards || []), ...movedCards];
        target.lastModified = now;
        updated += movedCards.length;
      }
    }

    writeLocal('flashcardSets', nextSets);
    return { updated, deleted, moved, touchedSetIds: Array.from(touchedSetIds) };
  }

  async function saveSet(set) {
    const nativeApi = getNativeApi();
    if (nativeApi) return nativeApi.saveSet(set);
    const sets = await listSets();
    const existing = sets.find((item) => String(item.id) === String(set.id));
    const next = {
      ...set,
      id: set.id || Date.now(),
      created: set.created || existing?.created || Date.now(),
      openedCount: set.openedCount ?? existing?.openedCount ?? 0,
      lastOpened: set.lastOpened ?? existing?.lastOpened ?? null,
      lastModified: Date.now()
    };
    const updated = sets.filter((item) => String(item.id) !== String(next.id));
    updated.push(next);
    writeLocal('flashcardSets', updated);
    return next;
  }

  async function replaceSets(sets) {
    const nativeApi = getNativeApi();
    if (nativeApi) return nativeApi.replaceSets(sets);
    writeLocal('flashcardSets', Array.isArray(sets) ? sets : []);
    return Array.isArray(sets) ? sets : [];
  }

  async function deleteSet(id) {
    const nativeApi = getNativeApi();
    if (nativeApi) return nativeApi.deleteSet(id);
    const sets = await listSets();
    writeLocal('flashcardSets', sets.filter((set) => String(set.id) !== String(id)));
    return true;
  }

  async function listClasses() {
    const nativeApi = getNativeApi();
    if (nativeApi) return nativeApi.listClasses();
    return readLocal('flashcardClasses', []);
  }

  async function saveClass(classData) {
    const nativeApi = getNativeApi();
    if (nativeApi) return nativeApi.saveClass(classData);
    const classes = await listClasses();
    const now = Date.now();
    const next = {
      ...classData,
      id: classData.id || `class-${now}`,
      name: String(classData.name || 'Untitled Class').trim() || 'Untitled Class',
      color: /^#[0-9a-f]{6}$/i.test(String(classData.color || '')) ? classData.color : '#3B82F6',
      created: classData.created || now,
      lastModified: now
    };
    const updated = classes.filter((item) => String(item.id) !== String(next.id));
    updated.push(next);
    writeLocal('flashcardClasses', updated);
    return next;
  }

  async function deleteClass(classId) {
    const nativeApi = getNativeApi();
    if (nativeApi) return nativeApi.deleteClass(classId);
    const classes = await listClasses();
    writeLocal('flashcardClasses', classes.filter((item) => String(item.id) !== String(classId)));
    const sets = await listSets();
    writeLocal('flashcardSets', sets.map((set) => (
      String(set.classId || '') === String(classId) ? { ...set, classId: null, lastModified: Date.now() } : set
    )));
    return true;
  }

  async function getProgress(setId) {
    const nativeApi = getNativeApi();
    if (nativeApi) return nativeApi.getProgress(setId);
    const progress = readLocal('studyProgress', {});
    return progress[String(setId)] || null;
  }

  async function getAllProgress() {
    const nativeApi = getNativeApi();
    if (nativeApi?.getAllProgress) return nativeApi.getAllProgress();
    return readLocal('studyProgress', {});
  }

  async function saveProgress(setId, value) {
    const nativeApi = getNativeApi();
    if (nativeApi) return nativeApi.saveProgress(setId, value);
    const progress = readLocal('studyProgress', {});
    progress[String(setId)] = value;
    writeLocal('studyProgress', progress);
    return true;
  }

  async function saveCardProgress(setId, cardId, patch) {
    const nativeApi = getNativeApi();
    if (nativeApi?.saveCardProgress) return nativeApi.saveCardProgress(setId, cardId, patch);
    return false;
  }

  async function saveCardProgressBatch(setId, patches) {
    const nativeApi = getNativeApi();
    if (nativeApi?.saveCardProgressBatch) return nativeApi.saveCardProgressBatch(setId, patches);
    if (nativeApi?.saveCardProgress) {
      await Promise.all(Object.entries(patches).map(([cardId, patch]) => nativeApi.saveCardProgress(setId, cardId, patch).catch(() => {})));
      return true;
    }
    return false;
  }

  async function getSettings() {
    const nativeApi = getNativeApi();
    if (nativeApi) return nativeApi.getSettings();
    return readLocal('flashcards-settings', {});
  }

  async function saveSettings(settings) {
    const nativeApi = getNativeApi();
    if (nativeApi) return nativeApi.saveSettings(settings);
    writeLocal('flashcards-settings', settings || {});
    return true;
  }

  async function mirrorLocalStorageWrite(key, value) {
    const nativeApi = getNativeApi();
    if (isHydrating || isWritingStateMirror || window.__eruditeApplyingSettings || !nativeApi) return;

    try {
      if (key === 'flashcardSets' || key === 'flashcardClasses') {
        return;
      } else if (key === 'flashcards-settings') {
        const current = await getSettings();
        await saveSettings({ ...current, ...(JSON.parse(value || '{}')) });
      } else if (key === 'flashcards-theme') {
        const current = await getSettings();
        await saveSettings({ ...current, theme: value || 'dark' });
      } else if (mirroredStateKeys.has(key)) {
        const parsedValue = parseMirroredStateValue(key, value);
        await setState(key, parsedValue);

        if (key === 'currentStudyProgress' && parsedValue && parsedValue.setId !== undefined) {
          await saveProgress(parsedValue.setId, parsedValue);
        }
      }
    } catch (error) {
      console.warn(`Could not mirror localStorage key "${key}" to local store:`, error);
    }
  }

  async function mirrorLocalStorageRemove(key) {
    const nativeApi = getNativeApi();
    if (isHydrating || isWritingStateMirror || !nativeApi) return;
    if (mirroredStateKeys.has(key)) {
      await removeState(key);
    }
  }

  function installLocalStorageMirror() {
    if (window.__eruditeLocalStorageMirrorInstalled) return;
    window.__eruditeLocalStorageMirrorInstalled = true;

    const originalSetItem = localStorage.setItem.bind(localStorage);
    const originalRemoveItem = localStorage.removeItem.bind(localStorage);

    localStorage.setItem = (key, value) => {
      originalSetItem(key, value);
      mirrorLocalStorageWrite(key, value);
    };

    localStorage.removeItem = (key) => {
      originalRemoveItem(key);
      mirrorLocalStorageRemove(key);
    };
  }

  async function migrateLegacyBrowserStorage() {
    const nativeApi = getNativeApi();
    if (!nativeApi) return;

    try {
      const localSets = readLocal('flashcardSets', null);
      const storedSets = await listSets();
      if (Array.isArray(localSets) && localSets.length > 0 && (!Array.isArray(storedSets) || storedSets.length === 0)) {
        await replaceSets(localSets);
      }

      const localClasses = readLocal('flashcardClasses', null);
      const storedClasses = await listClasses();
      if (Array.isArray(localClasses) && localClasses.length > 0 && (!Array.isArray(storedClasses) || storedClasses.length === 0)) {
        for (const classData of localClasses) {
          await saveClass(classData);
        }
      }

      const localSettings = readLocal('flashcards-settings', null);
      const storedSettings = await getSettings();
      if (localSettings && typeof localSettings === 'object' && (!storedSettings || Object.keys(storedSettings).length === 0)) {
        await saveSettings(localSettings);
      }

      for (const key of mirroredStateKeys) {
        const currentValue = nativeApi ? await nativeApi.getState(key) : await getState(key);
        const localRaw = localStorage.getItem(key);
        if ((currentValue === null || currentValue === undefined) && localRaw !== null) {
          const parsedValue = parseMirroredStateValue(key, localRaw);
          await setState(key, parsedValue);

          if (key === 'currentStudyProgress' && parsedValue && parsedValue.setId !== undefined) {
            await saveProgress(parsedValue.setId, parsedValue);
          }
        }
      }
    } catch (error) {
      console.warn('Could not migrate legacy browser flashcard storage:', error);
    }
  }

  function clearLegacyBrowserStorage() {
    if (!getNativeApi()) return;
    legacyDurableKeys.forEach(key => localStorage.removeItem(key));
  }

  async function hydrateLocalStorage() {
    installLocalStorageMirror();
    isHydrating = true;

    try {
      const nativeApi = getNativeApi();
      await migrateLegacyBrowserStorage();

      if (nativeApi) {
        const settings = await getSettings();
        if (settings && typeof settings === 'object') {
          localStorage.setItem('flashcards-settings', JSON.stringify(settings));
          if (settings.theme) {
            localStorage.setItem('flashcards-theme', settings.theme);
          }
        }
        // Do not clear legacy localStorage mirrors on mobile. They are a useful
        // read-only safety net if the native API is briefly unavailable.
        return;
      }

      const [sets, settings, srsMode, draft, progress, cursorEnabled, cursorStyle] = await Promise.all([
        listSets(),
        getSettings(),
        getState('srsModeEnabled'),
        getState('flashcardSetDraft'),
        getState('currentStudyProgress'),
        getState('customCursorEnabled'),
        getState('cursorStyle')
      ]);

      if (Array.isArray(sets)) {
        localStorage.setItem('flashcardSets', JSON.stringify(sets));
      }

      const classes = await listClasses();
      if (Array.isArray(classes)) {
        localStorage.setItem('flashcardClasses', JSON.stringify(classes));
      }

      if (settings && typeof settings === 'object') {
        localStorage.setItem('flashcards-settings', JSON.stringify(settings));
        if (settings.theme) {
          localStorage.setItem('flashcards-theme', settings.theme);
        }
      }

      if (srsMode !== null && srsMode !== undefined) {
        localStorage.setItem('srsModeEnabled', String(Boolean(srsMode)));
      }
      if (draft) {
        localStorage.setItem('flashcardSetDraft', JSON.stringify(draft));
      }
      if (progress) {
        localStorage.setItem('currentStudyProgress', JSON.stringify(progress));
      }
      if (cursorEnabled !== null && cursorEnabled !== undefined) {
        localStorage.setItem('customCursorEnabled', String(Boolean(cursorEnabled)));
      }
      if (cursorStyle) {
        localStorage.setItem('cursorStyle', cursorStyle);
      }
    } catch (error) {
      console.warn('Could not hydrate local flashcard state:', error);
    } finally {
      isHydrating = false;
    }
  }

  async function getState(key) {
    const nativeApi = getNativeApi();
    if (nativeApi) {
      if (key === 'srsModeEnabled') {
        const mirrored = localStorage.getItem(key);
        if (mirrored !== null) return parseMirroredStateValue(key, mirrored);
      }
      const value = await nativeApi.getState(key);
      if (value !== null && value !== undefined) return value;
      if (mirroredStateKeys.has(key)) {
        return parseMirroredStateValue(key, localStorage.getItem(key));
      }
      return value;
    }
    return readLocal(`erudite-state-${key}`, null);
  }

  async function setState(key, value) {
    const nativeApi = getNativeApi();
    if (nativeApi) {
      writeStateMirror(key, value);
      return nativeApi.setState(key, value);
    }
    writeLocal(`erudite-state-${key}`, value);
    return true;
  }

  async function removeState(key) {
    const nativeApi = getNativeApi();
    if (nativeApi) {
      removeStateMirror(key);
      return nativeApi.removeState(key);
    }
    localStorage.removeItem(`erudite-state-${key}`);
    return true;
  }

  async function saveImageFromFile(file, meta = {}) {
    const dataUrl = await readFileAsDataUrl(file);
    const nativeApi = getNativeApi();
    if (nativeApi) return nativeApi.saveImage(dataUrl, { ...meta, fileName: file.name });
    return dataUrl;
  }

  async function saveImageDataUrl(dataUrl, meta = {}) {
    const nativeApi = getNativeApi();
    if (nativeApi) return nativeApi.saveImage(dataUrl, meta);
    return dataUrl;
  }

  async function deleteImage(fileUrl) {
    const nativeApi = getNativeApi();
    if (nativeApi?.deleteImage) return nativeApi.deleteImage(fileUrl);
    return true;
  }

  async function saveFontFromFile(file) {
    const dataUrl = await readFileAsDataUrl(file);
    const nativeApi = getNativeApi();
    if (nativeApi) return nativeApi.saveFont(dataUrl, { fileName: file.name, prefix: 'content-font' });
    return dataUrl;
  }

  async function listPremadeSets(classId, subjectId) {
    const nativeApi = getNativeApi();
    if (nativeApi) return nativeApi.listPremadeSets(classId, subjectId);
    return [];
  }


  async function getDiagnostics() {
    const nativeApi = getNativeApi();
    if (nativeApi?.getDiagnostics) return nativeApi.getDiagnostics();

    const sets = await listSets();
    const classes = await listClasses();
    const settings = await getSettings();
    return {
      appVersion: 'web-preview',
      storageEngine: 'browser-localStorage',
      generatedAt: new Date().toISOString(),
      paths: {},
      counts: {
        sets: Array.isArray(sets) ? sets.length : 0,
        classes: Array.isArray(classes) ? classes.length : 0,
        cards: Array.isArray(sets)
          ? sets.reduce((total, set) => total + (Array.isArray(set.cards) ? set.cards.length : 0), 0)
          : 0
      },
      settings,
      health: {
        status: 'warning',
        issues: ['Browser preview storage is not the production SQLite store.']
      },
      recentBackups: [],
      brokenImageLinks: []
    };
  }

  async function exportBackup() {
    const nativeApi = getNativeApi();
    if (nativeApi?.exportBackup) return nativeApi.exportBackup();

    const sets = await listSets();
    const classes = await listClasses();
    const settings = await getSettings();
    const payload = {
      app: 'Erudite Flashcards',
      schemaVersion: 1,
      exportedAt: new Date().toISOString(),
      data: {
        sets,
        classes,
        settings,
        progress: readLocal('studyProgress', {}),
        state: {}
      }
    };
    const blob = new Blob([JSON.stringify(payload, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `erudite-flashcards-backup-${new Date().toISOString().slice(0, 10)}.json`;
    link.click();
    URL.revokeObjectURL(url);

    return {
      canceled: false,
      setCount: sets.length
    };
  }

  async function importBackup() {
    const nativeApi = getNativeApi();
    if (nativeApi?.importBackup) return nativeApi.importBackup();
    return {
      canceled: true,
      unsupported: true
    };
  }

  async function exportDelimited(format) {
    const nativeApi = getNativeApi();
    if (nativeApi?.exportDelimited) return nativeApi.exportDelimited(format);
    return {
      canceled: true,
      unsupported: true
    };
  }

  async function importDelimited() {
    const nativeApi = getNativeApi();
    if (nativeApi?.importDelimited) return nativeApi.importDelimited();
    return {
      canceled: true,
      unsupported: true
    };
  }

  async function recordReview(params) {
    const nativeApi = getNativeApi();
    if (nativeApi?.recordReview) return nativeApi.recordReview(params);
    return null;
  }

  async function undoReviewLog(cardId, logId) {
    const nativeApi = getNativeApi();
    if (nativeApi?.undoReviewLog) return nativeApi.undoReviewLog(cardId, logId);
    return null;
  }

  async function resetDeckSRS(setId, deleteHistory) {
    const nativeApi = getNativeApi();
    if (nativeApi?.resetDeckSRS) return nativeApi.resetDeckSRS(setId, deleteHistory);
    return null;
  }

  async function createDeckBackup(setId) {
    const nativeApi = getNativeApi();
    if (nativeApi?.createDeckBackup) return nativeApi.createDeckBackup(setId);
    return null;
  }

  async function createBackupSnapshot(reason = 'snapshot') {
    const nativeApi = getNativeApi();
    if (nativeApi?.createBackupSnapshot) return nativeApi.createBackupSnapshot(reason);
    return null;
  }

  async function saveStudySession(session) {
    const nativeApi = getNativeApi();
    if (nativeApi?.saveStudySession) return nativeApi.saveStudySession(session);
    return null;
  }

  async function getStudySessions(sinceMs) {
    const nativeApi = getNativeApi();
    if (nativeApi?.getStudySessions) return nativeApi.getStudySessions(sinceMs);
    return [];
  }

  window.flashcardStore = {
    listSets,
    listSetsMeta,
    getSetStatsMeta,
    listCardsForBrowser,
    bulkUpdateCards,
    getSet,
    saveSet,
    replaceSets,
    deleteSet,
    listClasses,
    saveClass,
    deleteClass,
    getProgress,
    getAllProgress,
    saveProgress,
    saveCardProgress,
    saveCardProgressBatch,
    getSettings,
    saveSettings,
    getState,
    setState,
    removeState,
    saveImageFromFile,
    saveImageDataUrl,
    deleteImage,
    saveFontFromFile,
    listPremadeSets,
    getDiagnostics,
    exportBackup,
    importBackup,
    exportDelimited,
    importDelimited,
    recordReview,
    undoReviewLog,
    resetDeckSRS,
    createDeckBackup,
    createBackupSnapshot,
    saveStudySession,
    getStudySessions
  };

  const menuApi = getNativeApi();
  window.flashcardMenuReady = menuApi?.onMenuCommand
    ? menuApi.onMenuCommand(command => {
        window.dispatchEvent(new CustomEvent('erudite-menu-command', { detail: command }));
      })
    : null;

  window.flashcardLocalReady = hydrateLocalStorage();
})();
