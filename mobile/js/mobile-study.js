(function () {
  const schema = window.EruditeCore?.schema;
  const statsCore = window.EruditeCore?.stats;

  const params = new URLSearchParams(window.location.search);
  const reviewDueSession = params.get('reviewDue') === 'true';

  const state = {
    set: null,
    allSets: [],
    srsMode: false,
    activeCards: [],
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
    }
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
    card: document.getElementById('study-card'),
    stage: document.getElementById('card-stage'),
    termText: document.getElementById('term-text'),
    definitionText: document.getElementById('definition-text'),
    termImage: document.getElementById('term-image'),
    definitionImage: document.getElementById('definition-image'),
    termImageWrap: document.getElementById('term-image-wrap'),
    definitionImageWrap: document.getElementById('definition-image-wrap'),
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
    toast: document.getElementById('study-toast')
  };

  const intervals = {
    Again: document.getElementById('interval-again'),
    Hard: document.getElementById('interval-hard'),
    Good: document.getElementById('interval-good'),
    Easy: document.getElementById('interval-easy')
  };

  let toastTimer = null;
  let pointer = null;
  let gestureLock = false;

  function showToast(message) {
    clearTimeout(toastTimer);
    els.toast.textContent = message;
    els.toast.classList.add('show');
    toastTimer = setTimeout(() => els.toast.classList.remove('show'), 1800);
  }

  function libraryUrl() {
    return '../index.html#library';
  }

  function studyUrl(setId, reviewDue = false) {
    const suffix = reviewDue ? '&reviewDue=true' : '';
    return `study.html?setId=${encodeURIComponent(setId)}${suffix}`;
  }

  function goLibrary() {
    window.location.href = libraryUrl();
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

  function setActiveIndex(value) {
    const max = Math.max(0, state.activeCards.length - 1);
    const next = Math.min(max, Math.max(0, Number(value) || 0));
    if (state.srsMode) state.srsIndex = next;
    else state.normalIndex = next;
  }

  function activeCard() {
    return state.activeCards[activeIndex()] || null;
  }

  function setFlipped(flipped, options = {}) {
    state.flipped = Boolean(flipped);
    if (options.noTransition) els.card.classList.add('no-transition');
    els.card.classList.toggle('is-flipped', state.flipped);
    updateRatingVisibility();
    if (options.noTransition) {
      void els.card.offsetWidth;
      els.card.classList.remove('no-transition');
    }
  }

  function isScrollableContent(target) {
    const scroll = target.closest?.('.card-scroll');
    return scroll && scroll.scrollHeight > scroll.clientHeight + 4 ? scroll : null;
  }

  function isInteractive(target) {
    return Boolean(target.closest?.('button, a, input, textarea, select, [contenteditable="true"], .modal:not(.hidden), .image-modal:not(.hidden)'));
  }

  function configureSystemBars() {
    const SystemBars = window.Capacitor?.Plugins?.SystemBars;
    if (!SystemBars) return;
    SystemBars.setStyle?.({ style: 'DARK' }).catch(() => {});
    SystemBars.show?.().catch(() => {});
  }

  async function waitForStore() {
    await Promise.all([
      window.eruditeMobileReady?.catch?.(() => {}),
      window.flashcardLocalReady?.catch?.(() => {})
    ].filter(Boolean));
    if (!window.flashcardStore) throw new Error('Flashcard store unavailable');
  }

  async function loadData() {
    await waitForStore();
    const setId = getSetId();
    if (setId === null || setId === undefined) {
      throw new Error('No set selected');
    }

    const [sets, srsMode] = await Promise.all([
      window.flashcardStore.listSets(),
      window.flashcardStore.getState('srsModeEnabled')
    ]);
    state.allSets = Array.isArray(sets) ? sets : [];
    const found = state.allSets.find(set => String(set.id) === String(setId));
    if (!found) throw new Error('Flashcard set not found');

    state.srsMode = srsMode === true || srsMode === 'true';
    state.set = schema?.normalizeSet ? schema.normalizeSet({
      ...found,
      openedCount: (found.openedCount || 0) + 1,
      lastOpened: Date.now()
    }, found) : {
      ...found,
      openedCount: (found.openedCount || 0) + 1,
      lastOpened: Date.now()
    };
    state.set = await window.flashcardStore.saveSet(state.set);

    await loadProgress();
    prepareActiveCards();
  }

  async function loadProgress() {
    const saved = await window.flashcardStore.getProgress(state.set.id);
    if (!saved || String(saved.setId) !== String(state.set.id)) return;
    const cardCount = state.set.cards?.length || 0;
    state.normalIndex = Math.min(Math.max(0, Number(saved.normalModeIndex ?? saved.cardIndex ?? 0) || 0), Math.max(0, cardCount - 1));
    state.srsIndex = Math.max(0, Number(saved.srsModeIndex ?? 0) || 0);
  }

  async function saveProgress() {
    if (!state.set) return;
    await window.flashcardStore.saveProgress(state.set.id, {
      setId: state.set.id,
      cardIndex: activeIndex(),
      normalModeIndex: state.normalIndex,
      srsModeIndex: state.srsIndex,
      srsModeLength: state.activeCards.length,
      srsCurrentCardKey: state.srsMode ? cardKey(activeCard()) : null,
      timestamp: Date.now()
    });
  }

  function prepareActiveCards() {
    if (!Array.isArray(state.set.cards)) state.set.cards = [];
    if (state.srsMode && window.srsManager?.isReady?.()) {
      state.set.cards = state.set.cards.map(card => card.srs ? card : window.srsManager.createSRSCard(card));
      const settings = getDeckSrsSettings();
      state.activeCards = window.srsManager.getDueCards(state.set.cards, {
        maxNewCards: settings.newCardsPerDay,
        maxDueCards: settings.reviewsPerDay,
        allowMultipleSessions: true,
        settings
      });
      state.srsIndex = Math.min(state.srsIndex, Math.max(0, state.activeCards.length - 1));
      return;
    }
    state.activeCards = state.set.cards || [];
    state.normalIndex = Math.min(state.normalIndex, Math.max(0, state.activeCards.length - 1));
  }

  function renderImage(img, wrap, src) {
    if (!src) {
      wrap.classList.add('hidden');
      img.removeAttribute('src');
      return;
    }
    img.src = src;
    wrap.classList.remove('hidden');
  }

  function preloadNeighborImages() {
    [state.activeCards[activeIndex() + 1], state.activeCards[activeIndex() - 1]].forEach(card => {
      [card?.termImage, card?.definitionImage].filter(Boolean).forEach(src => {
        const img = new Image();
        img.src = src;
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
    if (visible) updateRatingIntervals();
    els.hint.textContent = state.srsMode
      ? (state.flipped ? 'Choose how well you remembered it.' : 'Tap to reveal the answer.')
      : 'Tap to flip. Swipe sideways to move cards.';
  }

  function renderCard(options = {}) {
    const card = activeCard();
    if (!card) return;

    els.termText.innerHTML = sanitizeRichText(card.term);
    els.definitionText.innerHTML = sanitizeRichText(card.definition);
    renderImage(els.termImage, els.termImageWrap, card.termImage);
    renderImage(els.definitionImage, els.definitionImageWrap, card.definitionImage);
    els.card.style.setProperty('--drag-x', '0px');
    els.card.style.setProperty('--drag-y', '0px');
    els.card.style.setProperty('--drag-rotate', '0deg');
    setFlipped(false, { noTransition: options.noTransition !== false });
    els.card.querySelectorAll('.card-scroll').forEach(scroll => {
      scroll.scrollTop = 0;
    });
    preloadNeighborImages();
    updateProgress();
  }

  function updateProgress() {
    const total = state.activeCards.length;
    const index = total ? activeIndex() + 1 : 0;
    els.current.textContent = String(index);
    els.total.textContent = String(total);
    els.fill.style.width = total ? `${Math.round((index / total) * 100)}%` : '0%';
    els.modeLabel.textContent = state.srsMode ? 'SRS Review' : 'Study';
    els.title.textContent = state.set?.name || 'Study';
  }

  async function navigate(direction) {
    if (!state.activeCards.length || state.complete) return;
    if (state.srsMode) {
      if (!state.flipped) {
        setFlipped(true);
      } else {
        showToast('Rate this card to continue');
      }
      return;
    }

    const nextIndex = activeIndex() + (direction === 'next' ? 1 : -1);
    if (nextIndex < 0) {
      showToast('First card');
      return;
    }
    if (nextIndex >= state.activeCards.length) {
      await showCompletion();
      return;
    }
    animateOut(direction, () => {
      setActiveIndex(nextIndex);
      renderCard();
      saveProgress();
    });
  }

  function animateOut(direction, done) {
    const sign = direction === 'next' ? -1 : 1;
    els.card.classList.add('animating-out');
    els.card.style.setProperty('--drag-x', `${sign * 105}vw`);
    els.card.style.setProperty('--drag-y', '-0.35rem');
    els.card.style.setProperty('--drag-rotate', `${sign * -8}deg`);
    window.setTimeout(() => {
      els.card.classList.remove('animating-out');
      done();
    }, 210);
  }

  function flipCard() {
    if (!activeCard() || state.complete) return;
    setFlipped(!state.flipped);
  }

  async function handleRating(rating) {
    if (!state.srsMode || !state.flipped || state.complete || !window.srsManager?.isReady?.()) return;
    const current = activeCard();
    if (!current) return;

    const previous = current.srs ? { ...current.srs } : null;
    const reviewedAt = new Date().toISOString();
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
    state.activeCards[state.srsIndex] = updatedCard;
    state.set = await window.flashcardStore.saveSet(state.set);

    state.sessionStats.reviewed += 1;
    state.sessionStats[rating] += 1;
    state.sessionStats.nextDue = updatedCard.srs?.due || state.sessionStats.nextDue;

    state.srsIndex += 1;
    await saveProgress();

    if (state.srsIndex >= state.activeCards.length) {
      await showCompletion();
      return;
    }

    animateOut('next', () => {
      renderCard();
      saveProgress();
    });
  }

  async function findNextDueSetId() {
    if (!reviewDueSession || !state.srsMode || !window.srsManager?.isReady?.()) return null;
    for (const set of state.allSets || []) {
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
    els.card.addEventListener('pointerdown', event => {
      if (isInteractive(event.target) || gestureLock) return;
      pointer = {
        id: event.pointerId,
        x: event.clientX,
        y: event.clientY,
        lastX: event.clientX,
        lastY: event.clientY,
        time: performance.now(),
        horizontal: false,
        verticalScroll: false,
        scrollable: isScrollableContent(event.target)
      };
    });

    els.card.addEventListener('pointermove', event => {
      if (!pointer || pointer.id !== event.pointerId) return;
      const dx = event.clientX - pointer.x;
      const dy = event.clientY - pointer.y;
      pointer.lastX = event.clientX;
      pointer.lastY = event.clientY;

      if (!pointer.horizontal && !pointer.verticalScroll) {
        if (Math.abs(dy) > 12 && Math.abs(dy) > Math.abs(dx) && pointer.scrollable) {
          pointer.verticalScroll = true;
          return;
        }
        if (Math.abs(dx) > 12 && Math.abs(dx) > Math.abs(dy)) {
          pointer.horizontal = true;
          els.card.setPointerCapture?.(event.pointerId);
        }
      }

      if (pointer.horizontal) {
        event.preventDefault();
        const limitedX = Math.max(-90, Math.min(90, dx));
        els.card.style.setProperty('--drag-x', `${limitedX}px`);
        els.card.style.setProperty('--drag-y', `${Math.max(-10, Math.min(10, dy * 0.15))}px`);
        els.card.style.setProperty('--drag-rotate', `${limitedX * 0.045}deg`);
      }
    }, { passive: false });

    function finishPointer(event) {
      if (!pointer || pointer.id !== event.pointerId) return;
      const dx = event.clientX - pointer.x;
      const dy = event.clientY - pointer.y;
      const dt = Math.max(1, performance.now() - pointer.time);
      const velocity = Math.abs(dx) / dt;
      const wasHorizontal = pointer.horizontal && Math.abs(dx) > 48 && Math.abs(dx) > Math.abs(dy);
      const wasTap = Math.abs(dx) < 9 && Math.abs(dy) < 9 && !pointer.verticalScroll;
      pointer = null;

      els.card.style.setProperty('--drag-x', '0px');
      els.card.style.setProperty('--drag-y', '0px');
      els.card.style.setProperty('--drag-rotate', '0deg');

      if (wasHorizontal || velocity > 0.45) {
        navigate(dx < 0 ? 'next' : 'prev');
        return;
      }

      if (wasTap) {
        flipCard();
      }
    }

    els.card.addEventListener('pointerup', finishPointer);
    els.card.addEventListener('pointercancel', event => {
      if (!pointer || pointer.id !== event.pointerId) return;
      pointer = null;
      els.card.style.setProperty('--drag-x', '0px');
      els.card.style.setProperty('--drag-y', '0px');
      els.card.style.setProperty('--drag-rotate', '0deg');
    });
  }

  function installEvents() {
    els.back.addEventListener('click', goLibrary);
    els.libraryButton.addEventListener('click', goLibrary);
    els.emptyLibraryButton.addEventListener('click', goLibrary);
    els.continueButton.addEventListener('click', async () => {
      if (state.srsMode && state.nextDueSetId) {
        window.location.href = studyUrl(state.nextDueSetId, true);
        return;
      }
      els.completionModal.classList.add('hidden');
      state.complete = false;
      state.nextDueSetId = null;
      if (state.srsMode) {
        state.srsIndex = 0;
        prepareActiveCards();
        if (!state.activeCards.length) {
          showEmptyDue();
          return;
        }
      } else {
        state.normalIndex = 0;
        state.activeCards = state.set.cards || [];
      }
      renderCard();
      await saveProgress();
    });

    els.emptyCheckButton.addEventListener('click', async () => {
      els.emptyModal.classList.add('hidden');
      await loadData();
      if (!state.activeCards.length) showEmptyDue();
      else renderCard();
    });

    els.ratingDock.addEventListener('click', event => {
      const button = event.target.closest('[data-rating]');
      if (!button) return;
      handleRating(button.dataset.rating);
    });

    document.addEventListener('click', event => {
      const zoom = event.target.closest('[data-image-side]');
      if (!zoom) return;
      const side = zoom.dataset.imageSide;
      const src = side === 'term' ? els.termImage.src : els.definitionImage.src;
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
        navigate('prev');
      } else if (event.key === 'ArrowRight') {
        event.preventDefault();
        navigate('next');
      } else if (state.srsMode && state.flipped && ['1', '2', '3', '4'].includes(event.key)) {
        event.preventDefault();
        handleRating(['Again', 'Hard', 'Good', 'Easy'][Number(event.key) - 1]);
      }
    });

    document.addEventListener('visibilitychange', () => {
      if (document.hidden) saveProgress();
    });
  }

  async function init() {
    document.documentElement.classList.add('is-capacitor', 'is-mobile-shell');
    configureSystemBars();
    installEvents();
    installPointerGestures();
    try {
      await loadData();
      updateProgress();
      if (!state.activeCards.length) {
        showEmptyDue();
      } else {
        renderCard({ noTransition: true });
      }
    } catch (error) {
      console.error(error);
      showToast(error.message || 'Could not open study session');
      window.setTimeout(goLibrary, 900);
    } finally {
      requestAnimationFrame(() => els.shell.classList.remove('is-loading'));
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init, { once: true });
  } else {
    init();
  }
})();
