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
    busy: false
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
    studyActions: document.getElementById('study-actions'),
    studyDeckList: document.getElementById('study-deck-list'),
    srsSwitch: document.getElementById('srs-switch'),
    moreSrsLabel: document.getElementById('more-srs-label'),
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

  function clamp(number, min, max) {
    return Math.min(max, Math.max(min, number));
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

  function setStats(set) {
    if (statsCore?.getSetSrsStats) return statsCore.getSetSrsStats(set);
    const totalCards = Array.isArray(set?.cards) ? set.cards.length : 0;
    return { totalCards, dueCards: totalCards, newCards: totalCards, learningCards: 0, reviewCards: 0, matureCards: 0 };
  }

  function dueCardsForSet(set) {
    if (!state.srsMode) return [];
    if (set?.srsSettings?.enabled === false) return [];
    if (window.srsManager?.getDueCards) {
      return window.srsManager.getDueCards(set.cards || [], { settings: set.srsSettings || {} });
    }
    return (set.cards || []).filter(card => statsCore?.isDue ? statsCore.isDue(card.srs) : true);
  }

  function totalStats() {
    if (statsCore?.getLibraryStats) return statsCore.getLibraryStats(state.sets, state.classes);
    return {
      setCount: state.sets.length,
      classCount: state.classes.length,
      cardCount: state.sets.reduce((total, set) => total + (set.cards || []).length, 0),
      dueCards: state.sets.reduce((total, set) => total + dueCardsForSet(set).length, 0),
      retention: null
    };
  }

  function dueSets() {
    if (!state.srsMode) return [];
    return state.sets
      .map(set => ({ set, due: dueCardsForSet(set).length }))
      .filter(item => item.due > 0)
      .sort((a, b) => b.due - a.due || normalizeTimestamp(b.set.lastOpened || b.set.lastModified) - normalizeTimestamp(a.set.lastOpened || a.set.lastModified));
  }

  function reviewedDates() {
    const dates = [];
    state.sets.forEach(set => {
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
    const start = new Date();
    start.setHours(0, 0, 0, 0);
    return reviewedDates().filter(time => time >= start.getTime()).length;
  }

  function streakDays() {
    const dayKeys = new Set(reviewedDates().map(time => {
      const date = new Date(time);
      date.setHours(0, 0, 0, 0);
      return date.getTime();
    }));
    let streak = 0;
    const cursor = new Date();
    cursor.setHours(0, 0, 0, 0);
    while (dayKeys.has(cursor.getTime())) {
      streak += 1;
      cursor.setDate(cursor.getDate() - 1);
    }
    return streak;
  }

  function progressPercent(set) {
    const cards = set.cards || [];
    if (!cards.length) return 0;
    const touched = cards.filter(card => (card.srs?.reps || 0) > 0 || (card.reviewHistory || []).length > 0).length;
    return clamp(Math.round((touched / cards.length) * 100), 0, 100);
  }

  function playClick() {
    try {
      const audio = new Audio('assets/flashcard-assets/click.mp3');
      audio.volume = 0.22;
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
    await Promise.all([
      window.eruditeMobileReady?.catch?.(() => {}),
      window.flashcardLocalReady?.catch?.(() => {})
    ].filter(Boolean));
    if (!window.flashcardStore) {
      throw new Error('Flashcard store is not available.');
    }
  }

  async function loadData() {
    await waitForStorage();
    const [sets, classes, settings, srsMode] = await Promise.all([
      window.flashcardStore.listSets(),
      window.flashcardStore.listClasses(),
      window.flashcardStore.getSettings(),
      window.flashcardStore.getState('srsModeEnabled')
    ]);
    state.sets = (sets || []).map(set => schema?.normalizeSet ? schema.normalizeSet(set, null, { preserveLastModified: true }) : set);
    state.classes = (classes || []).map(item => schema?.normalizeClass ? schema.normalizeClass(item, null, { preserveLastModified: true }) : item);
    state.settings = settings || {};
    state.srsMode = srsMode === true || srsMode === 'true';
  }

  function setHeader() {
    const labels = {
      today: ['Today', 'Erudite'],
      library: ['Library', 'Flashcards'],
      study: ['Study', 'Review'],
      create: ['Create', 'New set'],
      more: ['More', 'Tools']
    };
    const [eyebrow, title] = labels[state.activeTab] || labels.today;
    selectors.eyebrow.textContent = eyebrow;
    selectors.title.textContent = title;
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
    const due = dueCardsForSet(set).length;
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
    const totals = totalStats();
    const due = dueSets();
    const todayReviews = reviewsToday();
    const streak = streakDays();
    const progress = totals.cardCount > 0 ? clamp(Math.round((todayReviews / Math.max(10, todayReviews + due.length)) * 100), 0, 100) : 0;
    const heroTitle = state.srsMode
      ? (totals.dueCards > 0 ? `${totals.dueCards} due today` : 'All clear today')
      : 'Ready when you are';
    const heroCopy = state.srsMode
      ? (totals.dueCards > 0 ? `Across ${plural(due.length, 'deck')}. Start with the highest workload first.` : 'No reviews are due. You can still study any deck normally.')
      : 'SRS is off. Study any deck normally or turn on SRS from More when you want scheduled reviews.';

    selectors.todayHero.innerHTML = `
      <div class="hero-grid">
        <div>
          <p class="mobile-eyebrow">${state.srsMode ? 'Review plan' : 'Study plan'}</p>
          <h2 class="hero-title">${escapeHtml(heroTitle)}</h2>
          <p class="hero-copy">${escapeHtml(heroCopy)}</p>
        </div>
        <div class="goal-ring" style="--progress:${progress * 3.6}deg">
          <div><strong>${progress}%</strong><span>Today</span></div>
        </div>
      </div>
      <div class="hero-metrics">
        <div class="metric-pill"><strong>${state.srsMode ? totals.dueCards : totals.setCount}</strong><span>${state.srsMode ? 'Due cards' : 'Decks'}</span></div>
        <div class="metric-pill"><strong>${todayReviews}</strong><span>Reviewed</span></div>
        <div class="metric-pill"><strong>${streak}</strong><span>Day streak</span></div>
      </div>
      <div class="hero-actions">
        ${state.srsMode && due.length ? `
          <button type="button" class="primary-action" data-action="review-due">
            <i class="fas fa-brain"></i>
            Review Now
          </button>
        ` : `
          <button type="button" class="primary-action" data-action="tab-library">
            <i class="fas fa-layer-group"></i>
            Open Library
          </button>
        `}
        <button type="button" class="secondary-action" data-action="open-create">
          <i class="fas fa-plus"></i>
          New
        </button>
      </div>
    `;

    const continueSets = [...state.sets]
      .sort((a, b) => {
        const dueDiff = dueCardsForSet(b).length - dueCardsForSet(a).length;
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
          copy: plural((set.cards || []).length, 'card')
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
      if (state.sort === 'cards') return (b.cards || []).length - (a.cards || []).length;
      if (state.sort === 'due') return dueCardsForSet(b).length - dueCardsForSet(a).length;
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
      const due = state.srsMode ? sets.reduce((total, set) => total + dueCardsForSet(set).length, 0) : 0;
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

  function renderStudy() {
    const due = dueSets();
    selectors.studyActions.innerHTML = `
      <div class="study-action-grid">
        ${state.srsMode && due.length ? `
          <button type="button" class="primary-action" data-action="review-due">
            <i class="fas fa-brain"></i>
            Review ${due.reduce((total, item) => total + item.due, 0)} Due Cards
          </button>
        ` : `
          <button type="button" class="primary-action" data-action="tab-library">
            <i class="fas fa-play"></i>
            Pick a Deck
          </button>
        `}
        <button type="button" class="secondary-action" data-action="toggle-srs">
          <i class="fas fa-brain"></i>
          ${state.srsMode ? 'Turn SRS Off' : 'Turn SRS On'}
        </button>
      </div>
    `;

    const sets = [...state.sets]
      .sort((a, b) => dueCardsForSet(b).length - dueCardsForSet(a).length || normalizeTimestamp(b.lastOpened || b.lastModified) - normalizeTimestamp(a.lastOpened || a.lastModified))
      .slice(0, 8);
    selectors.studyDeckList.innerHTML = sets.length
      ? sets.map(set => deckRow(set, { compact: true })).join('')
      : emptyPanel('fa-play', 'Nothing to study yet', 'Create a deck first, then your study sessions will appear here.');
  }

  function renderMore() {
    selectors.srsSwitch?.classList.toggle('on', state.srsMode);
    selectors.moreSrsLabel.textContent = state.srsMode ? 'On - due reviews are scheduled' : 'Off - normal study only';
  }

  function render() {
    renderToday();
    renderLibrary();
    renderStudy();
    renderMore();
  }

  async function refresh() {
    try {
      await loadData();
      render();
    } catch (error) {
      console.error(error);
      selectors.todayHero.innerHTML = emptyPanel('fa-triangle-exclamation', 'Could not load library', error.message || 'Storage failed to open.');
      showToast('Storage error');
    }
  }

  function navigateTo(url) {
    window.location.href = url;
  }

  function mobileStudyUrl(setId, reviewDue = false) {
    const suffix = reviewDue ? '&reviewDue=true' : '';
    return `mobile/study.html?setId=${encodeURIComponent(setId)}${suffix}`;
  }

  async function toggleSrs() {
    state.srsMode = !state.srsMode;
    await window.flashcardStore.setState('srsModeEnabled', state.srsMode);
    localStorage.setItem('srsModeEnabled', String(state.srsMode));
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

  function reviewDue() {
    const first = dueSets()[0]?.set;
    if (!first) {
      showToast('No reviews due');
      return;
    }
    navigateTo(mobileStudyUrl(first.id, true));
  }

  async function handleAction(action, target) {
    switch (action) {
      case 'tab-library':
        setActiveTab('library');
        break;
      case 'open-create':
        navigateTo('creator.html');
        break;
      case 'open-premade':
        navigateTo('premade-library.html');
        break;
      case 'open-browser':
        navigateTo('card-browser.html');
        break;
      case 'open-desktop-library':
        navigateTo('index.html#library');
        break;
      case 'open-backup':
        setActiveTab('more');
        break;
      case 'open-settings':
        setActiveTab('more');
        break;
      case 'review-due':
        reviewDue();
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
        navigateTo(mobileStudyUrl(target.dataset.setId || ''));
        break;
      case 'edit-set':
        navigateTo(`creator.html?setId=${encodeURIComponent(target.dataset.setId || '')}`);
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
    document.addEventListener('click', async event => {
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

    document.addEventListener('visibilitychange', () => {
      if (!document.hidden) refresh();
    });
  }

  async function init() {
    document.documentElement.classList.add('is-capacitor', 'is-mobile-shell', 'mobile-app-shell');
    await configureSystemBars();
    installEvents();
    await refresh();
    const initialTab = String(window.location.hash || '').replace('#', '');
    setActiveTab(['today', 'library', 'study', 'create', 'more'].includes(initialTab) ? initialTab : 'today');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init, { once: true });
  } else {
    init();
  }
})();
