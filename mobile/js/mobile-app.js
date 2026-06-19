(function () {
  const core = window.EruditeCore || {};
  const schema = core.schema;
  const statsCore = core.stats;
  const draftCore = core.draft;

  const CREATOR_DRAFT_KEY = 'mobileCreatorDraft';
  const BROWSER_RENDER_LIMIT = 250;

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
    analyticsCards: [],
    analyticsLoaded: false,
    analyticsLoading: false,
    analyticsError: null,
    analyticsLoadToken: 0,
    browserSearch: '',
    browserFilters: new Set(),
    browserSelectedCards: new Set(),
    browserVisibleIds: [],
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
    { id: 'ssc', name: 'SSC' },
    { id: 'quick-maths', name: 'Quick Maths' }
  ];

  const premadeSubjects = {
    '10th': ['Science', 'Maths', 'English', 'Civics', 'Geography', 'History', 'Hindi', 'Politics'],
    '11th': ['Physics', 'inorganic-chemistry', 'organic-chemistry', 'physical-chemistry', 'English', 'Maths', 'Biology', 'Physical-education'],
    '12th': ['Physics', 'inorganic-chemistry', 'organic-chemistry', 'physical-chemistry', 'English', 'Maths', 'Biology', 'Physical-education'],
    'neet-ug': ['Physics', 'Chemistry', 'Biology'],
    'jee-main': ['Physics', 'Chemistry', 'Maths'],
    'jee-advanced': ['Physics', 'Chemistry', 'Maths'],
    'ssc': ['general-awareness', 'quantitative-aptitude', 'reasoning', 'english'],
    'quick-maths': ['Mental-Maths']
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
  const STUDY_SESSION_MIN_MS = 5 * 1000;
  const DAY_MS = 24 * 60 * 60 * 1000;
  const STUDY_SESSION_LOOKBACK_MS = 365 * 24 * 60 * 60 * 1000;

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
    analyticsDashboard: document.getElementById('analytics-dashboard'),
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
    browserFilterStrip: document.getElementById('browser-filter-strip'),
    browserCountLabel: document.getElementById('browser-count-label'),
    browserSelectVisible: document.getElementById('browser-select-visible-btn'),
    browserList: document.getElementById('browser-list'),
    browserSelectionBar: document.getElementById('browser-selection-bar'),
    browserSelectedCount: document.getElementById('browser-selected-count'),
    browserClearSelection: document.getElementById('browser-clear-selection-btn'),
    srsSwitch: document.getElementById('srs-switch'),
    moreSrsLabel: document.getElementById('more-srs-label'),
    soundSwitch: document.getElementById('sound-switch'),
    moreSoundLabel: document.getElementById('more-sound-label'),
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

  function safeMediaSrc(value) {
    const raw = String(value || '').trim();
    if (!raw) return '';
    if (/["'<>`\\]/.test(raw)) return '';
    if (/^(javascript|vbscript):/i.test(raw)) return '';
    if (/^data:(image|audio|video)\//i.test(raw)) return raw;
    if (/^(blob:|file:|capacitor:|cdvfile:)/i.test(raw)) return raw;
    if (/^https?:\/\//i.test(raw)) {
      try {
        const url = new URL(raw);
        return ['localhost', '127.0.0.1', '::1', '[::1]'].includes(url.hostname) ? raw : '';
      } catch (_error) {
        return '';
      }
    }
    return raw.includes('://') ? '' : raw;
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

  function startOfLocalDayMs(value = Date.now()) {
    const timestamp = normalizeTimestamp(value) || Date.now();
    const date = new Date(timestamp);
    date.setHours(0, 0, 0, 0);
    return date.getTime();
  }

  function formatShortNumber(value) {
    const number = Number(value || 0);
    const abs = Math.abs(number);
    if (abs >= 1000000) return `${(number / 1000000).toFixed(abs >= 10000000 ? 0 : 1).replace(/\.0$/, '')}m`;
    if (abs >= 1000) return `${(number / 1000).toFixed(abs >= 10000 ? 0 : 1).replace(/\.0$/, '')}k`;
    return String(Math.round(number));
  }

  function formatDuration(ms) {
    const totalMs = Math.max(0, Number(ms || 0));
    if (totalMs <= 0) return '0s';
    if (totalMs < 60000) return `${Math.max(1, Math.round(totalMs / 1000))}s`;
    const minutes = Math.round(totalMs / 60000);
    if (minutes < 60) return `${minutes}m`;
    const hours = Math.floor(minutes / 60);
    const remainder = minutes % 60;
    return remainder ? `${hours}h ${remainder}m` : `${hours}h`;
  }

  function isTrackedStudySession(session) {
    return Boolean(
      normalizeTimestamp(session?.startedAt)
      && Number(session?.durationMs || 0) >= STUDY_SESSION_MIN_MS
      && Number(session?.cardsViewed || 0) > 0
    );
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
        if (isTrackedStudySession(session)) {
          dayKeys.add(String(startOfLocalDayMs(session.startedAt)));
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
    if (state.settings?.soundEffectsEnabled === false) return;
    try {
      const audio = new Audio('assets/flashcard-assets/click.mp3');
      audio.volume = 0.85;
      audio.play().catch(() => {});
    } catch (_error) {}
  }

  function playStar() {
    if (state.settings?.soundEffectsEnabled === false) return;
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

  function invalidateAnalytics() {
    state.analyticsLoadToken += 1;
    state.analyticsCards = [];
    state.analyticsLoaded = false;
    state.analyticsLoading = false;
    state.analyticsError = null;
  }

  async function loadAnalyticsCards(options = {}) {
    if (!options.force && state.analyticsLoaded) return state.analyticsCards;
    if (!options.force && state.analyticsLoading) return state.analyticsCards;

    const token = state.analyticsLoadToken + 1;
    state.analyticsLoadToken = token;
    state.analyticsLoading = true;
    state.analyticsError = null;
    if (state.activeTab === 'today') renderAnalyticsDashboard();

    try {
      let cards = [];
      if (!options.force && state.browserLoaded && Array.isArray(state.browserCards)) {
        cards = state.browserCards;
      } else if (window.flashcardStore?.listCardsForBrowser) {
        cards = await window.flashcardStore.listCardsForBrowser();
      }
      if (token !== state.analyticsLoadToken) return state.analyticsCards;
      state.analyticsCards = Array.isArray(cards) ? cards : [];
      state.analyticsLoaded = true;
      state.analyticsError = null;
      return state.analyticsCards;
    } catch (error) {
      if (token !== state.analyticsLoadToken) return state.analyticsCards;
      console.error('[mobile] Analytics load failed:', error);
      state.analyticsCards = [];
      state.analyticsLoaded = false;
      state.analyticsError = error;
      return [];
    } finally {
      if (token === state.analyticsLoadToken) {
        state.analyticsLoading = false;
        if (state.activeTab === 'today') renderAnalyticsDashboard();
      }
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
      window.flashcardStore.getStudySessions ? window.flashcardStore.getStudySessions(Date.now() - STUDY_SESSION_LOOKBACK_MS) : []
    ]);
    state.classes = (classes || []).map(item => schema?.normalizeClass ? schema.normalizeClass(item, null, { preserveLastModified: true }) : item);
    const normalizedSets = (sets || []).map(set => schema?.normalizeSet ? schema.normalizeSet(set, null, { preserveLastModified: true }) : set);
    state.sets = normalizeSetClassReferences(normalizedSets, state.classes);
    state.settings = settings || {};
    // Apply card styles on startup
    if (state.settings.cardStyle) {
      const cs = state.settings.cardStyle;
      let fontFamily = 'inherit';
      if (cs.font === 'sans-serif') fontFamily = "Inter, sans-serif";
      else if (cs.font === 'serif') fontFamily = "Georgia, serif";
      else if (cs.font === 'monospace') fontFamily = "Courier New, monospace";
      else if (cs.font === 'system') fontFamily = "system-ui, sans-serif";

      const root = document.documentElement;
      root.style.setProperty('--card-text-align', cs.align);
      root.style.setProperty('--card-text-weight', cs.weight);
      root.style.setProperty('--card-text-font-family', fontFamily);
      root.style.setProperty('--card-text-line-height', cs.lineHeight);
      root.style.setProperty('--card-text-letter-spacing', cs.letterSpacing);
    }
    state.srsMode = readSrsMode(srsMode);
    state.studySessions = studySessions || [];
    invalidateAnalytics();
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
      const isPremade = btnPremade && btnPremade.classList.contains('active');
      document.getElementById('mobile-user-headers')?.classList.toggle('hidden', isPremade);
      document.getElementById('mobile-user-decks-view')?.classList.toggle('hidden', isPremade);
      document.getElementById('mobile-premade-decks-view')?.classList.toggle('hidden', !isPremade);
      const btnCreate = document.querySelector('[data-action="open-create"]');
      if (btnCreate) btnCreate.classList.toggle('hidden', isPremade);
    } else {
      exitSelectMode();
    }
    if (tab !== 'browser') {
      clearBrowserSelection({ play: false, render: false });
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

  function emptyRatingCounts() {
    return { Again: 0, Hard: 0, Good: 0, Easy: 0 };
  }

  function addRatingCounts(target, source = {}) {
    ['Again', 'Hard', 'Good', 'Easy'].forEach(label => {
      target[label] += Number(source?.[label] || 0);
    });
    return target;
  }

  function ratingPassRate(counts) {
    const total = ['Again', 'Hard', 'Good', 'Easy'].reduce((sum, label) => sum + Number(counts?.[label] || 0), 0);
    const passed = Number(counts?.Hard || 0) + Number(counts?.Good || 0) + Number(counts?.Easy || 0);
    return {
      total,
      passed,
      percent: total > 0 ? Math.round((passed / total) * 100) : null
    };
  }

  function localDayKeyMs(value) {
    const timestamp = normalizeTimestamp(value);
    return timestamp ? startOfLocalDayMs(timestamp) : null;
  }

  function analyticsCardBucket(card) {
    const stateName = String(card?.srsState || 'New').toLowerCase();
    const intervalDays = Number(card?.intervalDays || 0);
    const reviewed = Number(card?.reviewCount || card?.reps || 0) > 0 || Boolean(card?.lastReviewedAt);
    if (stateName === 'learning' || stateName === 'relearning') return 'learning';
    if (intervalDays >= 21) return 'mature';
    if (reviewed) return 'young';
    return 'new';
  }

  function analyticsSummary(cards = []) {
    const summary = {
      totalCards: cards.length,
      activeCards: 0,
      reviewedCards: 0,
      dueCards: 0,
      overdueCards: 0,
      leechCards: 0,
      failedRecently: 0,
      ratingCounts: emptyRatingCounts(),
      retention: null,
      reviewEvents: 0,
      retentionBreakdown: [],
      buttonDistribution: [],
      todayStudyMs: 0,
      weekStudyMs: 0,
      todayCardsViewed: 0,
      weekCardsViewed: 0,
      averageSecondsPerCard: null
    };
    const buckets = {
      mature: { label: 'Mature', counts: emptyRatingCounts() },
      young: { label: 'Young', counts: emptyRatingCounts() },
      learning: { label: 'Learning', counts: emptyRatingCounts() }
    };

    cards.forEach(card => {
      const suspended = Boolean(card?.suspended);
      const buried = Boolean(card?.buried || card?.buriedUntil);
      if (!suspended && !buried) summary.activeCards += 1;
      if (card?.isDue) summary.dueCards += 1;
      if (card?.isOverdue) summary.overdueCards += 1;
      if (card?.leech) summary.leechCards += 1;
      if (card?.failedRecently) summary.failedRecently += 1;
      if (Number(card?.reviewCount || card?.reps || 0) > 0 || card?.lastReviewedAt) summary.reviewedCards += 1;

      addRatingCounts(summary.ratingCounts, card?.ratingCounts);
      const bucket = analyticsCardBucket(card);
      if (buckets[bucket]) addRatingCounts(buckets[bucket].counts, card?.ratingCounts);
    });

    const passRate = ratingPassRate(summary.ratingCounts);
    summary.retention = passRate.percent;
    summary.reviewEvents = passRate.total;
    summary.retentionBreakdown = Object.values(buckets)
      .map(bucket => {
        const rate = ratingPassRate(bucket.counts);
        return { label: bucket.label, percent: rate.percent, total: rate.total };
      })
      .filter(item => item.total > 0);
    summary.buttonDistribution = ['Again', 'Hard', 'Good', 'Easy'].map(label => ({
      label,
      count: Number(summary.ratingCounts[label] || 0),
      percent: passRate.total > 0 ? Math.round((Number(summary.ratingCounts[label] || 0) / passRate.total) * 100) : 0
    }));

    const todayStart = startOfLocalDayMs();
    const weekStart = todayStart - 6 * DAY_MS;
    (state.studySessions || []).filter(isTrackedStudySession).forEach(session => {
      const started = normalizeTimestamp(session.startedAt);
      const duration = Number(session.durationMs || 0);
      const cardsViewed = Number(session.cardsViewed || 0);
      if (started >= todayStart) {
        summary.todayStudyMs += duration;
        summary.todayCardsViewed += cardsViewed;
      }
      if (started >= weekStart) {
        summary.weekStudyMs += duration;
        summary.weekCardsViewed += cardsViewed;
      }
    });
    summary.averageSecondsPerCard = summary.weekCardsViewed > 0
      ? Math.round(summary.weekStudyMs / summary.weekCardsViewed / 1000)
      : null;
    return summary;
  }

  function buildForecast(cards = [], days = 7) {
    const todayStart = startOfLocalDayMs();
    const buckets = Array.from({ length: days }, (_, index) => {
      const dayMs = todayStart + index * DAY_MS;
      return {
        dayMs,
        count: 0,
        label: index === 0
          ? 'Today'
          : index === 1
            ? 'Tomorrow'
            : new Date(dayMs).toLocaleDateString(undefined, { weekday: 'short' })
      };
    });
    cards.forEach(card => {
      if (card?.suspended || card?.buried || card?.buriedUntil) return;
      const dueTime = normalizeTimestamp(card?.dueTime || card?.due);
      if (!dueTime) return;
      let offset = Math.floor((startOfLocalDayMs(dueTime) - todayStart) / DAY_MS);
      if (dueTime < todayStart) offset = 0;
      if (offset >= 0 && offset < days) buckets[offset].count += 1;
    });
    const max = Math.max(1, ...buckets.map(item => item.count));
    return buckets.map(item => ({
      ...item,
      percent: Math.round((item.count / max) * 100)
    }));
  }

  function buildStudyHeatmap(days = 28) {
    const todayStart = startOfLocalDayMs();
    const activity = new Map();
    const bump = (dayMs, patch = {}) => {
      if (!dayMs) return;
      const current = activity.get(dayMs) || { cards: 0, sessions: 0, reviews: 0, durationMs: 0 };
      activity.set(dayMs, {
        cards: current.cards + Number(patch.cards || 0),
        sessions: current.sessions + Number(patch.sessions || 0),
        reviews: current.reviews + Number(patch.reviews || 0),
        durationMs: current.durationMs + Number(patch.durationMs || 0)
      });
    };

    (state.studySessions || []).filter(isTrackedStudySession).forEach(session => {
      bump(startOfLocalDayMs(session.startedAt), {
        cards: Number(session.cardsViewed || 0),
        sessions: 1,
        durationMs: Number(session.durationMs || 0)
      });
    });

    let metaDayKeyCount = 0;
    state.sets.forEach(set => {
      (metaStats(set)?.reviewDayKeys || []).forEach(key => {
        metaDayKeyCount += 1;
        bump(localDayKeyMs(key), { reviews: 1 });
      });
    });
    if (!metaDayKeyCount) {
      reviewedDates().forEach(time => bump(startOfLocalDayMs(time), { reviews: 1 }));
    }

    const items = Array.from({ length: days }, (_, index) => {
      const dayMs = todayStart - (days - index - 1) * DAY_MS;
      const entry = activity.get(dayMs) || { cards: 0, sessions: 0, reviews: 0, durationMs: 0 };
      const score = entry.cards + entry.reviews + entry.sessions;
      return {
        dayMs,
        ...entry,
        score,
        label: new Date(dayMs).toLocaleDateString(undefined, { month: 'short', day: 'numeric' })
      };
    });
    const max = Math.max(1, ...items.map(item => item.score));
    return items.map(item => ({
      ...item,
      level: item.score <= 0 ? 0 : clamp(Math.ceil((item.score / max) * 4), 1, 4)
    }));
  }

  function buildDeckHealth(cards = []) {
    const rows = new Map();
    state.sets.forEach(set => {
      const stats = setStats(set);
      rows.set(String(set.id), {
        setId: String(set.id),
        name: set.name || 'Untitled Set',
        total: setCardCount(set),
        cardTotal: 0,
        due: 0,
        metaDue: Number(stats?.dueCards || dueCountForSet(set, { force: true }) || 0),
        overdue: 0,
        leeches: 0,
        counts: emptyRatingCounts(),
        metaRetention: stats?.retention ?? null
      });
    });

    cards.forEach(card => {
      const setId = String(card?.setId || '');
      if (!setId) return;
      if (!rows.has(setId)) {
        rows.set(setId, {
          setId,
          name: card?.deck || 'Untitled Set',
          total: 0,
          cardTotal: 0,
          due: 0,
          metaDue: 0,
          overdue: 0,
          leeches: 0,
          counts: emptyRatingCounts(),
          metaRetention: null
        });
      }
      const row = rows.get(setId);
      row.cardTotal += 1;
      if (card?.isDue) row.due += 1;
      if (card?.isOverdue) row.overdue += 1;
      if (card?.leech) row.leeches += 1;
      addRatingCounts(row.counts, card?.ratingCounts);
    });

    return Array.from(rows.values())
      .filter(row => (row.total || row.cardTotal) > 0)
      .map(row => {
        const total = row.total || row.cardTotal;
        const due = row.cardTotal ? row.due : row.metaDue;
        const rate = ratingPassRate(row.counts);
        const retention = rate.percent ?? row.metaRetention;
        const dueRatio = total ? due / total : 0;
        const overdueRatio = total ? row.overdue / total : 0;
        const leechRatio = total ? row.leeches / total : 0;
        const baseline = Number.isFinite(Number(retention)) ? Number(retention) : (rate.total > 0 ? 70 : 64);
        const score = clamp(Math.round(baseline - dueRatio * 20 - overdueRatio * 35 - leechRatio * 45), 0, 100);
        const workload = row.overdue > 0
          ? 'Backlog'
          : due > Math.max(30, total * 0.25)
            ? 'Heavy'
            : due > 0
              ? 'Ready'
              : 'Healthy';
        return {
          ...row,
          total,
          due,
          retention,
          score,
          workload
        };
      })
      .sort((a, b) => a.score - b.score || b.overdue - a.overdue || b.leeches - a.leeches || b.due - a.due)
      .slice(0, 4);
  }

  function renderAnalyticsDashboard() {
    if (!selectors.analyticsDashboard) return;
    const totals = totalStats({ forceDue: true });
    if (!totals.cardCount) {
      selectors.analyticsDashboard.innerHTML = emptyPanel('fa-chart-simple', 'No insights yet', 'Create or import a deck to see study analytics.');
      return;
    }

    if (state.analyticsError) {
      selectors.analyticsDashboard.innerHTML = emptyPanel(
        'fa-triangle-exclamation',
        'Insights unavailable',
        state.analyticsError?.message || 'Card analytics could not be loaded.',
        '<button type="button" class="secondary-action" data-action="refresh-analytics"><i class="fas fa-rotate"></i>Retry</button>'
      );
      return;
    }

    if (!state.analyticsLoaded) {
      if (!state.analyticsLoading && state.activeTab === 'today') {
        loadAnalyticsCards().catch(() => {});
      }
      selectors.analyticsDashboard.innerHTML = emptyPanel('fa-chart-line', 'Loading insights', 'Reading card metadata.');
      return;
    }

    const cards = state.analyticsCards || [];
    const summary = analyticsSummary(cards);
    const forecast = buildForecast(cards);
    const heatmap = buildStudyHeatmap();
    const deckHealth = buildDeckHealth(cards);
    const retentionLabel = summary.retention === null ? '--' : `${summary.retention}%`;
    const avgTime = summary.averageSecondsPerCard === null ? '--' : `${summary.averageSecondsPerCard}s`;
    const heatmapHtml = heatmap.map(day => `
      <span class="heatmap-cell level-${day.level}" title="${escapeAttr(`${day.label}: ${day.score ? `${day.score} activity` : 'No study'}`)}"></span>
    `).join('');
    const forecastHtml = forecast.map(day => `
      <div class="forecast-row">
        <span>${escapeHtml(day.label)}</span>
        <strong>${formatShortNumber(day.count)}</strong>
        <i style="--value:${clamp(day.percent, 0, 100)}%"></i>
      </div>
    `).join('');
    const distributionHtml = summary.buttonDistribution.map(item => `
      <div class="rating-row rating-${escapeAttr(item.label.toLowerCase())}">
        <span>${escapeHtml(item.label)}</span>
        <strong>${item.percent}%</strong>
        <i style="--value:${clamp(item.percent, 0, 100)}%"></i>
      </div>
    `).join('');
    const retentionBreakdownHtml = summary.retentionBreakdown.length
      ? summary.retentionBreakdown.map(item => `
          <span><strong>${escapeHtml(item.label)}</strong><em>${item.percent === null ? '--' : `${item.percent}%`}</em></span>
        `).join('')
      : '<span><strong>Reviews</strong><em>--</em></span>';
    const deckHealthHtml = deckHealth.length
      ? deckHealth.map(deck => `
          <article class="deck-health-row">
            <div>
              <strong>${escapeHtml(deck.name)}</strong>
              <span>${escapeHtml(deck.workload)} &middot; ${formatShortNumber(deck.due)} due &middot; ${formatShortNumber(deck.leeches)} weak</span>
            </div>
            <b>${deck.score}</b>
          </article>
        `).join('')
      : '<div class="insight-muted">No deck pressure yet.</div>';

    selectors.analyticsDashboard.innerHTML = `
      <div class="insight-grid">
        <article class="insight-card insight-score">
          <span class="insight-icon"><i class="fas fa-bullseye"></i></span>
          <div>
            <small>Actual retention</small>
            <strong>${retentionLabel}</strong>
            <p>${formatShortNumber(summary.reviewEvents)} graded reviews</p>
          </div>
        </article>
        <article class="insight-card">
          <span class="insight-icon warn"><i class="fas fa-calendar-day"></i></span>
          <div>
            <small>Due load</small>
            <strong>${formatShortNumber(summary.dueCards)}</strong>
            <p>${formatShortNumber(summary.overdueCards)} overdue</p>
          </div>
        </article>
        <article class="insight-card">
          <span class="insight-icon danger"><i class="fas fa-triangle-exclamation"></i></span>
          <div>
            <small>Weak cards</small>
            <strong>${formatShortNumber(summary.leechCards)}</strong>
            <p>${formatShortNumber(summary.failedRecently)} failed recently</p>
          </div>
        </article>
        <article class="insight-card">
          <span class="insight-icon calm"><i class="fas fa-stopwatch"></i></span>
          <div>
            <small>Today</small>
            <strong>${formatDuration(summary.todayStudyMs)}</strong>
            <p>${avgTime}/card this week</p>
          </div>
        </article>
      </div>

      <div class="insight-two-col">
        <article class="insight-panel">
          <div class="insight-panel-head">
            <strong>Retention</strong>
            <span>${formatShortNumber(summary.reviewedCards)} reviewed</span>
          </div>
          <div class="retention-breakdown">${retentionBreakdownHtml}</div>
          <div class="rating-list">${distributionHtml}</div>
        </article>
        <article class="insight-panel">
          <div class="insight-panel-head">
            <strong>Forecast</strong>
            <span>7 days</span>
          </div>
          <div class="forecast-list">${forecastHtml}</div>
        </article>
      </div>

      <article class="insight-panel">
        <div class="insight-panel-head">
          <strong>Study heatmap</strong>
          <span>${formatDuration(summary.weekStudyMs)} this week</span>
        </div>
        <div class="study-heatmap">${heatmapHtml}</div>
      </article>

      <article class="insight-panel">
        <div class="insight-panel-head">
          <strong>Deck health</strong>
          <span>Lowest scores</span>
        </div>
        <div class="deck-health-list">${deckHealthHtml}</div>
      </article>
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

    renderAnalyticsDashboard();

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
      const itemSrc = safeMediaSrc(item.src);
      if (!itemSrc) return '';
      const icon = item.kind === 'audio' ? 'fa-volume-high' : item.kind === 'video' ? 'fa-film' : 'fa-image';
      let preview = '';
      if (item.kind === 'audio') {
        preview = `<audio src="${escapeAttr(itemSrc)}" controls preload="metadata"></audio>`;
      } else if (item.kind === 'video') {
        preview = `<video src="${escapeAttr(itemSrc)}" controls preload="metadata"></video>`;
      } else {
        preview = `<img src="${escapeAttr(itemSrc)}" alt="">`;
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
    const backgroundSrc = safeMediaSrc(background?.src);
    const backgroundHtml = backgroundSrc ? `
      <div class="creator-background-preview" style="background-image:url('${escapeAttr(backgroundSrc)}')">
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
    const safeTerm = sanitizeEditorHtml(card.term || '');
    const safeDefinition = sanitizeEditorHtml(card.definition || '');
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
          <div class="rich-editor" contenteditable="true" data-editor-id="${escapeAttr(card.id)}" data-side="term" data-placeholder="Enter term">${safeTerm}</div>
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
          <div class="rich-editor" contenteditable="true" data-editor-id="${escapeAttr(card.id)}" data-side="definition" data-placeholder="Enter definition">${safeDefinition}</div>
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
              <div class="deck-icon"><i class="fas ${item.icon || 'fa-book-open'}"></i></div>
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
    const triggerBtn = document.getElementById('mobile-take-deck-class-trigger');
    const cancelBtn = document.getElementById('mobile-take-deck-cancel');
    const confirmBtn = document.getElementById('mobile-take-deck-confirm');

    let selectedClassId = '';

    const updateClassLabel = (classId) => {
      selectedClassId = classId;
      const label = document.getElementById('mobile-take-deck-class-label');
      if (label) {
        if (!classId) {
          label.textContent = 'General';
        } else {
          const cls = state.classes.find(c => String(c.id) === String(classId));
          label.textContent = cls ? cls.name : 'General';
        }
      }
    };

    if (nameInput) {
      nameInput.value = data.name || data.title || fileName.replace(/\.json$/i, '');
    }

    updateClassLabel('');

    overlay?.classList.remove('hidden');

    const onTriggerClick = (e) => {
      e.preventDefault();
      playClick();
      openClassSelectModal(
        selectedClassId,
        (classId) => {
          updateClassLabel(classId);
        },
        async () => {
          await createClassFromCreator();
        }
      );
    };

    const cleanupListeners = () => {
      cancelBtn?.removeEventListener('click', onCancel);
      confirmBtn?.removeEventListener('click', onConfirm);
      overlay?.removeEventListener('click', onOverlayClick);
      triggerBtn?.removeEventListener('click', onTriggerClick);
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
      const targetClassId = selectedClassId || null;

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
    triggerBtn?.addEventListener('click', onTriggerClick);
  }


  async function loadBrowserCards(options = {}) {
    if (options.force) state.browserLoaded = false;
    if (state.browserLoaded) return;
    selectors.browserList.innerHTML = emptyPanel('fa-spinner', 'Loading cards', 'Building a searchable local card list.');
    if (window.flashcardStore.listCardsForBrowser) {
      state.browserCards = await window.flashcardStore.listCardsForBrowser();
    } else {
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
    }
    state.browserLoaded = true;
    state.analyticsCards = state.browserCards;
    state.analyticsLoaded = true;
    state.analyticsLoading = false;
    state.analyticsError = null;
    state.analyticsLoadToken += 1;
    state.browserSelectedCards = new Set(
      Array.from(state.browserSelectedCards || []).filter(id => state.browserCards.some(card => String(card.id) === String(id)))
    );
  }

  function browserStateLabel(card) {
    if (card.suspended) return 'Suspended';
    if (card.buried) return 'Buried';
    return card.srsState || 'New';
  }

  function browserDueLabel(card) {
    if (card.suspended) return 'Suspended';
    if (card.buried) return 'Buried';
    if (card.isOverdue) return 'Overdue';
    if (card.isDue) return 'Due';
    if (!card.dueTime) return 'No due date';
    return `Due ${relativeTime(card.dueTime)}`;
  }

  function browserCardMatchesFilter(card, filter) {
    const stateName = String(card.srsState || 'New').toLowerCase();
    switch (filter) {
      case 'new':
      case 'learning':
      case 'review':
      case 'relearning':
        return stateName === filter;
      case 'due':
        return Boolean(card.isDue);
      case 'overdue':
        return Boolean(card.isOverdue);
      case 'suspended':
        return Boolean(card.suspended);
      case 'buried':
        return Boolean(card.buried || card.buriedUntil);
      case 'failed':
        return Boolean(card.failedRecently);
      case 'leeches':
        return Boolean(card.leech);
      case 'no-tags':
        return Boolean(card.noTags);
      case 'has-image':
        return Boolean(card.hasImage);
      case 'has-audio':
        return Boolean(card.hasAudio);
      default:
        return true;
    }
  }

  function filteredBrowserCards() {
    const query = state.browserSearch.trim().toLowerCase();
    const filters = Array.from(state.browserFilters || []);
    return state.browserCards.filter(card => {
      if (query) {
        const haystack = [
          card.deck,
          card.className,
          card.term,
          card.definition,
          card.srsState,
          ...(card.tags || [])
        ].join(' ').toLowerCase();
        if (!haystack.includes(query)) return false;
      }
      return filters.every(filter => browserCardMatchesFilter(card, filter));
    });
  }

  function renderBrowserFilters() {
    if (!selectors.browserFilterStrip) return;
    const active = state.browserFilters || new Set();
    selectors.browserFilterStrip.querySelectorAll('[data-browser-filter]').forEach(button => {
      const filter = button.dataset.browserFilter;
      button.classList.toggle('active', filter === 'all' ? active.size === 0 : active.has(filter));
    });
  }

  function renderBrowserSelection() {
    const count = state.browserSelectedCards ? state.browserSelectedCards.size : 0;
    if (selectors.browserSelectionBar) {
      selectors.browserSelectionBar.hidden = count === 0;
    }
    if (selectors.browserSelectedCount) {
      selectors.browserSelectedCount.textContent = `${count} ${count === 1 ? 'card' : 'cards'} selected`;
    }
    if (selectors.browserList) {
      selectors.browserList.querySelectorAll('[data-browser-card-select]').forEach(button => {
        const selected = state.browserSelectedCards.has(String(button.dataset.browserCardSelect));
        button.classList.toggle('selected', selected);
        button.setAttribute('aria-pressed', String(selected));
        const icon = button.querySelector('i');
        if (icon) icon.className = selected ? 'fas fa-check' : 'far fa-square';
      });
      selectors.browserList.querySelectorAll('.browser-card').forEach(row => {
        row.classList.toggle('selected', state.browserSelectedCards.has(String(row.dataset.cardId)));
      });
    }
  }

  function browserCardRow(card) {
    const id = String(card.id);
    const selected = state.browserSelectedCards?.has(id);
    const tags = (card.tags || []).slice(0, 4).map(tag => `<span>#${escapeHtml(tag)}</span>`).join('');
    const flags = [
      card.failedRecently ? '<span class="warning">Failed</span>' : '',
      card.leech ? '<span class="danger">Leech</span>' : '',
      card.hasImage ? '<span><i class="fas fa-image"></i> Image</span>' : '',
      card.hasAudio ? '<span><i class="fas fa-volume-high"></i> Audio</span>' : ''
    ].filter(Boolean).join('');

    return `
      <article class="browser-card ${selected ? 'selected' : ''}" data-card-id="${escapeAttr(id)}">
        <button type="button" class="browser-card-check ${selected ? 'selected' : ''}" data-browser-card-select="${escapeAttr(id)}" aria-label="Select card" aria-pressed="${selected ? 'true' : 'false'}">
          <i class="${selected ? 'fas fa-check' : 'far fa-square'}"></i>
        </button>
        <div class="browser-card-body">
          <div class="browser-card-head">
            <span>${escapeHtml(card.deck)}</span>
            <small>${escapeHtml(card.className)}</small>
          </div>
          <strong>${escapeHtml(card.term || 'Empty term')}</strong>
          <p>${escapeHtml(card.definition || 'Empty definition')}</p>
          <div class="deck-subline browser-card-meta">
            <span>${escapeHtml(browserStateLabel(card))}</span>
            <span>${escapeHtml(browserDueLabel(card))}</span>
            ${tags}
            ${flags}
          </div>
        </div>
      </article>
    `;
  }

  function renderBrowser() {
    if (!selectors.browserList) return;
    selectors.browserSearchInput.value = state.browserSearch;
    renderBrowserFilters();
    const allFilteredCards = filteredBrowserCards();
    const cards = allFilteredCards.slice(0, BROWSER_RENDER_LIMIT);
    state.browserVisibleIds = cards.map(card => String(card.id));

    if (selectors.browserCountLabel) {
      const shown = cards.length === allFilteredCards.length
        ? `${allFilteredCards.length}`
        : `${cards.length}/${allFilteredCards.length}`;
      selectors.browserCountLabel.textContent = `${shown} ${allFilteredCards.length === 1 ? 'card' : 'cards'}`;
    }
    if (selectors.browserSelectVisible) {
      selectors.browserSelectVisible.disabled = cards.length === 0;
    }

    selectors.browserList.innerHTML = cards.length
      ? cards.map(browserCardRow).join('')
      : emptyPanel('fa-table-list', 'No cards found', state.browserSearch || state.browserFilters.size ? 'Try another search or filter.' : 'Create or import a deck first.');
    renderBrowserSelection();
  }

  function toggleBrowserFilter(filter) {
    if (!state.browserFilters) state.browserFilters = new Set();
    if (filter === 'all') {
      state.browserFilters.clear();
    } else if (state.browserFilters.has(filter)) {
      state.browserFilters.delete(filter);
    } else {
      state.browserFilters.add(filter);
    }
    playClick();
    renderBrowser();
  }

  function toggleBrowserCardSelection(cardId) {
    const id = String(cardId || '');
    if (!id) return;
    if (!state.browserSelectedCards) state.browserSelectedCards = new Set();
    if (state.browserSelectedCards.has(id)) {
      state.browserSelectedCards.delete(id);
    } else {
      state.browserSelectedCards.add(id);
    }
    playClick();
    renderBrowserSelection();
  }

  function selectVisibleBrowserCards() {
    const visibleIds = (state.browserVisibleIds || []).map(String);
    if (!visibleIds.length) return;
    if (!state.browserSelectedCards) state.browserSelectedCards = new Set();
    const allSelected = visibleIds.every(id => state.browserSelectedCards.has(id));
    visibleIds.forEach(id => {
      if (allSelected) state.browserSelectedCards.delete(id);
      else state.browserSelectedCards.add(id);
    });
    playClick();
    renderBrowserSelection();
  }

  function clearBrowserSelection(options = {}) {
    if (!state.browserSelectedCards) state.browserSelectedCards = new Set();
    if (!state.browserSelectedCards.size) {
      if (selectors.browserSelectionBar) selectors.browserSelectionBar.hidden = true;
      return;
    }
    state.browserSelectedCards.clear();
    if (options.play !== false) playClick();
    if (options.render === false) {
      if (selectors.browserSelectionBar) selectors.browserSelectionBar.hidden = true;
      return;
    }
    renderBrowserSelection();
  }

  function browserSelectedIds() {
    return Array.from(state.browserSelectedCards || []).map(String);
  }

  function openBrowserFieldModal({
    title,
    icon = 'fa-pen',
    message = '',
    inputType = 'text',
    placeholder = '',
    value = '',
    options = [],
    okText = 'Apply',
    isDanger = false
  }) {
    return new Promise(resolve => {
      const overlay = document.createElement('div');
      overlay.className = 'mobile-modal-overlay browser-action-modal';
      const fieldHtml = options.length
        ? `<select class="mobile-modal-select" id="browser-action-field">
            ${options.map(item => `<option value="${escapeAttr(item.value)}">${escapeHtml(item.label)}</option>`).join('')}
          </select>`
        : `<input class="mobile-modal-input" id="browser-action-field" type="${escapeAttr(inputType)}" value="${escapeAttr(value)}" placeholder="${escapeAttr(placeholder)}" autocomplete="off">`;
      overlay.innerHTML = `
        <div class="mobile-modal-card">
          <h3 class="modal-title"><i class="fas ${escapeAttr(icon)}"></i> ${escapeHtml(title)}</h3>
          ${message ? `<p class="mobile-modal-hint">${escapeHtml(message)}</p>` : ''}
          <div class="mobile-modal-field">${fieldHtml}</div>
          <div class="mobile-modal-actions">
            <button type="button" class="mobile-modal-btn cancel" data-browser-action-cancel>Cancel</button>
            <button type="button" class="mobile-modal-btn confirm ${isDanger ? 'danger' : ''}" data-browser-action-confirm>${escapeHtml(okText)}</button>
          </div>
        </div>
      `;

      const close = result => {
        overlay.removeEventListener('click', onOverlayClick);
        overlay.querySelector('[data-browser-action-cancel]')?.removeEventListener('click', onCancel);
        overlay.querySelector('[data-browser-action-confirm]')?.removeEventListener('click', onConfirm);
        overlay.remove();
        state.lastModalClosedAt = Date.now();
        resolve(result);
      };
      const onCancel = () => close(null);
      const onConfirm = () => {
        const field = overlay.querySelector('#browser-action-field');
        close(field?.value || '');
      };
      const onOverlayClick = event => {
        if (event.target === overlay) close(null);
      };

      overlay.addEventListener('click', onOverlayClick);
      overlay.querySelector('[data-browser-action-cancel]')?.addEventListener('click', onCancel);
      overlay.querySelector('[data-browser-action-confirm]')?.addEventListener('click', onConfirm);
      document.body.appendChild(overlay);
      requestAnimationFrame(() => overlay.querySelector('#browser-action-field')?.focus());
    });
  }

  async function browserBulkOptions(action, count) {
    if (action === 'delete') {
      const ok = await showMobileConfirm({
        title: 'Delete Cards',
        message: `Delete ${count} selected ${count === 1 ? 'card' : 'cards'}? This cannot be undone.`,
        okText: 'Delete',
        isDanger: true
      });
      return ok ? {} : null;
    }
    if (action === 'reset-srs') {
      const ok = await showMobileConfirm({
        title: 'Reset SRS',
        message: `Reset scheduling for ${count} selected ${count === 1 ? 'card' : 'cards'}? Card text and tags will stay intact.`,
        okText: 'Reset',
        isDanger: true
      });
      return ok ? { deleteHistory: false } : null;
    }
    if (action === 'set-due') {
      const today = new Date().toISOString().slice(0, 10);
      const due = await openBrowserFieldModal({
        title: 'Set Due Date',
        icon: 'fa-calendar-day',
        message: `${count} selected ${count === 1 ? 'card' : 'cards'}`,
        inputType: 'date',
        value: today,
        okText: 'Set Due'
      });
      return due ? { due } : null;
    }
    if (action === 'move') {
      const options = [...state.sets]
        .sort((a, b) => String(a.name || '').localeCompare(String(b.name || '')))
        .map(set => ({ value: String(set.id), label: set.name || 'Untitled Set' }));
      const targetSetId = await openBrowserFieldModal({
        title: 'Move Cards',
        icon: 'fa-folder-open',
        message: `${count} selected ${count === 1 ? 'card' : 'cards'}`,
        options,
        okText: 'Move'
      });
      return targetSetId ? { targetSetId } : null;
    }
    if (action === 'add-tag' || action === 'remove-tag') {
      const tags = await openBrowserFieldModal({
        title: action === 'add-tag' ? 'Add Tags' : 'Remove Tags',
        icon: 'fa-tag',
        message: 'Separate multiple tags with commas.',
        placeholder: 'weak, biology, chapter-2',
        okText: action === 'add-tag' ? 'Add' : 'Remove'
      });
      return tags ? { tags } : null;
    }
    return {};
  }

  function browserBulkToast(action, result, count) {
    const changed = Number(result?.deleted || result?.moved || result?.updated || count || 0);
    const cardText = `${changed} ${changed === 1 ? 'card' : 'cards'}`;
    const labels = {
      suspend: `${cardText} suspended`,
      unsuspend: `${cardText} unsuspended`,
      'reset-srs': `${cardText} reset`,
      delete: `${cardText} deleted`,
      move: `${cardText} moved`,
      'set-due': `${cardText} updated`,
      'add-tag': `${cardText} tagged`,
      'remove-tag': `${cardText} updated`
    };
    showToast(labels[action] || `${cardText} updated`);
  }

  async function applyBrowserBulkAction(action) {
    const ids = browserSelectedIds();
    if (!ids.length) {
      showToast('Select cards first');
      return;
    }
    if (!window.flashcardStore?.bulkUpdateCards) {
      showToast('Bulk tools are not available');
      return;
    }

    const options = await browserBulkOptions(action, ids.length);
    if (options === null) return;

    showMicroLoader('Updating cards...');
    try {
      if ((action === 'delete' || action === 'reset-srs') && window.flashcardStore?.createBackupSnapshot) {
        await window.flashcardStore.createBackupSnapshot(`before-bulk-${action}`).catch(error => {
          console.warn('[mobile] Could not create bulk action backup snapshot:', error);
        });
      }
      const result = await window.flashcardStore.bulkUpdateCards(ids, action, options);
      clearBrowserSelection({ play: false, render: false });
      state.browserLoaded = false;
      await loadData();
      await loadBrowserCards({ force: true });
      render();
      browserBulkToast(action, result, ids.length);
    } catch (error) {
      console.error('[mobile] Bulk card action failed:', error);
      showToast(error?.message || 'Could not update cards');
    } finally {
      hideMicroLoader();
    }
  }


  function renderMore() {
    selectors.srsSwitch?.classList.toggle('on', state.srsMode);
    selectors.moreSrsLabel.textContent = state.srsMode ? 'On - due reviews are scheduled' : 'Off - normal study only';
    
    const soundEnabled = state.settings?.soundEffectsEnabled !== false;
    selectors.soundSwitch?.classList.toggle('on', soundEnabled);
    if (selectors.moreSoundLabel) {
      selectors.moreSoundLabel.textContent = soundEnabled ? 'On' : 'Off';
    }

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

  async function toggleSound() {
    const soundEnabled = state.settings?.soundEffectsEnabled !== false;
    state.settings = {
      ...(state.settings || {}),
      soundEffectsEnabled: !soundEnabled
    };
    if (window.flashcardStore?.saveSettings) {
      await window.flashcardStore.saveSettings(state.settings);
    }
    if (!soundEnabled) {
      playClick();
    }
    renderMore();
    showToast(state.settings.soundEffectsEnabled ? 'Sound effects enabled' : 'Sound effects disabled');
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

  function openTypographyModal() {
    const overlay = document.getElementById('mobile-typography-overlay');
    const cancelBtn = document.getElementById('mobile-typography-cancel');
    const saveBtn = document.getElementById('mobile-typography-save');
    if (!overlay) return;

    // Triggers and labels
    const alignTrigger = document.getElementById('mobile-card-align-trigger');
    const alignLabel = document.getElementById('mobile-card-align-label');
    const fontTrigger = document.getElementById('mobile-card-font-trigger');
    const fontLabel = document.getElementById('mobile-card-font-label');
    const weightTrigger = document.getElementById('mobile-card-weight-trigger');
    const weightLabel = document.getElementById('mobile-card-weight-label');
    const lineHeightTrigger = document.getElementById('mobile-card-line-height-trigger');
    const lineHeightLabel = document.getElementById('mobile-card-line-height-label');
    const letterSpacingTrigger = document.getElementById('mobile-card-letter-spacing-trigger');
    const letterSpacingLabel = document.getElementById('mobile-card-letter-spacing-label');

    const cs = state.settings?.cardStyle || {
      align: 'center',
      font: 'sans-serif',
      weight: '500',
      lineHeight: '1.4',
      letterSpacing: '0'
    };

    const tempStyle = {
      align: cs.align || 'center',
      font: cs.font || 'sans-serif',
      weight: cs.weight || '500',
      lineHeight: cs.lineHeight || '1.4',
      letterSpacing: cs.letterSpacing || '0'
    };

    const maps = {
      align: { left: 'Left', center: 'Center', right: 'Right' },
      font: { 'sans-serif': 'Sans-Serif (Default)', serif: 'Serif', monospace: 'Monospace', system: 'System Default' },
      weight: { '300': 'Light (300)', '400': 'Regular (400)', '500': 'Medium (500)', '600': 'Semibold (600)', '700': 'Bold (700)' },
      lineHeight: { '1.2': 'Compact (1.2)', '1.4': 'Normal (1.4)', '1.6': 'Relaxed (1.6)', '1.8': 'Loose (1.8)' },
      letterSpacing: { '-0.5px': 'Tight (-0.5px)', '0': 'Normal (0px)', '0.5px': 'Wide (0.5px)', '1px': 'Extra Wide (1px)', '1.5px': 'Loose (1.5px)' }
    };

    function updateLabels() {
      if (alignLabel) alignLabel.textContent = maps.align[tempStyle.align] || tempStyle.align;
      if (fontLabel) fontLabel.textContent = maps.font[tempStyle.font] || tempStyle.font;
      if (weightLabel) weightLabel.textContent = maps.weight[tempStyle.weight] || tempStyle.weight;
      if (lineHeightLabel) lineHeightLabel.textContent = maps.lineHeight[tempStyle.lineHeight] || tempStyle.lineHeight;
      if (letterSpacingLabel) letterSpacingLabel.textContent = maps.letterSpacing[tempStyle.letterSpacing] || tempStyle.letterSpacing;
    }

    // Initialize labels
    updateLabels();

    function openSubModal(overlayId, cancelId, currentValue, onSelect) {
      const subOverlay = document.getElementById(overlayId);
      const subCancelBtn = document.getElementById(cancelId);
      if (!subOverlay) return;

      const optionButtons = Array.from(subOverlay.querySelectorAll('.mobile-modal-option-btn'));
      optionButtons.forEach(btn => {
        btn.classList.toggle('selected', btn.dataset.value === currentValue);
      });

      subOverlay.classList.remove('hidden');

      function closeSub() {
        subOverlay.classList.add('hidden');
        cleanupSub();
      }

      function handleChoice(event) {
        const btn = event.target.closest('[data-value]');
        if (!btn) return;
        playClick();
        onSelect(btn.dataset.value);
        closeSub();
      }

      function onSubBackdropClick(event) {
        if (event.target === subOverlay) {
          closeSub();
        }
      }

      function cleanupSub() {
        optionButtons.forEach(btn => btn.removeEventListener('click', handleChoice));
        subCancelBtn?.removeEventListener('click', closeSub);
        subOverlay.removeEventListener('click', onSubBackdropClick);
      }

      optionButtons.forEach(btn => btn.addEventListener('click', handleChoice));
      subCancelBtn?.addEventListener('click', closeSub);
      subOverlay.addEventListener('click', onSubBackdropClick);
    }

    function onAlignClick() {
      openSubModal('mobile-align-select-overlay', 'mobile-align-select-cancel', tempStyle.align, val => {
        tempStyle.align = val;
        updateLabels();
      });
    }
    function onFontClick() {
      openSubModal('mobile-font-select-overlay', 'mobile-font-select-cancel', tempStyle.font, val => {
        tempStyle.font = val;
        updateLabels();
      });
    }
    function onWeightClick() {
      openSubModal('mobile-weight-select-overlay', 'mobile-weight-select-cancel', tempStyle.weight, val => {
        tempStyle.weight = val;
        updateLabels();
      });
    }
    function onLineHeightClick() {
      openSubModal('mobile-line-height-select-overlay', 'mobile-line-height-select-cancel', tempStyle.lineHeight, val => {
        tempStyle.lineHeight = val;
        updateLabels();
      });
    }
    function onLetterSpacingClick() {
      openSubModal('mobile-letter-spacing-select-overlay', 'mobile-letter-spacing-select-cancel', tempStyle.letterSpacing, val => {
        tempStyle.letterSpacing = val;
        updateLabels();
      });
    }

    alignTrigger?.addEventListener('click', onAlignClick);
    fontTrigger?.addEventListener('click', onFontClick);
    weightTrigger?.addEventListener('click', onWeightClick);
    lineHeightTrigger?.addEventListener('click', onLineHeightClick);
    letterSpacingTrigger?.addEventListener('click', onLetterSpacingClick);

    overlay.classList.remove('hidden');

    function close() {
      overlay.classList.add('hidden');
      cleanup();
      state.lastModalClosedAt = Date.now();
    }

    function onMainBackdropClick(event) {
      if (event.target === overlay) {
        close();
      }
    }

    async function handleSave() {
      state.settings = state.settings || {};
      state.settings.cardStyle = { ...tempStyle };

      // Set styles on the body element dynamically
      const csNew = state.settings.cardStyle;
      let fontFamily = 'inherit';
      if (csNew.font === 'sans-serif') fontFamily = "Inter, sans-serif";
      else if (csNew.font === 'serif') fontFamily = "Georgia, serif";
      else if (csNew.font === 'monospace') fontFamily = "Courier New, monospace";
      else if (csNew.font === 'system') fontFamily = "system-ui, sans-serif";

      const root = document.documentElement;
      root.style.setProperty('--card-text-align', csNew.align);
      root.style.setProperty('--card-text-weight', csNew.weight);
      root.style.setProperty('--card-text-font-family', fontFamily);
      root.style.setProperty('--card-text-line-height', csNew.lineHeight);
      root.style.setProperty('--card-text-letter-spacing', csNew.letterSpacing);

      playClick();
      close();
      
      try {
        await window.flashcardStore.saveSettings(state.settings);
        showToast('Typography settings saved');
      } catch (err) {
        console.warn('[mobile] Could not save typography settings:', err);
      }
    }

    function cleanup() {
      cancelBtn?.removeEventListener('click', close);
      saveBtn?.removeEventListener('click', handleSave);
      alignTrigger?.removeEventListener('click', onAlignClick);
      fontTrigger?.removeEventListener('click', onFontClick);
      weightTrigger?.removeEventListener('click', onWeightClick);
      lineHeightTrigger?.removeEventListener('click', onLineHeightClick);
      letterSpacingTrigger?.removeEventListener('click', onLetterSpacingClick);
      overlay.removeEventListener('click', onMainBackdropClick);
    }

    cancelBtn?.addEventListener('click', close);
    saveBtn?.addEventListener('click', handleSave);
    overlay.addEventListener('click', onMainBackdropClick);
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
      if (state.activeTab === 'browser' && state.browserSelectedCards?.size) {
        clearBrowserSelection();
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
      // 6. Browser backs out to Settings, then other tabs return to Today
      if (state.activeTab === 'browser') {
        setActiveTab('more');
        return;
      }
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
        document.getElementById('mobile-user-headers')?.classList.remove('hidden');
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
        document.getElementById('mobile-user-headers')?.classList.add('hidden');
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
      case 'refresh-analytics':
        playClick();
        state.analyticsLoaded = false;
        await loadAnalyticsCards({ force: true });
        break;
      case 'toggle-srs':
        await toggleSrs();
        break;
      case 'toggle-sound':
        await toggleSound();
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
      case 'select-typography':
        openTypographyModal();
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

  let deckSettingsSetId = null;
  let deckSettingsStudyOrder = '';
  let deckSettingsSrsEnabled = true;

  function openDeckSettingsModal(setId) {
    const set = state.sets.find(item => String(item.id) === String(setId));
    if (!set) return;

    deckSettingsSetId = setId;
    const srs = schema?.normalizeSrsSettings ? schema.normalizeSrsSettings(set.srsSettings || {}) : (set.srsSettings || { enabled: true });

    deckSettingsStudyOrder = set.normalStudyOrder || '';
    deckSettingsSrsEnabled = srs.enabled !== false;

    // Populate fields
    updateDeckStudyOrderUi();
    updateDeckSrsEnabledUi();

    const requestRetentionInput = document.getElementById('mobile-deck-request-retention');
    if (requestRetentionInput) {
      requestRetentionInput.value = srs.requestRetention;
    }

    const maxIntervalInput = document.getElementById('mobile-deck-max-interval');
    if (maxIntervalInput) {
      maxIntervalInput.value = srs.maxIntervalDays;
    }

    const newLimitInput = document.getElementById('mobile-deck-new-limit');
    if (newLimitInput) {
      newLimitInput.value = srs.newCardsPerDay ?? '';
    }

    const reviewLimitInput = document.getElementById('mobile-deck-review-limit');
    if (reviewLimitInput) {
      reviewLimitInput.value = srs.reviewsPerDay ?? '';
    }

    const overlay = document.getElementById('mobile-deck-settings-overlay');
    if (overlay) {
      overlay.classList.remove('hidden');
      playClick();
    }
  }

  function updateDeckStudyOrderUi() {
    const label = document.getElementById('mobile-deck-study-order-label');
    if (label) {
      const mapping = {
        '': 'Use Global Setting',
        'forward': 'Forward (First to Last)',
        'backward': 'Backward (Last to First)',
        'random': 'Random'
      };
      label.textContent = mapping[deckSettingsStudyOrder] || 'Use Global Setting';
    }
  }

  function updateDeckSrsEnabledUi() {
    const label = document.getElementById('mobile-deck-srs-enabled-label');
    if (label) {
      label.textContent = deckSettingsSrsEnabled ? 'Enabled (Apply SRS algorithm)' : 'Disabled (Normal browsing)';
    }
    const srsFields = document.getElementById('mobile-deck-srs-fields');
    if (srsFields) {
      srsFields.style.display = deckSettingsSrsEnabled ? 'flex' : 'none';
    }
  }

  function closeDeckSettingsModal() {
    const overlay = document.getElementById('mobile-deck-settings-overlay');
    if (overlay) {
      overlay.classList.add('hidden');
    }
    deckSettingsSetId = null;
    state.lastModalClosedAt = Date.now();
  }

  function openDeckStudyOrderModal() {
    const modal = document.getElementById('deck-study-order-modal');
    if (!modal) return;

    const optionButtons = Array.from(modal.querySelectorAll('.preset-option-btn'));
    optionButtons.forEach(btn => {
      btn.classList.toggle('selected', btn.dataset.orderVal === deckSettingsStudyOrder);
    });

    modal.classList.remove('hidden');
    playClick();
  }

  function closeDeckStudyOrderModal() {
    const modal = document.getElementById('deck-study-order-modal');
    if (modal) modal.classList.add('hidden');
  }

  function openDeckSrsEnabledModal() {
    const modal = document.getElementById('deck-srs-enabled-modal');
    if (!modal) return;

    const optionButtons = Array.from(modal.querySelectorAll('.preset-option-btn'));
    optionButtons.forEach(btn => {
      const isSel = (btn.dataset.srsVal === 'true') === deckSettingsSrsEnabled;
      btn.classList.toggle('selected', isSel);
    });

    modal.classList.remove('hidden');
    playClick();
  }

  function closeDeckSrsEnabledModal() {
    const modal = document.getElementById('deck-srs-enabled-modal');
    if (modal) modal.classList.add('hidden');
  }

  async function saveMobileDeckSettings() {
    if (!deckSettingsSetId) return;

    const requestRetentionInput = document.getElementById('mobile-deck-request-retention');
    const maxIntervalInput = document.getElementById('mobile-deck-max-interval');
    const newLimitInput = document.getElementById('mobile-deck-new-limit');
    const reviewLimitInput = document.getElementById('mobile-deck-review-limit');

    const srsSettings = schema?.normalizeSrsSettings ? schema.normalizeSrsSettings({
      enabled: deckSettingsSrsEnabled,
      requestRetention: requestRetentionInput?.value,
      maxIntervalDays: maxIntervalInput?.value,
      newCardsPerDay: newLimitInput?.value,
      reviewsPerDay: reviewLimitInput?.value
    }) : { enabled: deckSettingsSrsEnabled };

    const set = state.sets.find(item => String(item.id) === String(deckSettingsSetId));
    if (!set) return;

    const updatedSet = {
      ...set,
      srsSettings,
      normalStudyOrder: deckSettingsStudyOrder || null,
      lastModified: Date.now()
    };

    try {
      if (window.flashcardStore?.saveSet) {
        await window.flashcardStore.saveSet(updatedSet);
      }
      
      state.sets = state.sets.map(item => String(item.id) === String(deckSettingsSetId) ? updatedSet : item);
      renderLibrary();
      
      closeDeckSettingsModal();
      showToast('Deck settings saved');
    } catch (error) {
      console.error('[mobile] Error saving deck settings:', error);
      showToast('Could not save deck settings');
    }
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

      const deckStudyOrderTrigger = event.target.closest('#mobile-deck-study-order-trigger');
      if (deckStudyOrderTrigger) {
        event.preventDefault();
        openDeckStudyOrderModal();
        return;
      }

      const deckSrsEnabledTrigger = event.target.closest('#mobile-deck-srs-enabled-trigger');
      if (deckSrsEnabledTrigger) {
        event.preventDefault();
        openDeckSrsEnabledModal();
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

      const studyOrderBackdrop = event.target.closest('#deck-study-order-backdrop');
      if (studyOrderBackdrop) {
        event.preventDefault();
        playClick();
        closeDeckStudyOrderModal();
        return;
      }

      const orderOpt = event.target.closest('[data-order-val]');
      if (orderOpt && event.target.closest('#deck-study-order-options')) {
        event.preventDefault();
        playClick();
        const siblings = orderOpt.parentElement.querySelectorAll('.preset-option-btn');
        siblings.forEach(sibling => sibling.classList.remove('selected'));
        orderOpt.classList.add('selected');
        
        deckSettingsStudyOrder = orderOpt.dataset.orderVal || '';
        
        setTimeout(() => {
          closeDeckStudyOrderModal();
          updateDeckStudyOrderUi();
        }, 160);
        return;
      }

      const srsEnabledBackdrop = event.target.closest('#deck-srs-enabled-backdrop');
      if (srsEnabledBackdrop) {
        event.preventDefault();
        playClick();
        closeDeckSrsEnabledModal();
        return;
      }

      const srsEnabledOpt = event.target.closest('[data-srs-val]');
      if (srsEnabledOpt && event.target.closest('#deck-srs-enabled-options')) {
        event.preventDefault();
        playClick();
        const siblings = srsEnabledOpt.parentElement.querySelectorAll('.preset-option-btn');
        siblings.forEach(sibling => sibling.classList.remove('selected'));
        srsEnabledOpt.classList.add('selected');
        
        deckSettingsSrsEnabled = srsEnabledOpt.dataset.srsVal === 'true';
        
        setTimeout(() => {
          closeDeckSrsEnabledModal();
          updateDeckSrsEnabledUi();
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

      // 8d. Context option - Settings
      const ctxSettings = event.target.closest('#context-opt-settings');
      if (ctxSettings) {
        event.preventDefault();
        if (activeContextDeckId) {
          const setId = activeContextDeckId;
          closeDeckContextModal();
          openDeckSettingsModal(setId);
        }
        return;
      }

      // Deck settings modal - Save
      const deckSettingsSave = event.target.closest('#mobile-deck-settings-save');
      if (deckSettingsSave) {
        event.preventDefault();
        await saveMobileDeckSettings();
        return;
      }

      // Deck settings modal - Cancel
      const deckSettingsCancel = event.target.closest('#mobile-deck-settings-cancel');
      if (deckSettingsCancel) {
        event.preventDefault();
        playClick();
        closeDeckSettingsModal();
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
        if (event.target.id === 'mobile-deck-settings-overlay') {
          closeDeckSettingsModal();
        } else {
          event.target.classList.add('hidden');
          state.lastModalClosedAt = Date.now();
          const cancelBtn = event.target.querySelector('.mobile-modal-btn.cancel, .cancel');
          if (cancelBtn) cancelBtn.click();
        }
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

    selectors.browserFilterStrip?.addEventListener('click', event => {
      const button = event.target.closest('[data-browser-filter]');
      if (!button) return;
      toggleBrowserFilter(button.dataset.browserFilter || 'all');
    });

    selectors.browserList?.addEventListener('click', event => {
      const selectButton = event.target.closest('[data-browser-card-select]');
      if (selectButton) {
        event.preventDefault();
        toggleBrowserCardSelection(selectButton.dataset.browserCardSelect);
        return;
      }
      const selectedRow = event.target.closest('.browser-card');
      if (selectedRow && state.browserSelectedCards?.size) {
        event.preventDefault();
        toggleBrowserCardSelection(selectedRow.dataset.cardId);
      }
    });

    selectors.browserSelectVisible?.addEventListener('click', event => {
      event.preventDefault();
      selectVisibleBrowserCards();
    });

    selectors.browserClearSelection?.addEventListener('click', event => {
      event.preventDefault();
      clearBrowserSelection();
    });

    selectors.browserSelectionBar?.addEventListener('click', async event => {
      const actionButton = event.target.closest('[data-browser-bulk-action]');
      if (!actionButton) return;
      event.preventDefault();
      playClick();
      await applyBrowserBulkAction(actionButton.dataset.browserBulkAction);
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

    const mobileSrsEnabledSelect = document.getElementById('mobile-deck-srs-enabled');
    if (mobileSrsEnabledSelect) {
      mobileSrsEnabledSelect.addEventListener('change', (e) => {
        const srsFields = document.getElementById('mobile-deck-srs-fields');
        if (srsFields) {
          srsFields.style.display = (e.target.value === 'false') ? 'none' : 'flex';
        }
      });
    }

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
