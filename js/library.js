document.addEventListener('DOMContentLoaded', async () => {
    if (window.flashcardLocalReady) await window.flashcardLocalReady;
    // DOM Elements
    const setsContainer = document.getElementById('sets-container');
    const setTemplate = document.getElementById('set-template');
    const emptyState = document.getElementById('empty-state');
    const searchInput = document.getElementById('search-input');
    const sortSelect = document.getElementById('sort-select');
    const libraryViewTabs = document.querySelectorAll('.library-view-tab');
    const deleteModal = document.getElementById('delete-modal');
    const importModal = document.getElementById('import-modal');
    const settingsModal = document.getElementById('settings-modal');
    const totalSetsDisplay = document.getElementById('total-sets');
    const recentActivityDisplay = document.getElementById('recent-activity');
    const cancelDeleteBtn = document.getElementById('cancel-delete');
    const confirmDeleteBtn = document.getElementById('confirm-delete');
    const importSetBtn = document.getElementById('import-set-btn');
    const cardBrowserBtn = document.getElementById('card-browser-btn');
    const reviewDueBtn = document.getElementById('review-due-btn');
    const librarySubtitle = document.getElementById('library-subtitle');
    const closeImportBtn = document.getElementById('close-import-btn');
    const cancelImportBtn = document.getElementById('cancel-import');
    const confirmImportBtn = document.getElementById('confirm-import');
    const importContentTextarea = document.getElementById('import-content');
    const importSetNameInput = document.getElementById('import-set-name');
    const importClassSelect = document.getElementById('import-class-select');
    const previewCardsContainer = document.getElementById('preview-cards');
    const previewCountSpan = document.getElementById('preview-count');
    const settingsBtn = document.getElementById('settings-btn');
    const closeSettingsBtn = document.getElementById('close-settings-btn');
    const saveSettingsBtn = document.getElementById('save-settings');
    const resetSettingsBtn = document.getElementById('reset-settings');
    const appThemeSelect = document.getElementById('app-theme');
    const normalStudyOrderSelect = document.getElementById('normal-study-order');
    const exportBackupBtn = document.getElementById('export-backup');
    const restoreBackupBtn = document.getElementById('restore-backup');
    const exportCsvBtn = document.getElementById('export-csv');
    const exportTsvBtn = document.getElementById('export-tsv');
    const importDelimitedBtn = document.getElementById('import-delimited');
    const contentFontSelect = document.getElementById('content-font');
    const customContentFontDiv = document.getElementById('custom-content-font');
    const contentFontUpload = document.getElementById('content-font-upload');
    const cardBgOpacitySlider = document.getElementById('card-bg-opacity');
    const cardBgOpacityLabel = document.getElementById('card-bg-opacity-label');
    const copyPasteExportBtn = document.getElementById('copy-paste-export-btn');
    const copyPasteImportBtn = document.getElementById('copy-paste-import-btn');
    // Copy-paste export modal
    const copyPasteExportModal = document.getElementById('copy-paste-export-modal');
    const closeCopyExportBtn = document.getElementById('close-copy-export-btn');
    const cancelCopyExportBtn = document.getElementById('cancel-copy-export');
    const generateCopyExportBtn = document.getElementById('generate-copy-export');
    const doCopyExportBtn = document.getElementById('do-copy-export');
    const copyExportDeckSelect = document.getElementById('copy-export-deck-select');
    const copyExportTermSep = document.getElementById('copy-export-term-sep');
    const copyExportCardSep = document.getElementById('copy-export-card-sep');
    const copyExportTextArea = document.getElementById('copy-export-text-area');
    // Import separator inputs
    const importTermSepInput = document.getElementById('import-term-sep');
    const importCardSepInput = document.getElementById('import-card-sep');
    const deckSettingsModal = document.getElementById('deck-settings-modal');
    const closeDeckSettingsBtn = document.getElementById('close-deck-settings');
    const deckSettingsName = document.getElementById('deck-settings-name');
    const deckSrsEnabled = document.getElementById('deck-srs-enabled');
    const deckRequestRetention = document.getElementById('deck-request-retention');
    const deckMaxInterval = document.getElementById('deck-max-interval');
    const deckNewLimit = document.getElementById('deck-new-limit');
    const deckReviewLimit = document.getElementById('deck-review-limit');
    const cancelDeckSettingsBtn = document.getElementById('cancel-deck-settings');
    const saveDeckSettingsBtn = document.getElementById('save-deck-settings');
    const classModal = document.getElementById('class-modal');
    const closeClassModalBtn = document.getElementById('close-class-modal');
    const classModalTitle = document.getElementById('class-modal-title');
    const classNameInput = document.getElementById('class-name-input');
    const classColorInput = document.getElementById('class-color-input');
    const deleteClassBtn = document.getElementById('delete-class-btn');
    const cancelClassBtn = document.getElementById('cancel-class');
    const saveClassBtn = document.getElementById('save-class');
    
    // Premade flashcards elements
    const flashcardTypeRadios = document.querySelectorAll('input[name="flashcard-type"]');
    const subjectModal = document.getElementById('subject-modal');
    const topicModal = document.getElementById('topic-modal');
    const closeSubjectBtn = document.getElementById('close-subject-btn');
    const closeTopicBtn = document.getElementById('close-topic-btn');
    const backToSubjectBtn = document.getElementById('back-to-subject-btn');
    const subjectsContainer = document.getElementById('subjects-container');
    const topicsContainer = document.getElementById('topics-container');
    const selectedSubjectName = document.getElementById('selected-subject-name');
    
    // SRS elements
    const srsToggle = document.getElementById('srs-mode-toggle');
    const srsStatus = document.getElementById('srs-status');
    const dueCardsDisplay = document.getElementById('due-cards');
    const srsDashboard = document.getElementById('srs-dashboard');
    const srsNewCount = document.getElementById('srs-new-count');
    const srsLearningCount = document.getElementById('srs-learning-count');
    const srsReviewCount = document.getElementById('srs-review-count');
    const srsMatureCount = document.getElementById('srs-mature-count');
    const srsRetention = document.getElementById('srs-retention');
    const srsNextDue = document.getElementById('srs-next-due');

    // State
    const DEFAULT_SRS_SETTINGS = {
        enabled: true,
        requestRetention: 0.9,
        maxIntervalDays: 36500,
        newCardsPerDay: null,
        reviewsPerDay: null
    };

    let flashcardSets = [];
    let flashcardClasses = [];
    let setToDelete = null;
    let setForDeckSettings = null;
    let classForEditor = null;
    let classSelectTarget = null;
    let currentLibraryView = 'all';
    let selectedClassId = null;
    let parsedImportCards = [];
    let customFonts = {
        content: null
    };
    
    // Premade flashcards state
    let currentFlashcardType = 'my-flashcards'; // 'my-flashcards' or 'premade-flashcards'
    let selectedSubject = null;
    let firstDueSetId = null;
    
    // SRS state
    let srsModeEnabled = false; // Stored in Electron state.json; localStorage is fallback only.
    const clickSound = new Audio('assets/flashcard-assets/click.mp3');
    clickSound.volume = 0.3;

    function playClickSound() {
        clickSound.currentTime = 0;
        clickSound.play().catch(() => {});
    }

    function normalizeClassRecord(classData = {}) {
        const now = Date.now();
        return {
            id: classData.id || `class-${now}`,
            name: String(classData.name || 'Untitled Class').trim() || 'Untitled Class',
            color: /^#[0-9a-f]{6}$/i.test(String(classData.color || '')) ? classData.color : '#3B82F6',
            icon: classData.icon || 'fa-graduation-cap',
            created: classData.created || now,
            lastModified: classData.lastModified || now
        };
    }

    function getClassIcon(classId) {
        return getClassById(classId)?.icon || 'fa-layer-group';
    }

    function getClassById(classId) {
        if (!classId) return null;
        return flashcardClasses.find(classItem => String(classItem.id) === String(classId)) || null;
    }

    function getClassLabel(classId) {
        return getClassById(classId)?.name || 'General';
    }

    function getClassColor(classId) {
        return getClassById(classId)?.color || '#64748B';
    }

    async function reloadLibraryData() {
        const [sets, classes] = await Promise.all([
            window.flashcardStore?.listSets
                ? window.flashcardStore.listSets()
                : Promise.resolve(JSON.parse(localStorage.getItem('flashcardSets') || '[]')),
            window.flashcardStore?.listClasses
                ? window.flashcardStore.listClasses()
                : Promise.resolve(JSON.parse(localStorage.getItem('flashcardClasses') || '[]'))
        ]);

        flashcardSets = Array.isArray(sets) ? sets.map(set => ({ ...set, classId: set.classId ?? null })) : [];
        flashcardClasses = Array.isArray(classes) ? classes.map(normalizeClassRecord) : [];
        syncLocalMirror();
        if (!window.eruditeFlashcards) {
            localStorage.setItem('flashcardClasses', JSON.stringify(flashcardClasses));
        }
        populateClassSelect(importClassSelect);
    }

    function populateClassSelect(selectElement, selectedValue = '') {
        if (!selectElement) return;
        const valueToSelect = selectedValue ?? selectElement.value ?? '';
        selectElement.innerHTML = '<option value="">General</option>';
        flashcardClasses.forEach(classItem => {
            const option = document.createElement('option');
            option.value = classItem.id;
            option.textContent = classItem.name;
            selectElement.appendChild(option);
        });
        const newOption = document.createElement('option');
        newOption.value = '__new';
        newOption.textContent = '+ New Class';
        selectElement.appendChild(newOption);
        const finalValue = [...selectElement.options].some(option => option.value === valueToSelect) ? valueToSelect : '';
        selectElement.value = finalValue;

        if (selectElement.id === 'import-class-select') {
            const editBtn = document.getElementById('edit-import-class-btn');
            if (editBtn) {
                editBtn.style.display = (finalValue && finalValue !== '__new') ? 'inline-flex' : 'none';
            }
        }
    }

    let premadeSubjects = [
        {
            id: 'biology',
            name: 'Biology',
            icon: 'fas fa-dna',
            description: 'Study life sciences and living organisms',
            topics: [
                { id: 'botany-neet', name: 'Botany #NEET UG', description: 'Plant biology for NEET UG exam', tags: ['NEET UG', 'Botany'] },
                { id: 'morphologyoffloweringplants-neet', name: 'Morphology of Flowering Plants #NEET UG', description: 'Comprehensive study of flowering plant morphology covering roots, stems, leaves, flowers, and fruits', tags: ['NEET UG', 'Botany', 'Morphology', 'Flowering Plants'] },
                { id: 'anatomyoffloweringplants-neet', name: 'Anatomy of Flowering Plants #NEET UG', description: 'Comprehensive study of flowering plant anatomy covering tissues, organs, and structural adaptations', tags: ['NEET UG', 'Botany', 'Anatomy', 'Plant Tissues'] },
                { id: 'completeecology-neet', name: 'Complete Ecology #NEET UG', description: 'Comprehensive study of ecology covering all concepts from organism to biosphere level', tags: ['NEET UG', 'Botany', 'Ecology', 'Environmental Biology'] },
                { id: 'allbotanyexamplesexceptecology-neet', name: 'All Botany Examples Except Ecology #NEET UG', description: 'Comprehensive botany examples covering all topics except ecology for NEET UG', tags: ['NEET UG', 'Botany', 'Examples', 'Comprehensive'] },
                { id: 'zoology-neet', name: 'Zoology #NEET UG', description: 'Animal biology for NEET UG exam', tags: ['NEET UG', 'Zoology'] },
                { id: 'botany-cuet', name: 'Botany #CUET', description: 'Plant biology for CUET exam', tags: ['CUET', 'Botany'] },
                { id: 'biology-10th', name: 'Biology #10th Grade', description: 'Basic biology concepts for 10th grade', tags: ['10th Grade', 'Basic'] }
            ]
        },
        {
            id: 'chemistry',
            name: 'Chemistry',
            icon: 'fas fa-flask',
            description: 'Study matter, its properties, and reactions',
            topics: [
                { id: 'organic-neet', name: 'Organic Chemistry #NEET UG', description: 'Organic compounds and reactions for NEET UG', tags: ['NEET UG', 'Organic'] },
                { id: 'inorganic-neet', name: 'Inorganic Chemistry #NEET UG', description: 'Inorganic compounds for NEET UG', tags: ['NEET UG', 'Inorganic'] },
                { id: 'physical-neet', name: 'Physical Chemistry #NEET UG', description: 'Physical principles in chemistry for NEET UG', tags: ['NEET UG', 'Physical'] },
                { id: 'chemistry-10th', name: 'Chemistry #10th Grade', description: 'Basic chemistry concepts for 10th grade', tags: ['10th Grade', 'Basic'] }
            ]
        },
        {
            id: 'physics',
            name: 'Physics',
            icon: 'fas fa-atom',
            description: 'Study matter, energy, and their interactions',
            topics: [
                { id: 'mechanics-neet', name: 'Mechanics #NEET UG', description: 'Motion, forces, and energy for NEET UG', tags: ['NEET UG', 'Mechanics'] },
                { id: 'thermodynamics-neet', name: 'Thermodynamics #NEET UG', description: 'Heat and energy transfer for NEET UG', tags: ['NEET UG', 'Thermodynamics'] },
                { id: 'optics-neet', name: 'Optics #NEET UG', description: 'Light and optical phenomena for NEET UG', tags: ['NEET UG', 'Optics'] },
                { id: 'physics-10th', name: 'Physics #10th Grade', description: 'Basic physics concepts for 10th grade', tags: ['10th Grade', 'Basic'] }
            ]
        },
        {
            id: 'mathematics',
            name: 'Mathematics',
            icon: 'fas fa-calculator',
            description: 'Study numbers, shapes, and patterns',
            topics: [
                { id: 'algebra-jee', name: 'Algebra #JEE Mains', description: 'Algebraic concepts for JEE Mains', tags: ['JEE Mains', 'Algebra'] },
                { id: 'calculus-jee', name: 'Calculus #JEE Mains', description: 'Differential and integral calculus for JEE Mains', tags: ['JEE Mains', 'Calculus'] },
                { id: 'geometry-jee', name: 'Geometry #JEE Mains', description: 'Geometric shapes and properties for JEE Mains', tags: ['JEE Mains', 'Geometry'] },
                { id: 'math-10th', name: 'Mathematics #10th Grade', description: 'Basic math concepts for 10th grade', tags: ['10th Grade', 'Basic'] }
            ]
        },
        {
            id: 'english',
            name: 'English',
            icon: 'fas fa-language',
            description: 'Study language, literature, and communication',
            topics: [
                { id: 'grammar-cuet', name: 'Grammar #CUET', description: 'English grammar for CUET exam', tags: ['CUET', 'Grammar'] },
                { id: 'vocabulary-cuet', name: 'Vocabulary #CUET', description: 'English vocabulary for CUET exam', tags: ['CUET', 'Vocabulary'] },
                { id: 'literature-cuet', name: 'Literature #CUET', description: 'English literature for CUET exam', tags: ['CUET', 'Literature'] },
                { id: 'english-10th', name: 'English #10th Grade', description: 'Basic English concepts for 10th grade', tags: ['10th Grade', 'Basic'] }
            ]
        }
    ];

    // Show loading indicator in sets container
    function showLoadingIndicator(message = 'Loading flashcards...') {
        if (setsContainer) {
            setsContainer.innerHTML = `
                <div class="loading-indicator" style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 80px 20px; color: rgba(255, 255, 255, 0.7);">
                    <div class="loading-spinner" style="width: 50px; height: 50px; border: 4px solid rgba(255, 255, 255, 0.1); border-top-color: #667eea; border-radius: 50%; animation: spin 1s linear infinite;"></div>
                    <p style="margin-top: 24px; font-size: 18px; font-weight: 500;">${message}</p>
                    <p style="margin-top: 8px; font-size: 14px; opacity: 0.6;">Reading your local library</p>
                </div>
            `;
        }
    }

    function normalizeSrsSettings(settings = {}) {
        const numberOrNull = (value) => {
            if (value === null || value === undefined || value === '') return null;
            const numeric = Number(value);
            return Number.isFinite(numeric) && numeric >= 0 ? numeric : null;
        };

        return {
            ...DEFAULT_SRS_SETTINGS,
            ...settings,
            enabled: settings.enabled !== false,
            requestRetention: Number.isFinite(Number(settings.requestRetention))
                ? Math.min(0.99, Math.max(0.7, Number(settings.requestRetention)))
                : DEFAULT_SRS_SETTINGS.requestRetention,
            maxIntervalDays: Number.isFinite(Number(settings.maxIntervalDays))
                ? Math.max(1, Math.round(Number(settings.maxIntervalDays)))
                : DEFAULT_SRS_SETTINGS.maxIntervalDays,
            newCardsPerDay: numberOrNull(settings.newCardsPerDay),
            reviewsPerDay: numberOrNull(settings.reviewsPerDay)
        };
    }

    function syncLocalMirror(sets = flashcardSets) {
        if (window.eruditeFlashcards) return;
        localStorage.setItem('flashcardSets', JSON.stringify(sets));
    }

    // Load flashcard sets
    async function loadFlashcardSets() {
        showLoadingIndicator('Loading your flashcards...');
        
        try {
            await reloadLibraryData();

            // Ensure sets are unique by ID
            const uniqueSets = [];
            const seenIds = new Set();

            for (const set of flashcardSets) {
                if (!seenIds.has(set.id)) {
                    seenIds.add(set.id);
                    uniqueSets.push(set);
                }
            }

            flashcardSets = uniqueSets.map(set => {
                set.srsSettings = normalizeSrsSettings(set.srsSettings);
                if (set.cards && Array.isArray(set.cards)) {
                    set.cards = set.cards.map(card => {
                        if (!card.srs && window.srsManager && window.srsManager.isReady()) {
                            return window.srsManager.createSRSCard(card);
                        }
                        return card;
                    });
                }
                return set;
            });

            syncLocalMirror();
            if (!window.eruditeFlashcards) {
                localStorage.setItem('flashcardClasses', JSON.stringify(flashcardClasses));
            }

            updateLibraryStats();
            renderSets();
        } catch (error) {
            console.error('Error loading flashcard sets:', error);
            showToast('Error loading flashcard sets', 'error');
        }
    }

    // Update library statistics
    function updateLibraryStats() {
        totalSetsDisplay.textContent = flashcardSets.length;
        
        const recentActivity = flashcardSets.reduce((count, set) => {
            const lastWeek = Date.now() - (7 * 24 * 60 * 60 * 1000);
            return count + (set.lastOpened > lastWeek ? 1 : 0);
        }, 0);
        
        recentActivityDisplay.textContent = recentActivity;
        // Update due cards count
        updateDueCardsCount();
    }

    function updateLibrarySubtitle(dueCount = null) {
        if (!librarySubtitle) return;
        const recentActivity = recentActivityDisplay ? recentActivityDisplay.textContent || '0' : '0';
        librarySubtitle.textContent = srsModeEnabled && dueCount !== null
            ? `${flashcardSets.length} sets | ${dueCount} due | ${recentActivity} recent`
            : `${flashcardSets.length} sets | ${recentActivity} recent`;
    }

    // Render flashcard sets
    function renderSets(searchTerm = '') {
        const filteredSets = filterSets(searchTerm);
        const sortedSets = sortSets(filteredSets);
        setsContainer.innerHTML = '';

        if (currentLibraryView === 'classes') {
            renderClassCards(searchTerm);
            return;
        }

        if (sortedSets.length === 0) {
            updateEmptyStateText();
            showEmptyState();
        } else {
            hideEmptyState();
            sortedSets.forEach(set => {
                const card = createSetCard(set);
                setsContainer.appendChild(card);
            });
        }
    }

    function showEmptyState() {
        if (!emptyState) return;
        emptyState.classList.remove('hidden');
        emptyState.style.display = 'flex';
        setsContainer.appendChild(emptyState);
    }

    function hideEmptyState() {
        if (!emptyState) return;
        emptyState.style.display = 'none';
        emptyState.classList.add('hidden');
    }

    function updateEmptyStateText() {
        const heading = emptyState?.querySelector('h2');
        const description = emptyState?.querySelector('p');
        if (!heading || !description) return;

        if (selectedClassId) {
            heading.textContent = `No Sets in ${getClassLabel(selectedClassId)}`;
            description.textContent = 'Create or edit a set to add it to this class.';
        } else if (currentLibraryView === 'general') {
            heading.textContent = 'No General Sets';
            description.textContent = 'Sets without a class will appear here.';
        } else {
            heading.textContent = 'No Flashcard Sets Yet';
            description.textContent = 'Create your first set to start studying!';
        }
    }

    function renderClassCards(searchTerm = '') {
        const term = String(searchTerm || '').trim().toLowerCase();
        const classesToShow = flashcardClasses.filter(classItem => {
            if (!term) return true;
            const classSets = flashcardSets.filter(set => String(set.classId || '') === String(classItem.id));
            return classItem.name.toLowerCase().includes(term) ||
                classSets.some(set => String(set.name || '').toLowerCase().includes(term));
        });

        if (classesToShow.length === 0 && term) {
            const heading = emptyState.querySelector('h2');
            const description = emptyState.querySelector('p');
            if (heading) heading.textContent = 'No Classes Found';
            if (description) description.textContent = 'Try adjusting your search term.';
            showEmptyState();
            return;
        }

        hideEmptyState();

        if (!term) {
            setsContainer.appendChild(createAddClassCard());
        }

        classesToShow.forEach(classItem => {
            setsContainer.appendChild(createClassCard(classItem));
        });
    }

    function createAddClassCard() {
        const card = document.createElement('article');
        card.className = 'class-card add-class-card';
        card.innerHTML = `
            <div class="class-card-content add-class-content">
                <div class="add-class-inner">
                    <div class="add-class-icon">
                        <i class="fas fa-plus"></i>
                    </div>
                    <h3>Create New Class</h3>
                    <p>Organize sets by subject</p>
                </div>
            </div>
        `;
        card.addEventListener('click', () => {
            playClickSound();
            showClassModal();
        });
        return card;
    }

    function createClassCard(classItem) {
        const classSets = sortSets(flashcardSets.filter(set => String(set.classId || '') === String(classItem.id)));
        const dueCount = srsModeEnabled && window.srsManager?.isReady()
            ? classSets.reduce((total, set) => total + getSetSRSInfo(set).dueCards, 0)
            : 0;
        const card = document.createElement('article');
        card.className = 'class-card';
        card.style.setProperty('--class-color', classItem.color || '#3B82F6');

        const setPreview = classSets.slice(0, 5).map(set => `<span>${escapeHtml(set.name || 'Untitled Set')}</span>`).join('');
        const extraCount = Math.max(0, classSets.length - 5);
        card.innerHTML = `
            <button class="class-edit-btn" type="button" title="Edit class">
                <i class="fas fa-pen"></i>
            </button>
            <div class="class-card-content">
                <div class="class-card-top" aria-hidden="true"></div>
                <div class="class-card-main">
                    <div class="class-card-header">
                        <span class="class-color-dot"></span>
                        <div class="class-card-title">
                            <h3>${escapeHtml(classItem.name)}</h3>
                            <p>${classSets.length === 0 ? 'No sets yet' : `${classSets.length} ${classSets.length === 1 ? 'set' : 'sets'}`}</p>
                        </div>
                    </div>
                    <div class="class-card-meta">
                        <span><i class="fas fa-layer-group"></i>${classSets.length} ${classSets.length === 1 ? 'set' : 'sets'}</span>
                        ${srsModeEnabled ? `<span><i class="fas fa-brain"></i>${dueCount} due</span>` : ''}
                    </div>
                </div>
                <div class="class-set-preview">
                    ${setPreview || '<span class="class-card-empty">Add sets from creator</span>'}
                    ${extraCount ? `<span>+${extraCount} more</span>` : ''}
                </div>
            </div>
        `;

        card.addEventListener('click', () => {
            playClickSound();
            selectedClassId = classItem.id;
            currentLibraryView = 'all';
            updateViewTabs();
            renderSets(searchInput.value);
        });

        card.querySelector('.class-edit-btn')?.addEventListener('click', (event) => {
            event.preventDefault();
            event.stopPropagation();
            playClickSound();
            showClassModal(classItem);
        });

        return card;
    }

    function escapeHtml(value) {
        const div = document.createElement('div');
        div.textContent = String(value ?? '');
        return div.innerHTML;
    }

    function updateViewTabs() {
        libraryViewTabs.forEach(tab => {
            const isActive = selectedClassId
                ? tab.dataset.view === 'classes'
                : tab.dataset.view === currentLibraryView;
            tab.classList.toggle('active', isActive);
        });
    }

    function showClassModal(classItem = null, options = {}) {
        if (!classModal) return;
        classForEditor = classItem;
        classSelectTarget = options.selectElement || null;
        if (classModalTitle) classModalTitle.textContent = classItem ? 'Edit Class' : 'New Class';
        if (classNameInput) classNameInput.value = classItem?.name || '';
        if (classColorInput) classColorInput.value = classItem?.color || '#3B82F6';
        if (deleteClassBtn) deleteClassBtn.classList.toggle('hidden', !classItem);
        
        // Highlight active icon
        const activeIcon = classItem?.icon || 'fa-graduation-cap';
        const iconGrid = document.getElementById('class-icon-grid');
        if (iconGrid) {
            iconGrid.querySelectorAll('.icon-btn').forEach(btn => {
                btn.classList.toggle('active', btn.getAttribute('data-icon') === activeIcon);
            });
        }
        
        classModal.classList.remove('hidden');
        classModal.classList.add('visible');
        setTimeout(() => classNameInput?.focus(), 40);
    }

    function hideClassModal() {
        if (!classModal) return;
        classModal.classList.remove('visible');
        setTimeout(() => classModal.classList.add('hidden'), 300);
        classForEditor = null;
        classSelectTarget = null;
    }

    async function saveClassFromModal() {
        const name = classNameInput?.value.trim();
        if (!name) {
            showToast('Please enter a class name', 'error');
            classNameInput?.focus();
            return;
        }
        
        const activeIconBtn = document.querySelector('#class-icon-grid .icon-btn.active');
        const icon = activeIconBtn ? activeIconBtn.getAttribute('data-icon') : 'fa-graduation-cap';

        try {
            const classPayload = {
                ...(classForEditor || {}),
                name,
                color: classColorInput?.value || '#3B82F6',
                icon
            };
            const savedClass = window.flashcardStore?.saveClass
                ? await window.flashcardStore.saveClass(classPayload)
                : normalizeClassRecord(classPayload);

            if (!window.flashcardStore?.saveClass) {
                const updated = flashcardClasses.filter(item => String(item.id) !== String(savedClass.id));
                updated.push(savedClass);
                localStorage.setItem('flashcardClasses', JSON.stringify(updated));
            }

            await reloadLibraryData();
            if (classSelectTarget) {
                populateClassSelect(classSelectTarget, savedClass.id);
            }
            hideClassModal();
            updateLibraryStats();
            renderSets(searchInput.value);
            playClickSound();
            showToast('Class saved', 'success');
        } catch (error) {
            console.error('Error saving class:', error);
            showToast('Could not save class', 'error');
        }
    }

    async function deleteCurrentClass() {
        if (!classForEditor) return;
        const shouldDelete = window.confirm(`Delete "${classForEditor.name}"? Its sets will move to General.`);
        if (!shouldDelete) return;

        try {
            if (window.flashcardStore?.deleteClass) {
                await window.flashcardStore.deleteClass(classForEditor.id);
            } else {
                flashcardClasses = flashcardClasses.filter(item => String(item.id) !== String(classForEditor.id));
                flashcardSets = flashcardSets.map(set => (
                    String(set.classId || '') === String(classForEditor.id) ? { ...set, classId: null } : set
                ));
                localStorage.setItem('flashcardClasses', JSON.stringify(flashcardClasses));
                localStorage.setItem('flashcardSets', JSON.stringify(flashcardSets));
            }

            if (String(selectedClassId || '') === String(classForEditor.id)) {
                selectedClassId = null;
                currentLibraryView = 'general';
            }

            await reloadLibraryData();
            hideClassModal();
            updateViewTabs();
            updateLibraryStats();
            renderSets(searchInput.value);
            playClickSound();
            showToast('Class deleted; sets moved to General', 'success');
        } catch (error) {
            console.error('Error deleting class:', error);
            showToast('Could not delete class', 'error');
        }
    }

    // Create set card
    function createSetCard(set) {
        const card = setTemplate.content.cloneNode(true).querySelector('.set-card');
        
        // Set content
        const setNameEl = card.querySelector('.set-name');
        setNameEl.textContent = set.name;
        setNameEl.title = set.name; // show full name on hover when truncated
        const cardCount = Array.isArray(set.cards) ? set.cards.length : 0;
        card.querySelector('.card-count').textContent = `${cardCount} ${cardCount === 1 ? 'card' : 'cards'}`;
        
        // Format dates properly
        const createdDate = set.created || set.createdAt || Date.now();
        card.querySelector('.created-date').textContent = formatDate(createdDate);
        
        // Study count with proper fallback
        const studyCount = set.openedCount || 0;
        card.querySelector('.study-count').textContent = `${studyCount} ${studyCount === 1 ? 'time' : 'times'} studied`;

        const color = getClassColor(set.classId);
        const icon = getClassIcon(set.classId);

        // Render themed icon box
        const iconBox = card.querySelector('.set-icon-box');
        if (iconBox) {
            iconBox.style.backgroundColor = `${color}20`; // semi-transparent class color
            iconBox.style.color = color;
            iconBox.innerHTML = `<i class="fas ${icon}"></i>`;
        }

        const classPill = card.querySelector('.set-class-pill');
        if (classPill) {
            classPill.style.backgroundColor = `${color}15`;
            classPill.style.color = color;
            classPill.style.borderColor = `${color}30`;
            classPill.textContent = escapeHtml(getClassLabel(set.classId));
        }

        // Star Pinning (Favorite) logic
        const favoriteBtn = card.querySelector('.favorite-btn');
        if (favoriteBtn) {
            const isPinned = Boolean(set.pinned);
            favoriteBtn.innerHTML = isPinned ? `<i class="fas fa-star"></i>` : `<i class="far fa-star"></i>`;
            favoriteBtn.classList.toggle('active', isPinned);
            favoriteBtn.addEventListener('click', async (e) => {
                e.preventDefault();
                e.stopPropagation();
                
                set.pinned = !isPinned;
                try {
                    if (window.flashcardStore?.saveSet) {
                        await window.flashcardStore.saveSet(set);
                    } else {
                        const currentSets = JSON.parse(localStorage.getItem('flashcardSets') || '[]');
                        const index = currentSets.findIndex(item => String(item.id) === String(set.id));
                        if (index !== -1) {
                            currentSets[index].pinned = set.pinned;
                            localStorage.setItem('flashcardSets', JSON.stringify(currentSets));
                        }
                    }
                    showToast(set.pinned ? 'Set pinned to top' : 'Set unpinned', 'success');
                    reloadLibraryData().then(() => renderSets(searchInput.value));
                    playClickSound();
                } catch (err) {
                    console.error('Error toggling pin state:', err);
                }
            });
        }

        const srsSummary = card.querySelector('.set-srs-summary');
        if (srsSummary) {
            const srsInfo = getSetSRSInfo(set);
            srsSummary.classList.toggle('srs-summary-disabled', !srsModeEnabled);

            if (!srsModeEnabled || !window.srsManager || !window.srsManager.isReady()) {
                srsSummary.innerHTML = '';
                srsSummary.hidden = true;
            } else {
                srsSummary.hidden = false;
                srsSummary.innerHTML = `
                    <span><i class="fas fa-clock"></i> ${srsInfo.dueCards} due</span>
                    <span>${srsInfo.learningCards} learning</span>
                    <span>${srsInfo.nextDue}</span>
                `;
            }
        }

        // Action Buttons & Dropdown Options
        const menuTriggerBtn = card.querySelector('.menu-trigger-btn');
        const dropdownMenu = card.querySelector('.card-dropdown-menu');
        
        if (menuTriggerBtn && dropdownMenu) {
            menuTriggerBtn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                
                document.querySelectorAll('.card-dropdown-menu').forEach(menu => {
                    if (menu !== dropdownMenu) menu.classList.add('hidden');
                });
                
                dropdownMenu.classList.toggle('hidden');
                playClickSound();
            });
        }

        // Action buttons with error handling
        card.querySelector('.study-btn').addEventListener('click', (e) => {
            e.preventDefault();
            window.location.href = `study.html?setId=${set.id}`;
        });

        card.querySelector('.edit-btn').addEventListener('click', (e) => {
            e.preventDefault();
            if (dropdownMenu) dropdownMenu.classList.add('hidden');
            window.location.href = `creator.html?setId=${set.id}`;
        });

        const deckSettingsBtn = card.querySelector('.deck-settings-btn');
        if (deckSettingsBtn) {
            deckSettingsBtn.addEventListener('click', (e) => {
                e.preventDefault();
                if (dropdownMenu) dropdownMenu.classList.add('hidden');
                showDeckSettingsModal(set);
            });
        }

        card.querySelector('.delete-btn').addEventListener('click', (e) => {
            e.preventDefault();
            if (dropdownMenu) dropdownMenu.classList.add('hidden');
            setToDelete = set;
            showDeleteModal();
        });

        return card;
    }

    // Filter sets based on search
    function filterSets(searchTerm) {
        let scopedSets = flashcardSets;
        if (selectedClassId) {
            scopedSets = scopedSets.filter(set => String(set.classId || '') === String(selectedClassId));
        } else if (currentLibraryView === 'general') {
            scopedSets = scopedSets.filter(set => !set.classId);
        }

        if (!searchTerm) return scopedSets;
        
        const term = searchTerm.toLowerCase();
        return scopedSets.filter(set => 
            set.name.toLowerCase().includes(term) ||
            (set.description && set.description.toLowerCase().includes(term)) ||
            getClassLabel(set.classId).toLowerCase().includes(term)
        );
    }

    // Sort sets based on selected option (pinned sets always at top)
    function sortSets(sets) {
        const sortBy = sortSelect.value;
        
        return [...sets].sort((a, b) => {
            const pinnedA = a.pinned ? 1 : 0;
            const pinnedB = b.pinned ? 1 : 0;
            if (pinnedA !== pinnedB) {
                return pinnedB - pinnedA;
            }

            switch (sortBy) {
                case 'name':
                    return a.name.localeCompare(b.name);
                case 'cards':
                    const countA = Array.isArray(a.cards) ? a.cards.length : 0;
                    const countB = Array.isArray(b.cards) ? b.cards.length : 0;
                    return countB - countA;
                case 'studied':
                    return (b.openedCount || 0) - (a.openedCount || 0);
                case 'recent':
                default:
                    const dateA = a.createdAt || a.created || 0;
                    const dateB = b.createdAt || b.created || 0;
                    return dateB - dateA;
            }
        });
    }

    // Delete modal
    function showDeleteModal() {
        deleteModal.classList.remove('hidden');
        deleteModal.classList.add('visible');
    }

    function hideDeleteModal() {
        deleteModal.classList.remove('visible');
        setTimeout(() => deleteModal.classList.add('hidden'), 300);
    }

    // Delete set
    async function deleteSet() {
        if (!setToDelete) return;

        try {
            if (window.flashcardStore?.deleteSet) {
                await window.flashcardStore.deleteSet(setToDelete.id);
            } else {
                const currentSets = JSON.parse(localStorage.getItem('flashcardSets') || '[]');
                const updatedSets = currentSets.filter(set => set.id !== setToDelete.id);
                localStorage.setItem('flashcardSets', JSON.stringify(updatedSets));
            }

            await reloadLibraryData();

            // Clear the container and re-render
            setsContainer.innerHTML = '';
            renderSets(searchInput.value);

            hideDeleteModal();
            showToast('Flashcard set deleted', 'success');

            // Clear the reference to the deleted set
            setToDelete = null;

            // Update stats
            updateLibraryStats();
        } catch (error) {
            console.error('Error deleting set:', error);
            showToast('Error deleting set', 'error');
            hideDeleteModal();
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

    // Format date helper
    function formatDate(timestamp) {
        const date = new Date(timestamp);
        const now = new Date();
        const diffDays = Math.floor((now - date) / (1000 * 60 * 60 * 24));

        if (diffDays === 0) return 'Today';
        if (diffDays === 1) return 'Yesterday';
        if (diffDays < 7) return `${diffDays} days ago`;
        
        return date.toLocaleDateString('en-US', {
            month: 'short',
            day: 'numeric',
            year: date.getFullYear() !== now.getFullYear() ? 'numeric' : undefined
        });
    }

    function getDefaultAppSettings() {
        return window.DEFAULT_FLASHCARD_SETTINGS || {
            theme: 'dark',
            fonts: {
                content: "'Plus Jakarta Sans', sans-serif"
            }
        };
    }

    function normalizeAppSettings(settings = {}) {
        if (window.normalizeFlashcardSettings) {
            return window.normalizeFlashcardSettings(settings);
        }

        const defaults = getDefaultAppSettings();
        return {
            ...defaults,
            ...settings,
            fonts: {
                ...defaults.fonts,
                ...(settings.fonts || {})
            }
        };
    }

    function applyStoredSettings() {
        if (window.loadAndApplySettings) {
            window.loadAndApplySettings();
        }
    }

    // Import Modal
    function showImportModal() {
        importModal.classList.remove('hidden');
        importModal.classList.add('visible');
        // Clear previous data
        importSetNameInput.value = '';
        populateClassSelect(importClassSelect, selectedClassId || '');
        importContentTextarea.value = '';
        previewCardsContainer.innerHTML = '';
        previewCountSpan.textContent = '(0 cards)';
        parsedImportCards = [];
    }

    function hideImportModal() {
        importModal.classList.remove('visible');
        setTimeout(() => importModal.classList.add('hidden'), 300);
    }

    // Parse imported text to create flashcards
    function parseImportContent() {
        const content = importContentTextarea.value.trim();
        if (!content) {
            previewCardsContainer.innerHTML = '<div class="empty-preview">Paste your content above to see preview</div>';
            previewCountSpan.textContent = '(0 cards)';
            parsedImportCards = [];
            return;
        }

        // Read custom separators from inputs (support escape sequences \n and \t)
        const rawTermSep = importTermSepInput?.value || ';';
        const rawCardSep = importCardSepInput?.value || '@';
        const termSep = rawTermSep.replace(/\\n/g, '\n').replace(/\\t/g, '\t') || ';';
        const cardSep = rawCardSep.replace(/\\n/g, '\n').replace(/\\t/g, '\t') || '@';

        const cards = content.split(cardSep);
        parsedImportCards = cards
            .map(cardContent => {
                if (!cardContent.trim()) return null;
                const idx = cardContent.trim().indexOf(termSep);
                if (idx < 0) return null;
                return {
                    term: cardContent.trim().slice(0, idx).trim(),
                    definition: cardContent.trim().slice(idx + termSep.length).trim()
                };
            })
            .filter(card => card !== null && (card.term || card.definition));

        updateImportPreview();
    }

    function updateImportPreview() {
        // Clear preview
        previewCardsContainer.innerHTML = '';
        
        // Update count
        previewCountSpan.textContent = `(${parsedImportCards.length} cards)`;
        
        if (parsedImportCards.length === 0) {
            previewCardsContainer.innerHTML = '<div class="empty-preview">No valid cards found. Check your format.</div>';
            return;
        }
        
        // Add each card to preview (up to first 5)
        const cardsToShow = parsedImportCards.slice(0, 5);
        cardsToShow.forEach(card => {
            const previewCard = document.createElement('div');
            previewCard.className = 'preview-card';
            
            const term = document.createElement('div');
            term.className = 'term';
            term.textContent = card.term || '(Empty term)';
            
            const definition = document.createElement('div');
            definition.className = 'definition';
            definition.textContent = card.definition || '(Empty definition)';
            
            previewCard.appendChild(term);
            previewCard.appendChild(definition);
            previewCardsContainer.appendChild(previewCard);
        });
        
        // Show truncation message if needed
        if (parsedImportCards.length > 5) {
            const moreCards = document.createElement('div');
            moreCards.className = 'more-cards';
            moreCards.textContent = `+ ${parsedImportCards.length - 5} more cards`;
            previewCardsContainer.appendChild(moreCards);
        }
    }

    async function createImportedSet() {
        const setName = importSetNameInput.value.trim();

        // Validate
        if (!setName) {
            showFormError(importSetNameInput, 'Please enter a set name');
            return false;
        }

        if (parsedImportCards.length === 0) {
            showFormError(importContentTextarea, 'No valid cards found. Please check your format.');
            return false;
        }

        try {
            // Create new flashcard set
            const newSet = {
                name: setName,
                description: `Imported set with ${parsedImportCards.length} cards`,
                classId: importClassSelect?.value && importClassSelect.value !== '__new' ? importClassSelect.value : null,
                cards: parsedImportCards.map(card => ({
                    term: card.term,
                    definition: card.definition,
                    termImage: '',
                    definitionImage: '',
                    tags: [],
                    suspended: false,
                    buriedUntil: null,
                    reviewHistory: []
                })),
                srsSettings: { ...DEFAULT_SRS_SETTINGS },
                created: Date.now(),
                lastModified: Date.now(),
                openedCount: 0
            };

            if (window.flashcardStore?.saveSet) {
                await window.flashcardStore.saveSet(newSet);
            } else {
                const existingSets = JSON.parse(localStorage.getItem('flashcardSets') || '[]');
                existingSets.push({ ...newSet, id: Date.now() });
                localStorage.setItem('flashcardSets', JSON.stringify(existingSets));
            }
            await reloadLibraryData();

            // Hide modal and show success
            hideImportModal();
            showToast(`Successfully imported ${parsedImportCards.length} flashcards`, 'success');

            // Refresh the display
            renderSets(searchInput.value);
            updateLibraryStats();

            return true;
        } catch (error) {
            console.error('Error importing flashcards:', error);
            showToast('Error importing flashcards', 'error');
            return false;
        }
    }

    function showFormError(element, message) {
        // Add error class to form group
        const formGroup = element.closest('.form-group');
        formGroup.classList.add('error');
        
        // Add error message
        let errorMsg = formGroup.querySelector('.error-message');
        if (!errorMsg) {
            errorMsg = document.createElement('div');
            errorMsg.className = 'error-message';
            formGroup.appendChild(errorMsg);
        }
        errorMsg.textContent = message;
        
        // Clear error after 3 seconds
        setTimeout(() => {
            formGroup.classList.remove('error');
            errorMsg.remove();
        }, 3000);
    }

    // Settings Modal Functions
    function showSettingsModal() {
        settingsModal.classList.remove('hidden');
        settingsModal.classList.add('visible');
        loadSettingsValues();
    }

    function hideSettingsModal() {
        settingsModal.classList.remove('visible');
        setTimeout(() => settingsModal.classList.add('hidden'), 300);
    }

    async function loadSettingsValues() {
        const userSettings = window.getFlashcardSettings
            ? await window.getFlashcardSettings()
            : normalizeAppSettings(JSON.parse(localStorage.getItem('flashcards-settings') || '{}'));
        
        if (appThemeSelect) {
            appThemeSelect.value = userSettings.theme;
        }

        if (normalStudyOrderSelect) {
            normalStudyOrderSelect.value = userSettings.normalStudyOrder || 'forward';
        }

        if (userSettings.fonts) {
            if (userSettings.fonts.content.startsWith('custom-')) {
                contentFontSelect.value = 'custom';
                customContentFontDiv.classList.remove('hidden');
            } else {
                contentFontSelect.value = userSettings.fonts.content;
            }
        }

        // Sync cursor-style radio buttons to current saved preference
        const cursorRadios = document.querySelectorAll('input[name="cursor-style"]');
        if (cursorRadios.length) {
            const savedEnabled = localStorage.getItem('customCursorEnabled');
            const savedStyle   = localStorage.getItem('cursorStyle') || 'fluid';
            const isEnabled    = savedEnabled === null ? true : savedEnabled === 'true';
            // Map legacy 'comet' to 'fluid'
            const style        = (savedStyle === 'comet') ? 'fluid' : savedStyle;
            const activeValue  = (!isEnabled || style === 'default') ? 'default' : style;
            cursorRadios.forEach(r => { r.checked = (r.value === activeValue); });
        }

        // Initialize opacity slider
        if (cardBgOpacitySlider) {
            const opacityVal = parseFloat(userSettings.cardBgOpacity ?? 0.32);
            cardBgOpacitySlider.value = String(Number.isFinite(opacityVal) ? opacityVal : 0.32);
            if (cardBgOpacityLabel) cardBgOpacityLabel.textContent = (Number.isFinite(opacityVal) ? opacityVal : 0.32).toFixed(2);
        }
    }

    function showCopyPasteExportModal() {
        if (!copyPasteExportModal) return;
        if (copyExportDeckSelect) {
            copyExportDeckSelect.innerHTML = flashcardSets
                .map(s => `<option value="${s.id}">${s.name || 'Untitled'}</option>`)
                .join('');
        }
        if (copyExportTextArea) copyExportTextArea.value = '';
        if (doCopyExportBtn) doCopyExportBtn.style.display = 'none';
        copyPasteExportModal.classList.remove('hidden');
        copyPasteExportModal.classList.add('visible');
    }

    function hideCopyPasteExportModal() {
        if (!copyPasteExportModal) return;
        copyPasteExportModal.classList.remove('visible');
        setTimeout(() => copyPasteExportModal.classList.add('hidden'), 300);
    }

    function previewAppearanceSettings() {
        const previewSettings = normalizeAppSettings({
            theme: appThemeSelect?.value
        });
        const root = document.documentElement;

        root.setAttribute('data-theme', previewSettings.theme);
        root.removeAttribute('data-matte');
        root.style.removeProperty('--study-card-width');
        root.style.removeProperty('--study-card-aspect');
    }
    
    async function saveSettings() {
        const existingSettings = window.getFlashcardSettings
            ? await window.getFlashcardSettings()
            : normalizeAppSettings(JSON.parse(localStorage.getItem('flashcards-settings') || '{}'));
        const userSettings = normalizeAppSettings(existingSettings);

        userSettings.theme = appThemeSelect?.value || userSettings.theme;
        userSettings.normalStudyOrder = ['forward', 'backward', 'random'].includes(normalStudyOrderSelect?.value)
            ? normalStudyOrderSelect.value
            : (userSettings.normalStudyOrder || 'forward');
        delete userSettings.studyCard;

        // Save card background opacity
        if (cardBgOpacitySlider) {
            const opacityVal = parseFloat(cardBgOpacitySlider.value);
            if (Number.isFinite(opacityVal)) userSettings.cardBgOpacity = opacityVal;
        }

        if (contentFontSelect.value === 'custom' && customFonts.content) {
            userSettings.fonts.content = 'custom-' + customFonts.content.name;
        } else {
            userSettings.fonts.content = contentFontSelect.value;
        }
        
        if (window.saveFlashcardSettings) {
            await window.saveFlashcardSettings(userSettings);
        } else {
            localStorage.setItem('flashcards-settings', JSON.stringify(userSettings));
            localStorage.setItem('flashcards-theme', userSettings.theme);
            if (window.loadAndApplySettings) {
                window.loadAndApplySettings(userSettings);
            }
        }
        
        showToast('Settings saved successfully', 'success');
        hideSettingsModal();
    }
    
    async function resetSettings() {
        const defaultSettings = normalizeAppSettings(getDefaultAppSettings());

        if (appThemeSelect) appThemeSelect.value = defaultSettings.theme;
        if (normalStudyOrderSelect) normalStudyOrderSelect.value = defaultSettings.normalStudyOrder || 'forward';
        contentFontSelect.value = defaultSettings.fonts.content;
        customContentFontDiv.classList.add('hidden');
        customFonts = { content: null };

        if (window.saveFlashcardSettings) {
            await window.saveFlashcardSettings(defaultSettings);
        } else {
            localStorage.setItem('flashcards-settings', JSON.stringify(defaultSettings));
            localStorage.setItem('flashcards-theme', defaultSettings.theme);
            if (typeof loadAndApplySettings === 'function') {
                loadAndApplySettings(defaultSettings);
            }
        }
        
        showToast('Settings reset to default', 'info');
    }

    async function handleExportBackup() {
        if (!window.flashcardStore?.exportBackup) {
            showToast('Backup export is not available in this environment', 'error');
            return;
        }

        try {
            showToast('Preparing backup...', 'info');
            const result = await window.flashcardStore.exportBackup();
            if (result?.canceled) return;

            const setCount = result?.setCount ?? flashcardSets.length;
            showToast(`Backup exported (${setCount} sets)`, 'success');
        } catch (error) {
            console.error('Error exporting backup:', error);
            showToast('Could not export backup', 'error');
        }
    }

    async function handleRestoreBackup() {
        if (!window.flashcardStore?.importBackup) {
            showToast('Backup restore is not available in this environment', 'error');
            return;
        }

        const shouldRestore = window.confirm(
            'Restore backup will replace your current local flashcard library. Export a backup first if you want to keep the current version.'
        );
        if (!shouldRestore) return;

        try {
            const result = await window.flashcardStore.importBackup();
            if (result?.unsupported) {
                showToast('Backup restore is only available in the desktop app', 'error');
                return;
            }
            if (result?.canceled) return;

            await reloadLibraryData();
            updateLibraryStats();
            renderSets(searchInput.value);

            showToast(`Backup restored (${result.setCount ?? flashcardSets.length} sets)`, 'success');
            hideSettingsModal();
        } catch (error) {
            console.error('Error restoring backup:', error);
            showToast('Could not restore backup', 'error');
        }
    }

    async function handleExportDelimited(format) {
        if (!window.flashcardStore?.exportDelimited) {
            showToast('CSV/TSV export is only available in the desktop app', 'error');
            return;
        }

        try {
            const result = await window.flashcardStore.exportDelimited(format);
            if (result?.canceled) return;
            const label = format === 'tsv' ? 'TSV' : 'CSV';
            showToast(`${label} exported (${result.cardCount || 0} cards)`, 'success');
        } catch (error) {
            console.error(`Error exporting ${format}:`, error);
            showToast(`Could not export ${format.toUpperCase()}`, 'error');
        }
    }

    async function handleImportDelimited() {
        if (!window.flashcardStore?.importDelimited) {
            showToast('CSV/TSV import is only available in the desktop app', 'error');
            return;
        }

        try {
            const result = await window.flashcardStore.importDelimited();
            if (result?.canceled) return;
            await reloadLibraryData();
            updateLibraryStats();
            renderSets(searchInput.value);
            hideSettingsModal();
            showToast(`Imported ${result.cardCount || 0} cards`, 'success');
        } catch (error) {
            console.error('Error importing delimited flashcards:', error);
            showToast('Could not import CSV/TSV file', 'error');
        }
    }

    function showDeckSettingsModal(set) {
        if (!deckSettingsModal || !set) return;

        setForDeckSettings = set;
        const settings = normalizeSrsSettings(set.srsSettings);
        if (deckSettingsName) {
            deckSettingsName.textContent = `${set.name}: deck-specific SRS tuning and daily limits.`;
        }
        if (deckSrsEnabled) deckSrsEnabled.checked = settings.enabled;
        if (deckRequestRetention) deckRequestRetention.value = settings.requestRetention;
        if (deckMaxInterval) deckMaxInterval.value = settings.maxIntervalDays;
        if (deckNewLimit) deckNewLimit.value = settings.newCardsPerDay ?? '';
        if (deckReviewLimit) deckReviewLimit.value = settings.reviewsPerDay ?? '';

        deckSettingsModal.classList.remove('hidden');
        deckSettingsModal.classList.add('visible');
    }

    function hideDeckSettingsModal() {
        if (!deckSettingsModal) return;
        deckSettingsModal.classList.remove('visible');
        setTimeout(() => deckSettingsModal.classList.add('hidden'), 300);
        setForDeckSettings = null;
    }

    async function saveDeckSettings() {
        if (!setForDeckSettings) return;

        const settings = normalizeSrsSettings({
            enabled: deckSrsEnabled ? deckSrsEnabled.checked : true,
            requestRetention: deckRequestRetention?.value,
            maxIntervalDays: deckMaxInterval?.value,
            newCardsPerDay: deckNewLimit?.value,
            reviewsPerDay: deckReviewLimit?.value
        });

        const updatedSet = {
            ...setForDeckSettings,
            srsSettings: settings,
            lastModified: Date.now()
        };

        try {
            if (window.flashcardStore?.saveSet) {
                await window.flashcardStore.saveSet(updatedSet);
                flashcardSets = await window.flashcardStore.listSets();
            } else {
                flashcardSets = flashcardSets.map(set => set.id === updatedSet.id ? updatedSet : set);
            }
            syncLocalMirror();
            updateLibraryStats();
            renderSets(searchInput.value);
            hideDeckSettingsModal();
            showToast('Deck SRS settings saved', 'success');
        } catch (error) {
            console.error('Error saving deck settings:', error);
            showToast('Could not save deck settings', 'error');
        }
    }

    // Danger Zone Reset SRS functions
    const resetDeckSrsBtn = document.getElementById('reset-deck-srs-btn');
    const deckResetConfirmModal = document.getElementById('deck-reset-confirm-modal');
    const closeDeckResetConfirmBtn = document.getElementById('close-deck-reset-confirm');
    const cancelDeckResetConfirmBtn = document.getElementById('cancel-deck-reset-confirm');
    const resetKeepHistory = document.getElementById('reset-keep-history');
    const resetDeleteHistory = document.getElementById('reset-delete-history');
    const resetConfirmInput = document.getElementById('reset-confirm-input');
    const confirmDeckResetBtn = document.getElementById('confirm-deck-reset');
    const resetConfirmTextMatch = document.getElementById('reset-confirm-text-match');

    // Mutually exclusive checkboxes
    if (resetKeepHistory && resetDeleteHistory) {
        resetKeepHistory.addEventListener('change', () => {
            if (resetKeepHistory.checked) resetDeleteHistory.checked = false;
        });
        resetDeleteHistory.addEventListener('change', () => {
            if (resetDeleteHistory.checked) resetKeepHistory.checked = false;
        });
    }

    function showDeckResetConfirmModal() {
        if (!setForDeckSettings) return;

        // Hide deck settings modal first (but keep setForDeckSettings populated)
        if (deckSettingsModal) {
            deckSettingsModal.classList.add('hidden');
            deckSettingsModal.classList.remove('visible');
        }

        if (resetConfirmInput) resetConfirmInput.value = '';
        if (confirmDeckResetBtn) confirmDeckResetBtn.disabled = true;

        // Reset checkboxes to default
        if (resetKeepHistory) resetKeepHistory.checked = true;
        if (resetDeleteHistory) resetDeleteHistory.checked = false;

        if (deckResetConfirmModal) {
            deckResetConfirmModal.classList.remove('hidden');
            deckResetConfirmModal.classList.add('visible');
        }
    }

    function hideDeckResetConfirmModal() {
        if (deckResetConfirmModal) {
            deckResetConfirmModal.classList.remove('visible');
            setTimeout(() => deckResetConfirmModal.classList.add('hidden'), 300);
        }
        // Reopen deck settings modal
        if (setForDeckSettings && deckSettingsModal) {
            deckSettingsModal.classList.remove('hidden');
            deckSettingsModal.classList.add('visible');
        }
    }

    if (resetConfirmInput) {
        resetConfirmInput.addEventListener('input', () => {
            if (!setForDeckSettings) return;
            const inputVal = resetConfirmInput.value.trim().toLowerCase();
            const matchReset = 'reset';
            const matchName = setForDeckSettings.name.trim().toLowerCase();
            if (inputVal === matchReset || inputVal === matchName) {
                confirmDeckResetBtn.disabled = false;
            } else {
                confirmDeckResetBtn.disabled = true;
            }
        });
    }

    async function executeDeckReset() {
        if (!setForDeckSettings) return;

        const setId = setForDeckSettings.id;
        const deleteHistory = resetDeleteHistory ? resetDeleteHistory.checked : false;

        try {
            // 1. Create automatic backup JSON
            let backupPath = '';
            if (window.flashcardStore?.createDeckBackup) {
                backupPath = await window.flashcardStore.createDeckBackup(setId);
            }

            // 2. Perform reset
            if (window.flashcardStore?.resetDeckSRS) {
                await window.flashcardStore.resetDeckSRS(setId, deleteHistory);
            }

            // Close confirm modal
            if (deckResetConfirmModal) {
                deckResetConfirmModal.classList.remove('visible');
                deckResetConfirmModal.classList.add('hidden');
            }
            // Clear settings set ref
            setForDeckSettings = null;

            // Reload and refresh UI
            await reloadLibraryData();
            updateLibraryStats();
            renderSets(searchInput.value);

            // Show toast message with backup location
            let msg = 'SRS progress reset successfully.';
            if (backupPath) {
                const baseName = backupPath.split(/[\\/]/).pop();
                msg += ` Backup created: ${baseName}`;
            }
            showToast(msg, 'success');
        } catch (error) {
            console.error('Error resetting deck SRS:', error);
            showToast('Failed to reset deck SRS scheduling', 'error');
        }
    }
    
    // Handle custom font uploads
    function handleFontUpload(event, fontType) {
        const file = event.target.files[0];
        if (!file) return;
        
        if (file.name.toLowerCase().endsWith('.ttf') || file.name.toLowerCase().endsWith('.otf')) {
            const fontUrl = URL.createObjectURL(file);
            customFonts[fontType] = {
                name: file.name.split('.')[0],
                url: fontUrl
            };
            
            // Show a preview
            showToast(`Font "${file.name}" uploaded successfully`, 'success');
        } else {
            showToast('Please upload a TTF or OTF font file', 'error');
        }
    }

    // Premade Flashcards Functions
    function handleFlashcardTypeChange() {
        const selectedType = document.querySelector('input[name="flashcard-type"]:checked').value;
        currentFlashcardType = selectedType;
        
        if (selectedType === 'premade-flashcards') {
            // Redirect to the new premade flashcards page
            window.location.href = 'premade-library.html';
        } else {
            // Show user's flashcards
            renderSets();
        }
    }

    function showSubjectModal() {
        subjectModal.classList.remove('hidden');
        subjectModal.classList.add('visible');
        renderSubjects();
    }

    function hideSubjectModal() {
        subjectModal.classList.remove('visible');
        setTimeout(() => subjectModal.classList.add('hidden'), 300);
    }

    function showTopicModal(subject) {
        selectedSubject = subject;
        selectedSubjectName.textContent = subject.name;
        topicModal.classList.remove('hidden');
        topicModal.classList.add('visible');
        renderTopics(subject);
    }

    function hideTopicModal() {
        topicModal.classList.remove('visible');
        setTimeout(() => topicModal.classList.add('hidden'), 300);
    }

    function renderSubjects() {
        subjectsContainer.innerHTML = '';
        
        premadeSubjects.forEach(subject => {
            const subjectCard = document.createElement('div');
            subjectCard.className = 'subject-card';
            subjectCard.innerHTML = `
                <div class="subject-icon">
                    <i class="${subject.icon}"></i>
                </div>
                <div class="subject-name">${subject.name}</div>
                <div class="subject-description">${subject.description}</div>
            `;
            
            subjectCard.addEventListener('click', () => {
                hideSubjectModal();
                showTopicModal(subject);
            });
            
            subjectsContainer.appendChild(subjectCard);
        });
    }

    function renderTopics(subject) {
        topicsContainer.innerHTML = '';
        
        subject.topics.forEach(topic => {
            const topicCard = document.createElement('div');
            topicCard.className = 'topic-card';
            
            const tagsHtml = topic.tags.map(tag => `<span class="topic-tag">${tag}</span>`).join('');
            
            topicCard.innerHTML = `
                <div class="topic-icon">
                    <i class="${subject.icon}"></i>
                </div>
                <div class="topic-name">${topic.name}</div>
                <div class="topic-description">${topic.description}</div>
                <div class="topic-tags">${tagsHtml}</div>
            `;
            
            topicCard.addEventListener('click', () => {
                // Navigate to premade library page
                window.location.href = `premade-library.html?subject=${subject.id}&topic=${topic.id}`;
            });
            
            topicsContainer.appendChild(topicCard);
        });
    }

    // Event Listeners
    searchInput.addEventListener('input', () => renderSets(searchInput.value));
    sortSelect.addEventListener('change', () => {
        playClickSound();
        renderSets(searchInput.value);
    });

    libraryViewTabs.forEach(tab => {
        tab.addEventListener('click', () => {
            currentLibraryView = tab.dataset.view || 'all';
            selectedClassId = null;
            updateViewTabs();
            playClickSound();
            renderSets(searchInput.value);
        });
    });

    const editImportClassBtn = document.getElementById('edit-import-class-btn');
    if (importClassSelect) {
        importClassSelect.addEventListener('change', () => {
            playClickSound();
            const val = importClassSelect.value;
            if (editImportClassBtn) {
                editImportClassBtn.style.display = (val && val !== '__new') ? 'inline-flex' : 'none';
            }
            if (val === '__new') {
                importClassSelect.value = '';
                if (editImportClassBtn) editImportClassBtn.style.display = 'none';
                showClassModal(null, { selectElement: importClassSelect });
            }
        });
    }

    if (editImportClassBtn) {
        editImportClassBtn.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            playClickSound();
            const classId = importClassSelect.value;
            const classItem = flashcardClasses.find(c => String(c.id) === String(classId));
            if (classItem) {
                showClassModal(classItem, { selectElement: importClassSelect });
            }
        });
    }
    
    // Standalone extraction: timer/checklist navigation has been removed.

    const createSetBtn = document.getElementById('create-set-btn');
    if (createSetBtn) {
        createSetBtn.addEventListener('click', () => {
            window.location.href = 'creator.html?new=true';
        });
    }

    if (cardBrowserBtn) {
        cardBrowserBtn.addEventListener('click', () => {
            window.location.href = 'card-browser.html';
        });
    }
    
    const emptyStateCreateBtn = document.getElementById('empty-state-create-btn');
    if (emptyStateCreateBtn) {
        emptyStateCreateBtn.addEventListener('click', () => {
            window.location.href = 'creator.html?new=true';
        });
    }
    
    // Delete Modal Listeners
    cancelDeleteBtn.addEventListener('click', hideDeleteModal);
    confirmDeleteBtn.addEventListener('click', deleteSet);
    
    // Import Modal Listeners
    importSetBtn.addEventListener('click', showImportModal);
    if (reviewDueBtn) {
        reviewDueBtn.addEventListener('click', () => {
            if (firstDueSetId !== null) {
                window.location.href = `study.html?setId=${encodeURIComponent(firstDueSetId)}&reviewDue=true`;
            }
        });
    }
    closeImportBtn.addEventListener('click', hideImportModal);
    cancelImportBtn.addEventListener('click', hideImportModal);
    confirmImportBtn.addEventListener('click', createImportedSet);
    closeClassModalBtn?.addEventListener('click', hideClassModal);
    cancelClassBtn?.addEventListener('click', hideClassModal);
    saveClassBtn?.addEventListener('click', saveClassFromModal);
    deleteClassBtn?.addEventListener('click', deleteCurrentClass);
    
    // Class Icon selection click handler
    const classIconGrid = document.getElementById('class-icon-grid');
    if (classIconGrid) {
        classIconGrid.addEventListener('click', (e) => {
            const btn = e.target.closest('.icon-btn');
            if (!btn) return;
            classIconGrid.querySelectorAll('.icon-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            playClickSound();
        });
    }

    // Close dropdowns on clicking outside
    document.addEventListener('click', () => {
        document.querySelectorAll('.card-dropdown-menu').forEach(menu => {
            menu.classList.add('hidden');
        });
    });
    
    // Live preview as user types
    importContentTextarea.addEventListener('input', () => {
        parseImportContent();
    });

    // Re-parse when separators change
    importTermSepInput?.addEventListener('input', () => parseImportContent());
    importCardSepInput?.addEventListener('input', () => parseImportContent());
    
    // Clear form errors on input
    importSetNameInput.addEventListener('input', () => {
        const formGroup = importSetNameInput.closest('.form-group');
        formGroup.classList.remove('error');
        const errorMsg = formGroup.querySelector('.error-message');
        if (errorMsg) errorMsg.remove();
    });
    
    // Close modals when clicking outside
    deleteModal.addEventListener('click', (e) => {
        if (e.target === deleteModal) hideDeleteModal();
    });
    
    importModal.addEventListener('click', (e) => {
        if (e.target === importModal) hideImportModal();
    });

    // Settings Modal Event Listeners
    settingsBtn.addEventListener('click', showSettingsModal);
    closeSettingsBtn.addEventListener('click', hideSettingsModal);
    saveSettingsBtn.addEventListener('click', saveSettings);
    resetSettingsBtn.addEventListener('click', resetSettings);
    if (exportBackupBtn) exportBackupBtn.addEventListener('click', handleExportBackup);
    if (restoreBackupBtn) restoreBackupBtn.addEventListener('click', handleRestoreBackup);
    if (exportCsvBtn) exportCsvBtn.addEventListener('click', () => handleExportDelimited('csv'));
    if (exportTsvBtn) exportTsvBtn.addEventListener('click', () => handleExportDelimited('tsv'));
    if (importDelimitedBtn) importDelimitedBtn.addEventListener('click', handleImportDelimited);
    appThemeSelect?.addEventListener('change', previewAppearanceSettings);

    // Opacity slider live label
    cardBgOpacitySlider?.addEventListener('input', () => {
        if (cardBgOpacityLabel) cardBgOpacityLabel.textContent = parseFloat(cardBgOpacitySlider.value).toFixed(2);
    });

    // Copy-paste import button (opens import modal)
    copyPasteImportBtn?.addEventListener('click', () => { hideSettingsModal(); showImportModal(); });

    // Copy-paste export modal
    copyPasteExportBtn?.addEventListener('click', () => { hideSettingsModal(); showCopyPasteExportModal(); });
    closeCopyExportBtn?.addEventListener('click', hideCopyPasteExportModal);
    cancelCopyExportBtn?.addEventListener('click', hideCopyPasteExportModal);
    copyPasteExportModal?.addEventListener('click', e => { if (e.target === copyPasteExportModal) hideCopyPasteExportModal(); });

    generateCopyExportBtn?.addEventListener('click', async () => {
        const setId = copyExportDeckSelect?.value;
        if (!setId) { showToast('Select a deck', 'error'); return; }
        const rawTermSep = copyExportTermSep?.value || ';';
        const rawCardSep = copyExportCardSep?.value || '@';
        const termSep = rawTermSep.replace(/\\n/g, '\n').replace(/\\t/g, '\t') || ';';
        const cardSep = rawCardSep.replace(/\\n/g, '\n').replace(/\\t/g, '\t') || '@';
        try {
            const set = await window.flashcardStore.getSet(setId);
            if (!set) { showToast('Deck not found', 'error'); return; }
            const text = (set.cards || [])
                .filter(c => c.term || c.definition)
                .map(c => {
                    const term = String(c.term || '').replace(/<[^>]+>/g, '').trim();
                    const def = String(c.definition || '').replace(/<[^>]+>/g, '').trim();
                    return `${term}${termSep}${def}`;
                })
                .join(cardSep);
            if (copyExportTextArea) copyExportTextArea.value = text;
            if (doCopyExportBtn) doCopyExportBtn.style.display = '';
        } catch (err) {
            showToast('Could not generate export', 'error');
        }
    });

    doCopyExportBtn?.addEventListener('click', async () => {
        const text = copyExportTextArea?.value || '';
        if (!text) return;
        try {
            await navigator.clipboard.writeText(text);
            showToast('Copied to clipboard!', 'success');
        } catch (_) {
            copyExportTextArea?.select();
            document.execCommand('copy');
            showToast('Copied!', 'success');
        }
    });

    // Cursor style radio — applies immediately on change (no Save needed)
    document.querySelectorAll('input[name="cursor-style"]').forEach(radio => {
        radio.addEventListener('change', () => {
            const val = radio.value;
            if (typeof window.changeCursorStyle === 'function') {
                if (val === 'default') {
                    localStorage.setItem('customCursorEnabled', 'false');
                    window.changeCursorStyle('default');
                } else {
                    localStorage.setItem('customCursorEnabled', 'true');
                    window.changeCursorStyle(val);
                }
            }
        });
    });

    if (closeDeckSettingsBtn) closeDeckSettingsBtn.addEventListener('click', hideDeckSettingsModal);
    if (cancelDeckSettingsBtn) cancelDeckSettingsBtn.addEventListener('click', hideDeckSettingsModal);
    if (saveDeckSettingsBtn) saveDeckSettingsBtn.addEventListener('click', saveDeckSettings);
    
    // Reset SRS listeners
    if (resetDeckSrsBtn) resetDeckSrsBtn.addEventListener('click', showDeckResetConfirmModal);
    if (closeDeckResetConfirmBtn) closeDeckResetConfirmBtn.addEventListener('click', hideDeckResetConfirmModal);
    if (cancelDeckResetConfirmBtn) cancelDeckResetConfirmBtn.addEventListener('click', hideDeckResetConfirmModal);
    if (confirmDeckResetBtn) confirmDeckResetBtn.addEventListener('click', executeDeckReset);

    // Font dropdowns
    contentFontSelect.addEventListener('change', function() {
        if (this.value === 'custom') {
            customContentFontDiv.classList.remove('hidden');
        } else {
            customContentFontDiv.classList.add('hidden');
        }
    });
    
    // Font file uploads
    contentFontUpload.addEventListener('change', (e) => handleFontUpload(e, 'content'));
    
    // Close settings when clicking outside
    settingsModal.addEventListener('click', function(e) {
        if (e.target === settingsModal) {
            hideSettingsModal();
        }
    });

    if (deckSettingsModal) {
        deckSettingsModal.addEventListener('click', function(e) {
            if (e.target === deckSettingsModal) {
                hideDeckSettingsModal();
            }
        });
    }

    if (deckResetConfirmModal) {
        deckResetConfirmModal.addEventListener('click', function(e) {
            if (e.target === deckResetConfirmModal) {
                hideDeckResetConfirmModal();
            }
        });
    }

    // Premade flashcards event listeners
    flashcardTypeRadios.forEach(radio => {
        radio.addEventListener('change', handleFlashcardTypeChange);
    });

    // Subject modal event listeners
    closeSubjectBtn.addEventListener('click', hideSubjectModal);
    subjectModal.addEventListener('click', (e) => {
        if (e.target === subjectModal) hideSubjectModal();
    });

    // Topic modal event listeners
    closeTopicBtn.addEventListener('click', hideTopicModal);
    backToSubjectBtn.addEventListener('click', () => {
        hideTopicModal();
        showSubjectModal();
    });
    topicModal.addEventListener('click', (e) => {
        if (e.target === topicModal) hideTopicModal();
    });

    window.addEventListener('erudite-menu-toast', (event) => {
        const { message, type } = event.detail || {};
        if (message) showToast(message, type || 'info');
    });

    window.addEventListener('erudite-menu-command', async (event) => {
        switch (event.detail) {
            case 'import-flashcards':
                showImportModal();
                break;
            case 'review-due':
                if (firstDueSetId !== null) {
                    window.location.href = `study.html?setId=${encodeURIComponent(firstDueSetId)}&reviewDue=true`;
                } else {
                    showToast('No cards are due right now', 'info');
                }
                break;
            default:
                break;
        }
    });

    // Initialize
    applyStoredSettings();

    initializeFlashcards();

    async function initializeFlashcards() {
        await initializeSRS();
        await loadFlashcardSets();

        if (window.location.hash === '#import') {
            showImportModal();
        } else if (window.location.hash === '#review-due' && firstDueSetId !== null) {
            window.location.href = `study.html?setId=${encodeURIComponent(firstDueSetId)}&reviewDue=true`;
        }
    }

    // SRS Initialization and Management
    async function initializeSRS() {
        const savedSRSMode = window.flashcardStore?.getState
            ? await window.flashcardStore.getState('srsModeEnabled')
            : localStorage.getItem('srsModeEnabled');
        srsModeEnabled = savedSRSMode === true || savedSRSMode === 'true';
        
        // Update UI
        updateSRSToggle();
        updateSRSStatus();
        
        // Set up event listeners
        if (srsToggle) {
            srsToggle.addEventListener('change', handleSRSToggle);
        }
        
        // Keyboard shortcut (Ctrl+Shift+S)
        document.addEventListener('keydown', (e) => {
            if (e.ctrlKey && e.shiftKey && e.key === 'S') {
                e.preventDefault();
                srsToggle.checked = !srsToggle.checked;
                handleSRSToggle();
            }
        });
        
    }

    async function handleSRSToggle() {
        srsModeEnabled = srsToggle.checked;
        
        if (window.flashcardStore?.setState) {
            await window.flashcardStore.setState('srsModeEnabled', srsModeEnabled);
        } else {
            localStorage.setItem('srsModeEnabled', srsModeEnabled.toString());
        }
        
        // Update UI
        updateSRSStatus();
        updateDueCardsCount();
        renderSets(searchInput.value);
        
    }

    function updateSRSToggle() {
        if (srsToggle) {
            srsToggle.checked = srsModeEnabled;
        }
    }

    function updateSRSStatus() {
        if (srsStatus) {
            const statusText = srsStatus.querySelector('.srs-status-text');
            if (statusText) {
                statusText.textContent = srsModeEnabled ? 'SRS' : 'Normal Study';
            }
        }
    }

    function getNextDueLabel(cards, dueCount) {
        if (dueCount > 0) return 'Now';
        if (!window.srsManager || !window.srsManager.isReady()) return 'Unavailable';

        const now = new Date();
        const futureDueDates = (cards || [])
            .filter(card => card.srs && card.srs.due && !card.suspended)
            .map(card => new Date(card.srs.due))
            .filter(date => !isNaN(date.getTime()) && date > now)
            .sort((a, b) => a - b);

        if (futureDueDates.length === 0) return 'No reviews scheduled';
        return `in ${window.srsManager.formatIntervalLabel(futureDueDates[0], now)}`;
    }

    function getSetSRSInfo(set) {
        const cards = Array.isArray(set.cards) ? set.cards : [];
        const emptyStats = {
            totalCards: cards.length,
            newCards: cards.length,
            dueCards: 0,
            learningCards: 0,
            reviewCards: 0,
            relearningCards: 0,
            masteredCards: 0,
            nextDue: 'SRS off'
        };
        const settings = normalizeSrsSettings(set.srsSettings);

        if (!srsModeEnabled || !settings.enabled || !window.srsManager || !window.srsManager.isReady()) {
            emptyStats.nextDue = settings.enabled ? 'SRS off' : 'Deck off';
            return emptyStats;
        }

        const dueCards = window.srsManager.getDueCards(cards, {
            maxNewCards: null,
            maxDueCards: null,
            allowMultipleSessions: true,
            settings
        });
        const stats = window.srsManager.getSRSStatistics(cards);

        return {
            ...stats,
            dueCards: dueCards.length,
            learningCards: stats.learningCards + stats.relearningCards,
            nextDue: getNextDueLabel(cards, dueCards.length)
        };
    }

    function getRetentionLast30Days(sets = flashcardSets) {
        const cutoff = Date.now() - (30 * 24 * 60 * 60 * 1000);
        let total = 0;
        let retained = 0;

        sets.forEach(set => {
            (set.cards || []).forEach(card => {
                (card.reviewHistory || []).forEach(review => {
                    const reviewedAt = new Date(review.reviewedAt || review.time || review.timestamp).getTime();
                    if (!Number.isFinite(reviewedAt) || reviewedAt < cutoff) return;

                    total += 1;
                    if (review.rating !== 'Again') {
                        retained += 1;
                    }
                });
            });
        });

        return total === 0 ? null : Math.round((retained / total) * 100);
    }

    function updateSRSDashboard(totals) {
        if (!srsDashboard) return;

        srsDashboard.hidden = !srsModeEnabled;
        srsDashboard.classList.toggle('srs-dashboard-disabled', !srsModeEnabled);

        if (!srsModeEnabled || !window.srsManager || !window.srsManager.isReady()) {
            if (srsNewCount) srsNewCount.textContent = '0';
            if (srsLearningCount) srsLearningCount.textContent = '0';
            if (srsReviewCount) srsReviewCount.textContent = '0';
            if (srsMatureCount) srsMatureCount.textContent = '0';
            if (srsRetention) srsRetention.textContent = '--';
            if (srsNextDue) srsNextDue.textContent = 'Turn on SRS';
            return;
        }

        if (srsNewCount) srsNewCount.textContent = String(totals.newCards);
        if (srsLearningCount) srsLearningCount.textContent = String(totals.learningCards);
        if (srsReviewCount) srsReviewCount.textContent = String(totals.reviewCards);
        if (srsMatureCount) srsMatureCount.textContent = String(totals.masteredCards);
        if (srsRetention) srsRetention.textContent = totals.retention === null ? '--' : `${totals.retention}%`;
        if (srsNextDue) srsNextDue.textContent = totals.nextDue;
    }

    function updateDueCardsCount() {
        const dueStatItem = dueCardsDisplay?.closest('.stat-item');
        if (dueStatItem) {
            dueStatItem.hidden = !srsModeEnabled;
        }

        if (!srsModeEnabled || !window.srsManager || !window.srsManager.isReady()) {
            if (dueCardsDisplay) {
                dueCardsDisplay.textContent = '0';
            }
            updateSRSDashboard({
                newCards: 0,
                learningCards: 0,
                reviewCards: 0,
                masteredCards: 0,
                nextDue: 'Turn on SRS'
            });
            firstDueSetId = null;
            updateReviewDueButton(0);
            updateLibrarySubtitle(null);
            return;
        }

        // Calculate due cards across all sets
        let totalDueCards = 0;
        let totalNewCards = 0;
        let totalLearningCards = 0;
        let totalReviewCards = 0;
        let totalMatureCards = 0;
        const allCards = [];
        firstDueSetId = null;

        flashcardSets.forEach(set => {
            if (set.cards && Array.isArray(set.cards)) {
                const settings = normalizeSrsSettings(set.srsSettings);
                if (!settings.enabled) return;

                allCards.push(...set.cards);
                const dueCards = window.srsManager.getDueCards(set.cards, {
                    maxNewCards: null,
                    maxDueCards: null,
                    allowMultipleSessions: true,
                    settings
                });
                totalDueCards += dueCards.length;
                if (dueCards.length > 0 && firstDueSetId === null) {
                    firstDueSetId = set.id;
                }

                // Also calculate statistics for display
                const stats = window.srsManager.getSRSStatistics(set.cards);
                totalNewCards += stats.newCards;
                totalLearningCards += stats.learningCards + stats.relearningCards;
                totalReviewCards += stats.reviewCards;
                totalMatureCards += stats.masteredCards;
            }
        });

        if (dueCardsDisplay) {
            dueCardsDisplay.textContent = totalDueCards.toString();
            // Update status text to show more details
            if (srsStatus) {
                const statusText = srsStatus.querySelector('.srs-status-text');
                if (statusText) {
                    statusText.textContent = 'SRS';
                }
            }
        }

        updateSRSDashboard({
            newCards: totalNewCards,
            learningCards: totalLearningCards,
            reviewCards: totalReviewCards,
            masteredCards: totalMatureCards,
            retention: getRetentionLast30Days(),
            nextDue: getNextDueLabel(allCards, totalDueCards)
        });
        updateReviewDueButton(totalDueCards);
        updateLibrarySubtitle(totalDueCards);
    }

    function updateReviewDueButton(totalDueCards) {
        if (!reviewDueBtn) return;

        const shouldShow = srsModeEnabled && totalDueCards > 0 && firstDueSetId !== null;
        reviewDueBtn.classList.toggle('hidden', !shouldShow);

        if (shouldShow) {
            const label = reviewDueBtn.querySelector('span');
            if (label) {
                label.textContent = `Review ${totalDueCards} Due`;
            }
        }
    }

    // Export SRS functions for global access
    window.getSRSMode = () => srsModeEnabled;
    window.setSRSMode = async (enabled) => {
        srsModeEnabled = enabled;
        if (srsToggle) {
            srsToggle.checked = enabled;
        }
        if (window.flashcardStore?.setState) {
            await window.flashcardStore.setState('srsModeEnabled', Boolean(enabled));
        } else {
            localStorage.setItem('srsModeEnabled', enabled.toString());
        }
        updateSRSStatus();
        updateDueCardsCount();
    };

    // Add debug function to show SRS details
    window.showSRSDetails = () => {

        flashcardSets.forEach((set, setIndex) => {
            if (window.srsManager && window.srsManager.isReady()) {
                const stats = window.srsManager.getSRSStatistics(set.cards);
                window.srsManager.logSRSDetails(set.cards);
            }
        });

    };
});
