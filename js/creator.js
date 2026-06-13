document.addEventListener('DOMContentLoaded', async () => {
    if (window.flashcardLocalReady) await window.flashcardLocalReady;
    // Apply theme settings first to prevent flash of unstyled content
    applyThemeSettings();
    
    // DOM Elements
    const cardsContainer = document.getElementById('cards-container');
    const addCardBtn = document.getElementById('add-card-btn');
    const saveSetBtn = document.getElementById('save-set-btn');
    const setNameInput = document.getElementById('set-name');
    const setClassSelect = document.getElementById('set-class-select');
    const cardCountSpan = document.querySelector('.card-count');
    const cardTemplate = document.getElementById('card-template');
    const floatingAddBtn = document.getElementById('floating-add-btn');
    const backButton = document.getElementById('back-button');
    const backButtonText = document.getElementById('back-button-text');
    const creatorClassModal = document.getElementById('creator-class-modal');
    const creatorClassNameInput = document.getElementById('creator-class-name');
    const creatorClassColorInput = document.getElementById('creator-class-color');
    const closeCreatorClassBtn = document.getElementById('close-creator-class');
    const cancelCreatorClassBtn = document.getElementById('cancel-creator-class');
    const saveCreatorClassBtn = document.getElementById('save-creator-class');

    // Constants
    const AUTOSAVE_DELAY = 1000; // 1 second
    const DRAFT_SAVE_DELAY = 3000; // 3 seconds
    // IMAGE_MAX_SIZE constant removed as we're not restricting image sizes
    const DRAFT_STORAGE_KEY = 'flashcardSetDraft';

    // State
    let autoSaveTimeout = null;
    let draftSaveTimeout = null;
    let editMode = false;
    let editSetId = null;
    let existingSetData = null;
    let documentClickListener = null;
    let draftLoaded = false;
    let draftWritesSuppressed = false;
    let successfulSaveRedirecting = false;
    let flashcardClasses = [];
    let classForCreatorEditor = null;
    const MEDIA_ACCEPT = 'image/*,audio/*,video/*';
    const BACKGROUND_ACCEPT = 'image/*';
    const clickSound = new Audio('assets/flashcard-assets/click.mp3');
    clickSound.volume = 0.3;

    function playClickSound() {
        clickSound.currentTime = 0;
        clickSound.play().catch(() => {});
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

    function mediaIcon(kind) {
        if (kind === 'audio') return 'fa-volume-high';
        if (kind === 'video') return 'fa-film';
        return 'fa-image';
    }

    function escapeAttribute(value) {
        return String(value ?? '')
            .replace(/&/g, '&amp;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#039;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;');
    }

    function escapeText(value) {
        return String(value ?? '')
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;');
    }

    function getSideKeyFromElement(sideElement) {
        return sideElement?.classList?.contains('definition-side') ? 'definition' : 'term';
    }

    function ensureCardMediaState(cardElement) {
        cardElement.__cardData = cardElement.__cardData || {};
        cardElement.__cardData.media = normalizeCardMedia(cardElement.__cardData);
        cardElement.__cardData.background = normalizeCardBackground(cardElement.__cardData);
        return cardElement.__cardData;
    }

    function cardHasContent(card = {}) {
        const media = normalizeCardMedia(card.media || {});
        const background = normalizeCardBackground(card);
        return Boolean(
            String(card.term || '').trim() ||
            String(card.definition || '').trim() ||
            card.termImage ||
            card.definitionImage ||
            media.term.length ||
            media.definition.length ||
            background.term ||
            background.definition
        );
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

    async function loadFlashcardClasses(selectedValue = '') {
        const classes = window.flashcardStore?.listClasses
            ? await window.flashcardStore.listClasses()
            : JSON.parse(localStorage.getItem('flashcardClasses') || '[]');
        flashcardClasses = Array.isArray(classes) ? classes.map(normalizeClassRecord) : [];
        populateClassSelect(selectedValue);
    }

    function populateClassSelect(selectedValue = '') {
        if (!setClassSelect) return;
        const valueToSelect = selectedValue ?? setClassSelect.value ?? '';
        setClassSelect.innerHTML = '<option value="">General</option>';
        flashcardClasses.forEach(classItem => {
            const option = document.createElement('option');
            option.value = classItem.id;
            option.textContent = classItem.name;
            setClassSelect.appendChild(option);
        });
        const newOption = document.createElement('option');
        newOption.value = '__new';
        newOption.textContent = '+ New Class';
        setClassSelect.appendChild(newOption);
        const finalValue = [...setClassSelect.options].some(option => option.value === valueToSelect) ? valueToSelect : '';
        setClassSelect.value = finalValue;
        
        if (editClassBtn) {
            editClassBtn.style.display = (finalValue && finalValue !== '__new') ? 'inline-flex' : 'none';
        }
    }

    function showCreatorClassModal(classItem = null) {
        if (!creatorClassModal) return;
        classForCreatorEditor = classItem;
        
        const modalTitle = creatorClassModal.querySelector('h2');
        if (modalTitle) {
            modalTitle.textContent = classItem ? 'Edit Class' : 'New Class';
        }
        
        const submitBtnText = creatorClassModal.querySelector('#save-creator-class span');
        if (submitBtnText) {
            submitBtnText.textContent = classItem ? 'Save Class' : 'Create Class';
        }

        const deleteBtn = creatorClassModal.querySelector('#delete-creator-class');
        if (deleteBtn) {
            deleteBtn.classList.toggle('hidden', !classItem);
        }
        
        if (setClassSelect) setClassSelect.value = classItem?.id || '';
        if (creatorClassNameInput) creatorClassNameInput.value = classItem?.name || '';
        if (creatorClassColorInput) creatorClassColorInput.value = classItem?.color || '#3B82F6';
        
        // Highlight active icon
        const activeIcon = classItem?.icon || 'fa-graduation-cap';
        const iconGrid = document.getElementById('creator-class-icon-grid');
        if (iconGrid) {
            iconGrid.querySelectorAll('.icon-btn').forEach(btn => {
                btn.classList.toggle('active', btn.getAttribute('data-icon') === activeIcon);
            });
        }
        
        creatorClassModal.classList.add('show');
        setTimeout(() => creatorClassNameInput?.focus(), 40);
    }

    function hideCreatorClassModal() {
        creatorClassModal?.classList.remove('show');
        if (setClassSelect?.value === '__new') setClassSelect.value = '';
    }

    async function saveCreatorClassFromModal() {
        const name = creatorClassNameInput?.value.trim();
        if (!name) {
            showToast('Please enter a class name', 'error');
            creatorClassNameInput?.focus();
            return;
        }

        const color = /^#[0-9a-f]{6}$/i.test(String(creatorClassColorInput?.value || ''))
            ? creatorClassColorInput.value
            : '#3B82F6';
            
        // Get active icon
        const activeIconBtn = document.querySelector('#creator-class-icon-grid .icon-btn.active');
        const icon = activeIconBtn ? activeIconBtn.getAttribute('data-icon') : 'fa-graduation-cap';
        
        try {
            const classData = normalizeClassRecord({
                ...(classForCreatorEditor || {}),
                name,
                color,
                icon
            });
            const savedClass = window.flashcardStore?.saveClass
                ? await window.flashcardStore.saveClass(classData)
                : classData;

            if (!window.flashcardStore?.saveClass) {
                const updated = flashcardClasses.filter(item => String(item.id) !== String(savedClass.id));
                updated.push(savedClass);
                localStorage.setItem('flashcardClasses', JSON.stringify(updated));
            }

            await loadFlashcardClasses(savedClass.id);
            const editClassBtn = document.getElementById('edit-class-btn');
            if (editClassBtn) editClassBtn.style.display = 'inline-flex';
            hideCreatorClassModal();
            playClickSound();
            saveDraft();
            showToast(classForCreatorEditor ? 'Class updated' : 'Class created', 'success');
        } catch (error) {
            console.error('Error creating class:', error);
            setClassSelect.value = '';
            showToast('Could not create class', 'error');
        }
    }
    
    // Add references to draft modal elements
    const draftModal = document.getElementById('draft-modal');
    const continueDraftBtn = document.getElementById('continue-draft-btn');
    const deleteDraftBtn = document.getElementById('delete-draft-btn');
    const closeDraftBtn = document.querySelector('.close-draft-btn');

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

    function isTypingTarget(target) {
        return Boolean(target?.closest?.('input, textarea, select, [contenteditable="true"]'));
    }

    function closeVisibleCreatorOverlay() {
        let closed = false;

        document.querySelectorAll('.bulk-input-dropdown').forEach(dropdown => {
            dropdown.remove();
            closed = true;
        });

        document.querySelectorAll('.shortcuts-modal.show').forEach(modal => {
            if (modal.id === 'draft-modal') {
                hideDraftModal();
            } else {
                modal.classList.remove('show');
            }
            closed = true;
        });

        return closed;
    }

    function scrollToCard(cardElement) {
        if (!cardElement) return;
        setTimeout(() => {
            cardElement.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }, 100);
    }

    // Add keyboard shortcuts for desktop app
    document.addEventListener('keydown', (e) => {
        const isMod = e.ctrlKey || e.metaKey;
        const key = e.key.toLowerCase();
        const typing = isTypingTarget(e.target);

        if (key === 'escape' && closeVisibleCreatorOverlay()) {
            e.preventDefault();
            return;
        }

        if (!isMod || e.altKey) return;

        // Save set: Ctrl+S or Cmd+S
        if (key === 's') {
            e.preventDefault();
            if (!saveSetBtn.disabled) {
                saveSetBtn.click();
            }
            return;
        }

        // Add bulk cards: Ctrl+Shift+N or Cmd+Shift+N
        if (key === 'n' && e.shiftKey && !typing) {
            e.preventDefault();
            addCardBtn.click();
            return;
        }

        // Add single card: Ctrl+N or Cmd+N
        if (key === 'n' && !typing) {
            e.preventDefault();
            scrollToCard(addCard());
            return;
        }

        // Delete current card: Ctrl+Delete or Cmd+Delete
        if (key === 'delete') {
            // Find the currently focused card
            const activeElement = document.activeElement;
            const cardElement = activeElement?.closest?.('.card-editor');
            if (cardElement) {
                e.preventDefault();
                const deleteBtn = cardElement.querySelector('.delete-card');
                if (deleteBtn) {
                    deleteBtn.click();
                }
            }
            return;
        }

        // Import: Ctrl+O or Cmd+O
        if (key === 'o') {
            e.preventDefault();
            importSet();
            return;
        }

        // Export: Ctrl+E or Cmd+E
        if (key === 'e') {
            e.preventDefault();
            exportSet();
        }
    });

    // Theme Switcher Functions
    function applyFallbackTheme(theme) {
        if (window.loadAndApplySettings) {
            window.loadAndApplySettings();
        } else if (window.applyTheme) {
            window.applyTheme(theme);
        } else {
            document.documentElement.setAttribute('data-theme', theme);
        }
    }

    if (window.loadAndApplySettings) {
        window.loadAndApplySettings();
    } else {
        applyFallbackTheme(localStorage.getItem('flashcards-theme') || 'dark');
    }

    // Add event listeners
    addCardBtn.addEventListener('click', () => {
        // Remove any existing dropdown
        const existingDropdown = document.querySelector('.bulk-input-dropdown');
        if (existingDropdown) {
            existingDropdown.remove();
            return;
        }
        
        // Create a small dropdown input
        const dropdown = document.createElement('div');
        dropdown.className = 'bulk-input-dropdown';
        
        // Position it next to the button
        const buttonRect = addCardBtn.getBoundingClientRect();
        dropdown.style.top = `${buttonRect.bottom + window.scrollY + 5}px`;
        dropdown.style.left = `${buttonRect.left + window.scrollX}px`;
        
        dropdown.innerHTML = `
            <input type="number" min="1" max="50" value="5" placeholder="How many?">
            <button class="add-btn"><i class="fas fa-plus"></i></button>
        `;
        
        document.body.appendChild(dropdown);
        
        // Focus the input
        const input = dropdown.querySelector('input');
        input.focus();
        input.select();
        
        // Handle add button click
        const addBtn = dropdown.querySelector('.add-btn');
        addBtn.addEventListener('click', addCards);
        
        // Handle Enter key press
        input.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                addCards();
            } else if (e.key === 'Escape') {
                dropdown.remove();
            }
        });
        
        // Close when clicking outside
        document.addEventListener('click', closeDropdownOnClickOutside);
        
        function closeDropdownOnClickOutside(e) {
            if (!dropdown.contains(e.target) && e.target !== addCardBtn) {
                dropdown.remove();
                document.removeEventListener('click', closeDropdownOnClickOutside);
            }
        }
        
        function addCards() {
            const count = parseInt(input.value) || 0;
            if (count > 0 && count <= 50) {
                // Add the specified number of cards
                const lastCard = addBulkCards(count);
                // Close dropdown
                dropdown.remove();
                document.removeEventListener('click', closeDropdownOnClickOutside);
                // Scroll to the first new card
                if (lastCard) {
                    setTimeout(() => {
                        lastCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    }, 100);
                }
            } else {
                showToast('Please enter a number between 1 and 50', 'error');
                input.focus();
            }
        }
    });
    saveSetBtn.addEventListener('click', async (e) => {
        e.preventDefault();
        
        // Disable button and show saving indicator
        saveSetBtn.disabled = true;
        saveSetBtn.querySelector('span').textContent = 'Saving...';
        
        try {
            const saved = await saveSet();
            
            // If saveSet returns false, it means there was an error
            if (!saved) {
                saveSetBtn.disabled = false;
                saveSetBtn.querySelector('span').textContent = editMode ? 'Save Changes' : 'Save Set';
            }
            // If saved is true, we'll redirect away from this page so no need to reset the button
        } catch (error) {
            console.error('Error saving set:', error);
            showToast('Error saving flashcard set', 'error');
            
            // Always make sure button is re-enabled on error
            saveSetBtn.disabled = false;
            saveSetBtn.querySelector('span').textContent = editMode ? 'Save Changes' : 'Save Set';
        }
    });
    setNameInput.addEventListener('input', triggerAutosave);
    setNameInput.addEventListener('input', saveDraft);
    const editClassBtn = document.getElementById('edit-class-btn');
    const deleteCreatorClassBtn = document.getElementById('delete-creator-class');
    
    if (setClassSelect) {
        setClassSelect.addEventListener('change', () => {
            const val = setClassSelect.value;
            if (editClassBtn) {
                editClassBtn.style.display = (val && val !== '__new') ? 'inline-flex' : 'none';
            }
            playClickSound();
            if (val === '__new') {
                showCreatorClassModal();
            } else {
                saveDraft();
            }
        });
    }

    if (editClassBtn) {
        editClassBtn.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            const classId = setClassSelect.value;
            const classItem = flashcardClasses.find(c => String(c.id) === String(classId));
            if (classItem) {
                showCreatorClassModal(classItem);
            }
        });
    }

    if (deleteCreatorClassBtn) {
        deleteCreatorClassBtn.addEventListener('click', async (e) => {
            e.preventDefault();
            e.stopPropagation();
            if (!classForCreatorEditor) return;
            
            try {
                if (window.flashcardStore?.deleteClass) {
                    await window.flashcardStore.deleteClass(classForCreatorEditor.id);
                } else {
                    const currentClasses = JSON.parse(localStorage.getItem('flashcardClasses') || '[]');
                    const updatedClasses = currentClasses.filter(c => String(c.id) !== String(classForCreatorEditor.id));
                    localStorage.setItem('flashcardClasses', JSON.stringify(updatedClasses));
                    
                    const currentSets = JSON.parse(localStorage.getItem('flashcardSets') || '[]');
                    const updatedSets = currentSets.map(set => 
                        String(set.classId || '') === String(classForCreatorEditor.id) ? { ...set, classId: null } : set
                    );
                    localStorage.setItem('flashcardSets', JSON.stringify(updatedSets));
                }

                await loadFlashcardClasses('');
                if (editClassBtn) editClassBtn.style.display = 'none';
                hideCreatorClassModal();
                playClickSound();
                saveDraft();
                showToast('Class deleted', 'success');
            } catch (err) {
                console.error('Error deleting class:', err);
                showToast('Could not delete class', 'error');
            }
        });
    }
    closeCreatorClassBtn?.addEventListener('click', hideCreatorClassModal);
    cancelCreatorClassBtn?.addEventListener('click', hideCreatorClassModal);
    saveCreatorClassBtn?.addEventListener('click', saveCreatorClassFromModal);
    
    // Creator Class Modal Icon Selection Listener
    const creatorClassIconGrid = document.getElementById('creator-class-icon-grid');
    if (creatorClassIconGrid) {
        creatorClassIconGrid.addEventListener('click', (e) => {
            const btn = e.target.closest('.icon-btn');
            if (!btn) return;
            creatorClassIconGrid.querySelectorAll('.icon-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            playClickSound();
        });
    }
    
    creatorClassNameInput?.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {
            event.preventDefault();
            saveCreatorClassFromModal();
        }
    });
    cardsContainer.addEventListener('input', saveDraft);
    
    // Floating add button event listener
    if (floatingAddBtn) {
        floatingAddBtn.addEventListener('click', () => {
            const newCard = addCard();
            // Scroll to the new card with smooth animation
            if (newCard) {
                setTimeout(() => {
                    newCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }, 100);
            }
        });
    }

    // Check if we're in edit mode
    const urlParams = new URLSearchParams(window.location.search);
    const setId = urlParams.get('setId');
    const isNew = urlParams.get('new') === 'true';
    await loadFlashcardClasses();
    
    if (setId && !isNew) {
        // Editing an existing set
        editMode = true;
        editSetId = setId;
        loadExistingSet(editSetId); // This will clear draft via loadExistingSet
        saveSetBtn.querySelector('span').textContent = 'Save Changes';
        // Change back button text when in edit mode
        backButtonText.textContent = 'Save and Go Back';
    } else {
        if (isNew) {
            // Explicitly creating a new set (from "Create Set" button)
            // Check if there's a draft available
            const draft = await loadDraft();
            if (draft && draft.lastSaved) {
                // Show the draft recovery modal
                showDraftModal();
            } else {
                // No draft, start a new set
                setNameInput.value = '';
                cardsContainer.innerHTML = '';
                addCard(); // Add first empty card
            }
        } else {
            // Normal navigation to creator.html without parameters
            // Try to load existing draft
            const draft = await loadDraft();
            if (draft && draft.lastSaved) {
                // Show the draft recovery modal
                showDraftModal();
            } else {
                // No draft, start a new set
                setNameInput.value = '';
                cardsContainer.innerHTML = '';
                addCard(); // Add first empty card
            }
        }
        editMode = false;
        editSetId = null;
        saveSetBtn.querySelector('span').textContent = 'Save Set';
    }

    updateCardCount();
    updateAddBetweenButtons(); // Initialize add-between buttons

    // Initialize Sortable
    new Sortable(cardsContainer, {
        animation: 150,
        handle: '.card-number',
        ghostClass: 'card-ghost',
        onEnd: () => {
            updateCardNumbers();
            updateAddBetweenButtons();
            triggerAutosave();
        }
    });

    // Card Management
    function addCard(cardData = {}, position = -1) {
        if (!cardTemplate) {
            console.error('Card template not found!');
            return null;
        }

        const cardFragment = document.importNode(cardTemplate.content, true);
        const cardElement = cardFragment.querySelector('.card-editor');
        cardElement.__cardData = {
            ...cardData,
            media: normalizeCardMedia(cardData),
            background: normalizeCardBackground(cardData)
        };
        if (cardData.id) {
            cardElement.dataset.cardId = cardData.id;
        }
        
        // Setup text editors
        const termEditor = cardElement.querySelector('.term-side .editor');
        const definitionEditor = cardElement.querySelector('.definition-side .editor');
        
        // Ensure text wrapping for contenteditable
        ensureEditorWrapping(termEditor);
        ensureEditorWrapping(definitionEditor);
        
        // Set placeholder text
        termEditor.dataset.placeholder = 'Enter term';
        definitionEditor.dataset.placeholder = 'Enter definition';
        
        // Set card number
        const cardNumber = cardElement.querySelector('.card-number');
        if (cardNumber) {
            if (position === -1) {
                cardNumber.textContent = cardsContainer.children.length + 1;
            } else {
                cardNumber.textContent = position + 1;
            }
        }
        
        // Setup text formatting
        setupFormatting(cardElement.querySelector('.term-side'));
        setupFormatting(cardElement.querySelector('.definition-side'));
        
        // Setup image upload for both sides
        const termPreviewContainer = cardElement.querySelector('.term-side .image-preview-container');
        const defPreviewContainer = cardElement.querySelector('.definition-side .image-preview-container');
        
        setupImageUpload(
            cardElement.querySelector('.term-side .image-btn'), 
            termPreviewContainer
        );
        setupImageUpload(
            cardElement.querySelector('.definition-side .image-btn'), 
            defPreviewContainer
        );
        setupBackgroundUpload(
            cardElement.querySelector('.term-side .bg-btn'),
            termPreviewContainer
        );
        setupBackgroundUpload(
            cardElement.querySelector('.definition-side .bg-btn'),
            defPreviewContainer
        );
        
        // Setup drag and drop
        setupDragAndDrop(cardElement);
        
        // Populate card data if provided
        if (cardData.term) {
            termEditor.innerHTML = cardData.term;
        }
        if (cardData.definition) {
            definitionEditor.innerHTML = cardData.definition;
        }
        
        renderSideMedia(cardElement, 'term');
        renderSideMedia(cardElement, 'definition');
        
        // Add delete button functionality
        const deleteBtn = cardElement.querySelector('.delete-card');
        if (deleteBtn) {
            deleteBtn.addEventListener('click', () => {
                cardElement.remove();
                
                // Also remove the add-between button above this card if it exists
                const prevBtn = cardElement.previousElementSibling;
                if (prevBtn && prevBtn.classList.contains('add-between-btn')) {
                    prevBtn.remove();
                }
                
                updateCardNumbers();
                updateCardCount();
                updateAddBetweenButtons();
                saveDraft(); // Save draft when card is deleted
            });
        }
        
        // Add input event listeners for autosave
        termEditor.addEventListener('input', triggerAutosave);
        definitionEditor.addEventListener('input', triggerAutosave);
        
        // Append or insert the new card to the container
        if (position === -1 || position >= cardsContainer.children.length) {
            cardsContainer.appendChild(cardElement);
        } else {
            // Get the reference to insert before
            const insertBeforeElement = getCardAtPosition(position);
            if (insertBeforeElement) {
                cardsContainer.insertBefore(cardElement, insertBeforeElement);
            } else {
                cardsContainer.appendChild(cardElement);
            }
        }
        
        updateCardNumbers();
        updateCardCount();
        updateAddBetweenButtons();
        saveDraft(); // Save draft when new card is added
        triggerAutosave();
        
        // Return the card element for scrolling
        return cardElement;
    }

    // Function to get a card element at a specific position
    function getCardAtPosition(position) {
        let count = 0;
        for (const child of cardsContainer.children) {
            if (child.classList.contains('card-editor')) {
                if (count === position) {
                    return child;
                }
                count++;
            }
        }
        return null;
    }

    // Function to create and update "add between" buttons
    function updateAddBetweenButtons() {
        // First remove all existing add-between buttons
        document.querySelectorAll('.add-between-btn').forEach(btn => btn.remove());
        
        // Skip if there are no cards
        if (cardsContainer.children.length === 0) return;
        
        // Get all card elements
        const cards = Array.from(cardsContainer.children).filter(
            child => child.classList.contains('card-editor')
        );
        
        // Add buttons after each card except the last one
        for (let i = 0; i < cards.length - 1; i++) {
            const addBtn = document.createElement('button');
            addBtn.className = 'add-between-btn';
            addBtn.innerHTML = '<i class="fas fa-plus"></i>';
            addBtn.title = 'Add card here';
            
            // Position index for the new card (after current card)
            const position = i + 1;
            
            addBtn.addEventListener('click', () => {
                const newCard = addCard({}, position);
                // Scroll to the new card with smooth animation
                if (newCard) {
                    setTimeout(() => {
                        newCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    }, 100);
                }
            });
            
            // Insert after current card
            if (cards[i].nextSibling) {
                cardsContainer.insertBefore(addBtn, cards[i].nextSibling);
            } else {
                cardsContainer.appendChild(addBtn);
            }
        }
    }

    function setupFormatting(container) {
        const toolbar = container.querySelector('.format-toolbar');
        const editor = container.querySelector('.editor');
        const editorContainer = container.querySelector('.editor-container');
        const voiceBtn = container.querySelector('.voice-btn');
        const voiceUndoBtn = container.querySelector('.voice-undo-btn');
        const voiceLevel = container.querySelector('.voice-level');
        
        // Setup paste handling for images from clipboard
        editor.addEventListener('paste', handlePaste);
        
        function handlePaste(e) {
            // Check if the clipboard has images
            const clipboardData = e.clipboardData || window.clipboardData;
            const items = clipboardData.items;
            
            let imageItem = null;
            if (items) {
                // Find the first image item in the clipboard
                for (let i = 0; i < items.length; i++) {
                    if (items[i].type.indexOf('image') !== -1) {
                        imageItem = items[i];
                        break;
                    }
                }
            }
            
            // If we found an image in the clipboard
            if (imageItem) {
                e.preventDefault(); // Prevent the default paste action
                
                const blob = imageItem.getAsFile();
                if (!blob) return;

                const cardElement = container.closest('.card-editor');
                const side = getSideKeyFromElement(container);
                addMediaFileToCard(cardElement, side, blob).then(() => {
                    renderSideMedia(cardElement, side);
                    triggerAutosave();
                    showToast('Image pasted successfully', 'success');
                }).catch(error => {
                    console.error('Error processing pasted image:', error);
                    showToast('Error processing pasted image', 'error');
                });
                
                return false;
            }
            
            // If no image, let the default paste behavior continue
            return true;
        }
        
        if (!toolbar || !editor) {
            console.error('Format toolbar or editor not found');
            return;
        }
        
        // Make sure toolbar is visible by default
        if (toolbar) {
            toolbar.classList.remove('hidden');

            function setFormatButtonState(button, active) {
                button.classList.toggle('active', Boolean(active));
                button.setAttribute('aria-pressed', String(Boolean(active)));
            }
            
            // Set up formatting buttons
            toolbar.querySelectorAll('button').forEach(button => {
                button.setAttribute('aria-pressed', 'false');

                button.addEventListener('click', (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    const format = button.dataset.format;
                    
                    if (format === 'formula') {
                        editor.focus();
                        // Capture selection range before modal opens
                        const sel = window.getSelection();
                        let savedRange = null;
                        if (sel && sel.rangeCount > 0) savedRange = sel.getRangeAt(0).cloneRange();

                        const modal = document.getElementById('formula-modal');
                        const inputEl = document.getElementById('formula-modal-input');
                        if (!modal || !inputEl) {
                            // Fallback to native prompt if modal not found
                            const raw = window.prompt('Enter formula (LaTeX):', '');
                            const formula = window.EruditeMath?.inlineFormula
                                ? window.EruditeMath.inlineFormula(raw)
                                : (raw ? `\\(${raw.trim()}\\)` : '');
                            if (formula) { document.execCommand('insertText', false, formula); triggerAutosave(); }
                        } else {
                            inputEl.value = '';
                            // Use .show class — matches .shortcuts-modal CSS pattern
                            modal.classList.add('show');
                            requestAnimationFrame(() => inputEl.focus());

                            const doInsert = () => {
                                const raw = String(inputEl.value || '').trim();
                                modal.classList.remove('show');
                                cleanup();
                                if (!raw) return;
                                const formula = window.EruditeMath?.inlineFormula
                                    ? window.EruditeMath.inlineFormula(raw)
                                    : `\\(${raw}\\)`;
                                if (savedRange) {
                                    const s = window.getSelection();
                                    s.removeAllRanges();
                                    s.addRange(savedRange);
                                }
                                document.execCommand('insertText', false, formula);
                                triggerAutosave();
                            };
                            const doCancel = () => { modal.classList.remove('show'); cleanup(); };
                            const onKey = (e) => {
                                if (e.key === 'Enter') { e.preventDefault(); doInsert(); }
                                if (e.key === 'Escape') doCancel();
                            };
                            const cleanup = () => {
                                document.getElementById('formula-modal-confirm')?.removeEventListener('click', doInsert);
                                document.getElementById('formula-modal-cancel')?.removeEventListener('click', doCancel);
                                document.getElementById('formula-modal-close')?.removeEventListener('click', doCancel);
                                inputEl.removeEventListener('keydown', onKey);
                            };
                            document.getElementById('formula-modal-confirm')?.addEventListener('click', doInsert);
                            document.getElementById('formula-modal-cancel')?.addEventListener('click', doCancel);
                            document.getElementById('formula-modal-close')?.addEventListener('click', doCancel);
                            inputEl.addEventListener('keydown', onKey);
                            // Clicking backdrop (the modal itself) cancels
                            modal.addEventListener('click', e => { if (e.target === modal) doCancel(); }, { once: true });
                        }
                        setFormatButtonState(button, false);
                    } else if (format === 'list') {
                        setFormatButtonState(button, !button.classList.contains('active'));
                        if (!button.classList.contains('active')) {
                            const selection = window.getSelection();
                            const range = selection.getRangeAt(0);
                            const text = range.toString();
                            
                            if (text) {
                                const lines = text.split('\n');
                                const formattedText = lines.map(line => 
                                    line.trim() !== '' && !line.startsWith('• ') ? '• ' + line : line
                                ).join('\n');
                                range.deleteContents();
                                range.insertNode(document.createTextNode(formattedText));
                            }
                        }
                    } else {
                        // Get current selection state
                        const selection = window.getSelection();
                        if (selection.rangeCount > 0) {
                            // Toggle format state
                            document.execCommand(format, false, null);
                            // Update button state based on current format
                            const isFormatActive = document.queryCommandState(format);
                            setFormatButtonState(button, isFormatActive);
                        }
                    }
                    
                    editor.focus();
                    triggerAutosave();
                });

                // Update button state when text is selected
                editor.addEventListener('mouseup', () => {
                    if (!['list', 'formula'].includes(button.dataset.format)) {
                        const isFormatActive = document.queryCommandState(button.dataset.format);
                        setFormatButtonState(button, isFormatActive);
                    }
                });
                
                editor.addEventListener('keyup', () => {
                    if (!['list', 'formula'].includes(button.dataset.format)) {
                        const isFormatActive = document.queryCommandState(button.dataset.format);
                        setFormatButtonState(button, isFormatActive);
                    }
                });
            });
        }
        
        // Use a single global click listener for all toolbars
        if (!documentClickListener) {
            documentClickListener = (e) => {
                document.querySelectorAll('.format-toolbar').forEach(tb => {
                    if (!tb.contains(e.target) && 
                        !e.target.classList.contains('format-btn') && 
                        !e.target.closest('.format-btn')) {
                        tb.classList.add('hidden');
                    }
                });
            };
            document.addEventListener('click', documentClickListener);
        }

        // Legacy voice typing UI was removed from the creator.
        if (false) {
            let recognition = null;
            let isRecording = false;
            let mediaStream = null;
            let audioContext = null;
            let analyser = null;
            let rafId = null;
            let lastInsertedLength = 0;

            function ensureRecognition() {
                const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
                if (!SpeechRecognition) {
                    showToast('Voice typing not supported in this browser', 'error');
                    return null;
                }
                const rec = new SpeechRecognition();
                rec.lang = navigator.language || 'en-US';
                rec.interimResults = true;
                rec.continuous = true;
                return rec;
            }

            function smartPunctuate(text) {
                if (!text) return '';
                // Trim and collapse extra spaces
                let t = text.replace(/\s+/g, ' ').trim();
                if (!t) return '';
                // Capitalize first letter of sentence and after sentence boundaries
                t = t.replace(/(^|[.!?]\s+)([a-z])/g, (m, p1, p2) => p1 + p2.toUpperCase());
                // Basic proper nouns/acronyms heuristics can be added here if needed
                return t + ' ';
            }

            // Convert verbal punctuation and improve capitalization inline
            // Merge sequences like "v a c c i n e" -> "vaccine"
            function compressSpelledSequences(input) {
                if (!input) return '';
                // Replace any run of single-letter words (2 or more) with the letters joined
                return input.replace(/(?:^|\s)((?:[a-zA-Z]\s+){2,}[a-zA-Z])(?=\s|$)/g, (match, group) => {
                    const joined = group.replace(/\s+/g, '');
                    // Preserve leading space if present
                    return (match.startsWith(' ') ? ' ' : '') + joined;
                });
            }

            function smartPunctuateInline(text) {
                if (!text) return '';
                let t = text.replace(/\s+/g, ' ').trim();
                t = compressSpelledSequences(t);
                t = t.replace(/\b(open|start) quote(s)?\b/gi, '“')
                     .replace(/\b(close|end) quote(s)?\b/gi, '”')
                     .replace(/\b(open|start) paren(thesis)?\b/gi, '(')
                     .replace(/\b(close|end) paren(thesis)?\b/gi, ')')
                     .replace(/\bcomma\b/gi, ',')
                     .replace(/\bcolon\b/gi, ':')
                     .replace(/\bsemicolon\b/gi, ';')
                     .replace(/\bquestion mark\b/gi, '?')
                     .replace(/\bexclamation (point|mark)\b/gi, '!');
                // Auto-capitalize after colon
                t = t.replace(/(:\s*)([a-z])/g, (m, p1, p2) => p1 + p2.toUpperCase());
                // Capitalize sentence starts
                t = t.replace(/(^|[.!?]\s+)([a-z])/g, (m, p1, p2) => p1 + p2.toUpperCase());
                return t + ' ';
            }

            // Insert a reliable line break at caret inside editor
            function insertLineBreakAtCaret() {
                editor.focus();
                const selection = window.getSelection();
                if (!selection) return;
                let range;
                if (selection.rangeCount > 0) {
                    range = selection.getRangeAt(0);
                } else {
                    range = document.createRange();
                    range.selectNodeContents(editor);
                    range.collapse(false);
                    selection.addRange(range);
                }
                // Create BR and a zero-width space to keep caret visible
                const br = document.createElement('br');
                const zwsp = document.createTextNode('\u200B');
                range.deleteContents();
                range.insertNode(br);
                range.setStartAfter(br);
                range.insertNode(zwsp);
                range.setStartAfter(zwsp);
                range.collapse(true);
                selection.removeAllRanges();
                selection.addRange(range);
            }

            // Click toolbar format button
            function clickFormatButton(format, desired) {
                const btn = toolbar.querySelector(`button[data-format="${format}"]`);
                if (!btn) return true;
                // Ensure caret is inside the editor for execCommand to affect typing state
                editor.focus();
                const selection = window.getSelection();
                if (selection) {
                    if (selection.rangeCount === 0 || !editor.contains(selection.anchorNode)) {
                        const range = document.createRange();
                        range.selectNodeContents(editor);
                        range.collapse(false);
                        selection.removeAllRanges();
                        selection.addRange(range);
                    }
                }
                // Current state from the browser
                const cmdState = document.queryCommandState(format);
                const wantOn = desired === 'on' || (desired === 'toggle' && !cmdState);
                const wantOff = desired === 'off' || (desired === 'toggle' && cmdState);
                if (wantOn && !cmdState) {
                    document.execCommand(format, false, null);
                } else if (wantOff && cmdState) {
                    document.execCommand(format, false, null);
                }
                // Sync button UI to actual state
                const nowActive = document.queryCommandState(format);
                btn.classList.toggle('active', nowActive);
                return true;
            }

            // Command parsing: returns true if handled
            function applyDictationCommand(raw) {
                const text = raw.trim().toLowerCase();
                if (!text) return false;
                if (/(new\s*line|newline)/.test(text)) {
                    insertLineBreakAtCaret();
                    return true;
                }
                // Full stop / period
                if (/\b(full\s*stop|period)\b/.test(text)) {
                    document.execCommand('insertText', false, '. ');
                    return true;
                }
                if (/bullet(s)?/.test(text)) {
                    if (!document.execCommand('insertHTML', false, '<br>• ')) {
                        document.execCommand('insertText', false, '\n• ');
                    }
                    return true;
                }
                // Add X cards (e.g., "add 5 cards")
                const addMatch = text.match(/\badd\s+(\d+)\s+(card|cards)\b/);
                if (addMatch) {
                    const count = Math.max(1, Math.min(50, parseInt(addMatch[1], 10) || 0));
                    if (count > 0) {
                        let last = null;
                        for (let i = 0; i < count; i++) last = addCard();
                        if (last) {
                            const term = last.querySelector('.term-side .editor');
                            if (term) term.focus();
                            setTimeout(() => last.scrollIntoView({ behavior: 'smooth', block: 'center' }), 100);
                        }
                    }
                    return true;
                }
                // Focus term/definition side
                if (/\bterm\s+side\b/.test(text)) {
                    const currentCard = (document.activeElement && document.activeElement.closest && document.activeElement.closest('.card-editor')) || editor.closest('.card-editor');
                    if (currentCard) {
                        // Find the button that initiated this recording session
                        const sourceVoiceBtn = voiceBtn;
                        const termEditor = currentCard.querySelector('.term-side .editor');
                        const termVoiceBtn = currentCard.querySelector('.term-side .voice-btn');
                        
                        if (termEditor) {
                            termEditor.focus();
                            
                            // If we're currently recording, transfer the session to the term side
                            if (isRecording && sourceVoiceBtn && termVoiceBtn) {
                                // Stop current recording
                                sourceVoiceBtn.click();
                                // Start new recording on term side after a short delay
                                setTimeout(() => {
                                    termVoiceBtn.click();
                                }, 100);
                            }
                        }
                    }
                    return true;
                }
                if (/\bdefinition\s+side\b/i.test(text)) {
                    const currentCard = (document.activeElement && document.activeElement.closest && document.activeElement.closest('.card-editor')) || editor.closest('.card-editor');
                    if (currentCard) {
                        // Find the button that initiated this recording session
                        const sourceVoiceBtn = voiceBtn;
                        const defEditor = currentCard.querySelector('.definition-side .editor');
                        const defVoiceBtn = currentCard.querySelector('.definition-side .voice-btn');
                        
                        if (defEditor) {
                            defEditor.focus();
                            
                            // If we're currently recording, transfer the session to the definition side
                            if (isRecording && sourceVoiceBtn && defVoiceBtn) {
                                // Stop current recording
                                sourceVoiceBtn.click();
                                // Start new recording on definition side after a short delay
                                setTimeout(() => {
                                    defVoiceBtn.click();
                                }, 100);
                            }
                        }
                    }
                    return true;
                }
                // Bold / Unbold
                if (/\b(unbold|remove\s+bold|stop\s+bold)\b/.test(text)) {
                    clickFormatButton('bold', 'off');
                    return true;
                }
                if (/\b(bold|bold\s+that|make\s+(this|that)\s+bold)\b/.test(text)) {
                    clickFormatButton('bold', 'on');
                    return true;
                }
                // Italic / Unitalic
                if (/\b(unitalic|un\s+italic|remove\s+italic|un\s*italics|not\s+italic|stop\s+italic)\b/.test(text)) {
                    clickFormatButton('italic', 'off');
                    return true;
                }
                if (/\b(italic|italics|italicize|italicise)\b/.test(text)) {
                    clickFormatButton('italic', 'on');
                    return true;
                }
                // Underline / Ununderline
                if (/\b(ununderline|un\s+underline|remove\s+underline|no\s+underline|stop\s+underline)\b/.test(text)) {
                    clickFormatButton('underline', 'off');
                    return true;
                }
                if (/\b(underline|underlined)\b/.test(text)) {
                    clickFormatButton('underline', 'on');
                    return true;
                }
                // New card / Next card
                if (/(new\s+card|next\s+card)/.test(text)) {
                    // Find the button that initiated this recording session.
                    // 'voiceBtn' is available from the parent function's scope.
                    const sourceVoiceBtn = voiceBtn;

                    const newCard = addCard();
                    if (newCard) {
                        const termEditor = newCard.querySelector('.term-side .editor');
                        if (termEditor) termEditor.focus();
                        setTimeout(() => newCard.scrollIntoView({ behavior: 'smooth', block: 'center' }), 100);

                        // --- FIX STARTS HERE ---
                        // We will now transfer the voice recording session to the new card.
                        
                        // Find the voice button on the newly created card (we'll default to the term side).
                        const newCardVoiceBtn = newCard.querySelector('.term-side .voice-btn');
                        
                        if (sourceVoiceBtn && newCardVoiceBtn) {
                            // 1. Programmatically "click" the old button to stop its recording session.
                            sourceVoiceBtn.click(); 

                            // 2. After a short delay, "click" the new button to start a fresh session
                            //    that is correctly linked to the new card.
                            setTimeout(() => {
                                newCardVoiceBtn.click();
                            }, 100);
                        }
                        // --- FIX ENDS HERE ---
                    }
                    return true;
                }
                return false;
            }

            function escapeHTML(s) {
                return s
                    .replace(/&/g, '&amp;')
                    .replace(/</g, '&lt;')
                    .replace(/>/g, '&gt;')
                    .replace(/\"/g, '&quot;')
                    .replace(/'/g, '&#39;');
            }

            function buildFormattedHTML(text) {
                const safe = escapeHTML(text);
                const isBold = document.queryCommandState('bold');
                const isItalic = document.queryCommandState('italic');
                const isUnderline = document.queryCommandState('underline');
                let inner = safe;
                if (isBold) inner = `<b>${inner}</b>`;
                if (isItalic) inner = `<i>${inner}</i>`;
                if (isUnderline) inner = `<u>${inner}</u>`;
                return `<span class="dictation-chunk">${inner}</span>`;
            }

            function startRecording() {
                if (isRecording) return;
                recognition = ensureRecognition();
                if (!recognition) return;

                // Visual state
                voiceBtn.classList.add('recording');
                voiceBtn.title = 'Stop voice typing';
                toolbar.classList.add('recording');
                isRecording = true;
                if (voiceUndoBtn) voiceUndoBtn.style.display = 'inline-flex';

                let finalTranscript = '';

                recognition.onresult = (event) => {
                    let interimTranscript = '';
                    for (let i = event.resultIndex; i < event.results.length; i++) {
                        const transcript = event.results[i][0].transcript;
                        if (event.results[i].isFinal) {
                            finalTranscript += transcript;
                        } else {
                            interimTranscript += transcript;
                        }
                    }

                    // Ensure caret is in the currently active editor (supports focus after new card)
                    const activeEd = document.activeElement && document.activeElement.classList && document.activeElement.classList.contains('editor')
                        ? document.activeElement
                        : editor;
                    const selection = window.getSelection();
                    activeEd.focus();
                    if (selection) {
                        if (selection.rangeCount === 0 || !activeEd.contains(selection.anchorNode)) {
                            selection.removeAllRanges();
                            const range = document.createRange();
                            range.selectNodeContents(activeEd);
                            range.collapse(false);
                            selection.addRange(range);
                        }
                    }

                    if (finalTranscript) {
                        // Commands first
                        if (!applyDictationCommand(finalTranscript)) {
                            const punctuated = smartPunctuateInline(finalTranscript);
                            const html = buildFormattedHTML(punctuated);
                            // Insert as HTML so current formatting applies to the chunk
                            if (!document.execCommand('insertHTML', false, html)) {
                                // Fallback to text
                                document.execCommand('insertText', false, punctuated);
                            }
                            // Keep a rough length for legacy undo, but prefer span removal
                            lastInsertedLength = punctuated.length;
                        }
                        finalTranscript = '';
                        triggerAutosave();
                    }
                };

                recognition.onerror = (e) => {
                    console.error('Speech recognition error:', e);
                    showToast('Voice typing error', 'error');
                    stopRecording();
                };

                recognition.onend = () => {
                    // If stopped intentionally, keep state cleared; else, attempt restart
                    if (isRecording) {
                        try {
                            recognition.start();
                        } catch (err) {
                            // Some browsers throw if start called quickly; fallback to stop state
                            stopRecording();
                        }
                    }
                };

                try {
                    recognition.start();
                } catch (err) {
                    console.error('Failed to start recognition:', err);
                    showToast('Could not start voice typing', 'error');
                    stopRecording();
                }
                setupAudioLevel();
            }

            function stopRecording() {
                if (!isRecording) return;
                isRecording = false;
                voiceBtn.classList.remove('recording');
                voiceBtn.title = 'Start voice typing';
                toolbar.classList.remove('recording');
                try {
                    if (recognition) recognition.stop();
                } catch (_) {}
                recognition = null;
                teardownAudioLevel();
            }

            voiceBtn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                if (!isRecording) {
                    startRecording();
                } else {
                    stopRecording();
                }
            });

            // Undo last dictation insert
            if (voiceUndoBtn) {
                voiceUndoBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    // Prefer removing the last dictation chunk span if present
                    const chunks = editor.querySelectorAll('.dictation-chunk');
                    if (chunks.length > 0) {
                        const last = chunks[chunks.length - 1];
                        last.remove();
                        triggerAutosave();
                        return;
                    }
                    // Legacy fallback based on text length
                    if (lastInsertedLength > 0) {
                        const current = editor.textContent;
                        editor.textContent = current.slice(0, Math.max(0, current.length - lastInsertedLength));
                        lastInsertedLength = 0;
                        triggerAutosave();
                    }
                });
            }

            // Audio meter
            async function setupAudioLevel() {
                try {
                    if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia || !voiceLevel) return;
                    mediaStream = await navigator.mediaDevices.getUserMedia({ audio: true });
                    audioContext = new (window.AudioContext || window.webkitAudioContext)();
                    const source = audioContext.createMediaStreamSource(mediaStream);
                    analyser = audioContext.createAnalyser();
                    analyser.fftSize = 256;
                    source.connect(analyser);
                    const dataArray = new Uint8Array(analyser.frequencyBinCount);
                    const update = () => {
                        analyser.getByteTimeDomainData(dataArray);
                        let sum = 0;
                        for (let i = 0; i < dataArray.length; i++) {
                            const v = (dataArray[i] - 128) / 128;
                            sum += v * v;
                        }
                        const rms = Math.sqrt(sum / dataArray.length);
                        const level = Math.min(100, Math.max(0, Math.round(rms * 200)));
                        toolbar.style.setProperty('--voice-level', level + '%');
                        rafId = requestAnimationFrame(update);
                    };
                    update();
                } catch (err) {
                    console.warn('Audio meter unavailable:', err);
                }
            }

            function teardownAudioLevel() {
                if (rafId) cancelAnimationFrame(rafId);
                rafId = null;
                if (audioContext) { try { audioContext.close(); } catch (_) {} }
                audioContext = null;
                analyser = null;
                if (mediaStream) { mediaStream.getTracks().forEach(t => t.stop()); }
                mediaStream = null;
                toolbar.style.setProperty('--voice-level', '0%');
            }
        }

        // Handle bullet lists for new lines
        editor.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                const selection = window.getSelection();
                const range = selection.getRangeAt(0);
                const currentLine = range.startContainer;
                
                if (currentLine.textContent.startsWith('• ')) {
                    e.preventDefault();
                    document.execCommand('insertHTML', false, '\n• ');
                }
            }
        });

        // Store the content for autosave
        editor.addEventListener('input', () => {
            triggerAutosave();
        });
    }

    function renderSideMedia(cardElement, side) {
        const cardData = ensureCardMediaState(cardElement);
        const sideElement = cardElement.querySelector(side === 'definition' ? '.definition-side' : '.term-side');
        const previewContainer = sideElement?.querySelector('.image-preview-container');
        const previewList = previewContainer?.querySelector('.media-preview-list');
        const legacyPreview = previewContainer?.querySelector('.image-preview');
        const legacyRemove = previewContainer?.querySelector('.remove-image-btn');
        const backgroundPreview = previewContainer?.querySelector('.background-preview');
        if (!previewContainer || !previewList) return;

        const legacyKey = side === 'definition' ? 'definitionImage' : 'termImage';
        const legacySrc = cardData[legacyKey] || '';
        if (legacyPreview) {
            legacyPreview.src = legacySrc;
            legacyPreview.style.display = legacySrc ? 'block' : 'none';
        }
        if (legacyRemove) legacyRemove.style.display = legacySrc ? 'block' : 'none';

        const sideMedia = normalizeCardMedia(cardData)[side] || [];
        previewList.innerHTML = sideMedia.map(item => {
            const icon = mediaIcon(item.kind);
            const src = escapeAttribute(item.src || '');
            const name = escapeText(item.name || item.kind || 'media');
            const attrName = escapeAttribute(item.name || item.kind || 'media');
            let preview = '';
            if (item.kind === 'audio') {
                preview = `<audio src="${src}" controls preload="metadata" title="${attrName}"></audio>`;
            } else if (item.kind === 'video') {
                preview = `<video src="${src}" controls preload="metadata" title="${attrName}"></video>`;
            } else {
                preview = `<img src="${src}" alt="${attrName}">`;
            }
            return `
                <div class="media-preview-item" data-media-id="${item.id}">
                    <div>
                        <div class="media-preview-meta">
                            <i class="fas ${icon}"></i>
                            <span>${name}</span>
                        </div>
                        ${preview}
                    </div>
                    <button type="button" class="remove-media-btn" data-remove-media="${item.id}" title="Remove media">&times;</button>
                </div>
            `;
        }).join('');

        previewList.querySelectorAll('[data-remove-media]').forEach(button => {
            button.addEventListener('click', async event => {
                event.preventDefault();
                event.stopPropagation();
                const id = button.dataset.removeMedia;
                const mediaState = normalizeCardMedia(cardData);
                const item = (mediaState[side] || []).find(entry => String(entry.id) === String(id));
                if (item?.src && window.flashcardStore?.deleteImage) {
                    await window.flashcardStore.deleteImage(item.src).catch(() => {});
                }
                cardData.media = {
                    ...mediaState,
                    [side]: (mediaState[side] || []).filter(entry => String(entry.id) !== String(id))
                };
                renderSideMedia(cardElement, side);
                triggerAutosave();
            });
        });

        const background = normalizeCardBackground(cardData)[side];
        if (backgroundPreview) {
            backgroundPreview.classList.toggle('hidden', !background);
            backgroundPreview.style.backgroundImage = background ? `url("${background.src}")` : '';
            const removeBackground = backgroundPreview.querySelector('.remove-background-btn');
            if (removeBackground) {
                removeBackground.onclick = async event => {
                    event.preventDefault();
                    event.stopPropagation();
                    if (background?.src && window.flashcardStore?.deleteImage) {
                        await window.flashcardStore.deleteImage(background.src).catch(() => {});
                    }
                    cardData.background = {
                        ...normalizeCardBackground(cardData),
                        [side]: null
                    };
                    renderSideMedia(cardElement, side);
                    triggerAutosave();
                };
            }
        }
    }

    function setupImageUpload(button, previewContainer) {
        const input = document.createElement('input');
        input.type = 'file';
        input.accept = MEDIA_ACCEPT;
        input.multiple = true;

        const cardElement = previewContainer.closest('.card-editor');
        const side = getSideKeyFromElement(previewContainer.closest('.card-side'));
        const preview = previewContainer.querySelector('.image-preview');
        const removeBtn = previewContainer.querySelector('.remove-image-btn');

        if (removeBtn) {
            removeBtn.addEventListener('click', async (e) => {
                e.stopPropagation(); // Prevent event from bubbling up

                const data = ensureCardMediaState(cardElement);
                const legacyKey = side === 'definition' ? 'definitionImage' : 'termImage';
                const currentSrc = data[legacyKey] || preview.src;
                if (currentSrc && window.flashcardStore?.deleteImage) {
                    await window.flashcardStore.deleteImage(currentSrc);
                }

                data[legacyKey] = '';
                renderSideMedia(cardElement, side);
                triggerAutosave();
            });
        }

        button.addEventListener('click', () => input.click());

        input.addEventListener('change', async () => {
            const files = Array.from(input.files || []);
            if (!files.length) return;

            try {
                button.disabled = true;
                button.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';

                let added = 0;
                for (const file of files) {
                    if (!file.type.startsWith('image/') && !file.type.startsWith('audio/') && !file.type.startsWith('video/')) continue;
                    await addMediaFileToCard(cardElement, side, file);
                    added += 1;
                }

                if (!added) {
                    showToast('No supported media files selected', 'error');
                    return;
                }

                renderSideMedia(cardElement, side);
                triggerAutosave();
                showToast(added === 1 ? 'Media added successfully' : `${added} media files added`, 'success');
            } catch (error) {
                console.error('Error processing media:', error);
                showToast('Error processing media', 'error');
            } finally {
                input.value = '';
                button.disabled = false;
                button.innerHTML = '<i class="fas fa-paperclip"></i>';
            }
        });
    }

    function setupBackgroundUpload(button, previewContainer) {
        if (!button) return;
        const input = document.createElement('input');
        input.type = 'file';
        input.accept = BACKGROUND_ACCEPT;
        const cardElement = previewContainer.closest('.card-editor');
        const side = getSideKeyFromElement(previewContainer.closest('.card-side'));

        button.addEventListener('click', () => input.click());
        input.addEventListener('change', async () => {
            const file = input.files?.[0];
            if (!file) return;
            if (!file.type.startsWith('image/')) {
                showToast('Please select an image for the background', 'error');
                return;
            }
            try {
                button.disabled = true;
                button.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
                const src = await processMediaFile(file, {
                    setId: editMode ? editSetId : 'draft',
                    side,
                    prefix: `${side}-background`
                });
                const data = ensureCardMediaState(cardElement);
                data.background = {
                    ...normalizeCardBackground(data),
                    [side]: window.EruditeMedia?.normalizeCardBackground
                        ? window.EruditeMedia.normalizeCardBackground({ [side]: { src, mime: file.type, name: file.name } })[side]
                        : { src, mime: file.type, name: file.name, fit: 'cover', opacity: 0.32 }
                };
                renderSideMedia(cardElement, side);
                triggerAutosave();
                showToast('Background image set', 'success');
            } catch (error) {
                console.error('Error setting background:', error);
                showToast('Could not set background', 'error');
            } finally {
                input.value = '';
                button.disabled = false;
                button.innerHTML = '<i class="fas fa-panorama"></i>';
            }
        });
    }

    async function addMediaFileToCard(cardElement, side, file) {
        if (!file.type.startsWith('image/') && !file.type.startsWith('audio/') && !file.type.startsWith('video/')) {
            throw new Error('Unsupported media type');
        }

        const cardIndex = Array.from(cardsContainer.children)
            .filter(child => child.classList?.contains('card-editor'))
            .indexOf(cardElement);
        const src = await processMediaFile(file, {
            setId: editMode ? editSetId : 'draft',
            cardIndex,
            side,
            prefix: `${side}-media`
        });
        const data = ensureCardMediaState(cardElement);
        const mediaState = normalizeCardMedia(data);
        const item = window.EruditeMedia?.mediaItemFromSource
            ? window.EruditeMedia.mediaItemFromSource(src, file)
            : {
                id: `media-${Date.now()}-${Math.random().toString(36).slice(2)}`,
                kind: file.type.startsWith('audio/') ? 'audio' : file.type.startsWith('video/') ? 'video' : 'image',
                mime: file.type,
                name: file.name,
                src,
                created: Date.now()
            };
        data.media = {
            ...mediaState,
            [side]: [...(mediaState[side] || []), item]
        };
    }

    function setupDragAndDrop(cardElement) {
        const termSide = cardElement.querySelector('.term-side');
        const definitionSide = cardElement.querySelector('.definition-side');
        const termPreview = termSide.querySelector('.image-preview');
        const definitionPreview = definitionSide.querySelector('.image-preview');

        [termSide, definitionSide].forEach(side => {
            side.addEventListener('dragenter', handleDragEnter);
            side.addEventListener('dragleave', handleDragLeave);
            side.addEventListener('dragover', handleDragOver);
            side.addEventListener('drop', handleDrop);
        });

        function handleDragEnter(e) {
            e.preventDefault();
            e.stopPropagation();
            e.currentTarget.classList.add('drag-over');
        }

        function handleDragLeave(e) {
            e.preventDefault();
            e.stopPropagation();
            if (e.currentTarget.contains(e.relatedTarget)) return;
            e.currentTarget.classList.remove('drag-over');
        }

        function handleDragOver(e) {
            e.preventDefault();
            e.stopPropagation();
        }

        async function handleDrop(e) {
            e.preventDefault();
            e.stopPropagation();
            
            const side = e.currentTarget;
            side.classList.remove('drag-over');
            
            const files = e.dataTransfer.files;
            if (files.length === 0) return;

            try {
                const cardElement = side.closest('.card-editor');
                const targetSide = getSideKeyFromElement(side);
                let added = 0;
                for (const file of Array.from(files)) {
                    if (!file.type.startsWith('image/') && !file.type.startsWith('audio/') && !file.type.startsWith('video/')) continue;
                    await addMediaFileToCard(cardElement, targetSide, file);
                    added += 1;
                }
                if (!added) {
                    showToast('No supported media files selected', 'error');
                    return;
                }
                renderSideMedia(cardElement, targetSide);
                triggerAutosave();
                showToast(added === 1 ? 'Media added successfully' : `${added} media files added`, 'success');
            } catch (error) {
                console.error('Error processing dragged media:', error);
                showToast('Error processing media', 'error');
            }
        }
    }

    async function processMediaFile(file, meta = {}) {
        if (window.flashcardStore?.saveImageFromFile) {
            return await window.flashcardStore.saveImageFromFile(file, meta);
        }

        return await readFileAsDataURL(file);
    }

    function readFileAsDataURL(file) {
        return new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.onload = () => resolve(reader.result);
            reader.onerror = reject;
            reader.readAsDataURL(file);
        });
    }

    // Autosave and draft saving functions
    function updateAutosaveIndicator(success) {
        const indicator = document.querySelector('.autosave-indicator');
        if (!indicator) return;
        
        indicator.innerHTML = success ? 
            '<i class="fas fa-save"></i><span>Saved</span>' : 
            '<i class="fas fa-exclamation-circle"></i><span>Error saving</span>';
        
        indicator.style.opacity = '1';
        setTimeout(() => {
            indicator.style.opacity = '0';
        }, 2000);
    }

    // Autosave functionality
    function triggerAutosave() {
        if (autoSaveTimeout) {
            clearTimeout(autoSaveTimeout);
        }
        
        // Also trigger draft save with every autosave
        triggerDraftSave();
        
        // Update indicator to show "Saving..."
        const indicator = document.querySelector('.autosave-indicator');
        if (indicator) {
            indicator.innerHTML = '<i class="fas fa-sync fa-spin"></i><span>Saving...</span>';
            indicator.style.opacity = '1';
        }
        
        autoSaveTimeout = setTimeout(() => {
            saveDraft();
            updateAutosaveIndicator(true);
        }, AUTOSAVE_DELAY);
    }

    // Function to start continuous draft saving
    function triggerDraftSave() {
        if (draftWritesSuppressed || successfulSaveRedirecting) return;

        if (draftSaveTimeout) {
            clearTimeout(draftSaveTimeout);
        }
        
        // Use a longer timeout for draft saving to not interfere with typing
        draftSaveTimeout = setTimeout(() => {
            saveDraft();
            // Recursively call this function to keep saving drafts
            triggerDraftSave();
        }, DRAFT_SAVE_DELAY);
    }

    function closeAllFormatToolbars() {
        document.querySelectorAll('.format-toolbar').forEach(toolbar => {
            toolbar.classList.add('hidden');
        });
    }

    function cancelDraftTimers() {
        if (draftSaveTimeout) {
            clearTimeout(draftSaveTimeout);
            draftSaveTimeout = null;
        }
        if (autoSaveTimeout) {
            clearTimeout(autoSaveTimeout);
            autoSaveTimeout = null;
        }
    }

    async function clearDraftState() {
        localStorage.removeItem(DRAFT_STORAGE_KEY);
        if (window.flashcardStore?.removeState) {
            try {
                await window.flashcardStore.removeState(DRAFT_STORAGE_KEY);
            } catch (error) {
                console.warn('Could not clear draft from local store:', error);
            }
        }
    }

    function normalizeDraftCard(card = {}) {
        return {
            term: String(card.term || '').trim(),
            definition: String(card.definition || '').trim(),
            termImage: String(card.termImage || ''),
            definitionImage: String(card.definitionImage || ''),
            media: normalizeCardMedia(card.media || {}),
            background: normalizeCardBackground(card)
        };
    }

    function draftMatchesSavedSet(draft, set) {
        if (!draft || !set) return false;
        if (String(draft.name || '').trim() !== String(set.name || '').trim()) return false;
        if (String(draft.classId || '') !== String(set.classId || '')) return false;

        const draftCards = Array.isArray(draft.cards) ? draft.cards.map(normalizeDraftCard) : [];
        const savedCards = Array.isArray(set.cards) ? set.cards.map(normalizeDraftCard) : [];
        if (draftCards.length === 0 || draftCards.length !== savedCards.length) return false;

        const savedAt = Number(set.lastModified || set.created || 0);
        const draftSavedAt = Number(draft.lastSaved || 0);
        const savedCloseToDraft = savedAt > 0 && draftSavedAt > 0 && Math.abs(draftSavedAt - savedAt) < (10 * 60 * 1000);
        if (!savedCloseToDraft) return false;

        return draftCards.every((card, index) => {
            const savedCard = savedCards[index];
            return card.term === savedCard.term &&
                card.definition === savedCard.definition &&
                card.termImage === savedCard.termImage &&
                card.definitionImage === savedCard.definitionImage &&
                JSON.stringify(card.media) === JSON.stringify(savedCard.media) &&
                JSON.stringify(card.background) === JSON.stringify(savedCard.background);
        });
    }

    async function discardDraftIfAlreadySaved(draft) {
        if (!draft || !window.flashcardStore?.listSets) return draft;

        try {
            const sets = await window.flashcardStore.listSets();
            const alreadySaved = Array.isArray(sets) && sets.some(set => draftMatchesSavedSet(draft, set));
            if (alreadySaved) {
                await clearDraftState();
                return null;
            }
        } catch (error) {
            console.warn('Could not check draft against saved sets:', error);
        }

        return draft;
    }

    // Draft handling functions
    function saveDraft() {
        // Don't save drafts when in edit mode
        if (editMode || draftWritesSuppressed || successfulSaveRedirecting) return true;
        
        try {
            // Only save if there's actual content
            const cards = getCardsData();
            const hasContent = setNameInput.value.trim() || cards.some(cardHasContent);
            
            if (hasContent) {
                const draft = {
                    name: setNameInput.value,
                    classId: setClassSelect?.value && setClassSelect.value !== '__new' ? setClassSelect.value : null,
                    cards: cards,
                    lastSaved: Date.now()
                };
                if (window.flashcardStore?.setState) {
                    window.flashcardStore.setState(DRAFT_STORAGE_KEY, draft).catch(error => {
                        console.warn('Could not save draft to local store:', error);
                    });
                } else {
                    localStorage.setItem(DRAFT_STORAGE_KEY, JSON.stringify(draft));
                }
            } else {
                if (window.flashcardStore?.removeState) {
                    window.flashcardStore.removeState(DRAFT_STORAGE_KEY).catch(error => {
                        console.warn('Could not remove draft from local store:', error);
                    });
                } else {
                    localStorage.removeItem(DRAFT_STORAGE_KEY);
                }
            }
            return true;
        } catch (error) {
            console.error('Error saving draft:', error);
            updateAutosaveIndicator(false);
            return false;
        }
    }

    async function loadDraft() {
        let draft = null;

        if (window.flashcardStore?.getState) {
            draft = await window.flashcardStore.getState(DRAFT_STORAGE_KEY);
            return discardDraftIfAlreadySaved(draft);
        }

        const draftData = localStorage.getItem(DRAFT_STORAGE_KEY);
        draft = draftData ? JSON.parse(draftData) : null;
        return discardDraftIfAlreadySaved(draft);
    }
    
    // Function to handle loading draft data into the editor
    function loadDraftIntoEditor(draft) {
        if (!draft) return false;
        
        try {
            // Set the title
            setNameInput.value = draft.name || '';
            if (setClassSelect) setClassSelect.value = draft.classId || '';
            
            // Clear existing cards
            cardsContainer.innerHTML = '';
            
            // Add cards from draft
            if (draft.cards && Array.isArray(draft.cards)) {
                if (draft.cards.length > 0) {
                    draft.cards.forEach(card => {
                        addCard(card);
                    });
                } else {
                    // Add at least one empty card if no cards exist
                    addCard();
                }
            } else {
                // Add at least one empty card if no cards exist
                addCard();
            }
            
            updateCardCount();
            updateCardNumbers();
            updateAddBetweenButtons();
            
            draftLoaded = true;
            showToast('Draft loaded successfully', 'info');
            return true;
        } catch (error) {
            console.error('Error loading draft:', error);
            showToast('Error loading draft', 'error');
            return false;
        }
    }
    
    // Function to show the draft recovery modal
    function showDraftModal() {
        if (draftModal) {
            draftModal.classList.add('show');
        }
    }
    
    // Function to hide the draft recovery modal
    function hideDraftModal() {
        if (draftModal) {
            draftModal.classList.remove('show');
        }
    }

    async function continueDraft() {
        const draft = await loadDraft();
        if (draft) {
            loadDraftIntoEditor(draft);
        } else if (cardsContainer.children.length === 0) {
            addCard();
            updateCardCount();
            updateCardNumbers();
            updateAddBetweenButtons();
        }
        hideDraftModal();
    }
    
    // Function to delete the current draft
    async function deleteDraft() {
        await clearDraftState();
        draftLoaded = false;
        hideDraftModal();
        
        // Create a new empty set
        setNameInput.value = '';
        if (setClassSelect) setClassSelect.value = '';
        cardsContainer.innerHTML = '';
        addCard(); // Add first empty card
        updateCardCount();
        updateCardNumbers();
        updateAddBetweenButtons();
        
        showToast('Started new set', 'info');
    }

    // Helper function to get data from all cards
    function getCardsData() {
        return Array.from(cardsContainer.children)
            .filter(card => card.classList.contains('card-editor'))
            .map(card => {
            const termEditor = card.querySelector('.term-side .editor');
            const defEditor = card.querySelector('.definition-side .editor');
            const termImg = card.querySelector('.term-side .image-preview');
            const defImg = card.querySelector('.definition-side .image-preview');
            
            const cardData = {
                ...(card.__cardData || {}),
                term: termEditor ? termEditor.innerHTML : '',
                definition: defEditor ? defEditor.innerHTML : '',
                termImage: termImg && termImg.style.display !== 'none' && termImg.src ? termImg.src : '',
                definitionImage: defImg && defImg.style.display !== 'none' && defImg.src ? defImg.src : '',
                media: normalizeCardMedia(card.__cardData?.media || {}),
                background: normalizeCardBackground(card.__cardData || {}),
                tags: Array.isArray(card.__cardData?.tags) ? card.__cardData.tags : [],
                suspended: Boolean(card.__cardData?.suspended),
                buriedUntil: card.__cardData?.buriedUntil || null,
                reviewHistory: Array.isArray(card.__cardData?.reviewHistory) ? card.__cardData.reviewHistory : []
            };
            
            if (window.srsManager && window.srsManager.isReady() && !cardData.srs) {
                return window.srsManager.createSRSCard(cardData);
            }
            
            return cardData;
        });
    }

    // Save Set
    async function saveSet() {
        if (!await validateSet()) return false;

        try {
            // First get all card data
            const cardPromises = Array.from(cardsContainer.children)
                .filter(card => card.classList.contains('card-editor'))
                .map(async card => await getCardData(card));

            // Wait for all card data to be processed
            const allCards = await Promise.all(cardPromises);

            // Then filter out empty cards
            const cards = allCards.filter(cardHasContent);

            const flashcardSet = {
                ...(editMode && existingSetData ? existingSetData : {}),
                id: editMode ? editSetId : (window.flashcardStore?.saveSet ? undefined : Date.now()),
                name: setNameInput.value.trim(),
                classId: setClassSelect?.value && setClassSelect.value !== '__new' ? setClassSelect.value : null,
                cards,
                created: editMode ? existingSetData?.created : Date.now(),
                createdAt: editMode ? existingSetData?.createdAt : Date.now(),
                lastModified: Date.now(),
                openedCount: editMode ? (existingSetData?.openedCount || 0) : 0,
                srsSettings: existingSetData?.srsSettings || {
                    enabled: true,
                    requestRetention: 0.9,
                    maxIntervalDays: 36500,
                    newCardsPerDay: null,
                    reviewsPerDay: null
                }
            };

            const savedSet = window.flashcardStore?.saveSet
                ? await window.flashcardStore.saveSet(flashcardSet)
                : flashcardSet;

            if (!window.flashcardStore?.listSets) {
                const existingSets = JSON.parse(localStorage.getItem('flashcardSets') || '[]')
                    .filter(set => set.id !== savedSet.id)
                    .concat(savedSet);
                localStorage.setItem('flashcardSets', JSON.stringify(existingSets));
            }

            // Clear draft after successful save
            successfulSaveRedirecting = true;
            draftWritesSuppressed = true;
            cancelDraftTimers();
            await clearDraftState();

            // Clear state
            editMode = false;
            editSetId = null;
            existingSetData = null;

            // Show success message
            showToast('Flashcard set saved successfully', 'success');

            // Remove the beforeunload handler before redirecting
            window.removeEventListener('beforeunload', beforeUnloadHandler);

            // Redirect to the library page
            window.location.replace('flashcards.html');
            return true;
        } catch (error) {
            console.error('Error saving set:', error);
            showToast('Error saving flashcard set', 'error');
            return false;
        }
    }

    // Validation
    async function validateSet() {
        const name = setNameInput.value.trim();
        if (!name) {
            showToast('Please enter a set name', 'error');
            setNameInput.focus();
            setNameInput.classList.add('error');
            setTimeout(() => setNameInput.classList.remove('error'), 820); // Remove after shake animation
            return false;
        }

        try {
            // Get all card data
            const cardPromises = Array.from(cardsContainer.children)
                .filter(card => card.classList.contains('card-editor'))
                .map(async card => await getCardData(card));
            
            // Wait for all card data to be processed
            const allCards = await Promise.all(cardPromises);
            
            // Filter out empty cards
            const cards = allCards.filter(cardHasContent);

            if (cards.length === 0) {
                showToast('Please add at least one card with content', 'error');
                return false;
            }

            return true;
        } catch (error) {
            console.error('Error validating set:', error);
            showToast('Error validating set', 'error');
            return false;
        }
    }

    async function getCardData(cardElement) {
        if (!cardElement) {
            console.error('Card element is null or undefined');
            return { term: '', definition: '', termImage: '', definitionImage: '' };
        }

        const termEditor = cardElement.querySelector('.term-side .editor');
        const defEditor = cardElement.querySelector('.definition-side .editor');
        const termImg = cardElement.querySelector('.term-side .image-preview');
        const defImg = cardElement.querySelector('.definition-side .image-preview');
        
        function getImageSrc(img) {
            if (img && img.style && img.style.display !== 'none' && img.src) {
                return img.src;
            }
            return '';
        }

        const previous = cardElement.__cardData || {};
        const cardData = {
            ...previous,
            id: previous.id || cardElement.dataset.cardId || undefined,
            term: termEditor ? termEditor.innerHTML : '',
            definition: defEditor ? defEditor.innerHTML : '',
            termImage: getImageSrc(termImg),
            definitionImage: getImageSrc(defImg),
            media: normalizeCardMedia(previous.media || {}),
            background: normalizeCardBackground(previous),
            tags: Array.isArray(previous.tags) ? previous.tags : [],
            suspended: Boolean(previous.suspended),
            buriedUntil: previous.buriedUntil || null,
            reviewHistory: Array.isArray(previous.reviewHistory) ? previous.reviewHistory : []
        };
        
        // Add SRS fields only for new cards. Existing cards keep their scheduling.
        if (window.srsManager && window.srsManager.isReady() && !cardData.srs) {
            const initialized = window.srsManager.createSRSCard(cardData);
            cardElement.__cardData = initialized;
            return initialized;
        }
        
        cardElement.__cardData = cardData;
        return cardData;
    }

    function validateCard(cardElement) {
        const termEditor = cardElement.querySelector('.term-side .editor');
        const defEditor = cardElement.querySelector('.definition-side .editor');
        const termImg = cardElement.querySelector('.term-side .image-preview');
        const defImg = cardElement.querySelector('.definition-side .image-preview');
        
        const termContent = termEditor ? termEditor.textContent.trim() : '';
        const definitionContent = defEditor ? defEditor.textContent.trim() : '';
        
        const hasTermImage = termImg && termImg.style.display !== 'none' && termImg.src;
        const hasDefImage = defImg && defImg.style.display !== 'none' && defImg.src;
        
        return cardHasContent({
            ...(cardElement.__cardData || {}),
            term: termContent,
            definition: definitionContent,
            termImage: hasTermImage ? termImg.src : '',
            definitionImage: hasDefImage ? defImg.src : ''
        });
    }

    function updateCardNumbers() {
        let cardIndex = 0;
        Array.from(cardsContainer.children).forEach(child => {
            if (child.classList.contains('card-editor')) {
                const number = child.querySelector('.card-number');
                if (number) {
                    number.textContent = cardIndex + 1;
                }
                cardIndex++;
            }
        });
    }

    function updateCardCount() {
        // Count only actual card elements, not add-between buttons
        const count = Array.from(cardsContainer.children).filter(
            child => child.classList.contains('card-editor')
        ).length;
        cardCountSpan.textContent = `${count} card${count === 1 ? '' : 's'}`;
    }

    function showToast(message, type = 'info') {
        const toast = document.createElement('div');
        toast.className = `toast toast-${type}`;
        toast.innerHTML = `
            <i class="fas fa-${type === 'success' ? 'check-circle' : type === 'error' ? 'exclamation-circle' : 'info-circle'}"></i>
            <span>${message}</span>
        `;
        
        document.body.appendChild(toast);
        setTimeout(() => {
            toast.classList.add('show');
        }, 100);
        
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => {
                document.body.removeChild(toast);
            }, 300);
        }, 3000);
    }

    // Handle page unload. New unsaved sets are protected by local drafts;
    // existing sets are saved through explicit Save / Save and Go Back.
    const beforeUnloadHandler = (e) => {
        if (!editMode && !draftWritesSuppressed && !successfulSaveRedirecting) saveDraft();
    };

    window.addEventListener('beforeunload', beforeUnloadHandler);
    window.addEventListener('pagehide', () => {
        if (!editMode && !draftWritesSuppressed && !successfulSaveRedirecting) saveDraft();
    });

    // Clean up event listeners when navigating away
    window.addEventListener('unload', async () => {
        if (documentClickListener) {
            document.removeEventListener('click', documentClickListener);
        }
        window.removeEventListener('beforeunload', beforeUnloadHandler);
        
        if (!editMode && !draftWritesSuppressed && !successfulSaveRedirecting) saveDraft();
    });
    
    // Add event listener for back button
    if (backButton) {
        backButton.addEventListener('click', async (e) => {
            e.preventDefault();
            
            if (editMode) {
                // In edit mode, save the set before going back
                backButton.disabled = true;
                try {
                    const saved = await saveSet();
                    if (saved) {
                        // If saved successfully, redirect to the library page
                        window.location.href = 'flashcards.html';
                    } else {
                        // If there was an error saving, re-enable the button
                        backButton.disabled = false;
                    }
                } catch (error) {
                    console.error('Error saving set:', error);
                    showToast('Error saving flashcard set', 'error');
                    backButton.disabled = false;
                }
            } else {
                saveDraft();
                window.location.href = 'flashcards.html';
            }
        });
    }

    // Load existing set for editing
    async function loadExistingSet(setId) {
        // Clear any existing draft when loading a set for editing
        await clearDraftState();

        if (!setId) {
            console.error('Invalid set ID');
            showToast('Invalid flashcard set ID', 'error');
            window.location.href = 'flashcards.html';
            return;
        }

        try {
            const sets = window.flashcardStore?.listSets
                ? await window.flashcardStore.listSets()
                : JSON.parse(localStorage.getItem('flashcardSets') || '[]');
            const set = sets.find(s => String(s.id) === String(setId));

            if (!set) {
                showToast('Flashcard set not found', 'error');
                window.location.href = 'flashcards.html';
                return;
            }

            existingSetData = set;
            editSetId = set.id;

            // Load set name
            setNameInput.value = set.name || '';
            await loadFlashcardClasses(set.classId || '');

            // Clear any existing cards
            cardsContainer.innerHTML = '';

            // Load cards
            if (set.cards && Array.isArray(set.cards)) {
                set.cards.forEach(card => {
                    addCard(card);
                });
            } else {
                // Add at least one empty card if no cards exist
                addCard();
            }

            updateCardCount();
            showToast('Flashcard set loaded for editing', 'info');
        } catch (error) {
            console.error('Error loading flashcard set:', error);
            showToast('Error loading flashcard set', 'error');
        }
    }

    // Function to add multiple cards at once
    function addBulkCards(count) {
        let lastCard = null;
        
        for (let i = 0; i < count; i++) {
            lastCard = addCard();
        }
        
        showToast(`Added ${count} cards successfully`, 'success');
        return lastCard;
    }

    // Export flashcard set to JSON file
    async function exportSet() {
        try {
            const setName = setNameInput.value.trim() || 'Untitled Set';
            
            // Get cards data
            const cards = getCardsData().filter(cardHasContent);
            
            if (cards.length === 0) {
                showToast('Cannot export empty set', 'error');
                return;
            }
            
            const flashcardSet = {
                name: setName,
                classId: setClassSelect?.value && setClassSelect.value !== '__new' ? setClassSelect.value : null,
                cards: cards,
                exportDate: Date.now()
            };
            
            // Convert to JSON string
            const jsonString = JSON.stringify(flashcardSet, null, 2);
            
            // For web: Create a download link
            const blob = new Blob([jsonString], { type: 'application/json' });
            const url = URL.createObjectURL(blob);
            
            const a = document.createElement('a');
            a.href = url;
            a.download = `${setName.replace(/[^a-z0-9]/gi, '_').toLowerCase()}.json`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            
            showToast('Set exported successfully', 'success');
            
            // In Electron, we'd use the Electron API instead
            /*
            if (window.electron) {
                window.electron.saveFile(jsonString, setName);
            }
            */
        } catch (error) {
            console.error('Error exporting set:', error);
            showToast('Error exporting set', 'error');
        }
    }

    // Import flashcard set from JSON file
    async function importSet() {
        try {
            // For web: Create file input
            const fileInput = document.createElement('input');
            fileInput.type = 'file';
            fileInput.accept = '.json';
            
            fileInput.addEventListener('change', async (e) => {
                const file = e.target.files[0];
                if (!file) return;
                
                const reader = new FileReader();
                reader.onload = async (event) => {
                    try {
                        const data = JSON.parse(event.target.result);
                        
                        if (!data.cards || !Array.isArray(data.cards)) {
                            showToast('Invalid flashcard set file', 'error');
                            return;
                        }
                        
                        // Clear existing content
                        setNameInput.value = data.name || '';
                        if (setClassSelect) setClassSelect.value = data.classId || '';
                        cardsContainer.innerHTML = '';
                        
                        // Import cards
                        let lastCard = null;
                        data.cards.forEach(card => {
                            lastCard = addCard(card);
                        });
                        
                        updateCardNumbers();
                        updateCardCount();
                        updateAddBetweenButtons();
                        triggerAutosave();
                        
                        showToast(`Imported ${data.cards.length} cards successfully`, 'success');
                        
                        // Scroll to first card
                        if (lastCard) {
                            setTimeout(() => {
                                cardsContainer.firstElementChild.scrollIntoView({ behavior: 'smooth', block: 'start' });
                            }, 100);
                        }
                    } catch (error) {
                        console.error('Error parsing import file:', error);
                        showToast('Invalid flashcard set file', 'error');
                    }
                };
                
                reader.readAsText(file);
            });
            
            fileInput.click();
            
            // In Electron, we'd use the Electron API instead
            /*
            if (window.electron) {
                const result = await window.electron.openFile();
                if (result.success) {
                    // Process the file content from result.data
                }
            }
            */
        } catch (error) {
            console.error('Error importing set:', error);
            showToast('Error importing set', 'error');
        }
    }

    // Set up event listeners for import/export buttons
    const importBtn = document.getElementById('import-btn');
    if (importBtn) {
        importBtn.addEventListener('click', importSet);
    }

    const exportBtn = document.getElementById('export-btn');
    if (exportBtn) {
        exportBtn.addEventListener('click', exportSet);
    }

    // Set up keyboard shortcuts modal
    const shortcutsHelpBtn = document.getElementById('shortcuts-help-btn');
    const shortcutsModal = document.getElementById('shortcuts-modal');
    const closeShortcutsBtn = document.querySelector('.close-shortcuts-btn');
    
    // Set up file help modal
    const fileHelpBtn = document.getElementById('file-help-btn');
    const fileHelpModal = document.getElementById('file-help-modal');
    const closeFileHelpBtn = document.querySelector('.close-file-help-btn');
    
    // Set up draft modal event handlers
    if (draftModal) {
        // Handle continue draft button
        if (continueDraftBtn) {
            continueDraftBtn.addEventListener('click', continueDraft);
        }
        
        // Handle delete draft button
        if (deleteDraftBtn) {
            deleteDraftBtn.addEventListener('click', () => {
                deleteDraft();
            });
        }
        
        // Handle close button
        if (closeDraftBtn) {
            closeDraftBtn.addEventListener('click', continueDraft);
        }
        
        // Close on Escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && draftModal.classList.contains('show')) {
                continueDraft();
            }
        });
    }

    if (shortcutsHelpBtn && shortcutsModal) {
        shortcutsHelpBtn.addEventListener('click', () => {
            shortcutsModal.classList.add('show');
        });
        
        // Close on X button click
        if (closeShortcutsBtn) {
            closeShortcutsBtn.addEventListener('click', () => {
                shortcutsModal.classList.remove('show');
            });
        }
        
        // Close on click outside
        shortcutsModal.addEventListener('click', (e) => {
            if (e.target === shortcutsModal) {
                shortcutsModal.classList.remove('show');
            }
        });
        
        // Close on Escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && shortcutsModal.classList.contains('show')) {
                shortcutsModal.classList.remove('show');
            }
        });
    }

    // Set up file help modal event handlers
    if (fileHelpBtn && fileHelpModal) {
        fileHelpBtn.addEventListener('click', () => {
            fileHelpModal.classList.add('show');
        });
        
        // Close on X button click
        if (closeFileHelpBtn) {
            closeFileHelpBtn.addEventListener('click', () => {
                fileHelpModal.classList.remove('show');
            });
        }
        
        // Close on click outside
        fileHelpModal.addEventListener('click', (e) => {
            if (e.target === fileHelpModal) {
                fileHelpModal.classList.remove('show');
            }
        });
        
        // Close on Escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && fileHelpModal.classList.contains('show')) {
                fileHelpModal.classList.remove('show');
            }
        });
    }

    // Function to enforce text wrapping on editors
    function ensureEditorWrapping(editor) {
        editor.style.wordWrap = 'break-word';
        editor.style.overflowWrap = 'break-word';
        editor.style.whiteSpace = 'pre-wrap';
        editor.style.width = '100%';
        editor.style.maxWidth = '100%';
        editor.style.display = 'block';
        
        // Add event listener to enforce wrapping on input
        editor.addEventListener('input', function() {
            this.style.wordWrap = 'break-word';
            this.style.overflowWrap = 'break-word';
            this.style.whiteSpace = 'pre-wrap';
        });
    }
});
