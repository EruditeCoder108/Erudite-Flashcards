document.addEventListener('DOMContentLoaded', async () => {
    if (window.flashcardLocalReady) await window.flashcardLocalReady;
    // Apply theme settings first to prevent flash of unstyled content
    applyThemeSettings();
    
    // DOM Elements
    const studyContainer = document.querySelector('.study-container');
    const studyArea = document.querySelector('.study-area');
    const cardContainer = document.querySelector('.card-container');
    const flashcardContainer = document.querySelector('.flashcard');
    const flashcardInner = document.querySelector('.flashcard-inner');
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');
    const progressDisplay = document.getElementById('progress');
    const progressFill = document.querySelector('.progress-fill');
    const completionScreen = document.getElementById('completion-screen');
    const closeCompletionBtn = document.getElementById('close-completion-btn');
    const practiceAgainBtn = document.getElementById('practice-again-btn');
    const goHomeBtn = document.getElementById('go-home-btn');
    const setNameDisplay = document.getElementById('set-name-display');
    const imageModal = document.getElementById('image-modal');
    const zoomedImage = document.getElementById('zoomed-image');
    const closeImageBtn = document.getElementById('close-image-btn');
    const termImage = document.querySelector('.term-image');
    const definitionImage = document.querySelector('.definition-image');
    const backBtn = document.querySelector('.back-btn');

    function isMobileRuntime() {
        return Boolean(window.Capacitor) || document.documentElement.classList.contains('is-capacitor');
    }

    function libraryUrl(isPremade = false) {
        if (!isMobileRuntime()) {
            return isPremade ? 'premade-library.html' : 'flashcards.html';
        }
        return 'index.html#library';
    }

    function studyUrl(setId, reviewDue = false) {
        const suffix = reviewDue ? '&reviewDue=true' : '';
        if (!isMobileRuntime()) {
            return `study.html?setId=${encodeURIComponent(setId)}${suffix}`;
        }
        return `mobile/study.html?setId=${encodeURIComponent(setId)}${suffix}`;
    }

    function goToLibrary(isPremade = false) {
        window.location.href = libraryUrl(isPremade);
    }

    // Create audio elements for sound effects
    const successSound = new Audio('assets/audio/success.mp3');
    successSound.volume = 0.6;

    const flipSound = new Audio('assets/flashcard-assets/flip-sound.mp3');
    flipSound.volume = 0.6;

    const nextCardSound = new Audio('assets/flashcard-assets/Next-card.mp3');
    nextCardSound.volume = 0.6;

    let currentCardIndex = 0;
    let flashcardSet = null;
    const STORAGE_KEY = 'currentStudyProgress';
    let isFlipping = false;
    
    // SRS State
    const pageParams = new URLSearchParams(window.location.search);
    const reviewDueSession = pageParams.get('reviewDue') === 'true';
    let srsModeEnabled = false;
    let srsCards = [];
    let srsReviewedCardIds = new Set();
    let isCardFlipped = false;
    let srsSessionComplete = false;
    let srsSessionStats = { reviewed: 0, Again: 0, Hard: 0, Good: 0, Easy: 0, nextDue: null };
    let pointerStart = null;
    let touchStart = null;
    let lastSwipeAt = 0;
    let suppressNextClick = false;
    let srsCurrentCardKey = null;
    let hasRenderedInitialCard = false;
    const FLIP_LOCK_MS = 380;
    const SWIPE_DISTANCE_THRESHOLD = 50;
    const SWIPE_VELOCITY_THRESHOLD = 0.45;

    // Mode-specific progress tracking
    let normalModeCardIndex = 0;
    let srsModeCardIndex = 0;
    let normalStudyOrder = 'forward';
    let normalOrder = [];
    let normalStudyCards = [];
    let restoredProgress = null;

    // Phased SRS State & Session UUID
    const studySessionId = (typeof crypto !== 'undefined' && crypto.randomUUID) 
        ? crypto.randomUUID() 
        : 'session-' + Date.now() + '-' + Math.random().toString(36).substring(2, 9);
    let srsUndoStack = [];
    let cardIdForDueDate = null;

    function getSetIdFromParams(params = pageParams) {
        const rawSetId = params.get('setId');
        if (rawSetId === null) return null;

        const numericSetId = Number(rawSetId);
        return Number.isFinite(numericSetId) && rawSetId.trim() !== '' ? numericSetId : rawSetId;
    }

    function getDeckSrsSettings(set = flashcardSet) {
        const numberOrNull = (value) => {
            if (value === null || value === undefined || value === '') return null;
            const number = Number(value);
            return Number.isFinite(number) ? number : null;
        };
        const requestRetention = numberOrNull(set?.srsSettings?.requestRetention) ?? 0.9;
        const maxIntervalDays = numberOrNull(set?.srsSettings?.maxIntervalDays) ?? 36500;
        const newCardsPerDay = numberOrNull(set?.srsSettings?.newCardsPerDay);
        const reviewsPerDay = numberOrNull(set?.srsSettings?.reviewsPerDay);

        return {
            enabled: set?.srsSettings?.enabled !== false,
            requestRetention: Math.min(0.99, Math.max(0.7, requestRetention)),
            maxIntervalDays: Math.max(1, Math.round(maxIntervalDays)),
            newCardsPerDay: newCardsPerDay === null ? null : Math.max(0, Math.round(newCardsPerDay)),
            reviewsPerDay: reviewsPerDay === null ? null : Math.max(0, Math.round(reviewsPerDay))
        };
    }

    function sameCard(a, b) {
        if (!a || !b) return false;
        if (a.id && b.id) return String(a.id) === String(b.id);
        return a.term === b.term && a.definition === b.definition;
    }

    function cardProgressKey(card) {
        if (!card) return null;
        if (card.id) return `id:${card.id}`;
        return `text:${card.term || ''}::${card.definition || ''}`;
    }

    function getProgressId() {
        return flashcardSet?.id ?? getSetIdFromParams(pageParams);
    }

    function clampIndex(value, length) {
        const index = Number(value);
        if (!Number.isFinite(index) || index < 0) return 0;
        return Math.min(Math.floor(index), Math.max(0, length - 1));
    }

    function playNextCardSound() {
        nextCardSound.currentTime = 0;
        nextCardSound.play().catch(error => {
            console.error('Error playing next card sound:', error);
        });
    }

    function getActiveCards() {
        if (srsModeEnabled && srsCards.length > 0) {
            return {
                cards: srsCards,
                index: srsModeCardIndex,
                setIndex: (value) => {
                    srsModeCardIndex = value;
                    currentCardIndex = value;
                }
            };
        }

        return {
            cards: normalStudyCards.length ? normalStudyCards : (flashcardSet?.cards || []),
            index: normalModeCardIndex,
            setIndex: (value) => {
                normalModeCardIndex = value;
                currentCardIndex = value;
            }
        };
    }

    function shuffledIndices(length) {
        const indices = Array.from({ length }, (_, index) => index);
        for (let i = indices.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [indices[i], indices[j]] = [indices[j], indices[i]];
        }
        return indices;
    }

    function normalizeNormalStudyOrder(value) {
        return ['forward', 'backward', 'random'].includes(value) ? value : 'forward';
    }

    async function loadStudyPreferences() {
        try {
            const settings = window.getFlashcardSettings
                ? await window.getFlashcardSettings()
                : (window.flashcardStore?.getSettings
                    ? await window.flashcardStore.getSettings()
                    : JSON.parse(localStorage.getItem('flashcards-settings') || '{}'));
            normalStudyOrder = normalizeNormalStudyOrder(settings?.normalStudyOrder);
            // Store for use in rendering (e.g. cardBgOpacity)
            window._studyAppSettings = settings || {};
        } catch (error) {
            console.warn('Could not load study order setting:', error);
            normalStudyOrder = 'forward';
        }
    }

    function buildNormalOrder(length) {
        if (normalStudyOrder === 'random') return shuffledIndices(length);
        const order = Array.from({ length }, (_, index) => index);
        return normalStudyOrder === 'backward' ? order.reverse() : order;
    }

    function getSavedNormalIndex(progress, length) {
        if (normalStudyOrder === 'random') return 0;
        const legacyIndex = progress?.cardIndex ?? 0;
        const normalProgress = progress?.normalProgress || {};
        
        // Decouple progress: if progress holds SRS keys, ignore cardIndex as fallback
        const hasSrsProgress = progress?.srsModeLength !== undefined || progress?.srsModeIndex !== undefined || progress?.srsCurrentCardKey !== undefined;
        const fallbackIndex = hasSrsProgress ? 0 : legacyIndex;

        const value = normalStudyOrder === 'backward'
            ? (normalProgress.backward ?? progress?.normalBackwardIndex ?? 0)
            : (normalProgress.forward ?? progress?.normalForwardIndex ?? progress?.normalModeIndex ?? fallbackIndex);
        return clampIndex(value, length || 1);
    }

    function prepareNormalStudyCards(options = {}) {
        const cards = Array.isArray(flashcardSet?.cards) ? flashcardSet.cards : [];
        if (!cards.length) {
            normalOrder = [];
            normalStudyCards = [];
            normalModeCardIndex = 0;
            return;
        }

        normalOrder = buildNormalOrder(cards.length);

        normalStudyCards = normalOrder.map(index => cards[index]).filter(Boolean);
        normalModeCardIndex = clampIndex(normalModeCardIndex, normalStudyCards.length || 1);
    }

    function isInteractiveTarget(target) {
        if (!target) return false;
        return Boolean(target.closest('button, a, input, textarea, select, audio, video, [contenteditable="true"], .modal.visible, .completion-screen.visible, .zoom-image-btn, .media-zoom-button, .image-container.has-image, .card-media-item'));
    }

    function getScrollableCardContent(target) {
        const content = target?.closest?.('.card-content');
        if (!content) return null;
        return content.scrollHeight > content.clientHeight + 4 ? content : null;
    }

    function isBlockingOverlayVisible() {
        return Boolean(document.querySelector('.modal.visible, .completion-screen.visible, .shortcuts-modal.show'));
    }

    function resetVisibleScroll() {
        const activeContent = flashcardContainer.classList.contains('flipped')
            ? document.querySelector('.card-face.back .card-content')
            : document.querySelector('.card-face.front .card-content');

        if (activeContent) {
            activeContent.scrollTop = 0;
        }
    }

    function setCardFlipped(flipped, options = {}) {
        if (options.noTransition) {
            flashcardContainer.classList.add('no-transition');
        }

        flashcardContainer.classList.toggle('flipped', Boolean(flipped));
        isCardFlipped = Boolean(flipped);

        if (options.noTransition) {
            void flashcardContainer.offsetWidth;
            flashcardContainer.classList.remove('no-transition');
        }
    }

    function revealStudySurface() {
        requestAnimationFrame(() => {
            studyContainer?.classList.remove('is-loading');
        });
    }

    // Apply saved theme settings from localStorage
    function applyThemeSettings() {
        // If global functions from settings.js are available, use them
        if (window.loadAndApplySettings) {
            window.loadAndApplySettings();
        } else {
            // Fallback implementation if settings.js functions are not available
            const savedTheme = localStorage.getItem('flashcards-theme') || 'dark';
            document.documentElement.setAttribute('data-theme', savedTheme);
            
            // Add transition class
            document.documentElement.classList.add('theme-transition');
            
            // Force repaint to apply styles immediately
            document.documentElement.style.display = 'none';
            void document.documentElement.offsetHeight;
            document.documentElement.style.display = '';
            
            // Remove transition class after animation completes
            setTimeout(() => {
                document.documentElement.classList.remove('theme-transition');
            }, 300);
        }
    }

    // Load saved progress
    async function loadSavedProgress() {
        try {
            const progressId = getProgressId();
            if (progressId === null || progressId === undefined) return;

            const savedProgress = window.flashcardStore?.getProgress
                ? await window.flashcardStore.getProgress(progressId)
                : JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');

            if (savedProgress && String(savedProgress.setId) === String(progressId)) {
                restoredProgress = savedProgress;
                
                // Decoupled structure loading
                if (savedProgress.normal) {
                    normalModeCardIndex = savedProgress.normal.studyOrder === 'backward'
                        ? (savedProgress.normal.backwardIndex ?? 0)
                        : (savedProgress.normal.forwardIndex ?? 0);
                } else {
                    normalModeCardIndex = getSavedNormalIndex(savedProgress, flashcardSet?.cards?.length || 1);
                }
                
                if (savedProgress.srs) {
                    srsCurrentCardKey = savedProgress.srs.currentCardKey || null;
                    if (savedProgress.srs.reviewedCardIds && Array.isArray(savedProgress.srs.reviewedCardIds)) {
                        srsReviewedCardIds = new Set(savedProgress.srs.reviewedCardIds);
                    } else {
                        srsReviewedCardIds = new Set();
                    }
                } else {
                    srsCurrentCardKey = savedProgress.srsCurrentCardKey || null;
                    if (savedProgress.srsReviewedCardIds && Array.isArray(savedProgress.srsReviewedCardIds)) {
                        srsReviewedCardIds = new Set(savedProgress.srsReviewedCardIds);
                    } else {
                        srsReviewedCardIds = new Set();
                    }
                }
                
                srsModeCardIndex = clampIndex(
                    savedProgress.srsModeIndex ?? 0,
                    savedProgress.srsModeLength || flashcardSet?.cards?.length || 1
                );
                currentCardIndex = srsModeEnabled ? srsModeCardIndex : normalModeCardIndex;
            }
        } catch (error) {
            console.error('Error loading saved progress:', error);
        }
    }

    // Save current progress
    async function saveProgress(options = {}) {
        try {
            if (!flashcardSet) return;
            const progressId = getProgressId();
            if (progressId === null || progressId === undefined) return;
            if (!srsModeEnabled && normalStudyOrder === 'random') return;

            const currentSrsCard = srsCards[srsModeCardIndex] || null;
            if (srsModeEnabled) {
                srsCurrentCardKey = currentSrsCard ? cardProgressKey(currentSrsCard) : null;
            }

            const normalProgress = {
                ...(restoredProgress?.normalProgress || {})
            };
            if (!srsModeEnabled && normalStudyOrder !== 'random') {
                normalProgress[normalStudyOrder] = normalModeCardIndex;
            }

            const progress = {
                setId: progressId,
                cardIndex: currentCardIndex, // Keep for compatibility
                normalModeIndex: normalProgress.forward ?? normalModeCardIndex,
                normalForwardIndex: normalProgress.forward ?? 0,
                normalBackwardIndex: normalProgress.backward ?? 0,
                normalProgress,
                normalStudyOrder,
                normalModeLength: normalStudyCards.length || flashcardSet.cards.length,
                normalOrder,
                srsModeIndex: srsModeCardIndex,
                srsModeLength: srsCards.length,
                srsCurrentCardKey,
                srsReviewedCardIds: Array.from(srsReviewedCardIds),
                timestamp: Date.now(),
                
                // Decoupled structure saving
                normal: {
                    forwardIndex: normalProgress.forward ?? (normalStudyOrder === 'forward' ? normalModeCardIndex : 0),
                    backwardIndex: normalProgress.backward ?? (normalStudyOrder === 'backward' ? normalModeCardIndex : 0),
                    studyOrder: normalStudyOrder
                },
                srs: {
                    currentCardKey: srsCurrentCardKey,
                    reviewedCardIds: Array.from(srsReviewedCardIds),
                    sessionStats: srsSessionStats
                }
            };

            if (window.flashcardStore?.saveProgress) {
                await window.flashcardStore.saveProgress(progressId, progress);
            } else {
                localStorage.setItem(STORAGE_KEY, JSON.stringify(progress));
            }

            restoredProgress = progress;

            if (options.notify) {
                showToast('Progress saved', 'success');
            }
        } catch (error) {
            console.error('Error saving progress:', error);
            showToast('Failed to save progress', 'error');
        }
    }

    function getPremadeSrsStateKey(set = flashcardSet) {
        return set?.isPremade && set.id ? `premadeSrs:${set.id}` : null;
    }

    async function loadPremadeSrsOverlay() {
        const key = getPremadeSrsStateKey();
        if (!key || !Array.isArray(flashcardSet?.cards)) return;

        try {
            const saved = window.flashcardStore?.getState
                ? await window.flashcardStore.getState(key)
                : JSON.parse(localStorage.getItem(key) || 'null');
            const savedCards = Array.isArray(saved?.cards) ? saved.cards : [];
            if (savedCards.length === 0) return;

            const savedByKey = new Map(savedCards.map(card => [card.key, card]));
            flashcardSet.cards = flashcardSet.cards.map(card => {
                const savedCard = savedByKey.get(cardProgressKey(card));
                if (!savedCard) return card;
                return {
                    ...card,
                    srs: savedCard.srs || card.srs,
                    reviewHistory: Array.isArray(savedCard.reviewHistory) ? savedCard.reviewHistory : card.reviewHistory,
                    tags: Array.isArray(savedCard.tags) ? savedCard.tags : card.tags,
                    suspended: Boolean(savedCard.suspended),
                    buriedUntil: savedCard.buriedUntil ?? null
                };
            });
        } catch (error) {
            console.warn('Could not load premade SRS progress:', error);
        }
    }

    async function savePremadeSrsOverlay() {
        const key = getPremadeSrsStateKey();
        if (!key || !Array.isArray(flashcardSet?.cards)) return;

        const overlay = {
            setId: flashcardSet.id,
            updatedAt: Date.now(),
            cards: flashcardSet.cards.map(card => ({
                key: cardProgressKey(card),
                srs: card.srs || null,
                reviewHistory: Array.isArray(card.reviewHistory) ? card.reviewHistory : [],
                tags: Array.isArray(card.tags) ? card.tags : [],
                suspended: Boolean(card.suspended),
                buriedUntil: card.buriedUntil ?? null
            }))
        };

        try {
            if (window.flashcardStore?.setState) {
                await window.flashcardStore.setState(key, overlay);
            } else {
                localStorage.setItem(key, JSON.stringify(overlay));
            }
        } catch (error) {
            console.warn('Could not save premade SRS progress:', error);
        }
    }

    // Toast notification
    function showToast(message, type = 'info') {
        const toast = document.createElement('div');
        toast.textContent = message;
        toast.classList.add('toast', type);
        document.body.appendChild(toast);
        
        setTimeout(() => {
            toast.classList.add('fade-out');
            setTimeout(() => toast.remove(), 300);
        }, 2000);
    }

    // Load flashcard set
    async function loadFlashcardSet() {
        try {
            const urlParams = new URLSearchParams(window.location.search);
            const isPremade = urlParams.get('premade') === 'true';
            
            if (isPremade) {
                // Load premade flashcard set
                const classParam = urlParams.get('class');
                const subjectParam = urlParams.get('subject');
                const setId = urlParams.get('set');
                
                if (!classParam || !subjectParam || !setId) {
                    showToast('Invalid premade flashcard parameters!', 'error');
                    goToLibrary(true);
                    return;
                }
                
                // Map subject names to folder names
                const subjectFolderMap = {
                    'Science': 'Science',
                    'Mathematics': 'Maths',
                    'Maths': 'Maths',
                    'English': 'English',
                    'Civics': 'Civics',
                    'Geography': 'Geography',
                    'History': 'History',
                    'Hindi': 'Hindi',
                    'Politics': 'Politics',
                    'Physics': 'Physics',
                    'Inorganic Chemistry': 'inorganic-chemistry',
                    'Organic Chemistry': 'organic-chemistry',
                    'Physical Chemistry': 'physical-chemistry',
                    'Biology': 'Biology',
                    'Physical Education': 'Physical-education'
                };
                
                const folderName = subjectFolderMap[subjectParam] || subjectParam;
                const folderPath = `Premade-cards/${classParam}/${folderName}`;
                
                // Try to load the specific set file
                const fullUrl = `${folderPath}/${setId}`;
                let response = await fetch(fullUrl);
                
                // If the first attempt fails, try with different path variations
                if (!response.ok) {
                    // Try with encoded subject name
                    const encodedSubject = encodeURIComponent(subjectParam);
                    const altPath1 = `Premade-cards/${classParam}/${encodedSubject}/${setId}`;
                    response = await fetch(altPath1);
                    
                    if (!response.ok) {
                        // Try with the original subject name
                        const altPath2 = `Premade-cards/${classParam}/${subjectParam}/${setId}`;
                        response = await fetch(altPath2);
                    }
                }
                
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status} - Could not find file at ${fullUrl}`);
                }
                
                const premadeData = await response.json();
                
                // Convert premade data to flashcard set format
                flashcardSet = {
                    id: `premade-${classParam}-${subjectParam}-${setId}`,
                    name: premadeData.name,
                    description: premadeData.description,
                    cards: premadeData.cards.map(card => ({
                        term: card.term,
                        definition: card.definition,
                        termImage: card.termImage || '',
                        definitionImage: card.definitionImage || ''
                    })),
                    created: Date.now(),
                    lastModified: Date.now(),
                    openedCount: 0,
                    isPremade: true,
                    class: classParam,
                    subject: subjectParam,
                    setId: setId
                };
                await loadPremadeSrsOverlay();
                
            } else {
                const setId = getSetIdFromParams(urlParams);
                const sets = window.flashcardStore?.listSets
                    ? await window.flashcardStore.listSets()
                    : JSON.parse(localStorage.getItem('flashcardSets') || '[]');
                flashcardSet = sets.find(set => String(set.id) === String(setId));

                if (!flashcardSet) {
                    showToast('Flashcard set not found!', 'error');
                    goToLibrary(false);
                    return;
                }

                flashcardSet = {
                    ...flashcardSet,
                    openedCount: (flashcardSet.openedCount || 0) + 1,
                    lastOpened: Date.now()
                };

                if (window.flashcardStore?.saveSet) {
                    flashcardSet = await window.flashcardStore.saveSet(flashcardSet);
                } else {
                    const updatedSets = sets.map(set => String(set.id) === String(setId) ? flashcardSet : set);
                    localStorage.setItem('flashcardSets', JSON.stringify(updatedSets));
                }
            }

            // Update UI
            setNameDisplay.textContent = flashcardSet.name;
            
            // Update back button based on flashcard type
            if (flashcardSet.isPremade) {
                backBtn.href = libraryUrl(true);
            } else {
                backBtn.href = libraryUrl(false);
            }
            
            await loadStudyPreferences();
            await loadSavedProgress();
            prepareNormalStudyCards({ useSavedOrder: true });

            // Activate SRS mode if enabled
            if (srsModeEnabled && window.srsManager && window.srsManager.isReady()) {
                const srsActivated = activateSRSMode();
                if (!srsActivated) {
                    revealStudySurface();
                    return;
                }
            }

            showCard({ initial: !hasRenderedInitialCard });
            updateNavButtons();
            updateProgress();
        } catch (error) {
            console.error('Error loading flashcard set:', error);
            showToast(`Error loading flashcard set: ${error.message}`, 'error');
            setTimeout(() => {
                const urlParams = new URLSearchParams(window.location.search);
                const isPremade = urlParams.get('premade') === 'true';
                if (isPremade) {
                    goToLibrary(true);
                } else {
                    goToLibrary(false);
                }
            }, 3000);
        }
    }

    // Show current card
    function showCard(options = {}) {
        if (!flashcardSet || flashcardSet.cards.length === 0) return;
        const isInitialRender = options.initial || !hasRenderedInitialCard;

        const active = getActiveCards();
        let cardsToUse = active.cards;
        let currentIndex = active.index;

        if (currentIndex >= cardsToUse.length || currentIndex < 0) {
            console.warn('Invalid card index:', currentIndex, 'for cards length:', cardsToUse.length);
            currentIndex = 0;
            active.setIndex(0);
        }

        // Update the global currentCardIndex for compatibility with existing functions
        currentCardIndex = currentIndex;
        const card = cardsToUse[currentIndex];
        const termText = document.querySelector('.term-text');
        const definitionText = document.querySelector('.definition-text');
        const termImage = document.querySelector('.term-image');
        const definitionImage = document.querySelector('.definition-image');
        const termFace = document.querySelector('.card-face.front');
        const definitionFace = document.querySelector('.card-face.back');
        const termMediaList = document.querySelector('.term-media-list');
        const definitionMediaList = document.querySelector('.definition-media-list');

        // Make sure the card is in term view (not flipped)
        // We no longer need to reset the flip state here since it's handled in navigate
        // but we'll keep it for safety
        if (flashcardContainer.classList.contains('flipped')) {
            setCardFlipped(false, { noTransition: true });
        }
        
        if (!isInitialRender) {
            flashcardContainer.classList.add('new-card');
            setTimeout(() => flashcardContainer.classList.remove('new-card'), 300);
        } else {
            flashcardContainer.classList.remove('new-card');
        }

        fadeElement(termText, () => {
            termText.innerHTML = formatContent(card.term);
            window.EruditeMath?.renderMath?.(termText);
        });

        fadeElement(definitionText, () => {
            definitionText.innerHTML = formatContent(card.definition);
            window.EruditeMath?.renderMath?.(definitionText);
        });

        // Handle images before sizing text so mixed cards pick the right layout.
        handleImage(termImage, card.termImage);
        handleImage(definitionImage, card.definitionImage);
        applyCardBackground(termFace, card, 'term');
        applyCardBackground(definitionFace, card, 'definition');
        renderMediaList(termMediaList, card, 'term');
        renderMediaList(definitionMediaList, card, 'definition');

        adjustContentCentering(termText);
        adjustContentCentering(definitionText);
        
        // Update progress indicators
        updateProgress();
        updateNavButtons();
        
        // Save progress 
        saveProgress();

        if (isInitialRender) {
            hasRenderedInitialCard = true;
            revealStudySurface();
        }
    }

    // Format content for different types
    function formatContent(content) {
        if (!content) return '';
        
        // HTML content (from contenteditable) should be preserved exactly as is
        return content;
    }

    function escapeAttribute(value) {
        return String(value ?? '')
            .replace(/&/g, '&amp;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#039;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;');
    }

    // Adjust content centering based on length and type
    function adjustContentCentering(element) {
        // Remove existing classes
        element.classList.remove('large-content', 'medium-content', 'small-content');
        
        // Check content length and structure
        const contentLength = element.textContent.length;
        const hasLists = element.querySelector('ul, ol') !== null;
        const hasParagraphs = element.querySelector('p') !== null;
        const hasLineBreaks = element.innerHTML.includes('<br');
        const cardFace = element.closest('.card-face');
        const imageContainer = cardFace?.querySelector('.image-container');
        const mediaList = cardFace?.querySelector('.card-media-list');
        const hasImages = Boolean(imageContainer?.classList.contains('has-image') || mediaList?.children?.length);
        
        // Get the card content container parent
        const cardContent = element.closest('.card-content');
        if (cardContent) {
            cardContent.classList.remove(
                'content-small',
                'content-medium',
                'content-large',
                'with-image',
                'no-image'
            );
            cardContent.classList.add(hasImages ? 'with-image' : 'no-image');
            cardContent.style.alignItems = '';
            cardContent.style.justifyContent = '';
            cardContent.scrollTop = 0;
        }
        
        // Apply the appropriate class based on content
        if (hasLists || hasParagraphs || contentLength > 150 || hasLineBreaks) {
            element.classList.add('large-content');
            cardContent?.classList.add('content-large');
        } else if (contentLength > 50 || hasImages) {
            element.classList.add('medium-content');
            cardContent?.classList.add('content-medium');
        } else {
            element.classList.add('small-content');
            cardContent?.classList.add('content-small');
        }
        
        // If content starts with list items, ensure they're properly aligned
        if (hasLists) {
            element.style.textAlign = 'left';
        }
    }

    // Content swap helper. Keep it instant to avoid ghosting during touch flips/swipes.
    function fadeElement(element, updateFn) {
        element.style.opacity = '1';
        updateFn();
    }

    // Handle image display
    function handleImage(imgElement, imgSrc) {
        const zoomBtn = imgElement.nextElementSibling;
        const imageContainer = imgElement.closest('.image-container');
        if (imgSrc) {
            imgElement.src = imgSrc;
            imgElement.style.display = 'block';
            imageContainer?.classList.add('has-image');
            // Show zoom button only if image exists
            if (zoomBtn) zoomBtn.style.display = 'flex';
            fadeElement(imgElement, () => {});
        } else {
            imgElement.style.display = 'none';
            imgElement.removeAttribute('src');
            imageContainer?.classList.remove('has-image');
            // Hide zoom button if no image
            if (zoomBtn) zoomBtn.style.display = 'none';
        }
    }

    function applyCardBackground(faceElement, card, side) {
        const backgroundEl = faceElement?.querySelector(side === 'definition' ? '.definition-bg' : '.term-bg');
        const background = window.EruditeMedia?.getSideBackground?.(card, side) || null;
        if (!backgroundEl) return;
        if (!background?.src) {
            backgroundEl.classList.remove('visible', 'no-overlay');
            backgroundEl.style.backgroundImage = '';
            return;
        }
        backgroundEl.style.backgroundImage = `url("${background.src}")`;
        backgroundEl.style.backgroundSize = background.fit || 'cover';
        // Use global cardBgOpacity from loaded settings if available
        const globalOpacity = parseFloat(window._studyAppSettings?.cardBgOpacity);
        const opacity = Number.isFinite(globalOpacity) ? globalOpacity : (background.opacity ?? 0.32);
        backgroundEl.style.setProperty('--card-bg-opacity', String(opacity));
        backgroundEl.classList.add('visible');
        if (opacity >= 1.0) {
            backgroundEl.classList.add('no-overlay');
        } else {
            backgroundEl.classList.remove('no-overlay');
        }
    }

    function renderMediaList(container, card, side) {
        if (!container) return;
        const items = (window.EruditeMedia?.getSideMedia?.(card, side, { includeLegacy: false }) || [])
            .filter(item => item && item.src);
        container.innerHTML = items.map(item => {
            const src = escapeAttribute(item.src || '');
            const name = escapeAttribute(item.name || item.kind || 'Media');
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
                        <i class="fas fa-search-plus"></i>
                    </button>
                </div>
            `;
        }).join('');
    }

    // Update progress
    function updateProgress() {
        if (!flashcardSet || !progressDisplay) return;

        if (srsModeEnabled) {
            const completed = srsReviewedCardIds.size;
            const total = srsCards.length + completed;
            const progress = Math.min(100, (completed / Math.max(1, total)) * 100);

            progressDisplay.textContent = `${completed}/${total}`;
            if (progressFill) {
                progressFill.style.width = `${progress}%`;
            }
            return;
        }

        const { cards: cardsToUse, index: currentIndex } = getActiveCards();

        const total = Math.max(1, cardsToUse.length); // Prevent division by zero
        const current = Math.max(1, currentIndex + 1);
        const progress = Math.min(100, (current / total) * 100); // Cap at 100%

        progressDisplay.textContent = `${current}/${total}`;
        if (progressFill) {
            progressFill.style.width = `${progress}%`;
        }
    }

    // Update navigation buttons
    function updateNavButtons() {
        const { cards: cardsToUse, index: currentIndex } = getActiveCards();

        if (srsModeEnabled) {
            // In SRS mode, disable navigation buttons completely
            prevBtn.disabled = true;
            nextBtn.disabled = true;
            prevBtn.style.display = 'none';
            nextBtn.style.display = 'none';
        } else {
            // In normal mode, show navigation buttons
            prevBtn.disabled = currentIndex === 0;
            nextBtn.disabled = cardsToUse.length === 0;
            prevBtn.style.display = 'flex';
            nextBtn.style.display = 'flex';
        }
    }

    // Navigate between cards
    function navigate(direction, options = {}) {
        if (!flashcardSet || flashcardSet.cards.length === 0) return;

        const { cards: cardsToUse, index: currentIndex, setIndex } = getActiveCards();

        const newIndex = direction === 'prev' ? currentIndex - 1 : currentIndex + 1;

        // Don't allow going past the bounds
        if (newIndex < 0) return;
        if (newIndex > cardsToUse.length - 1) {
            // Only show completion screen if we're moving forward from the last card
            if (currentIndex === cardsToUse.length - 1 && direction === 'next') {
                completionScreen.classList.remove('hidden');
                completionScreen.classList.add('visible');
                showToast('Congratulations! Set completed!', 'success');

                // Play success sound
                successSound.play().catch(error => {
                    console.error('Error playing success sound:', error);
                });
            }
            return;
        }

        if (options.playSound !== false) {
            playNextCardSound();
        }

        setIndex(newIndex);

        // If the card is currently flipped, immediately reset it
        // without showing the flip animation before showing the new card
        if (flashcardContainer.classList.contains('flipped')) {
            setCardFlipped(false, { noTransition: true });
        }
        
        showCard();
        updateNavButtons();
    }

    function flipCard(options = {}) {
        if (srsModeEnabled && srsSessionComplete) return;
        if (!flashcardSet || isFlipping) return;
        if (options.onlyReveal && flashcardContainer.classList.contains('flipped')) return;

        isFlipping = true;
        flipSound.currentTime = 0;
        flipSound.play().catch(error => {
            console.error('Error playing flip sound:', error);
        });

        setCardFlipped(options.onlyReveal ? true : !flashcardContainer.classList.contains('flipped'));

        setTimeout(() => {
            resetVisibleScroll();
            isFlipping = false;

            if (srsModeEnabled && flashcardContainer.classList.contains('flipped')) {
                showRatingInterface();
            } else if (!flashcardContainer.classList.contains('flipped')) {
                hideRatingInterface();
            }
        }, FLIP_LOCK_MS);
    }

    function animateSwipeOut(dx, dy, callback) {
        const travelX = Math.sign(dx || 1) * Math.min(window.innerWidth * 0.55, 520);
        const travelY = Math.sign(dy || 1) * Math.min(window.innerHeight * 0.16, 120);
        const rotation = Math.max(-10, Math.min(10, dx / 18));

        playNextCardSound();
        flashcardContainer.classList.add('swipe-out');
        flashcardContainer.style.transform = `translate(${travelX}px, ${travelY}px) rotate(${rotation}deg)`;

        setTimeout(() => {
            callback();
            flashcardContainer.classList.add('no-transition');
            flashcardContainer.classList.remove('swipe-out');
            flashcardContainer.style.transform = '';
            void flashcardContainer.offsetWidth;
            flashcardContainer.classList.remove('no-transition');
        }, 220);
    }

    function handleStudySwipe(dx, dy) {
        if (srsModeEnabled) {
            if (!flashcardContainer.classList.contains('flipped')) {
                flipCard({ onlyReveal: true });
            }
            return;
        }

        const { cards, index } = getActiveCards();
        if (index >= cards.length - 1) {
            navigate('next');
            return;
        }

        animateSwipeOut(dx, dy, () => navigate('next', { playSound: false }));
    }

    function finishSwipeGesture(dx, dy, elapsed, event) {
        const now = performance.now();
        if (now - lastSwipeAt < 280) return;

        const distance = Math.hypot(dx, dy);
        const velocity = distance / Math.max(1, elapsed);
        if (distance < SWIPE_DISTANCE_THRESHOLD && velocity < SWIPE_VELOCITY_THRESHOLD) return;

        lastSwipeAt = now;
        event?.preventDefault?.();
        suppressNextClick = true;
        setTimeout(() => {
            suppressNextClick = false;
        }, 320);
        handleStudySwipe(dx, dy);
    }

    if (studyArea) {
        studyArea.addEventListener('pointerdown', (event) => {
            if (event.pointerType === 'touch') return;
            if (event.button !== undefined && event.button !== 0) return;
            if (isInteractiveTarget(event.target)) return;
            pointerStart = {
                id: event.pointerId,
                x: event.clientX,
                y: event.clientY,
                time: performance.now()
            };
        });

        studyArea.addEventListener('pointerup', (event) => {
            if (!pointerStart || pointerStart.id !== event.pointerId) return;

            const dx = event.clientX - pointerStart.x;
            const dy = event.clientY - pointerStart.y;
            const elapsed = Math.max(1, performance.now() - pointerStart.time);
            pointerStart = null;

            finishSwipeGesture(dx, dy, elapsed, event);
        });

        studyArea.addEventListener('pointermove', (event) => {
            if (!pointerStart || pointerStart.id !== event.pointerId) return;
            if (Math.hypot(event.clientX - pointerStart.x, event.clientY - pointerStart.y) > 12) {
                event.preventDefault();
            }
        });

        studyArea.addEventListener('pointercancel', () => {
            pointerStart = null;
        });

        studyArea.addEventListener('touchstart', (event) => {
            if (isInteractiveTarget(event.target) || event.touches.length !== 1) return;
            const touch = event.touches[0];
            touchStart = {
                x: touch.clientX,
                y: touch.clientY,
                time: performance.now(),
                scrollTarget: getScrollableCardContent(event.target),
                isScrollingContent: false
            };
        }, { passive: true });

        studyArea.addEventListener('touchmove', (event) => {
            if (!touchStart || event.touches.length !== 1) return;
            const touch = event.touches[0];
            const dx = touch.clientX - touchStart.x;
            const dy = touch.clientY - touchStart.y;
            const absX = Math.abs(dx);
            const absY = Math.abs(dy);

            if (touchStart.scrollTarget && absY > 8 && absY > absX * 1.15) {
                touchStart.isScrollingContent = true;
                suppressNextClick = true;
                return;
            }

            if (Math.hypot(dx, dy) > 12) {
                event.preventDefault();
            }
        }, { passive: false });

        studyArea.addEventListener('touchend', (event) => {
            if (!touchStart || event.changedTouches.length === 0) return;
            const touch = event.changedTouches[0];
            const dx = touch.clientX - touchStart.x;
            const dy = touch.clientY - touchStart.y;
            const elapsed = Math.max(1, performance.now() - touchStart.time);
            const wasScrollingContent = touchStart.isScrollingContent;
            touchStart = null;

            if (wasScrollingContent) {
                setTimeout(() => {
                    suppressNextClick = false;
                }, 180);
                return;
            }

            finishSwipeGesture(dx, dy, elapsed, event);
        }, { passive: false });

        studyArea.addEventListener('touchcancel', () => {
            touchStart = null;
        });
    }

    // ── Image zoom intercept (capture phase) ──
    // The 3D card flip uses position:absolute overlapping faces with
    // backface-visibility:hidden. In Chromium's preserve-3d context,
    // pointer-events can land on the wrong face. Rather than fight
    // the 3D hit-testing, we intercept at the capture phase: if the
    // currently-visible face has an image, open zoom and kill the event.
    flashcardContainer.addEventListener('click', (event) => {
        // Determine which face is currently visible
        const isFlippedNow = flashcardContainer.classList.contains('flipped');
        const visibleFace = flashcardContainer.querySelector(
            isFlippedNow ? '.card-face.back' : '.card-face.front'
        );
        const imgContainer = visibleFace?.querySelector('.image-container.has-image');
        if (!imgContainer) return; // no image on visible face — let it through

        // Check if the click landed on or near the image area.
        // Because 3D transforms can misdirect event.target, we also
        // check if the click coordinates fall inside the image container.
        const rect = imgContainer.getBoundingClientRect();
        const inBounds = (
            event.clientX >= rect.left &&
            event.clientX <= rect.right &&
            event.clientY >= rect.top &&
            event.clientY <= rect.bottom
        );

        // Direct hit: target is inside image container (normal case)
        const directHit = imgContainer.contains(event.target);

        if (directHit || inBounds) {
            event.stopImmediatePropagation();
            event.preventDefault();
            const img = imgContainer.querySelector('img[src]');
            if (img?.src) {
                openImageModal(img.currentSrc || img.src);
            }
        }
    }, true); // capture phase — fires BEFORE the bubble-phase flip handler

    // Event Handlers — flip card on click (bubble phase)
    flashcardContainer.addEventListener('click', (event) => {
        if (suppressNextClick) {
            event.preventDefault();
            return;
        }
        if (isInteractiveTarget(event.target)) return;
        flipCard();
    });

    // Add hover effect indicators
    flashcardContainer.addEventListener('mouseenter', () => {
        flashcardContainer.classList.add('hover-effect');
    });
    
    flashcardContainer.addEventListener('mouseleave', () => {
        flashcardContainer.classList.remove('hover-effect');
    });

    // Add keyboard controls for better accessibility
    document.addEventListener('keydown', (e) => {
        if (e.repeat || isBlockingOverlayVisible() || isInteractiveTarget(document.activeElement)) return;

        const ratingContainer = document.getElementById('srs-rating-container');
        const ratingVisible = ratingContainer && !ratingContainer.classList.contains('hidden');

        if (srsModeEnabled) {
            if (srsSessionComplete) {
                e.preventDefault();
                return;
            }

            // Bind Z or Ctrl+Z for undo review
            if (e.key.toLowerCase() === 'z' || (e.ctrlKey && e.key.toLowerCase() === 'z')) {
                e.preventDefault();
                undoLastReview();
                return;
            }

            if (e.key === ' ' || e.key === 'Enter') {
                e.preventDefault();
                flipCard({ onlyReveal: true });
                return;
            }

            if (ratingVisible && ['1', '2', '3', '4'].includes(e.key)) {
                e.preventDefault();
                const ratings = ['Again', 'Hard', 'Good', 'Easy'];
                handleSRSRating(ratings[Number(e.key) - 1]);
            }
            return;
        }

        if (e.key === 'ArrowLeft') {
            e.preventDefault();
            navigate('prev');
        } else if (e.key === 'ArrowRight') {
            e.preventDefault();
            navigate('next');
        } else if (e.key === ' ' || e.key === 'Enter') {
            e.preventDefault();
            flipCard();
        }
    });

    // Close completion screen
    if (closeCompletionBtn) {
        closeCompletionBtn.addEventListener('click', () => {
            if (srsModeEnabled) return;
            completionScreen.classList.remove('visible');
            completionScreen.classList.add('hidden');
        });
    }

    practiceAgainBtn.addEventListener('click', () => {
        const nextDueSetId = completionScreen.dataset.nextDueSetId;
        if (srsModeEnabled && reviewDueSession && nextDueSetId) {
            window.location.href = studyUrl(nextDueSetId, true);
            return;
        }

        // Hide completion screen
        completionScreen.classList.remove('visible');
        completionScreen.classList.add('hidden');

        // Reset appropriate card index
        if (srsModeEnabled && window.srsManager && window.srsManager.isReady()) {
            srsSessionComplete = false;
            srsModeCardIndex = 0;
            srsReviewedCardIds.clear();
            srsCurrentCardKey = null;
            if (activateSRSMode()) {
                showCard();
                updateNavButtons();
                updateProgress();
            }
        } else {
            normalModeCardIndex = 0;
            prepareNormalStudyCards({ useSavedOrder: false });
            showCard();
            updateNavButtons();
        }
    });

    goHomeBtn.addEventListener('click', async () => {
        if (window.flashcardStore?.removeState) {
            await window.flashcardStore.removeState(STORAGE_KEY);
        } else {
            localStorage.removeItem(STORAGE_KEY);
        }
        if (flashcardSet && flashcardSet.isPremade) {
            goToLibrary(true);
        } else {
            goToLibrary(false);
        }
    });

    window.addEventListener('erudite-menu-toast', (event) => {
        const { message, type } = event.detail || {};
        if (message) showToast(message, type || 'info');
    });

    // Navigation button event listeners
    prevBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        if (!prevBtn.disabled) {
            navigate('prev');
        }
    });

    nextBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        if (!nextBtn.disabled) {
            navigate('next');
        }
    });

    // Image Zoom functionality
    function openImageModal(imgSrc) {
        if (!imgSrc) return;
        
        zoomedImage.src = imgSrc;
        imageModal.classList.remove('hidden');
        imageModal.classList.add('visible');
        
        // Pre-load the image
        const img = new Image();
        img.onload = function() {
            zoomedImage.src = imgSrc;
        };
        img.src = imgSrc;
    }
    
    function closeImageModal() {
        imageModal.classList.remove('visible');
        setTimeout(() => {
            imageModal.classList.add('hidden');
        }, 300);
    }
    
    // Pointer-down isolation: prevent swipe gesture from starting
    // when the user presses on the image area.
    flashcardContainer.addEventListener('pointerdown', (event) => {
        const isFlippedNow = flashcardContainer.classList.contains('flipped');
        const visibleFace = flashcardContainer.querySelector(
            isFlippedNow ? '.card-face.back' : '.card-face.front'
        );
        const imgContainer = visibleFace?.querySelector('.image-container.has-image, .card-media-item');
        if (!imgContainer) return;

        const rect = imgContainer.getBoundingClientRect();
        const inBounds = (
            event.clientX >= rect.left &&
            event.clientX <= rect.right &&
            event.clientY >= rect.top &&
            event.clientY <= rect.bottom
        );
        if (imgContainer.contains(event.target) || inBounds) {
            event.stopPropagation();
        }
    }, true);
    
    // Close image modal when clicking the close button
    closeImageBtn.addEventListener('click', closeImageModal);

    // Set Due Date modal bindings
    const closeSrsDateBtn = document.getElementById('close-srs-date');
    const cancelSrsDateBtn = document.getElementById('cancel-srs-date');
    const saveSrsDateBtn = document.getElementById('save-srs-date');
    const srsDateModal = document.getElementById('srs-date-modal');
    const srsDueDateInput = document.getElementById('srs-due-date-input');

    if (closeSrsDateBtn) closeSrsDateBtn.addEventListener('click', hideSrsDateModal);
    if (cancelSrsDateBtn) cancelSrsDateBtn.addEventListener('click', hideSrsDateModal);
    if (saveSrsDateBtn) {
        saveSrsDateBtn.addEventListener('click', () => {
            if (cardIdForDueDate && srsDueDateInput?.value) {
                setDueDateActiveCard(srsDueDateInput.value);
                hideSrsDateModal();
            }
        });
    }
    if (srsDateModal) {
        srsDateModal.addEventListener('click', (e) => {
            if (e.target === srsDateModal) {
                hideSrsDateModal();
            }
        });
    }

    flashcardContainer.addEventListener('click', event => {
        const zoomButton = event.target.closest('[data-zoom-src]');
        if (!zoomButton) return;
        event.preventDefault();
        event.stopPropagation();
        openImageModal(zoomButton.dataset.zoomSrc);
    });
    
    // Close image modal when clicking outside the image
    imageModal.addEventListener('click', (e) => {
        if (e.target === imageModal) {
            closeImageModal();
        }
    });
    
    // Close image modal or date modal with escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            if (!imageModal.classList.contains('hidden')) {
                closeImageModal();
            }
            const dateModal = document.getElementById('srs-date-modal');
            if (dateModal && !dateModal.classList.contains('hidden')) {
                hideSrsDateModal();
            }
        }
    });

    // SRS Initialization
    async function initializeSRS() {
        const savedSRSMode = window.flashcardStore?.getState
            ? await window.flashcardStore.getState('srsModeEnabled')
            : localStorage.getItem('srsModeEnabled');
        srsModeEnabled = savedSRSMode === true || savedSRSMode === 'true';
        studyContainer?.classList.toggle('srs-mode-active', srsModeEnabled);

        window.getSRSMode = () => srsModeEnabled;
        window.setSRSMode = async (enabled) => {
            srsModeEnabled = Boolean(enabled);
            if (window.flashcardStore?.setState) {
                await window.flashcardStore.setState('srsModeEnabled', srsModeEnabled);
            } else {
                localStorage.setItem('srsModeEnabled', String(srsModeEnabled));
            }

            if (!flashcardSet) return;
            if (srsModeEnabled && window.srsManager && window.srsManager.isReady()) {
                if (activateSRSMode()) {
                    showCard();
                    updateNavButtons();
                    updateProgress();
                }
            } else {
                deactivateSRSMode();
                prepareNormalStudyCards({ useSavedOrder: true });
                showCard();
                updateNavButtons();
                updateProgress();
            }
        };

        if (srsModeEnabled && window.srsManager && window.srsManager.isReady()) {
            // SRS mode will be activated after flashcard set is loaded
        } else {
            // Ensure SRS mode is deactivated
            deactivateSRSMode();
        }
    }

    function sortSrsSessionQueue(queue, now = new Date()) {
        const dueNow = [];
        const dueFuture = [];

        queue.forEach(card => {
            const isDueNow = !card.srs || !card.srs.due || new Date(card.srs.due) <= now;
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

    let dueSoonTimer = null;

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
                        <button id="due-soon-continue" class="primary-button">
                            <i class="fas fa-play"></i>
                            Review Now (Bypass Wait)
                        </button>
                        <button id="due-soon-finish" class="secondary-button">
                            <i class="fas fa-check-double"></i>
                            Finish Session
                        </button>
                    </div>
                `;
                
                // Re-bind listeners because we replaced innerHTML
                document.getElementById('due-soon-continue').addEventListener('click', () => {
                    if (dueSoonTimer) clearInterval(dueSoonTimer);
                    messageContainer.remove();
                    // Force show the card immediately
                    showCard();
                    updateNavButtons();
                    updateProgress();
                });
                
                document.getElementById('due-soon-finish').addEventListener('click', () => {
                    if (dueSoonTimer) clearInterval(dueSoonTimer);
                    messageContainer.remove();
                    srsSessionComplete = true;
                    showCompletionScreen();
                });
            }
        };

        messageContainer.innerHTML = `<div class="mastered-message-content"></div>`;
        const studyContainer = document.querySelector('.study-container');
        studyContainer.parentNode.insertBefore(messageContainer, studyContainer);
        
        updateText();
        dueSoonTimer = setInterval(() => {
            const diffMs = nextDueTime - Date.now();
            if (diffMs <= 0) {
                clearInterval(dueSoonTimer);
                dueSoonTimer = null;
                messageContainer.remove();
                // Show the card now that it's due
                showCard();
                updateNavButtons();
                updateProgress();
            } else {
                updateText();
            }
        }, 1000);
    }

    // Activate SRS mode
    function activateSRSMode() {
        if (!flashcardSet || !flashcardSet.cards || flashcardSet.cards.length === 0) {
            console.warn('Cannot activate SRS mode: no cards available');
            return false;
        }


        try {
            // Add SRS mode class to study container
            const studyContainer = document.querySelector('.study-container');
            if (studyContainer) {
                studyContainer.classList.add('srs-mode-active');
            }

            // Add SRS mode indicator to header
            const headerRight = document.querySelector('.header-right');
            if (headerRight) {
                let srsIndicator = document.getElementById('srs-mode-indicator');
                if (!srsIndicator) {
                    srsIndicator = document.createElement('div');
                    srsIndicator.id = 'srs-mode-indicator';
                    srsIndicator.className = 'srs-mode-indicator';
                    srsIndicator.innerHTML = '<i class="fas fa-brain"></i><span>SRS Mode</span>';
                    headerRight.insertBefore(srsIndicator, headerRight.firstChild);
                }
            }

            // Ensure all cards have SRS data (only add if missing)
            flashcardSet.cards = flashcardSet.cards.map(card => {
                if (!card.srs && window.srsManager && window.srsManager.isReady()) {
                    return window.srsManager.createSRSCard(card);
                }
                return card;
            });

            // Filter cards for SRS mode
            const allDueCards = window.srsManager.getDueCards(flashcardSet.cards, {
                maxNewCards: getDeckSrsSettings().newCardsPerDay,
                maxDueCards: getDeckSrsSettings().reviewsPerDay,
                allowMultipleSessions: true,
                settings: getDeckSrsSettings()
            });

            // Filter out already reviewed cards in this session
            srsCards = allDueCards.filter(card => !srsReviewedCardIds.has(cardProgressKey(card)));

            // Re-sort the session queue
            srsCards = sortSrsSessionQueue(srsCards);

            if (srsCards.length === 0) {
                showAllCardsMasteredMessage();
                return false;
            }

            srsSessionComplete = false;
            srsSessionStats = {
                reviewed: srsReviewedCardIds.size,
                Again: srsSessionStats.Again || 0,
                Hard: srsSessionStats.Hard || 0,
                Good: srsSessionStats.Good || 0,
                Easy: srsSessionStats.Easy || 0,
                nextDue: srsSessionStats.nextDue || null
            };

            // Add rating interface to the study page
            addRatingInterface();

            // Resume the saved SRS card when it is still due and in the active queue.
            // Move it to index 0 (front of queue) so it is shown first.
            if (srsCurrentCardKey) {
                const keyedIndex = srsCards.findIndex(card => cardProgressKey(card) === srsCurrentCardKey);
                if (keyedIndex > 0) {
                    const resumedCard = srsCards.splice(keyedIndex, 1)[0];
                    srsCards.unshift(resumedCard);
                }
            }

            srsModeCardIndex = 0;
            currentCardIndex = 0;

            // Check if the first card in the queue is in the future
            const firstCardDue = srsCards[0].srs?.due ? new Date(srsCards[0].srs.due).getTime() : 0;
            const diffMs = firstCardDue - Date.now();
            if (diffMs > 0) {
                showLearningCardsDueSoonMessage(srsCards.length, firstCardDue);
            }

            return true;
        } catch (error) {
            console.error('Error activating SRS mode:', error);
            showToast('Error activating SRS mode', 'error');
            return false;
        }
    }

    // Deactivate SRS mode (for when switching back to normal mode)
    function deactivateSRSMode() {

        try {
            // Remove SRS mode class from study container
            const studyContainer = document.querySelector('.study-container');
            if (studyContainer) {
                studyContainer.classList.remove('srs-mode-active');
                studyContainer.classList.remove('rating-visible');
            }

            // Remove SRS mode indicator from header
            const srsIndicator = document.getElementById('srs-mode-indicator');
            if (srsIndicator) {
                srsIndicator.remove();
            }

            // Remove rating interface
            const ratingContainer = document.getElementById('srs-rating-container');
            if (ratingContainer) {
                ratingContainer.remove();
            }

            if (dueSoonTimer) {
                clearInterval(dueSoonTimer);
                dueSoonTimer = null;
            }
            const existingMessage = document.getElementById('mastered-message');
            if (existingMessage) {
                existingMessage.remove();
            }

            // Reset to use all cards and normal mode index
            srsCards = [];
            srsReviewedCardIds.clear();
            srsCurrentCardKey = null;
            currentCardIndex = normalModeCardIndex; // Restore normal mode progress
        } catch (error) {
            console.error('Error deactivating SRS mode:', error);
        }
    }

    // Show rating interface
    function showRatingInterface() {
        if (srsSessionComplete) return;
        const ratingContainer = document.getElementById('srs-rating-container');
        if (ratingContainer) {
            updateRatingIntervals();
            ratingContainer.classList.remove('hidden');
            studyContainer?.classList.add('rating-visible');
        }
    }

    // Hide rating interface
    function hideRatingInterface() {
        const ratingContainer = document.getElementById('srs-rating-container');
        if (ratingContainer) {
            ratingContainer.classList.add('hidden');
        }
        studyContainer?.classList.remove('rating-visible');
    }

    // Add rating interface to the study page
    function addRatingInterface() {
        const existingRatingContainer = document.getElementById('srs-rating-container');
        if (existingRatingContainer) {
            existingRatingContainer.remove();
        }

        // Create rating buttons container
        const ratingContainer = document.createElement('div');
        ratingContainer.id = 'srs-rating-container';
        ratingContainer.className = 'srs-rating-container hidden';
        
        ratingContainer.innerHTML = `
            <div class="srs-rating-header">
                <h3>How well did you know this card?</h3>
            </div>
            <div class="srs-rating-buttons">
                <button class="srs-rating-action-btn srs-undo-btn" id="srs-undo-btn" title="Undo review (Z)" disabled>
                    <i class="fas fa-undo"></i>
                    <span>Undo</span>
                </button>
                <button class="srs-rating-btn again-btn" data-rating="Again">
                    <i class="fas fa-times"></i>
                    <span>Again</span>
                    <small class="rating-shortcut">1</small>
                    <em class="rating-interval">...</em>
                </button>
                <button class="srs-rating-btn hard-btn" data-rating="Hard">
                    <i class="fas fa-minus"></i>
                    <span>Hard</span>
                    <small class="rating-shortcut">2</small>
                    <em class="rating-interval">...</em>
                </button>
                <button class="srs-rating-btn good-btn" data-rating="Good">
                    <i class="fas fa-check"></i>
                    <span>Good</span>
                    <small class="rating-shortcut">3</small>
                    <em class="rating-interval">...</em>
                </button>
                <button class="srs-rating-btn easy-btn" data-rating="Easy">
                    <i class="fas fa-plus"></i>
                    <span>Easy</span>
                    <small class="rating-shortcut">4</small>
                    <em class="rating-interval">...</em>
                </button>
                <div class="srs-actions-dropdown-container">
                    <button class="srs-rating-action-btn srs-actions-btn" id="srs-actions-btn" title="More options">
                        <i class="fas fa-ellipsis-h"></i>
                        <span>More</span>
                    </button>
                    <div class="srs-actions-dropdown-menu hidden" id="srs-actions-menu">
                        <button class="dropdown-item srs-action-bury"><i class="fas fa-eye-slash"></i> Bury Card</button>
                        <button class="dropdown-item srs-action-suspend"><i class="fas fa-pause"></i> Suspend Card</button>
                        <button class="dropdown-item srs-action-reset"><i class="fas fa-rotate-left"></i> Reset Card</button>
                        <button class="dropdown-item srs-action-due"><i class="fas fa-calendar-alt"></i> Set Due Date...</button>
                    </div>
                </div>
            </div>
        `;
        
        // Place rating controls in reserved space below the study area.
        studyArea.parentNode.insertBefore(ratingContainer, studyArea.nextSibling);
        
        // Add event listeners for rating buttons
        const ratingButtons = ratingContainer.querySelectorAll('.srs-rating-btn');
        ratingButtons.forEach(button => {
            button.addEventListener('click', () => {
                if (srsSessionComplete) return;
                const rating = button.dataset.rating;
                handleSRSRating(rating);
            });
        });

        // Add event listeners for Undo and More Actions
        const undoBtn = ratingContainer.querySelector('#srs-undo-btn');
        if (undoBtn) {
            undoBtn.addEventListener('click', () => {
                undoLastReview();
            });
        }

        const actionsBtn = ratingContainer.querySelector('#srs-actions-btn');
        const actionsMenu = ratingContainer.querySelector('#srs-actions-menu');
        if (actionsBtn && actionsMenu) {
            actionsBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                actionsMenu.classList.toggle('hidden');
            });
            // Close dropdown when clicking outside
            document.addEventListener('click', (e) => {
                if (!actionsBtn.contains(e.target) && !actionsMenu.contains(e.target)) {
                    actionsMenu.classList.add('hidden');
                }
            });
        }

        const buryBtn = ratingContainer.querySelector('.srs-action-bury');
        if (buryBtn) buryBtn.addEventListener('click', () => { actionsMenu?.classList.add('hidden'); buryActiveCard(); });

        const suspendBtn = ratingContainer.querySelector('.srs-action-suspend');
        if (suspendBtn) suspendBtn.addEventListener('click', () => { actionsMenu?.classList.add('hidden'); suspendActiveCard(); });

        const resetBtn = ratingContainer.querySelector('.srs-action-reset');
        if (resetBtn) resetBtn.addEventListener('click', () => { actionsMenu?.classList.add('hidden'); resetActiveCard(); });

        const dueBtn = ratingContainer.querySelector('.srs-action-due');
        if (dueBtn) dueBtn.addEventListener('click', () => {
            actionsMenu?.classList.add('hidden');
            const currentCard = srsCards[0];
            if (currentCard) {
                showSrsDateModal(currentCard.id);
            }
        });

        updateUndoButtonState();
    }

    function updateRatingIntervals() {
        const ratingContainer = document.getElementById('srs-rating-container');
        if (!ratingContainer || !window.srsManager || !window.srsManager.isReady()) return;

        const currentCard = srsCards[0];
        if (!currentCard) return;

        const previews = window.srsManager.getRatingPreviews(currentCard, getDeckSrsSettings());
        ratingContainer.querySelectorAll('.srs-rating-btn').forEach(button => {
            const rating = button.dataset.rating;
            const interval = button.querySelector('.rating-interval');
            const preview = previews[rating];

            if (interval) {
                interval.textContent = preview?.intervalLabel || 'soon';
            }
        });
    }

    // Handle SRS rating
    async function handleSRSRating(rating) {
        if (!srsModeEnabled || !window.srsManager || srsSessionComplete) return;

        // Current card in dynamic queue is always at index 0
        const currentCard = srsCards[0];
        if (!currentCard) return;
        
        try {
            let logId = null;
            let updatedCard = null;
            const previousSrs = currentCard.srs ? { ...currentCard.srs } : null;
            const reviewedAt = Date.now();
            
            const updatedCardBase = window.srsManager.reviewCard(currentCard, rating, getDeckSrsSettings());
            
            if (window.flashcardStore?.recordReview) {
                updatedCard = await window.flashcardStore.recordReview({
                    cardId: currentCard.id,
                    rating,
                    previousSrs,
                    nextSrs: updatedCardBase.srs,
                    reviewedAt,
                    elapsedMs: 0,
                    sessionId: studySessionId
                });
                const lastHistory = updatedCard.reviewHistory[updatedCard.reviewHistory.length - 1];
                logId = lastHistory?.id;
            } else {
                // Fallback local memory and saveSet
                const generatedLogId = `log-${currentCard.id}-${reviewedAt}-${Math.random().toString(36).substring(2, 7)}`;
                const newHistoryEntry = {
                    id: generatedLogId,
                    rating,
                    time: reviewedAt,
                    elapsed: 0,
                    sessionId: studySessionId,
                    previousState: previousSrs?.state || 'New',
                    nextState: updatedCardBase.srs?.state || 'New',
                    previousDue: previousSrs?.due || null,
                    nextDue: updatedCardBase.srs?.due || null,
                    previousInterval: previousSrs?.interval || 0,
                    nextInterval: updatedCardBase.srs?.interval || 0,
                    previousStability: previousSrs?.stability || 0,
                    nextStability: updatedCardBase.srs?.stability || 0,
                    previousDifficulty: previousSrs?.difficulty || 0,
                    nextDifficulty: updatedCardBase.srs?.difficulty || 0
                };
                const reviewHistory = Array.isArray(currentCard.reviewHistory) ? [...currentCard.reviewHistory, newHistoryEntry] : [newHistoryEntry];
                updatedCard = {
                    ...currentCard,
                    srs: updatedCardBase.srs,
                    reviewHistory
                };
                
                const setCardIndex = flashcardSet.cards.findIndex(card => sameCard(card, currentCard));
                if (setCardIndex !== -1) {
                    flashcardSet.cards[setCardIndex] = updatedCard;
                    if (flashcardSet.isPremade) {
                        await savePremadeSrsOverlay();
                    } else if (window.flashcardStore?.saveSet) {
                        flashcardSet = await window.flashcardStore.saveSet(flashcardSet);
                    } else {
                        const sets = JSON.parse(localStorage.getItem('flashcardSets') || '[]');
                        const updatedSets = sets.map(set => String(set.id) === String(flashcardSet.id) ? flashcardSet : set);
                        localStorage.setItem('flashcardSets', JSON.stringify(updatedSets));
                    }
                }
                logId = generatedLogId;
            }
            
            // Push undo transaction before changing queue
            pushUndoTransaction('review', currentCard, { logId });

            srsSessionStats[rating] = (srsSessionStats[rating] || 0) + 1;
            srsSessionStats.nextDue = updatedCard.srs?.due || srsSessionStats.nextDue;
            
            // Remove the card from the front of the queue
            srsCards.shift();

            const nextState = updatedCard.srs?.state || 'New';
            const nextDueTime = new Date(updatedCard.srs?.due || 0).getTime();
            const diffMs = nextDueTime - Date.now();

            const SHORT_TERM_LIMIT_MS = 20 * 60 * 1000; // 20 minutes
            const isShortTerm = (nextState === 'Learning' || nextState === 'Relearning') && diffMs < SHORT_TERM_LIMIT_MS;

            if (rating === 'Again' || isShortTerm) {
                // Keep in active session queue
                srsCards.push(updatedCard);
            } else {
                // Successfully reviewed (passed) and graduated/long-term: mark it completed in this session
                srsReviewedCardIds.add(cardProgressKey(currentCard));
            }

            // Re-sort the session queue
            srsCards = sortSrsSessionQueue(srsCards);

            srsSessionStats.reviewed = srsReviewedCardIds.size;
            srsModeCardIndex = 0;
            currentCardIndex = 0;
            srsCurrentCardKey = srsCards[0] ? cardProgressKey(srsCards[0]) : null;

            await saveProgress();

            // Check if session is complete
            if (srsCards.length === 0) {
                hideRatingInterface();
                srsSessionComplete = true;
                await showCompletionScreen();
            } else {
                // Check if the next card is in the future
                const nextCardDue = srsCards[0].srs?.due ? new Date(srsCards[0].srs.due).getTime() : 0;
                const nextDiffMs = nextCardDue - Date.now();
                
                if (nextDiffMs > 0) {
                    hideRatingInterface();
                    showLearningCardsDueSoonMessage(srsCards.length, nextCardDue);
                } else {
                    hideRatingInterface();
                    showCard();
                    updateNavButtons();
                    updateProgress();
                }
            }
            
        } catch (error) {
            console.error('Error processing SRS rating:', error);
            showToast('Error processing rating', 'error');
        }
    }

    // Phased SRS Undo & Actions Helpers
    function pushUndoTransaction(actionType, card, extra = {}) {
        srsUndoStack.push({
            type: actionType,
            cardId: card.id,
            cardStateSnapshot: JSON.parse(JSON.stringify(card)),
            queueSnapshot: JSON.parse(JSON.stringify(srsCards)),
            reviewedIdsSnapshot: Array.from(srsReviewedCardIds),
            sessionStatsSnapshot: { ...srsSessionStats },
            extra
        });
        if (srsUndoStack.length > 10) {
            srsUndoStack.shift();
        }
        updateUndoButtonState();
    }

    function updateUndoButtonState() {
        const undoBtn = document.getElementById('srs-undo-btn');
        if (undoBtn) {
            undoBtn.disabled = srsUndoStack.length === 0;
        }
    }

    async function undoLastReview() {
        if (srsUndoStack.length === 0) return;
        const transaction = srsUndoStack.pop();
        
        try {
            let revertedCard = transaction.cardStateSnapshot;
            if (window.flashcardStore?.undoReviewLog && transaction.type === 'review') {
                const logId = transaction.extra?.logId;
                if (logId) {
                    revertedCard = await window.flashcardStore.undoReviewLog(transaction.cardId, logId);
                }
            } else {
                // Revert local and persist
                const setCardIndex = flashcardSet.cards.findIndex(c => String(c.id) === String(transaction.cardId));
                if (setCardIndex !== -1) {
                    flashcardSet.cards[setCardIndex] = transaction.cardStateSnapshot;
                }
                if (window.flashcardStore?.saveSet) {
                    flashcardSet = await window.flashcardStore.saveSet(flashcardSet);
                } else {
                    const sets = JSON.parse(localStorage.getItem('flashcardSets') || '[]');
                    const updatedSets = sets.map(set => String(set.id) === String(flashcardSet.id) ? flashcardSet : set);
                    localStorage.setItem('flashcardSets', JSON.stringify(updatedSets));
                }
            }

            srsCards = transaction.queueSnapshot;
            const queueIndex = srsCards.findIndex(c => String(c.id) === String(transaction.cardId));
            if (queueIndex !== -1) {
                srsCards[queueIndex] = revertedCard;
            }
            srsReviewedCardIds = new Set(transaction.reviewedIdsSnapshot);
            srsSessionStats = transaction.sessionStatsSnapshot;
            srsSessionComplete = false;
            
            srsModeCardIndex = 0;
            currentCardIndex = 0;
            srsCurrentCardKey = srsCards[0] ? cardProgressKey(srsCards[0]) : null;

            await saveProgress();
            updateUndoButtonState();

            hideRatingInterface();
            const existingMessage = document.getElementById('mastered-message');
            if (existingMessage) {
                existingMessage.remove();
            }
            
            const firstCardDue = srsCards[0]?.srs?.due ? new Date(srsCards[0].srs.due).getTime() : 0;
            const diffMs = firstCardDue - Date.now();
            if (diffMs > 0) {
                showLearningCardsDueSoonMessage(srsCards.length, firstCardDue);
            } else {
                showCard();
                updateNavButtons();
                updateProgress();
            }
            
            showToast('Review undone', 'info');
        } catch (error) {
            console.error('Error undoing review:', error);
            showToast('Failed to undo review', 'error');
        }
    }

    async function updateSingleCardAndPersist(card) {
        const setCardIndex = flashcardSet.cards.findIndex(c => String(c.id) === String(card.id));
        if (setCardIndex !== -1) {
            flashcardSet.cards[setCardIndex] = card;
        }
        if (window.flashcardStore?.saveSet) {
            flashcardSet = await window.flashcardStore.saveSet(flashcardSet);
        } else {
            const sets = JSON.parse(localStorage.getItem('flashcardSets') || '[]');
            const updatedSets = sets.map(set => String(set.id) === String(flashcardSet.id) ? flashcardSet : set);
            localStorage.setItem('flashcardSets', JSON.stringify(updatedSets));
        }
    }

    async function buryActiveCard() {
        const currentCard = srsCards[0];
        if (!currentCard) return;

        const now = new Date();
        const tomorrow = new Date(now.getFullYear(), now.getMonth(), now.getDate() + 1, 4, 0, 0, 0);
        
        pushUndoTransaction('bury', currentCard);

        const updatedCard = {
            ...currentCard,
            buriedUntil: tomorrow.toISOString()
        };

        try {
            await updateSingleCardAndPersist(updatedCard);
            srsCards.shift();
            srsCurrentCardKey = srsCards[0] ? cardProgressKey(srsCards[0]) : null;
            await saveProgress();
            
            showToast('Card buried until tomorrow', 'success');
            handlePostActionTransition();
        } catch (error) {
            console.error('Error burying card:', error);
            showToast('Failed to bury card', 'error');
        }
    }

    async function suspendActiveCard() {
        const currentCard = srsCards[0];
        if (!currentCard) return;

        pushUndoTransaction('suspend', currentCard);

        const updatedCard = {
            ...currentCard,
            suspended: true
        };

        try {
            await updateSingleCardAndPersist(updatedCard);
            srsCards.shift();
            srsCurrentCardKey = srsCards[0] ? cardProgressKey(srsCards[0]) : null;
            await saveProgress();

            showToast('Card suspended', 'success');
            handlePostActionTransition();
        } catch (error) {
            console.error('Error suspending card:', error);
            showToast('Failed to suspend card', 'error');
        }
    }

    async function resetActiveCard() {
        const currentCard = srsCards[0];
        if (!currentCard) return;

        pushUndoTransaction('reset', currentCard);

        const updatedCard = {
            ...currentCard,
            srs: undefined,
            reviewHistory: []
        };

        try {
            await updateSingleCardAndPersist(updatedCard);
            
            const initializedCard = window.srsManager?.createSRSCard ? window.srsManager.createSRSCard(updatedCard) : updatedCard;
            srsCards[0] = initializedCard;
            srsCards = sortSrsSessionQueue(srsCards);
            srsCurrentCardKey = srsCards[0] ? cardProgressKey(srsCards[0]) : null;
            await saveProgress();

            showToast('SRS scheduling reset', 'success');
            
            hideRatingInterface();
            showCard();
            updateNavButtons();
            updateProgress();
        } catch (error) {
            console.error('Error resetting card:', error);
            showToast('Failed to reset card', 'error');
        }
    }

    async function setDueDateActiveCard(dueDateStr) {
        const currentCard = srsCards[0];
        if (!currentCard) return;

        pushUndoTransaction('set_due', currentCard);

        const updatedSrs = currentCard.srs ? {
            ...currentCard.srs,
            due: new Date(dueDateStr).toISOString()
        } : {
            state: 'New',
            due: new Date(dueDateStr).toISOString(),
            interval: 0,
            stability: 0,
            difficulty: 0
        };

        const updatedCard = {
            ...currentCard,
            srs: updatedSrs
        };

        try {
            await updateSingleCardAndPersist(updatedCard);
            
            const isDueNow = new Date(dueDateStr) <= new Date();
            if (isDueNow) {
                srsCards[0] = updatedCard;
                srsCards = sortSrsSessionQueue(srsCards);
            } else {
                srsCards.shift();
            }
            
            srsCurrentCardKey = srsCards[0] ? cardProgressKey(srsCards[0]) : null;
            await saveProgress();

            showToast('Card due date updated', 'success');
            handlePostActionTransition();
        } catch (error) {
            console.error('Error setting due date:', error);
            showToast('Failed to update due date', 'error');
        }
    }

    function handlePostActionTransition() {
        if (srsCards.length === 0) {
            hideRatingInterface();
            srsSessionComplete = true;
            showCompletionScreen();
        } else {
            const firstCardDue = srsCards[0].srs?.due ? new Date(srsCards[0].srs.due).getTime() : 0;
            const diffMs = firstCardDue - Date.now();
            if (diffMs > 0) {
                hideRatingInterface();
                showLearningCardsDueSoonMessage(srsCards.length, firstCardDue);
            } else {
                hideRatingInterface();
                showCard();
                updateNavButtons();
                updateProgress();
            }
        }
    }

    function showSrsDateModal(cardId) {
        const dateModal = document.getElementById('srs-date-modal');
        const dateInput = document.getElementById('srs-due-date-input');
        if (dateModal && dateInput) {
            cardIdForDueDate = cardId;
            const now = new Date();
            const year = now.getFullYear();
            const month = String(now.getMonth() + 1).padStart(2, '0');
            const day = String(now.getDate()).padStart(2, '0');
            dateInput.value = `${year}-${month}-${day}`;
            
            dateModal.classList.remove('hidden');
            dateModal.classList.add('visible');
        }
    }

    function hideSrsDateModal() {
        const dateModal = document.getElementById('srs-date-modal');
        if (dateModal) {
            dateModal.classList.remove('visible');
            setTimeout(() => dateModal.classList.add('hidden'), 300);
        }
        cardIdForDueDate = null;
    }

    async function findNextDueSetId(excludedSetId) {
        if (!reviewDueSession || !window.srsManager || !window.srsManager.isReady()) {
            return null;
        }

        try {
            const sets = window.flashcardStore?.listSets
                ? await window.flashcardStore.listSets()
                : JSON.parse(localStorage.getItem('flashcardSets') || '[]');
            const excluded = String(excludedSetId);

            for (const set of sets || []) {
                if (String(set.id) === excluded) continue;
                if (set.srsSettings?.enabled === false) continue;

                const cards = Array.isArray(set.cards) ? set.cards : [];
                const cardsWithSRS = cards.map(card => {
                    if (!card.srs && window.srsManager && window.srsManager.isReady()) {
                        return window.srsManager.createSRSCard(card);
                    }
                    return card;
                });
                const dueCards = window.srsManager.getDueCards(cardsWithSRS, {
                    maxNewCards: null,
                    maxDueCards: null,
                    allowMultipleSessions: true,
                    settings: getDeckSrsSettings(set)
                });

                if (dueCards.length > 0) {
                    return set.id;
                }
            }
        } catch (error) {
            console.warn('Unable to find the next due set:', error);
        }

        return null;
    }

    // Show completion screen for SRS mode
    async function showCompletionScreen() {
        const nextDueSetId = srsModeEnabled ? await findNextDueSetId(flashcardSet?.id) : null;
        completionScreen.dataset.nextDueSetId = nextDueSetId ? String(nextDueSetId) : '';

        const title = completionScreen.querySelector('.completion-header h2');
        const description = completionScreen.querySelector('.completion-header p');
        const summary = document.getElementById('completion-summary');

        if (closeCompletionBtn) {
            closeCompletionBtn.style.display = srsModeEnabled ? 'none' : '';
        }

        if (srsModeEnabled && reviewDueSession && nextDueSetId) {
            if (title) title.textContent = 'Set Complete';
            if (description) description.textContent = 'More due cards are ready in another set.';
            practiceAgainBtn.innerHTML = '<i class="fas fa-arrow-right"></i> Continue Review';
        } else if (srsModeEnabled) {
            if (title) title.textContent = 'SRS Complete';
            if (description) description.textContent = 'You are caught up for this set.';
            practiceAgainBtn.innerHTML = '<i class="fas fa-redo"></i> Check Again';
        } else {
            if (title) title.textContent = 'Congratulations!';
            if (description) description.textContent = "You've completed this set!";
            practiceAgainBtn.innerHTML = '<i class="fas fa-redo"></i> Practice Again';
        }

        if (summary) {
            if (srsModeEnabled) {
                const nextDueLabel = srsSessionStats.nextDue && window.srsManager?.formatIntervalLabel
                    ? window.srsManager.formatIntervalLabel(srsSessionStats.nextDue)
                    : 'Later';
                summary.innerHTML = `
                    <span>${srsSessionStats.reviewed}<small>Reviewed</small></span>
                    <span>${srsSessionStats.Again}/${srsSessionStats.Hard}/${srsSessionStats.Good}/${srsSessionStats.Easy}<small>Again Hard Good Easy</small></span>
                    <span>${nextDueLabel}<small>Next Due</small></span>
                `;
                summary.classList.remove('hidden');
            } else {
                summary.classList.add('hidden');
                summary.innerHTML = '';
            }
        }

        completionScreen.classList.remove('hidden');
        completionScreen.classList.add('visible');
        showToast(nextDueSetId ? 'Set complete. More reviews are waiting.' : 'SRS session completed!', 'success');

        // Play success sound
        successSound.play().catch(error => {
            console.error('Error playing success sound:', error);
        });
    }

    // Show message when all cards are mastered
    function showAllCardsMasteredMessage() {
        const existingMessage = document.getElementById('mastered-message');
        if (existingMessage) {
            existingMessage.remove();
        }

        const messageContainer = document.createElement('div');
        messageContainer.id = 'mastered-message';
        messageContainer.className = 'mastered-message-container';
        messageContainer.innerHTML = `
            <div class="mastered-message-content">
                <div class="mastered-icon">
                    <i class="fas fa-trophy"></i>
                </div>
                <h2>No Cards Due</h2>
                <p>You are caught up for this set.</p>
                <p>Your next review will be available when cards become due.</p>
                <div class="mastered-actions">
                    <button id="mastered-study-again" class="primary-button">
                        <i class="fas fa-redo"></i>
                        Check Again
                    </button>
                    <button id="mastered-go-home" class="secondary-button">
                        <i class="fas fa-home"></i>
                        Back to Library
                    </button>
                </div>
            </div>
        `;

        // Insert before the study container
        const studyContainer = document.querySelector('.study-container');
        studyContainer.parentNode.insertBefore(messageContainer, studyContainer);

        // Add event listeners
        const studyAgainBtn = document.getElementById('mastered-study-again');
        const goHomeBtn = document.getElementById('mastered-go-home');

        studyAgainBtn.addEventListener('click', () => {
            messageContainer.remove();
            // Reactivate SRS mode to show cards again
            if (srsModeEnabled && window.srsManager && window.srsManager.isReady()) {
                srsReviewedCardIds.clear();
                srsCurrentCardKey = null;
                if (activateSRSMode()) {
                    showCard();
                    updateNavButtons();
                    updateProgress();
                }
            }
        });

        goHomeBtn.addEventListener('click', async () => {
            if (window.flashcardStore?.removeState) {
                await window.flashcardStore.removeState(STORAGE_KEY);
            } else {
                localStorage.removeItem(STORAGE_KEY);
            }
            goToLibrary(false);
        });
    }

    // Initialize
    await initializeSRS();
    await loadFlashcardSet();
});
