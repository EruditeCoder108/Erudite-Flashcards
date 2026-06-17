(function () {
  const core = window.EruditeCore || {};
  const schema = core.schema;
  const statsCore = core.stats;
  const draftCore = core.draft;

  const CREATOR_DRAFT_KEY = 'mobileCreatorDraft';

  const state = {
    sets: [],
    classes: [],
    settings: {},
    progressBySet: new Map(),
    srsMode: false,
    studySessions: [],
    activeTab: 'today',
    libraryFilter: 'all',
    search: '',
    sort: 'recent',
    browserCards: [],
    browserLoaded: false,
    browserSearch: '',
    premadeClass: '10th',
    premadeSubject: 'Science',
    premadeSets: [],
    creator: {
      editingSetId: null,
      originalSet: null,
      classId: '',
      cards: [],
      draftLoaded: false
    },
    pendingImageTarget: null,
    busy: false,
    creatorSaving: false,
    selectMode: false,
    selectedDecks: new Set(),
    lastModalClosedAt: 0
  };

  let creatorDraftTimer = null;
  let formatStateFrame = 0;
  let orphanRepairTimer = null;

  const premadeClasses = [
    { id: '10th', name: 'Class 10' },
    { id: '11th', name: 'Class 11' },
    { id: '12th', name: 'Class 12' },
    { id: 'neet-ug', name: 'NEET UG' },
    { id: 'jee-main', name: 'JEE Main' },
    { id: 'jee-advanced', name: 'JEE Advanced' },
    { id: 'ssc', name: 'SSC' }
  ];

  const premadeSubjects = {
    '10th': ['Science', 'Maths', 'English', 'Civics', 'Geography', 'History', 'Hindi', 'Politics'],
    '11th': ['Physics', 'inorganic-chemistry', 'organic-chemistry', 'physical-chemistry', 'English', 'Maths', 'Biology', 'Physical-education'],
    '12th': ['Physics', 'inorganic-chemistry', 'organic-chemistry', 'physical-chemistry', 'English', 'Maths', 'Biology', 'Physical-education'],
    'neet-ug': ['physics', 'chemistry', 'biology'],
    'jee-main': ['physics', 'chemistry', 'maths'],
    'jee-advanced': ['physics', 'chemistry', 'maths'],
    'ssc': ['general-awareness', 'quantitative-aptitude', 'reasoning', 'english']
  };

  const sortOrder = ['recent', 'name', 'cards', 'due'];
  const sortLabels = {
    recent: 'Most recent',
    name: 'A to Z',
    cards: 'Cards',
    due: 'Due'
  };

  const classColorChoices = ['#3B82F6', '#8B5CF6', '#10B981', '#F59E0B', '#EF4444', '#06B6D4', '#EC4899', '#64748B'];
  const classIconChoices = ['fa-graduation-cap', 'fa-book', 'fa-calculator', 'fa-flask', 'fa-dna', 'fa-landmark', 'fa-globe', 'fa-palette', 'fa-music', 'fa-code', 'fa-quote-left'];

  const selectors = {
    title: document.getElementById('mobile-title'),
    eyebrow: document.getElementById('mobile-eyebrow'),
    views: Array.from(document.querySelectorAll('.mobile-view')),
    tabs: Array.from(document.querySelectorAll('.tab-button')),
    filters: document.getElementById('library-filters'),
    searchInput: document.getElementById('mobile-search-input'),
    sortLabel: document.getElementById('library-sort-label'),
    countLabel: document.getElementById('library-count-label'),
    todayHero: document.getElementById('today-hero'),
    continueList: document.getElementById('continue-list'),
    activityList: document.getElementById('activity-list'),
    libraryList: document.getElementById('library-list'),
    createForm: document.getElementById('mobile-create-form'),
    createTitle: document.getElementById('mobile-create-title'),
    createClassLabel: document.getElementById('mobile-create-class-label'),
    creatorCards: document.getElementById('mobile-creator-cards'),
    imageInput: document.getElementById('mobile-image-input'),
    backgroundInput: document.getElementById('mobile-background-input'),
    txtInput: document.getElementById('mobile-txt-input'),
    premadeClassFilters: document.getElementById('premade-class-filters'),
    premadeSubjectFilters: document.getElementById('premade-subject-filters'),
    premadeList: document.getElementById('premade-list'),
    browserSearchInput: document.getElementById('browser-search-input'),
    browserList: document.getElementById('browser-list'),
    srsSwitch: document.getElementById('srs-switch'),
    moreSrsLabel: document.getElementById('more-srs-label'),
    normalStudyOrder: null,
    bgOpacitySlider: document.getElementById('mobile-bg-opacity'),
    themeLabel: document.getElementById('more-theme-label'),
    importTermSepInput: document.getElementById('mobile-import-term-sep'),
    importCardSepInput: document.getElementById('mobile-import-card-sep'),
    loadingCover: document.getElementById('app-loading-cover'),
    loadingTitle: document.getElementById('app-loading-title'),
    loadingCopy: document.getElementById('app-loading-copy'),
    toast: document.getElementById('mobile-toast'),
    headerQuote: document.getElementById('mobile-header-quote'),
    // Custom modals
    formulaOverlay: document.getElementById('formula-modal-overlay'),
    formulaInput: document.getElementById('formula-modal-input'),
    formulaConfirm: document.getElementById('formula-modal-confirm'),
    formulaCancel: document.getElementById('formula-modal-cancel'),
    draftRestoreOverlay: document.getElementById('draft-restore-overlay'),
    draftRestoreContinue: document.getElementById('draft-restore-continue'),
    draftRestoreDiscard: document.getElementById('draft-restore-discard'),
    copyExportOverlay: document.getElementById('copy-export-overlay'),
    copyExportDeck: document.getElementById('copy-export-deck'),
    copyExportTermSep: document.getElementById('copy-export-term-sep'),
    copyExportCardSep: document.getElementById('copy-export-card-sep'),
    copyExportText: document.getElementById('copy-export-text'),
    copyExportGenerate: document.getElementById('copy-export-generate'),
    copyExportCopy: document.getElementById('copy-export-copy'),
    copyExportCancel: document.getElementById('copy-export-cancel'),
    pasteImportOverlay: document.getElementById('paste-import-overlay'),
    pasteImportName: document.getElementById('paste-import-name'),
    pasteImportClassTrigger: document.getElementById('mobile-paste-import-class-trigger'),
    pasteImportPreset: document.getElementById('paste-import-preset'),
    pasteImportSeparatorRow: document.getElementById('paste-import-separator-row'),
    pasteImportTermSep: document.getElementById('paste-import-term-sep'),
    pasteImportCardSep: document.getElementById('paste-import-card-sep'),
    pasteImportText: document.getElementById('paste-import-text'),
    pasteImportPresetTrigger: document.getElementById('mobile-paste-import-preset-trigger'),
    presetSelectModal: document.getElementById('preset-select-modal'),
    pasteImportConfirm: document.getElementById('paste-import-confirm'),
    pasteImportCancel: document.getElementById('paste-import-cancel')
  };

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

  function cssEscape(value) {
    if (window.CSS?.escape) return CSS.escape(String(value));
    return String(value).replace(/["\\]/g, '\\$&');
  }

  function clamp(number, min, max) {
    return Math.min(max, Math.max(min, number));
  }

  function readStoredBoolean(value, fallback = false) {
    if (value === true || value === 'true') return true;
    if (value === false || value === 'false') return false;
    return Boolean(fallback);
  }

  function readSrsMode(storedValue) {
    const mirrored = localStorage.getItem('srsModeEnabled');
    if (mirrored !== null) return mirrored === 'true';
    return readStoredBoolean(storedValue, false);
  }

  function persistSrsMode(enabled) {
    state.srsMode = Boolean(enabled);
    localStorage.setItem('srsModeEnabled', String(state.srsMode));
    window.flashcardStore?.setState?.('srsModeEnabled', state.srsMode)
      .then(() => flushStore(900))
      .catch(error => {
        console.error('SRS mode save failed:', error);
        showToast('Could not save SRS setting');
      });
  }

  function plural(count, singular, pluralText = `${singular}s`) {
    return `${count} ${count === 1 ? singular : pluralText}`;
  }

  function normalizeTimestamp(value) {
    if (!value) return 0;
    const number = Number(value);
    if (Number.isFinite(number) && number > 0) return number;
    const date = new Date(value);
    return Number.isNaN(date.getTime()) ? 0 : date.getTime();
  }

  function relativeTime(value) {
    const timestamp = normalizeTimestamp(value);
    if (!timestamp) return 'Not studied yet';
    const diff = Date.now() - timestamp;
    const minute = 60 * 1000;
    const hour = 60 * minute;
    const day = 24 * hour;
    if (diff < minute) return 'Just now';
    if (diff < hour) return `${Math.floor(diff / minute)}m ago`;
    if (diff < day) return `${Math.floor(diff / hour)}h ago`;
    if (diff < day * 2) return 'Yesterday';
    if (diff < day * 30) return `${Math.floor(diff / day)}d ago`;
    return new Date(timestamp).toLocaleDateString(undefined, { month: 'short', day: 'numeric' });
  }

  function validColor(color, fallback = '#3b82f6') {
    return /^#[0-9a-f]{6}$/i.test(String(color || '')) ? color : fallback;
  }

  function iconClass(icon, fallback = 'fa-layer-group') {
    const clean = String(icon || fallback).replace(/[^a-zA-Z0-9 -]/g, '').trim();
    if (!clean) return `fas ${fallback}`;
    if (clean.includes('fa-')) {
      return clean.startsWith('fa') && !clean.startsWith('fas') && !clean.startsWith('far')
        ? `fas ${clean}`
        : clean;
    }
    return `fas ${fallback}`;
  }

  function classMap() {
    return new Map(state.classes.map(item => [String(item.id), item]));
  }

  function getClassForSet(set) {
    if (!set?.classId) return null;
    return classMap().get(String(set.classId)) || null;
  }

  function normalizeSetClassReferences(sets, classes) {
    const classIds = new Set((classes || []).map(item => String(item.id)));
    return (sets || []).map(set => (
      set?.classId && !classIds.has(String(set.classId))
        ? { ...set, classId: null, __classOrphanRepaired: true }
        : set
    ));
  }

  function scheduleOrphanClassRepair() {
    clearTimeout(orphanRepairTimer);
    const orphaned = state.sets.filter(set => set.__classOrphanRepaired && set.id);
    if (!orphaned.length) return;
    orphanRepairTimer = window.setTimeout(async () => {
      try {
        for (const set of orphaned) {
          await window.flashcardStore.saveSet({ id: set.id, classId: null, __metaOnly: true });
        }
        await flushStore(900);
      } catch (error) {
        console.warn('[mobile] Could not repair orphaned class references:', error);
      }
    }, 700);
  }

  function metaStats(set) {
    return set?.mobileStats && typeof set.mobileStats === 'object' ? set.mobileStats : null;
  }

  function setCardCount(set) {
    return Number(set?.cardCount ?? metaStats(set)?.totalCards ?? (Array.isArray(set?.cards) ? set.cards.length : 0)) || 0;
  }

  function setStats(set) {
    const meta = metaStats(set);
    if (meta) {
      return {
        totalCards: setCardCount(set),
        dueCards: Number(meta.dueCards || 0),
        newCards: Number(meta.newCards || 0),
        learningCards: Number(meta.learningCards || 0),
        reviewCards: Number(meta.reviewCards || 0),
        relearningCards: Number(meta.relearningCards || 0),
        matureCards: Number(meta.matureCards || 0),
        retention: meta.retention ?? null,
        nextDue: meta.nextDue || null
      };
    }
    if (set.cards?.length && statsCore?.getSetSrsStats) return statsCore.getSetSrsStats(set);
    const totalCards = setCardCount(set);
    return { totalCards, dueCards: totalCards, newCards: totalCards, learningCards: 0, reviewCards: 0, matureCards: 0 };
  }

  function dueCountForSet(set, options = {}) {
    const force = Boolean(options.force);
    if (!force && !state.srsMode) return 0;
    if (set?.srsSettings?.enabled === false) return 0;
    const meta = metaStats(set);
    if (meta) return Number(meta.dueCards || 0);
    return dueCardsForSet(set, { force }).length;
  }

  function dueCardsForSet(set, options = {}) {
    const force = Boolean(options.force);
    if (!force && !state.srsMode) return [];
    if (set?.srsSettings?.enabled === false) return [];
    if (!set.cards?.length) return [];
    if (window.srsManager?.getDueCards) {
      return window.srsManager.getDueCards(set.cards || [], { settings: set.srsSettings || {} });
    }
    return (set.cards || []).filter(card => statsCore?.isDue ? statsCore.isDue(card.srs) : true);
  }

  function totalStats(options = {}) {
    const forceDue = options.forceDue !== false;
    const totals = {
      setCount: state.sets.length,
      classCount: state.classes.length,
      cardCount: 0,
      dueCards: 0,
      newCards: 0,
      learningCards: 0,
      reviewCards: 0,
      matureCards: 0,
      retention: null
    };
    const retentions = [];
    state.sets.forEach(set => {
      const stats = setStats(set);
      totals.cardCount += setCardCount(set);
      totals.dueCards += dueCountForSet(set, { force: forceDue });
      totals.newCards += Number(stats.newCards || 0);
      totals.learningCards += Number(stats.learningCards || 0);
      totals.reviewCards += Number(stats.reviewCards || 0);
      totals.matureCards += Number(stats.matureCards || 0);
      if (stats.retention !== null && stats.retention !== undefined) retentions.push(Number(stats.retention));
    });
    if (retentions.length) {
      totals.retention = Math.round(retentions.reduce((sum, value) => sum + value, 0) / retentions.length);
    }
    return totals;
  }

  function dueSets(options = {}) {
    const force = Boolean(options.force);
    if (!force && !state.srsMode) return [];
    return state.sets
      .map(set => ({ set, due: dueCountForSet(set, { force }) }))
      .filter(item => item.due > 0)
      .sort((a, b) => b.due - a.due || normalizeTimestamp(b.set.lastOpened || b.set.lastModified) - normalizeTimestamp(a.set.lastOpened || a.set.lastModified));
  }

  function reviewedDates() {
    const dates = [];
    state.sets.forEach(set => {
      const meta = metaStats(set);
      if (meta?.lastReviewAt) dates.push(Number(meta.lastReviewAt));
      (set.cards || []).forEach(card => {
        (card.reviewHistory || []).forEach(review => {
          const time = normalizeTimestamp(review.reviewedAt || review.time || review.date);
          if (time) dates.push(time);
        });
      });
    });
    return dates;
  }

  function reviewsToday() {
    const metaTotal = state.sets.reduce((total, set) => total + Number(metaStats(set)?.reviewedToday || 0), 0);
    if (metaTotal > 0 || state.sets.some(set => metaStats(set))) return metaTotal;
    const start = new Date();
    start.setHours(0, 0, 0, 0);
    return reviewedDates().filter(time => time >= start.getTime()).length;
  }

  function streakDays() {
    const dayKeys = new Set();
    state.sets.forEach(set => {
      (metaStats(set)?.reviewDayKeys || []).forEach(key => dayKeys.add(String(key)));
    });
    reviewedDates().forEach(time => {
      const date = new Date(time);
      date.setHours(0, 0, 0, 0);
      dayKeys.add(String(date.getTime()));
    });
    if (Array.isArray(state.studySessions)) {
      state.studySessions.forEach(session => {
        if (session.durationMs >= 60000) {
          const date = new Date(session.startedAt);
          date.setHours(0, 0, 0, 0);
          dayKeys.add(String(date.getTime()));
        }
      });
    }
    if (!dayKeys.size) {
      return 0;
    }
    let streak = 0;
    const cursor = new Date();
    cursor.setHours(0, 0, 0, 0);
    if (!dayKeys.has(String(cursor.getTime()))) {
      cursor.setDate(cursor.getDate() - 1);
    }
    while (dayKeys.has(String(cursor.getTime()))) {
      streak += 1;
      cursor.setDate(cursor.getDate() - 1);
    }
    return streak;
  }

  function progressPercent(set) {
    const cardCount = setCardCount(set);
    if (!cardCount) return 0;
    if (state.srsMode) {
      const due = dueCountForSet(set, { force: true });
      return clamp(Math.round(((cardCount - Math.min(due, cardCount)) / cardCount) * 100), 0, 100);
    }
    const savedProgress = state.progressBySet?.get(String(set.id));
    const savedIndex = Number(savedProgress?.normalModeIndex ?? savedProgress?.cardIndex);
    if (Number.isFinite(savedIndex) && savedIndex >= 0) {
      const progressLength = Math.max(cardCount, Number(savedProgress?.normalModeLength || 0) || 0);
      return clamp(Math.round(((Math.min(savedIndex, progressLength - 1) + 1) / Math.max(1, progressLength)) * 100), 0, 100);
    }
    const meta = metaStats(set);
    if (meta?.reviewCount) {
      return clamp(Math.round((Math.min(Number(meta.reviewCount || 0), cardCount) / cardCount) * 100), 0, 100);
    }
    if (set.cards?.length) {
      const srsReviewed = set.cards.filter(card => (card.srs?.reps || 0) > 0 || (card.reviewHistory || []).length > 0).length;
      if (srsReviewed > 0) {
        return clamp(Math.round((srsReviewed / cardCount) * 100), 0, 100);
      }
    }
    if ((set.openedCount || 0) > 0) {
      return clamp(Math.min(Math.round(((set.openedCount || 0) / Math.max(3, cardCount)) * 100), 95), 5, 95);
    }
    return 0;
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

  function playClick() {
    triggerHaptic();
    try {
      const audio = new Audio('assets/flashcard-assets/click.mp3');
      audio.volume = 0.85;
      audio.play().catch(() => {});
    } catch (_error) {}
  }

  function playStar() {
    try {
      const audio = new Audio('assets/audio/Star.mp3');
      audio.volume = 0.85;
      audio.play().catch(() => {});
    } catch (_error) {}
  }

  let toastTimer = null;
  function showToast(message) {
    if (!selectors.toast) return;
    clearTimeout(toastTimer);
    selectors.toast.textContent = message;
    selectors.toast.classList.add('show');
    toastTimer = setTimeout(() => selectors.toast.classList.remove('show'), 2200);
  }

  function normalizeNormalStudyOrder(value) {
    return ['forward', 'backward', 'random'].includes(value) ? value : 'forward';
  }

  async function configureSystemBars() {
    const SystemBars = window.Capacitor?.Plugins?.SystemBars;
    if (!SystemBars) return;
    const isLight = state.settings?.theme === 'light';
    await SystemBars.setStyle?.({ style: isLight ? 'LIGHT' : 'DARK' }).catch(() => {});
    await SystemBars.setAnimation?.({ animation: 'NONE' }).catch(() => {});
    await SystemBars.show?.().catch(() => {});
  }

  async function waitForStorage() {
    const promises = [
      window.eruditeMobileReady,
      window.flashcardLocalReady
    ].filter(Boolean);
    await Promise.all(promises);
    if (!window.flashcardStore) {
      throw new Error('Flashcard store is not available.');
    }
  }

  async function loadData() {
    await waitForStorage();
    const listSetsFast = window.flashcardStore.listSetsMeta || window.flashcardStore.listSets;
    const [sets, classes, settings, srsMode, studySessions] = await Promise.all([
      listSetsFast.call(window.flashcardStore),
      window.flashcardStore.listClasses(),
      window.flashcardStore.getSettings(),
      window.flashcardStore.getState('srsModeEnabled'),
      window.flashcardStore.getStudySessions ? window.flashcardStore.getStudySessions() : []
    ]);
    state.classes = (classes || []).map(item => schema?.normalizeClass ? schema.normalizeClass(item, null, { preserveLastModified: true }) : item);
    const normalizedSets = (sets || []).map(set => schema?.normalizeSet ? schema.normalizeSet(set, null, { preserveLastModified: true }) : set);
    state.sets = normalizeSetClassReferences(normalizedSets, state.classes);
    state.settings = settings || {};
    state.srsMode = readSrsMode(srsMode);
    state.studySessions = studySessions || [];
    const theme = state.settings?.theme || 'dark';
    localStorage.setItem('erudite-theme', theme);
    document.body.classList.toggle('theme-light', theme === 'light');
    document.documentElement.classList.toggle('theme-light', theme === 'light');
    configureSystemBars().catch(() => {});
    
    let allProgress = {};
    try {
      allProgress = await window.flashcardStore.getAllProgress();
    } catch (err) {
      console.warn('[mobile] Could not fetch all progress:', err);
    }
    const progressEntries = state.sets.map(set => {
      const stored = allProgress[String(set.id)];
      return [String(set.id), stored || null];
    });
    state.progressBySet = new Map(progressEntries.filter(([, progress]) => Boolean(progress)));
    scheduleOrphanClassRepair();
  }

  function setHeader() {
    const titles = {
      today: 'Today',
      library: 'Library',
      create: 'Create',
      premade: 'Premade',
      browser: 'Cards',
      more: 'Settings'
    };
    selectors.eyebrow.textContent = 'Erudite Flashcards';
    selectors.title.textContent = titles[state.activeTab] || 'Today';
  }

  function updateTabIndicator(tab) {
    const activeBtn = document.querySelector(`.tab-button[data-tab="${tab}"]`);
    const indicator = document.getElementById('mobile-tab-indicator');
    if (activeBtn && indicator) {
      // Small timeout to ensure browser has computed coordinates correctly
      requestAnimationFrame(() => {
        indicator.style.width = `${activeBtn.offsetWidth}px`;
        indicator.style.left = `${activeBtn.offsetLeft}px`;
      });
    }
  }

  function setActiveTab(tab) {
    state.activeTab = tab;
    try {
      window.history.replaceState(null, null, '#' + tab);
    } catch (e) {
      console.warn('[mobile] Could not update hash state:', e);
    }
    selectors.views.forEach(view => view.classList.toggle('active', view.id === `view-${tab}`));
    selectors.tabs.forEach(button => button.classList.toggle('active', button.dataset.tab === tab));
    
    // Toggle sticky header creator save button
    const headerSaveBtn = document.getElementById('header-creator-save-btn');
    if (headerSaveBtn) {
      headerSaveBtn.classList.toggle('hidden', tab !== 'create');
    }
    const headerImportBtn = document.getElementById('header-paste-import-btn');
    if (headerImportBtn) {
      headerImportBtn.classList.toggle('hidden', tab === 'create');
    }
    if (selectors.headerQuote) {
      selectors.headerQuote.classList.toggle('hidden', tab === 'create');
    }

    updateTabIndicator(tab);
    setHeader();
    if (tab === 'library') {
      const btnPremade = document.querySelector('.source-option[data-action="open-premade"]');
      if (btnPremade && !btnPremade.classList.contains('active')) {
        document.getElementById('mobile-user-decks-view')?.classList.remove('hidden');
        document.getElementById('mobile-premade-decks-view')?.classList.add('hidden');
        const btnCreate = document.querySelector('[data-action="open-create"]');
        if (btnCreate) btnCreate.classList.remove('hidden');
      }
    } else {
      exitSelectMode();
    }
    render();
  }

  function deckRow(set, options = {}) {
    const currentClass = getClassForSet(set);
    const color = validColor(currentClass?.color, '#3b82f6');
    const stats = setStats(set);
    const due = dueCountForSet(set);
    const percent = progressPercent(set);
    const showDue = state.srsMode && due > 0;
    const title = escapeHtml(set.name || 'Untitled Set');
    const classLabel = currentClass ? currentClass.name : 'General';
    const icon = iconClass(currentClass?.icon, 'fa-layer-group');
    const lastActivity = set.lastOpened || set.lastModified || set.created;

    const isSelected = state.selectMode && state.selectedDecks && state.selectedDecks.has(String(set.id));
    const isSelectMode = state.selectMode;

    return `
      <article class="deck-row ${isSelected ? 'selected' : ''}" data-set-card="${escapeAttr(set.id)}">
        <div class="deck-icon" style="background:${color}24;color:${color}">
          <i class="${escapeAttr(icon)}"></i>
        </div>
        <div class="deck-main">
          <div class="deck-title-line">
            <h3 class="deck-title">${title}</h3>
            ${set.pinned ? '<span class="status-pill"><i class="fas fa-star"></i>Pinned</span>' : ''}
          </div>
          <div class="deck-subline">
            <span>${plural(stats.totalCards || 0, 'card')}</span>
            <span class="class-pill" style="background:${color}1f;color:${color}">${escapeHtml(classLabel)}</span>
            ${showDue ? `<span>${due} due</span>` : `<span>${escapeHtml(relativeTime(lastActivity))}</span>`}
          </div>
          <div class="progress-track" style="--progress:${percent}%"><span></span></div>
        </div>
        <div class="deck-actions" style="${isSelectMode ? 'display:none;' : ''}">
          ${options.compact ? '' : `
            <button type="button" class="small-icon-button ${set.pinned ? 'starred' : ''}" data-action="toggle-pin" data-set-id="${escapeAttr(set.id)}" aria-label="${set.pinned ? 'Unpin' : 'Pin'} deck">
              <i class="${set.pinned ? 'fas' : 'far'} fa-star"></i>
            </button>
            <button type="button" class="small-icon-button" data-action="edit-set" data-set-id="${escapeAttr(set.id)}" aria-label="Edit ${title}">
              <i class="fas fa-pen"></i>
            </button>
          `}
          <button type="button" class="small-icon-button primary" data-action="study-set" data-set-id="${escapeAttr(set.id)}" aria-label="Study ${title}">
            <i class="fas fa-play"></i>
          </button>
        </div>
      </article>
    `;
  }

  function emptyPanel(icon, title, copy, action = '') {
    return `
      <div class="empty-panel">
        <i class="fas ${escapeAttr(icon)}"></i>
        <strong>${escapeHtml(title)}</strong>
        <p>${escapeHtml(copy)}</p>
        ${action}
      </div>
    `;
  }

  function renderToday() {
    const totals = totalStats({ forceDue: true });
    const todayReviews = reviewsToday();
    const streak = streakDays();
    const remainingReviews = Number(totals.dueCards || 0);
    const dailyWork = todayReviews + remainingReviews;
    const hasDecks = totals.setCount > 0 || totals.cardCount > 0;
    const progress = dailyWork > 0
      ? clamp(Math.round((todayReviews / dailyWork) * 100), 0, 100)
      : (hasDecks ? 100 : 0);
    const progressLabel = dailyWork > 0 ? 'Goal' : (hasDecks ? 'Ready' : 'Start');
    const reviewAction = totals.dueCards > 0 ? 'review-due-smart' : (hasDecks ? 'tab-library' : 'open-create');
    const reviewLabel = totals.dueCards > 0 ? `Review ${totals.dueCards} Left` : (hasDecks ? 'Open Library' : 'Create Deck');

    selectors.todayHero.innerHTML = `
      <div class="hero-dashboard">
        <div class="goal-ring" style="--progress:${progress * 3.6}deg">
          <div><strong>${progress}%</strong><span>${progressLabel}</span></div>
        </div>
        <div class="hero-metrics">
          <div class="metric-pill"><strong>${totals.setCount}</strong><span>Decks</span></div>
          <div class="metric-pill"><strong>${todayReviews}</strong><span>Reviewed</span></div>
          <div class="metric-pill"><strong>${streak}</strong><span>Day streak</span></div>
        </div>
      </div>
      <div class="hero-actions">
        <button type="button" class="primary-action" data-action="${reviewAction}">
          <i class="fas ${totals.dueCards > 0 ? 'fa-brain' : 'fa-layer-group'}"></i>
          ${escapeHtml(reviewLabel)}
        </button>
        <button type="button" class="secondary-action" data-action="open-create">
          <i class="fas fa-plus"></i>
          New
        </button>
      </div>
    `;

    const continueSets = [...state.sets]
      .sort((a, b) => {
        const dueDiff = dueCountForSet(b, { force: true }) - dueCountForSet(a, { force: true });
        if (state.srsMode && dueDiff !== 0) return dueDiff;
        return normalizeTimestamp(b.lastOpened || b.lastModified) - normalizeTimestamp(a.lastOpened || a.lastModified);
      })
      .slice(0, 4);

    selectors.continueList.innerHTML = continueSets.length
      ? continueSets.map(set => deckRow(set, { compact: true })).join('')
      : emptyPanel('fa-layer-group', 'No decks yet', 'Create your first flashcard set or import a backup from desktop.');

    selectors.activityList.innerHTML = renderActivity();
  }

  function renderActivity() {
    const events = [];
    state.sets.forEach(set => {
      const meta = metaStats(set);
      if (meta?.lastReviewAt) {
        events.push({
          time: Number(meta.lastReviewAt),
          icon: 'fa-check',
          title: `Reviewed ${plural(Number(meta.reviewCount || 1), 'card')}`,
          copy: set.name || 'Untitled Set'
        });
      }
      (set.cards || []).forEach(card => {
        (card.reviewHistory || []).forEach(review => {
          const time = normalizeTimestamp(review.reviewedAt || review.time || review.date);
          if (time) {
            events.push({
              time,
              icon: 'fa-check',
              title: `Reviewed ${card.term ? `"${card.term}"` : 'a card'}`,
              copy: set.name || 'Untitled Set'
            });
          }
        });
      });
      const modified = normalizeTimestamp(set.lastModified || set.created);
      if (modified) {
        events.push({
          time: modified,
          icon: 'fa-layer-group',
          title: set.lastOpened ? `Studied ${set.name || 'a deck'}` : `Updated ${set.name || 'a deck'}`,
          copy: plural(setCardCount(set), 'card')
        });
      }
    });

    const recent = events.sort((a, b) => b.time - a.time).slice(0, 5);
    if (!recent.length) {
      return emptyPanel('fa-clock-rotate-left', 'No activity yet', 'Your review history and deck updates will appear here.');
    }

    return recent.map(event => `
      <div class="activity-row">
        <span class="settings-icon"><i class="fas ${escapeAttr(event.icon)}"></i></span>
        <span><strong>${escapeHtml(event.title)}</strong><small>${escapeHtml(event.copy)}</small></span>
        <span class="activity-time">${escapeHtml(relativeTime(event.time))}</span>
      </div>
    `).join('');
  }

  function filteredSets() {
    const query = state.search.trim().toLowerCase();
    let sets = [...state.sets];

    if (state.libraryFilter === 'general') {
      sets = sets.filter(set => !set.classId);
    } else if (state.libraryFilter === 'starred') {
      sets = sets.filter(set => set.pinned);
    } else if (state.libraryFilter.startsWith('class:')) {
      const classId = state.libraryFilter.slice(6);
      sets = sets.filter(set => String(set.classId || '') === String(classId));
    }

    if (query) {
      sets = sets.filter(set => {
        const currentClass = getClassForSet(set);
        const haystack = [
          set.name,
          set.description,
          currentClass?.name,
          ...(set.cards || []).flatMap(card => [card.term, card.definition, ...(card.tags || [])])
        ].join(' ').toLowerCase();
        return haystack.includes(query);
      });
    }

    return sets.sort((a, b) => {
      if (a.pinned !== b.pinned) return a.pinned ? -1 : 1;
      if (state.sort === 'name') return String(a.name || '').localeCompare(String(b.name || ''));
      if (state.sort === 'cards') return setCardCount(b) - setCardCount(a);
      if (state.sort === 'due') return dueCountForSet(b, { force: true }) - dueCountForSet(a, { force: true });
      return normalizeTimestamp(b.lastOpened || b.lastModified || b.created) - normalizeTimestamp(a.lastOpened || a.lastModified || a.created);
    });
  }

  function renderLibrary() {
    selectors.searchInput.value = state.search;
    selectors.sortLabel.textContent = sortLabels[state.sort] || 'Recent';
    Array.from(selectors.filters.querySelectorAll('.filter-chip')).forEach(button => {
      button.classList.toggle('active', button.dataset.filter === state.libraryFilter);
    });

    if (state.libraryFilter === 'classes') {
      renderClasses();
      return;
    }

    const sets = filteredSets();
    const classTitle = state.libraryFilter.startsWith('class:')
      ? state.classes.find(item => String(item.id) === state.libraryFilter.slice(6))?.name
      : null;
    selectors.countLabel.textContent = classTitle
      ? `${classTitle} - ${plural(sets.length, 'deck')}`
      : plural(sets.length, 'deck');

    if (!sets.length) {
      const action = state.search
        ? ''
        : '<button type="button" class="primary-action" data-action="open-create"><i class="fas fa-plus"></i>Create Set</button>';
      selectors.libraryList.innerHTML = emptyPanel(
        'fa-layer-group',
        state.search ? 'No matching decks' : 'No flashcard sets yet',
        state.search ? 'Try another search or switch filters.' : 'Create a deck, import a backup, or browse premade cards.',
        action
      );
      return;
    }

    const back = state.libraryFilter.startsWith('class:')
      ? '<button type="button" class="secondary-action" data-action="filter-classes"><i class="fas fa-arrow-left"></i>Classes</button>'
      : '';
    selectors.libraryList.innerHTML = `${back}${sets.map(set => deckRow(set)).join('')}`;
  }

  function renderClasses() {
    selectors.countLabel.textContent = plural(state.classes.length, 'class', 'classes');
    const query = state.search.trim().toLowerCase();
    const classes = state.classes
      .filter(item => !query || String(item.name || '').toLowerCase().includes(query))
      .sort((a, b) => String(a.name || '').localeCompare(String(b.name || '')));

    if (!classes.length) {
      selectors.libraryList.innerHTML = emptyPanel(
        'fa-chalkboard-user',
        'No classes yet',
        'Create classes from the deck editor to group sets like Biology, Math, English, or General.'
      );
      return;
    }

    selectors.libraryList.innerHTML = classes.map(classItem => {
      const color = validColor(classItem.color);
      const sets = state.sets.filter(set => String(set.classId || '') === String(classItem.id));
      const preview = sets.slice(0, 4).map(set => `<span>${escapeHtml(set.name || 'Untitled')}</span>`).join('');
      const extra = sets.length > 4 ? `<span>+${sets.length - 4} more</span>` : '';
      const due = state.srsMode ? sets.reduce((total, set) => total + dueCountForSet(set), 0) : 0;
      return `
        <div class="class-card" style="--class-color:${color}; position: relative;">
          <button type="button" class="class-card-click-area" data-action="open-class" data-class-id="${escapeAttr(classItem.id)}">
            <div class="class-card-content">
              <div class="class-title-row">
                <span class="class-icon"><i class="${escapeAttr(iconClass(classItem.icon, 'fa-graduation-cap'))}"></i></span>
                <div>
                  <h3 class="class-name">${escapeHtml(classItem.name)}</h3>
                  <div class="deck-subline">
                    <span>${plural(sets.length, 'deck')}</span>
                    ${state.srsMode ? `<span>${due} due</span>` : ''}
                  </div>
                </div>
              </div>
              <div class="class-preview">${preview || '<span>No decks yet</span>'}${extra}</div>
            </div>
          </button>
          <button type="button" class="class-edit-btn" data-action="edit-class" data-class-id="${escapeAttr(classItem.id)}" aria-label="Edit Class">
            <i class="fas fa-edit"></i>
          </button>
          <button type="button" class="class-delete-btn" data-action="delete-class" data-class-id="${escapeAttr(classItem.id)}" aria-label="Delete Class">
            <i class="fas fa-trash-can"></i>
          </button>
        </div>
      `;
    }).join('');
  }

  function plainTextFromHtml(value) {
    const element = document.createElement('div');
    element.innerHTML = String(value || '');
    return element.textContent || '';
  }

  function sanitizeEditorHtml(value) {
    const template = document.createElement('template');
    template.innerHTML = String(value || '').trim();
    const allowed = new Set(['B', 'STRONG', 'I', 'EM', 'U', 'BR', 'DIV', 'P', 'UL', 'OL', 'LI', 'SPAN']);
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
    return template.innerHTML;
  }

  function normalizeCardMedia(card = {}) {
    return window.EruditeMedia?.normalizeCardMedia
      ? window.EruditeMedia.normalizeCardMedia(card.media || {})
      : {
          term: Array.isArray(card.media?.term) ? card.media.term : [],
          definition: Array.isArray(card.media?.definition) ? card.media.definition : []
        };
  }

  function normalizeCardBackground(card = {}) {
    return window.EruditeMedia?.normalizeCardBackground
      ? window.EruditeMedia.normalizeCardBackground(card.background || {}, card)
      : {
          term: card.background?.term || null,
          definition: card.background?.definition || null
        };
  }

  function cardHasContent(card = {}) {
    const media = normalizeCardMedia(card);
    const background = normalizeCardBackground(card);
    return Boolean(
      plainTextFromHtml(card.term || '').trim()
      || plainTextFromHtml(card.definition || '').trim()
      || card.termImage
      || card.definitionImage
      || media.term.length
      || media.definition.length
      || background.term
      || background.definition
    );
  }

  function emptyCreatorCard() {
    const now = Date.now();
    return {
      id: schema?.createId ? schema.createId('card') : `card-${now}-${Math.random().toString(36).slice(2)}`,
      term: '',
      definition: '',
      termImage: '',
      definitionImage: '',
      media: { term: [], definition: [] },
      background: { term: null, definition: null },
      tags: [],
      suspended: false,
      buriedUntil: null,
      reviewHistory: [],
      created: now,
      lastModified: now
    };
  }

  function ensureCreatorCard() {
    if (!state.creator.cards.length) state.creator.cards = [emptyCreatorCard()];
  }

  function resetCreator() {
    clearTimeout(creatorDraftTimer);
    state.creator.editingSetId = null;
    state.creator.originalSet = null;
    state.creator.classId = '';
    state.creator.cards = [emptyCreatorCard()];
    state.creator.draftLoaded = false;
    if (selectors.createTitle) selectors.createTitle.value = '';
    if (selectors.createClassLabel) selectors.createClassLabel.textContent = 'General';
  }

  function syncCreatorFromDom() {
    if (!selectors.creatorCards) return;
    state.creator.cards = state.creator.cards.map(card => {
      const term = selectors.creatorCards.querySelector(`[data-editor-id="${cssEscape(card.id)}"][data-side="term"]`);
      const definition = selectors.creatorCards.querySelector(`[data-editor-id="${cssEscape(card.id)}"][data-side="definition"]`);
      return {
        ...card,
        term: sanitizeEditorHtml(term?.innerHTML || card.term || ''),
        definition: sanitizeEditorHtml(definition?.innerHTML || card.definition || '')
      };
    });
  }

  function formatButton(command, label, icon) {
    return `
      <button type="button" class="format-button" data-creator-action="format" data-command="${command}" aria-label="${label}">
        <i class="fas ${icon}"></i>
      </button>
    `;
  }

  function mediaPreviewHtml(card, side) {
    const media = normalizeCardMedia(card)[side] || [];
    const legacyKey = side === 'definition' ? 'definitionImage' : 'termImage';
    const legacy = card[legacyKey]
      ? [{
          id: `${side}-legacy-image`,
          kind: 'image',
          name: side === 'definition' ? 'Definition image' : 'Term image',
          src: card[legacyKey],
          legacy: true
        }]
      : [];
    const items = [...legacy, ...media];
    const background = normalizeCardBackground(card)[side];
    const mediaHtml = items.map(item => {
      const icon = item.kind === 'audio' ? 'fa-volume-high' : item.kind === 'video' ? 'fa-film' : 'fa-image';
      let preview = '';
      if (item.kind === 'audio') {
        preview = `<audio src="${escapeAttr(item.src)}" controls preload="metadata"></audio>`;
      } else if (item.kind === 'video') {
        preview = `<video src="${escapeAttr(item.src)}" controls preload="metadata"></video>`;
      } else {
        preview = `<img src="${escapeAttr(item.src)}" alt="">`;
      }
      return `
        <div class="creator-image-preview media-preview-item">
          <div class="media-preview-head">
            <span><i class="fas ${icon}"></i> ${escapeHtml(item.name || 'Media')}</span>
            <button type="button" data-creator-action="${item.legacy ? 'remove-image' : 'remove-media'}" data-card-id="${escapeAttr(card.id)}" data-side="${side}" data-media-id="${escapeAttr(item.id)}" aria-label="Remove media"><i class="fas fa-xmark"></i></button>
          </div>
          ${preview}
        </div>
      `;
    }).join('');
    const backgroundHtml = background ? `
      <div class="creator-background-preview" style="background-image:url('${escapeAttr(background.src)}')">
        <span><i class="fas fa-panorama"></i> Background</span>
        <button type="button" data-creator-action="remove-background" data-card-id="${escapeAttr(card.id)}" data-side="${side}" aria-label="Remove background">
          <i class="fas fa-xmark"></i>
        </button>
      </div>
    ` : '';
    return `${backgroundHtml}${mediaHtml}`;
  }

  function cardEditor(card, index) {
    card.media = normalizeCardMedia(card);
    card.background = normalizeCardBackground(card);
    const termMedia = mediaPreviewHtml(card, 'term');
    const definitionMedia = mediaPreviewHtml(card, 'definition');

    return `
      <article class="mobile-card-editor" data-card-id="${escapeAttr(card.id)}">
        <header>
          <span>Card ${index + 1}</span>
          <button type="button" class="small-icon-button" data-creator-action="delete-card" data-card-id="${escapeAttr(card.id)}" aria-label="Delete card">
            <i class="fas fa-trash"></i>
          </button>
        </header>
        <section class="editor-side">
          <div class="editor-side-head">
            <strong>Term</strong>
            <div class="creator-toolbar">
              ${formatButton('bold', 'Bold', 'fa-bold')}
              ${formatButton('italic', 'Italic', 'fa-italic')}
              ${formatButton('underline', 'Underline', 'fa-underline')}
              ${formatButton('formula', 'Formula', 'fa-square-root-variable')}
              <button type="button" class="format-button" data-creator-action="media" data-card-id="${escapeAttr(card.id)}" data-side="term" aria-label="Add term media">
                <i class="fas fa-paperclip"></i>
              </button>
              <button type="button" class="format-button" data-creator-action="background" data-card-id="${escapeAttr(card.id)}" data-side="term" aria-label="Set term background">
                <i class="fas fa-panorama"></i>
              </button>
            </div>
          </div>
          <div class="rich-editor" contenteditable="true" data-editor-id="${escapeAttr(card.id)}" data-side="term" data-placeholder="Enter term">${card.term || ''}</div>
          ${termMedia}
        </section>
        <section class="editor-side">
          <div class="editor-side-head">
            <strong>Definition</strong>
            <div class="creator-toolbar">
              ${formatButton('bold', 'Bold', 'fa-bold')}
              ${formatButton('italic', 'Italic', 'fa-italic')}
              ${formatButton('underline', 'Underline', 'fa-underline')}
              ${formatButton('formula', 'Formula', 'fa-square-root-variable')}
              <button type="button" class="format-button" data-creator-action="media" data-card-id="${escapeAttr(card.id)}" data-side="definition" aria-label="Add definition media">
                <i class="fas fa-paperclip"></i>
              </button>
              <button type="button" class="format-button" data-creator-action="background" data-card-id="${escapeAttr(card.id)}" data-side="definition" aria-label="Set definition background">
                <i class="fas fa-panorama"></i>
              </button>
            </div>
          </div>
          <div class="rich-editor" contenteditable="true" data-editor-id="${escapeAttr(card.id)}" data-side="definition" data-placeholder="Enter definition">${card.definition || ''}</div>
          ${definitionMedia}
        </section>
      </article>
    `;
  }

  function renderCreate() {
    const currentId = state.creator.classId || '';
    const currentClass = state.classes.find(item => String(item.id) === String(currentId));
    const labelSpan = document.getElementById('mobile-create-class-label');
    if (labelSpan) {
      labelSpan.textContent = currentClass ? currentClass.name : 'General';
    }

    // Populate custom select options
    const optionsContainer = document.getElementById('class-select-options');
    if (optionsContainer) {
      optionsContainer.innerHTML = [
        `<button type="button" class="context-option-row ${!currentId ? 'selected-class-opt' : ''}" data-class-val="">
          <i class="fas fa-layer-group"></i>
          <span>General</span>
        </button>`,
        ...state.classes.map(item => {
          const isSel = String(item.id) === String(currentId);
          const icon = iconClass(item.icon, 'fa-graduation-cap');
          return `<button type="button" class="context-option-row ${isSel ? 'selected-class-opt' : ''}" data-class-val="${escapeAttr(item.id)}">
            <i class="fas ${escapeAttr(icon)}"></i>
            <span>${escapeHtml(item.name)}</span>
          </button>`;
        }),
        `<button type="button" class="context-option-row create-class-option" data-class-action="new">
          <i class="fas fa-plus"></i>
          <span>New class</span>
        </button>`
      ].join('');
    }

    ensureCreatorCard();
    if (selectors.creatorCards) {
      selectors.creatorCards.innerHTML = `
        ${state.creator.cards.map((card, index) => cardEditor(card, index)).join('')}
        <button type="button" class="creator-bottom-add" data-creator-action="add-card" aria-label="Add another card">
          <i class="fas fa-plus"></i>
          <span>Add card</span>
        </button>
      `;
    }
  }

  function openPresetSelectModal() {
    const modal = selectors.presetSelectModal;
    if (!modal) return;
    const currentVal = selectors.pasteImportPreset?.value || 'standard';
    const buttons = modal.querySelectorAll('.preset-option-btn');
    buttons.forEach(btn => {
      btn.classList.toggle('selected', btn.dataset.presetVal === currentVal);
    });
    modal.classList.remove('hidden');
  }

  function updatePasteImportPresetLabel() {
    const labelEl = document.getElementById('mobile-paste-import-preset-label');
    if (!labelEl) return;
    const val = selectors.pasteImportPreset?.value || 'standard';
    let text = 'Standard (Word ; Meaning @ Card)';
    if (val === 'newline-semicolon') text = 'Line-by-Line (Word ; Meaning)';
    else if (val === 'newline-dash') text = 'Line-by-Line (Word - Meaning)';
    else if (val === 'newline-colon') text = 'Line-by-Line (Word : Meaning)';
    else if (val === 'custom') text = 'Custom Separators...';
    labelEl.textContent = text;
  }

  function openClassSelectModal(currentId, onSelect, onCreateNew) {
    const optionsContainer = document.getElementById('class-select-options');
    if (optionsContainer) {
      optionsContainer.innerHTML = [
        `<button type="button" class="context-option-row ${!currentId ? 'selected-class-opt' : ''}" data-class-val="">
          <i class="fas fa-layer-group"></i>
          <span>General</span>
        </button>`,
        ...state.classes.map(item => {
          const isSel = String(item.id) === String(currentId);
          const icon = iconClass(item.icon, 'fa-graduation-cap');
          return `<button type="button" class="context-option-row ${isSel ? 'selected-class-opt' : ''}" data-class-val="${escapeAttr(item.id)}">
            <i class="fas ${escapeAttr(icon)}"></i>
            <span>${escapeHtml(item.name)}</span>
          </button>`;
        }),
        `<button type="button" class="context-option-row create-class-option" data-class-action="new">
          <i class="fas fa-plus"></i>
          <span>New class</span>
        </button>`
      ].join('');
    }

    state.classSelectCallbacks = { onSelect, onCreateNew };
    const modal = document.getElementById('class-select-modal');
    if (modal) modal.style.display = 'flex';
  }

  function openMobileClassEditor(existingClass = null) {
    return new Promise(resolve => {
      const existing = document.getElementById('mobile-class-editor-modal');
      if (existing) existing.remove();

      let selectedColor = existingClass?.color || classColorChoices[0];
      let selectedIcon = existingClass?.icon || classIconChoices[0];
      const modal = document.createElement('div');
      modal.className = 'deck-context-modal class-editor-sheet';
      modal.id = 'mobile-class-editor-modal';
      modal.innerHTML = `
        <div class="context-modal-backdrop" data-class-editor-cancel></div>
        <div class="context-modal-content">
          <div class="context-modal-header">
            <h3>${existingClass ? 'Edit Class' : 'New Class'}</h3>
          </div>
          <div class="mobile-class-editor-form">
            <label class="mobile-field">
              <span>Name</span>
              <input id="mobile-class-editor-name" type="text" maxlength="80" autocomplete="off" placeholder="Biology" value="${escapeAttr(existingClass?.name || '')}">
            </label>
            <div class="mobile-field">
              <span>Color</span>
              <div class="class-color-grid">
                ${classColorChoices.map(color => `
                  <button type="button" class="class-color-choice ${color === selectedColor ? 'active' : ''}" data-color="${color}" style="--swatch:${color}" aria-label="Use ${color}"></button>
                `).join('')}
                <label class="class-color-custom" aria-label="Custom color">
                  <i class="fas fa-eye-dropper"></i>
                  <input id="mobile-class-editor-color" type="color" value="${selectedColor}">
                </label>
              </div>
            </div>
            <div class="mobile-field">
              <span>Icon</span>
              <div class="class-icon-grid">
                ${classIconChoices.map(icon => `
                  <button type="button" class="class-icon-choice ${icon === selectedIcon ? 'active' : ''}" data-icon="${icon}" aria-label="${icon}">
                    <i class="fas ${icon}"></i>
                  </button>
                `).join('')}
              </div>
            </div>
            <div class="class-editor-actions">
              <button type="button" class="secondary-action" data-class-editor-cancel>Cancel</button>
              <button type="button" class="primary-action" data-class-editor-save><i class="fas fa-check"></i>${existingClass ? 'Save' : 'Create'}</button>
            </div>
          </div>
        </div>
      `;

      const close = value => {
        modal.remove();
        resolve(value);
      };

      modal.addEventListener('click', event => {
        const colorButton = event.target.closest('[data-color]');
        if (colorButton) {
          selectedColor = validColor(colorButton.dataset.color, selectedColor);
          modal.querySelectorAll('.class-color-choice').forEach(button => button.classList.toggle('active', button === colorButton));
          const input = modal.querySelector('#mobile-class-editor-color');
          if (input) input.value = selectedColor;
          playClick();
          return;
        }

        const iconButton = event.target.closest('[data-icon]');
        if (iconButton) {
          selectedIcon = iconButton.dataset.icon || selectedIcon;
          modal.querySelectorAll('.class-icon-choice').forEach(button => button.classList.toggle('active', button === iconButton));
          playClick();
          return;
        }

        if (event.target.closest('[data-class-editor-cancel]')) {
          event.preventDefault();
          close(null);
          return;
        }

        if (event.target.closest('[data-class-editor-save]')) {
          event.preventDefault();
          const name = String(modal.querySelector('#mobile-class-editor-name')?.value || '').trim();
          if (!name) {
            modal.querySelector('#mobile-class-editor-name')?.focus();
            showToast('Name the class');
            return;
          }
          close({ name, color: selectedColor, icon: selectedIcon });
        }
      });

      modal.querySelector('#mobile-class-editor-color')?.addEventListener('input', event => {
        selectedColor = validColor(event.target.value, selectedColor);
        modal.querySelectorAll('.class-color-choice').forEach(button => button.classList.remove('active'));
      });

      document.body.appendChild(modal);
      requestAnimationFrame(() => modal.querySelector('#mobile-class-editor-name')?.focus());
    });
  }

  async function createClassFromCreator() {
    const result = await openMobileClassEditor();
    if (!result) return;
    const classData = schema?.normalizeClass
      ? schema.normalizeClass({
          name: result.name,
          color: validColor(result.color, '#3B82F6'),
          icon: result.icon || 'fa-graduation-cap'
        })
      : {
          id: `class-${Date.now()}`,
          name: result.name,
          color: validColor(result.color, '#3B82F6'),
          icon: result.icon || 'fa-graduation-cap',
          created: Date.now(),
          lastModified: Date.now()
        };
    try {
      const saved = await window.flashcardStore.saveClass(classData);
      // Immediately update local state and re-render so the new class appears in the dropdown
      state.classes = await window.flashcardStore.listClasses();
      const savedId = saved?.id || classData.id;
      // Flush store in background — do not await to avoid blocking UI
      flushStore(900).catch(err => console.warn('[mobile] flushStore after class create:', err));
      playClick();
      showToast('Class created');

      if (state.classSelectCallbacks?.onSelect) {
        state.classSelectCallbacks.onSelect(savedId);
      } else {
        state.creator.classId = savedId;
        renderCreate();
        scheduleCreatorDraftSave();
      }
      state.classSelectCallbacks = null;
    } catch (error) {
      console.error(error);
      showToast('Could not create class');
    }
  }

  function parseBulkCards(text) {
    const termSep = parseSeparator(state.settings?.importTermSep || ';');
    const cardSep = parseSeparator(state.settings?.importCardSep || '@');

    return String(text || '')
      .split(cardSep)
      .map(chunk => {
        const idx = chunk.indexOf(termSep);
        if (idx < 0) return null;
        const term = chunk.slice(0, idx).trim();
        const definition = chunk.slice(idx + termSep.length).trim();
        if (!term && !definition) return null;
        return {
          ...emptyCreatorCard(),
          term: escapeHtml(term.trim()),
          definition: escapeHtml(definition.trim())
        };
      })
      .filter(Boolean);
  }

  async function loadSetIntoCreator(setId) {
    const found = await window.flashcardStore.getSet(setId);
    if (!found) {
      showToast('Could not open deck');
      return;
    }
    const normalized = schema?.normalizeSet ? schema.normalizeSet(found, null, { preserveLastModified: true }) : found;
    state.creator.editingSetId = normalized.id;
    state.creator.originalSet = normalized;
    state.creator.classId = normalized.classId || '';
    state.creator.cards = (normalized.cards || []).map(card => ({ ...card }));
    if (!state.creator.cards.length) state.creator.cards = [emptyCreatorCard()];
    selectors.createTitle.value = normalized.name || '';
    setActiveTab('create');
  }

  function hasCardContent(card) {
    return cardHasContent({
      ...card,
      term: plainTextFromHtml(card.term || card.sanitizedTerm || '').trim(),
      definition: plainTextFromHtml(card.definition || card.sanitizedDefinition || '').trim()
    });
  }

  function creatorSnapshot() {
    syncCreatorFromDom();
    return {
      version: 1,
      editingSetId: state.creator.editingSetId || null,
      savedSetId: state.creator.originalSet?.id || state.creator.editingSetId || null,
      name: String(selectors.createTitle?.value || '').trim(),
      classId: state.creator.classId || null,
      cards: state.creator.cards.map(card => ({
        ...card,
        term: sanitizeEditorHtml(card.term),
        definition: sanitizeEditorHtml(card.definition)
      })),
      updatedAt: Date.now()
    };
  }

  function isMeaningfulCreatorDraft(draft) {
    if (draftCore?.hasMeaningfulDraft) return draftCore.hasMeaningfulDraft(draft);
    if (!draft || typeof draft !== 'object') return false;
    if (String(draft.name || '').trim()) return true;
    if (draft.classId) return true;
    return Array.isArray(draft.cards) && draft.cards.some(hasCardContent);
  }

  function hasVisibleCreatorWork() {
    const snapshot = creatorSnapshot();
    return isMeaningfulCreatorDraft(snapshot);
  }

  async function saveCreatorDraft(options = {}) {
    clearTimeout(creatorDraftTimer);
    const snapshot = creatorSnapshot();
    try {
      if (isMeaningfulCreatorDraft(snapshot)) {
        localStorage.setItem(CREATOR_DRAFT_KEY, JSON.stringify(snapshot));
        if (options.persistStore) {
          await window.flashcardStore.setState(CREATOR_DRAFT_KEY, snapshot);
        }
      } else {
        localStorage.removeItem(CREATOR_DRAFT_KEY);
        if (options.persistStore) {
          await window.flashcardStore.removeState(CREATOR_DRAFT_KEY);
        }
      }
      if (options.flush) await flushStore(options.flushTimeout || 900);
    } catch (error) {
      console.warn('[mobile] draft save failed:', error);
    }
  }

  function scheduleCreatorDraftSave() {
    clearTimeout(creatorDraftTimer);
    creatorDraftTimer = window.setTimeout(() => {
      const run = () => saveCreatorDraft().catch(error => console.warn('[mobile] draft autosave failed:', error));
      if (window.requestIdleCallback) {
        window.requestIdleCallback(run, { timeout: 1800 });
      } else {
        window.setTimeout(run, 80);
      }
    }, 2200);
  }

  async function clearCreatorDraft() {
    clearTimeout(creatorDraftTimer);
    localStorage.removeItem(CREATOR_DRAFT_KEY);
    try {
      await window.flashcardStore.removeState(CREATOR_DRAFT_KEY);
    } catch (error) {
      console.warn('[mobile] draft clear failed:', error);
    }
  }

  async function loadDraftIntoCreator(draft) {
    const editingId = draft?.editingSetId || draft?.savedSetId || null;
    let original = null;
    if (editingId) {
      try {
        original = await window.flashcardStore.getSet(editingId);
      } catch (_) {
        original = null;
      }
    }
    const normalizedOriginal = original && schema?.normalizeSet
      ? schema.normalizeSet(original, null, { preserveLastModified: true })
      : original;
    state.creator.editingSetId = normalizedOriginal?.id || null;
    state.creator.originalSet = normalizedOriginal || null;
    state.creator.classId = draft?.classId || '';
    state.creator.cards = Array.isArray(draft?.cards) && draft.cards.length
      ? draft.cards.map(card => schema?.normalizeCard ? schema.normalizeCard(card) : { ...emptyCreatorCard(), ...card })
      : [emptyCreatorCard()];
    state.creator.draftLoaded = true;
    if (selectors.createTitle) selectors.createTitle.value = draft?.name || normalizedOriginal?.name || '';
  }

  async function maybeRestoreCreatorDraft() {
    if (hasVisibleCreatorWork()) return;
    let draft = null;
    try {
      draft = JSON.parse(localStorage.getItem(CREATOR_DRAFT_KEY) || 'null');
    } catch (_) {
      draft = null;
    }
    try {
      draft = draft || await window.flashcardStore.getState(CREATOR_DRAFT_KEY);
    } catch (_) {
      draft = draft || null;
    }
    if (!isMeaningfulCreatorDraft(draft)) return;

    const savedId = draft.savedSetId || draft.editingSetId || null;
    if (savedId && draftCore?.isDraftSameAsSavedSet) {
      try {
        const saved = await window.flashcardStore.getSet(savedId);
        if (saved && draftCore.isDraftSameAsSavedSet(draft, saved)) {
          await clearCreatorDraft();
          return;
        }
      } catch (_) {}
    }

    const shouldContinue = await showDraftRestoreModal();
    if (shouldContinue) {
      await loadDraftIntoCreator(draft);
      showToast('Draft restored');
    } else {
      await clearCreatorDraft();
      resetCreator();
    }
  }

  async function openCreator() {
    await maybeRestoreCreatorDraft();
    setActiveTab('create');
  }

  async function saveMobileDeck() {
    if (!window.flashcardStore?.saveSet) {
      throw new Error('Storage is still starting. Try again in a moment.');
    }
    syncCreatorFromDom();
    const name = String(selectors.createTitle?.value || '').trim();
    const cards = state.creator.cards
      .map(card => ({
        ...card,
        term: sanitizeEditorHtml(card.term),
        definition: sanitizeEditorHtml(card.definition),
        lastModified: Date.now()
      }))
      .filter(hasCardContent);
    if (!name) {
      showToast('Add a deck name');
      selectors.createTitle?.focus();
      return;
    }
    if (!cards.length) {
      showToast('Add at least one card');
      selectors.creatorCards?.querySelector('[contenteditable="true"]')?.focus();
      return;
    }

    const original = state.creator.originalSet || {};
    const saved = await window.flashcardStore.saveSet({
      ...original,
      id: state.creator.editingSetId || original.id,
      name,
      classId: state.creator.classId || null,
      cards,
      srsSettings: schema?.normalizeSrsSettings ? schema.normalizeSrsSettings(original.srsSettings || {}) : (original.srsSettings || { enabled: true }),
      pinned: Boolean(original.pinned)
    });
    await clearCreatorDraft();
    // Flush store in background — no need to block navigation on it
    flushStore(1800).catch(err => console.warn('[mobile] flushStore after save:', err));
    showToast(`Saved ${plural(cards.length, 'card')}`);
    state.browserLoaded = false;
    resetCreator();
    if (saved?.id) {
      state.sets = state.sets.map(item => String(item.id) === String(saved.id) ? saved : item);
    }
    await refresh();
    setActiveTab('library');
  }

  function subjectLabel(subject) {
    return String(subject || '').replace(/-/g, ' ').replace(/\b\w/g, char => char.toUpperCase());
  }

  function renderPremade() {
    if (!selectors.premadeList) return;
    selectors.premadeClassFilters.innerHTML = premadeClasses.map(item => `
      <button type="button" class="filter-chip ${state.premadeClass === item.id ? 'active' : ''}" data-action="premade-class" data-class-id="${escapeAttr(item.id)}">
        ${escapeHtml(item.name)}
      </button>
    `).join('');

    const subjects = premadeSubjects[state.premadeClass] || [];
    if (!subjects.includes(state.premadeSubject)) state.premadeSubject = subjects[0] || '';
    selectors.premadeSubjectFilters.innerHTML = subjects.map(subject => `
      <button type="button" class="filter-chip ${state.premadeSubject === subject ? 'active' : ''}" data-action="premade-subject" data-subject-id="${escapeAttr(subject)}">
        ${escapeHtml(subjectLabel(subject))}
      </button>
    `).join('');

    selectors.premadeList.innerHTML = state.premadeSets.length
      ? state.premadeSets.map(item => {
          const file = item.fileName || item.filename || item.file || item.path || '';
          return `
            <article class="premade-row">
              <div class="deck-icon"><i class="fas fa-book-open"></i></div>
              <div class="deck-main">
                <h3 class="deck-title">${escapeHtml(item.name || item.title || file || 'Premade Deck')}</h3>
                <div class="deck-subline">
                  <span>${escapeHtml(subjectLabel(state.premadeSubject))}</span>
                  ${item.cardCount ? `<span>${plural(Number(item.cardCount) || 0, 'card')}</span>` : ''}
                </div>
              </div>
              <button type="button" class="small-icon-button primary" data-action="import-premade" data-file="${escapeAttr(file)}" aria-label="Import premade deck">
                <i class="fas fa-plus"></i>
              </button>
            </article>
          `;
        }).join('')
      : emptyPanel('fa-book-open', 'No premade decks here yet', 'This subject has no bundled decks in the current build.');
  }

  async function loadPremade() {
    selectors.premadeList.innerHTML = emptyPanel('fa-spinner', 'Loading premade decks', 'Checking bundled starter decks.');
    const sets = await window.flashcardStore.listPremadeSets(state.premadeClass, state.premadeSubject);
    state.premadeSets = Array.isArray(sets) ? sets : [];
    renderPremade();
  }

  async function importPremade(fileName) {
    if (!fileName) {
      showToast('Premade file missing');
      return;
    }
    const data = await window.flashcardStore.getPremadeSet(state.premadeClass, state.premadeSubject, fileName);
    if (!data) {
      showToast('Could not import deck');
      return;
    }

    const overlay = document.getElementById('take-deck-overlay');
    const nameInput = document.getElementById('mobile-take-deck-name');
    const classSelect = document.getElementById('mobile-take-deck-class');
    const cancelBtn = document.getElementById('mobile-take-deck-cancel');
    const confirmBtn = document.getElementById('mobile-take-deck-confirm');

    if (nameInput) {
      nameInput.value = data.name || data.title || fileName.replace(/\.json$/i, '');
    }

    if (classSelect) {
      classSelect.innerHTML = '<option value="">General</option>';
      (state.classes || []).forEach(c => {
        const opt = document.createElement('option');
        opt.value = c.id;
        opt.textContent = c.name;
        classSelect.appendChild(opt);
      });
    }

    overlay?.classList.remove('hidden');

    const cleanupListeners = () => {
      cancelBtn?.removeEventListener('click', onCancel);
      confirmBtn?.removeEventListener('click', onConfirm);
      overlay?.removeEventListener('click', onOverlayClick);
    };

    const onCancel = () => {
      overlay?.classList.add('hidden');
      cleanupListeners();
    };

    const onOverlayClick = (e) => {
      if (e.target === overlay) {
        overlay?.classList.add('hidden');
        cleanupListeners();
      }
    };

    const onConfirm = async () => {
      const targetName = nameInput?.value.trim() || data.name || fileName.replace(/\.json$/i, '');
      const targetClassId = classSelect?.value || null;

      try {
        const saved = await window.flashcardStore.saveSet({
          ...data,
          id: null,
          name: targetName,
          classId: targetClassId
        });
        showToast(`Imported ${saved.name || 'deck'}`);
        state.browserLoaded = false;
        overlay?.classList.add('hidden');
        cleanupListeners();
        await refresh();
        setActiveTab('library');
      } catch (e) {
        console.error(e);
        showToast('Could not import deck');
      }
    };

    cancelBtn?.addEventListener('click', onCancel);
    confirmBtn?.addEventListener('click', onConfirm);
    overlay?.addEventListener('click', onOverlayClick);
  }


  async function loadBrowserCards() {
    if (state.browserLoaded) return;
    selectors.browserList.innerHTML = emptyPanel('fa-spinner', 'Loading cards', 'Building a searchable local card list.');
    const sets = await window.flashcardStore.listSets();
    const classLookup = classMap();
    state.browserCards = [];
    (sets || []).forEach(set => {
      const className = set.classId ? classLookup.get(String(set.classId))?.name : 'General';
      (set.cards || []).forEach(card => {
        state.browserCards.push({
          setId: set.id,
          deck: set.name || 'Untitled Set',
          className: className || 'General',
          term: card.term || '',
          definition: card.definition || '',
          tags: Array.isArray(card.tags) ? card.tags : [],
          srsState: card.srs?.state || 'New'
        });
      });
    });
    state.browserLoaded = true;
  }

  function renderBrowser() {
    if (!selectors.browserList) return;
    selectors.browserSearchInput.value = state.browserSearch;
    const query = state.browserSearch.trim().toLowerCase();
    const cards = state.browserCards.filter(card => {
      if (!query) return true;
      return [card.deck, card.className, card.term, card.definition, card.srsState, ...(card.tags || [])]
        .join(' ')
        .toLowerCase()
        .includes(query);
    }).slice(0, 120);

    selectors.browserList.innerHTML = cards.length
      ? cards.map(card => `
        <article class="browser-card">
          <div class="browser-card-head">
            <span>${escapeHtml(card.deck)}</span>
            <small>${escapeHtml(card.className)}</small>
          </div>
          <strong>${escapeHtml(card.term || 'Empty term')}</strong>
          <p>${escapeHtml(card.definition || 'Empty definition')}</p>
          <div class="deck-subline">
            <span>${escapeHtml(card.srsState)}</span>
            ${(card.tags || []).slice(0, 3).map(tag => `<span>#${escapeHtml(tag)}</span>`).join('')}
          </div>
        </article>
      `).join('')
      : emptyPanel('fa-table-list', 'No cards found', query ? 'Try another search.' : 'Create or import a deck first.');
  }


  function renderMore() {
    selectors.srsSwitch?.classList.toggle('on', state.srsMode);
    selectors.moreSrsLabel.textContent = state.srsMode ? 'On - due reviews are scheduled' : 'Off - normal study only';
    const order = normalizeNormalStudyOrder(state.settings?.normalStudyOrder);
    const orderLabels = {
      forward: 'Beginning',
      backward: 'End',
      random: 'Random'
    };
    const label = document.getElementById('more-study-order-label');
    if (label) {
      label.textContent = orderLabels[order] || 'Beginning';
    }
    if (selectors.themeLabel) {
      const theme = state.settings?.theme || 'dark';
      selectors.themeLabel.textContent = theme === 'light' ? 'Aura Light' : 'Dark Blue';
    }
  }

  function renderActive() {
    switch (state.activeTab) {
      case 'today':
        renderToday();
        break;
      case 'library':
        renderLibrary();
        break;
      case 'create':
        renderCreate();
        break;
      case 'premade':
        renderPremade();
        break;
      case 'browser':
        renderBrowser();
        break;
      case 'more':
        renderMore();
        break;
      default:
        renderToday();
        break;
    }
  }

  function render(options = {}) {
    if (options.all) {
      renderToday();
      renderLibrary();
      renderCreate();
      renderPremade();
      renderBrowser();
      renderMore();
      return;
    }
    renderActive();
  }

  async function refresh() {
    try {
      await loadData();
      render();
    } catch (error) {
      console.error('Refresh error:', error);
      const errorHtml = emptyPanel('fa-triangle-exclamation', 'Could not load library', error.message || 'Storage failed to open.');
      selectors.todayHero.innerHTML = errorHtml;
      selectors.libraryList.innerHTML = errorHtml;
      selectors.continueList.innerHTML = '';
      selectors.activityList.innerHTML = '';
      showToast('Storage error — try restarting the app');
    }
  }

  function showAppLoader(title = 'Erudite Flashcards', copy = 'Loading') {
    if (selectors.loadingTitle) selectors.loadingTitle.textContent = title;
    if (selectors.loadingCopy) selectors.loadingCopy.textContent = copy;
    const cover = document.getElementById('app-loading-cover');
    if (cover) cover.style.display = '';
    document.body.classList.remove('app-ready');
    document.body.classList.add('is-route-loading');
  }

  function hideAppLoader() {
    document.body.classList.add('app-ready');
    document.body.classList.remove('is-route-loading');
    setTimeout(() => {
      const cover = document.getElementById('app-loading-cover');
      if (cover) cover.style.display = 'none';
    }, 200);
  }

  function showMicroLoader(text = 'Saving changes...') {
    const overlay = document.getElementById('micro-loader-overlay');
    if (overlay) {
      const textEl = overlay.querySelector('.micro-loader-text');
      if (textEl) textEl.textContent = text;
      overlay.classList.remove('hidden');
    }
  }

  function hideMicroLoader() {
    const overlay = document.getElementById('micro-loader-overlay');
    if (overlay) {
      overlay.classList.add('hidden');
    }
  }

  function navigateTo(url, options = {}) {
    showAppLoader(options.title || 'Opening Study', options.copy || 'Preparing your cards');
    requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        window.location.href = url;
      });
    });
  }

  function mobileStudyUrl(setId, options = {}) {
    const reviewDue = typeof options === 'boolean' ? options : Boolean(options.reviewDue);
    const srsMode = typeof options === 'object' && Object.prototype.hasOwnProperty.call(options, 'srsMode')
      ? Boolean(options.srsMode)
      : state.srsMode;
    const query = new URLSearchParams({
      setId: String(setId),
      srs: String(Boolean(reviewDue || srsMode)),
      from: state.activeTab || 'library'
    });
    if (reviewDue) query.set('reviewDue', 'true');
    return `mobile/study.html?${query.toString()}`;
  }

  async function flushStore(timeoutMs = 100) {
    const flush = window.eruditeMobileFlashcards?.flush || window.flashcardStore?.flush;
    if (typeof flush !== 'function') return;
    await Promise.race([
      flush().catch(() => {}),
      new Promise(resolve => window.setTimeout(resolve, timeoutMs))
    ]);
  }

  async function toggleSrs() {
    persistSrsMode(!state.srsMode);
    playClick();
    render();
    showToast(state.srsMode ? 'SRS mode on' : 'SRS mode off');
  }

  async function togglePin(setId) {
    const set = state.sets.find(item => String(item.id) === String(setId));
    if (!set) return;
    const nextPinned = !set.pinned;
    await window.flashcardStore.saveSet({ ...set, pinned: nextPinned });
    if (nextPinned) {
      playStar();
    } else {
      playClick();
    }
    await refresh();
  }

  function showMobileConfirm({ title, message, okText = 'Delete', cancelText = 'Cancel', isDanger = true }) {
    return new Promise((resolve) => {
      const overlay = document.getElementById('mobile-confirm-overlay');
      const titleEl = document.getElementById('mobile-confirm-title');
      const msgEl = document.getElementById('mobile-confirm-message');
      const cancelBtn = document.getElementById('mobile-confirm-cancel');
      const okBtn = document.getElementById('mobile-confirm-ok');

      if (!overlay || !titleEl || !msgEl || !cancelBtn || !okBtn) {
        resolve(false);
        return;
      }

      titleEl.innerHTML = `<i class="fas fa-exclamation-triangle" style="color: ${isDanger ? '#f87171' : '#f59e0b'}; margin-right: 0.5rem;"></i> ${title}`;
      msgEl.textContent = message;
      okBtn.textContent = okText;
      cancelBtn.textContent = cancelText;

      if (isDanger) {
        okBtn.classList.add('danger');
      } else {
        okBtn.classList.remove('danger');
      }

      overlay.classList.remove('hidden');

      function cleanUp() {
        cancelBtn.removeEventListener('click', onCancel);
        okBtn.removeEventListener('click', onOk);
        overlay.classList.add('hidden');
        state.lastModalClosedAt = Date.now();
      }

      function onCancel() {
        if (typeof playClick === 'function') playClick();
        cleanUp();
        resolve(false);
      }

      function onOk() {
        if (typeof playClick === 'function') playClick();
        cleanUp();
        resolve(true);
      }

      cancelBtn.addEventListener('click', onCancel);
      okBtn.addEventListener('click', onOk);
    });
  }

  async function resetNonSrsProgress(setId) {
    const ok = await showMobileConfirm({
      title: 'Reset Progress',
      message: 'Are you sure you want to reset the normal (non-SRS) study progress for this deck? This will reset the card navigation index to the beginning.',
      okText: 'Reset',
      isDanger: false
    });
    if (!ok) return;

    try {
      const saved = await window.flashcardStore.getProgress(setId);
      if (saved) {
        saved.cardIndex = 0;
        saved.normalModeIndex = 0;
        saved.normalForwardIndex = 0;
        saved.normalBackwardIndex = 0;
        if (saved.normalProgress) {
          saved.normalProgress.forward = 0;
          saved.normalProgress.backward = 0;
        }
        if (saved.normal) {
          saved.normal.forwardIndex = 0;
          saved.normal.backwardIndex = 0;
        }
        saved.timestamp = Date.now();
        await window.flashcardStore.saveProgress(setId, saved);
      }
      localStorage.removeItem('erudite-mobile-progress:' + setId);
      showToast('Normal study progress reset');
      await refresh();
    } catch (error) {
      console.error('Error resetting progress:', error);
      showToast('Could not reset study progress');
    }
  }

  async function executeDeckSrsReset(setId) {
    const deleteHistory = await showMobileConfirm({
      title: 'Delete History?',
      message: 'Do you want to delete the review history as well? (Select Delete History to clear logs, or Keep History to retain stats)',
      okText: 'Delete History',
      cancelText: 'Keep History',
      isDanger: true
    });
    const ok = await showMobileConfirm({
      title: 'Reset SRS Data',
      message: 'Are you sure you want to reset the SRS scheduling data for this deck? This will make all cards behave like new cards again. Card content will not be modified.',
      okText: 'Reset',
      isDanger: true
    });
    if (!ok) return;

    try {
      await window.flashcardStore.resetDeckSRS(setId, deleteHistory);
      localStorage.removeItem('erudite-mobile-progress:' + setId);
      try {
        const patches = JSON.parse(localStorage.getItem('erudite-mobile-study-card-patches-v1') || 'null');
        if (patches && patches.sets && patches.sets[setId]) {
          delete patches.sets[setId];
          localStorage.setItem('erudite-mobile-study-card-patches-v1', JSON.stringify(patches));
        }
      } catch (_) {}
      showToast('SRS scheduling reset successfully');
      await refresh();
    } catch (error) {
      console.error('Error resetting SRS data:', error);
      showToast('Could not reset SRS data');
    }
  }

  async function deleteSet(setId) {
    const set = state.sets.find(item => String(item.id) === String(setId));
    if (!set) return;
    const ok = await showMobileConfirm({
      title: 'Delete Deck',
      message: `Are you sure you want to delete "${set.name || 'Untitled Set'}"? This cannot be undone.`,
      okText: 'Delete',
      isDanger: true
    });
    if (!ok) return;
    showMicroLoader('Deleting deck...');
    try {
      await window.flashcardStore.deleteSet(setId);
      showToast('Deck deleted');
      await refresh();
    } finally {
      hideMicroLoader();
    }
  }

  async function deleteClass(classId) {
    const classItem = state.classes.find(c => String(c.id) === String(classId));
    if (!classItem) return;
    const sets = state.sets.filter(set => String(set.classId || '') === String(classId));
    const deckText = sets.length > 0 
      ? `Any decks in this class (${sets.length} total) will be moved to General.`
      : '';
    const ok = await showMobileConfirm({
      title: 'Delete Class',
      message: `Are you sure you want to delete the class "${classItem.name}"? ${deckText} This cannot be undone.`,
      okText: 'Delete',
      isDanger: true
    });
    if (!ok) return;

    showMicroLoader('Deleting class...');
    try {
      await window.flashcardStore.deleteClass(classId);
      playClick();
      showToast('Class deleted');
      await refresh();
    } catch (error) {
      console.error('[mobile] Could not delete class:', error);
      showToast('Could not delete class');
    } finally {
      hideMicroLoader();
    }
  }

  async function editClass(classId) {
    const classItem = state.classes.find(item => String(item.id) === String(classId));
    if (!classItem) return;

    const result = await openMobileClassEditor(classItem);
    if (!result) return;

    showMicroLoader('Saving class...');
    try {
      const updated = schema?.normalizeClass
        ? schema.normalizeClass({
            ...classItem,
            name: result.name,
            color: validColor(result.color, '#3B82F6'),
            icon: result.icon || 'fa-graduation-cap',
            lastModified: Date.now()
          }, classItem, { preserveLastModified: false })
        : {
            ...classItem,
            name: result.name,
            color: validColor(result.color, '#3B82F6'),
            icon: result.icon || 'fa-graduation-cap',
            lastModified: Date.now()
          };

      await window.flashcardStore.saveClass(updated);
      showToast('Class updated successfully');

      // Update local state classes array
      state.classes = state.classes.map(item => String(item.id) === String(updated.id) ? updated : item);
      await refresh();
    } catch (error) {
      console.error('[mobile] Could not save class updates:', error);
      showToast('Could not save class updates');
    } finally {
      hideMicroLoader();
    }
  }

  // ─── Custom Modal Helpers ──────────────────────────────────────────────

  /**
   * Opens the formula modal. Resolves when user confirms/cancels.
   * savedRange: Selection range to restore before inserting formula.
   */
  function openFormulaModal(onReady) {
    const overlay = selectors.formulaOverlay;
    const input = selectors.formulaInput;
    if (!overlay || !input) {
      const raw = window.prompt('Enter formula (LaTeX):', '');
      if (!raw) return;
      const formula = window.EruditeMath?.inlineFormula
        ? window.EruditeMath.inlineFormula(raw)
        : `\\(${raw.trim()}\\)`;
      if (formula) document.execCommand('insertText', false, formula);
      return;
    }

    // Capture current selection range so we can restore it after modal interaction
    let savedRange = null;
    const sel = window.getSelection();
    if (sel && sel.rangeCount > 0) savedRange = sel.getRangeAt(0).cloneRange();

    input.value = '';
    overlay.classList.remove('hidden');
    requestAnimationFrame(() => input.focus());

    function doInsert() {
      const rawInput = String(input.value || '').trim();
      overlay.classList.add('hidden');
      cleanup();
      if (!rawInput) return;
      const formula = window.EruditeMath?.inlineFormula
        ? window.EruditeMath.inlineFormula(rawInput)
        : `\\(${rawInput}\\)`;
      if (onReady) onReady(savedRange);
      if (formula) document.execCommand('insertText', false, formula);
      updateFormatState();
      scheduleCreatorDraftSave();
    }

    function doCancel() {
      overlay.classList.add('hidden');
      cleanup();
    }

    function handleKeydown(e) {
      if (e.key === 'Enter') { e.preventDefault(); doInsert(); }
      if (e.key === 'Escape') doCancel();
    }

    function cleanup() {
      selectors.formulaConfirm?.removeEventListener('click', doInsert);
      selectors.formulaCancel?.removeEventListener('click', doCancel);
      input.removeEventListener('keydown', handleKeydown);
    }

    selectors.formulaConfirm?.addEventListener('click', doInsert);
    selectors.formulaCancel?.addEventListener('click', doCancel);
    input.addEventListener('keydown', handleKeydown);
  }

  /**
   * Shows the draft restore confirm modal. Returns promise<boolean>.
   */
  function showDraftRestoreModal() {
    return new Promise(resolve => {
      const overlay = selectors.draftRestoreOverlay;
      if (!overlay) {
        resolve(window.confirm('Continue your unsaved draft?\n\nOK = Continue draft\nCancel = Start a new deck'));
        return;
      }
      overlay.classList.remove('hidden');

      function cleanup() {
        selectors.draftRestoreContinue?.removeEventListener('click', onContinue);
        selectors.draftRestoreDiscard?.removeEventListener('click', onDiscard);
        overlay.classList.add('hidden');
      }
      function onContinue() { cleanup(); resolve(true); }
      function onDiscard() { cleanup(); resolve(false); }

      selectors.draftRestoreContinue?.addEventListener('click', onContinue);
      selectors.draftRestoreDiscard?.addEventListener('click', onDiscard);
    });
  }

  function openStudyOrderModal() {
    const overlay = document.getElementById('study-order-overlay');
    const cancelBtn = document.getElementById('study-order-cancel');
    if (!overlay) return;

    const currentOrder = normalizeNormalStudyOrder(state.settings?.normalStudyOrder);
    const optionButtons = Array.from(overlay.querySelectorAll('.mobile-modal-option-btn'));
    
    // Highlight the current active choice
    optionButtons.forEach(btn => {
      btn.classList.toggle('selected', btn.dataset.value === currentOrder);
    });

    overlay.classList.remove('hidden');

    function close() {
      overlay.classList.add('hidden');
      cleanup();
      state.lastModalClosedAt = Date.now();
    }

    async function handleSelect(event) {
      const btn = event.target.closest('[data-value]');
      if (!btn) return;
      
      const nextOrder = btn.dataset.value;
      state.settings = {
        ...(state.settings || {}),
        normalStudyOrder: nextOrder
      };
      
      playClick();
      close();
      renderMore();

      try {
        await window.flashcardStore.saveSettings(state.settings);
        showToast(
          nextOrder === 'forward'
            ? 'Normal study starts at the beginning'
            : nextOrder === 'backward'
              ? 'Normal study starts at the end'
              : 'Normal study randomizes every session'
        );
      } catch (error) {
        console.error('Could not save study order:', error);
        showToast('Could not save study order');
      }
    }

    function cleanup() {
      optionButtons.forEach(btn => btn.removeEventListener('click', handleSelect));
      cancelBtn?.removeEventListener('click', close);
    }

    optionButtons.forEach(btn => btn.addEventListener('click', handleSelect));
    cancelBtn?.addEventListener('click', close);
  }

  function openThemeSelectModal() {
    const overlay = document.getElementById('theme-select-overlay');
    const cancelBtn = document.getElementById('theme-select-cancel');
    if (!overlay) return;

    const currentTheme = state.settings?.theme || 'dark';
    const optionButtons = Array.from(overlay.querySelectorAll('.mobile-modal-option-btn'));
    
    // Highlight the current active choice
    optionButtons.forEach(btn => {
      btn.classList.toggle('selected', btn.dataset.value === currentTheme);
    });

    overlay.classList.remove('hidden');

    function close() {
      overlay.classList.add('hidden');
      cleanup();
      state.lastModalClosedAt = Date.now();
    }

    async function handleSelect(event) {
      const btn = event.target.closest('[data-value]');
      if (!btn) return;
      
      const nextTheme = btn.dataset.value;
      localStorage.setItem('erudite-theme', nextTheme);
      state.settings = {
        ...(state.settings || {}),
        theme: nextTheme
      };
      
      document.body.classList.toggle('theme-light', nextTheme === 'light');
      document.documentElement.classList.toggle('theme-light', nextTheme === 'light');
      configureSystemBars().catch(() => {});
      
      playClick();
      close();
      renderMore();

      try {
        await window.flashcardStore.saveSettings(state.settings);
      } catch (err) {
        console.warn('[mobile] Could not save theme:', err);
      }
    }

    function cleanup() {
      optionButtons.forEach(btn => btn.removeEventListener('click', handleSelect));
      cancelBtn?.removeEventListener('click', close);
    }

    optionButtons.forEach(btn => btn.addEventListener('click', handleSelect));
    cancelBtn?.addEventListener('click', close);
  }

  /**
   * Parses a separator string, supporting \n, \t escape sequences.
   */
  function parseSeparator(raw) {
    return String(raw || '')
      .replace(/\\n/g, '\n')
      .replace(/\\t/g, '\t')
      || ';';
  }

  /**
   * Opens the copy-export modal and populates it with current decks.
   */
  async function openCopyExportModal() {
    const overlay = selectors.copyExportOverlay;
    if (!overlay) return;
    // Populate deck dropdown
    const deckSelect = selectors.copyExportDeck;
    if (deckSelect) {
      deckSelect.innerHTML = state.sets.map(s =>
        `<option value="${escapeAttr(String(s.id))}">${escapeHtml(s.name || 'Untitled')}</option>`
      ).join('');
    }
    if (selectors.copyExportText) selectors.copyExportText.value = '';
    if (selectors.copyExportCopy) selectors.copyExportCopy.style.display = 'none';
    overlay.classList.remove('hidden');

    function doGenerate() {
      const setId = selectors.copyExportDeck?.value;
      const set = state.sets.find(s => String(s.id) === String(setId));
      if (!set) { showToast('Select a deck'); return; }
      const termSep = parseSeparator(selectors.copyExportTermSep?.value || ';');
      const cardSep = parseSeparator(selectors.copyExportCardSep?.value || '@');
      // Need full set with cards - fetch it
      window.flashcardStore.getSet(setId).then(fullSet => {
        const cards = (fullSet?.cards || set.cards || []);
        const text = cards
          .filter(c => c.term || c.definition)
          .map(c => {
            const term = String(c.term || '').replace(/<[^>]+>/g, '').trim();
            const def = String(c.definition || '').replace(/<[^>]+>/g, '').trim();
            return `${term}${termSep}${def}`;
          })
          .join(cardSep);
        if (selectors.copyExportText) selectors.copyExportText.value = text;
        if (selectors.copyExportCopy) selectors.copyExportCopy.style.display = '';
      }).catch(() => showToast('Could not load deck'));
    }

    async function doCopy() {
      const text = selectors.copyExportText?.value || '';
      if (!text) return;
      try {
        await navigator.clipboard.writeText(text);
        showToast('Copied to clipboard!');
      } catch (_) {
        // Fallback: select all text in textarea
        selectors.copyExportText?.select();
        document.execCommand('copy');
        showToast('Copied!');
      }
    }

    function doClose() {
      overlay.classList.add('hidden');
      cleanup();
      state.lastModalClosedAt = Date.now();
    }

    function cleanup() {
      selectors.copyExportGenerate?.removeEventListener('click', doGenerate);
      selectors.copyExportCopy?.removeEventListener('click', doCopy);
      selectors.copyExportCancel?.removeEventListener('click', doClose);
    }
    selectors.copyExportGenerate?.addEventListener('click', doGenerate);
    selectors.copyExportCopy?.addEventListener('click', doCopy);
    selectors.copyExportCancel?.addEventListener('click', doClose);
  }

  function updatePasteImportClassTrigger() {
    const triggerLabel = document.getElementById('mobile-paste-import-class-label');
    if (triggerLabel) {
      const currentClass = state.classes.find(item => String(item.id) === String(state.pasteImportClassId || ''));
      triggerLabel.textContent = currentClass ? currentClass.name : 'General';
    }
  }

  /**
   * Opens the paste-import modal.
   */
  function openPasteImportModal() {
    const overlay = selectors.pasteImportOverlay;
    if (!overlay) return;
    if (selectors.pasteImportText) selectors.pasteImportText.value = '';
    if (selectors.pasteImportName) selectors.pasteImportName.value = '';
    if (selectors.pasteImportTermSep) selectors.pasteImportTermSep.value = state.settings?.importTermSep || ';';
    if (selectors.pasteImportCardSep) selectors.pasteImportCardSep.value = state.settings?.importCardSep || '@';
    
    state.pasteImportClassId = ''; // default to General
    updatePasteImportClassTrigger();

    if (selectors.pasteImportPreset) selectors.pasteImportPreset.value = 'standard';
    updatePasteImportPresetLabel();
    if (selectors.pasteImportSeparatorRow) selectors.pasteImportSeparatorRow.style.display = 'none';

    updateTextareaPlaceholder();
    updateLivePreview();
    overlay.classList.remove('hidden');

    function parseInputToCards() {
      const text = String(selectors.pasteImportText?.value || '').trim();
      if (!text) return [];

      const preset = selectors.pasteImportPreset?.value || 'standard';
      let termSep = ';';
      let cardSep = '@';

      if (preset === 'custom') {
        termSep = parseSeparator(selectors.pasteImportTermSep?.value || ';');
        cardSep = parseSeparator(selectors.pasteImportCardSep?.value || '@');
      } else if (preset === 'standard') {
        termSep = ';';
        cardSep = '@';
      } else if (preset === 'newline-semicolon') {
        termSep = ';';
        cardSep = '\n';
      } else if (preset === 'newline-dash') {
        termSep = '-';
        cardSep = '\n';
      } else if (preset === 'newline-colon') {
        termSep = ':';
        cardSep = '\n';
      }

      return text.split(cardSep)
        .map(chunk => {
          if (!chunk.trim()) return null;
          const idx = chunk.indexOf(termSep);
          if (idx < 0) return null;
          const term = chunk.slice(0, idx).trim();
          const definition = chunk.slice(idx + termSep.length).trim();
          if (!term && !definition) return null;
          return { term, definition };
        })
        .filter(Boolean);
    }

    function updateLivePreview() {
      const previewCardsContainer = document.getElementById('mobile-paste-preview-cards');
      const previewCountLabel = document.getElementById('mobile-paste-preview-count');
      if (!previewCardsContainer || !previewCountLabel) return;

      const parsedCards = parseInputToCards();
      previewCountLabel.textContent = `(${parsedCards.length} ${parsedCards.length === 1 ? 'card' : 'cards'})`;

      if (!parsedCards.length) {
        previewCardsContainer.innerHTML = `<div style="text-align: center; color: var(--text-muted, #94a3b8); font-size: 0.85rem; padding: 1.25rem 0; border: 1px dashed var(--border, rgba(255, 255, 255, 0.1)); border-radius: 0.5rem; background: rgba(255,255,255,0.01);">Type or paste text above to see preview</div>`;
        return;
      }

      const maxToShow = 15;
      const itemsHtml = parsedCards.slice(0, maxToShow).map(card => `
        <div class="mobile-preview-card-item" style="padding: 0.5rem 0.75rem; border-radius: 0.5rem; background: var(--surface-hover, rgba(255, 255, 255, 0.03)); border: 1px solid var(--border, rgba(255, 255, 255, 0.08)); font-size: 0.85rem; display: flex; flex-direction: column; gap: 0.2rem; margin-bottom: 0.15rem;">
          <div style="font-weight: 700; color: var(--text);"><span style="color: var(--primary, #3b82f6); font-size: 0.75rem; font-weight: 900; margin-right: 0.25rem;">Q:</span> ${escapeHtml(card.term)}</div>
          <div style="color: var(--text-muted, #94a3b8);"><span style="color: #10b981; font-size: 0.75rem; font-weight: 900; margin-right: 0.25rem;">A:</span> ${escapeHtml(card.definition)}</div>
        </div>
      `).join('');

      let suffixHtml = '';
      if (parsedCards.length > maxToShow) {
        suffixHtml = `<div style="text-align: center; font-size: 0.8rem; color: var(--text-muted); font-weight: 600; padding: 0.3rem 0;">+ ${parsedCards.length - maxToShow} more cards</div>`;
      }

      previewCardsContainer.innerHTML = itemsHtml + suffixHtml;
    }

    function updateTextareaPlaceholder() {
      const preset = selectors.pasteImportPreset?.value || 'standard';
      if (!selectors.pasteImportText) return;

      if (preset === 'standard') {
        selectors.pasteImportText.placeholder = "Paste your cards here…\nExample:\nterm1;definition1@term2;definition2...";
      } else if (preset === 'newline-semicolon') {
        selectors.pasteImportText.placeholder = "Paste your cards here…\nExample:\nterm1;definition1\nterm2;definition2...";
      } else if (preset === 'newline-dash') {
        selectors.pasteImportText.placeholder = "Paste your cards here…\nExample:\nterm1 - definition1\nterm2 - definition2...";
      } else if (preset === 'newline-colon') {
        selectors.pasteImportText.placeholder = "Paste your cards here…\nExample:\nterm1: definition1\nterm2: definition2...";
      } else {
        const tSep = selectors.pasteImportTermSep?.value || ';';
        const cSep = selectors.pasteImportCardSep?.value || '@';
        selectors.pasteImportText.placeholder = `Paste your cards here…\nExample:\nterm1${tSep}definition1${cSep}term2${tSep}definition2...`;
      }
    }

    function handlePresetChange() {
      const preset = selectors.pasteImportPreset?.value || 'standard';
      if (selectors.pasteImportSeparatorRow) {
        selectors.pasteImportSeparatorRow.style.display = preset === 'custom' ? 'flex' : 'none';
      }
      updateTextareaPlaceholder();
      updateLivePreview();
      updatePasteImportPresetLabel();
    }

    async function doImport() {
      const name = String(selectors.pasteImportName?.value || '').trim() || 'Imported Deck';
      const parsedCards = parseInputToCards();
      if (!parsedCards.length) { showToast('No valid term/definition pairs found'); return; }

      const creatorCards = parsedCards.map(c => ({
        ...emptyCreatorCard(),
        term: c.term,
        definition: c.definition
      }));

      try {
        const classId = state.pasteImportClassId || null;
        const set = { name, cards: creatorCards, classId };
        await window.flashcardStore.saveSet(set);
        overlay.classList.add('hidden');
        state.lastModalClosedAt = Date.now();
        cleanup();
        setActiveTab('library');
        await refresh();
        showToast(`Imported ${plural(creatorCards.length, 'card')}`);
      } catch (err) {
        console.error(err);
        showToast('Import failed');
      }
    }

    function doCancel() {
      overlay.classList.add('hidden');
      cleanup();
      state.lastModalClosedAt = Date.now();
    }

    function cleanup() {
      selectors.pasteImportConfirm?.removeEventListener('click', doImport);
      selectors.pasteImportCancel?.removeEventListener('click', doCancel);
      selectors.pasteImportPreset?.removeEventListener('change', handlePresetChange);
      selectors.pasteImportText?.removeEventListener('input', updateLivePreview);
      selectors.pasteImportTermSep?.removeEventListener('input', updateLivePreview);
      selectors.pasteImportCardSep?.removeEventListener('input', updateLivePreview);
    }
    selectors.pasteImportConfirm?.addEventListener('click', doImport);
    selectors.pasteImportCancel?.addEventListener('click', doCancel);
    selectors.pasteImportPreset?.addEventListener('change', handlePresetChange);
    selectors.pasteImportText?.addEventListener('input', updateLivePreview);
    selectors.pasteImportTermSep?.addEventListener('input', updateLivePreview);
    selectors.pasteImportCardSep?.addEventListener('input', updateLivePreview);
  }

  // ─── Capacitor Back Button (double-press to exit) ────────────────────────

  let lastBackPressTime = 0;

  function setupCapacitorBackButton() {
    if (typeof window.Capacitor === 'undefined' || !window.Capacitor?.Plugins?.App) return;
    const { App } = window.Capacitor.Plugins;
    App.addListener('backButton', () => {
      // 1. Close any open custom modals first
      const openOverlays = Array.from(document.querySelectorAll('.mobile-modal-overlay:not(.hidden), .compact-floating-modal:not(.hidden)'));
      if (openOverlays.length > 0) {
        openOverlays.forEach(el => el.classList.add('hidden'));
        state.lastModalClosedAt = Date.now();
        return;
      }
      // 2. Close deck context modal if open
      const deckCtx = document.getElementById('deck-context-modal');
      if (deckCtx && deckCtx.style.display !== 'none') {
        closeDeckContextModal();
        return;
      }
      // 3. Close class select modal
      const classSelect = document.getElementById('class-select-modal');
      if (classSelect && classSelect.style.display !== 'none') {
        classSelect.style.display = 'none';
        state.lastModalClosedAt = Date.now();
        return;
      }
      // 4. Exit select mode
      if (state.selectMode) {
        exitSelectMode();
        return;
      }
      // 5. If in create tab, go to library
      if (state.activeTab === 'create') {
        setActiveTab('library');
        return;
      }
      // 6. If not on today tab, switch to today
      if (state.activeTab !== 'today') {
        setActiveTab('today');
        return;
      }
      // 7. On main screen: double-press to exit
      const now = Date.now();
      if (now - lastBackPressTime < 2000) {
        App.exitApp();
      } else {
        lastBackPressTime = now;
        showToast('Press back again to exit');
      }
    });
  }

  async function exportBackup() {
    try {
      const result = await window.flashcardStore.exportBackup();
      if (!result?.canceled) showToast('Backup exported');
    } catch (error) {
      console.error(error);
      showToast('Export failed');
    }
  }

  async function importBackup() {
    try {
      const result = await window.flashcardStore.importBackup();
      if (!result?.canceled) {
        showMicroLoader('Restoring library...');
        try {
          showToast(`Restored ${result.setCount || 0} decks`);
          await refresh();
        } finally {
          hideMicroLoader();
        }
      }
    } catch (error) {
      console.error(error);
      showToast('Import failed');
    }
  }

  async function reviewDue(options = {}) {
    const force = Boolean(options.force || !state.srsMode);
    const first = dueSets({ force })[0]?.set;
    if (!first) {
      showToast('No reviews due');
      return;
    }
    if (!state.srsMode) {
      persistSrsMode(true);
      render();
    }
    await flushStore(500);
    navigateTo(mobileStudyUrl(first.id, { reviewDue: true, srsMode: true }), {
      title: 'Opening Review',
      copy: 'Finding cards due now'
    });
  }

  async function reviewDueSmart() {
    const first = dueSets({ force: true })[0]?.set;
    if (!first) {
      showToast('No reviews due');
      return;
    }
    if (!state.srsMode) {
      persistSrsMode(true);
      render();
    }
    playClick();
    await flushStore(500);
    navigateTo(mobileStudyUrl(first.id, { reviewDue: true, srsMode: true }), {
      title: 'Opening Review',
      copy: 'Finding cards due now'
    });
  }

  function updateFormatState() {
    if (!selectors.creatorCards) return;
    const activeEditor = document.activeElement?.closest?.('.rich-editor');
    selectors.creatorCards.querySelectorAll('[data-creator-action="format"]').forEach(button => {
      const command = button.dataset.command;
      const active = Boolean(activeEditor && command && command !== 'formula' && document.queryCommandState(command));
      button.classList.toggle('active', active);
    });
  }

  function scheduleFormatStateUpdate() {
    if (formatStateFrame) return;
    formatStateFrame = requestAnimationFrame(() => {
      formatStateFrame = 0;
      updateFormatState();
    });
  }

  async function handleCreatorAction(action, target) {
    switch (action) {
      case 'add-card': {
        syncCreatorFromDom();
        const card = emptyCreatorCard();
        state.creator.cards.push(card);
        renderCreate();
        scheduleCreatorDraftSave();
        requestAnimationFrame(() => {
          const newCardEl = selectors.creatorCards?.querySelector(`[data-editor-id="${cssEscape(card.id)}"][data-side="term"]`);
          if (newCardEl) {
            newCardEl.focus();
            // Scroll the new card smoothly into view
            newCardEl.closest('.creator-card')?.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
          }
        });
        break;
      }
      case 'delete-card': {
        syncCreatorFromDom();
        state.creator.cards = state.creator.cards.filter(card => String(card.id) !== String(target.dataset.cardId));
        ensureCreatorCard();
        renderCreate();
        scheduleCreatorDraftSave();
        break;
      }
      case 'format': {
        const command = target.dataset.command;
        if (!command) break;
        if (command === 'formula') {
          // Use custom HTML modal instead of window.prompt
          openFormulaModal(savedRange => {
            if (savedRange) {
              const sel = window.getSelection();
              sel.removeAllRanges();
              sel.addRange(savedRange);
            }
          });
        } else {
          document.execCommand(command, false, null);
        }
        updateFormatState();
        scheduleCreatorDraftSave();
        break;
      }
      case 'media':
        state.pendingImageTarget = {
          cardId: target.dataset.cardId,
          side: target.dataset.side === 'definition' ? 'definition' : 'term',
          mode: 'media'
        };
        selectors.imageInput?.click();
        break;
      case 'background':
        state.pendingImageTarget = {
          cardId: target.dataset.cardId,
          side: target.dataset.side === 'definition' ? 'definition' : 'term',
          mode: 'background'
        };
        selectors.backgroundInput?.click();
        break;
      case 'remove-image': {
        syncCreatorFromDom();
        const key = target.dataset.side === 'definition' ? 'definitionImage' : 'termImage';
        state.creator.cards = state.creator.cards.map(card => (
          String(card.id) === String(target.dataset.cardId) ? { ...card, [key]: '' } : card
        ));
        renderCreate();
        scheduleCreatorDraftSave();
        break;
      }
      case 'remove-media': {
        syncCreatorFromDom();
        const side = target.dataset.side === 'definition' ? 'definition' : 'term';
        const mediaId = target.dataset.mediaId;
        state.creator.cards = state.creator.cards.map(card => {
          if (String(card.id) !== String(target.dataset.cardId)) return card;
          const media = normalizeCardMedia(card);
          return {
            ...card,
            media: {
              ...media,
              [side]: (media[side] || []).filter(item => String(item.id) !== String(mediaId))
            }
          };
        });
        renderCreate();
        scheduleCreatorDraftSave();
        break;
      }
      case 'remove-background': {
        syncCreatorFromDom();
        const side = target.dataset.side === 'definition' ? 'definition' : 'term';
        state.creator.cards = state.creator.cards.map(card => {
          if (String(card.id) !== String(target.dataset.cardId)) return card;
          const background = normalizeCardBackground(card);
          return {
            ...card,
            background: {
              ...background,
              [side]: null
            }
          };
        });
        renderCreate();
        scheduleCreatorDraftSave();
        break;
      }
      case 'import-txt':
        selectors.txtInput?.click();
        break;
      default:
        break;
    }
  }

  async function handleAction(action, target) {
    switch (action) {
      case 'tab-library': {
        setActiveTab('library');
        const btnLibrary = document.querySelector('.source-option[data-action="tab-library"]');
        const btnPremade = document.querySelector('.source-option[data-action="open-premade"]');
        if (btnLibrary) {
          btnLibrary.classList.add('active');
          btnLibrary.setAttribute('aria-checked', 'true');
        }
        if (btnPremade) {
          btnPremade.classList.remove('active');
          btnPremade.setAttribute('aria-checked', 'false');
        }
        document.getElementById('mobile-user-decks-view')?.classList.remove('hidden');
        document.getElementById('mobile-premade-decks-view')?.classList.add('hidden');
        const btnCreate = document.querySelector('[data-action="open-create"]');
        if (btnCreate) btnCreate.classList.remove('hidden');
        break;
      }
      case 'open-create':
        await openCreator();
        break;
      case 'open-premade': {
        setActiveTab('library');
        const btnLibrary = document.querySelector('.source-option[data-action="tab-library"]');
        const btnPremade = document.querySelector('.source-option[data-action="open-premade"]');
        if (btnLibrary) {
          btnLibrary.classList.remove('active');
          btnLibrary.setAttribute('aria-checked', 'false');
        }
        if (btnPremade) {
          btnPremade.classList.add('active');
          btnPremade.setAttribute('aria-checked', 'true');
        }
        document.getElementById('mobile-user-decks-view')?.classList.add('hidden');
        document.getElementById('mobile-premade-decks-view')?.classList.remove('hidden');
        const btnCreate = document.querySelector('[data-action="open-create"]');
        if (btnCreate) btnCreate.classList.add('hidden');
        await loadPremade();
        break;
      }
      case 'open-browser':
        setActiveTab('browser');
        await loadBrowserCards();
        renderBrowser();
        break;
      case 'open-backup':
        setActiveTab('more');
        break;
      case 'open-settings':
        setActiveTab('more');
        break;
      case 'review-due':
        await reviewDue();
        break;
      case 'review-due-smart':
        await reviewDueSmart();
        break;
      case 'toggle-srs':
        await toggleSrs();
        break;
      case 'toggle-pin':
        await togglePin(target.dataset.setId);
        break;
      case 'delete-set':
        await deleteSet(target.dataset.setId);
        break;
      case 'delete-class':
        await deleteClass(target.dataset.classId);
        break;
      case 'edit-class':
        await editClass(target.dataset.classId);
        break;
      case 'select-study-order':
        openStudyOrderModal();
        break;
      case 'select-theme':
        openThemeSelectModal();
        break;
      case 'study-set':
        showAppLoader('Opening Study', 'Preparing your deck');
        await new Promise(resolve => setTimeout(resolve, 50));
        await flushStore(1200);
        navigateTo(mobileStudyUrl(target.dataset.setId || '', { srsMode: state.srsMode }), {
          title: 'Opening Study',
          copy: 'Preparing your deck'
        });
        break;
      case 'edit-set':
        await loadSetIntoCreator(target.dataset.setId);
        break;
      case 'open-class':
        state.libraryFilter = `class:${target.dataset.classId}`;
        state.activeTab = 'library';
        playClick();
        setActiveTab('library');
        break;
      case 'filter-classes':
        state.libraryFilter = 'classes';
        renderLibrary();
        break;
      case 'cycle-sort': {
        const available = state.srsMode ? sortOrder : sortOrder.filter(item => item !== 'due');
        const index = available.indexOf(state.sort);
        state.sort = available[(index + 1) % available.length] || 'recent';
        playClick();
        renderLibrary();
        break;
      }
      case 'premade-class':
        state.premadeClass = target.dataset.classId || '10th';
        state.premadeSubject = (premadeSubjects[state.premadeClass] || [])[0] || '';
        playClick();
        renderPremade();
        await loadPremade();
        break;
      case 'premade-subject':
        state.premadeSubject = target.dataset.subjectId || '';
        playClick();
        renderPremade();
        await loadPremade();
        break;
      case 'import-premade':
        await importPremade(target.dataset.file || '');
        break;
      case 'export-backup':
        await exportBackup();
        break;
      case 'import-backup':
        await importBackup();
        break;
      case 'copy-export':
        await openCopyExportModal();
        break;
      case 'paste-import':
        openPasteImportModal();
        break;
      default:
        break;
    }
  }

  // --- Long Press & Multi-Select Logic ---
  let longPressTimer = null;
  let longPressTarget = null;
  let isLongPress = false;
  let startX = 0;
  let startY = 0;
  let activeContextDeckId = null;

  function handlePointerDown(e) {
    if (Date.now() - (state.lastModalClosedAt || 0) < 350) {
      return;
    }

    const deckRow = e.target.closest('.deck-row');
    if (!deckRow) return;

    if (state.selectMode) {
      return; // Handled by click event
    }

    if (e.target.closest('button') || e.target.closest('a')) {
      return;
    }

    longPressTarget = deckRow;
    isLongPress = false;
    startX = e.clientX;
    startY = e.clientY;

    deckRow.classList.add('long-pressing');

    longPressTimer = setTimeout(() => {
      isLongPress = true;
      deckRow.classList.remove('long-pressing');
      const setId = deckRow.dataset.setCard;
      openDeckContextModal(setId);
    }, 600);
  }

  async function handlePointerUp(e) {
    if (longPressTimer) {
      clearTimeout(longPressTimer);
      longPressTimer = null;
    }
    if (longPressTarget) {
      longPressTarget.classList.remove('long-pressing');
      
      if (!isLongPress && !state.selectMode) {
        const setId = longPressTarget.dataset.setCard;
        showAppLoader('Opening Study', 'Preparing your deck');
        await new Promise(resolve => setTimeout(resolve, 50));
        await flushStore(1200);
        navigateTo(mobileStudyUrl(setId || '', { srsMode: state.srsMode }), {
          title: 'Opening Study',
          copy: 'Preparing your deck'
        });
      }
      longPressTarget = null;
    }
  }

  function handlePointerMove(e) {
    if (longPressTarget) {
      const diffX = Math.abs(e.clientX - startX);
      const diffY = Math.abs(e.clientY - startY);
      if (diffX > 10 || diffY > 10) {
        clearTimeout(longPressTimer);
        longPressTimer = null;
        longPressTarget.classList.remove('long-pressing');
        longPressTarget = null;
      }
    }
  }

  function handlePointerCancel(e) {
    if (longPressTimer) {
      clearTimeout(longPressTimer);
      longPressTimer = null;
    }
    if (longPressTarget) {
      longPressTarget.classList.remove('long-pressing');
      longPressTarget = null;
    }
  }

  function openDeckContextModal(setId) {
    const set = state.sets.find(item => String(item.id) === String(setId));
    if (!set) return;

    activeContextDeckId = setId;

    const modal = document.getElementById('deck-context-modal');
    const titleLabel = document.getElementById('context-deck-title');
    if (modal && titleLabel) {
      titleLabel.textContent = set.name || 'Untitled Set';
      modal.style.display = 'flex';
      playClick();
    }
  }

  function closeDeckContextModal() {
    const modal = document.getElementById('deck-context-modal');
    if (modal) {
      modal.style.display = 'none';
    }
    activeContextDeckId = null;
    state.lastModalClosedAt = Date.now();
  }

  function enterSelectMode(initialSetId) {
    state.selectMode = true;
    state.selectedDecks = new Set();
    if (initialSetId) {
      state.selectedDecks.add(String(initialSetId));
    }
    
    const bar = document.getElementById('selection-bar');
    if (bar) bar.style.display = 'flex';
    
    const tabbar = document.querySelector('.mobile-tabbar');
    if (tabbar) tabbar.style.display = 'none';

    document.querySelectorAll('.deck-row').forEach(row => {
      const setId = String(row.dataset.setCard);
      row.classList.toggle('selected', state.selectedDecks.has(setId));
      const actions = row.querySelector('.deck-actions');
      if (actions) actions.style.display = 'none';
    });

    updateSelectionBar();
  }

  function exitSelectMode() {
    state.selectMode = false;
    state.selectedDecks = new Set();

    const bar = document.getElementById('selection-bar');
    if (bar) bar.style.display = 'none';

    const tabbar = document.querySelector('.mobile-tabbar');
    if (tabbar) tabbar.style.display = 'grid';

    document.querySelectorAll('.deck-row').forEach(row => {
      row.classList.remove('selected');
      const actions = row.querySelector('.deck-actions');
      if (actions) actions.style.display = '';
    });
  }

  function toggleDeckSelection(setId) {
    if (!state.selectedDecks) {
      state.selectedDecks = new Set();
    }
    const idStr = String(setId);
    if (state.selectedDecks.has(idStr)) {
      state.selectedDecks.delete(idStr);
    } else {
      state.selectedDecks.add(idStr);
    }
    
    document.querySelectorAll('.deck-row').forEach(row => {
      if (String(row.dataset.setCard) === idStr) {
        row.classList.toggle('selected', state.selectedDecks.has(idStr));
      }
    });

    updateSelectionBar();
  }

  function updateSelectionBar() {
    const count = state.selectedDecks ? state.selectedDecks.size : 0;
    const countLabel = document.getElementById('selection-count');
    if (countLabel) {
      countLabel.textContent = `${count} ${count === 1 ? 'deck' : 'decks'} selected`;
    }
  }

  async function deleteSelectedDecks() {
    if (!state.selectedDecks || !state.selectedDecks.size) return;
    
    const count = state.selectedDecks.size;
    const ok = await showMobileConfirm({
      title: 'Delete Decks',
      message: `Are you sure you want to delete ${count} selected ${count === 1 ? 'deck' : 'decks'}? This cannot be undone.`,
      okText: 'Delete',
      isDanger: true
    });
    if (!ok) return;

    state.busy = true;
    try {
      for (const setId of state.selectedDecks) {
        await window.flashcardStore.deleteSet(setId);
      }
      showToast(`${count} ${count === 1 ? 'deck' : 'decks'} deleted`);
      exitSelectMode();
      await refresh();
    } catch (error) {
      console.error(error);
      showToast('Could not delete some decks');
    } finally {
      state.busy = false;
    }
  }

  function installEvents() {
    document.addEventListener('pointerdown', event => {
      if (event.target.closest('[data-creator-action="format"]')) {
        event.preventDefault();
      }
    });

    document.addEventListener('click', async event => {
      // Global haptic feedback for click operations
      const clickable = event.target.closest('button, [role="button"], .tab-button, .deck-row, .settings-row, .context-option-row, .mobile-modal-option-btn, .rating-btn, .class-card-click-area, .class-delete-btn, .class-edit-btn, .format-button, .compact-action, .primary-action, .secondary-action, .small-icon-button, .creator-bottom-add');
      if (clickable) {
        triggerHaptic();
      }

      if (state.selectMode) {
        const deckRow = event.target.closest('.deck-row');
        if (deckRow) {
          event.preventDefault();
          event.stopPropagation();
          toggleDeckSelection(deckRow.dataset.setCard);
          return;
        }
      }

      const creatorTarget = event.target.closest('[data-creator-action]');
      if (creatorTarget) {
        event.preventDefault();
        await handleCreatorAction(creatorTarget.dataset.creatorAction, creatorTarget);
        return;
      }

      const actionTarget = event.target.closest('[data-action]');
      if (actionTarget) {
        event.preventDefault();
        if (state.busy) return;
        state.busy = true;
        try {
          await handleAction(actionTarget.dataset.action, actionTarget);
        } finally {
          state.busy = false;
        }
        return;
      }

      const tab = event.target.closest('[data-tab]');
      if (tab) {
        event.preventDefault();
        playClick();
        if (tab.dataset.tab === 'create' && state.activeTab !== 'create') {
          await openCreator();
          return;
        }
        setActiveTab(tab.dataset.tab);
        return;
      }

      // 1. Custom Class Select Trigger click
      const classTrigger = event.target.closest('#mobile-create-class-trigger');
      if (classTrigger) {
        event.preventDefault();
        playClick();
        openClassSelectModal(
          state.creator.classId || '',
          (classId) => {
            state.creator.classId = classId;
            renderCreate();
            scheduleCreatorDraftSave();
          },
          async () => {
            await createClassFromCreator();
          }
        );
        return;
      }

      const pasteClassTrigger = event.target.closest('#mobile-paste-import-class-trigger');
      if (pasteClassTrigger) {
        event.preventDefault();
        playClick();
        openClassSelectModal(
          state.pasteImportClassId || '',
          (classId) => {
            state.pasteImportClassId = classId;
            updatePasteImportClassTrigger();
          },
          async () => {
            await createClassFromCreator();
          }
        );
        return;
      }

      const pastePresetTrigger = event.target.closest('#mobile-paste-import-preset-trigger');
      if (pastePresetTrigger) {
        event.preventDefault();
        playClick();
        openPresetSelectModal();
        return;
      }

      const presetBackdrop = event.target.closest('#preset-select-backdrop');
      if (presetBackdrop) {
        event.preventDefault();
        playClick();
        selectors.presetSelectModal?.classList.add('hidden');
        state.lastModalClosedAt = Date.now();
        return;
      }

      const presetOpt = event.target.closest('[data-preset-val]');
      if (presetOpt && event.target.closest('#preset-select-options')) {
        event.preventDefault();
        playClick();
        const siblings = presetOpt.parentElement.querySelectorAll('.preset-option-btn');
        siblings.forEach(sibling => sibling.classList.remove('selected'));
        presetOpt.classList.add('selected');
        
        const selectedVal = presetOpt.dataset.presetVal || 'standard';
        
        setTimeout(() => {
          selectors.presetSelectModal?.classList.add('hidden');
          state.lastModalClosedAt = Date.now();
          if (selectors.pasteImportPreset) {
            selectors.pasteImportPreset.value = selectedVal;
            selectors.pasteImportPreset.dispatchEvent(new Event('change'));
          }
        }, 160);
        return;
      }

      // 2. Class select backdrop click
      const classBackdrop = event.target.closest('#class-select-backdrop');
      if (classBackdrop) {
        event.preventDefault();
        playClick();
        const modal = document.getElementById('class-select-modal');
        if (modal) {
          modal.style.display = 'none';
          state.lastModalClosedAt = Date.now();
        }
        return;
      }

      // 3. Class option selection click
      const classAction = event.target.closest('[data-class-action]');
      if (classAction && event.target.closest('#class-select-options')) {
        event.preventDefault();
        const modal = document.getElementById('class-select-modal');
        if (modal) {
          modal.style.display = 'none';
          state.lastModalClosedAt = Date.now();
        }
        if (classAction.dataset.classAction === 'new') {
          await createClassFromCreator();
        }
        return;
      }

      const classOpt = event.target.closest('[data-class-val]');
      if (classOpt && event.target.closest('#class-select-options')) {
        event.preventDefault();
        playClick();
        
        // Instant border highlight transfer
        const siblings = classOpt.parentElement.querySelectorAll('.context-option-row');
        siblings.forEach(sibling => sibling.classList.remove('selected-class-opt'));
        classOpt.classList.add('selected-class-opt');
        
        const selectedId = classOpt.dataset.classVal || '';
        
        // Delayed modal closure for tactile animation visibility
        setTimeout(() => {
          const modal = document.getElementById('class-select-modal');
          if (modal) {
            modal.style.display = 'none';
            state.lastModalClosedAt = Date.now();
          }
          if (state.classSelectCallbacks?.onSelect) {
            state.classSelectCallbacks.onSelect(selectedId);
          } else {
            state.creator.classId = selectedId;
            renderCreate();
            scheduleCreatorDraftSave();
          }
          state.classSelectCallbacks = null;
        }, 180);
        return;
      }

      // 4. Cancel selection button
      const cancelSel = event.target.closest('#btn-cancel-selection');
      if (cancelSel) {
        event.preventDefault();
        playClick();
        exitSelectMode();
        return;
      }

      // 5. Delete selected button
      const deleteSel = event.target.closest('#btn-delete-selected');
      if (deleteSel) {
        event.preventDefault();
        await deleteSelectedDecks();
        return;
      }

      // 6. Context backdrop click to cancel
      const ctxBackdrop = event.target.closest('#context-backdrop');
      if (ctxBackdrop) {
        event.preventDefault();
        playClick();
        closeDeckContextModal();
        return;
      }

      // 7. Context option - Delete
      const ctxDelete = event.target.closest('#context-opt-delete');
      if (ctxDelete) {
        event.preventDefault();
        if (activeContextDeckId) {
          const setId = activeContextDeckId;
          closeDeckContextModal();
          await deleteSet(setId);
        }
        return;
      }

      // 8. Context option - Select
      const ctxSelect = event.target.closest('#context-opt-select');
      if (ctxSelect) {
        event.preventDefault();
        if (activeContextDeckId) {
          const setId = activeContextDeckId;
          closeDeckContextModal();
          enterSelectMode(setId);
        }
        return;
      }

      // 8b. Context option - Reset Progress
      const ctxResetProgress = event.target.closest('#context-opt-reset-progress');
      if (ctxResetProgress) {
        event.preventDefault();
        if (activeContextDeckId) {
          const setId = activeContextDeckId;
          closeDeckContextModal();
          await resetNonSrsProgress(setId);
        }
        return;
      }

      // 8c. Context option - Reset SRS Data
      const ctxResetSrs = event.target.closest('#context-opt-reset-srs');
      if (ctxResetSrs) {
        event.preventDefault();
        if (activeContextDeckId) {
          const setId = activeContextDeckId;
          closeDeckContextModal();
          await executeDeckSrsReset(setId);
        }
        return;
      }

      // 9. Context option - Cancel
      const ctxCancel = event.target.closest('#context-opt-cancel');
      if (ctxCancel) {
        event.preventDefault();
        playClick();
        closeDeckContextModal();
        return;
      }

      // 10. Click outside modals / overlays to close them
      if (event.target.classList.contains('mobile-modal-overlay')) {
        event.preventDefault();
        event.stopPropagation();
        playClick();
        event.target.classList.add('hidden');
        state.lastModalClosedAt = Date.now();
        const cancelBtn = event.target.querySelector('.mobile-modal-btn.cancel, .cancel');
        if (cancelBtn) cancelBtn.click();
        return;
      }

      if (event.target.classList.contains('context-modal-backdrop')) {
        const parent = event.target.parentElement;
        if (parent && parent.classList.contains('deck-context-modal')) {
          event.preventDefault();
          event.stopPropagation();
          playClick();
          if (parent.id === 'mobile-class-editor-modal') {
            const cancelBtn = parent.querySelector('[data-class-editor-cancel]');
            if (cancelBtn) cancelBtn.click();
            else parent.remove();
          } else if (parent.id === 'deck-context-modal') {
            closeDeckContextModal();
          } else if (parent.id === 'class-select-modal') {
            parent.style.display = 'none';
          }
          return;
        }
      }
    });

    selectors.filters?.addEventListener('click', event => {
      const button = event.target.closest('[data-filter]');
      if (!button) return;
      state.libraryFilter = button.dataset.filter;
      playClick();
      renderLibrary();
    });

    selectors.searchInput?.addEventListener('input', event => {
      state.search = event.target.value || '';
      renderLibrary();
    });

    selectors.browserSearchInput?.addEventListener('input', event => {
      state.browserSearch = event.target.value || '';
      renderBrowser();
    });



    selectors.createForm?.addEventListener('input', event => {
      if (!event.target.closest('#view-create')) return;
      scheduleCreatorDraftSave();
    });



    selectors.createForm?.addEventListener('submit', async event => {
      event.preventDefault();
      if (state.creatorSaving) return;
      state.creatorSaving = true;
      try {
        await saveMobileDeck();
      } catch (error) {
        console.error('Could not save deck:', error);
        showToast(error?.message || 'Could not save deck');
      } finally {
        state.creatorSaving = false;
      }
    });

    selectors.imageInput?.addEventListener('change', async event => {
      const files = Array.from(event.target.files || []);
      const target = state.pendingImageTarget;
      event.target.value = '';
      state.pendingImageTarget = null;
      if (!files.length || !target) return;
      syncCreatorFromDom();
      try {
        const added = [];
        for (const file of files) {
          if (!file.type.startsWith('image/') && !file.type.startsWith('audio/') && !file.type.startsWith('video/')) continue;
          const src = await window.flashcardStore.saveImageFromFile(file, {
            deckId: state.creator.editingSetId || 'draft',
            side: target.side,
            prefix: `${target.side}-media`
          });
          added.push(window.EruditeMedia?.mediaItemFromSource
            ? window.EruditeMedia.mediaItemFromSource(src, file)
            : {
                id: `media-${Date.now()}-${Math.random().toString(36).slice(2)}`,
                kind: file.type.startsWith('audio/') ? 'audio' : file.type.startsWith('video/') ? 'video' : 'image',
                mime: file.type,
                name: file.name,
                src,
                created: Date.now()
              });
        }
        if (!added.length) {
          showToast('No supported media files selected');
          return;
        }
        state.creator.cards = state.creator.cards.map(card => (
          String(card.id) === String(target.cardId)
            ? {
                ...card,
                media: {
                  ...normalizeCardMedia(card),
                  [target.side]: [...(normalizeCardMedia(card)[target.side] || []), ...added]
                }
              }
            : card
        ));
        renderCreate();
        scheduleCreatorDraftSave();
        showToast(added.length === 1 ? 'Media added' : `${added.length} media files added`);
      } catch (error) {
        console.error(error);
        showToast('Could not add media');
      }
    });

    selectors.backgroundInput?.addEventListener('change', async event => {
      const file = event.target.files?.[0];
      const target = state.pendingImageTarget;
      event.target.value = '';
      state.pendingImageTarget = null;
      if (!file || !target) return;
      if (!file.type.startsWith('image/')) {
        showToast('Use an image for the background');
        return;
      }
      syncCreatorFromDom();
      try {
        const src = await window.flashcardStore.saveImageFromFile(file, {
          deckId: state.creator.editingSetId || 'draft',
          side: target.side,
          prefix: `${target.side}-background`
        });
        const backgroundItem = window.EruditeMedia?.normalizeCardBackground
          ? window.EruditeMedia.normalizeCardBackground({ [target.side]: { src, mime: file.type, name: file.name } })[target.side]
          : { src, mime: file.type, name: file.name, fit: 'cover', opacity: 0.32 };
        state.creator.cards = state.creator.cards.map(card => (
          String(card.id) === String(target.cardId)
            ? {
                ...card,
                background: {
                  ...normalizeCardBackground(card),
                  [target.side]: backgroundItem
                }
              }
            : card
        ));
        renderCreate();
        scheduleCreatorDraftSave();
        showToast('Background set');
      } catch (error) {
        console.error(error);
        showToast('Could not set background');
      }
    });

    selectors.txtInput?.addEventListener('change', async event => {
      const file = event.target.files?.[0];
      event.target.value = '';
      if (!file) return;
      try {
        const text = await file.text();
        const imported = parseBulkCards(text);
        if (!imported.length) {
          showToast('No Term;Definition pairs found');
          return;
        }
        syncCreatorFromDom();
        const existing = state.creator.cards.filter(hasCardContent);
        state.creator.cards = [...existing, ...imported];
        renderCreate();
        scheduleCreatorDraftSave();
        showToast(`Imported ${plural(imported.length, 'card')}`);
      } catch (error) {
        console.error(error);
        showToast('Could not import TXT');
      }
    });

    const headerSaveBtn = document.getElementById('header-creator-save-btn');
    if (headerSaveBtn) {
      headerSaveBtn.addEventListener('click', async event => {
        event.preventDefault();
        playClick();
        if (state.creatorSaving) return;
        state.creatorSaving = true;
        try {
          await saveMobileDeck();
        } catch (error) {
          console.error(error);
          showToast(error?.message || 'Could not save deck');
        } finally {
          state.creatorSaving = false;
        }
      });
    }

    document.addEventListener('selectionchange', scheduleFormatStateUpdate);

    const handleAppPause = async () => {
      if (state.activeTab === 'create') {
        await saveCreatorDraft({ persistStore: true, flush: true, flushTimeout: 900 }).catch(() => {});
      } else {
        await flushStore(900).catch(() => {});
      }
    };

    const handleAppResume = async () => {
      if (state.activeTab !== 'create') {
        await refresh();
      }
    };

    document.addEventListener('visibilitychange', () => {
      if (document.hidden) {
        handleAppPause().catch(() => {});
      } else {
        handleAppResume().catch(() => {});
      }
    });

    if (window.Capacitor?.Plugins?.App) {
      window.Capacitor.Plugins.App.addListener('appStateChange', ({ isActive }) => {
        if (!isActive) {
          handleAppPause().catch(() => {});
        } else {
          handleAppResume().catch(() => {});
        }
      });
    }

    // Pointer gesture listeners for long-press on library list
    if (selectors.libraryList) {
      selectors.libraryList.addEventListener('pointerdown', handlePointerDown);
      selectors.libraryList.addEventListener('pointerup', handlePointerUp);
      selectors.libraryList.addEventListener('pointermove', handlePointerMove);
      selectors.libraryList.addEventListener('pointercancel', handlePointerCancel);
    }

    // Card background opacity slider
    selectors.bgOpacitySlider?.addEventListener('input', async event => {
      const opacity = parseFloat(event.target.value);
      if (!Number.isFinite(opacity)) return;
      state.settings = { ...(state.settings || {}), cardBgOpacity: opacity };
      try {
        await window.flashcardStore.saveSettings(state.settings);
      } catch (err) {
        console.warn('[mobile] Could not save card bg opacity:', err);
      }
    });



    // Import Term Separator input
    selectors.importTermSepInput?.addEventListener('input', async event => {
      const val = event.target.value;
      state.settings = { ...(state.settings || {}), importTermSep: val };
      try {
        await window.flashcardStore.saveSettings(state.settings);
      } catch (err) {
        console.warn('[mobile] Could not save importTermSep:', err);
      }
    });

    // Import Card Separator input
    selectors.importCardSepInput?.addEventListener('input', async event => {
      const val = event.target.value;
      state.settings = { ...(state.settings || {}), importCardSep: val };
      try {
        await window.flashcardStore.saveSettings(state.settings);
      } catch (err) {
        console.warn('[mobile] Could not save importCardSep:', err);
      }
    });

    window.addEventListener('resize', () => {
      if (state.activeTab) {
        updateTabIndicator(state.activeTab);
      }
    });
  }

  function initSwipeNavigation() {
    let startX = 0;
    let startY = 0;
    let startTime = 0;
    const tabsOrder = ['today', 'library', 'create', 'more'];

    document.addEventListener('touchstart', (e) => {
      if (e.touches.length > 1) return;

      const target = e.target;
      
      // Exclude range inputs, horizontal filter strips, text inputs/textareas
      const ignoreSelector = 'input[type="range"], .mobile-opacity-slider, .filter-strip, .deck-source-switch, input[type="text"], input[type="search"], textarea';
      if (target.closest(ignoreSelector)) {
        return;
      }

      // Also exclude if inside any active popup/modal
      if (target.closest('.mobile-modal-overlay') || target.closest('.deck-context-modal') || target.closest('.micro-loader-overlay')) {
        return;
      }

      startX = e.touches[0].clientX;
      startY = e.touches[0].clientY;
      startTime = Date.now();
    }, { passive: true });

    document.addEventListener('touchend', (e) => {
      if (startX === 0 && startY === 0) return;

      const endX = e.changedTouches[0].clientX;
      const endY = e.changedTouches[0].clientY;
      const endTime = Date.now();

      const deltaX = endX - startX;
      const deltaY = endY - startY;
      const timeDiff = endTime - startTime;

      startX = 0;
      startY = 0;
      startTime = 0;

      const minDistance = 75;
      const maxTime = 400;

      if (Math.abs(deltaX) > minDistance && Math.abs(deltaX) > Math.abs(deltaY) * 1.8 && timeDiff < maxTime) {
        const currentIdx = tabsOrder.indexOf(state.activeTab);
        if (currentIdx === -1) return;

        if (deltaX > 0) {
          // Swipe right -> Previous Tab
          if (currentIdx > 0) {
            const prevTab = tabsOrder[currentIdx - 1];
            playClick();
            setActiveTab(prevTab);
          }
        } else {
          // Swipe left -> Next Tab
          if (currentIdx < tabsOrder.length - 1) {
            const nextTab = tabsOrder[currentIdx + 1];
            playClick();
            setActiveTab(nextTab);
          }
        }
      }
    }, { passive: true });

    document.addEventListener('touchcancel', () => {
      startX = 0;
      startY = 0;
      startTime = 0;
    }, { passive: true });
  }

  function updateDailyQuote() {
    const quotes = [
      "Discipline beats motivation.",
      "Study now, shine later.",
      "Consistency creates champions.",
      "Small steps, every day.",
      "Focus is a superpower.",
      "Success is rented daily.",
      "Results love repetition.",
      "Future you is watching.",
      "Don't wish. Work.",
      "Excuses kill dreams.",
      "Start before you're ready.",
      "Done is better than perfect.",
      "One chapter at a time.",
      "Stay patient and persistent.",
      "Progress over perfection.",
      "Action cures anxiety.",
      "Comfort is the enemy of growth.",
      "Discipline equals freedom.",
      "Keep showing up.",
      "Make today count.",
      "Be stronger than your excuses.",
      "Your habits build your future.",
      "Consistency compounds.",
      "Focus on the next step.",
      "Every page matters.",
      "Motivation starts, discipline finishes.",
      "Success leaves clues.",
      "The grind remembers.",
      "Outwork your yesterday.",
      "Difficult today, easier tomorrow.",
      "Master the basics relentlessly.",
      "The secret is consistency.",
      "Dream big, execute daily.",
      "Winners repeat boring things.",
      "Effort never betrays you.",
      "Keep promises to yourself.",
      "Learn, apply, repeat.",
      "Greatness grows quietly.",
      "A focused hour beats a distracted day.",
      "Discipline is self-respect in action.",
      "What you repeat, you become.",
      "The pain of regret lasts longer.",
      "Train your mind to obey.",
      "Success is a daily habit.",
      "The future rewards preparation.",
      "Show up, even on bad days.",
      "One more page.",
      "One more problem.",
      "One more day.",
      "Never miss twice."
    ];
    const now = new Date();
    const daySeed = now.getFullYear() * 365 + now.getMonth() * 31 + now.getDate();
    const index = daySeed % quotes.length;
    const quote = quotes[index];
    if (selectors.headerQuote) {
      selectors.headerQuote.textContent = quote;
    }
  }

  async function init() {
    document.documentElement.classList.add('is-capacitor', 'is-mobile-shell', 'mobile-app-shell');
    configureSystemBars().catch(() => {});
    installEvents();
    initSwipeNavigation();
    setupCapacitorBackButton();
    updateDailyQuote();
    // Set tab first so the correct view is visible during data loading
    const initialTab = String(window.location.hash || '').replace('#', '');
    const tab = ['today', 'library', 'create', 'premade', 'browser', 'more'].includes(initialTab) ? initialTab : 'today';
    state.activeTab = tab;
    selectors.views.forEach(view => view.classList.toggle('active', view.id === `view-${tab}`));
    selectors.tabs.forEach(button => button.classList.toggle('active', button.dataset.tab === tab));
    
    // Toggle sticky header creator save button
    const headerSaveBtn = document.getElementById('header-creator-save-btn');
    if (headerSaveBtn) {
      headerSaveBtn.classList.toggle('hidden', tab !== 'create');
    }
    const headerImportBtn = document.getElementById('header-paste-import-btn');
    if (headerImportBtn) {
      headerImportBtn.classList.toggle('hidden', tab === 'create');
    }
    if (selectors.headerQuote) {
      selectors.headerQuote.classList.toggle('hidden', tab === 'create');
    }

    setHeader();
    updateTabIndicator(tab);
    
    // Defer CPU-intensive database load to allow transition/loader animation to initialize smoothly
    setTimeout(async () => {
      await refresh();
      // Initialize opacity slider from loaded settings
      if (selectors.bgOpacitySlider) {
        const opacity = parseFloat(state.settings?.cardBgOpacity ?? 0.32);
        if (Number.isFinite(opacity)) selectors.bgOpacitySlider.value = String(opacity);
      }
      // Initialize theme selection from loaded settings
      renderMore();
      // Initialize import separators from loaded settings
      if (selectors.importTermSepInput) {
        selectors.importTermSepInput.value = state.settings?.importTermSep ?? ';';
      }
      if (selectors.importCardSepInput) {
        selectors.importCardSepInput.value = state.settings?.importCardSep ?? '@';
      }
      hideAppLoader();
    }, 280);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init, { once: true });
  } else {
    init();
  }
})();
