(function () {
  const core = window.EruditeCore || {};
  const schema = core.schema;
  const statsCore = core.stats;

  const state = {
    sets: [],
    classes: [],
    settings: {},
    srsMode: false,
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
      cards: []
    },
    pendingImageTarget: null,
    busy: false
  };

  const premadeClasses = [
    { id: '10th', name: 'Class 10' },
    { id: '11th', name: 'Class 11' },
    { id: '12th', name: 'Class 12' }
  ];

  const premadeSubjects = {
    '10th': ['Science', 'Maths', 'English', 'Civics', 'Geography', 'History', 'Hindi', 'Politics'],
    '11th': ['Physics', 'inorganic-chemistry', 'organic-chemistry', 'physical-chemistry', 'English', 'Maths', 'Biology', 'Physical-education'],
    '12th': ['Physics', 'inorganic-chemistry', 'organic-chemistry', 'physical-chemistry', 'English', 'Maths', 'Biology', 'Physical-education']
  };

  const sortOrder = ['recent', 'name', 'cards', 'due'];
  const sortLabels = {
    recent: 'Most recent',
    name: 'A to Z',
    cards: 'Cards',
    due: 'Due'
  };

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
    createClass: document.getElementById('mobile-create-class'),
    creatorCards: document.getElementById('mobile-creator-cards'),
    imageInput: document.getElementById('mobile-image-input'),
    txtInput: document.getElementById('mobile-txt-input'),
    premadeClassFilters: document.getElementById('premade-class-filters'),
    premadeSubjectFilters: document.getElementById('premade-subject-filters'),
    premadeList: document.getElementById('premade-list'),
    browserSearchInput: document.getElementById('browser-search-input'),
    browserList: document.getElementById('browser-list'),
    srsSwitch: document.getElementById('srs-switch'),
    moreSrsLabel: document.getElementById('more-srs-label'),
    loadingCover: document.getElementById('app-loading-cover'),
    loadingTitle: document.getElementById('app-loading-title'),
    loadingCopy: document.getElementById('app-loading-copy'),
    toast: document.getElementById('mobile-toast')
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
    window.flashcardStore?.setState?.('srsModeEnabled', state.srsMode).catch(error => {
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
    if (!dayKeys.size) {
      reviewedDates().forEach(time => {
        const date = new Date(time);
        date.setHours(0, 0, 0, 0);
        dayKeys.add(String(date.getTime()));
      });
    }
    let streak = 0;
    const cursor = new Date();
    cursor.setHours(0, 0, 0, 0);
    while (dayKeys.has(String(cursor.getTime()))) {
      streak += 1;
      cursor.setDate(cursor.getDate() - 1);
    }
    return streak;
  }

  function progressPercent(set) {
    const cardCount = setCardCount(set);
    if (!cardCount) return 0;
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

  function playClick() {
    try {
      const audio = new Audio('assets/flashcard-assets/click.mp3');
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

  async function configureSystemBars() {
    const SystemBars = window.Capacitor?.Plugins?.SystemBars;
    if (!SystemBars) return;
    await SystemBars.setStyle?.({ style: 'DARK' }).catch(() => {});
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
    const [sets, classes, settings, srsMode] = await Promise.all([
      listSetsFast.call(window.flashcardStore),
      window.flashcardStore.listClasses(),
      window.flashcardStore.getSettings(),
      window.flashcardStore.getState('srsModeEnabled')
    ]);
    state.sets = (sets || []).map(set => schema?.normalizeSet ? schema.normalizeSet(set, null, { preserveLastModified: true }) : set);
    state.classes = (classes || []).map(item => schema?.normalizeClass ? schema.normalizeClass(item, null, { preserveLastModified: true }) : item);
    state.settings = settings || {};
    state.srsMode = readSrsMode(srsMode);
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

  function setActiveTab(tab) {
    state.activeTab = tab;
    selectors.views.forEach(view => view.classList.toggle('active', view.id === `view-${tab}`));
    selectors.tabs.forEach(button => button.classList.toggle('active', button.dataset.tab === tab));
    setHeader();
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

    return `
      <article class="deck-row" data-set-card="${escapeAttr(set.id)}">
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
        <div class="deck-actions">
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
    const progress = dailyWork > 0 ? clamp(Math.round((todayReviews / dailyWork) * 100), 0, 100) : 0;
    const progressLabel = dailyWork > 0 ? 'Goal' : 'Ready';
    const reviewAction = totals.dueCards > 0 ? 'review-due-smart' : 'tab-library';
    const reviewLabel = totals.dueCards > 0 ? `Review ${totals.dueCards} Left` : 'Open Library';

    selectors.todayHero.innerHTML = `
      <div class="hero-dashboard">
        <button type="button" class="goal-ring" data-action="${reviewAction}" style="--progress:${progress * 3.6}deg" aria-label="${escapeAttr(reviewLabel)}">
          <div><strong>${progress}%</strong><span>${progressLabel}</span></div>
        </button>
        <div class="hero-metrics">
          <button type="button" class="metric-pill" data-action="tab-library"><strong>${totals.setCount}</strong><span>Decks</span></button>
          <button type="button" class="metric-pill" data-action="${reviewAction}"><strong>${todayReviews}</strong><span>Reviewed</span></button>
          <button type="button" class="metric-pill" data-action="${reviewAction}"><strong>${streak}</strong><span>Day streak</span></button>
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
        <button type="button" class="class-card" data-action="open-class" data-class-id="${escapeAttr(classItem.id)}" style="--class-color:${color}">
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

  function emptyCreatorCard() {
    const now = Date.now();
    return {
      id: schema?.createId ? schema.createId('card') : `card-${now}-${Math.random().toString(36).slice(2)}`,
      term: '',
      definition: '',
      termImage: '',
      definitionImage: '',
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
    state.creator.editingSetId = null;
    state.creator.originalSet = null;
    state.creator.classId = '';
    state.creator.cards = [emptyCreatorCard()];
    if (selectors.createTitle) selectors.createTitle.value = '';
    if (selectors.createClass) selectors.createClass.value = '';
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

  function cardEditor(card, index) {
    const termImage = card.termImage
      ? `<div class="creator-image-preview"><img src="${escapeAttr(card.termImage)}" alt=""><button type="button" data-creator-action="remove-image" data-card-id="${escapeAttr(card.id)}" data-side="term" aria-label="Remove term image"><i class="fas fa-xmark"></i></button></div>`
      : '';
    const definitionImage = card.definitionImage
      ? `<div class="creator-image-preview"><img src="${escapeAttr(card.definitionImage)}" alt=""><button type="button" data-creator-action="remove-image" data-card-id="${escapeAttr(card.id)}" data-side="definition" aria-label="Remove definition image"><i class="fas fa-xmark"></i></button></div>`
      : '';

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
              <button type="button" class="format-button" data-creator-action="image" data-card-id="${escapeAttr(card.id)}" data-side="term" aria-label="Add term image">
                <i class="fas fa-image"></i>
              </button>
            </div>
          </div>
          <div class="rich-editor" contenteditable="true" data-editor-id="${escapeAttr(card.id)}" data-side="term" data-placeholder="Enter term">${card.term || ''}</div>
          ${termImage}
        </section>
        <section class="editor-side">
          <div class="editor-side-head">
            <strong>Definition</strong>
            <div class="creator-toolbar">
              ${formatButton('bold', 'Bold', 'fa-bold')}
              ${formatButton('italic', 'Italic', 'fa-italic')}
              ${formatButton('underline', 'Underline', 'fa-underline')}
              <button type="button" class="format-button" data-creator-action="image" data-card-id="${escapeAttr(card.id)}" data-side="definition" aria-label="Add definition image">
                <i class="fas fa-image"></i>
              </button>
            </div>
          </div>
          <div class="rich-editor" contenteditable="true" data-editor-id="${escapeAttr(card.id)}" data-side="definition" data-placeholder="Enter definition">${card.definition || ''}</div>
          ${definitionImage}
        </section>
      </article>
    `;
  }

  function renderCreate() {
    if (!selectors.createClass) return;
    const current = state.creator.classId || '';
    selectors.createClass.innerHTML = [
      '<option value="">General</option>',
      ...state.classes.map(item => `<option value="${escapeAttr(item.id)}">${escapeHtml(item.name)}</option>`)
    ].join('');
    selectors.createClass.value = state.classes.some(item => String(item.id) === String(current)) ? current : '';

    ensureCreatorCard();
    if (selectors.creatorCards) {
      selectors.creatorCards.innerHTML = state.creator.cards.map((card, index) => cardEditor(card, index)).join('');
    }
  }

  function parseBulkCards(text) {
    return String(text || '')
      .split(/\r?\n+/)
      .map(line => line.trim())
      .filter(Boolean)
      .map(line => {
        const separator = line.includes(';') ? ';' : (line.includes('\t') ? '\t' : null);
        if (!separator) return null;
        const [term, ...rest] = line.split(separator);
        const definition = rest.join(separator).trim();
        if (!term.trim() || !definition) return null;
        return {
          ...emptyCreatorCard(),
          term: escapeHtml(term.trim()),
          definition: escapeHtml(definition)
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
    selectors.createClass.value = state.creator.classId;
    setActiveTab('create');
  }

  function hasCardContent(card) {
    return Boolean(
      plainTextFromHtml(card.term).trim()
      || plainTextFromHtml(card.definition).trim()
      || card.termImage
      || card.definitionImage
    );
  }

  async function saveMobileDeck() {
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
    await window.flashcardStore.saveSet({
      ...original,
      id: state.creator.editingSetId || original.id,
      name,
      classId: state.creator.classId || null,
      cards,
      srsSettings: schema?.normalizeSrsSettings ? schema.normalizeSrsSettings(original.srsSettings || {}) : (original.srsSettings || { enabled: true }),
      pinned: Boolean(original.pinned)
    });
    showToast(`Saved ${plural(cards.length, 'card')}`);
    state.browserLoaded = false;
    resetCreator();
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
    const saved = await window.flashcardStore.saveSet({
      ...data,
      id: null,
      name: data.name || data.title || fileName.replace(/\.json$/i, ''),
      classId: null
    });
    showToast(`Imported ${saved.name || 'deck'}`);
    state.browserLoaded = false;
    await refresh();
    setActiveTab('library');
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
    document.body.classList.remove('app-ready');
    document.body.classList.add('is-route-loading');
  }

  function hideAppLoader() {
    document.body.classList.add('app-ready');
    document.body.classList.remove('is-route-loading');
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
      srs: String(Boolean(reviewDue || srsMode))
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
    await window.flashcardStore.saveSet({ ...set, pinned: !set.pinned });
    playClick();
    await refresh();
  }

  async function deleteSet(setId) {
    const set = state.sets.find(item => String(item.id) === String(setId));
    if (!set) return;
    const ok = window.confirm(`Delete "${set.name || 'Untitled Set'}"? This cannot be undone.`);
    if (!ok) return;
    await window.flashcardStore.deleteSet(setId);
    showToast('Deck deleted');
    await refresh();
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
        showToast(`Restored ${result.setCount || 0} decks`);
        await refresh();
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
      const active = Boolean(activeEditor && command && document.queryCommandState(command));
      button.classList.toggle('active', active);
    });
  }

  async function handleCreatorAction(action, target) {
    switch (action) {
      case 'add-card': {
        syncCreatorFromDom();
        const card = emptyCreatorCard();
        state.creator.cards.push(card);
        renderCreate();
        requestAnimationFrame(() => {
          selectors.creatorCards?.querySelector(`[data-editor-id="${cssEscape(card.id)}"][data-side="term"]`)?.focus();
        });
        break;
      }
      case 'delete-card': {
        syncCreatorFromDom();
        state.creator.cards = state.creator.cards.filter(card => String(card.id) !== String(target.dataset.cardId));
        ensureCreatorCard();
        renderCreate();
        break;
      }
      case 'format': {
        const command = target.dataset.command;
        if (!command) break;
        document.execCommand(command, false, null);
        updateFormatState();
        break;
      }
      case 'image':
        state.pendingImageTarget = {
          cardId: target.dataset.cardId,
          side: target.dataset.side === 'definition' ? 'definition' : 'term'
        };
        selectors.imageInput?.click();
        break;
      case 'remove-image': {
        syncCreatorFromDom();
        const key = target.dataset.side === 'definition' ? 'definitionImage' : 'termImage';
        state.creator.cards = state.creator.cards.map(card => (
          String(card.id) === String(target.dataset.cardId) ? { ...card, [key]: '' } : card
        ));
        renderCreate();
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
      case 'tab-library':
        setActiveTab('library');
        break;
      case 'open-create':
        setActiveTab('create');
        break;
      case 'open-premade':
        setActiveTab('premade');
        await loadPremade();
        break;
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
      case 'study-set':
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
      default:
        break;
    }
  }

  function installEvents() {
    document.addEventListener('pointerdown', event => {
      if (event.target.closest('[data-creator-action="format"]')) {
        event.preventDefault();
      }
    });

    document.addEventListener('click', async event => {
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
        if (tab.dataset.tab === 'create' && state.activeTab !== 'create' && !state.creator.editingSetId) {
          ensureCreatorCard();
        }
        setActiveTab(tab.dataset.tab);
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

    selectors.createClass?.addEventListener('change', event => {
      state.creator.classId = event.target.value || '';
    });

    selectors.createForm?.addEventListener('submit', async event => {
      event.preventDefault();
      if (state.busy) return;
      state.busy = true;
      try {
        await saveMobileDeck();
      } finally {
        state.busy = false;
      }
    });

    selectors.imageInput?.addEventListener('change', async event => {
      const file = event.target.files?.[0];
      const target = state.pendingImageTarget;
      event.target.value = '';
      state.pendingImageTarget = null;
      if (!file || !target) return;
      syncCreatorFromDom();
      try {
        const src = await window.flashcardStore.saveImageFromFile(file, {
          deckId: state.creator.editingSetId || 'draft',
          side: target.side
        });
        const key = target.side === 'definition' ? 'definitionImage' : 'termImage';
        state.creator.cards = state.creator.cards.map(card => (
          String(card.id) === String(target.cardId) ? { ...card, [key]: src } : card
        ));
        renderCreate();
        showToast('Image added');
      } catch (error) {
        console.error(error);
        showToast('Could not add image');
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
        showToast(`Imported ${plural(imported.length, 'card')}`);
      } catch (error) {
        console.error(error);
        showToast('Could not import TXT');
      }
    });

    document.addEventListener('selectionchange', updateFormatState);

    document.addEventListener('visibilitychange', () => {
      if (!document.hidden && state.activeTab !== 'create') refresh();
    });
  }

  async function init() {
    document.documentElement.classList.add('is-capacitor', 'is-mobile-shell', 'mobile-app-shell');
    configureSystemBars().catch(() => {});
    installEvents();
    // Set tab first so the correct view is visible during data loading
    const initialTab = String(window.location.hash || '').replace('#', '');
    const tab = ['today', 'library', 'create', 'premade', 'browser', 'more'].includes(initialTab) ? initialTab : 'today';
    state.activeTab = tab;
    selectors.views.forEach(view => view.classList.toggle('active', view.id === `view-${tab}`));
    selectors.tabs.forEach(button => button.classList.toggle('active', button.dataset.tab === tab));
    setHeader();
    
    const startTime = Date.now();
    // Defer CPU-intensive database load to allow transition/loader animation to initialize smoothly
    setTimeout(async () => {
      await refresh();
      const elapsed = Date.now() - startTime;
      const delay = Math.max(0, 3000 - elapsed);
      setTimeout(hideAppLoader, delay);
    }, 150);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init, { once: true });
  } else {
    init();
  }
})();
