(function () {
  const schema = window.EruditeCore?.schema;
  const statsCore = window.EruditeCore?.stats;

  const params = new URLSearchParams(window.location.search);
  const reviewDueSession = params.get('reviewDue') === 'true';
  const requestedSrsMode = params.get('srs');
  const PROGRESS_MIRROR_PREFIX = 'erudite-mobile-progress:';
  const STUDY_PATCHES_KEY = 'erudite-mobile-study-card-patches-v1';

  const sounds = {
    flip: new Audio('../assets/flashcard-assets/flip-sound.mp3'),
    next: new Audio('../assets/flashcard-assets/Next-card.mp3'),
    success: new Audio('../assets/audio/success.mp3')
  };

  Object.values(sounds).forEach(audio => {
    audio.volume = 0.85;
  });

  function playSound(type) {
    try {
      const audio = sounds[type];
      if (audio) {
        audio.currentTime = 0;
        audio.play().catch(() => {});
      }
    } catch (_) {}
  }

  function triggerHaptic() {
    try {
      const Haptics = window.Capacitor?.Plugins?.Haptics;
      if (Haptics && typeof Haptics.impact === 'function') {
        Haptics.impact({ style: 'light' }).catch(() => {});
      } else if (navigator.vibrate) {
        navigator.vibrate(30);
      }
    } catch (_e) {}
  }

  const state = {
    set: null,
    allSets: [],
    srsMode: false,
    activeCards: [],
    normalOrder: [],
    studyOrder: 'forward',
    normalIndex: 0,
    srsIndex: 0,
    flipped: false,
    complete: false,
    nextDueSetId: null,
    sessionStats: {
      reviewed: 0,
      Again: 0,
      Hard: 0,
      Good: 0,
      Easy: 0,
      nextDue: null
    },
    settings: {},
    sessionStartedAt: null,
    sessionCardsViewed: null
  };

  const els = {
    shell: document.getElementById('study-shell'),
    title: document.getElementById('study-title'),
    modeLabel: document.getElementById('study-mode-label'),
    current: document.getElementById('progress-current'),
    total: document.getElementById('progress-total'),
    fill: document.getElementById('progress-fill'),
    hint: document.getElementById('gesture-hint'),
    back: document.getElementById('back-button'),
    prev: document.getElementById('prev-button'),
    card: null,
    stage: document.getElementById('card-stage'),
    ratingDock: document.getElementById('rating-dock'),
    completionModal: document.getElementById('completion-modal'),
    completionTitle: document.getElementById('completion-title'),
    completionCopy: document.getElementById('completion-copy'),
    completionStats: document.getElementById('completion-stats'),
    continueButton: document.getElementById('continue-button'),
    libraryButton: document.getElementById('library-button'),
    emptyModal: document.getElementById('empty-modal'),
    emptyCheckButton: document.getElementById('empty-check-button'),
    emptyLibraryButton: document.getElementById('empty-library-button'),
    imageModal: document.getElementById('image-modal'),
    zoomedImage: document.getElementById('zoomed-image'),
    imageClose: document.getElementById('image-close-button'),
    loadingCover: document.getElementById('study-loading-cover'),
    loadingTitle: document.getElementById('study-loading-title'),
    loadingCopy: document.getElementById('study-loading-copy'),
    toast: document.getElementById('study-toast')
  };

  const cards = [
    document.getElementById('card-0'),
    document.getElementById('card-1'),
    document.getElementById('card-2')
  ];

  let activeCardIndex = 1;
  let nextCardIndex = 2;
  let prevCardIndex = 0;

  let srsReviewedCardIds = new Set();
  let srsUndoStack = [];
  const studySessionId = 'session-mobile-' + Date.now() + '-' + Math.random().toString(36).substring(2, 7);

  const intervals = {
    Again: document.getElementById('interval-again'),
    Hard: document.getElementById('interval-hard'),
    Good: document.getElementById('interval-good'),
    Easy: document.getElementById('interval-easy')
  };

  let toastTimer = null;
  let dueSoonTimer = null;
  let pointer = null;
  let animating = false;
  let ratingInFlight = false;
  let ratingTimer = null;
  let queuedNavigation = null;
  let openedSaveTimer = null;
  let progressSaveTimer = null;
  let cardProgressSaveTimer = null;
  let dragFrame = 0;
  let queuedDrag = null;
  let transitionToken = 0;
  let flipTimer = null;
  let routeLeaving = false;
  let restoredProgress = null;
  const preloadedImages = new Set();
  const pendingCardPatches = new Map();
  const SWIPE_DURATION = 175;
  const FLIP_DURATION = 420;

  function showToast(message) {
    clearTimeout(toastTimer);
    els.toast.textContent = message;
    els.toast.classList.add('show');
    toastTimer = setTimeout(() => els.toast.classList.remove('show'), 1800);
  }

  function libraryUrl() {
    const fromTab = params.get('from') || 'library';
    return `../index.html#${fromTab}`;
  }

  function studyUrl(setId, reviewDue = false) {
    const fromTab = params.get('from') || 'library';
    const query = new URLSearchParams({
      setId: String(setId),
      srs: String(Boolean(reviewDue || state.srsMode)),
      from: fromTab
    });
    if (reviewDue) query.set('reviewDue', 'true');
    return `study.html?${query.toString()}`;
  }

  function showStudyLoader(title = 'Opening Study', copy = 'Preparing your cards') {
    if (els.loadingTitle) els.loadingTitle.textContent = title;
    if (els.loadingCopy) els.loadingCopy.textContent = copy;
    const cover = document.getElementById('study-loading-cover');
    if (cover) cover.style.display = '';
    document.body.classList.remove('study-ready');
    document.body.classList.add('is-route-loading');
  }

  function hideStudyLoader() {
    document.body.classList.add('study-ready');
    document.body.classList.remove('is-route-loading');
    setTimeout(() => {
      const cover = document.getElementById('study-loading-cover');
      if (cover) cover.style.display = 'none';
    }, 200);
  }

  function navigateAway(url, title, copy) {
    showStudyLoader(title, copy);
    requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        window.location.href = url;
      });
    });
  }

  async function flushStore(timeoutMs = 1200) {
    const flush = window.eruditeMobileFlashcards?.flush || window.flashcardStore?.flush;
    if (typeof flush !== 'function') return;
    await Promise.race([
      flush().catch(() => {}),
      new Promise(resolve => window.setTimeout(resolve, timeoutMs))
    ]);
  }

  async function flushStudyStateBeforeRoute() {
    try { await saveSessionLog(); } catch (_) {}
    try { await saveProgress({ immediate: true }); } catch (_) {}
    try { await saveOpenedMeta({ immediate: true }); } catch (_) {}
    try { await flushCardProgress(); } catch (_) {}
    try { await flushStore(1400); } catch (_) {}
  }

  function markRouteTrigger(trigger) {
    const button = trigger?.currentTarget || trigger;
    if (!button?.classList) return;
    button.classList.add('is-busy');
    button.setAttribute('aria-busy', 'true');
    if ('disabled' in button) button.disabled = true;
  }

  async function goLibrary(trigger = null) {
    markRouteTrigger(trigger);
    if (routeLeaving) return;
    routeLeaving = true;
    showStudyLoader('Opening Library', 'Refreshing your decks');
    await new Promise(resolve => setTimeout(resolve, 50));
    await flushStudyStateBeforeRoute();
    navigateAway(libraryUrl(), 'Opening Library', 'Refreshing your decks');
  }

  function getSetId() {
    const raw = params.get('setId');
    if (raw === null) return null;
    const numeric = Number(raw);
    return Number.isFinite(numeric) && raw.trim() !== '' ? numeric : raw;
  }

  function escapeHtml(value) {
    return String(value ?? '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  function escapeAttr(value) {
    return escapeHtml(value).replace(/`/g, '&#096;');
  }

  function sanitizeRichText(value) {
    const raw = String(value || '').trim();
    if (!raw) return '';
    const template = document.createElement('template');
    template.innerHTML = raw;
    const allowed = new Set(['B', 'STRONG', 'I', 'EM', 'U', 'BR', 'P', 'DIV', 'UL', 'OL', 'LI', 'SPAN']);
    const walk = document.createTreeWalker(template.content, NodeFilter.SHOW_ELEMENT);
    const nodes = [];
    while (walk.nextNode()) nodes.push(walk.currentNode);
    nodes.forEach(node => {
      if (!allowed.has(node.tagName)) {
        node.replaceWith(document.createTextNode(node.textContent || ''));
        return;
      }
      Array.from(node.attributes).forEach(attr => node.removeAttribute(attr.name));
    });
    return template.innerHTML || escapeHtml(raw).replace(/\n/g, '<br>');
  }

  function sameCard(a, b) {
    if (!a || !b) return false;
    if (a.id && b.id) return String(a.id) === String(b.id);
    return a.term === b.term && a.definition === b.definition;
  }

  function cardKey(card) {
    if (!card) return null;
    return card.id ? `id:${card.id}` : `text:${card.term || ''}::${card.definition || ''}`;
  }

  function getDeckSrsSettings(set = state.set) {
    const raw = set?.srsSettings || {};
    const numberOrNull = value => {
      if (value === null || value === undefined || value === '') return null;
      const number = Number(value);
      return Number.isFinite(number) ? number : null;
    };
    const requestRetention = numberOrNull(raw.requestRetention) ?? 0.9;
    const maxIntervalDays = numberOrNull(raw.maxIntervalDays) ?? 36500;
    const newCardsPerDay = numberOrNull(raw.newCardsPerDay);
    const reviewsPerDay = numberOrNull(raw.reviewsPerDay);
    return {
      enabled: raw.enabled !== false,
      requestRetention: Math.min(0.99, Math.max(0.7, requestRetention)),
      maxIntervalDays: Math.max(1, Math.round(maxIntervalDays)),
      newCardsPerDay: newCardsPerDay === null ? null : Math.max(0, Math.round(newCardsPerDay)),
      reviewsPerDay: reviewsPerDay === null ? null : Math.max(0, Math.round(reviewsPerDay))
    };
  }

  function activeIndex() {
    return state.srsMode ? state.srsIndex : state.normalIndex;
  }

  function shuffledIndices(length) {
    const indices = Array.from({ length }, (_, index) => index);
    for (let i = indices.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [indices[i], indices[j]] = [indices[j], indices[i]];
    }
    return indices;
  }

  function normalizeStudyOrder(value) {
    return ['forward', 'backward', 'random'].includes(value) ? value : 'forward';
  }

  function buildNormalOrder(length) {
    if (state.studyOrder === 'random') return shuffledIndices(length);
    const order = Array.from({ length }, (_, index) => index);
    return state.studyOrder === 'backward' ? order.reverse() : order;
  }

  function savedNormalIndex(progress, length) {
    if (state.studyOrder === 'random') return 0;
    const normalProgress = progress?.normalProgress || {};
    const legacyIndex = progress?.cardIndex ?? 0;
    
    // Decouple progress: if progress holds SRS keys, ignore cardIndex as fallback
    const hasSrsProgress = progress?.srsModeLength !== undefined || progress?.srsModeIndex !== undefined || progress?.srsCurrentCardKey !== undefined;
    const fallbackIndex = hasSrsProgress ? 0 : legacyIndex;
    
    const value = state.studyOrder === 'backward'
      ? (normalProgress.backward ?? progress?.normalBackwardIndex ?? 0)
      : (normalProgress.forward ?? progress?.normalForwardIndex ?? progress?.normalModeIndex ?? fallbackIndex);
    return Math.min(Math.max(0, Number(value) || 0), Math.max(0, length - 1));
  }

  function readStoredBoolean(value, fallback = false) {
    if (value === true || value === 'true') return true;
    if (value === false || value === 'false') return false;
    return Boolean(fallback);
  }

  function resolveSrsMode(storedValue) {
    if (reviewDueSession) return true;
    if (requestedSrsMode === 'true') return true;
    if (requestedSrsMode === 'false') return false;
    const mirrored = localStorage.getItem('srsModeEnabled');
    if (mirrored !== null) return mirrored === 'true';
    return readStoredBoolean(storedValue, false);
  }

  function setActiveIndex(value) {
    const max = Math.max(0, state.activeCards.length - 1);
    const next = Math.min(max, Math.max(0, Number(value) || 0));
    if (state.srsMode) state.srsIndex = next;
    else state.normalIndex = next;
  }

  function activeCard() {
    return state.activeCards[activeIndex()] || null;
  }

  function getCardElements(cardEl) {
    if (!cardEl) return null;
    return {
      termText: cardEl.querySelector('.term-text'),
      definitionText: cardEl.querySelector('.definition-text'),
      termImage: cardEl.querySelector('.term-image'),
      definitionImage: cardEl.querySelector('.definition-image'),
      termImageWrap: cardEl.querySelector('.term-image-wrap'),
      definitionImageWrap: cardEl.querySelector('.definition-image-wrap'),
      termMediaList: cardEl.querySelector('.term-media-list'),
      definitionMediaList: cardEl.querySelector('.definition-media-list'),
      termBg: cardEl.querySelector('.term-bg'),
      definitionBg: cardEl.querySelector('.definition-bg'),
      cardInner: cardEl.querySelector('.study-card-inner')
    };
  }

  function setCardFlipped(cardEl, flipped, options = {}) {
    if (!cardEl) return;
    if (options.noTransition) cardEl.classList.add('no-transition');
    const shouldAnimateFlip = !options.noTransition && cardEl === cards[activeCardIndex];
    if (shouldAnimateFlip) {
      clearTimeout(flipTimer);
      els.stage?.classList.add('card-is-flipping');
      flipTimer = window.setTimeout(() => {
        els.stage?.classList.remove('card-is-flipping');
      }, FLIP_DURATION + 70);
    }
    cardEl.classList.toggle('is-flipped', flipped);
    requestAnimationFrame(() => {
      updateCardScrollability(cardEl);
    });
    if (cardEl === cards[activeCardIndex]) {
      state.flipped = Boolean(flipped);
      clearTimeout(ratingTimer);
      if (!options.noTransition && state.srsMode && flipped) {
        els.hint.textContent = 'Revealing answer...';
        ratingTimer = window.setTimeout(updateRatingVisibility, FLIP_DURATION);
      } else {
        updateRatingVisibility();
      }
    }
    if (options.noTransition) {
      requestAnimationFrame(() => {
        requestAnimationFrame(() => {
          cardEl.classList.remove('no-transition');
        });
      });
    }
  }

  function setFlipped(flipped, options = {}) {
    setCardFlipped(cards[activeCardIndex], flipped, options);
  }

  function queueNavigation(vector = { x: -1, y: 0 }) {
    if (state.srsMode || state.complete) return;
    queuedNavigation = vector;
  }

  function runQueuedNavigation() {
    if (!queuedNavigation || animating || state.srsMode || state.complete) return;
    const vector = queuedNavigation;
    queuedNavigation = null;
    requestAnimationFrame(() => navigateForward(vector));
  }

  function isScrollableContent(target) {
    const scroll = target.closest?.('.card-scroll');
    return scroll && scroll.scrollHeight > scroll.clientHeight + 4 ? scroll : null;
  }

  function isInteractive(target) {
    return Boolean(target.closest?.('button, a, input, textarea, select, audio, video, [contenteditable="true"], .modal:not(.hidden), .image-modal:not(.hidden)'));
  }

  function configureSystemBars() {
    const SystemBars = window.Capacitor?.Plugins?.SystemBars;
    if (!SystemBars) return;
    const isLight = state.settings?.theme === 'light';
    SystemBars.setStyle?.({ style: isLight ? 'LIGHT' : 'DARK' }).catch(() => {});
    SystemBars.show?.().catch(() => {});
  }

  async function waitForStore() {
    const promises = [
      window.eruditeMobileReady,
      window.flashcardLocalReady
    ].filter(Boolean);
    await Promise.all(promises);
    if (!window.flashcardStore) throw new Error('Flashcard store unavailable');
  }

  async function loadData() {
    await waitForStore();
    const setId = getSetId();
    if (setId === null || setId === undefined) {
      throw new Error('No set selected');
    }

    const [found, srsMode, settings] = await Promise.all([
      window.flashcardStore.getSet(setId),
      window.flashcardStore.getState('srsModeEnabled'),
      window.flashcardStore.getSettings?.()
    ]);
    if (!found) throw new Error('Flashcard set not found');

    state.srsMode = resolveSrsMode(srsMode);
    state.studyOrder = normalizeStudyOrder(settings?.normalStudyOrder);
    state.settings = settings || {};
    const theme = state.settings?.theme || 'dark';
    localStorage.setItem('erudite-theme', theme);
    document.body.classList.toggle('theme-light', theme === 'light');
    document.documentElement.classList.toggle('theme-light', theme === 'light');
    if (reviewDueSession) {
      localStorage.setItem('srsModeEnabled', 'true');
      window.flashcardStore.setState('srsModeEnabled', true).catch(() => {});
    }
    state.set = schema?.normalizeSet ? schema.normalizeSet({
      ...found,
      openedCount: (found.openedCount || 0) + 1,
      lastOpened: Date.now()
    }, found) : {
      ...found,
      openedCount: (found.openedCount || 0) + 1,
      lastOpened: Date.now()
    };

    await loadProgress();
    prepareActiveCards();
    state.sessionStartedAt = Date.now();
    state.sessionCardsViewed = new Set();
  }

  function scheduleOpenedSave() {
    if (!state.set) return;
    clearTimeout(openedSaveTimer);
    openedSaveTimer = window.setTimeout(() => {
      saveOpenedMeta().catch(error => console.warn('[mobile-study] opened metadata save failed:', error));
    }, 210);
  }

  async function saveOpenedMeta(options = {}) {
    if (!state.set) return false;
    clearTimeout(openedSaveTimer);
    const { id, openedCount, lastOpened } = state.set;
    await window.flashcardStore.saveSet({
      id,
      openedCount,
      lastOpened,
      __metaOnly: true
    });
    if (options.immediate) await flushStore(options.flushTimeout || 900);
    return true;
  }

  async function saveSessionLog() {
    if (!state.set || !state.sessionStartedAt) return;
    const durationMs = Date.now() - state.sessionStartedAt;
    if (durationMs < 5000) return;
    const sessionPayload = {
      id: studySessionId,
      setId: state.set.id,
      startedAt: state.sessionStartedAt,
      durationMs: durationMs,
      cardsViewed: state.sessionCardsViewed?.size || 0,
      mode: state.srsMode ? 'srs' : 'normal'
    };
    try {
      await window.flashcardStore.saveStudySession(sessionPayload);
    } catch (err) {
      console.warn('[mobile-study] Could not save study session:', err);
    }
  }

  async function loadProgress() {
    const saved = await window.flashcardStore.getProgress(state.set.id);
    const mirrored = readProgressMirror();
    const progress = mirrored && (!saved || Number(mirrored.timestamp || 0) >= Number(saved.timestamp || 0))
      ? mirrored
      : saved;
    if (!progress || String(progress.setId) !== String(state.set.id)) {
      srsReviewedCardIds = new Set();
      return;
    }
    restoredProgress = progress;
    const cardCount = state.set.cards?.length || 0;
    state.normalIndex = savedNormalIndex(progress, cardCount || 1);
    state.srsIndex = Math.max(0, Number(progress.srsModeIndex ?? 0) || 0);
    if (progress.srsReviewedCardIds && Array.isArray(progress.srsReviewedCardIds)) {
      srsReviewedCardIds = new Set(progress.srsReviewedCardIds);
    } else {
      srsReviewedCardIds = new Set();
    }
  }

  function progressMirrorKey() {
    return state.set ? `${PROGRESS_MIRROR_PREFIX}${state.set.id}` : '';
  }

  function buildProgressPayload() {
    if (!state.set) return null;
    const normalProgress = {
      ...(restoredProgress?.normalProgress || {})
    };
    if (!state.srsMode && state.studyOrder !== 'random') {
      normalProgress[state.studyOrder] = state.normalIndex;
    }
    return {
      setId: state.set.id,
      cardIndex: activeIndex(),
      normalModeIndex: normalProgress.forward ?? state.normalIndex,
      normalForwardIndex: normalProgress.forward ?? 0,
      normalBackwardIndex: normalProgress.backward ?? 0,
      normalProgress,
      normalStudyOrder: state.studyOrder,
      normalModeLength: state.set?.cards?.length || state.activeCards.length || 0,
      normalOrder: state.normalOrder,
      srsModeIndex: state.srsIndex,
      srsModeLength: state.activeCards.length,
      srsCurrentCardKey: state.srsMode ? cardKey(activeCard()) : null,
      srsReviewedCardIds: Array.from(srsReviewedCardIds),
      timestamp: Date.now()
    };
  }

  function readProgressMirror() {
    try {
      const key = progressMirrorKey();
      return key ? JSON.parse(localStorage.getItem(key) || 'null') : null;
    } catch (_) {
      return null;
    }
  }

  function writeProgressMirror(payload) {
    try {
      const key = progressMirrorKey();
      if (key && payload) localStorage.setItem(key, JSON.stringify(payload));
    } catch (_) {}
  }

  function saveProgress(options = {}) {
    if (!state.srsMode && state.studyOrder === 'random') return Promise.resolve(false);
    const payload = buildProgressPayload();
    if (!payload) return Promise.resolve(false);
    restoredProgress = payload;
    writeProgressMirror(payload);
    clearTimeout(progressSaveTimer);
    if (options.immediate) {
      return window.flashcardStore.saveProgress(state.set.id, payload)
        .then(() => true)
        .catch(() => false);
    }
    const delay = options.immediate ? 0 : 900;
    progressSaveTimer = window.setTimeout(() => {
      window.flashcardStore.saveProgress(state.set.id, payload).catch(() => {});
    }, delay);
    return Promise.resolve(true);
  }

  function queueStudyCardPatch(card) {
    if (!state.set || !card?.id) return;
    let payload = null;
    try {
      payload = JSON.parse(localStorage.getItem(STUDY_PATCHES_KEY) || 'null');
    } catch (_) {
      payload = null;
    }
    const next = payload && payload.sets ? payload : { version: 1, updatedAt: Date.now(), sets: {} };
    const setId = String(state.set.id);
    const cardId = String(card.id);
    next.updatedAt = Date.now();
    next.sets[setId] = next.sets[setId] || { cards: {} };
    next.sets[setId].cards[cardId] = {
      srs: card.srs || null,
      reviewHistory: Array.isArray(card.reviewHistory) ? card.reviewHistory : [],
      suspended: Boolean(card.suspended),
      buriedUntil: card.buriedUntil || null,
      lastModified: Date.now()
    };
    try { localStorage.setItem(STUDY_PATCHES_KEY, JSON.stringify(next)); } catch (_) {}
  }

  function scheduleCardProgressSave(card, delay = 420) {
    if (!state.set || !card?.id) return;
    queueStudyCardPatch(card);
    pendingCardPatches.set(String(card.id), {
      srs: card.srs || null,
      reviewHistory: Array.isArray(card.reviewHistory) ? card.reviewHistory : [],
      suspended: Boolean(card.suspended),
      buriedUntil: card.buriedUntil || null,
      lastModified: Date.now()
    });
    clearTimeout(cardProgressSaveTimer);
    cardProgressSaveTimer = window.setTimeout(() => {
      const saveCard = window.flashcardStore.saveCardProgress || window.eruditeMobileFlashcards?.saveCardProgress;
      if (typeof saveCard === 'function') {
        const patch = pendingCardPatches.get(String(card.id));
        pendingCardPatches.delete(String(card.id));
        if (patch) saveCard(state.set.id, card.id, patch).catch(() => {});
      }
    }, delay);
  }

  async function flushCardProgress() {
    if (!state.set || !pendingCardPatches.size) return;
    clearTimeout(cardProgressSaveTimer);
    const saveCard = window.flashcardStore.saveCardProgress || window.eruditeMobileFlashcards?.saveCardProgress;
    if (typeof saveCard !== 'function') {
      await window.flashcardStore.saveSet(state.set);
      pendingCardPatches.clear();
      return;
    }
    const entries = Array.from(pendingCardPatches.entries());
    pendingCardPatches.clear();
    await Promise.all(entries.map(([cardId, patch]) => saveCard(state.set.id, cardId, patch).catch(() => {})));
  }

  function sortSrsSessionQueue(queue, now = new Date()) {
    const dueNow = [];
    const dueFuture = [];

    queue.forEach(card => {
      const isDueNow = !card.srs || !card.srs.due || (window.srsManager && window.srsManager.isReady() ? window.srsManager.isDue(card.srs, now) : new Date(card.srs.due) <= now);
      if (isDueNow) {
        dueNow.push(card);
      } else {
        dueFuture.push(card);
      }
    });

    // Sort dueNow by priority: Learning/Relearning first, then Review, then New
    dueNow.sort((a, b) => {
      const stateA = a.srs?.state || 'New';
      const stateB = b.srs?.state || 'New';

      const priority = (state) => {
        if (state === 'Learning' || state === 'Relearning') return 0;
        if (state === 'Review') return 1;
        return 2;
      };

      const pA = priority(stateA);
      const pB = priority(stateB);
      if (pA !== pB) return pA - pB;

      // If same priority, sort by due date ascending
      const dueA = new Date(a.srs?.due || 0).getTime();
      const dueB = new Date(b.srs?.due || 0).getTime();
      return dueA - dueB;
    });

    // Sort dueFuture by due date ascending (the one that will be due first comes first)
    dueFuture.sort((a, b) => {
      const dueA = new Date(a.srs?.due || 0).getTime();
      const dueB = new Date(b.srs?.due || 0).getTime();
      return dueA - dueB;
    });

    return [...dueNow, ...dueFuture];
  }

  function showLearningCardsDueSoonMessage(dueCount, nextDueTime) {
    const existingMessage = document.getElementById('mastered-message');
    if (existingMessage) {
      existingMessage.remove();
    }
    if (dueSoonTimer) {
      clearInterval(dueSoonTimer);
      dueSoonTimer = null;
    }

    const messageContainer = document.createElement('div');
    messageContainer.id = 'mastered-message';
    messageContainer.className = 'mastered-message-container';
    
    const updateText = () => {
      const diffSec = Math.max(0, Math.ceil((nextDueTime - Date.now()) / 1000));
      const min = Math.floor(diffSec / 60);
      const sec = diffSec % 60;
      const timeStr = min > 0 ? `${min}m ${sec}s` : `${sec}s`;
      
      const content = messageContainer.querySelector('.mastered-message-content');
      if (content) {
        content.innerHTML = `
          <div class="mastered-icon">
            <i class="fas fa-hourglass-half fa-spin"></i>
          </div>
          <h2>Learning Cards Due Soon</h2>
          <p>You have ${dueCount} learning card${dueCount === 1 ? '' : 's'} that will be due in <strong>${timeStr}</strong>.</p>
          <div class="mastered-actions">
            <button id="due-soon-continue" class="primary-action">
              <i class="fas fa-play" style="margin-right: 0.5rem;"></i>
              Review Now (Bypass Wait)
            </button>
            <button id="due-soon-finish" class="secondary-action">
              <i class="fas fa-check-double" style="margin-right: 0.5rem;"></i>
              Finish Session
            </button>
          </div>
        `;
        
        // Re-bind listeners because we replaced innerHTML
        const contBtn = document.getElementById('due-soon-continue');
        if (contBtn) {
          contBtn.addEventListener('click', () => {
            if (dueSoonTimer) clearInterval(dueSoonTimer);
            messageContainer.remove();
            renderStack();
            updateProgress();
          });
        }
        
        const finBtn = document.getElementById('due-soon-finish');
        if (finBtn) {
          finBtn.addEventListener('click', () => {
            if (dueSoonTimer) clearInterval(dueSoonTimer);
            messageContainer.remove();
            showCompletion();
          });
        }
      }
    };

    messageContainer.innerHTML = `<div class="mastered-message-content"></div>`;
    document.body.appendChild(messageContainer);
    
    updateText();
    dueSoonTimer = setInterval(() => {
      const diffMs = nextDueTime - Date.now();
      if (diffMs <= 0) {
        clearInterval(dueSoonTimer);
        dueSoonTimer = null;
        messageContainer.remove();
        renderStack();
        updateProgress();
      } else {
        updateText();
      }
    }, 1000);
  }

  function prepareActiveCards() {
    const existingMessage = document.getElementById('mastered-message');
    if (existingMessage) {
      existingMessage.remove();
    }
    if (dueSoonTimer) {
      clearInterval(dueSoonTimer);
      dueSoonTimer = null;
    }

    if (!Array.isArray(state.set.cards)) state.set.cards = [];
    if (state.srsMode && window.srsManager?.isReady?.()) {
      const settings = getDeckSrsSettings();
      const allDueCards = window.srsManager.getDueCards(state.set.cards, {
        maxNewCards: settings.newCardsPerDay,
        maxDueCards: settings.reviewsPerDay,
        allowMultipleSessions: true,
        settings
      });

      // Filter out already reviewed cards in this session
      state.activeCards = allDueCards.filter(card => !srsReviewedCardIds.has(cardKey(card)));

      // Sort the session queue
      state.activeCards = sortSrsSessionQueue(state.activeCards);

      // Resume the saved SRS card when it is still due and in the active queue.
      // Move it to index 0 (front of queue) so it is shown first.
      const resumedKey = restoredProgress?.srsCurrentCardKey;
      if (resumedKey) {
        const keyedIndex = state.activeCards.findIndex(card => cardKey(card) === resumedKey);
        if (keyedIndex > 0) {
          const resumedCard = state.activeCards.splice(keyedIndex, 1)[0];
          state.activeCards.unshift(resumedCard);
        }
      }

      state.srsIndex = 0;
    } else {
      const cards = state.set.cards || [];
      state.normalOrder = buildNormalOrder(cards.length);
      state.activeCards = state.normalOrder.map(index => cards[index]).filter(Boolean);
      state.normalIndex = Math.min(state.normalIndex, Math.max(0, state.activeCards.length - 1));
    }
  }

  function ensureCardSanitized(card) {
    if (!card || card.__sanitizedReady) return card;
    Object.defineProperties(card, {
      sanitizedTerm: {
        value: sanitizeRichText(card.term),
        writable: true,
        configurable: true
      },
      sanitizedDefinition: {
        value: sanitizeRichText(card.definition),
        writable: true,
        configurable: true
      },
      __sanitizedReady: {
        value: true,
        writable: true,
        configurable: true
      }
    });
    return card;
  }

  function warmVisibleCards() {
    const currentIdx = activeIndex();
    [currentIdx - 1, currentIdx, currentIdx + 1, currentIdx + 2].forEach(index => {
      const card = state.activeCards[index];
      if (card) ensureCardSanitized(card);
    });
  }

  function renderImage(img, wrap, src) {
    if (!src) {
      wrap.classList.add('hidden');
      img.removeAttribute('src');
      return;
    }
    if (img.getAttribute('src') !== src) {
      img.decoding = 'async';
      img.src = src;
    }
    wrap.classList.remove('hidden');
  }

  function renderCardBackground(element, card, side) {
    const background = window.EruditeMedia?.getSideBackground?.(card, side) || null;
    const faceEl = element.closest('.card-face');
    const labelEl = faceEl?.querySelector('.card-label');
    if (!element) return;
    if (!background?.src) {
      element.classList.remove('visible', 'no-overlay');
      element.style.backgroundImage = '';
      if (labelEl) labelEl.style.display = '';
      return;
    }
    element.style.backgroundImage = `url("${background.src}")`;
    element.style.backgroundSize = background.fit || 'cover';
    // Use global cardBgOpacity setting if available, otherwise fall back to per-card opacity
    const globalOpacity = window.flashcardStore?.getSettingsSync?.()?.cardBgOpacity
      ?? state.settings?.cardBgOpacity;
    const opacity = Number.isFinite(parseFloat(globalOpacity))
      ? parseFloat(globalOpacity)
      : (background.opacity ?? 0.32);
    element.style.setProperty('--card-bg-opacity', String(opacity));
    element.classList.add('visible');
    if (opacity >= 1.0) {
      element.classList.add('no-overlay');
      if (labelEl) labelEl.style.display = 'none';
    } else {
      element.classList.remove('no-overlay');
      if (labelEl) labelEl.style.display = '';
    }
  }

  function renderMediaList(container, card, side) {
    if (!container) return;
    const items = (window.EruditeMedia?.getSideMedia?.(card, side, { includeLegacy: false }) || [])
      .filter(item => item && item.src);
    container.innerHTML = items.map(item => {
      const src = escapeAttr(item.src || '');
      const name = escapeAttr(item.name || item.kind || 'Media');
      if (item.kind === 'audio') {
        return `<div class="card-media-item"><audio src="${src}" controls preload="metadata" title="${name}"></audio></div>`;
      }
      if (item.kind === 'video') {
        return `<div class="card-media-item"><video src="${src}" controls preload="metadata" title="${name}"></video></div>`;
      }
      return `
        <div class="card-media-item">
          <img src="${src}" alt="${name}" loading="lazy">
          <button type="button" class="media-zoom-button" data-zoom-src="${src}" aria-label="View image larger">
            <i class="fas fa-magnifying-glass-plus"></i>
          </button>
        </div>
      `;
    }).join('');
  }

  function preloadNeighborImages() {
    [state.activeCards[activeIndex() + 1], state.activeCards[activeIndex() - 1]].filter(Boolean).forEach(card => {
      const mediaImages = ['term', 'definition']
        .flatMap(side => window.EruditeMedia?.getSideMedia?.(card, side, { includeLegacy: false }) || [])
        .filter(item => item.kind === 'image')
        .map(item => item.src);
      const backgrounds = ['term', 'definition']
        .map(side => window.EruditeMedia?.getSideBackground?.(card, side)?.src)
        .filter(Boolean);
      [card?.termImage, card?.definitionImage, ...mediaImages, ...backgrounds].filter(Boolean).forEach(src => {
        if (src.startsWith('data:')) return; // Skip base64 data URLs to save memory
        if (preloadedImages.has(src)) return;
        preloadedImages.add(src);
        const img = new Image();
        img.decoding = 'async';
        img.src = src;
        img.decode?.().catch(() => {});
      });
    });
  }

  function updateRatingIntervals() {
    if (!state.srsMode || !window.srsManager?.isReady?.()) return;
    const card = activeCard();
    if (!card) return;
    const previews = window.srsManager.getRatingPreviews(card, getDeckSrsSettings());
    Object.entries(intervals).forEach(([rating, element]) => {
      if (element) element.textContent = previews[rating]?.intervalLabel || 'soon';
    });
  }

  function updateRatingVisibility() {
    const visible = state.srsMode && state.flipped && !state.complete && Boolean(activeCard());
    els.ratingDock.classList.toggle('hidden', !visible);
    els.shell.classList.toggle('srs-back-visible', visible);
    els.shell.classList.toggle('srs-mode-active', state.srsMode && !state.complete);
    if (visible) updateRatingIntervals();
    els.hint.textContent = state.srsMode
      ? (state.flipped ? 'Choose how well you remembered it.' : 'Tap to reveal the answer.')
      : 'Tap to flip. Swipe left or right to go next.';
  }

  function updateCardScrollability(cardEl) {
    if (!cardEl) return;
    cardEl.querySelectorAll('.card-scroll').forEach(scroll => {
      const isScrollable = scroll.scrollHeight > scroll.clientHeight + 4;
      scroll.style.touchAction = isScrollable ? 'pan-y' : 'none';
    });
  }

  function populateCardElement(cardEl, cardData) {
    if (!cardEl) return;
    if (!cardData) {
      cardEl.classList.add('empty-card');
      return;
    }
    ensureCardSanitized(cardData);
    cardEl.classList.remove('empty-card');
    const elements = getCardElements(cardEl);
    if (!elements) return;

    elements.termText.innerHTML = cardData.sanitizedTerm;
    elements.definitionText.innerHTML = cardData.sanitizedDefinition;
    window.EruditeMath?.renderMath?.(elements.termText);
    window.EruditeMath?.renderMath?.(elements.definitionText);
    renderImage(elements.termImage, elements.termImageWrap, cardData.termImage);
    renderImage(elements.definitionImage, elements.definitionImageWrap, cardData.definitionImage);
    renderCardBackground(elements.termBg, cardData, 'term');
    renderCardBackground(elements.definitionBg, cardData, 'definition');
    renderMediaList(elements.termMediaList, cardData, 'term');
    renderMediaList(elements.definitionMediaList, cardData, 'definition');
    
    cardEl.querySelectorAll('.card-scroll').forEach(scroll => {
      scroll.scrollTop = 0;
    });

    setCardFlipped(cardEl, false, { noTransition: true });

    requestAnimationFrame(() => {
      updateCardScrollability(cardEl);
    });
  }

  function clearCardRuntimeStyles(card) {
    if (!card) return;
    card.classList.remove('dragging');
    card.style.transform = '';
    card.style.opacity = '';
    card.style.zIndex = '';
  }

  function updateRoles() {
    cards.forEach((card, idx) => {
      if (!card) return;
      card.classList.remove('slot-active', 'slot-next', 'slot-prev', 'dragging');
      clearCardRuntimeStyles(card);
      
      const elements = getCardElements(card);
      if (elements && elements.termImage) {
        elements.termImage.style.transform = '';
      }
      
      if (idx === activeCardIndex) {
        card.classList.add('slot-active');
        els.card = card;
      } else if (idx === nextCardIndex) {
        card.classList.add('slot-next');
      } else if (idx === prevCardIndex) {
        card.classList.add('slot-prev');
      }
    });

    state.flipped = cards[activeCardIndex] ? cards[activeCardIndex].classList.contains('is-flipped') : false;
    updateRatingVisibility();
  }

  function renderStack() {
    const currentIdx = activeIndex();
    clearTimeout(flipTimer);
    els.stage?.classList.remove('card-is-flipping');
    warmVisibleCards();
    
    populateCardElement(cards[activeCardIndex], state.activeCards[currentIdx]);
    populateCardElement(cards[nextCardIndex], state.activeCards[currentIdx + 1]);
    populateCardElement(cards[prevCardIndex], state.activeCards[currentIdx - 1]);
    
    const activeCardData = state.activeCards[currentIdx];
    if (activeCardData && activeCardData.id && state.sessionCardsViewed) {
      state.sessionCardsViewed.add(String(activeCardData.id));
    }
    
    updateRoles();
    preloadNeighborImages();
    updateProgress();
  }

  function applyActiveDrag(x = 0, y = 0) {
    const activeEl = cards[activeCardIndex];
    const nextEl = cards[nextCardIndex];
    if (!activeEl) return;
    
    const rotate = Math.max(-7, Math.min(7, x * 0.032));
    activeEl.style.transform = `translate3d(${x}px, ${y}px, 0) rotate(${rotate}deg)`;
    
    if (nextEl && !nextEl.classList.contains('empty-card')) {
      const dist = Math.sqrt(x * x + y * y);
      const progress = Math.min(1, dist / 50);
      const nextScale = 0.96 + (0.04 * progress);
      const nextOffset = 10 - (10 * progress);
      nextEl.style.transform = `translate3d(0, ${nextOffset}px, 0) scale(${nextScale})`;
      nextEl.style.opacity = 0.9 + (0.1 * progress);
    }
  }

  function setDrag(x = 0, y = 0) {
    queuedDrag = { x, y };
    if (dragFrame) return;
    dragFrame = requestAnimationFrame(() => {
      dragFrame = 0;
      const next = queuedDrag || { x: 0, y: 0 };
      queuedDrag = null;
      applyActiveDrag(next.x, next.y);
    });
  }

  function updateProgress() {
    const total = state.activeCards.length;
    const index = total ? activeIndex() + 1 : 0;
    els.current.textContent = String(index);
    els.total.textContent = String(total);
    els.fill.style.width = total ? `${Math.round((index / total) * 100)}%` : '0%';
    els.modeLabel.textContent = state.srsMode ? 'SRS Review' : 'Study';
    els.title.textContent = state.set?.name || 'Study';
    if (els.prev) {
      els.prev.disabled = animating || activeIndex() <= 0 || state.srsMode;
    }

    const srsUndoBtn = document.getElementById('srs-undo-btn');
    const srsActionsBtn = document.getElementById('srs-actions-btn');
    if (srsUndoBtn && srsActionsBtn) {
      if (state.srsMode) {
        srsUndoBtn.classList.remove('hidden');
        srsActionsBtn.classList.remove('hidden');
        srsUndoBtn.disabled = srsUndoStack.length === 0;
      } else {
        srsUndoBtn.classList.add('hidden');
        srsActionsBtn.classList.add('hidden');
      }
    }
  }

  async function navigateForward(exitVector) {
    if (animating) {
      queueNavigation(exitVector || { x: -1, y: 0 });
      return;
    }
    if (!state.activeCards.length || state.complete) return;
    if (state.srsMode) {
      if (!state.flipped) {
        flipCard();
      } else {
        showToast('Rate this card to continue');
      }
      return;
    }

    const nextIndex = activeIndex() + 1;
    if (nextIndex >= state.activeCards.length) {
      await showCompletion();
      return;
    }
    
    animateOut(exitVector || { x: -1, y: 0 }, () => {
      setActiveIndex(nextIndex);
      
      prevCardIndex = activeCardIndex;
      activeCardIndex = nextCardIndex;
      nextCardIndex = (nextCardIndex + 1) % 3;
      
      const currentIdx = activeIndex();
      populateCardElement(cards[nextCardIndex], state.activeCards[currentIdx + 1]);
      
      updateRoles();
      preloadNeighborImages();
      updateProgress();
      saveProgress();
      runQueuedNavigation();
    });
  }

  function navigateBack() {
    if (animating) return;
    if (!state.activeCards.length || state.complete || state.srsMode) return;
    const prevIndex = activeIndex() - 1;
    if (prevIndex < 0) {
      showToast('First card');
      return;
    }
    
    animating = true;
    const token = ++transitionToken;
    playSound('next');
    if (els.prev) els.prev.disabled = true;
    if (dragFrame) cancelAnimationFrame(dragFrame);
    dragFrame = 0;
    queuedDrag = null;
    
    const activeEl = cards[activeCardIndex];
    const prevEl = cards[prevCardIndex];
    
    if (prevEl) {
      prevEl.classList.add('no-transition');
      prevEl.style.transform = 'translate3d(-100vw, 0, 0) rotate(-8deg)';
      prevEl.style.opacity = 0;
      prevEl.style.zIndex = 4;
      requestAnimationFrame(() => {
        if (token !== transitionToken) return;
        prevEl.classList.remove('no-transition');
        prevEl.style.transform = 'translate3d(0, 0, 0) scale(1)';
        prevEl.style.opacity = 1;
      });
    }
    
    if (activeEl) {
      activeEl.style.transform = 'translate3d(0, 10px, 0) scale(0.96)';
      activeEl.style.opacity = 0.9;
    }
    
    window.setTimeout(() => {
      if (token !== transitionToken) return;
      setActiveIndex(prevIndex);
      
      nextCardIndex = activeCardIndex;
      activeCardIndex = prevCardIndex;
      prevCardIndex = (prevCardIndex + 2) % 3;
      
      const currentIdx = activeIndex();
      populateCardElement(cards[prevCardIndex], state.activeCards[currentIdx - 1]);
      
      updateRoles();
      preloadNeighborImages();
      animating = false;
      updateProgress();
      saveProgress();
      runQueuedNavigation();
    }, SWIPE_DURATION);
  }

  function animateOut(vector, done) {
    const vx = (vector?.x || 0) < 0 ? -1 : 1;
    animating = true;
    const token = ++transitionToken;
    updateProgress();
    playSound('next');
    
    const activeEl = cards[activeCardIndex];
    const nextEl = cards[nextCardIndex];
    
    if (dragFrame) cancelAnimationFrame(dragFrame);
    dragFrame = 0;
    queuedDrag = null;
    
    if (activeEl) {
      activeEl.classList.remove('dragging');
      // If it's a vertical swipe, translate vertically, otherwise translate horizontally
      const tx = vector?.y ? 0 : (vx * 118);
      const ty = vector?.y ? (vector.y * 118) : 0;
      const rotate = vector?.y ? 0 : (vx * 8);
      activeEl.style.transform = `translate3d(${tx}vw, ${ty}vh, 0) rotate(${rotate}deg)`;
      activeEl.style.opacity = 0;
    }
    
    if (nextEl) {
      nextEl.classList.remove('no-transition');
      if (!nextEl.classList.contains('empty-card')) {
        nextEl.style.transform = 'translate3d(0, 0, 0) scale(1)';
        nextEl.style.opacity = 1;
      }
    }
    
    window.setTimeout(() => {
      if (token !== transitionToken) return;
      animating = false;
      done();
      runQueuedNavigation();
    }, SWIPE_DURATION);
  }

  function flipCard() {
    if (animating) return;
    const activeEl = cards[activeCardIndex];
    if (!activeCard() || state.complete) return;
    setCardFlipped(activeEl, !state.flipped);
    playSound('flip');
  }

  async function handleRating(rating, exitVector = { x: -1, y: 0 }) {
    if (ratingInFlight || animating || !state.srsMode || !state.flipped || state.complete || !window.srsManager?.isReady?.()) return;
    const current = activeCard();
    if (!current) return;
    ratingInFlight = true;

    const previous = current.srs ? { ...current.srs } : null;
    const reviewedAt = new Date().toISOString();
    
    // Save undo transaction snapshot
    pushUndoTransaction('review', current, { rating });

    const reviewed = window.srsManager.reviewCard(current, rating, getDeckSrsSettings());
    const updatedCard = {
      ...reviewed,
      reviewHistory: [
        ...(Array.isArray(current.reviewHistory) ? current.reviewHistory : []),
        {
          reviewedAt,
          rating,
          previousState: previous?.state || 'New',
          nextState: reviewed.srs?.state || null,
          previousDue: previous?.due || null,
          nextDue: reviewed.srs?.due || null
        }
      ]
    };

    const originalIndex = state.set.cards.findIndex(card => sameCard(card, current));
    if (originalIndex >= 0) state.set.cards[originalIndex] = updatedCard;

    // Cache the next card in the queue before modifying
    const oldNextCard = state.activeCards[1];

    // Remove the current card from the front of the queue
    state.activeCards.shift();

    const nextState = updatedCard.srs?.state || 'New';
    const nextDueTime = new Date(updatedCard.srs?.due || 0).getTime();
    const diffMs = nextDueTime - Date.now();

    const SHORT_TERM_LIMIT_MS = 20 * 60 * 1000; // 20 minutes
    const isShortTerm = (nextState === 'Learning' || nextState === 'Relearning') && diffMs < SHORT_TERM_LIMIT_MS;

    if (rating === 'Again' || isShortTerm) {
      // Keep in active session queue
      state.activeCards.push(updatedCard);
    } else {
      // Successfully reviewed (passed) and graduated: mark it completed in this session
      srsReviewedCardIds.add(cardKey(current));
    }

    // Sort queue
    state.activeCards = sortSrsSessionQueue(state.activeCards);
    state.srsIndex = 0;

    state.sessionStats.reviewed = srsReviewedCardIds.size;
    state.sessionStats[rating] += 1;
    state.sessionStats.nextDue = updatedCard.srs?.due || state.sessionStats.nextDue;

    saveProgress();
    scheduleCardProgressSave(updatedCard);

    // Check if session is complete
    if (state.activeCards.length === 0) {
      await showCompletion();
      ratingInFlight = false;
      return;
    }

    // Check if the next card is in the future
    const nextCardDue = state.activeCards[0].srs?.due ? new Date(state.activeCards[0].srs.due).getTime() : 0;
    const nextDiffMs = nextCardDue - Date.now();
    if (nextDiffMs > 0) {
      els.ratingDock.classList.add('hidden');
      showLearningCardsDueSoonMessage(state.activeCards.length, nextCardDue);
      ratingInFlight = false;
      return;
    }

    // Get the new active card
    const newActiveCard = state.activeCards[0];
    const isSameCard = newActiveCard && sameCard(newActiveCard, current);

    if (isSameCard) {
      // Flip back to the front
      const activeEl = cards[activeCardIndex];
      setCardFlipped(activeEl, false);
      window.setTimeout(() => {
        populateCardElement(activeEl, newActiveCard);
        updateRoles();
        preloadNeighborImages();
        updateProgress();
        saveProgress();
        ratingInFlight = false;
      }, FLIP_DURATION);
    } else {
      // If the new active card is different from the card that was in the next slot,
      // populate the next slot element with the new active card first so it transitions correctly.
      if (!oldNextCard || !sameCard(newActiveCard, oldNextCard)) {
        populateCardElement(cards[nextCardIndex], newActiveCard);
      }

      animateOut(exitVector, () => {
        prevCardIndex = activeCardIndex;
        activeCardIndex = nextCardIndex;
        nextCardIndex = (nextCardIndex + 1) % 3;
        
        const currentIdx = activeIndex(); // which is 0
        populateCardElement(cards[nextCardIndex], state.activeCards[currentIdx + 1]);
        
        updateRoles();
        preloadNeighborImages();
        updateProgress();
        saveProgress();
        animating = false;
        ratingInFlight = false;
      });
    }
  }

  async function findNextDueSetId() {
    if (!reviewDueSession || !state.srsMode || !window.srsManager?.isReady?.()) return null;
    // Lazy-load other sets only at completion — use lightweight meta + individual getSet as needed
    let allSets;
    try {
      allSets = await window.flashcardStore.listSets();
    } catch (_) { return null; }
    for (const set of allSets || []) {
      if (String(set.id) === String(state.set.id)) continue;
      if (set.srsSettings?.enabled === false) continue;
      const cards = (set.cards || []).map(card => card.srs ? card : window.srsManager.createSRSCard(card));
      const due = window.srsManager.getDueCards(cards, {
        maxNewCards: null,
        maxDueCards: null,
        allowMultipleSessions: true,
        settings: getDeckSrsSettings(set)
      });
      if (due.length > 0) return set.id;
    }
    return null;
  }

  async function showCompletion() {
    state.complete = true;
    state.nextDueSetId = await findNextDueSetId();
    els.ratingDock.classList.add('hidden');
    els.shell.classList.remove('srs-back-visible');
    playSound('success');

    if (state.srsMode) {
      els.completionTitle.textContent = state.nextDueSetId ? 'Set Complete' : 'SRS Complete';
      els.completionCopy.textContent = state.nextDueSetId
        ? 'More due cards are ready in another set.'
        : 'You are caught up for this session.';
      const nextDue = state.sessionStats.nextDue && window.srsManager?.formatIntervalLabel
        ? window.srsManager.formatIntervalLabel(state.sessionStats.nextDue)
        : 'Later';
      els.completionStats.innerHTML = `
        <span>${state.sessionStats.reviewed}<small>Reviewed</small></span>
        <span>${state.sessionStats.Again}/${state.sessionStats.Hard}/${state.sessionStats.Good}/${state.sessionStats.Easy}<small>A/H/G/E</small></span>
        <span>${nextDue}<small>Next Due</small></span>
      `;
      els.completionStats.classList.remove('hidden');
      els.continueButton.textContent = state.nextDueSetId ? 'Continue Review' : 'Check Again';
    } else {
      els.completionTitle.textContent = 'Set Complete';
      els.completionCopy.textContent = 'You reached the end of this deck.';
      els.completionStats.classList.add('hidden');
      els.continueButton.textContent = 'Practice Again';
    }

    els.completionModal.classList.remove('hidden');
  }

  function showEmptyDue() {
    els.emptyModal.classList.remove('hidden');
  }

  function installPointerGestures() {
    const SWIPE_THRESHOLD = 50;
    const VELOCITY_THRESHOLD = 0.42;
    const DEAD_ZONE = 10;

    // Create swipe glow overlay dynamically and append to body for full-screen edge glow
    let overlay = document.querySelector('.swipe-glow-overlay');
    if (!overlay) {
      overlay = document.createElement('div');
      overlay.className = 'swipe-glow-overlay';
      const directions = ['top', 'bottom', 'left', 'right'];
      directions.forEach(dir => {
        const d = document.createElement('div');
        d.className = `swipe-glow-${dir}`;
        d.style.display = 'none';
        overlay.appendChild(d);
      });
      document.body.appendChild(overlay);
    }

    const ratingButtons = {
      Again: document.querySelector('.rating-button.again'),
      Hard: document.querySelector('.rating-button.hard'),
      Good: document.querySelector('.rating-button.good'),
      Easy: document.querySelector('.rating-button.easy')
    };

    function updateSwipeFeedback(dx, dy) {
      if (!overlay) return;
      const absDx = Math.abs(dx);
      const absDy = Math.abs(dy);
      const dist = Math.sqrt(dx * dx + dy * dy);

      if (dist < 15) {
        overlay.style.opacity = '0';
        Object.values(ratingButtons).forEach(btn => btn?.classList.remove('active-drag'));
        return;
      }

      let activeDir = '';
      let activeRating = '';

      if (absDx >= absDy) {
        if (dx < 0) {
          activeDir = 'left';
          activeRating = 'Again';
        } else {
          activeDir = 'right';
          activeRating = 'Good';
        }
      } else {
        if (dy < 0) {
          activeDir = 'top';
          activeRating = 'Easy';
        } else {
          activeDir = 'bottom';
          activeRating = 'Hard';
        }
      }

      const glows = {
        top: overlay.querySelector('.swipe-glow-top'),
        bottom: overlay.querySelector('.swipe-glow-bottom'),
        left: overlay.querySelector('.swipe-glow-left'),
        right: overlay.querySelector('.swipe-glow-right')
      };

      Object.entries(glows).forEach(([dir, el]) => {
        if (el) el.style.display = dir === activeDir ? 'block' : 'none';
      });

      // Highlight the correct rating button
      Object.entries(ratingButtons).forEach(([rating, btn]) => {
        if (btn) {
          if (rating === activeRating) {
            btn.classList.add('active-drag');
          } else {
            btn.classList.remove('active-drag');
          }
        }
      });

      const opacity = Math.min(1, dist / 120);
      overlay.style.opacity = String(opacity);
    }

    function clearSwipeFeedback() {
      if (overlay) overlay.style.opacity = '0';
      Object.values(ratingButtons).forEach(btn => btn?.classList.remove('active-drag'));
    }

    els.stage.addEventListener('pointerdown', event => {
      if (animating) {
        // Do not queue navigation if click is on or near the previous button
        const prevEl = els.prev;
        if (prevEl) {
          const rect = prevEl.getBoundingClientRect();
          const margin = 15;
          const inPrev = (
            event.clientX >= rect.left - margin &&
            event.clientX <= rect.right + margin &&
            event.clientY >= rect.top - margin &&
            event.clientY <= rect.bottom + margin
          );
          if (inPrev) return;
        }
        if (!isInteractive(event.target)) queueNavigation({ x: -1, y: 0 });
        return;
      }
      const activeCardEl = cards[activeCardIndex];
      if (!activeCardEl || !activeCardEl.contains(event.target)) return;
      if (isInteractive(event.target)) return;

      // Dynamically sync scrollability/touch-action at touch start
      updateCardScrollability(activeCardEl);
      
      pointer = {
        id: event.pointerId,
        x: event.clientX,
        y: event.clientY,
        time: performance.now(),
        dragging: false,
        scrolling: false,
        scrollable: isScrollableContent(event.target),
        srsLocked: state.srsMode
      };
    });

    els.stage.addEventListener('pointermove', event => {
      if (!pointer || pointer.id !== event.pointerId) return;
      const activeCardEl = cards[activeCardIndex];
      if (!activeCardEl) return;
      
      const dx = event.clientX - pointer.x;
      const dy = event.clientY - pointer.y;
      const absDx = Math.abs(dx);
      const absDy = Math.abs(dy);

      if (pointer.scrolling) return;

      if (!pointer.dragging) {
        if (absDx > DEAD_ZONE || absDy > DEAD_ZONE) {
          // Primarily vertical swipe on scrollable content -> scroll instead of drag
          if (absDy > DEAD_ZONE && absDy > absDx * 1.18 && pointer.scrollable) {
            pointer.scrolling = true;
            activeCardEl.classList.remove('dragging');
            return;
          }

          // Drag is allowed if not SRS, or SRS when card is flipped
          const dragAllowed = !state.srsMode || state.flipped;
          if (dragAllowed) {
            pointer.dragging = true;
            els.stage.setPointerCapture?.(event.pointerId);
            activeCardEl.classList.add('dragging');
          }
        }
      }

      if (pointer.dragging) {
        event.preventDefault();
        setDrag(dx, dy);
        if (pointer.srsLocked && state.flipped) {
          updateSwipeFeedback(dx, dy);
        }
      }
    }, { passive: false });

    function finishPointer(event) {
      if (!pointer || pointer.id !== event.pointerId) return;
      clearSwipeFeedback();
      const activeCardEl = cards[activeCardIndex];
      const nextCardEl = cards[nextCardIndex];
      
      if (activeCardEl) {
        activeCardEl.classList.remove('dragging');
      }
      
      const dx = event.clientX - pointer.x;
      const dy = event.clientY - pointer.y;
      const dt = Math.max(1, performance.now() - pointer.time);
      const absDx = Math.abs(dx);
      const absDy = Math.abs(dy);
      
      const wasTap = absDx < 9 && absDy < 9 && !pointer.scrolling;
      
      const isSwipe = !pointer.scrolling && !wasTap && (
        absDx >= SWIPE_THRESHOLD ||
        absDy >= SWIPE_THRESHOLD ||
        (absDx / dt) >= VELOCITY_THRESHOLD ||
        (absDy / dt) >= VELOCITY_THRESHOLD
      );

      const wasSrsLocked = pointer.srsLocked;
      pointer = null;

      if (wasSrsLocked) {
        if (state.flipped) {
          if (wasTap) {
            flipCard();
          } else if (isSwipe) {
            if (absDx >= absDy) {
              if (dx < 0) {
                handleRating('Again', { x: -1, y: 0 });
              } else {
                handleRating('Good', { x: 1, y: 0 });
              }
            } else {
              if (dy < 0) {
                handleRating('Easy', { x: 0, y: -1 });
              } else {
                handleRating('Hard', { x: 0, y: 1 });
              }
            }
            return;
          }
        } else {
          // If unflipped, any tap or flick/swipe flips the card
          if (wasTap || absDx >= 25 || absDy >= 25) {
            flipCard();
          }
        }
        
        // Reset card transform on release
        if (activeCardEl) {
          activeCardEl.style.transform = '';
          activeCardEl.style.opacity = '';
        }
        if (nextCardEl) {
          nextCardEl.style.transform = '';
          nextCardEl.style.opacity = '';
        }
        return;
      }

      if (isSwipe) {
        if (absDx >= absDy) {
          navigateForward({ x: dx < 0 ? -1 : 1, y: 0 });
        } else {
          navigateForward({ x: 0, y: dy < 0 ? -1 : 1 });
        }
        return;
      }

      if (activeCardEl) {
        activeCardEl.style.transform = '';
        activeCardEl.style.opacity = '';
      }
      if (nextCardEl) {
        nextCardEl.style.transform = '';
        nextCardEl.style.opacity = '';
      }

      if (wasTap) {
        flipCard();
      }
    }

    els.stage.addEventListener('pointerup', finishPointer);
    els.stage.addEventListener('pointercancel', event => {
      if (!pointer || pointer.id !== event.pointerId) return;
      clearSwipeFeedback();
      const activeCardEl = cards[activeCardIndex];
      const nextCardEl = cards[nextCardIndex];
      pointer = null;
      if (activeCardEl) {
        activeCardEl.classList.remove('dragging');
        activeCardEl.style.transform = '';
        activeCardEl.style.opacity = '';
      }
      if (nextCardEl) {
        nextCardEl.style.transform = '';
        nextCardEl.style.opacity = '';
      }
    });
  }

  // Undo & Manual Card Actions for Mobile SRS Mode
  function pushUndoTransaction(actionType, card, extra = {}) {
    srsUndoStack.push({
      type: actionType,
      cardId: card.id,
      srsIndexSnapshot: state.srsIndex,
      sessionStatsSnapshot: { ...state.sessionStats },
      activeCardsSnapshot: JSON.parse(JSON.stringify(state.activeCards)),
      setCardsSnapshot: JSON.parse(JSON.stringify(state.set.cards)),
      reviewedCardIdsSnapshot: Array.from(srsReviewedCardIds),
      extra
    });
    if (srsUndoStack.length > 10) {
      srsUndoStack.shift();
    }
    updateUndoButtonState();
  }

  function updateUndoButtonState() {
    const srsUndoBtn = document.getElementById('srs-undo-btn');
    if (srsUndoBtn) {
      srsUndoBtn.disabled = srsUndoStack.length === 0;
    }
  }

  async function undoLastReview() {
    if (srsUndoStack.length === 0) return;
    const transaction = srsUndoStack.pop();

    state.activeCards = transaction.activeCardsSnapshot;
    state.set.cards = transaction.setCardsSnapshot;
    state.srsIndex = transaction.srsIndexSnapshot;
    state.sessionStats = transaction.sessionStatsSnapshot;
    srsReviewedCardIds = new Set(transaction.reviewedCardIdsSnapshot || []);
    state.complete = false;

    // Persist reverted card progress
    const currentIdx = activeIndex();
    const revertedCard = state.activeCards[currentIdx];
    if (revertedCard) {
      scheduleCardProgressSave(revertedCard);
    }
    await saveProgress();
    updateUndoButtonState();

    // Re-hide rating dock initially on card revert (until card is flipped again)
    state.flipped = false;
    els.ratingDock.classList.add('hidden');
    
    // Hide completion modal if it was shown
    els.completionModal.classList.add('hidden');

    // Clean up wait overlay if it was shown
    const existingMessage = document.getElementById('mastered-message');
    if (existingMessage) {
      existingMessage.remove();
    }
    if (dueSoonTimer) {
      clearInterval(dueSoonTimer);
      dueSoonTimer = null;
    }

    // Re-render carousel cards
    populateCardElement(cards[activeCardIndex], state.activeCards[currentIdx]);
    populateCardElement(cards[nextCardIndex], state.activeCards[currentIdx + 1]);
    populateCardElement(cards[prevCardIndex], state.activeCards[currentIdx - 1]);

    const activeEl = cards[activeCardIndex];
    if (activeEl) {
      activeEl.classList.remove('flipped');
      activeEl.style.transform = '';
      activeEl.style.opacity = '';
    }

    updateRoles();
    updateProgress();
    showToast('Review undone');
  }

  async function buryActiveCard() {
    const current = activeCard();
    if (!current) return;

    const now = new Date();
    const tomorrow = new Date(now.getFullYear(), now.getMonth(), now.getDate() + 1, 4, 0, 0, 0);

    pushUndoTransaction('bury', current);

    const updatedCard = {
      ...current,
      buriedUntil: tomorrow.toISOString()
    };

    const originalIndex = state.set.cards.findIndex(card => sameCard(card, current));
    if (originalIndex >= 0) state.set.cards[originalIndex] = updatedCard;

    // Remove from active reviews queue
    state.activeCards.splice(state.srsIndex, 1);
    
    // Persist
    scheduleCardProgressSave(updatedCard);
    await saveProgress();

    showToast('Card buried until tomorrow');
    handlePostActionTransition();
  }

  async function suspendActiveCard() {
    const current = activeCard();
    if (!current) return;

    pushUndoTransaction('suspend', current);

    const updatedCard = {
      ...current,
      suspended: true
    };

    const originalIndex = state.set.cards.findIndex(card => sameCard(card, current));
    if (originalIndex >= 0) state.set.cards[originalIndex] = updatedCard;

    // Remove from active reviews queue
    state.activeCards.splice(state.srsIndex, 1);
    
    // Persist
    scheduleCardProgressSave(updatedCard);
    await saveProgress();

    showToast('Card suspended');
    handlePostActionTransition();
  }

  async function resetActiveCard() {
    const current = activeCard();
    if (!current) return;

    pushUndoTransaction('reset', current);

    const updatedCard = {
      ...current,
      srs: undefined,
      reviewHistory: []
    };

    const originalIndex = state.set.cards.findIndex(card => sameCard(card, current));
    if (originalIndex >= 0) state.set.cards[originalIndex] = updatedCard;

    // Remove from active reviews queue since it is no longer due
    state.activeCards.splice(state.srsIndex, 1);
    
    // Persist
    scheduleCardProgressSave(updatedCard);
    await saveProgress();

    showToast('SRS scheduling reset');
    handlePostActionTransition();
  }

  async function setDueDateActiveCard(dueDateStr) {
    const current = activeCard();
    if (!current) return;

    pushUndoTransaction('set_due', current);

    const updatedCard = {
      ...current,
      srs: current.srs ? {
        ...current.srs,
        due: new Date(dueDateStr).toISOString()
      } : {
        state: 'New',
        due: new Date(dueDateStr).toISOString(),
        interval: 0,
        stability: 0,
        difficulty: 0
      }
    };

    const originalIndex = state.set.cards.findIndex(card => sameCard(card, current));
    if (originalIndex >= 0) state.set.cards[originalIndex] = updatedCard;

    // Check if the due date is in the future
    const isDueNow = window.srsManager && window.srsManager.isReady() ? window.srsManager.isDue({ state: updatedCard.srs?.state, due: dueDateStr }, new Date()) : new Date(dueDateStr) <= new Date();
    const isDueLater = !isDueNow;
    if (isDueLater) {
      state.activeCards.splice(state.srsIndex, 1);
    } else {
      state.activeCards[state.srsIndex] = updatedCard;
    }
    
    // Persist
    scheduleCardProgressSave(updatedCard);
    await saveProgress();

    showToast('Card due date updated');
    handlePostActionTransition();
  }

  function handlePostActionTransition() {
    if (state.activeCards.length === 0) {
      showCompletion();
      return;
    }

    state.srsIndex = 0; // Reset index in dynamic queue mode
    
    // Check if the next card is in the future
    const nextCardDue = state.activeCards[0].srs?.due ? new Date(state.activeCards[0].srs.due).getTime() : 0;
    const nextDiffMs = nextCardDue - Date.now();
    if (state.srsMode && nextDiffMs > 0) {
      state.flipped = false;
      els.ratingDock.classList.add('hidden');
      showLearningCardsDueSoonMessage(state.activeCards.length, nextCardDue);
      return;
    }

    // Otherwise, reveal the next card
    state.flipped = false;
    els.ratingDock.classList.add('hidden');

    // Populate current and neighbor cards in the carousel
    const currentIdx = activeIndex();
    populateCardElement(cards[activeCardIndex], state.activeCards[currentIdx]);
    populateCardElement(cards[nextCardIndex], state.activeCards[currentIdx + 1]);
    populateCardElement(cards[prevCardIndex], state.activeCards[currentIdx - 1]);

    const activeEl = cards[activeCardIndex];
    if (activeEl) {
      activeEl.classList.remove('flipped');
      activeEl.style.transform = '';
      activeEl.style.opacity = '';
    }

    updateRoles();
    updateProgress();
  }

  // Bottom Sheet Panel handlers
  function showActionsSheet() {
    const sheet = document.getElementById('srs-actions-sheet');
    if (sheet) {
      sheet.classList.remove('hidden');
    }
  }

  function hideActionsSheet() {
    const sheet = document.getElementById('srs-actions-sheet');
    if (sheet) {
      sheet.classList.add('hidden');
    }
  }

  function showDateModal() {
    const modal = document.getElementById('srs-mobile-date-modal');
    const input = document.getElementById('srs-mobile-due-date-input');
    if (modal && input) {
      const now = new Date();
      const year = now.getFullYear();
      const month = String(now.getMonth() + 1).padStart(2, '0');
      const day = String(now.getDate()).padStart(2, '0');
      input.value = `${year}-${month}-${day}`;
      modal.classList.remove('hidden');
    }
  }

  function hideDateModal() {
    const modal = document.getElementById('srs-mobile-date-modal');
    if (modal) {
      modal.classList.add('hidden');
    }
  }

  function installEvents() {
    els.back.addEventListener('click', () => goLibrary(els.back));
    els.prev?.addEventListener('click', () => navigateBack());
    const handleModalLibraryRoute = event => {
      if (event.type === 'pointerdown' && event.button !== undefined && event.button !== 0) return;
      event.preventDefault();
      event.stopPropagation();
      goLibrary(event.currentTarget);
    };
    els.libraryButton.addEventListener('pointerdown', handleModalLibraryRoute, { passive: false });
    els.libraryButton.addEventListener('click', handleModalLibraryRoute);
    els.emptyLibraryButton.addEventListener('pointerdown', handleModalLibraryRoute, { passive: false });
    els.emptyLibraryButton.addEventListener('click', handleModalLibraryRoute);
    els.continueButton.addEventListener('click', async () => {
      if (state.srsMode && state.nextDueSetId) {
        if (routeLeaving) return;
        routeLeaving = true;
        els.continueButton.disabled = true;
        showStudyLoader('Opening Review', 'Loading the next due deck');
        await new Promise(resolve => setTimeout(resolve, 50));
        await flushStudyStateBeforeRoute();
        navigateAway(studyUrl(state.nextDueSetId, true), 'Opening Review', 'Loading the next due deck');
        return;
      }
      els.continueButton.disabled = true;
      try {
        els.completionModal.classList.add('hidden');
        state.complete = false;
        state.nextDueSetId = null;
        if (state.srsMode) {
          state.srsIndex = 0;
          srsUndoStack = [];
          updateUndoButtonState();
          prepareActiveCards();
          if (!state.activeCards.length) {
            showEmptyDue();
            return;
          }
        } else {
          state.normalIndex = 0;
          restoredProgress = null;
          prepareActiveCards();
        }
        renderStack();
        await saveProgress();
      } finally {
        els.continueButton.disabled = false;
      }
    });

    els.emptyCheckButton.addEventListener('click', async () => {
      els.emptyModal.classList.add('hidden');
      await loadData();
      if (!state.activeCards.length) showEmptyDue();
      else renderStack();
    });

    els.ratingDock.addEventListener('click', event => {
      const button = event.target.closest('[data-rating]');
      if (!button) return;
      handleRating(button.dataset.rating);
    });

    // SRS Undo & Actions listeners
    const srsUndoBtn = document.getElementById('srs-undo-btn');
    const srsActionsBtn = document.getElementById('srs-actions-btn');
    const srsActionsSheetBackdrop = document.getElementById('srs-actions-sheet-backdrop');
    const actionCancelBtn = document.getElementById('action-cancel');
    const actionBuryBtn = document.getElementById('action-bury');
    const actionSuspendBtn = document.getElementById('action-suspend');
    const actionResetBtn = document.getElementById('action-reset');
    const actionSetDueBtn = document.getElementById('action-set-due');
    const srsMobileDateCancelBtn = document.getElementById('srs-mobile-date-cancel');
    const srsMobileDateConfirmBtn = document.getElementById('srs-mobile-date-confirm');
    const srsMobileDueDateInput = document.getElementById('srs-mobile-due-date-input');

    if (srsUndoBtn) srsUndoBtn.addEventListener('click', () => undoLastReview());
    if (srsActionsBtn) srsActionsBtn.addEventListener('click', () => showActionsSheet());
    if (srsActionsSheetBackdrop) srsActionsSheetBackdrop.addEventListener('click', () => hideActionsSheet());
    if (actionCancelBtn) actionCancelBtn.addEventListener('click', () => hideActionsSheet());

    if (actionBuryBtn) {
      actionBuryBtn.addEventListener('click', () => {
        hideActionsSheet();
        buryActiveCard();
      });
    }
    if (actionSuspendBtn) {
      actionSuspendBtn.addEventListener('click', () => {
        hideActionsSheet();
        suspendActiveCard();
      });
    }
    if (actionResetBtn) {
      actionResetBtn.addEventListener('click', () => {
        hideActionsSheet();
        resetActiveCard();
      });
    }
    if (actionSetDueBtn) {
      actionSetDueBtn.addEventListener('click', () => {
        hideActionsSheet();
        showDateModal();
      });
    }

    if (srsMobileDateCancelBtn) srsMobileDateCancelBtn.addEventListener('click', () => hideDateModal());
    if (srsMobileDateConfirmBtn) {
      srsMobileDateConfirmBtn.addEventListener('click', () => {
        const dateVal = srsMobileDueDateInput?.value;
        if (dateVal) {
          hideDateModal();
          setDueDateActiveCard(dateVal);
        }
      });
    }

    document.addEventListener('click', event => {
      // Global haptic feedback for click operations in study mode
      const clickable = event.target.closest('button, [role="button"], .tab-button, .context-option-row, .rating-button, .bottom-sheet-item, .bottom-sheet-cancel, .secondary-action, .primary-action');
      if (clickable) {
        triggerHaptic();
      }

      // Close modal/bottom-sheet if clicking on the backdrop overlay
      if (event.target.classList.contains('modal')) {
        event.preventDefault();
        event.stopPropagation();
        const cancelBtn = event.target.querySelector('.secondary-action, .cancel');
        if (cancelBtn) {
          cancelBtn.click();
        } else {
          event.target.classList.add('hidden');
        }
        return;
      }

      if (event.target.id === 'srs-actions-sheet-backdrop') {
        event.preventDefault();
        event.stopPropagation();
        hideActionsSheet();
        return;
      }

      const mediaZoom = event.target.closest('[data-zoom-src]');
      if (mediaZoom) {
        event.preventDefault();
        event.stopPropagation();
        els.zoomedImage.src = mediaZoom.dataset.zoomSrc || '';
        if (els.zoomedImage.src) els.imageModal.classList.remove('hidden');
        return;
      }
      const zoom = event.target.closest('[data-image-side]');
      if (!zoom) return;
      const activeEl = cards[activeCardIndex];
      const elements = getCardElements(activeEl);
      if (!elements) return;
      const side = zoom.dataset.imageSide;
      const src = side === 'term' ? elements.termImage.src : elements.definitionImage.src;
      if (!src) return;
      els.zoomedImage.src = src;
      els.imageModal.classList.remove('hidden');
    });

    els.imageClose.addEventListener('click', () => els.imageModal.classList.add('hidden'));
    els.imageModal.addEventListener('click', event => {
      if (event.target === els.imageModal) els.imageModal.classList.add('hidden');
    });

    document.addEventListener('keydown', event => {
      if (event.repeat || isInteractive(event.target)) return;
      if (animating) {
        if (!state.srsMode && event.key === 'ArrowRight') {
          event.preventDefault();
          queueNavigation({ x: -1, y: 0 });
        }
        return;
      }
      if (event.key === 'Escape') {
        els.imageModal.classList.add('hidden');
        return;
      }
      if (event.key === ' ' || event.key === 'Enter') {
        event.preventDefault();
        if (state.srsMode && state.flipped) return;
        flipCard();
      } else if (event.key === 'ArrowLeft') {
        event.preventDefault();
        navigateBack();
      } else if (event.key === 'ArrowRight') {
        event.preventDefault();
        navigateForward({ x: -1, y: 0 });
      } else if (state.srsMode && state.flipped && ['1', '2', '3', '4'].includes(event.key)) {
        event.preventDefault();
        handleRating(['Again', 'Hard', 'Good', 'Easy'][Number(event.key) - 1]);
      }
    });

    document.addEventListener('visibilitychange', async () => {
      if (document.hidden) {
        try { await saveSessionLog(); } catch (_) {}
        try { await saveProgress({ immediate: true }); } catch (_) {}
        try { await saveOpenedMeta({ immediate: true }); } catch (_) {}
        try { await flushCardProgress(); } catch (_) {}
        try { await flushStore(1400); } catch (_) {}
      }
    });
  }

  async function init() {
    document.documentElement.classList.add('is-capacitor', 'is-mobile-shell', 'study-session-active');
    configureSystemBars();
    installEvents();
    installPointerGestures();

    // Capacitor hardware back button: go back to library
    if (window.Capacitor?.Plugins?.App) {
      window.Capacitor.Plugins.App.addListener('backButton', () => {
        // Close any open modals first
        const openModal = document.querySelector('.image-modal:not(.hidden), .mobile-modal-overlay:not(.hidden)');
        if (openModal) {
          openModal.classList.add('hidden');
          return;
        }
        goLibrary();
      });
    }
    
    // Defer CPU-intensive database load to allow transition/loader animation to initialize smoothly
    setTimeout(async () => {
      try {
        await loadData();
        updateProgress();
        if (!state.activeCards.length) {
          showEmptyDue();
        } else {
          renderStack();
        }
        scheduleOpenedSave();
      } catch (error) {
        console.error(error);
        showToast(error.message || 'Could not open study session');
        window.setTimeout(goLibrary, 900);
      } finally {
        requestAnimationFrame(() => {
          els.shell.classList.remove('is-loading');
          hideStudyLoader();
        });
      }
    }, 280);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init, { once: true });
  } else {
    init();
  }
})();
