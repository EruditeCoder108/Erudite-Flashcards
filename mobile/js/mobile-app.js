(function () {
  const core = window.EruditeCore || {};
  const schema = core.schema;
  const statsCore = core.stats;
  const draftCore = core.draft;

  const CREATOR_DRAFT_KEY = 'mobileCreatorDraft';
  const BROWSER_RENDER_LIMIT = 250;
  const NORMAL_STUDY_DAILY_GOAL = 20;
  const FORMULA_SYMBOL_GROUPS = [
    {
      label: 'Basic',
      items: [
        ['+', '+'], ['-', '-'], ['×', '\\times'], ['÷', '\\div'], ['=', '='], ['≠', '\\ne'],
        ['≈', '\\approx'], ['±', '\\pm'], ['≤', '\\le'], ['≥', '\\ge'], ['∞', '\\infty']
      ]
    },
    {
      label: 'Greek',
      items: [
        ['α', '\\alpha'], ['β', '\\beta'], ['γ', '\\gamma'], ['Δ', '\\Delta'], ['θ', '\\theta'],
        ['λ', '\\lambda'], ['μ', '\\mu'], ['π', '\\pi'], ['ρ', '\\rho'], ['σ', '\\sigma'],
        ['φ', '\\phi'], ['ω', '\\omega'], ['Ω', '\\Omega']
      ]
    },
    {
      label: 'Templates',
      items: [
        ['a⁄b', '\\frac{|}{}'], ['√', '\\sqrt{|}'], ['x²', '^{|}'], ['x₁', '_{|}'],
        ['Σ', '\\sum_{i=1}^{n} |'], ['∫', '\\int |\\,dx'], ['lim', '\\lim_{x\\to 0} |'],
        ['d/dx', '\\frac{d}{dx}|'], ['∂', '\\partial |']
      ]
    },
    {
      label: 'Physics',
      items: [
        ['→', '\\rightarrow'], ['←', '\\leftarrow'], ['·', '\\cdot'], ['vec', '\\vec{|}'],
        ['hat', '\\hat{|}'], ['°', '^\\circ'], ['m/s', '\\mathrm{m/s}'], ['N', '\\mathrm{N}'],
        ['J', '\\mathrm{J}'], ['kg', '\\mathrm{kg}'], ['C', '\\mathrm{C}']
      ]
    },
    {
      label: 'Laws',
      items: [
        ['F=ma', 'F=ma'], ['E=mc²', 'E=mc^2'], ['V=IR', 'V=IR'],
        ['p=mv', 'p=mv'], ['KE', 'KE=\\frac{1}{2}mv^2'],
        ['v=u+at', 'v=u+at'], ['s=ut+½at²', 's=ut+\\frac{1}{2}at^2']
      ]
    }
  ];

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
    analyticsWindow: '30',
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
    occlusionEditor: {
      cardId: null,
      originalCard: null,
      draft: null,
      selectedMaskId: null,
      shape: 'rect',
      pointer: null
    },
    busy: false,
    creatorSaving: false,
    highlightColor: 'yellow',
    suppressNextHighlightClick: false,
    selectMode: false,
    selectedDecks: new Set(),
    lastModalClosedAt: 0
  };

  let creatorDraftTimer = null;
  let formatStateFrame = 0;
  let highlightHoldTimer = null;
  let creatorDeleteHoldTimer = null;
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
  const CREATOR_IMPORT_MAX_CARDS = 999;
  const OCCLUSION_MAX_MASKS = 80;
  const OCCLUSION_MIN_SIZE = 0.035;

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
    customStudyPanel: document.getElementById('custom-study-panel'),
    continueList: document.getElementById('continue-list'),
    activityList: document.getElementById('activity-list'),
    libraryList: document.getElementById('library-list'),
    createForm: document.getElementById('mobile-create-form'),
    createTitle: document.getElementById('mobile-create-title'),
    createClassLabel: document.getElementById('mobile-create-class-label'),
    creatorCards: document.getElementById('mobile-creator-cards'),
    imageInput: document.getElementById('mobile-image-input'),
    occlusionImageInput: document.getElementById('mobile-occlusion-image-input'),
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
    htmlInteractionSwitch: document.getElementById('html-interaction-switch'),
    moreHtmlInteractionLabel: document.getElementById('more-html-interaction-label'),
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
    formulaPreview: document.getElementById('formula-preview'),
    formulaSymbolGrid: document.getElementById('formula-symbol-grid'),
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
    bulkCardOverlay: document.getElementById('bulk-card-overlay'),
    bulkCardCount: document.getElementById('bulk-card-count'),
    bulkCardConfirm: document.getElementById('bulk-card-confirm'),
    bulkCardCancel: document.getElementById('bulk-card-cancel'),
    occlusionOverlay: document.getElementById('occlusion-editor-overlay'),
    occlusionStage: document.getElementById('occlusion-editor-stage'),
    occlusionImage: document.getElementById('occlusion-editor-image'),
    occlusionLayer: document.getElementById('occlusion-editor-layer'),
    occlusionStatus: document.getElementById('occlusion-editor-status'),
    occlusionClose: document.getElementById('occlusion-editor-close'),
    occlusionCancel: document.getElementById('occlusion-editor-cancel'),
    occlusionSave: document.getElementById('occlusion-editor-save'),
    occlusionAddMask: document.getElementById('occlusion-add-mask'),
    occlusionDeleteMask: document.getElementById('occlusion-delete-mask'),
    occlusionShapeRect: document.getElementById('occlusion-shape-rect'),
    occlusionShapeEllipse: document.getElementById('occlusion-shape-ellipse'),
    occlusionAnswer: document.getElementById('occlusion-answer-input'),
    occlusionHint: document.getElementById('occlusion-hint-input'),
    importHelpOverlay: document.getElementById('import-help-overlay'),
    importHelpCopy: document.getElementById('import-help-copy'),
    importHelpClose: document.getElementById('import-help-close'),
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
        if (state.activeTab === 'today') {
          renderAnalyticsDashboard();
          renderCustomStudyPanel();
        }
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
      headerImportBtn.classList.remove('hidden');
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

  function normalizeAnalyticsWindow(value) {
    return ['7', '30', '90', 'all'].includes(String(value)) ? String(value) : '30';
  }

  function analyticsWindowLabel(value = state.analyticsWindow) {
    const labels = {
      '7': '7 days',
      '30': '30 days',
      '90': '90 days',
      all: 'All time'
    };
    return labels[normalizeAnalyticsWindow(value)] || labels['30'];
  }

  function cardRatingCounts(card, windowKey = state.analyticsWindow) {
    const key = normalizeAnalyticsWindow(windowKey);
    return card?.ratingWindows?.[key] || (key === 'all' ? card?.ratingCounts : null) || emptyRatingCounts();
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

  function analyticsSummary(cards = [], windowKey = state.analyticsWindow) {
    const summary = {
      totalCards: cards.length,
      activeCards: 0,
      reviewedCards: 0,
      dueCards: 0,
      overdueCards: 0,
      leechCards: 0,
      weakCards: 0,
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
      if (card?.leech || card?.failedRecently) summary.weakCards += 1;
      if (Number(card?.reviewCount || card?.reps || 0) > 0 || card?.lastReviewedAt) summary.reviewedCards += 1;

      const counts = cardRatingCounts(card, windowKey);
      addRatingCounts(summary.ratingCounts, counts);
      const bucket = analyticsCardBucket(card);
      if (buckets[bucket]) addRatingCounts(buckets[bucket].counts, counts);
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

  function studyActivitySummary() {
    const summary = {
      todayStudyMs: 0,
      weekStudyMs: 0,
      todayCardsViewed: 0,
      weekCardsViewed: 0,
      todaySessions: 0,
      weekSessions: 0,
      averageSecondsPerCard: null
    };
    const todayStart = startOfLocalDayMs();
    const weekStart = todayStart - 6 * DAY_MS;
    (state.studySessions || []).filter(isTrackedStudySession).forEach(session => {
      const started = normalizeTimestamp(session.startedAt);
      const duration = Number(session.durationMs || 0);
      const cardsViewed = Number(session.cardsViewed || 0);
      if (started >= todayStart) {
        summary.todayStudyMs += duration;
        summary.todayCardsViewed += cardsViewed;
        summary.todaySessions += 1;
      }
      if (started >= weekStart) {
        summary.weekStudyMs += duration;
        summary.weekCardsViewed += cardsViewed;
        summary.weekSessions += 1;
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

  function buildDeckHealth(cards = [], windowKey = state.analyticsWindow) {
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
        weak: 0,
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
          weak: 0,
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
      if (card?.leech || card?.failedRecently) row.weak += 1;
      addRatingCounts(row.counts, cardRatingCounts(card, windowKey));
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
        const weakRatio = total ? row.weak / total : 0;
        const leechRatio = total ? row.leeches / total : 0;
        const baseline = Number.isFinite(Number(retention)) ? Number(retention) : (rate.total > 0 ? 70 : 64);
        const score = clamp(Math.round(baseline - dueRatio * 20 - overdueRatio * 35 - weakRatio * 20 - leechRatio * 25), 0, 100);
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
      .sort((a, b) => a.score - b.score || b.overdue - a.overdue || b.weak - a.weak || b.due - a.due)
      .slice(0, 4);
  }

  function renderAnalyticsDashboard() {
    if (!selectors.analyticsDashboard) return;
    const totals = totalStats({ forceDue: state.srsMode });
    if (!totals.cardCount) {
      selectors.analyticsDashboard.innerHTML = emptyPanel('fa-chart-simple', 'No insights yet', 'Create or import a deck to see study analytics.');
      return;
    }

    if (!state.srsMode) {
      const activity = studyActivitySummary();
      const heatmap = buildStudyHeatmap();
      const avgTime = activity.averageSecondsPerCard === null ? '--' : `${activity.averageSecondsPerCard}s`;
      const heatmapHtml = heatmap.map(day => `
        <span class="heatmap-cell level-${day.level}" title="${escapeAttr(`${day.label}: ${day.score ? `${day.score} activity` : 'No study'}`)}"></span>
      `).join('');

      selectors.analyticsDashboard.innerHTML = `
        <div class="insight-grid">
          <article class="insight-card">
            <span class="insight-icon"><i class="fas fa-layer-group"></i></span>
            <div>
              <small>Library</small>
              <strong>${formatShortNumber(totals.cardCount)}</strong>
              <p>${formatShortNumber(totals.setCount)} decks</p>
            </div>
          </article>
          <article class="insight-card">
            <span class="insight-icon calm"><i class="fas fa-stopwatch"></i></span>
            <div>
              <small>Today</small>
              <strong>${formatDuration(activity.todayStudyMs)}</strong>
              <p>${formatShortNumber(activity.todayCardsViewed)} cards viewed</p>
            </div>
          </article>
          <article class="insight-card">
            <span class="insight-icon warn"><i class="fas fa-fire"></i></span>
            <div>
              <small>Habit</small>
              <strong>${streakDays()}</strong>
              <p>day streak</p>
            </div>
          </article>
          <article class="insight-card">
            <span class="insight-icon"><i class="fas fa-gauge-high"></i></span>
            <div>
              <small>Pace</small>
              <strong>${avgTime}</strong>
              <p>${formatShortNumber(activity.weekCardsViewed)} cards this week</p>
            </div>
          </article>
        </div>

        <article class="insight-panel">
          <div class="insight-panel-head">
            <strong>Study heatmap</strong>
            <span>${formatDuration(activity.weekStudyMs)} this week</span>
          </div>
          <div class="study-heatmap">${heatmapHtml}</div>
        </article>
      `;
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
    const analyticsWindow = normalizeAnalyticsWindow(state.analyticsWindow);
    const windowLabel = analyticsWindowLabel(analyticsWindow);
    const summary = analyticsSummary(cards, analyticsWindow);
    const forecast = buildForecast(cards);
    const heatmap = buildStudyHeatmap();
    const deckHealth = buildDeckHealth(cards, analyticsWindow);
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
              <span>${escapeHtml(deck.workload)} &middot; ${formatShortNumber(deck.due)} due &middot; ${formatShortNumber(deck.weak)} weak</span>
            </div>
            <b>${deck.score}</b>
          </article>
        `).join('')
      : '<div class="insight-muted">No deck pressure yet.</div>';

    selectors.analyticsDashboard.innerHTML = `
      <div class="insight-controls" role="group" aria-label="Analytics time window">
        ${[
          ['7', '7d'],
          ['30', '30d'],
          ['90', '90d'],
          ['all', 'All']
        ].map(([value, label]) => `
          <button type="button" class="${analyticsWindow === value ? 'active' : ''}" data-action="analytics-window" data-window="${escapeAttr(value)}" aria-pressed="${analyticsWindow === value ? 'true' : 'false'}">
            ${escapeHtml(label)}
          </button>
        `).join('')}
      </div>
      <div class="insight-grid">
        <article class="insight-card insight-score">
          <span class="insight-icon"><i class="fas fa-bullseye"></i></span>
          <div>
            <small>Actual retention</small>
            <strong>${retentionLabel}</strong>
            <p>${formatShortNumber(summary.reviewEvents)} reviews, ${escapeHtml(windowLabel)}</p>
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
            <strong>${formatShortNumber(summary.weakCards)}</strong>
            <p>${formatShortNumber(summary.failedRecently)} failed recently, ${formatShortNumber(summary.leechCards)} leeches</p>
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
            <span>${escapeHtml(windowLabel)}</span>
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

  function customStudyFilterLabel(filter, tag = '') {
    const labels = {
      'failed-today': 'Failed Today',
      overdue: 'Overdue',
      'review-ahead': 'Review Ahead',
      leeches: 'Weak Cards',
      tag: tag ? `#${tag}` : 'Tag'
    };
    return labels[filter] || 'Custom Study';
  }

  function customStudyFilterIcon(filter) {
    const icons = {
      'failed-today': 'fa-arrow-rotate-left',
      overdue: 'fa-calendar-xmark',
      'review-ahead': 'fa-calendar-plus',
      leeches: 'fa-triangle-exclamation',
      tag: 'fa-tag'
    };
    return icons[filter] || 'fa-filter';
  }

  function cardMatchesCustomStudyFilter(card, filter, tag = '') {
    const dueTime = normalizeTimestamp(card?.dueTime || card?.due);
    const todayStart = startOfLocalDayMs();
    const tomorrowStart = todayStart + DAY_MS;
    const weekEnd = todayStart + 8 * DAY_MS;
    switch (filter) {
      case 'failed-today':
        return Boolean(card?.failedToday);
      case 'overdue':
        return Boolean(card?.isOverdue);
      case 'review-ahead':
        return Boolean(dueTime && dueTime >= tomorrowStart && dueTime < weekEnd && !card?.suspended && !card?.buried);
      case 'leeches':
        return Boolean(card?.leech || card?.failedRecently);
      case 'tag':
        return Boolean(tag && (card?.tags || []).map(item => String(item).toLowerCase()).includes(String(tag).toLowerCase()));
      default:
        return false;
    }
  }

  function customStudyCandidates(filter, tag = '') {
    return (state.analyticsCards || []).filter(card => cardMatchesCustomStudyFilter(card, filter, tag));
  }

  function customStudyDeckChoice(filter, tag = '') {
    const rows = new Map();
    customStudyCandidates(filter, tag).forEach(card => {
      const setId = String(card?.setId || '');
      if (!setId) return;
      const current = rows.get(setId) || {
        setId,
        deck: card?.deck || 'Untitled Set',
        count: 0,
        due: 0,
        overdue: 0
      };
      current.count += 1;
      if (card?.isDue) current.due += 1;
      if (card?.isOverdue) current.overdue += 1;
      rows.set(setId, current);
    });
    return Array.from(rows.values())
      .sort((a, b) => b.count - a.count || b.overdue - a.overdue || b.due - a.due)[0] || null;
  }

  function topCustomStudyTags(cards = [], limit = 3) {
    const counts = new Map();
    cards.forEach(card => {
      (card?.tags || []).forEach(tag => {
        const clean = String(tag || '').trim();
        if (!clean) return;
        counts.set(clean, (counts.get(clean) || 0) + 1);
      });
    });
    return Array.from(counts.entries())
      .sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))
      .slice(0, limit)
      .map(([tag, count]) => ({ tag, count }));
  }

  function buildCustomStudyItems() {
    const base = [
      { filter: 'failed-today', label: 'Failed Today', copy: 'Practice cards missed today.' },
      { filter: 'overdue', label: 'Overdue', copy: 'Clear stale reviews safely.' },
      { filter: 'review-ahead', label: 'Review Ahead', copy: 'Practice cards due this week.' },
      { filter: 'leeches', label: 'Weak Cards', copy: 'Focus on leeches.' }
    ].map(item => ({
      ...item,
      choice: customStudyDeckChoice(item.filter)
    }));

    const tagItems = topCustomStudyTags(state.analyticsCards, 3).map(item => ({
      filter: 'tag',
      tag: item.tag,
      label: `#${item.tag}`,
      copy: `${formatShortNumber(item.count)} tagged cards.`,
      choice: customStudyDeckChoice('tag', item.tag)
    }));

    return [...base, ...tagItems].filter(item => item.choice?.count > 0).slice(0, 6);
  }

  function renderCustomStudyPanel() {
    if (!selectors.customStudyPanel) return;
    const totals = totalStats({ forceDue: state.srsMode });
    if (!totals.cardCount) {
      selectors.customStudyPanel.innerHTML = emptyPanel('fa-filter', 'No custom sessions yet', 'Create or import a deck first.');
      return;
    }
    if (!state.srsMode) {
      selectors.customStudyPanel.innerHTML = emptyPanel('fa-filter', 'SRS filters are hidden', 'Turn on SRS to use failed, overdue, review-ahead, and weak-card sessions.');
      return;
    }
    if (state.analyticsError) {
      selectors.customStudyPanel.innerHTML = emptyPanel('fa-filter', 'Custom study unavailable', 'Refresh insights to rebuild card filters.');
      return;
    }
    if (!state.analyticsLoaded) {
      if (!state.analyticsLoading && state.activeTab === 'today') {
        loadAnalyticsCards().catch(() => {});
      }
      selectors.customStudyPanel.innerHTML = emptyPanel('fa-spinner', 'Preparing filters', 'Reading card metadata.');
      return;
    }

    const items = buildCustomStudyItems();
    if (!items.length) {
      selectors.customStudyPanel.innerHTML = emptyPanel('fa-filter', 'Nothing needs a custom session', 'Weak, overdue, review-ahead, and tag sessions will appear here.');
      return;
    }

    selectors.customStudyPanel.innerHTML = `
      <div class="custom-study-grid">
        ${items.map(item => `
          <article class="custom-study-card">
            <span class="insight-icon"><i class="fas ${escapeAttr(customStudyFilterIcon(item.filter))}"></i></span>
            <strong>${escapeHtml(item.label)}</strong>
            <small>${formatShortNumber(item.choice.count)} cards in ${escapeHtml(item.choice.deck)}</small>
            <em>${escapeHtml(item.copy)}</em>
            <div class="custom-study-actions">
              <button type="button" data-action="start-custom-study" data-filter="${escapeAttr(item.filter)}" data-tag="${escapeAttr(item.tag || '')}">
                Practice
              </button>
              <button type="button" class="primary" data-action="start-custom-study-reschedule" data-filter="${escapeAttr(item.filter)}" data-tag="${escapeAttr(item.tag || '')}">
                SRS Review
              </button>
            </div>
          </article>
        `).join('')}
      </div>
    `;
  }

  function renderToday() {
    const totals = totalStats({ forceDue: state.srsMode });
    const todayReviews = reviewsToday();
    const activity = studyActivitySummary();
    const streak = streakDays();
    const hasDecks = totals.setCount > 0 || totals.cardCount > 0;
    const remainingReviews = state.srsMode ? Number(totals.dueCards || 0) : 0;
    const dailyWork = state.srsMode ? todayReviews + remainingReviews : activity.todayCardsViewed;
    const normalStudyGoal = hasDecks ? Math.max(1, Math.min(NORMAL_STUDY_DAILY_GOAL, Number(totals.cardCount || 0) || NORMAL_STUDY_DAILY_GOAL)) : 0;
    const progress = state.srsMode
      ? (dailyWork > 0 ? clamp(Math.round((todayReviews / dailyWork) * 100), 0, 100) : (hasDecks ? 100 : 0))
      : (normalStudyGoal > 0 ? clamp(Math.round((activity.todayCardsViewed / normalStudyGoal) * 100), 0, 100) : 0);
    const progressLabel = state.srsMode
      ? (dailyWork > 0 ? 'Goal' : (hasDecks ? 'Ready' : 'Start'))
      : (hasDecks ? 'Goal' : 'Start');
    const reviewAction = state.srsMode && totals.dueCards > 0 ? 'review-due-smart' : (hasDecks ? 'tab-library' : 'open-create');
    const reviewLabel = state.srsMode && totals.dueCards > 0 ? `Review ${totals.dueCards} Left` : (hasDecks ? 'Study Decks' : 'Create Deck');
    const middleMetricValue = state.srsMode ? todayReviews : activity.todayCardsViewed;
    const middleMetricLabel = state.srsMode ? 'Reviewed' : 'Studied';

    selectors.todayHero.innerHTML = `
      <div class="hero-dashboard">
        <div class="goal-ring" style="--progress:${progress * 3.6}deg">
          <div><strong>${progress}%</strong><span>${progressLabel}</span></div>
        </div>
        <div class="hero-metrics">
          <div class="metric-pill"><strong>${totals.setCount}</strong><span>Decks</span></div>
          <div class="metric-pill"><strong>${middleMetricValue}</strong><span>${middleMetricLabel}</span></div>
          <div class="metric-pill"><strong>${streak}</strong><span>Day streak</span></div>
        </div>
      </div>
      <div class="hero-actions">
        <button type="button" class="primary-action" data-action="${reviewAction}">
          <i class="fas ${state.srsMode && totals.dueCards > 0 ? 'fa-brain' : 'fa-layer-group'}"></i>
          ${escapeHtml(reviewLabel)}
        </button>
        <button type="button" class="secondary-action" data-action="open-create">
          <i class="fas fa-plus"></i>
          New
        </button>
      </div>
    `;

    renderAnalyticsDashboard();
    renderCustomStudyPanel();

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
    const allowed = new Set(['B', 'STRONG', 'I', 'EM', 'U', 'BR', 'DIV', 'P', 'UL', 'OL', 'LI', 'SPAN', 'MARK', 'CODE', 'PRE', 'BLOCKQUOTE', 'HR']);
    const allowedHighlightClasses = new Set(['highlight-yellow', 'highlight-green', 'highlight-blue', 'highlight-pink']);
    const walk = document.createTreeWalker(template.content, NodeFilter.SHOW_ELEMENT);
    const nodes = [];
    while (walk.nextNode()) nodes.push(walk.currentNode);
    nodes.forEach(node => {
      if (!allowed.has(node.tagName)) {
        node.replaceWith(document.createTextNode(node.textContent || ''));
        return;
      }
      Array.from(node.attributes).forEach(attr => {
        if (node.tagName === 'MARK' && attr.name === 'class') {
          const safeClasses = String(attr.value || '')
            .split(/\s+/)
            .filter(name => allowedHighlightClasses.has(name));
          if (safeClasses.length) {
            node.setAttribute('class', safeClasses.join(' '));
            return;
          }
        }
        node.removeAttribute(attr.name);
      });
    });
    return template.innerHTML.replace(/\u200B/g, '');
  }

  const ADVANCED_HTML_MAX_LENGTH = 30000;
  const ADVANCED_CSS_MAX_LENGTH = 18000;
  const ADVANCED_HTML_CANVAS = {
    width: 340,
    height: 470,
    radius: 20
  };

  function normalizeAdvancedHtml(value = {}) {
    const source = value && typeof value === 'object' ? value : {};
    const sharedCss = String(source.css || '');
    return {
      frontHtml: String(source.frontHtml || source.html || '').slice(0, ADVANCED_HTML_MAX_LENGTH),
      backHtml: String(source.backHtml || '').slice(0, ADVANCED_HTML_MAX_LENGTH),
      frontCss: String(source.frontCss || sharedCss).slice(0, ADVANCED_CSS_MAX_LENGTH),
      backCss: String(source.backCss || sharedCss).slice(0, ADVANCED_CSS_MAX_LENGTH)
    };
  }

  function isAdvancedHtmlCard(card = {}) {
    return String(card.noteType || '').toLowerCase() === 'advanced-html'
      || String(card.cardTemplate || '').toLowerCase() === 'advanced-html';
  }

  function advancedHtmlPayload(card = {}) {
    const direct = card.advancedHtml;
    if (direct && typeof direct === 'object' && (direct.frontHtml || direct.backHtml || direct.frontCss || direct.backCss || direct.css || direct.html)) return direct;
    return card.noteFields && typeof card.noteFields === 'object' ? card.noteFields : (direct || {});
  }

  function sanitizeHtmlClassValue(value) {
    return String(value || '')
      .split(/\s+/)
      .map(item => item.replace(/[^\w:-]/g, ''))
      .filter(Boolean)
      .slice(0, 12)
      .join(' ');
  }

  function sanitizeAdvancedHtml(value) {
    const template = document.createElement('template');
    template.innerHTML = String(value || '').slice(0, ADVANCED_HTML_MAX_LENGTH);
    const allowed = new Set([
      'DIV', 'SECTION', 'ARTICLE', 'HEADER', 'FOOTER', 'MAIN',
      'H1', 'H2', 'H3', 'H4', 'H5', 'H6',
      'P', 'SPAN', 'STRONG', 'B', 'EM', 'I', 'U', 'SMALL',
      'MARK', 'CODE', 'PRE', 'BLOCKQUOTE', 'BR', 'HR',
      'UL', 'OL', 'LI',
      'TABLE', 'THEAD', 'TBODY', 'TFOOT', 'TR', 'TH', 'TD',
      'IMG', 'SUP', 'SUB'
    ]);
    const removeEntirely = new Set(['SCRIPT', 'STYLE', 'IFRAME', 'OBJECT', 'EMBED', 'LINK', 'META', 'BASE', 'FORM', 'INPUT', 'BUTTON', 'SELECT', 'TEXTAREA', 'CANVAS', 'VIDEO', 'AUDIO']);
    const walk = document.createTreeWalker(template.content, NodeFilter.SHOW_ELEMENT);
    const nodes = [];
    while (walk.nextNode()) nodes.push(walk.currentNode);
    nodes.forEach(node => {
      if (removeEntirely.has(node.tagName)) {
        node.remove();
        return;
      }
      if (!allowed.has(node.tagName)) {
        node.replaceWith(...Array.from(node.childNodes));
        return;
      }
      Array.from(node.attributes).forEach(attr => {
        const name = attr.name.toLowerCase();
        const raw = String(attr.value || '');
        if (name.startsWith('on') || name === 'style' || name === 'srcdoc' || name === 'href') {
          node.removeAttribute(attr.name);
          return;
        }
        if (name === 'class') {
          const safeClass = sanitizeHtmlClassValue(raw);
          if (safeClass) node.setAttribute('class', safeClass);
          else node.removeAttribute(attr.name);
          return;
        }
        if (name === 'id') {
          const safeId = raw.replace(/[^\w:-]/g, '').slice(0, 64);
          if (safeId) node.setAttribute('id', safeId);
          else node.removeAttribute(attr.name);
          return;
        }
        if (node.tagName === 'IMG') {
          if (name === 'src') {
            const src = safeMediaSrc(raw);
            if (src && !/^https?:\/\//i.test(src) && !/^data:image\/svg/i.test(src)) node.setAttribute('src', src);
            else node.removeAttribute(attr.name);
            return;
          }
          if (name === 'alt' || name === 'title') {
            node.setAttribute(attr.name, raw.slice(0, 160));
            return;
          }
          if ((name === 'width' || name === 'height') && /^(\d{1,4}|[1-9]\d?%)$/.test(raw.trim())) {
            node.setAttribute(attr.name, raw.trim());
            return;
          }
        }
        if ((node.tagName === 'TD' || node.tagName === 'TH') && (name === 'colspan' || name === 'rowspan') && /^\d{1,2}$/.test(raw.trim())) {
          node.setAttribute(attr.name, raw.trim());
          return;
        }
        node.removeAttribute(attr.name);
      });
    });
    return template.innerHTML.trim();
  }

  function sanitizeAdvancedCss(value) {
    let css = String(value || '').slice(0, ADVANCED_CSS_MAX_LENGTH);
    css = css.replace(/\/\*[\s\S]*?\*\//g, '');
    css = css.replace(/@import\b[^;]*;?/gi, '');
    css = css.replace(/url\s*\(\s*(['"]?)(?!data:image\/)[^)]+?\1\s*\)/gi, 'none');
    css = css.replace(/url\s*\(\s*(['"]?)data:image\/svg[^)]*?\1\s*\)/gi, 'none');
    css = css.replace(/\b(expression|javascript|vbscript)\s*\(/gi, '');
    css = css.replace(/\bposition\s*:\s*(fixed|sticky)\s*;?/gi, '');
    css = css.replace(/\bz-index\s*:\s*-?\d+\s*;?/gi, '');
    css = css.replace(/<\/?style[^>]*>/gi, '');
    css = css.replace(/<\/?script[^>]*>/gi, '');
    return css.trim();
  }

  function sanitizeAdvancedHtmlCard(value = {}) {
    const normalized = normalizeAdvancedHtml(value);
    return {
      frontHtml: sanitizeAdvancedHtml(normalized.frontHtml),
      backHtml: sanitizeAdvancedHtml(normalized.backHtml),
      frontCss: sanitizeAdvancedCss(normalized.frontCss),
      backCss: sanitizeAdvancedCss(normalized.backCss)
    };
  }

  function advancedHtmlSide(card = {}, side = 'front') {
    const html = normalizeAdvancedHtml(advancedHtmlPayload(card));
    return side === 'back'
      ? (html.backHtml || html.frontHtml || '')
      : (html.frontHtml || '');
  }

  function advancedHtmlSrcdoc(card = {}, side = 'front') {
    const html = sanitizeAdvancedHtml(advancedHtmlSide(card, side));
    const normalized = normalizeAdvancedHtml(advancedHtmlPayload(card));
    const css = sanitizeAdvancedCss(side === 'back' ? normalized.backCss : normalized.frontCss);
    const content = html || `<div class="empty-card-copy">${side === 'back' ? 'Back HTML preview' : 'Front HTML preview'}</div>`;
    return `<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><style>
      *{box-sizing:border-box}html,body{width:100%;height:100%;margin:0;background:transparent;color:#e5edf8;font-family:Inter,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;overflow:auto;overflow-wrap:anywhere}
      body{display:block;min-width:100%;min-height:100%}.erudite-html-card{display:block;min-width:100%;min-height:100%;padding:12px;line-height:1.45;overflow:visible}.erudite-html-card img{max-width:100%;height:auto;border-radius:8px}.erudite-html-card table{border-collapse:collapse}.erudite-html-card th,.erudite-html-card td{padding:6px;border:1px solid rgba(148,163,184,.25)}.empty-card-copy{display:grid;min-height:220px;place-items:center;color:#94a3b8;font-weight:800;text-align:center}
      ${css}
    </style></head><body><div class="erudite-html-card">${content}</div></body></html>`;
  }

  function advancedHtmlFallbackText(card = {}, side = 'front') {
    const text = plainTextFromHtml(advancedHtmlSide(card, side)).replace(/\s+/g, ' ').trim();
    if (text) return text.slice(0, 500);
    return '';
  }

  async function copyPlainText(text) {
    try {
      await navigator.clipboard.writeText(text);
      return true;
    } catch (_) {
      const textarea = document.createElement('textarea');
      textarea.value = text;
      textarea.setAttribute('readonly', '');
      textarea.style.position = 'fixed';
      textarea.style.opacity = '0';
      document.body.appendChild(textarea);
      textarea.select();
      const ok = document.execCommand('copy');
      textarea.remove();
      return ok;
    }
  }

  function buildAdvancedHtmlPrompt(card = {}) {
    const frontText = plainTextFromHtml(card.term || advancedHtmlSide(card, 'front')).replace(/\s+/g, ' ').trim();
    const backText = plainTextFromHtml(card.definition || advancedHtmlSide(card, 'back')).replace(/\s+/g, ' ').trim();
    return [
      'Create an Erudite mobile flashcard using HTML and CSS only.',
      '',
      'Return exactly four fenced code blocks with these labels:',
      'FRONT_HTML',
      'FRONT_CSS',
      'BACK_HTML',
      'BACK_CSS',
      '',
      'Hard rules:',
      '- No JavaScript, no <script>, no event attributes, no external URLs, no @import.',
      '- No iframe, form, input, button, audio, video, canvas, fixed/sticky positioning, or z-index tricks.',
      '- Do not include the app shell, <article>, .card-scroll, or iframe in the returned HTML.',
      '- Use one root wrapper such as <div class="card-design"> in each HTML block.',
      '- Use only classes/IDs that belong to the card design.',
      '- The custom HTML lives inside a smaller sandbox inside the flashcard, not the full card.',
      `- Exact design canvas: ${ADVANCED_HTML_CANVAS.width}px wide x ${ADVANCED_HTML_CANVAS.height}px tall, ${ADVANCED_HTML_CANVAS.radius}px corner radius.`,
      '- Treat those as CSS pixels, not physical screenshot pixels.',
      `- Your root .card-design should be width: ${ADVANCED_HTML_CANVAS.width}px; min-height: ${ADVANCED_HTML_CANVAS.height}px; border-radius: ${ADVANCED_HTML_CANVAS.radius}px; overflow: hidden or auto.`,
      '- Prefer responsive inner layout using max-width: 100%, flexible rows/columns, and readable spacing.',
      `- Avoid fixed inner heights taller than ${ADVANCED_HTML_CANVAS.height}px unless the content is intentionally scrollable.`,
      '- Keep text readable, responsive, and friendly to math/physics formulas and step-by-step solutions.',
      '',
      'The app renders your result like this:',
      '<article class="card-face">',
      '  <div class="card-scroll">',
      '    <div class="card-label">TERM or DEFINITION</div>',
      `    <div class="advanced-html-study-frame" style="width:${ADVANCED_HTML_CANVAS.width}px;height:${ADVANCED_HTML_CANVAS.height}px;border-radius:${ADVANCED_HTML_CANVAS.radius}px;overflow:auto;">`,
      '      #shadow-root',
      '      <div class="erudite-html-card">YOUR HTML/CSS DESIGN FILLS THIS CANVAS</div>',
      '    </div>',
      '  </div>',
      '</article>',
      '',
      `Front content: ${frontText || '[write the question/front here]'}`,
      `Back content: ${backText || '[write the answer/back here]'}`,
      '',
      'Make the front feel like the question side and the back feel like the revealed answer side.'
    ].join('\n');
  }

  function richEditorForNode(node) {
    const element = node?.nodeType === Node.ELEMENT_NODE ? node : node?.parentElement;
    return element?.closest?.('.rich-editor') || null;
  }

  function activeRichEditor() {
    const selection = window.getSelection();
    if (selection?.rangeCount) {
      const anchorEditor = richEditorForNode(selection.anchorNode);
      const focusEditor = richEditorForNode(selection.focusNode);
      if (anchorEditor && anchorEditor === focusEditor) return anchorEditor;
    }
    return document.activeElement?.closest?.('.rich-editor') || null;
  }

  function selectionRangeInEditor(editor) {
    if (!editor) return null;
    const selection = window.getSelection();
    if (!selection?.rangeCount) return null;
    const range = selection.getRangeAt(0);
    if (!editor.contains(range.commonAncestorContainer)) return null;
    return range;
  }

  function selectionHtml(range) {
    const container = document.createElement('div');
    container.appendChild(range.cloneContents());
    return sanitizeEditorHtml(container.innerHTML);
  }

  function replaceSelectionHtml(editor, html) {
    editor.focus();
    document.execCommand('insertHTML', false, sanitizeEditorHtml(html));
    syncCreatorFromDom();
    updateFormatState();
    scheduleCreatorDraftSave();
  }

  function placeCaretInside(node) {
    const selection = window.getSelection();
    if (!selection) return;
    const range = document.createRange();
    if (node.nodeType === Node.TEXT_NODE) {
      range.setStart(node, node.textContent.length);
    } else {
      range.selectNodeContents(node);
      range.collapse(false);
    }
    selection.removeAllRanges();
    selection.addRange(range);
  }

  function insertElementAtRange(editor, element, range) {
    const activeRange = range || selectionRangeInEditor(editor);
    if (!activeRange) return false;
    activeRange.deleteContents();
    activeRange.insertNode(element);
    editor.focus();
    return true;
  }

  function wrapOrStartInlineElement(tagName, options = {}) {
    const editor = activeRichEditor();
    if (!editor) {
      showToast('Tap a card field first');
      return false;
    }
    const range = selectionRangeInEditor(editor);
    if (!range) {
      showToast('Tap where you want to type');
      return false;
    }
    const element = document.createElement(tagName);
    if (options.className) element.className = options.className;
    if (range.collapsed) {
      const text = document.createTextNode('\u200B');
      element.appendChild(text);
      if (!insertElementAtRange(editor, element, range)) return false;
      placeCaretInside(text);
    } else {
      element.appendChild(range.extractContents());
      range.insertNode(element);
      placeCaretInside(element);
    }
    syncCreatorFromDom();
    updateFormatState();
    scheduleCreatorDraftSave();
    return true;
  }

  function insertCodeBlockAtCaret() {
    const editor = activeRichEditor();
    if (!editor) {
      showToast('Tap a card field first');
      return false;
    }
    const range = selectionRangeInEditor(editor);
    if (!range) {
      showToast('Tap where you want to type');
      return false;
    }
    const pre = document.createElement('pre');
    const code = document.createElement('code');
    if (range.collapsed) {
      code.appendChild(document.createTextNode('\u200B'));
    } else {
      code.textContent = range.toString();
    }
    pre.appendChild(code);
    const spacer = document.createElement('div');
    spacer.appendChild(document.createElement('br'));
    range.deleteContents();
    range.insertNode(spacer);
    range.insertNode(pre);
    editor.focus();
    placeCaretInside(code.firstChild || code);
    syncCreatorFromDom();
    updateFormatState();
    scheduleCreatorDraftSave();
    return true;
  }

  function insertClozeAtCaret(cardId, side) {
    const editor = selectors.creatorCards?.querySelector(`[data-editor-id="${cssEscape(cardId)}"][data-side="${side}"]`);
    if (!editor) return false;
    editor.focus();
    const range = selectionRangeInEditor(editor);
    if (!range) return false;
    const cardIndex = state.creator.cards.findIndex(card => String(card.id) === String(cardId));
    const sourceCard = cardIndex >= 0 ? state.creator.cards[cardIndex] : {};
    const existingIndexes = clozeIndexesFromText(`${sourceCard.term || ''} ${sourceCard.definition || ''}`);
    const nextIndex = existingIndexes.length ? Math.max(...existingIndexes) + 1 : 1;
    const selected = range.collapsed ? '' : range.toString().trim();
    const before = document.createTextNode(`{{c${nextIndex}::`);
    const hidden = document.createTextNode(selected || '\u200B');
    const after = document.createTextNode('}}');
    range.deleteContents();
    range.insertNode(after);
    range.insertNode(hidden);
    range.insertNode(before);
    placeCaretInside(hidden);
    syncCreatorFromDom();
    if (cardIndex >= 0) {
      state.creator.cards[cardIndex] = {
        ...state.creator.cards[cardIndex],
        noteType: 'cloze',
        cardTemplate: 'cloze-source'
      };
    }
    scheduleCreatorDraftSave();
    showToast('Cloze ready');
    return true;
  }

  function selectionHasAncestor(tagNames = []) {
    const selection = window.getSelection();
    if (!selection?.rangeCount) return false;
    const wanted = new Set(tagNames.map(tag => String(tag).toUpperCase()));
    let node = selection.anchorNode;
    while (node && node !== selectors.creatorCards) {
      if (node.nodeType === Node.ELEMENT_NODE && wanted.has(node.tagName)) return true;
      node = node.parentNode;
    }
    return false;
  }

  function insertHighlightContent() {
    return wrapOrStartInlineElement('mark', { className: `highlight-${state.highlightColor || 'yellow'}` });
  }

  function insertInlineCodeContent() {
    return wrapOrStartInlineElement('code');
  }

  function insertCodeBlockContent() {
    return insertCodeBlockAtCaret();
  }

  async function openHighlightColorMenu() {
    const next = await openBrowserFieldModal({
      title: 'Highlight Color',
      icon: 'fa-highlighter',
      message: 'Choose the color used by the highlight tool.',
      options: [
        { value: 'yellow', label: 'Yellow' },
        { value: 'green', label: 'Green' },
        { value: 'blue', label: 'Blue' },
        { value: 'pink', label: 'Pink' }
      ],
      value: state.highlightColor || 'yellow',
      okText: 'Use Color'
    });
    if (!next) return;
    state.highlightColor = ['yellow', 'green', 'blue', 'pink'].includes(next) ? next : 'yellow';
    showToast(`${state.highlightColor[0].toUpperCase()}${state.highlightColor.slice(1)} highlight`);
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
    const advancedHtml = normalizeAdvancedHtml(advancedHtmlPayload(card));
    const occlusion = normalizeImageOcclusion(card.imageOcclusion, card);
    return Boolean(
      plainTextFromHtml(card.term || '').trim()
      || plainTextFromHtml(card.definition || '').trim()
      || sanitizeAdvancedHtml(advancedHtml.frontHtml)
      || sanitizeAdvancedHtml(advancedHtml.backHtml)
      || (occlusion.image && occlusion.masks.length)
      || card.termImage
      || card.definitionImage
      || media.term.length
      || media.definition.length
      || background.term
      || background.definition
    );
  }

  function createLocalId(prefix) {
    return schema?.createId ? schema.createId(prefix) : `${prefix}-${Date.now()}-${Math.random().toString(36).slice(2)}`;
  }

  function emptyCreatorCard() {
    const now = Date.now();
    const noteId = createLocalId('note');
    return {
      id: createLocalId('card'),
      noteId,
      noteType: 'basic',
      cardTemplate: 'front-back',
      noteFields: {},
      clozeIndex: null,
      imageOcclusion: null,
      advancedHtml: { frontHtml: '', backHtml: '', frontCss: '', backCss: '' },
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

  function boundedBulkCardCount(value) {
    const count = Number.parseInt(String(value || '').trim(), 10);
    if (!Number.isFinite(count)) return 1;
    return Math.min(999, Math.max(1, count));
  }

  function scrollCreatorCardIntoView(cardId, block = 'center') {
    requestAnimationFrame(() => {
      const cardEl = selectors.creatorCards?.querySelector(`[data-card-id="${cssEscape(cardId)}"]`);
      cardEl?.scrollIntoView({ behavior: 'smooth', block });
    });
  }

  function focusCreatorCard(cardId) {
    requestAnimationFrame(() => {
      const editor = selectors.creatorCards?.querySelector(`[data-editor-id="${cssEscape(cardId)}"][data-side="term"], [data-html-editor-id="${cssEscape(cardId)}"]`);
      if (editor) {
        editor.focus();
        editor.closest('.mobile-card-editor')?.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    });
  }

  function openBulkCardModal() {
    if (!selectors.bulkCardOverlay || !selectors.bulkCardCount) return;
    selectors.bulkCardCount.value = selectors.bulkCardCount.value || '10';
    selectors.bulkCardOverlay.classList.remove('hidden');
    requestAnimationFrame(() => {
      selectors.bulkCardCount?.focus();
      selectors.bulkCardCount?.select?.();
    });
  }

  function closeBulkCardModal() {
    selectors.bulkCardOverlay?.classList.add('hidden');
    state.lastModalClosedAt = Date.now();
  }

  function addBlankCreatorCards(count, insertAt = state.creator.cards.length) {
    const safeCount = boundedBulkCardCount(count);
    const cards = Array.from({ length: safeCount }, () => emptyCreatorCard());
    const safeIndex = Math.min(Math.max(0, insertAt), state.creator.cards.length);
    state.creator.cards.splice(safeIndex, 0, ...cards);
    return cards;
  }

  async function confirmDeleteCardsFrom(cardId) {
    syncCreatorFromDom();
    const index = state.creator.cards.findIndex(card => String(card.id) === String(cardId));
    if (index < 0) return;
    const count = state.creator.cards.length - index;
    const ok = await showMobileConfirm({
      title: 'Delete Cards',
      message: `Delete Card ${index + 1} and every card below it? This removes ${count} ${count === 1 ? 'card' : 'cards'} and all content in them from this draft.`,
      okText: `Delete ${count}`,
      isDanger: true
    });
    if (!ok) return;
    state.creator.cards.splice(index, count);
    ensureCreatorCard();
    renderCreate();
    scheduleCreatorDraftSave();
    showToast(`${count} ${count === 1 ? 'card' : 'cards'} deleted`);
  }

  function selectedOcclusionMask() {
    const draft = state.occlusionEditor.draft;
    if (!draft) return null;
    return (draft.masks || []).find(mask => String(mask.id) === String(state.occlusionEditor.selectedMaskId)) || null;
  }

  function setOcclusionShape(shape) {
    state.occlusionEditor.shape = shape === 'ellipse' ? 'ellipse' : 'rect';
    selectors.occlusionShapeRect?.classList.toggle('active', state.occlusionEditor.shape === 'rect');
    selectors.occlusionShapeEllipse?.classList.toggle('active', state.occlusionEditor.shape === 'ellipse');
  }

  function renderedImageContentRect(img, container) {
    if (!img || !container) return null;
    const containerRect = container.getBoundingClientRect();
    const imageRect = img.getBoundingClientRect();
    let boxWidth = imageRect.width;
    let boxHeight = imageRect.height;
    let boxLeft = imageRect.left - containerRect.left;
    let boxTop = imageRect.top - containerRect.top;

    if (!boxWidth || !boxHeight) {
      boxWidth = container.clientWidth || containerRect.width;
      boxHeight = container.clientHeight || containerRect.height;
      boxLeft = 0;
      boxTop = 0;
    }

    const naturalWidth = img.naturalWidth || boxWidth;
    const naturalHeight = img.naturalHeight || boxHeight;
    if (!naturalWidth || !naturalHeight || !boxWidth || !boxHeight) {
      return { left: boxLeft, top: boxTop, width: boxWidth, height: boxHeight };
    }

    const fit = window.getComputedStyle?.(img)?.objectFit || 'fill';
    let contentWidth = boxWidth;
    let contentHeight = boxHeight;

    if (fit === 'contain' || fit === 'scale-down') {
      const scale = Math.min(boxWidth / naturalWidth, boxHeight / naturalHeight);
      contentWidth = naturalWidth * scale;
      contentHeight = naturalHeight * scale;
    } else if (fit === 'cover') {
      const scale = Math.max(boxWidth / naturalWidth, boxHeight / naturalHeight);
      contentWidth = naturalWidth * scale;
      contentHeight = naturalHeight * scale;
    }

    return {
      left: boxLeft + (boxWidth - contentWidth) / 2,
      top: boxTop + (boxHeight - contentHeight) / 2,
      width: contentWidth,
      height: contentHeight
    };
  }

  function syncOcclusionLayerRect() {
    const stage = selectors.occlusionStage;
    const image = selectors.occlusionImage;
    const layer = selectors.occlusionLayer;
    if (!stage || !image || !layer) return;
    const rect = renderedImageContentRect(image, stage);
    if (!rect || rect.width <= 0 || rect.height <= 0) return;
    layer.style.left = `${rect.left}px`;
    layer.style.top = `${rect.top}px`;
    layer.style.width = `${rect.width}px`;
    layer.style.height = `${rect.height}px`;
  }

  function scheduleOcclusionLayerSync() {
    requestAnimationFrame(() => {
      requestAnimationFrame(syncOcclusionLayerRect);
    });
  }

  function bindOcclusionEditorLayout() {
    state.occlusionEditor.layoutCleanup?.();
    const stage = selectors.occlusionStage;
    const image = selectors.occlusionImage;
    if (!stage || !image) return;
    const resizeObserver = typeof ResizeObserver !== 'undefined'
      ? new ResizeObserver(scheduleOcclusionLayerSync)
      : null;
    resizeObserver?.observe(stage);
    resizeObserver?.observe(image);
    window.addEventListener('resize', scheduleOcclusionLayerSync);
    window.visualViewport?.addEventListener('resize', scheduleOcclusionLayerSync);
    image.addEventListener('load', scheduleOcclusionLayerSync);
    state.occlusionEditor.layoutCleanup = () => {
      resizeObserver?.disconnect();
      window.removeEventListener('resize', scheduleOcclusionLayerSync);
      window.visualViewport?.removeEventListener('resize', scheduleOcclusionLayerSync);
      image.removeEventListener('load', scheduleOcclusionLayerSync);
    };
  }

  function renderOcclusionEditor() {
    const draft = state.occlusionEditor.draft;
    if (!draft || !selectors.occlusionLayer) return;
    syncOcclusionLayerRect();
    const selected = String(state.occlusionEditor.selectedMaskId || '');
    selectors.occlusionLayer.innerHTML = draft.masks.map((mask, index) => `
      <button type="button"
        class="occlusion-editor-mask shape-${escapeAttr(mask.shape || 'rect')} ${String(mask.id) === selected ? 'active' : ''}"
        data-occlusion-mask-id="${escapeAttr(mask.id)}"
        style="left:${mask.x * 100}%;top:${mask.y * 100}%;width:${mask.w * 100}%;height:${mask.h * 100}%"
        aria-label="Mask ${index + 1}">
        <i class="occlusion-move-handle" data-occlusion-move="1" aria-hidden="true"></i>
        <span>${index + 1}</span>
        <i class="occlusion-resize-handle" data-occlusion-resize="1" aria-hidden="true"></i>
      </button>
    `).join('');
    const selectedMask = selectedOcclusionMask();
    if (selectors.occlusionAnswer && document.activeElement !== selectors.occlusionAnswer) {
      selectors.occlusionAnswer.value = plainTextFromHtml(selectedMask?.answer || '');
    }
    if (selectors.occlusionHint && document.activeElement !== selectors.occlusionHint) {
      selectors.occlusionHint.value = plainTextFromHtml(selectedMask?.hint || '');
    }
    if (selectors.occlusionStatus) {
      const count = draft.masks.length;
      selectors.occlusionStatus.textContent = count
        ? `${plural(count, 'mask')} ready. Each mask becomes one study card.`
        : 'Add masks over the parts you want to test.';
    }
    selectors.occlusionDeleteMask?.toggleAttribute('disabled', !selectedMask);
  }

  function openOcclusionEditor(cardId) {
    syncCreatorFromDom();
    const index = state.creator.cards.findIndex(card => String(card.id) === String(cardId));
    if (index < 0) return false;
    const original = clonePlain(state.creator.cards[index]);
    const source = createImageOcclusionDraft(state.creator.cards[index], firstCardImageSource(state.creator.cards[index]));
    const occlusion = normalizeImageOcclusion(source.imageOcclusion, source);
    if (!occlusion.image) return false;
    state.creator.cards[index] = source;
    state.occlusionEditor.cardId = source.id;
    state.occlusionEditor.originalCard = original;
    state.occlusionEditor.draft = clonePlain(occlusion);
    state.occlusionEditor.selectedMaskId = occlusion.masks[0]?.id || null;
    setOcclusionShape(occlusion.masks[0]?.shape || 'rect');
    if (selectors.occlusionImage) {
      selectors.occlusionImage.src = occlusion.image;
      selectors.occlusionImage.onload = () => {
        syncOcclusionLayerRect();
        renderOcclusionEditor();
      };
    }
    selectors.occlusionOverlay?.classList.remove('hidden');
    bindOcclusionEditorLayout();
    requestAnimationFrame(renderOcclusionEditor);
    scheduleOcclusionLayerSync();
    return true;
  }

  function closeOcclusionEditor(options = {}) {
    state.occlusionEditor.layoutCleanup?.();
    if (options.restoreOriginal && state.occlusionEditor.originalCard && state.occlusionEditor.cardId) {
      state.creator.cards = state.creator.cards.map(card => (
        String(card.id) === String(state.occlusionEditor.cardId)
          ? clonePlain(state.occlusionEditor.originalCard)
          : card
      ));
      renderCreate();
    }
    selectors.occlusionOverlay?.classList.add('hidden');
    state.occlusionEditor = {
      cardId: null,
      originalCard: null,
      draft: null,
      selectedMaskId: null,
      shape: 'rect',
      pointer: null,
      layoutCleanup: null
    };
    state.lastModalClosedAt = Date.now();
  }

  function addOcclusionMask() {
    const draft = state.occlusionEditor.draft;
    if (!draft) return;
    if (draft.masks.length >= OCCLUSION_MAX_MASKS) {
      showToast(`Limit is ${OCCLUSION_MAX_MASKS} masks`);
      return;
    }
    const next = normalizeOcclusionMask({
      shape: state.occlusionEditor.shape,
      x: 0.34,
      y: 0.4,
      w: 0.32,
      h: 0.13,
      answer: `Hidden part ${draft.masks.length + 1}`
    }, draft.masks.length);
    draft.masks.push(next);
    state.occlusionEditor.selectedMaskId = next.id;
    renderOcclusionEditor();
    selectors.occlusionAnswer?.focus();
    selectors.occlusionAnswer?.select?.();
  }

  function deleteSelectedOcclusionMask() {
    const draft = state.occlusionEditor.draft;
    const mask = selectedOcclusionMask();
    if (!draft || !mask) return;
    const index = draft.masks.findIndex(item => String(item.id) === String(mask.id));
    draft.masks.splice(index, 1);
    state.occlusionEditor.selectedMaskId = draft.masks[Math.min(index, draft.masks.length - 1)]?.id || null;
    renderOcclusionEditor();
  }

  function updateSelectedOcclusionText() {
    const mask = selectedOcclusionMask();
    if (!mask) return;
    mask.answer = sanitizeEditorHtml(String(selectors.occlusionAnswer?.value || '').slice(0, 220));
    mask.hint = sanitizeEditorHtml(String(selectors.occlusionHint?.value || '').slice(0, 220));
  }

  function updateOcclusionMaskElement(mask) {
    const element = selectors.occlusionLayer?.querySelector(`[data-occlusion-mask-id="${cssEscape(mask.id)}"]`);
    if (!element) return false;
    element.style.left = `${mask.x * 100}%`;
    element.style.top = `${mask.y * 100}%`;
    element.style.width = `${mask.w * 100}%`;
    element.style.height = `${mask.h * 100}%`;
    return true;
  }

  function updateOcclusionSelectionUi() {
    const selected = String(state.occlusionEditor.selectedMaskId || '');
    selectors.occlusionLayer?.querySelectorAll('[data-occlusion-mask-id]').forEach(element => {
      element.classList.toggle('active', String(element.dataset.occlusionMaskId) === selected);
    });
    const mask = selectedOcclusionMask();
    if (selectors.occlusionAnswer) selectors.occlusionAnswer.value = plainTextFromHtml(mask?.answer || '');
    if (selectors.occlusionHint) selectors.occlusionHint.value = plainTextFromHtml(mask?.hint || '');
    selectors.occlusionDeleteMask?.toggleAttribute('disabled', !mask);
  }

  function saveOcclusionEditor() {
    updateSelectedOcclusionText();
    const draft = state.occlusionEditor.draft;
    const cardId = state.occlusionEditor.cardId;
    if (!draft || !cardId) return;
    if (!safeMediaSrc(draft.image)) {
      showToast('Choose an image first');
      return;
    }
    if (!Array.isArray(draft.masks) || !draft.masks.length) {
      showToast('Add at least one mask');
      return;
    }
    if (draft.masks.some(mask => !plainTextFromHtml(mask.answer || '').trim())) {
      showToast('Every mask needs an answer');
      return;
    }
    const normalized = normalizeImageOcclusion(draft, {});
    state.creator.cards = state.creator.cards.map(card => (
      String(card.id) === String(cardId)
        ? createImageOcclusionDraft(card, normalized.image)
        : card
    ));
    state.creator.cards = state.creator.cards.map(card => (
      String(card.id) === String(cardId)
        ? {
            ...card,
            imageOcclusion: {
              ...normalized,
              lastModified: Date.now()
            },
            lastModified: Date.now()
          }
        : card
    ));
    closeOcclusionEditor();
    renderCreate();
    scheduleCreatorDraftSave();
    showToast(`Saved ${plural(normalized.masks.length, 'mask')}`);
  }

  function startOcclusionPointer(event) {
    const maskEl = event.target.closest?.('[data-occlusion-mask-id]');
    if (!maskEl || !selectors.occlusionLayer?.contains(maskEl)) return;
    event.preventDefault();
    updateSelectedOcclusionText();
    const mask = (state.occlusionEditor.draft?.masks || [])
      .find(item => String(item.id) === String(maskEl.dataset.occlusionMaskId));
    if (!mask) return;
    state.occlusionEditor.selectedMaskId = mask.id;
    const rect = selectors.occlusionLayer.getBoundingClientRect();
    state.occlusionEditor.pointer = {
      id: event.pointerId,
      mode: event.target.closest('[data-occlusion-resize]') ? 'resize' : 'move',
      startX: event.clientX,
      startY: event.clientY,
      layerW: Math.max(1, rect.width),
      layerH: Math.max(1, rect.height),
      mask: { ...mask }
    };
    maskEl.setPointerCapture?.(event.pointerId);
    updateOcclusionSelectionUi();
  }

  function moveOcclusionPointer(event) {
    const pointer = state.occlusionEditor.pointer;
    if (!pointer || pointer.id !== event.pointerId) return;
    event.preventDefault();
    const mask = selectedOcclusionMask();
    if (!mask) return;
    const dx = (event.clientX - pointer.startX) / pointer.layerW;
    const dy = (event.clientY - pointer.startY) / pointer.layerH;
    if (pointer.mode === 'resize') {
      mask.w = clamp(pointer.mask.w + dx, OCCLUSION_MIN_SIZE, 1 - pointer.mask.x);
      mask.h = clamp(pointer.mask.h + dy, OCCLUSION_MIN_SIZE, 1 - pointer.mask.y);
    } else {
      mask.x = clamp(pointer.mask.x + dx, 0, 1 - pointer.mask.w);
      mask.y = clamp(pointer.mask.y + dy, 0, 1 - pointer.mask.h);
    }
    if (!updateOcclusionMaskElement(mask)) renderOcclusionEditor();
  }

  function endOcclusionPointer(event) {
    const pointer = state.occlusionEditor.pointer;
    if (!pointer || pointer.id !== event.pointerId) return;
    state.occlusionEditor.pointer = null;
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
      const frontHtml = selectors.creatorCards.querySelector(`[data-html-editor-id="${cssEscape(card.id)}"][data-html-part="front"]`);
      const backHtml = selectors.creatorCards.querySelector(`[data-html-editor-id="${cssEscape(card.id)}"][data-html-part="back"]`);
      const frontCss = selectors.creatorCards.querySelector(`[data-html-editor-id="${cssEscape(card.id)}"][data-html-part="front-css"]`);
      const backCss = selectors.creatorCards.querySelector(`[data-html-editor-id="${cssEscape(card.id)}"][data-html-part="back-css"]`);
      const currentAdvanced = normalizeAdvancedHtml(advancedHtmlPayload(card));
      const nextAdvanced = {
        frontHtml: frontHtml ? sanitizeAdvancedHtml(frontHtml.value) : sanitizeAdvancedHtml(currentAdvanced.frontHtml),
        backHtml: backHtml ? sanitizeAdvancedHtml(backHtml.value) : sanitizeAdvancedHtml(currentAdvanced.backHtml),
        frontCss: frontCss ? sanitizeAdvancedCss(frontCss.value) : sanitizeAdvancedCss(currentAdvanced.frontCss),
        backCss: backCss ? sanitizeAdvancedCss(backCss.value) : sanitizeAdvancedCss(currentAdvanced.backCss)
      };
      return {
        ...card,
        term: sanitizeEditorHtml(term?.innerHTML || card.term || ''),
        definition: sanitizeEditorHtml(definition?.innerHTML || card.definition || ''),
        advancedHtml: nextAdvanced
      };
    });
  }

  function clonePlain(value) {
    try {
      return JSON.parse(JSON.stringify(value));
    } catch (_) {
      return value;
    }
  }

  function cardWithNoteDefaults(card) {
    const advanced = isAdvancedHtmlCard(card);
    const occlusion = isImageOcclusionCard(card);
    return {
      ...card,
      noteId: card.noteId || createLocalId('note'),
      noteType: advanced ? 'advanced-html' : (occlusion ? 'image-occlusion' : (card.noteType || 'basic')),
      cardTemplate: advanced ? 'advanced-html' : (occlusion ? (card.cardTemplate || 'image-occlusion-source') : (card.cardTemplate || 'front-back')),
      noteFields: card.noteFields && typeof card.noteFields === 'object' ? card.noteFields : {},
      imageOcclusion: occlusion ? normalizeImageOcclusion(card.imageOcclusion, card) : (card.imageOcclusion || null),
      advancedHtml: sanitizeAdvancedHtmlCard(advancedHtmlPayload(card))
    };
  }

  function isReverseTemplate(card = {}) {
    return card.cardTemplate === 'back-front';
  }

  function hasClozeSyntax(card = {}) {
    return clozeIndexesFromText(`${card.term || ''} ${card.definition || ''}`).length > 0;
  }

  function cardHasReverseSibling(card = {}) {
    const noteId = String(card.noteId || '');
    if (!noteId) return false;
    return state.creator.cards.some(item => (
      String(item.id) !== String(card.id)
      && String(item.noteId || '') === noteId
      && isReverseTemplate(item)
    ));
  }

  function creatorCardWantsReverse(card = {}) {
    if (isAdvancedHtmlCard(card) || isImageOcclusionCard(card)) return false;
    return Boolean(card.generateReverse || cardHasReverseSibling(card));
  }

  function stripCreatorFields(card = {}) {
    const { generateReverse, ...rest } = card;
    return rest;
  }

  function createReverseCard(card) {
    const now = Date.now();
    const noteId = card.noteId || createLocalId('note');
    const media = normalizeCardMedia(card);
    const background = normalizeCardBackground(card);
    return {
      ...clonePlain(card),
      id: createLocalId('card'),
      noteId,
      noteType: 'basic-reverse',
      cardTemplate: 'back-front',
      noteFields: {
        front: card.term || '',
        back: card.definition || ''
      },
      term: card.definition || '',
      definition: card.term || '',
      termImage: card.definitionImage || '',
      definitionImage: card.termImage || '',
      media: {
        term: clonePlain(media.definition || []),
        definition: clonePlain(media.term || [])
      },
      background: {
        term: clonePlain(background.definition || null),
        definition: clonePlain(background.term || null)
      },
      srs: undefined,
      reviewHistory: [],
      suspended: false,
      buriedUntil: null,
      created: now,
      lastModified: now
    };
  }

  function clozeIndexesFromText(value) {
    const indexes = new Set();
    String(value || '').replace(/\{\{c(\d+)::([\s\S]*?)\}\}/gi, (_match, index) => {
      indexes.add(Number(index));
      return '';
    });
    return Array.from(indexes).sort((a, b) => a - b);
  }

  function clozeTextForIndex(value, targetIndex, reveal = false) {
    return String(value || '').replace(/\{\{c(\d+)::([\s\S]*?)\}\}/gi, (_match, index, answer) => {
      const isTarget = Number(index) === Number(targetIndex);
      if (reveal || !isTarget) return answer;
      return '<strong>[...]</strong>';
    });
  }

  function expandClozeCard(card) {
    const source = card.term || card.definition || '';
    const indexes = clozeIndexesFromText(source);
    if (!indexes.length) return [cardWithNoteDefaults(card)];
    const noteId = card.noteId || createLocalId('note');
    return indexes.map(index => ({
      ...clonePlain(card),
      id: indexes.length === 1 ? card.id : createLocalId('card'),
      noteId,
      noteType: 'cloze',
      cardTemplate: `cloze-${index}`,
      clozeIndex: index,
      noteFields: {
        text: source,
        extra: card.term ? card.definition || '' : ''
      },
      term: clozeTextForIndex(source, index, false),
      definition: `${clozeTextForIndex(source, index, true)}${card.term && card.definition ? `<hr>${card.definition}` : ''}`,
      srs: indexes.length === 1 ? card.srs : undefined,
      reviewHistory: indexes.length === 1 ? (card.reviewHistory || []) : [],
      created: card.created || Date.now(),
      lastModified: Date.now()
    }));
  }

  function expandCreatorCard(card) {
    const base = cardWithNoteDefaults(card);
    if (isImageOcclusionCard(base)) {
      return expandImageOcclusionCard(base);
    }
    if (isAdvancedHtmlCard(base)) {
      return [stripCreatorFields({
        ...base,
        noteType: 'advanced-html',
        cardTemplate: 'advanced-html',
        noteFields: {
          ...(base.noteFields || {}),
          frontHtml: base.advancedHtml?.frontHtml || '',
          backHtml: base.advancedHtml?.backHtml || '',
          frontCss: base.advancedHtml?.frontCss || '',
          backCss: base.advancedHtml?.backCss || ''
        },
        term: sanitizeEditorHtml(base.term || advancedHtmlFallbackText(base, 'front')),
        definition: sanitizeEditorHtml(base.definition || advancedHtmlFallbackText(base, 'back'))
      })];
    }
    if (hasClozeSyntax(base)) {
      return expandClozeCard(base).map(stripCreatorFields);
    }
    if (base.noteType === 'cloze') {
      base.noteType = 'basic';
      base.cardTemplate = 'front-back';
      base.clozeIndex = null;
      base.noteFields = {};
    }
    if (creatorCardWantsReverse(base) && !isReverseTemplate(base)) {
      const front = {
        ...base,
        noteType: 'basic-reverse',
        cardTemplate: 'front-back',
        noteFields: {
          ...(base.noteFields || {}),
          front: base.term || '',
          back: base.definition || ''
        }
      };
      return [
        stripCreatorFields(front),
        stripCreatorFields(createReverseCard(front))
      ];
    }
    return [stripCreatorFields(base)];
  }

  function creatorCardsFromStoredCards(cards = []) {
    const normalized = (Array.isArray(cards) ? cards : [])
      .map(card => schema?.normalizeCard ? schema.normalizeCard(card) : { ...emptyCreatorCard(), ...card });
    const groups = new Map();
    normalized.forEach(card => {
      const noteId = String(card.noteId || '');
      if (!noteId) return;
      if (!groups.has(noteId)) groups.set(noteId, []);
      groups.get(noteId).push(card);
    });

    const used = new Set();
    const creatorCards = [];
    normalized.forEach(card => {
      const id = String(card.id || '');
      if (used.has(id)) return;
      const group = groups.get(String(card.noteId || '')) || [card];

      if (isImageOcclusionCard(card)) {
        const occlusionCards = group.filter(isImageOcclusionCard);
        occlusionCards.forEach(item => used.add(String(item.id || '')));
        const first = occlusionCards[0] || card;
        const image = firstCardImageSource(first);
        const masks = occlusionCards
          .map((item, index) => {
            const occlusion = normalizeImageOcclusion(item.imageOcclusion, item);
            const targetId = String(item.imageOcclusion?.targetMaskId || item.noteFields?.maskId || '');
            const targetIndex = Number(item.imageOcclusion?.targetMaskIndex ?? index);
            const found = occlusion.masks.find(mask => String(mask.id) === targetId)
              || occlusion.masks[targetIndex]
              || normalizeOcclusionMask({}, index);
            return {
              ...found,
              cardId: item.id || found.cardId || createLocalId('card'),
              answer: sanitizeEditorHtml(item.noteFields?.answer || item.definition || found.answer || `Hidden part ${index + 1}`),
              hint: sanitizeEditorHtml(item.noteFields?.hint || found.hint || '')
            };
          })
          .slice(0, OCCLUSION_MAX_MASKS);
        creatorCards.push({
          ...first,
          id: first.id || createLocalId('card'),
          noteId: first.noteId || createLocalId('note'),
          noteType: 'image-occlusion',
          cardTemplate: 'image-occlusion-source',
          term: sanitizeEditorHtml(first.noteFields?.title || first.term || 'Image occlusion'),
          definition: '',
          termImage: image,
          definitionImage: '',
          media: { term: [], definition: [] },
          background: { term: null, definition: null },
          imageOcclusion: normalizeImageOcclusion({ image, masks }, first),
          srs: undefined,
          reviewHistory: []
        });
        return;
      }

      if (isAdvancedHtmlCard(card)) {
        used.add(id);
        creatorCards.push({
          ...card,
          noteType: 'advanced-html',
          cardTemplate: 'advanced-html',
          advancedHtml: sanitizeAdvancedHtmlCard(advancedHtmlPayload(card))
        });
        return;
      }

      if (card.noteType === 'cloze' && card.noteFields?.text) {
        const clozeCards = group.filter(item => item.noteType === 'cloze' && item.noteFields?.text);
        clozeCards.forEach(item => used.add(String(item.id || '')));
        creatorCards.push({
          ...card,
          id: card.id || createLocalId('card'),
          noteType: 'cloze',
          cardTemplate: 'cloze-source',
          clozeIndex: null,
          term: card.noteFields.text || card.term || '',
          definition: card.noteFields.extra || '',
          srs: undefined,
          reviewHistory: []
        });
        return;
      }

      const front = group.find(item => item.cardTemplate === 'front-back' && item.noteType !== 'cloze' && item.noteType !== 'image-occlusion' && !isAdvancedHtmlCard(item));
      const reverse = group.find(item => isReverseTemplate(item));
      if (reverse && front && isReverseTemplate(card)) return;
      if (reverse && front && String(front.id) === id) {
        used.add(String(front.id || ''));
        used.add(String(reverse.id || ''));
        creatorCards.push({
          ...front,
          noteType: 'basic-reverse',
          cardTemplate: 'front-back',
          generateReverse: true
        });
        return;
      }

      used.add(id);
      creatorCards.push({ ...card });
    });
    return creatorCards.length ? creatorCards : [emptyCreatorCard()];
  }

  function syncGeneratedCards(cards = []) {
    const groups = new Map();
    cards.forEach(card => {
      const noteId = card.noteId || createLocalId('note');
      card.noteId = noteId;
      if (!groups.has(noteId)) groups.set(noteId, []);
      groups.get(noteId).push(card);
    });

    groups.forEach(group => {
      const front = group.find(card => card.cardTemplate === 'front-back' && !isAdvancedHtmlCard(card))
        || group.find(card => card.noteType !== 'cloze' && card.noteType !== 'image-occlusion' && !isAdvancedHtmlCard(card));
      if (!front) return;
      group.forEach(card => {
        card.noteFields = {
          ...(card.noteFields || {}),
          front: front.term || '',
          back: front.definition || ''
        };
        if (card.cardTemplate === 'back-front') {
          card.noteType = 'basic-reverse';
          card.term = front.definition || '';
          card.definition = front.term || '';
        }
      });
    });

    return cards;
  }

  function firstCardImageSource(card = {}) {
    const media = normalizeCardMedia(card);
    const background = normalizeCardBackground(card);
    const mediaImage = [...(media.term || []), ...(media.definition || [])]
      .find(item => item.kind === 'image' && safeMediaSrc(item.src));
    const occlusionImage = card.imageOcclusion && typeof card.imageOcclusion === 'object'
      ? safeMediaSrc(card.imageOcclusion.image || card.imageOcclusion.src || card.imageOcclusion.dataUrl)
      : '';
    return occlusionImage
      || safeMediaSrc(card.termImage)
      || safeMediaSrc(card.definitionImage)
      || safeMediaSrc(mediaImage?.src)
      || safeMediaSrc(background.term?.src)
      || safeMediaSrc(background.definition?.src)
      || '';
  }

  function isImageOcclusionCard(card = {}) {
    return String(card.noteType || '').toLowerCase() === 'image-occlusion'
      || String(card.cardTemplate || '').toLowerCase().startsWith('image-occlusion');
  }

  function normalizeUnit(value, fallback = 0) {
    const number = Number(value);
    if (!Number.isFinite(number)) return fallback;
    const unit = number > 1 ? number / 100 : number;
    return Math.min(1, Math.max(0, unit));
  }

  function normalizeOcclusionMask(mask = {}, index = 0) {
    const source = mask && typeof mask === 'object' ? mask : {};
    const width = Math.min(0.95, Math.max(OCCLUSION_MIN_SIZE, normalizeUnit(source.w ?? source.width, 0.24)));
    const height = Math.min(0.95, Math.max(OCCLUSION_MIN_SIZE, normalizeUnit(source.h ?? source.height, 0.12)));
    const x = Math.min(1 - width, normalizeUnit(source.x ?? source.left, 0.38));
    const y = Math.min(1 - height, normalizeUnit(source.y ?? source.top, 0.4));
    const shape = String(source.shape || '').toLowerCase() === 'ellipse' ? 'ellipse' : 'rect';
    return {
      id: String(source.id || createLocalId('mask')),
      cardId: String(source.cardId || source.cardID || createLocalId('card')),
      shape,
      x,
      y,
      w: width,
      h: height,
      answer: sanitizeEditorHtml(String(source.answer || source.label || source.text || '').slice(0, 220)),
      hint: sanitizeEditorHtml(String(source.hint || '').slice(0, 220))
    };
  }

  function normalizeImageOcclusion(value = {}, card = {}) {
    const source = value && typeof value === 'object' ? value : {};
    const image = safeMediaSrc(source.image || source.src || source.dataUrl || card.termImage || firstCardImageSource({ ...card, imageOcclusion: null }));
    const masks = (Array.isArray(source.masks) ? source.masks : [])
      .slice(0, OCCLUSION_MAX_MASKS)
      .map(normalizeOcclusionMask)
      .filter(mask => mask.answer && plainTextFromHtml(mask.answer).trim());
    return {
      version: 1,
      coordinateSpace: 'image',
      mode: source.mode === 'hide-all' ? 'hide-all' : 'hide-one',
      image,
      masks,
      created: source.created || Date.now(),
      lastModified: source.lastModified || Date.now()
    };
  }

  function createImageOcclusionDraft(card = {}, imageSrc = '') {
    const now = Date.now();
    const noteId = card.noteId || createLocalId('note');
    return {
      ...card,
      id: card.id || createLocalId('card'),
      noteId,
      noteType: 'image-occlusion',
      cardTemplate: 'image-occlusion-source',
      noteFields: {
        ...(card.noteFields || {}),
        image: imageSrc
      },
      term: sanitizeEditorHtml(card.term || 'Image occlusion'),
      definition: sanitizeEditorHtml(card.definition || ''),
      termImage: imageSrc,
      definitionImage: '',
      imageOcclusion: {
        ...normalizeImageOcclusion(card.imageOcclusion, card),
        image: imageSrc,
        masks: normalizeImageOcclusion(card.imageOcclusion, card).masks
      },
      advancedHtml: { frontHtml: '', backHtml: '', frontCss: '', backCss: '' },
      media: { term: [], definition: [] },
      background: { term: null, definition: null },
      generateReverse: false,
      tags: Array.from(new Set([...(card.tags || []), 'image-occlusion'])).slice(0, 30),
      created: card.created || now,
      lastModified: now
    };
  }

  function expandImageOcclusionCard(card) {
    const base = cardWithNoteDefaults(card);
    const occlusion = normalizeImageOcclusion(base.imageOcclusion, base);
    if (!occlusion.image || !occlusion.masks.length) return [];
    const noteId = base.noteId || createLocalId('note');
    const title = plainTextFromHtml(base.term || '').trim() || 'Image occlusion';
    return occlusion.masks.map((mask, index) => {
      const answerText = sanitizeEditorHtml(mask.answer || `Hidden part ${index + 1}`);
      const hintText = sanitizeEditorHtml(mask.hint || '');
      return stripCreatorFields({
        ...clonePlain(base),
        id: mask.cardId || createLocalId('card'),
        noteId,
        noteType: 'image-occlusion',
        cardTemplate: 'image-occlusion-mask',
        noteFields: {
          ...(base.noteFields || {}),
          image: occlusion.image,
          title,
          answer: answerText,
          hint: hintText,
          maskId: mask.id
        },
        term: hintText
          ? `<strong>Guess the hidden part.</strong><br><small>Hint: ${hintText}</small>`
          : '<strong>Guess the hidden part.</strong>',
        definition: answerText,
        termImage: occlusion.image,
        definitionImage: occlusion.image,
        media: { term: [], definition: [] },
        background: { term: null, definition: null },
        imageOcclusion: {
          ...occlusion,
          targetMaskId: mask.id,
          targetMaskIndex: index
        },
        srs: mask.cardId === base.id ? base.srs : undefined,
        reviewHistory: mask.cardId === base.id ? (base.reviewHistory || []) : [],
        created: base.created || Date.now(),
        lastModified: Date.now()
      });
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

  function creatorCardBadges(card = {}) {
    const badges = [];
    const clozeCount = clozeIndexesFromText(`${card.term || ''} ${card.definition || ''}`).length;
    if (isAdvancedHtmlCard(card)) {
      badges.push(['HTML/CSS', 'fa-code']);
    } else if (card.noteType === 'image-occlusion') {
      badges.push(['Occlusion', 'fa-object-ungroup']);
    } else if (clozeCount || card.noteType === 'cloze') {
      badges.push([clozeCount > 1 ? `Cloze x${clozeCount}` : 'Cloze', 'fa-code']);
    } else if (creatorCardWantsReverse(card)) {
      badges.push(['Basic + Reverse', 'fa-right-left']);
    } else {
      badges.push(['Basic', 'fa-rectangle-list']);
    }
    if (card.suspended) badges.push(['Suspended', 'fa-pause']);
    return badges.map(([label, icon]) => `
      <span class="creator-card-badge"><i class="fas ${escapeAttr(icon)}"></i>${escapeHtml(label)}</span>
    `).join('');
  }

  function advancedHtmlEditor(card = {}) {
    const advancedHtml = normalizeAdvancedHtml(card.advancedHtml || {});
    return `
      <section class="advanced-html-editor" aria-label="Advanced HTML card editor">
        <div class="advanced-html-actions">
          <button type="button" data-creator-action="copy-html-prompt" data-card-id="${escapeAttr(card.id)}">
            <i class="fas fa-wand-magic-sparkles"></i>
            <span>Copy AI Prompt</span>
          </button>
          <button type="button" data-creator-action="basic-card" data-card-id="${escapeAttr(card.id)}">
            <i class="fas fa-rectangle-list"></i>
            <span>Basic</span>
          </button>
        </div>
        <label class="advanced-html-field">
          <span>Front HTML</span>
          <textarea class="advanced-html-textarea" data-html-editor-id="${escapeAttr(card.id)}" data-html-part="front" rows="8" spellcheck="false" autocomplete="off">${escapeHtml(advancedHtml.frontHtml)}</textarea>
        </label>
        <label class="advanced-html-field">
          <span>Front CSS</span>
          <textarea class="advanced-html-textarea advanced-html-css" data-html-editor-id="${escapeAttr(card.id)}" data-html-part="front-css" rows="7" spellcheck="false" autocomplete="off">${escapeHtml(advancedHtml.frontCss)}</textarea>
        </label>
        <label class="advanced-html-field">
          <span>Back HTML</span>
          <textarea class="advanced-html-textarea" data-html-editor-id="${escapeAttr(card.id)}" data-html-part="back" rows="8" spellcheck="false" autocomplete="off">${escapeHtml(advancedHtml.backHtml)}</textarea>
        </label>
        <label class="advanced-html-field">
          <span>Back CSS</span>
          <textarea class="advanced-html-textarea advanced-html-css" data-html-editor-id="${escapeAttr(card.id)}" data-html-part="back-css" rows="7" spellcheck="false" autocomplete="off">${escapeHtml(advancedHtml.backCss)}</textarea>
        </label>
      </section>
    `;
  }

  function imageOcclusionEditor(card = {}) {
    const occlusion = normalizeImageOcclusion(card.imageOcclusion, card);
    const image = safeMediaSrc(occlusion.image || firstCardImageSource(card));
    const answered = occlusion.masks.filter(mask => plainTextFromHtml(mask.answer || '').trim()).length;
    return `
      <section class="occlusion-summary-card" aria-label="Image occlusion card editor">
        ${image ? `<img src="${escapeAttr(image)}" alt="Occlusion source image">` : `<div class="deck-icon"><i class="fas fa-image"></i></div>`}
        <div class="occlusion-summary-main">
          <strong>${escapeHtml(occlusion.masks.length ? `${plural(occlusion.masks.length, 'mask')}` : 'No masks yet')}</strong>
          <small>${escapeHtml(answered ? `${answered} with answers. Saved as one study card per mask.` : 'Add masks and answers before saving.')}</small>
          <div class="occlusion-summary-actions">
            <button type="button" data-creator-action="image-occlusion" data-card-id="${escapeAttr(card.id)}">
              <i class="fas fa-pen"></i> Edit masks
            </button>
            <button type="button" data-creator-action="basic-card" data-card-id="${escapeAttr(card.id)}">
              <i class="fas fa-rectangle-list"></i> Basic
            </button>
          </div>
        </div>
      </section>
    `;
  }

  function cardEditor(card, index) {
    card.media = normalizeCardMedia(card);
    card.background = normalizeCardBackground(card);
    card.advancedHtml = sanitizeAdvancedHtmlCard(advancedHtmlPayload(card));
    const advanced = isAdvancedHtmlCard(card);
    const occlusion = isImageOcclusionCard(card);
    const safeTerm = sanitizeEditorHtml(card.term || '');
    const safeDefinition = sanitizeEditorHtml(card.definition || '');
    const termMedia = mediaPreviewHtml(card, 'term');
    const definitionMedia = mediaPreviewHtml(card, 'definition');
    const reverseOn = !advanced && !occlusion && creatorCardWantsReverse(card);

    return `
      <article class="mobile-card-editor" data-card-id="${escapeAttr(card.id)}">
        <header>
          <div class="creator-card-title">
            <span>Card ${index + 1}</span>
            <div class="creator-card-badges">${creatorCardBadges(card)}</div>
          </div>
          <div class="creator-card-actions">
            <button type="button" class="small-icon-button" data-creator-action="move-card-up" data-card-id="${escapeAttr(card.id)}" aria-label="Move card up" ${index === 0 ? 'disabled' : ''}>
              <i class="fas fa-arrow-up"></i>
            </button>
            <button type="button" class="small-icon-button" data-creator-action="move-card-down" data-card-id="${escapeAttr(card.id)}" aria-label="Move card down" ${index === state.creator.cards.length - 1 ? 'disabled' : ''}>
              <i class="fas fa-arrow-down"></i>
            </button>
            <button type="button" class="small-icon-button" data-creator-action="insert-card-after" data-card-id="${escapeAttr(card.id)}" aria-label="Insert card after this card">
              <i class="fas fa-plus"></i>
            </button>
            <button type="button" class="small-icon-button danger" data-creator-action="delete-card" data-card-id="${escapeAttr(card.id)}" aria-label="Delete card. Hold to delete this card and all cards below.">
              <i class="fas fa-trash"></i>
            </button>
          </div>
        </header>
        <div class="creator-generate-row" role="toolbar" aria-label="Card generation tools">
          <button type="button" class="${reverseOn ? 'active' : ''}" ${advanced || occlusion ? 'disabled' : ''} data-creator-action="reverse-card" data-card-id="${escapeAttr(card.id)}" aria-pressed="${reverseOn ? 'true' : 'false'}">
            <i class="fas fa-right-left"></i>
            <span>Reverse</span>
          </button>
          <button type="button" ${advanced || occlusion ? 'disabled' : ''} data-creator-action="cloze" data-card-id="${escapeAttr(card.id)}" data-side="term">
            <i class="fas fa-eye-slash"></i>
            <span>Cloze</span>
          </button>
          <button type="button" class="${occlusion ? 'active' : ''}" ${advanced ? 'disabled' : ''} data-creator-action="image-occlusion" data-card-id="${escapeAttr(card.id)}" aria-pressed="${occlusion ? 'true' : 'false'}">
            <i class="fas fa-object-ungroup"></i>
            <span>Occlusion</span>
          </button>
          <button type="button" class="${advanced ? 'active' : ''}" ${occlusion ? 'disabled' : ''} data-creator-action="advanced-html-card" data-card-id="${escapeAttr(card.id)}" aria-pressed="${advanced ? 'true' : 'false'}">
            <i class="fas fa-code"></i>
            <span>HTML</span>
          </button>
        </div>
        ${occlusion ? imageOcclusionEditor(card) : (advanced ? advancedHtmlEditor(card) : `
        <section class="editor-side">
          <div class="editor-side-head">
            <strong>Term</strong>
            <div class="creator-toolbar">
              ${formatButton('bold', 'Bold', 'fa-bold')}
              ${formatButton('italic', 'Italic', 'fa-italic')}
              ${formatButton('underline', 'Underline', 'fa-underline')}
              ${formatButton('highlight', 'Highlight', 'fa-highlighter')}
              ${formatButton('inlineCode', 'Inline code', 'fa-terminal')}
              ${formatButton('codeBlock', 'Code block', 'fa-file-code')}
              ${formatButton('formula', 'Formula', 'fa-square-root-variable')}
              <button type="button" class="format-button" data-creator-action="cloze" data-card-id="${escapeAttr(card.id)}" data-side="term" aria-label="Cloze selected text">
                <i class="fas fa-eye-slash"></i>
              </button>
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
              ${formatButton('highlight', 'Highlight', 'fa-highlighter')}
              ${formatButton('inlineCode', 'Inline code', 'fa-terminal')}
              ${formatButton('codeBlock', 'Code block', 'fa-file-code')}
              ${formatButton('formula', 'Formula', 'fa-square-root-variable')}
              <button type="button" class="format-button" data-creator-action="cloze" data-card-id="${escapeAttr(card.id)}" data-side="definition" aria-label="Cloze selected text">
                <i class="fas fa-eye-slash"></i>
              </button>
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
        `)}
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

  function importUserError(message) {
    const error = new Error(message);
    error.userMessage = message;
    return error;
  }

  function importString(value) {
    return value == null ? '' : String(value);
  }

  function normalizeImportTags(value) {
    const list = Array.isArray(value)
      ? value
      : String(value || '').split(/[;,]/);
    return Array.from(new Set(list
      .map(item => String(item || '').trim())
      .filter(Boolean)))
      .slice(0, 30);
  }

  function importFlag(value) {
    if (value === true) return true;
    if (typeof value === 'number') return value > 0;
    return ['true', '1', 'yes', 'y', 'on', 'reverse'].includes(String(value || '').trim().toLowerCase());
  }

  function normalizeImportType(value) {
    const raw = String(value || '').trim().toLowerCase().replace(/[\s_]+/g, '-');
    if (['advanced-html', 'advancedhtml', 'custom-html', 'html', 'html-css'].includes(raw)) return 'advanced-html';
    if (['image-occlusion', 'imageocclusion', 'occlusion', 'io'].includes(raw)) return 'image-occlusion';
    if (['cloze', 'fill-blank', 'fill-in-blank', 'fill-in-the-blank'].includes(raw)) return 'cloze';
    if (['reverse', 'basic-reverse', 'back-front'].includes(raw)) return 'reverse';
    return 'basic';
  }

  function safeImportDataUrl(value, kinds = ['image', 'audio', 'video']) {
    const src = safeMediaSrc(value);
    if (!src || /^data:image\/svg/i.test(src)) return '';
    const kindPattern = kinds.join('|');
    return new RegExp(`^data:(${kindPattern})/`, 'i').test(src) ? src : '';
  }

  function importMediaItem(value) {
    const source = typeof value === 'string' ? { src: value } : (value && typeof value === 'object' ? value : {});
    const src = safeImportDataUrl(source.src || source.url || source.dataUrl);
    if (!src) return null;
    const mime = String(source.mime || source.type || src.slice(5, src.indexOf(';') > 0 ? src.indexOf(';') : src.indexOf(','))).trim();
    const kind = mime.startsWith('audio/') ? 'audio' : mime.startsWith('video/') ? 'video' : 'image';
    return {
      id: createLocalId('media'),
      kind,
      mime,
      name: String(source.name || source.fileName || kind).trim() || kind,
      src,
      created: Date.now()
    };
  }

  function importMediaSide(value) {
    const items = Array.isArray(value) ? value : (value ? [value] : []);
    return items.map(importMediaItem).filter(Boolean).slice(0, 12);
  }

  function importBackgroundSide(value) {
    const source = typeof value === 'string' ? { src: value } : (value && typeof value === 'object' ? value : {});
    const src = safeImportDataUrl(source.src || source.url || source.dataUrl, ['image']);
    if (!src) return null;
    return {
      id: createLocalId('background'),
      src,
      mime: String(source.mime || source.type || 'image').trim(),
      name: String(source.name || source.fileName || 'Background').trim() || 'Background',
      fit: ['cover', 'contain'].includes(source.fit) ? source.fit : 'cover',
      opacity: Math.min(0.7, Math.max(0.08, Number(source.opacity ?? 0.32) || 0.32)),
      created: Date.now()
    };
  }

  function importCardObject(value) {
    if (Array.isArray(value)) {
      return {
        term: value[0],
        definition: value[1],
        tags: value[2],
        reverse: value[3],
        type: value[4]
      };
    }
    return value && typeof value === 'object' ? value : null;
  }

  function creatorCardFromImport(value) {
    const source = importCardObject(value);
    if (!source) return null;
    const requestedType = normalizeImportType(source.type || source.noteType || source.cardType || (source.advancedHtml ? 'advanced-html' : (source.occlusion || source.imageOcclusion ? 'image-occlusion' : 'basic')));
    const media = source.media && typeof source.media === 'object' ? source.media : {};
    const background = source.background && typeof source.background === 'object' ? source.background : {};
    const base = {
      ...emptyCreatorCard(),
      tags: normalizeImportTags(source.tags),
      media: {
        term: importMediaSide(media.term || source.termMedia || source.frontMedia),
        definition: importMediaSide(media.definition || source.definitionMedia || source.backMedia)
      },
      background: {
        term: importBackgroundSide(background.term || source.termBackground || source.frontBackground),
        definition: importBackgroundSide(background.definition || source.definitionBackground || source.backBackground)
      }
    };

    if (requestedType === 'advanced-html') {
      const advanced = source.advancedHtml && typeof source.advancedHtml === 'object' ? source.advancedHtml : {};
      const card = {
        ...base,
        noteType: 'advanced-html',
        cardTemplate: 'advanced-html',
        term: sanitizeEditorHtml(importString(source.term || source.front || source.question || source.prompt)),
        definition: sanitizeEditorHtml(importString(source.definition || source.back || source.answer || source.meaning)),
        advancedHtml: sanitizeAdvancedHtmlCard({
          frontHtml: advanced.frontHtml || source.frontHtml || advanced.html || source.html || '',
          backHtml: advanced.backHtml || source.backHtml || '',
          frontCss: advanced.frontCss || source.frontCss || advanced.css || source.css || '',
          backCss: advanced.backCss || source.backCss || advanced.css || source.css || ''
        })
      };
      return cardHasContent(card) ? card : null;
    }

    if (requestedType === 'image-occlusion') {
      const occlusion = source.occlusion && typeof source.occlusion === 'object'
        ? source.occlusion
        : (source.imageOcclusion && typeof source.imageOcclusion === 'object' ? source.imageOcclusion : {});
      const imageSource = typeof source.image === 'string'
        ? source.image
        : (source.image && typeof source.image === 'object' ? (source.image.dataUrl || source.image.src || source.image.url) : '');
      const image = safeImportDataUrl(occlusion.image || occlusion.dataUrl || imageSource, ['image']);
      if (!image) return null;
      const card = createImageOcclusionDraft({
        ...base,
        term: sanitizeEditorHtml(importString(source.term || source.title || source.prompt || 'Image occlusion')),
        definition: sanitizeEditorHtml(importString(source.definition || source.extra || ''))
      }, image);
      card.imageOcclusion = normalizeImageOcclusion({
        image,
        mode: occlusion.mode,
        masks: Array.isArray(occlusion.masks) ? occlusion.masks : []
      }, card);
      return cardHasContent(card) ? card : null;
    }

    if (requestedType === 'cloze') {
      const card = {
        ...base,
        term: sanitizeEditorHtml(importString(source.text || source.cloze || source.term || source.front)),
        definition: sanitizeEditorHtml(importString(source.extra || source.definition || source.back || source.answer))
      };
      return cardHasContent(card) ? card : null;
    }

    const card = {
      ...base,
      term: sanitizeEditorHtml(importString(source.term || source.front || source.question || source.prompt)),
      definition: sanitizeEditorHtml(importString(source.definition || source.back || source.answer || source.meaning)),
      generateReverse: requestedType === 'reverse' || importFlag(source.reverse)
    };
    return cardHasContent(card) ? card : null;
  }

  function parseDelimitedRows(text, delimiter) {
    const rows = [];
    let row = [];
    let field = '';
    let quoted = false;
    const input = String(text || '');
    const pushField = () => {
      row.push(field);
      field = '';
    };
    const pushRow = () => {
      pushField();
      if (row.some(cell => String(cell || '').trim())) rows.push(row);
      row = [];
    };

    for (let index = 0; index < input.length; index += 1) {
      const char = input[index];
      if (char === '"') {
        if (quoted && input[index + 1] === '"') {
          field += '"';
          index += 1;
        } else if (quoted) {
          quoted = false;
        } else if (!field) {
          quoted = true;
        } else {
          field += char;
        }
      } else if (char === delimiter && !quoted) {
        pushField();
      } else if ((char === '\n' || char === '\r') && !quoted) {
        if (char === '\r' && input[index + 1] === '\n') index += 1;
        pushRow();
      } else {
        field += char;
      }
    }
    if (field || row.length) pushRow();
    return rows;
  }

  function importHeaderName(value) {
    return String(value || '').trim().toLowerCase().replace(/[\s_-]+/g, '');
  }

  function importHeaderIndex(headers, names) {
    const targets = new Set(names);
    return headers.findIndex(header => targets.has(importHeaderName(header)));
  }

  function delimitedRowsHaveHeader(row = []) {
    const known = new Set(['term', 'front', 'question', 'prompt', 'text', 'cloze', 'definition', 'back', 'answer', 'meaning', 'tags', 'tag', 'reverse', 'type', 'cardtype', 'notetype']);
    return row.some(cell => known.has(importHeaderName(cell)));
  }

  function parseDelimitedImport(text, delimiter) {
    const rows = parseDelimitedRows(text, delimiter);
    if (!rows.length) return [];
    const hasHeader = delimitedRowsHaveHeader(rows[0]);
    const headers = hasHeader ? rows[0] : [];
    const indexes = {
      term: importHeaderIndex(headers, ['term', 'front', 'question', 'prompt', 'text', 'cloze']),
      definition: importHeaderIndex(headers, ['definition', 'back', 'answer', 'meaning']),
      tags: importHeaderIndex(headers, ['tags', 'tag']),
      reverse: importHeaderIndex(headers, ['reverse']),
      type: importHeaderIndex(headers, ['type', 'cardtype', 'notetype'])
    };
    return rows.slice(hasHeader ? 1 : 0)
      .map(row => {
        const data = hasHeader
          ? {
              term: indexes.term >= 0 ? row[indexes.term] : '',
              definition: indexes.definition >= 0 ? row[indexes.definition] : '',
              tags: indexes.tags >= 0 ? row[indexes.tags] : '',
              reverse: indexes.reverse >= 0 ? row[indexes.reverse] : '',
              type: indexes.type >= 0 ? row[indexes.type] : ''
            }
          : {
              term: row[0],
              definition: row[1],
              tags: row[2],
              reverse: row[3],
              type: row[4]
            };
        return creatorCardFromImport(data);
      })
      .filter(Boolean);
  }

  function parseJsonCreatorImport(text) {
    let json;
    try {
      json = JSON.parse(String(text || ''));
    } catch (_) {
      throw importUserError('Invalid JSON file');
    }
    const root = Array.isArray(json) ? { cards: json } : (json && typeof json === 'object' ? json : {});
    const deck = root.deck && typeof root.deck === 'object' ? root.deck : {};
    const rawCards = Array.isArray(root.cards)
      ? root.cards
      : (Array.isArray(root.flashcards) ? root.flashcards : (Array.isArray(deck.cards) ? deck.cards : []));
    if (rawCards.length > CREATOR_IMPORT_MAX_CARDS) {
      throw importUserError(`Import supports up to ${CREATOR_IMPORT_MAX_CARDS} cards`);
    }
    return {
      format: 'JSON',
      name: String(root.name || root.deckName || root.title || deck.name || deck.deckName || '').trim(),
      className: String(root.className || root.class || root.subject || deck.className || '').trim(),
      cards: rawCards.map(creatorCardFromImport).filter(Boolean)
    };
  }

  function parseCreatorImportFile(file, text) {
    const name = String(file?.name || '').toLowerCase();
    const type = String(file?.type || '').toLowerCase();
    let result;
    if (name.endsWith('.json') || type.includes('json')) {
      result = parseJsonCreatorImport(text);
    } else if (name.endsWith('.csv') || type.includes('csv')) {
      result = { format: 'CSV', cards: parseDelimitedImport(text, ',') };
    } else if (name.endsWith('.tsv') || type.includes('tab-separated')) {
      result = { format: 'TSV', cards: parseDelimitedImport(text, '\t') };
    } else {
      result = { format: 'TXT', cards: parseBulkCards(text) };
    }
    if ((result.cards || []).length > CREATOR_IMPORT_MAX_CARDS) {
      throw importUserError(`Import supports up to ${CREATOR_IMPORT_MAX_CARDS} cards`);
    }
    return result;
  }

  function applyCreatorImport(imported) {
    const cards = Array.isArray(imported?.cards) ? imported.cards : [];
    if (!cards.length) {
      showToast(`No valid ${imported?.format || 'file'} cards found`);
      return false;
    }

    syncCreatorFromDom();
    const currentName = String(selectors.createTitle?.value || '').trim();
    if (!currentName && imported.name && selectors.createTitle) {
      selectors.createTitle.value = imported.name;
    }
    if (!state.creator.classId && imported.className) {
      const match = state.classes.find(item => String(item.name || '').trim().toLowerCase() === imported.className.toLowerCase());
      if (match) state.creator.classId = match.id;
    }

    const existing = state.creator.cards.filter(hasCardContent);
    state.creator.cards = [...existing, ...cards];
    renderCreate();
    scheduleCreatorDraftSave();
    showToast(`Imported ${plural(cards.length, 'card')} from ${imported.format || 'file'}`);
    return true;
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
    state.creator.cards = creatorCardsFromStoredCards(normalized.cards || []);
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
      ? creatorCardsFromStoredCards(draft.cards)
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
      .map(card => {
        const normalized = cardWithNoteDefaults(card);
        const advanced = isAdvancedHtmlCard(normalized);
        return {
          ...normalized,
          term: sanitizeEditorHtml(advanced ? (normalized.term || advancedHtmlFallbackText(normalized, 'front')) : normalized.term),
          definition: sanitizeEditorHtml(advanced ? (normalized.definition || advancedHtmlFallbackText(normalized, 'back')) : normalized.definition),
          advancedHtml: sanitizeAdvancedHtmlCard(advancedHtmlPayload(normalized)),
          lastModified: Date.now()
        };
      })
      .filter(hasCardContent)
      .flatMap(expandCreatorCard);
    const syncedCards = syncGeneratedCards(cards);
    if (!name) {
      showToast('Add a deck name');
      selectors.createTitle?.focus();
      return;
    }
    if (!cards.length) {
      showToast('Add at least one card');
      selectors.creatorCards?.querySelector('[contenteditable="true"], textarea')?.focus();
      return;
    }

    const original = state.creator.originalSet || {};
    const saved = await window.flashcardStore.saveSet({
      ...original,
      id: state.creator.editingSetId || original.id,
      name,
      classId: state.creator.classId || null,
      cards: syncedCards,
      srsSettings: schema?.normalizeSrsSettings ? schema.normalizeSrsSettings(original.srsSettings || {}) : (original.srsSettings || { enabled: true }),
      pinned: Boolean(original.pinned)
    });
    await clearCreatorDraft();
    // Flush store in background — no need to block navigation on it
    flushStore(1800).catch(err => console.warn('[mobile] flushStore after save:', err));
    showToast(`Saved ${plural(syncedCards.length, 'card')}`);
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
    const noteType = String(card.noteType || '').toLowerCase();
    const template = String(card.cardTemplate || '').toLowerCase();
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
      case 'reverse':
        return template === 'back-front' || noteType === 'basic-reverse';
      case 'cloze':
        return noteType === 'cloze';
      case 'image-occlusion':
        return noteType === 'image-occlusion';
      case 'advanced-html':
        return noteType === 'advanced-html' || template === 'advanced-html';
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

  function browserNoteTypeLabel(card = {}) {
    const noteType = String(card.noteType || '').toLowerCase();
    const template = String(card.cardTemplate || '').toLowerCase();
    if (noteType === 'advanced-html' || template === 'advanced-html') return 'HTML/CSS';
    if (noteType === 'cloze') return 'Cloze';
    if (noteType === 'image-occlusion') return 'Occlusion';
    if (template === 'back-front') return 'Reverse';
    if (noteType === 'basic-reverse') return 'Basic + Reverse';
    return '';
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
    const noteLabel = browserNoteTypeLabel(card);
    const flags = [
      noteLabel ? `<span>${escapeHtml(noteLabel)}</span>` : '',
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
        : inputType === 'textarea'
          ? `<textarea class="mobile-modal-input mobile-modal-textarea" id="browser-action-field" rows="7" placeholder="${escapeAttr(placeholder)}" autocomplete="off" spellcheck="false">${escapeHtml(value)}</textarea>`
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

    const htmlInteractionEnabled = state.settings?.htmlInteractionDisabled !== true;
    selectors.htmlInteractionSwitch?.classList.toggle('on', htmlInteractionEnabled);
    if (selectors.moreHtmlInteractionLabel) {
      selectors.moreHtmlInteractionLabel.textContent = htmlInteractionEnabled
        ? 'On - HTML can scroll and receive taps'
        : 'Off - swipe and tap the whole HTML card';
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
    if (cover) {
      cover.style.display = '';
      cover.classList.add('no-anim');
    }
    document.body.classList.remove('app-ready');
    document.body.classList.add('is-route-loading');
  }

  function hideAppLoader() {
    document.body.classList.add('app-ready');
    document.body.classList.remove('is-route-loading');
    setTimeout(() => {
      const cover = document.getElementById('app-loading-cover');
      if (cover) {
        cover.style.display = 'none';
        cover.classList.remove('no-anim');
      }
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
    if (options.filter) query.set('filter', String(options.filter));
    if (options.tag) query.set('tag', String(options.tag));
    if (options.preview) query.set('preview', 'true');
    if (options.reschedule) query.set('reschedule', 'true');
    return `mobile/study.html?${query.toString()}`;
  }

  async function startCustomStudy(filter, tag = '', options = {}) {
    await loadAnalyticsCards();
    const choice = customStudyDeckChoice(filter, tag);
    if (!choice) {
      showToast('No cards match that custom study');
      renderCustomStudyPanel();
      return;
    }
    const reschedule = Boolean(options.reschedule);
    navigateTo(mobileStudyUrl(choice.setId, {
      srsMode: reschedule,
      filter,
      tag,
      preview: !reschedule,
      reschedule
    }), {
      title: customStudyFilterLabel(filter, tag),
      copy: reschedule ? 'Opening filtered review' : 'Opening preview session'
    });
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

  async function toggleHtmlInteraction() {
    const interactionEnabled = state.settings?.htmlInteractionDisabled !== true;
    state.settings = {
      ...(state.settings || {}),
      htmlInteractionDisabled: interactionEnabled
    };
    if (window.flashcardStore?.saveSettings) {
      await window.flashcardStore.saveSettings(state.settings);
    }
    playClick();
    renderMore();
    showToast(interactionEnabled
      ? 'HTML card interaction disabled'
      : 'HTML card interaction enabled');
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
  function normalizeFormulaText(raw) {
    return String(raw || '')
      .replace(/[−–—]/g, '-')
      .replace(/[×✕]/g, '\\times ')
      .replace(/[÷]/g, '\\div ')
      .replace(/[≈]/g, '\\approx ')
      .replace(/[≤]/g, '\\le ')
      .replace(/[≥]/g, '\\ge ')
      .replace(/[≠]/g, '\\ne ')
      .replace(/[π]/g, '\\pi ')
      .replace(/[θ]/g, '\\theta ')
      .replace(/[α]/g, '\\alpha ')
      .replace(/[β]/g, '\\beta ')
      .replace(/[γ]/g, '\\gamma ')
      .replace(/[μ]/g, '\\mu ')
      .replace(/[Ω]/g, '\\Omega ')
      .replace(/(\d)\s+x\s+(\d)/gi, '$1 \\times $2')
      .trim();
  }

  function mathStepsFormula(raw) {
    const lines = String(raw || '')
      .split(/\r?\n/)
      .map(line => normalizeFormulaText(line))
      .filter(Boolean)
      .map(line => {
        const operatorMatch = line.match(/^(=|\\approx|≈|\\le|≤|\\ge|≥|<|>|\+|-)\s*(.*)$/);
        if (operatorMatch) {
          const op = normalizeFormulaText(operatorMatch[1]);
          return `&${op} ${operatorMatch[2] || ''}`.trim();
        }
        return `&${line}`;
      });
    if (!lines.length) return '';
    return `\\[\\begin{aligned}${lines.join('\\\\')}\\end{aligned}\\]`;
  }

  function formulaMarkup(raw, mode = 'inline') {
    const value = normalizeFormulaText(raw);
    if (!value) return '';
    if (mode === 'steps') return mathStepsFormula(raw);
    if (mode === 'display') {
      return window.EruditeMath?.blockFormula ? window.EruditeMath.blockFormula(value) : `\\[${value}\\]`;
    }
    return window.EruditeMath?.inlineFormula ? window.EruditeMath.inlineFormula(value) : `\\(${value}\\)`;
  }

  function insertFormulaSnippet(input, snippet) {
    if (!input || !snippet) return;
    const start = Number(input.selectionStart || 0);
    const end = Number(input.selectionEnd || start);
    const selected = input.value.slice(start, end);
    let text = String(snippet).replace('|', selected || '');
    let caret = text.indexOf('|');
    if (caret >= 0) text = text.replace('|', '');
    else caret = text.indexOf('{}');
    input.setRangeText(text, start, end, 'end');
    const nextPos = caret >= 0 ? start + caret + (caret === text.indexOf('{}') ? 1 : 0) : start + text.length;
    input.focus();
    input.setSelectionRange(nextPos, nextPos);
    input.dispatchEvent(new Event('input', { bubbles: true }));
  }

  function renderFormulaPalette() {
    const grid = selectors.formulaSymbolGrid;
    if (!grid) return;
    grid.innerHTML = FORMULA_SYMBOL_GROUPS.map(group => `
      <section class="formula-symbol-group">
        <strong>${escapeHtml(group.label)}</strong>
        <div>
          ${group.items.map(([label, insert]) => `
            <button type="button" data-formula-insert="${escapeAttr(insert)}">${escapeHtml(label)}</button>
          `).join('')}
        </div>
      </section>
    `).join('');
  }

  function updateFormulaPreview(mode = 'inline') {
    const preview = selectors.formulaPreview;
    const input = selectors.formulaInput;
    if (!preview || !input) return;
    const markup = formulaMarkup(input.value, mode);
    preview.innerHTML = markup
      ? `<div class="formula-preview-card">${escapeHtml(markup)}</div>`
      : '<div class="formula-preview-empty">Preview appears here</div>';
    if (markup) {
      const card = preview.querySelector('.formula-preview-card');
      window.EruditeMath?.renderMath?.(card);
    }
  }

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

    let mode = 'inline';
    input.value = '';
    renderFormulaPalette();
    overlay.querySelectorAll('[data-formula-mode]').forEach(button => {
      button.classList.toggle('active', button.dataset.formulaMode === mode);
    });
    updateFormulaPreview(mode);
    overlay.classList.remove('hidden');
    requestAnimationFrame(() => input.focus());

    function setMode(nextMode) {
      mode = ['inline', 'display', 'steps'].includes(nextMode) ? nextMode : 'inline';
      overlay.querySelectorAll('[data-formula-mode]').forEach(button => {
        button.classList.toggle('active', button.dataset.formulaMode === mode);
      });
      input.placeholder = mode === 'steps'
        ? '45 \\times 34\n= 1350 + 180\n= 1530'
        : mode === 'display'
          ? '\\frac{mv^2}{r} = qvB'
          : 'E=mc^2';
      updateFormulaPreview(mode);
    }

    function doInsert() {
      const rawInput = String(input.value || '').trim();
      overlay.classList.add('hidden');
      cleanup();
      if (!rawInput) return;
      const formula = formulaMarkup(rawInput, mode);
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
      if (e.key === 'Enter' && mode !== 'steps' && !e.shiftKey) { e.preventDefault(); doInsert(); }
      if (e.key === 'Escape') doCancel();
    }

    function handleModeClick(event) {
      const button = event.target.closest('[data-formula-mode]');
      if (!button) return;
      setMode(button.dataset.formulaMode);
    }

    function handlePaletteClick(event) {
      const button = event.target.closest('[data-formula-insert]');
      if (!button) return;
      event.preventDefault();
      insertFormulaSnippet(input, button.dataset.formulaInsert || '');
    }

    function handleInput() {
      updateFormulaPreview(mode);
    }

    function cleanup() {
      selectors.formulaConfirm?.removeEventListener('click', doInsert);
      selectors.formulaCancel?.removeEventListener('click', doCancel);
      overlay.removeEventListener('click', handleModeClick);
      selectors.formulaSymbolGrid?.removeEventListener('click', handlePaletteClick);
      input.removeEventListener('input', handleInput);
      input.removeEventListener('keydown', handleKeydown);
    }

    selectors.formulaConfirm?.addEventListener('click', doInsert);
    selectors.formulaCancel?.addEventListener('click', doCancel);
    overlay.addEventListener('click', handleModeClick);
    selectors.formulaSymbolGrid?.addEventListener('click', handlePaletteClick);
    input.addEventListener('input', handleInput);
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

  function buildImportJsonAiPrompt() {
    return [
      'Create an Erudite Flashcards import JSON file.',
      '',
      'Return valid JSON only. Do not wrap it in Markdown. Do not add comments.',
      'Use this content-only shape:',
      '{',
      '  "version": 1,',
      '  "name": "Deck name",',
      '  "className": "Optional existing class name",',
      '  "cards": [',
      '    { "type": "basic", "term": "Question", "definition": "Answer", "tags": ["tag"], "reverse": false },',
      '    { "type": "cloze", "text": "The SI unit of force is {{c1::newton}}." },',
      '    { "type": "image-occlusion", "term": "Diagram title", "image": { "dataUrl": "data:image/png;base64,..." }, "occlusion": { "masks": [{ "shape": "rect", "x": 0.12, "y": 0.2, "w": 0.25, "h": 0.1, "answer": "Nucleus" }] } },',
      '    {',
      '      "type": "advanced-html",',
      '      "term": "Short searchable front text",',
      '      "definition": "Short searchable back text",',
      '      "advancedHtml": {',
      '        "frontHtml": "<div class=\\"card-design\\">...</div>",',
      '        "frontCss": ".card-design{width:340px;min-height:470px;border-radius:20px;overflow:auto}",',
      '        "backHtml": "<div class=\\"card-design\\">...</div>",',
      '        "backCss": ".card-design{width:340px;min-height:470px;border-radius:20px;overflow:auto}"',
      '      }',
      '    }',
      '  ]',
      '}',
      '',
      'Rules:',
      '- Never include id, noteId, srs, reviewHistory, due dates, reps, lapses, streaks, or analytics fields.',
      '- Use math as "\\\\(F = ma\\\\)" for inline math or "\\\\[x^2 + y^2\\\\]" for display math.',
      '- Safe rich text may use b, strong, i, em, u, lists, blockquote, code, pre, hr, and mark highlight-yellow/green/blue/pink.',
      '- Image occlusion masks use normalized x/y/w/h values from 0 to 1 and require an answer. Use data URL images only.',
      `- Advanced HTML cards live inside a ${ADVANCED_HTML_CANVAS.width}px x ${ADVANCED_HTML_CANVAS.height}px canvas with ${ADVANCED_HTML_CANVAS.radius}px corner radius.`,
      '- Advanced HTML must use HTML and CSS only: no JavaScript, no scripts, no iframes, no forms, no external URLs, no fixed/sticky overlays.',
      '- Keep every card readable on a mobile phone.'
    ].join('\n');
  }

  function openImportHelpModal() {
    selectors.importHelpOverlay?.classList.remove('hidden');
  }

  function closeImportHelpModal() {
    selectors.importHelpOverlay?.classList.add('hidden');
    state.lastModalClosedAt = Date.now();
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
      // 5. Do not use the hardware back button for in-app tab navigation.
      // On any main tab, double-press exits the app.
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
      const active = Boolean(activeEditor && command && (
        command === 'highlight'
          ? selectionHasAncestor(['MARK'])
          : command === 'inlineCode'
            ? selectionHasAncestor(['CODE'])
            : command === 'codeBlock'
              ? selectionHasAncestor(['PRE'])
              : command !== 'formula' && document.queryCommandState(command)
      ));
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
            newCardEl.closest('.mobile-card-editor')?.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
          }
        });
        break;
      }
      case 'bulk-add-cards':
        openBulkCardModal();
        break;
      case 'insert-card-after': {
        syncCreatorFromDom();
        const index = state.creator.cards.findIndex(card => String(card.id) === String(target.dataset.cardId));
        const insertIndex = index >= 0 ? index + 1 : state.creator.cards.length;
        const [card] = addBlankCreatorCards(1, insertIndex);
        renderCreate();
        scheduleCreatorDraftSave();
        focusCreatorCard(card.id);
        showToast('Card inserted');
        break;
      }
      case 'move-card-up':
      case 'move-card-down': {
        syncCreatorFromDom();
        const index = state.creator.cards.findIndex(card => String(card.id) === String(target.dataset.cardId));
        const delta = action === 'move-card-up' ? -1 : 1;
        const nextIndex = index + delta;
        if (index < 0 || nextIndex < 0 || nextIndex >= state.creator.cards.length) break;
        const [card] = state.creator.cards.splice(index, 1);
        state.creator.cards.splice(nextIndex, 0, card);
        renderCreate();
        scheduleCreatorDraftSave();
        scrollCreatorCardIntoView(card.id);
        break;
      }
      case 'delete-card': {
        if (target.dataset.longDeleteFired === '1') {
          target.dataset.longDeleteFired = '';
          break;
        }
        syncCreatorFromDom();
        state.creator.cards = state.creator.cards.filter(card => String(card.id) !== String(target.dataset.cardId));
        ensureCreatorCard();
        renderCreate();
        scheduleCreatorDraftSave();
        break;
      }
      case 'reverse-card': {
        syncCreatorFromDom();
        const index = state.creator.cards.findIndex(card => String(card.id) === String(target.dataset.cardId));
        if (index < 0) break;
        const source = cardWithNoteDefaults(state.creator.cards[index]);
        if (isAdvancedHtmlCard(source)) {
          showToast('HTML cards use their own front and back');
          break;
        }
        if (!plainTextFromHtml(source.term).trim() || !plainTextFromHtml(source.definition).trim()) {
          showToast('Add term and definition first');
          break;
        }
        const nextEnabled = !creatorCardWantsReverse(source);
        const noteId = String(source.noteId || '');
        state.creator.cards = state.creator.cards.filter(card => (
          String(card.id) === String(source.id)
          || String(card.noteId || '') !== noteId
          || !isReverseTemplate(card)
        ));
        const nextIndex = state.creator.cards.findIndex(card => String(card.id) === String(source.id));
        state.creator.cards[nextIndex >= 0 ? nextIndex : index] = {
          ...source,
          noteType: nextEnabled ? 'basic-reverse' : 'basic',
          cardTemplate: 'front-back',
          generateReverse: nextEnabled,
          noteFields: {
            front: source.term || '',
            back: source.definition || ''
          }
        };
        renderCreate();
        scheduleCreatorDraftSave();
        showToast(nextEnabled ? 'Reverse enabled' : 'Reverse disabled');
        break;
      }
      case 'advanced-html-card': {
        syncCreatorFromDom();
        const index = state.creator.cards.findIndex(card => String(card.id) === String(target.dataset.cardId));
        if (index < 0) break;
        const source = state.creator.cards[index];
        if (isAdvancedHtmlCard(source)) {
          state.creator.cards[index] = {
            ...source,
            noteType: 'basic',
            cardTemplate: 'front-back',
            generateReverse: false,
            term: source.term || sanitizeEditorHtml(advancedHtmlFallbackText(source, 'front')),
            definition: source.definition || sanitizeEditorHtml(advancedHtmlFallbackText(source, 'back'))
          };
          renderCreate();
          scheduleCreatorDraftSave();
          showToast('HTML card disabled');
          break;
        }
        state.creator.cards[index] = {
          ...source,
          noteType: 'advanced-html',
          cardTemplate: 'advanced-html',
          generateReverse: false,
          advancedHtml: sanitizeAdvancedHtmlCard({
            frontHtml: advancedHtmlPayload(source).frontHtml || advancedHtmlPayload(source).html || source.term || '',
            backHtml: advancedHtmlPayload(source).backHtml || source.definition || '',
            frontCss: advancedHtmlPayload(source).frontCss || advancedHtmlPayload(source).css || '',
            backCss: advancedHtmlPayload(source).backCss || advancedHtmlPayload(source).css || ''
          })
        };
        renderCreate();
        scheduleCreatorDraftSave();
        showToast('HTML card enabled');
        break;
      }
      case 'basic-card': {
        syncCreatorFromDom();
        const index = state.creator.cards.findIndex(card => String(card.id) === String(target.dataset.cardId));
        if (index < 0) break;
        const source = state.creator.cards[index];
        const wasOcclusion = isImageOcclusionCard(source);
        const occlusionImage = wasOcclusion ? normalizeImageOcclusion(source.imageOcclusion, source).image : '';
        state.creator.cards[index] = {
          ...source,
          noteType: 'basic',
          cardTemplate: 'front-back',
          generateReverse: false,
          imageOcclusion: null,
          termImage: source.termImage || occlusionImage || '',
          term: source.term || sanitizeEditorHtml(advancedHtmlFallbackText(source, 'front')),
          definition: source.definition || sanitizeEditorHtml(advancedHtmlFallbackText(source, 'back'))
        };
        renderCreate();
        scheduleCreatorDraftSave();
        showToast('Basic card enabled');
        break;
      }
      case 'copy-html-prompt': {
        syncCreatorFromDom();
        const card = state.creator.cards.find(item => String(item.id) === String(target.dataset.cardId));
        if (!card) break;
        const copied = await copyPlainText(buildAdvancedHtmlPrompt(card));
        showToast(copied ? 'Prompt copied' : 'Could not copy prompt');
        break;
      }
      case 'cloze': {
        const side = target.dataset.side === 'definition' ? 'definition' : 'term';
        insertClozeAtCaret(target.dataset.cardId, side);
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
        } else if (command === 'highlight') {
          if (state.suppressNextHighlightClick) {
            state.suppressNextHighlightClick = false;
            break;
          }
          insertHighlightContent();
        } else if (command === 'inlineCode') {
          insertInlineCodeContent();
        } else if (command === 'codeBlock') {
          insertCodeBlockContent();
        } else {
          document.execCommand(command, false, null);
        }
        updateFormatState();
        scheduleCreatorDraftSave();
        break;
      }
      case 'image-occlusion': {
        syncCreatorFromDom();
        const index = state.creator.cards.findIndex(card => String(card.id) === String(target.dataset.cardId));
        if (index < 0) break;
        const source = state.creator.cards[index];
        if (isAdvancedHtmlCard(source)) {
          showToast('HTML cards cannot use image occlusion');
          break;
        }
        const imageSrc = firstCardImageSource(source);
        if (!imageSrc) {
          state.pendingImageTarget = {
            cardId: source.id,
            side: 'term',
            mode: 'occlusion'
          };
          selectors.occlusionImageInput?.click();
          break;
        }
        openOcclusionEditor(source.id);
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
      case 'import-file':
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
      case 'start-custom-study':
        await startCustomStudy(target.dataset.filter || '', target.dataset.tag || '');
        break;
      case 'start-custom-study-reschedule':
        await startCustomStudy(target.dataset.filter || '', target.dataset.tag || '', { reschedule: true });
        break;
      case 'refresh-analytics':
        playClick();
        state.analyticsLoaded = false;
        await loadAnalyticsCards({ force: true });
        break;
      case 'analytics-window':
        state.analyticsWindow = normalizeAnalyticsWindow(target.dataset.window);
        playClick();
        renderAnalyticsDashboard();
        break;
      case 'toggle-srs':
        await toggleSrs();
        break;
      case 'toggle-sound':
        await toggleSound();
        break;
      case 'toggle-html-interaction':
        await toggleHtmlInteraction();
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
      case 'import-help':
        openImportHelpModal();
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
    const isNativeEditableTarget = target => {
      const element = target?.nodeType === Node.ELEMENT_NODE ? target : target?.parentElement;
      return Boolean(element?.closest?.([
        'input',
        'textarea',
        'select',
        '[contenteditable="true"]',
        '.rich-editor',
        '.advanced-html-textarea'
      ].join(',')));
    };

    document.addEventListener('contextmenu', event => {
      if (isNativeEditableTarget(event.target)) return;
      event.preventDefault();
    }, { capture: true });

    document.addEventListener('dragstart', event => {
      if (isNativeEditableTarget(event.target)) return;
      event.preventDefault();
    }, { capture: true });

    document.addEventListener('selectstart', event => {
      if (isNativeEditableTarget(event.target)) return;
      event.preventDefault();
    }, { capture: true });

    document.addEventListener('pointerdown', event => {
      if (event.pointerType === 'mouse' && event.target.closest('[data-creator-action="format"]')) {
        event.preventDefault();
      }
      const highlightButton = event.target.closest('[data-creator-action="format"][data-command="highlight"]');
      if (highlightButton) {
        clearTimeout(highlightHoldTimer);
        highlightHoldTimer = window.setTimeout(() => {
          state.suppressNextHighlightClick = true;
          triggerHaptic();
          openHighlightColorMenu().catch(error => console.warn('[mobile] highlight color menu failed:', error));
        }, 520);
      }
      const deleteButton = event.target.closest('[data-creator-action="delete-card"]');
      if (deleteButton) {
        clearTimeout(creatorDeleteHoldTimer);
        deleteButton.dataset.longDeleteFired = '';
        creatorDeleteHoldTimer = window.setTimeout(() => {
          creatorDeleteHoldTimer = null;
          deleteButton.dataset.longDeleteFired = '1';
          triggerHaptic();
          confirmDeleteCardsFrom(deleteButton.dataset.cardId)
            .catch(error => console.warn('[mobile] bulk delete confirm failed:', error));
        }, 620);
      }
    });

    ['pointerup', 'pointercancel', 'pointerleave'].forEach(type => {
      document.addEventListener(type, () => {
        clearTimeout(highlightHoldTimer);
        highlightHoldTimer = null;
        clearTimeout(creatorDeleteHoldTimer);
        creatorDeleteHoldTimer = null;
      });
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

    selectors.occlusionImageInput?.addEventListener('change', async event => {
      const file = event.target.files?.[0];
      const target = state.pendingImageTarget;
      event.target.value = '';
      state.pendingImageTarget = null;
      if (!file || !target) return;
      if (!file.type.startsWith('image/')) {
        showToast('Use an image for occlusion');
        return;
      }
      syncCreatorFromDom();
      const index = state.creator.cards.findIndex(card => String(card.id) === String(target.cardId));
      if (index < 0) return;
      try {
        const src = await window.flashcardStore.saveImageFromFile(file, {
          deckId: state.creator.editingSetId || 'draft',
          side: 'term',
          prefix: 'occlusion'
        });
        state.creator.cards[index] = {
          ...state.creator.cards[index],
          termImage: src
        };
        openOcclusionEditor(state.creator.cards[index].id);
      } catch (error) {
        console.error(error);
        showToast('Could not add occlusion image');
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
        const imported = parseCreatorImportFile(file, text);
        applyCreatorImport(imported);
      } catch (error) {
        console.error(error);
        showToast(error.userMessage || 'Could not import file');
      }
    });

    selectors.bulkCardCancel?.addEventListener('click', event => {
      event.preventDefault();
      playClick();
      closeBulkCardModal();
    });

    selectors.bulkCardConfirm?.addEventListener('click', event => {
      event.preventDefault();
      playClick();
      syncCreatorFromDom();
      const count = boundedBulkCardCount(selectors.bulkCardCount?.value);
      if (selectors.bulkCardCount) selectors.bulkCardCount.value = String(count);
      const cards = addBlankCreatorCards(count);
      renderCreate();
      scheduleCreatorDraftSave();
      closeBulkCardModal();
      if (cards.length) scrollCreatorCardIntoView(cards[0].id, 'nearest');
      showToast(`Added ${plural(count, 'blank card')}`);
    });

    selectors.bulkCardCount?.addEventListener('keydown', event => {
      if (event.key === 'Enter') {
        event.preventDefault();
        selectors.bulkCardConfirm?.click();
      }
    });

    document.querySelectorAll('[data-bulk-card-preset]').forEach(button => {
      button.addEventListener('click', event => {
        event.preventDefault();
        playClick();
        if (selectors.bulkCardCount) {
          selectors.bulkCardCount.value = button.dataset.bulkCardPreset || '10';
          selectors.bulkCardCount.focus();
        }
      });
    });

    selectors.occlusionClose?.addEventListener('click', event => {
      event.preventDefault();
      playClick();
      closeOcclusionEditor({ restoreOriginal: true });
    });

    selectors.occlusionCancel?.addEventListener('click', event => {
      event.preventDefault();
      playClick();
      closeOcclusionEditor({ restoreOriginal: true });
    });

    selectors.occlusionSave?.addEventListener('click', event => {
      event.preventDefault();
      playClick();
      saveOcclusionEditor();
    });

    selectors.occlusionAddMask?.addEventListener('click', event => {
      event.preventDefault();
      playClick();
      updateSelectedOcclusionText();
      addOcclusionMask();
    });

    selectors.occlusionDeleteMask?.addEventListener('click', event => {
      event.preventDefault();
      playClick();
      deleteSelectedOcclusionMask();
    });

    selectors.occlusionShapeRect?.addEventListener('click', event => {
      event.preventDefault();
      playClick();
      setOcclusionShape('rect');
      const mask = selectedOcclusionMask();
      if (mask) {
        mask.shape = 'rect';
        renderOcclusionEditor();
      }
    });

    selectors.occlusionShapeEllipse?.addEventListener('click', event => {
      event.preventDefault();
      playClick();
      setOcclusionShape('ellipse');
      const mask = selectedOcclusionMask();
      if (mask) {
        mask.shape = 'ellipse';
        renderOcclusionEditor();
      }
    });

    selectors.occlusionAnswer?.addEventListener('input', updateSelectedOcclusionText);
    selectors.occlusionHint?.addEventListener('input', updateSelectedOcclusionText);
    selectors.occlusionLayer?.addEventListener('pointerdown', startOcclusionPointer);
    selectors.occlusionLayer?.addEventListener('pointermove', moveOcclusionPointer);
    selectors.occlusionLayer?.addEventListener('pointerup', endOcclusionPointer);
    selectors.occlusionLayer?.addEventListener('pointercancel', endOcclusionPointer);
    window.addEventListener('resize', () => {
      if (!selectors.occlusionOverlay?.classList.contains('hidden')) {
        requestAnimationFrame(renderOcclusionEditor);
      }
    });

    selectors.importHelpClose?.addEventListener('click', event => {
      event.preventDefault();
      playClick();
      closeImportHelpModal();
    });

    selectors.importHelpCopy?.addEventListener('click', async event => {
      event.preventDefault();
      playClick();
      const ok = await copyPlainText(buildImportJsonAiPrompt());
      showToast(ok ? 'AI prompt copied' : 'Could not copy prompt');
    });

    selectors.importHelpOverlay?.addEventListener('click', event => {
      if (event.target !== selectors.importHelpOverlay) return;
      event.preventDefault();
      playClick();
      closeImportHelpModal();
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
    const resetSwipeStart = () => {
      startX = 0;
      startY = 0;
      startTime = 0;
    };
    const isHorizontalScroller = element => {
      let node = element?.nodeType === Node.ELEMENT_NODE ? element : element?.parentElement;
      while (node && node !== document.body) {
        const style = window.getComputedStyle(node);
        const overflowX = style.overflowX;
        if ((overflowX === 'auto' || overflowX === 'scroll') && node.scrollWidth > node.clientWidth + 2) {
          return true;
        }
        node = node.parentElement;
      }
      return false;
    };

    document.addEventListener('touchstart', (e) => {
      resetSwipeStart();
      if (e.touches.length > 1) return;

      const target = e.target;
      
      // Exclude controls and horizontally scrollable UI from tab-swipe navigation.
      const ignoreSelector = [
        'button',
        '[role="button"]',
        'input',
        'textarea',
        'select',
        '[contenteditable="true"]',
        '.rich-editor',
        '.creator-toolbar',
        '.filter-strip',
        '.deck-source-switch',
        '.mobile-opacity-slider',
        '.formula-palette',
        '.mobile-modal-card'
      ].join(',');
      if (target.closest(ignoreSelector) || isHorizontalScroller(target)) {
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
      resetSwipeStart();
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
      headerImportBtn.classList.remove('hidden');
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
