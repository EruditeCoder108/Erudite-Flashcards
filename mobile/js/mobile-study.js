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

  const intervals = {
    Again: document.getElementById('interval-again'),
    Hard: document.getElementById('interval-hard'),
    Good: document.getElementById('interval-good'),
    Easy: document.getElementById('interval-easy')
  };

  let toastTimer = null;
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
  const preloadedImages = new Set();
  const SWIPE_DURATION = 175;
  const FLIP_DURATION = 420;

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
    const query = new URLSearchParams({
      setId: String(setId),
      srs: String(Boolean(reviewDue || state.srsMode))
    });
    if (reviewDue) query.set('reviewDue', 'true');
    return `study.html?${query.toString()}`;
  }

  function showStudyLoader(title = 'Opening Study', copy = 'Preparing your cards') {
    if (els.loadingTitle) els.loadingTitle.textContent = title;
    if (els.loadingCopy) els.loadingCopy.textContent = copy;
    document.body.classList.remove('study-ready');
    document.body.classList.add('is-route-loading');
  }

  function hideStudyLoader() {
    document.body.classList.add('study-ready');
    document.body.classList.remove('is-route-loading');
  }

  function navigateAway(url, title, copy) {
    showStudyLoader(title, copy);
    requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        window.location.href = url;
      });
    });
  }

  async function goLibrary() {
    try { saveProgress(); } catch (_) {}
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
    return Boolean(target.closest?.('button, a, input, textarea, select, [contenteditable="true"], .modal:not(.hidden), .image-modal:not(.hidden)'));
  }

  function configureSystemBars() {
    const SystemBars = window.Capacitor?.Plugins?.SystemBars;
    if (!SystemBars) return;
    SystemBars.setStyle?.({ style: 'DARK' }).catch(() => {});
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

    const [found, srsMode] = await Promise.all([
      window.flashcardStore.getSet(setId),
      window.flashcardStore.getState('srsModeEnabled')
    ]);
    if (!found) throw new Error('Flashcard set not found');

    state.srsMode = resolveSrsMode(srsMode);
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
  }

  function scheduleOpenedSave() {
    if (!state.set) return;
    clearTimeout(openedSaveTimer);
    const { id, openedCount, lastOpened } = state.set;
    openedSaveTimer = window.setTimeout(() => {
      window.flashcardStore.saveSet({
        id,
        openedCount,
        lastOpened,
        __metaOnly: true
      }).catch(error => console.warn('[mobile-study] opened metadata save failed:', error));
    }, 210);
  }

  async function loadProgress() {
    const saved = await window.flashcardStore.getProgress(state.set.id);
    const mirrored = readProgressMirror();
    const progress = mirrored && (!saved || Number(mirrored.timestamp || 0) >= Number(saved.timestamp || 0))
      ? mirrored
      : saved;
    if (!progress || String(progress.setId) !== String(state.set.id)) return;
    const cardCount = state.set.cards?.length || 0;
    state.normalIndex = Math.min(Math.max(0, Number(progress.normalModeIndex ?? progress.cardIndex ?? 0) || 0), Math.max(0, cardCount - 1));
    state.srsIndex = Math.max(0, Number(progress.srsModeIndex ?? 0) || 0);
  }

  function progressMirrorKey() {
    return state.set ? `${PROGRESS_MIRROR_PREFIX}${state.set.id}` : '';
  }

  function buildProgressPayload() {
    if (!state.set) return null;
    return {
      setId: state.set.id,
      cardIndex: activeIndex(),
      normalModeIndex: state.normalIndex,
      srsModeIndex: state.srsIndex,
      srsModeLength: state.activeCards.length,
      srsCurrentCardKey: state.srsMode ? cardKey(activeCard()) : null,
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
    const payload = buildProgressPayload();
    if (!payload) return Promise.resolve(false);
    writeProgressMirror(payload);
    clearTimeout(progressSaveTimer);
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
    clearTimeout(cardProgressSaveTimer);
    cardProgressSaveTimer = window.setTimeout(() => {
      const saveCard = window.flashcardStore.saveCardProgress || window.eruditeMobileFlashcards?.saveCardProgress;
      if (typeof saveCard === 'function') {
        saveCard(state.set.id, card.id, {
          srs: card.srs || null,
          reviewHistory: Array.isArray(card.reviewHistory) ? card.reviewHistory : [],
          suspended: Boolean(card.suspended),
          buriedUntil: card.buriedUntil || null,
          lastModified: Date.now()
        }).catch(() => {});
      }
    }, delay);
  }

  function prepareActiveCards() {
    if (!Array.isArray(state.set.cards)) state.set.cards = [];
    if (state.srsMode && window.srsManager?.isReady?.()) {
      const settings = getDeckSrsSettings();
      state.activeCards = window.srsManager.getDueCards(state.set.cards, {
        maxNewCards: settings.newCardsPerDay,
        maxDueCards: settings.reviewsPerDay,
        allowMultipleSessions: true,
        settings
      });
      state.srsIndex = Math.min(state.srsIndex, Math.max(0, state.activeCards.length - 1));
    } else {
      state.activeCards = state.set.cards || [];
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

  function preloadNeighborImages() {
    [state.activeCards[activeIndex() + 1], state.activeCards[activeIndex() - 1]].forEach(card => {
      [card?.termImage, card?.definitionImage].filter(Boolean).forEach(src => {
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
    if (visible) updateRatingIntervals();
    els.hint.textContent = state.srsMode
      ? (state.flipped ? 'Choose how well you remembered it.' : 'Tap to reveal the answer.')
      : 'Tap to flip. Swipe left or right to go next.';
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
    renderImage(elements.termImage, elements.termImageWrap, cardData.termImage);
    renderImage(elements.definitionImage, elements.definitionImageWrap, cardData.definitionImage);
    
    cardEl.querySelectorAll('.card-scroll').forEach(scroll => {
      scroll.scrollTop = 0;
    });

    setCardFlipped(cardEl, false, { noTransition: true });
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
    
    updateRoles();
    preloadNeighborImages();
    updateProgress();
  }

  function applyActiveDrag(x = 0) {
    const activeEl = cards[activeCardIndex];
    const nextEl = cards[nextCardIndex];
    if (!activeEl) return;
    
    const rotate = Math.max(-7, Math.min(7, x * 0.032));
    activeEl.style.transform = `translate3d(${x}px, 0px, 0) rotate(${rotate}deg)`;
    
    if (nextEl && !nextEl.classList.contains('empty-card')) {
      const progress = Math.min(1, Math.abs(x) / 50);
      const nextScale = 0.96 + (0.04 * progress);
      const nextOffset = 10 - (10 * progress);
      nextEl.style.transform = `translate3d(0, ${nextOffset}px, 0) scale(${nextScale})`;
      nextEl.style.opacity = 0.9 + (0.1 * progress);
    }
  }

  function setDrag(x = 0) {
    queuedDrag = { x };
    if (dragFrame) return;
    dragFrame = requestAnimationFrame(() => {
      dragFrame = 0;
      const next = queuedDrag || { x: 0 };
      queuedDrag = null;
      applyActiveDrag(next.x);
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
      activeEl.style.transform = `translate3d(${vx * 118}vw, 0px, 0) rotate(${vx * 8}deg)`;
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

  async function handleRating(rating) {
    if (ratingInFlight || animating || !state.srsMode || !state.flipped || state.complete || !window.srsManager?.isReady?.()) return;
    const current = activeCard();
    if (!current) return;
    ratingInFlight = true;

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

    state.sessionStats.reviewed += 1;
    state.sessionStats[rating] += 1;
    state.sessionStats.nextDue = updatedCard.srs?.due || state.sessionStats.nextDue;

    state.srsIndex += 1;
    saveProgress();
    scheduleCardProgressSave(updatedCard);

    if (state.srsIndex >= state.activeCards.length) {
      await showCompletion();
      ratingInFlight = false;
      return;
    }

    animateOut({ x: -1, y: 0 }, () => {
      prevCardIndex = activeCardIndex;
      activeCardIndex = nextCardIndex;
      nextCardIndex = (nextCardIndex + 1) % 3;
      
      const currentIdx = activeIndex();
      populateCardElement(cards[nextCardIndex], state.activeCards[currentIdx + 1]);
      
      updateRoles();
      preloadNeighborImages();
      updateProgress();
      saveProgress();
      animating = false;
      ratingInFlight = false;
    });
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
    const DRAG_LIMIT = 104;
    const HORIZONTAL_BIAS = 1.12;

    els.stage.addEventListener('pointerdown', event => {
      if (animating) {
        if (!isInteractive(event.target)) queueNavigation({ x: -1, y: 0 });
        return;
      }
      const activeCardEl = cards[activeCardIndex];
      if (!activeCardEl || !activeCardEl.contains(event.target)) return;
      if (isInteractive(event.target)) return;
      
      pointer = {
        id: event.pointerId,
        x: event.clientX,
        y: event.clientY,
        time: performance.now(),
        dragging: false,
        scrolling: false,
        scrollable: isScrollableContent(event.target)
      };
      
      activeCardEl.classList.add('dragging');
    });

    els.stage.addEventListener('pointermove', event => {
      if (!pointer || pointer.id !== event.pointerId) return;
      const activeCardEl = cards[activeCardIndex];
      if (!activeCardEl) return;
      
      const dx = event.clientX - pointer.x;
      const dy = event.clientY - pointer.y;
      const absDx = Math.abs(dx);
      const absDy = Math.abs(dy);

      if (!pointer.dragging && !pointer.scrolling) {
        if (absDy > DEAD_ZONE && absDy > absDx * 1.18 && pointer.scrollable) {
          pointer.scrolling = true;
          activeCardEl.classList.remove('dragging');
          return;
        }
        if (absDx > DEAD_ZONE && absDx > absDy * HORIZONTAL_BIAS) {
          pointer.dragging = true;
          els.stage.setPointerCapture?.(event.pointerId);
        } else if (absDy > DEAD_ZONE && absDy >= absDx) {
          pointer.scrolling = Boolean(pointer.scrollable);
          if (pointer.scrolling) {
            activeCardEl.classList.remove('dragging');
          }
          return;
        }
      }

      if (pointer.scrolling) return;

      if (pointer.dragging) {
        event.preventDefault();
        setDrag(Math.sign(dx) * Math.min(absDx, DRAG_LIMIT));
      }
    }, { passive: false });

    function finishPointer(event) {
      if (!pointer || pointer.id !== event.pointerId) return;
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
      const velocity = absDx / dt;
      const wasTap = absDx < 9 && absDy < 9 && !pointer.scrolling;
      const wasSwipe = !pointer.scrolling
        && absDx > absDy * HORIZONTAL_BIAS
        && (absDx >= SWIPE_THRESHOLD || velocity >= VELOCITY_THRESHOLD)
        && !wasTap;
      
      pointer = null;

      if (wasSwipe) {
        navigateForward({ x: dx < 0 ? -1 : 1, y: 0 });
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

  function installEvents() {
    els.back.addEventListener('click', () => goLibrary());
    els.prev?.addEventListener('click', () => navigateBack());
    els.libraryButton.addEventListener('click', () => goLibrary());
    els.emptyLibraryButton.addEventListener('click', () => goLibrary());
    els.continueButton.addEventListener('click', async () => {
      if (state.srsMode && state.nextDueSetId) {
        navigateAway(studyUrl(state.nextDueSetId, true), 'Opening Review', 'Loading the next due deck');
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
      renderStack();
      await saveProgress();
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

    document.addEventListener('click', event => {
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
        try { await saveProgress({ immediate: true }); } catch (_) {}
        try { await window.eruditeMobileFlashcards?.flush?.(); } catch (_) {}
      }
    });
  }

  async function init() {
    document.documentElement.classList.add('is-capacitor', 'is-mobile-shell', 'study-session-active');
    configureSystemBars();
    installEvents();
    installPointerGestures();
    
    const startTime = Date.now();
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
        const elapsed = Date.now() - startTime;
        const delay = Math.max(0, 3000 - elapsed);
        setTimeout(() => {
          requestAnimationFrame(() => {
            els.shell.classList.remove('is-loading');
            hideStudyLoader();
          });
        }, delay);
      }
    }, 150);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init, { once: true });
  } else {
    init();
  }
})();
