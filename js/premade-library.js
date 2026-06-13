document.addEventListener('DOMContentLoaded', async () => {
    if (window.flashcardLocalReady) await window.flashcardLocalReady;
    // DOM Elements
    const classSelection = document.getElementById('class-selection');
    const subjectSelection = document.getElementById('subject-selection');
    const flashcardSetsDisplay = document.getElementById('flashcard-sets-display');
    const setsContainer = document.getElementById('sets-container');
    const flashcardSetTemplate = document.getElementById('flashcard-set-template');
    const emptyState = document.getElementById('empty-state');
    const searchInput = document.getElementById('search-input');
    const sortSelect = document.getElementById('sort-select');
    const addToSetModal = document.getElementById('add-to-set-modal');
    const settingsModal = document.getElementById('settings-modal');
    const totalSetsDisplay = document.getElementById('total-sets');
    const classNameDisplay = document.getElementById('class-name');
    const subjectNameDisplay = document.getElementById('subject-name');
    const cancelAddToSetBtn = document.getElementById('cancel-add-to-set');
    const confirmAddToSetBtn = document.getElementById('confirm-add-to-set');
    const settingsBtn = document.getElementById('settings-btn');
    const closeSettingsBtn = document.getElementById('close-settings-btn');
    const saveSettingsBtn = document.getElementById('save-settings');
    const resetSettingsBtn = document.getElementById('reset-settings');
    const contentFontSelect = document.getElementById('content-font');
    const customContentFontDiv = document.getElementById('custom-content-font');
    const contentFontUpload = document.getElementById('content-font-upload');

    // Navigation elements
    const classStat = document.getElementById('class-stat');
    const subjectStat = document.getElementById('subject-stat');
    const subjectGrid = document.getElementById('subject-grid');

    // State
    let currentClass = null;
    let currentSubject = null;
    let flashcardSets = [];
    let setToAdd = null;
    let customFonts = {
        content: null
    };

    const classLabels = {
        '10th': 'Class 10th',
        '11th': 'Class 11th',
        '12th': 'Class 12th',
        'neet-ug': 'NEET UG',
        'jee-main': 'JEE Main',
        'jee-advanced': 'JEE Advanced',
        'ssc': 'SSC'
    };

    // Subject definitions for each class
    const subjectsByClass = {
        '10th': [
            { id: 'Science', name: 'Science', icon: 'fas fa-flask', description: 'Physics, Chemistry, Biology' },
            { id: 'Maths', name: 'Mathematics', icon: 'fas fa-calculator', description: 'Algebra, Geometry, Statistics' },
            { id: 'English', name: 'English', icon: 'fas fa-book', description: 'Literature, Grammar, Writing' },
            { id: 'Civics', name: 'Civics', icon: 'fas fa-landmark', description: 'Government, Constitution, Rights' },
            { id: 'Geography', name: 'Geography', icon: 'fas fa-globe', description: 'Physical & Human Geography' },
            { id: 'History', name: 'History', icon: 'fas fa-monument', description: 'World & Indian History' },
            { id: 'Hindi', name: 'Hindi', icon: 'fas fa-language', description: 'Hindi Literature & Grammar' },
            { id: 'Politics', name: 'Politics', icon: 'fas fa-vote-yea', description: 'Political Science' }
        ],
        '11th': [
            { id: 'Physics', name: 'Physics', icon: 'fas fa-atom', description: 'Mechanics, Thermodynamics, Waves' },
            { id: 'inorganic-chemistry', name: 'Inorganic Chemistry', icon: 'fas fa-vial', description: 'Elements, Compounds, Reactions' },
            { id: 'organic-chemistry', name: 'Organic Chemistry', icon: 'fas fa-flask', description: 'Carbon Compounds, Reactions' },
            { id: 'physical-chemistry', name: 'Physical Chemistry', icon: 'fas fa-microscope', description: 'Kinetics, Thermodynamics' },
            { id: 'English', name: 'English', icon: 'fas fa-book', description: 'Literature, Grammar, Writing' },
            { id: 'Maths', name: 'Mathematics', icon: 'fas fa-calculator', description: 'Algebra, Calculus, Statistics' },
            { id: 'Biology', name: 'Biology', icon: 'fas fa-dna', description: 'Botany, Zoology, Human Biology' },
            { id: 'Physical-education', name: 'Physical Education', icon: 'fas fa-running', description: 'Sports, Health, Fitness' }
        ],
        '12th': [
            { id: 'Physics', name: 'Physics', icon: 'fas fa-atom', description: 'Electromagnetism, Optics, Modern Physics' },
            { id: 'inorganic-chemistry', name: 'Inorganic Chemistry', icon: 'fas fa-vial', description: 'Elements, Compounds, Reactions' },
            { id: 'organic-chemistry', name: 'Organic Chemistry', icon: 'fas fa-flask', description: 'Carbon Compounds, Reactions' },
            { id: 'physical-chemistry', name: 'Physical Chemistry', icon: 'fas fa-microscope', description: 'Kinetics, Thermodynamics' },
            { id: 'English', name: 'English', icon: 'fas fa-book', description: 'Literature, Grammar, Writing' },
            { id: 'Maths', name: 'Mathematics', icon: 'fas fa-calculator', description: 'Algebra, Calculus, Statistics' },
            { id: 'Biology', name: 'Biology', icon: 'fas fa-dna', description: 'Botany, Zoology, Human Biology' },
            { id: 'Physical-education', name: 'Physical Education', icon: 'fas fa-running', description: 'Sports, Health, Fitness' }
        ],
        'neet-ug': [
            { id: 'Physics', name: 'Physics', icon: 'fas fa-atom', description: 'Mechanics, electricity, optics, modern physics' },
            { id: 'Chemistry', name: 'Chemistry', icon: 'fas fa-flask', description: 'Physical, organic, and inorganic chemistry' },
            { id: 'Biology', name: 'Biology', icon: 'fas fa-dna', description: 'Botany, zoology, and human biology' }
        ],
        'jee-main': [
            { id: 'Physics', name: 'Physics', icon: 'fas fa-atom', description: 'JEE Main physics practice' },
            { id: 'Chemistry', name: 'Chemistry', icon: 'fas fa-flask', description: 'JEE Main chemistry practice' },
            { id: 'Maths', name: 'Mathematics', icon: 'fas fa-calculator', description: 'JEE Main mathematics practice' }
        ],
        'jee-advanced': [
            { id: 'Physics', name: 'Physics', icon: 'fas fa-atom', description: 'Advanced physics practice' },
            { id: 'Chemistry', name: 'Chemistry', icon: 'fas fa-flask', description: 'Advanced chemistry practice' },
            { id: 'Maths', name: 'Mathematics', icon: 'fas fa-calculator', description: 'Advanced mathematics practice' }
        ],
        'ssc': [
            { id: 'general-awareness', name: 'General Awareness', icon: 'fas fa-landmark', description: 'Static GK, current affairs, polity, history, geography' },
            { id: 'quantitative-aptitude', name: 'Quantitative Aptitude', icon: 'fas fa-calculator', description: 'Arithmetic, algebra, geometry, and data interpretation' },
            { id: 'reasoning', name: 'Reasoning', icon: 'fas fa-brain', description: 'Verbal and non-verbal reasoning' },
            { id: 'english', name: 'English', icon: 'fas fa-book', description: 'Vocabulary, grammar, and comprehension' }
        ]
    };

    // Initialize the application
    function initialize() {
        showClassSelection();
        applyStoredSettings();
        setupEventListeners();
    }

    // Show class selection screen
    function showClassSelection() {
        classSelection.classList.remove('hidden');
        subjectSelection.classList.add('hidden');
        flashcardSetsDisplay.classList.add('hidden');
        
        // Reset state
        currentClass = null;
        currentSubject = null;
        flashcardSets = [];
        
        // Update header stats
        classNameDisplay.textContent = 'Select Class';
        subjectNameDisplay.textContent = 'Select Subject';
        totalSetsDisplay.textContent = '0';
        
        // Update stat item styles
        classStat.style.opacity = '0.6';
        subjectStat.style.opacity = '0.6';
    }

    // Show subject selection screen
    function showSubjectSelection(selectedClass) {
        currentClass = selectedClass;
        
        classSelection.classList.add('hidden');
        subjectSelection.classList.remove('hidden');
        flashcardSetsDisplay.classList.add('hidden');
        
        // Update header stats
        classNameDisplay.textContent = classLabels[selectedClass] || selectedClass;
        subjectNameDisplay.textContent = 'Select Subject';
        totalSetsDisplay.textContent = '0';
        
        // Update stat item styles
        classStat.style.opacity = '1';
        subjectStat.style.opacity = '0.6';
        
        // Populate subjects
        populateSubjects(selectedClass);
    }

    // Show flashcard sets display
    function showFlashcardSets(selectedSubject) {
        currentSubject = selectedSubject;
        
        classSelection.classList.add('hidden');
        subjectSelection.classList.add('hidden');
        flashcardSetsDisplay.classList.remove('hidden');
        
        // Update header stats
        subjectNameDisplay.textContent = selectedSubject;
        
        // Update stat item styles
        classStat.style.opacity = '1';
        subjectStat.style.opacity = '1';
        
        // Load and display flashcard sets
        loadFlashcardSets(currentClass, selectedSubject);
    }

    // Populate subjects for the selected class
    function populateSubjects(selectedClass) {
        const subjects = subjectsByClass[selectedClass] || [];
        subjectGrid.innerHTML = '';
        
        subjects.forEach(subject => {
            const subjectCard = document.createElement('div');
            subjectCard.className = 'subject-card';
            subjectCard.dataset.subject = subject.id;
            
            subjectCard.innerHTML = `
                <div class="subject-icon">
                    <i class="${subject.icon}"></i>
                </div>
                <h3>${subject.name}</h3>
                <p>${subject.description}</p>
            `;
            
            subjectCard.addEventListener('click', () => {
                showFlashcardSets(subject.name);
            });
            
            subjectGrid.appendChild(subjectCard);
        });
    }

    // Load flashcard sets for a specific class and subject
    async function loadFlashcardSets(selectedClass, selectedSubject) {
        try {
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
                'Chemistry': 'chemistry',
                'Inorganic Chemistry': 'inorganic-chemistry',
                'Organic Chemistry': 'organic-chemistry',
                'Physical Chemistry': 'physical-chemistry',
                'Biology': 'Biology',
                'Physical Education': 'Physical-education',
                'General Awareness': 'general-awareness',
                'Quantitative Aptitude': 'quantitative-aptitude',
                'Reasoning': 'reasoning'
            };
            
            const folderName = subjectFolderMap[selectedSubject] || selectedSubject;
            const folderPath = `Premade-cards/${selectedClass}/${folderName}`;
            
            // Get known files for this subject
            const knownFiles = getKnownFiles(selectedClass, folderName);
            
            if (knownFiles.length === 0) {
                showEmptyState();
                return;
            }

            // Load all flashcard sets
            const sets = [];
            
            for (const fileName of knownFiles) {
                try {
                    const setData = await loadFlashcardSetData(folderPath, fileName);
            if (setData) {
                        // Add the filename to the set data so we can use it later
                        setData.fileName = fileName;
                        sets.push(setData);
                    }
                } catch (error) {
                    console.warn(`Failed to load ${fileName}:`, error);
                }
            }
            
            flashcardSets = sets;
            updateLibraryStats();
            renderSets();
            
        } catch (error) {
            console.error('Error loading flashcard sets:', error);
            showToast('Error loading flashcard sets', 'error');
            showEmptyState();
        }
    }

    // Get known files for a subject (this would ideally be dynamic)
    function getKnownFiles(selectedClass, folderName) {
        // This is a simplified approach - in reality, you'd want a server endpoint
        // that lists the files in the directory
        const knownFiles = {
            'Biology': ['Allbotanyexamplesexceptecology-neetug.json', 'Anatomyoffloweringplants-neetug.json', 'completeecology-neetug.json', 'Morphologyoffloweringplants-neetug.json', 'cell-biology.json'],
            'Science': ['basic-physics.json', 'basic-chemistry.json'],
            'Maths': ['algebra-basics.json'],
            'English': ['grammar-basics.json'],
            'Civics': [],
            'Geography': [],
            'History': ['indian-independence.json'],
            'Hindi': [],
            'Politics': [],
            'Physics': [],
            'chemistry': [],
            'inorganic-chemistry': [],
            'organic-chemistry': [],
            'physical-chemistry': [],
            'Physical-education': [],
            'general-awareness': [],
            'quantitative-aptitude': [],
            'reasoning': [],
            'english': []
        };
        
        return knownFiles[folderName] || [];
    }

    // Load individual flashcard set data
    async function loadFlashcardSetData(folderPath, fileName) {
        try {
            const fullPath = `${folderPath}/${fileName}`;
            const response = await fetch(fullPath);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status} for ${fullPath}`);
            }
            return await response.json();
        } catch (error) {
            console.error(`Error loading ${fileName}:`, error);
            return null;
        }
    }

    // Update library statistics
    function updateLibraryStats() {
        totalSetsDisplay.textContent = flashcardSets.length;
    }

    // Render flashcard sets
    function renderSets(searchTerm = '') {
        const filteredSets = filterSets(searchTerm);
        const sortedSets = sortSets(filteredSets);

        // Clear container completely first
        setsContainer.innerHTML = '';
        
        // Add empty state if needed
        if (sortedSets.length === 0) {
            emptyState.style.display = 'flex';
        } else {
            emptyState.style.display = 'none';
            
            // Add each set card
            sortedSets.forEach(set => {
                const card = createFlashcardSetCard(set);
                setsContainer.appendChild(card);
            });
        }
    }

    // Create flashcard set card
    function createFlashcardSetCard(set) {
        const card = flashcardSetTemplate.content.cloneNode(true).querySelector('.set-card');
        
        // Set content
        card.querySelector('.set-name').textContent = set.name;
        card.querySelector('.card-count').textContent = `${set.cards ? set.cards.length : 0} cards`;
        card.querySelector('.difficulty-level').textContent = set.difficulty || 'intermediate';
        card.querySelector('.estimated-time').textContent = set.estimatedTime || '45 minutes';
        card.querySelector('.set-description').textContent = set.description || '';
        
        // Add tags
        const tagsContainer = card.querySelector('.set-tags');
        if (set.tags && set.tags.length > 0) {
            set.tags.forEach(tag => {
                const tagElement = document.createElement('span');
                tagElement.className = 'topic-tag';
                tagElement.textContent = tag;
                tagsContainer.appendChild(tagElement);
            });
        }

        // Action buttons
        card.querySelector('.study-btn').addEventListener('click', (e) => {
            e.preventDefault();
            
            // Use the filename instead of the set.id
            const fileName = set.fileName || set.id;
            const studyUrl = `study.html?premade=true&class=${currentClass}&subject=${currentSubject}&set=${fileName}`;
            window.location.href = studyUrl;
        });

        card.querySelector('.add-to-set-btn').addEventListener('click', (e) => {
            e.preventDefault();
            setToAdd = set;
            showAddToSetModal();
        });

        return card;
    }

    // Filter sets based on search
    function filterSets(searchTerm) {
        if (!searchTerm) return flashcardSets;
        
        const term = searchTerm.toLowerCase();
        return flashcardSets.filter(set => 
            set.name.toLowerCase().includes(term) ||
            (set.description && set.description.toLowerCase().includes(term)) ||
            (set.tags && set.tags.some(tag => tag.toLowerCase().includes(term)))
        );
    }

    // Sort sets based on selected option
    function sortSets(sets) {
        const sortBy = sortSelect.value;
        
        return [...sets].sort((a, b) => {
            switch (sortBy) {
                case 'name':
                    return a.name.localeCompare(b.name);
                case 'cards':
                    return (b.cards ? b.cards.length : 0) - (a.cards ? a.cards.length : 0);
                case 'difficulty':
                    const difficultyOrder = { 'basic': 1, 'intermediate': 2, 'advanced': 3 };
                    return (difficultyOrder[a.difficulty] || 2) - (difficultyOrder[b.difficulty] || 2);
                case 'time':
                    const timeA = parseInt(a.estimatedTime) || 45;
                    const timeB = parseInt(b.estimatedTime) || 45;
                    return timeA - timeB;
                default:
                    return 0;
            }
        });
    }

    // Add to set modal
    function showAddToSetModal() {
        addToSetModal.classList.remove('hidden');
        addToSetModal.classList.add('visible');
    }

    function hideAddToSetModal() {
        addToSetModal.classList.remove('visible');
        setTimeout(() => addToSetModal.classList.add('hidden'), 300);
    }

    // Add premade set to user's library
    async function addToUserLibrary() {
        if (!setToAdd) return;
        
        try {
            // Create a new set for user's library
            const newSet = {
                id: Date.now(),
                name: `${setToAdd.name} (Copied)`,
                description: setToAdd.description || '',
                cards: setToAdd.cards ? setToAdd.cards.map(card => ({
                    term: card.term,
                    definition: card.definition,
                    termImage: card.termImage || '',
                    definitionImage: card.definitionImage || ''
                })) : [],
                created: Date.now(),
                lastModified: Date.now(),
                openedCount: 0,
                isPremadeCopy: true,
                originalPremadeId: setToAdd.id
            };
            
            if (window.flashcardStore?.saveSet) {
                await window.flashcardStore.saveSet(newSet);
            } else {
                const existingSets = JSON.parse(localStorage.getItem('flashcardSets') || '[]');
                existingSets.push(newSet);
                localStorage.setItem('flashcardSets', JSON.stringify(existingSets));
            }
            
            hideAddToSetModal();
            showToast(`Successfully added "${setToAdd.name}" to your library`, 'success');
            
            // Clear the reference
            setToAdd = null;
        } catch (error) {
            console.error('Error adding set to library:', error);
            showToast('Error adding set to library', 'error');
            hideAddToSetModal();
        }
    }

    // Show empty state
    function showEmptyState() {
        setsContainer.innerHTML = '';
        emptyState.style.display = 'flex';
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

    function applyStoredSettings() {
        if (window.loadAndApplySettings) {
            window.loadAndApplySettings();
        }
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

    function loadSettingsValues() {
        // Load saved settings from localStorage
        const defaultSettings = {
            fonts: {
                content: "'Plus Jakarta Sans', sans-serif"
            }
        };
        
        // Load saved settings or use defaults
        const savedSettings = JSON.parse(localStorage.getItem('flashcards-settings') || '{}');
        const userSettings = { ...defaultSettings, ...savedSettings };
        
        // Set font dropdown values
        if (userSettings.fonts) {
            if (userSettings.fonts.content.startsWith('custom-')) {
                contentFontSelect.value = 'custom';
                customContentFontDiv.classList.remove('hidden');
            } else {
                contentFontSelect.value = userSettings.fonts.content;
            }
        }
        
    }
    
    function saveSettings() {
        // Get saved settings to update or use defaults
        const defaultSettings = {
            fonts: {
                content: "'Plus Jakarta Sans', sans-serif"
            }
        };
        
        // Load existing settings if available
        const existingSettings = JSON.parse(localStorage.getItem('flashcards-settings') || '{}');
        const userSettings = { ...defaultSettings, ...existingSettings };
        
        // Update font settings
        if (contentFontSelect.value === 'custom' && customFonts.content) {
            userSettings.fonts.content = 'custom-' + customFonts.content.name;
        } else {
            userSettings.fonts.content = contentFontSelect.value;
        }
        
        // Save to localStorage
        localStorage.setItem('flashcards-settings', JSON.stringify(userSettings));
        
        // Apply settings using the functions from settings.js
        if (window.loadAndApplySettings) {
            window.loadAndApplySettings();
        } else {
            // Fallback implementation if settings.js functions are not available
            const fontStyle = document.getElementById('custom-fonts') || document.createElement('style');
            fontStyle.id = 'custom-fonts';
            document.head.appendChild(fontStyle);
            
            const selectedFont = contentFontSelect.value;
            fontStyle.textContent = `
                .flashcard .card-face .term-text,
                .flashcard .card-face .definition-text {
                    font-family: ${selectedFont} !important;
                }
            `;
        }
        
        // Show feedback
        showToast('Settings saved successfully', 'success');
        hideSettingsModal();
    }
    
    function resetSettings() {
        // Default settings
        const defaultSettings = {
            fonts: {
                content: "'Plus Jakarta Sans', sans-serif"
            }
        };
        
        // Update UI
        contentFontSelect.value = defaultSettings.fonts.content;
        
        // Hide custom font uploads
        customContentFontDiv.classList.add('hidden');
        
        // Clear custom fonts
        customFonts = {
            content: null
        };
        
        // Apply default settings
        localStorage.setItem('flashcards-settings', JSON.stringify(defaultSettings));
        
        // Apply settings using the functions from settings.js
        if (typeof loadAndApplySettings === 'function') {
            loadAndApplySettings();
        }
        
        showToast('Settings reset to default', 'info');
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

    // Setup event listeners
    function setupEventListeners() {
        // Class selection
        document.querySelectorAll('.class-card').forEach(card => {
            card.addEventListener('click', () => {
                const selectedClass = card.dataset.class;
                showSubjectSelection(selectedClass);
            });
        });

        // Navigation buttons using stat items
        classStat.addEventListener('click', () => {
            if (currentClass) {
                showClassSelection();
            }
        });
        
        subjectStat.addEventListener('click', () => {
            if (currentSubject && currentClass) {
                showSubjectSelection(currentClass);
            }
        });

        // Search and sort
    searchInput.addEventListener('input', () => renderSets(searchInput.value));
    sortSelect.addEventListener('change', () => renderSets(searchInput.value));
    
    // Add to Set Modal Listeners
    cancelAddToSetBtn.addEventListener('click', hideAddToSetModal);
    confirmAddToSetBtn.addEventListener('click', addToUserLibrary);
    
    // Close modals when clicking outside
    addToSetModal.addEventListener('click', (e) => {
        if (e.target === addToSetModal) hideAddToSetModal();
    });

    // Settings Modal Event Listeners
    settingsBtn.addEventListener('click', showSettingsModal);
    closeSettingsBtn.addEventListener('click', hideSettingsModal);
    saveSettingsBtn.addEventListener('click', saveSettings);
    resetSettingsBtn.addEventListener('click', resetSettings);
    
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
    }

    // Initialize the application
    initialize();
});
