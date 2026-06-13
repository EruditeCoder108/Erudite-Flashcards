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
    const shuffleModeBtn = document.getElementById('shuffle-mode-btn');

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
    let shuffleMode = pageParams.get('shuffle') === 'true';
    let normalOrder = [];
    let normalStudyCards = [];
    let restoredProgress = null;

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

    function isValidOrder(order, length) {
        if (!Array.isArray(order) || order.length !== length) return false;
        const seen = new Set(order.map(Number));
        return seen.size === length && [...seen].every(index => Number.isInteger(index) && index >= 0 && index < length);
    }

    function prepareNormalStudyCards(options = {}) {
        const cards = Array.isArray(flashcardSet?.cards) ? flashcardSet.cards : [];
        if (!cards.length) {
            normalOrder = [];
            normalStudyCards = [];
            normalModeCardIndex = 0;
            return;
        }

        if (shuffleMode) {
            const savedOrder = options.useSavedOrder && isValidOrder(restoredProgress?.normalOrder, cards.length)
                ? restoredProgress.normalOrder.map(Number)
                : null;
            normalOrder = savedOrder || shuffledIndices(cards.length);
        } else {
            normalOrder = Array.from({ length: cards.length }, (_, index) => index);
        }

        normalStudyCards = normalOrder.map(index => cards[index]).filter(Boolean);
        normalModeCardIndex = clampIndex(normalModeCardIndex, normalStudyCards.length || 1);
    }

    function updateShuffleButton() {
        if (!shuffleModeBtn) return;
        shuffleModeBtn.classList.toggle('active', shuffleMode);
        shuffleModeBtn.setAttribute('aria-pressed', String(shuffleMode));
        shuffleModeBtn.style.display = srsModeEnabled ? 'none' : 'inline-flex';
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
                if (!pageParams.has('shuffle')) {
                    shuffleMode = Boolean(savedProgress.shuffleMode);
                }
                const legacyIndex = savedProgress.cardIndex ?? 0;
                normalModeCardIndex = clampIndex(
                    savedProgress.normalModeIndex ?? legacyIndex,
                    flashcardSet?.cards?.length || 1
                );
                srsModeCardIndex = clampIndex(
                    savedProgress.srsModeIndex ?? 0,
                    savedProgress.srsModeLength || flashcardSet?.cards?.length || 1
                );
                srsCurrentCardKey = savedProgress.srsCurrentCardKey || null;
                currentCardIndex = srsModeEnabled ? srsModeCardIndex : normalModeCardIndex;
                updateShuffleButton();
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

            const currentSrsCard = srsCards[srsModeCardIndex] || null;
            if (srsModeEnabled) {
                srsCurrentCardKey = currentSrsCard ? cardProgressKey(currentSrsCard) : null;
            }

            const progress = {
                setId: progressId,
                cardIndex: currentCardIndex, // Keep for compatibility
                normalModeIndex: normalModeCardIndex,
                normalModeLength: normalStudyCards.length || flashcardSet.cards.length,
                shuffleMode,
                normalOrder,
                srsModeIndex: srsModeCardIndex,
                srsModeLength: srsCards.length,
                srsCurrentCardKey,
                timestamp: Date.now()
            };

            if (window.flashcardStore?.saveProgress) {
                await window.flashcardStore.saveProgress(progressId, progress);
            } else {
                localStorage.setItem(STORAGE_KEY, JSON.stringify(progress));
            }

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
            backgroundEl.classList.remove('visible');
            backgroundEl.style.backgroundImage = '';
            return;
        }
        backgroundEl.style.backgroundImage = `url("${background.src}")`;
        backgroundEl.style.backgroundSize = background.fit || 'cover';
        backgroundEl.style.setProperty('--card-bg-opacity', String(background.opacity ?? 0.32));
        backgroundEl.classList.add('visible');
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
        updateShuffleButton();

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

    if (shuffleModeBtn) {
        shuffleModeBtn.addEventListener('click', () => {
            if (srsModeEnabled) return;
            shuffleMode = !shuffleMode;
            normalModeCardIndex = 0;
            prepareNormalStudyCards({ useSavedOrder: false });
            updateShuffleButton();
            showCard();
            updateProgress();
            saveProgress();
            showToast(shuffleMode ? 'Shuffle mode on' : 'Shuffle mode off', 'info');
        });
    }

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
    
    // Close image modal with escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && !imageModal.classList.contains('hidden')) {
            closeImageModal();
        }
    });

    // SRS Initialization
    async function initializeSRS() {
        const savedSRSMode = window.flashcardStore?.getState
            ? await window.flashcardStore.getState('srsModeEnabled')
            : localStorage.getItem('srsModeEnabled');
        srsModeEnabled = savedSRSMode === true || savedSRSMode === 'true';
        studyContainer?.classList.toggle('srs-mode-active', srsModeEnabled);
        updateShuffleButton();

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
            updateShuffleButton();
        };

        if (srsModeEnabled && window.srsManager && window.srsManager.isReady()) {
            // SRS mode will be activated after flashcard set is loaded
        } else {
            // Ensure SRS mode is deactivated
            deactivateSRSMode();
        }
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

            // Filter cards for SRS mode (no daily limits - show all due cards)
            srsCards = window.srsManager.getDueCards(flashcardSet.cards, {
                maxNewCards: getDeckSrsSettings().newCardsPerDay,
                maxDueCards: getDeckSrsSettings().reviewsPerDay,
                allowMultipleSessions: true,
                settings: getDeckSrsSettings()
            });

            if (srsCards.length === 0) {
                showAllCardsMasteredMessage();
                return false;
            }

            srsSessionComplete = false;
            srsSessionStats = { reviewed: 0, Again: 0, Hard: 0, Good: 0, Easy: 0, nextDue: null };

            // Add rating interface to the study page
            addRatingInterface();

            // Resume the saved SRS card when it is still due. If it was already rated
            // and dropped out of the due list, start at the first remaining due card.
            const keyedIndex = srsCurrentCardKey
                ? srsCards.findIndex(card => cardProgressKey(card) === srsCurrentCardKey)
                : -1;

            if (keyedIndex >= 0) {
                srsModeCardIndex = keyedIndex;
            } else {
                srsModeCardIndex = 0;
            }

            currentCardIndex = srsModeCardIndex;
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

            // Reset to use all cards and normal mode index
            srsCards = [];
            currentCardIndex = normalModeCardIndex; // Restore normal mode progress
        } catch (error) {
            console.error('Error deactivating SRS mode:', error);
        }
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
    }

    function updateRatingIntervals() {
        const ratingContainer = document.getElementById('srs-rating-container');
        if (!ratingContainer || !window.srsManager || !window.srsManager.isReady()) return;

        const currentCard = srsCards[currentCardIndex];
        if (!currentCard) return;

        const previews = window.srsManager.getRatingPreviews(currentCard, getDeckSrsSettings());
        ratingContainer.querySelectorAll('.srs-rating-btn').forEach(button => {
            const rating = button.dataset.rating;
            const interval = button.querySelector('.rating-interval');
            const preview = previews[rating];

            if (interval) {
                interval.textContent = preview?.intervalLabel || 'soon';
            }

            if (preview?.due) {
                button.title = `${rating}: next review ${preview.intervalLabel}`;
            }
        });
    }

    // Handle SRS rating
    async function handleSRSRating(rating) {
        if (!srsModeEnabled || !window.srsManager || srsSessionComplete) return;

        // Check bounds
        if (currentCardIndex < 0 || currentCardIndex >= srsCards.length) {
            console.error('Invalid card index in SRS rating:', currentCardIndex);
            return;
        }

        const currentCard = srsCards[currentCardIndex];
        if (!currentCard) return;
        
        
        try {
            const previousState = currentCard.srs ? { ...currentCard.srs } : null;
            const reviewedAt = new Date().toISOString();
            const updatedCardBase = window.srsManager.reviewCard(currentCard, rating, getDeckSrsSettings());
            const updatedCard = {
                ...updatedCardBase,
                reviewHistory: [
                    ...(Array.isArray(currentCard.reviewHistory) ? currentCard.reviewHistory : []),
                    {
                        reviewedAt,
                        rating,
                        previousState: previousState?.state || 'New',
                        nextState: updatedCardBase.srs?.state || null,
                        previousDue: previousState?.due || null,
                        nextDue: updatedCardBase.srs?.due || null
                    }
                ]
            };
            
            const cardIndex = flashcardSet.cards.findIndex(card => sameCard(card, currentCard));
            
            if (cardIndex !== -1) {
                flashcardSet.cards[cardIndex] = updatedCard;

                // Update the card in srsCards array as well
                const srsCardIndex = srsCards.findIndex(card => sameCard(card, currentCard));
                if (srsCardIndex !== -1) {
                    srsCards[srsCardIndex] = updatedCard;
                }

                if (flashcardSet.isPremade) {
                    await savePremadeSrsOverlay();
                } else if (window.flashcardStore?.saveSet) {
                    flashcardSet = await window.flashcardStore.saveSet(flashcardSet);
                } else if (!flashcardSet.isPremade) {
                    const sets = JSON.parse(localStorage.getItem('flashcardSets') || '[]');
                    const updatedSets = sets.map(set => String(set.id) === String(flashcardSet.id) ? flashcardSet : set);
                    localStorage.setItem('flashcardSets', JSON.stringify(updatedSets));
                }

                srsSessionStats.reviewed += 1;
                srsSessionStats[rating] = (srsSessionStats[rating] || 0) + 1;
                srsSessionStats.nextDue = updatedCard.srs?.due || srsSessionStats.nextDue;
            } else {
                console.error('Could not find card in original set to update SRS data');
            }
            
            // Move to next card in SRS mode
            srsModeCardIndex++;
            currentCardIndex = srsModeCardIndex;
            await saveProgress();

            // Check if session is complete
            if (srsModeCardIndex >= srsCards.length) {
                hideRatingInterface();
                srsSessionComplete = true;
                await showCompletionScreen();
            } else {
                // Hide rating interface and show next card
                hideRatingInterface();
                showCard();
                updateNavButtons();
                updateProgress();
            }
            
        } catch (error) {
            console.error('Error processing SRS rating:', error);
            showToast('Error processing rating', 'error');
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
