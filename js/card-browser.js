document.addEventListener('DOMContentLoaded', async () => {
    if (window.flashcardLocalReady) await window.flashcardLocalReady;

    const searchInput = document.getElementById('card-search');
    const stateFilter = document.getElementById('card-state-filter');
    const tableBody = document.getElementById('card-browser-body');
    const emptyState = document.getElementById('card-browser-empty');
    const subtitle = document.getElementById('browser-subtitle');
    const totalCardsEl = document.getElementById('browser-total-cards');
    const dueCardsEl = document.getElementById('browser-due-cards');
    const suspendedCardsEl = document.getElementById('browser-suspended-cards');

    let sets = [];
    let rows = [];

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

    function stripHtml(value = '') {
        const element = document.createElement('div');
        element.innerHTML = value;
        return element.textContent || element.innerText || '';
    }

    function textPreview(value = '', length = 90) {
        const text = stripHtml(value).replace(/\s+/g, ' ').trim();
        return text.length > length ? `${text.slice(0, length - 1)}...` : text;
    }

    function formatDue(value) {
        if (!value) return 'Now';
        const date = new Date(value);
        if (Number.isNaN(date.getTime())) return 'Now';
        if (window.srsManager?.formatIntervalLabel) {
            const label = window.srsManager.formatIntervalLabel(date);
            return label === 'now' ? 'Now' : `in ${label}`;
        }
        return date.toLocaleDateString();
    }

    function getCardState(card) {
        if (card.suspended) return 'Suspended';
        return card.srs?.state || 'New';
    }

    function buildRows() {
        rows = [];
        sets.forEach(set => {
            (set.cards || []).forEach((card, cardIndex) => {
                rows.push({
                    setId: set.id,
                    setName: set.name || 'Untitled',
                    set,
                    card,
                    cardIndex
                });
            });
        });
    }

    function matchesFilters(row) {
        const search = searchInput.value.trim().toLowerCase();
        const state = getCardState(row.card);

        if (stateFilter.value !== 'all' && state !== stateFilter.value) {
            return false;
        }

        if (!search) return true;

        const haystack = [
            row.setName,
            stripHtml(row.card.term || ''),
            stripHtml(row.card.definition || ''),
            state,
            ...(Array.isArray(row.card.tags) ? row.card.tags : [])
        ].join(' ').toLowerCase();

        return haystack.includes(search);
    }

    function updateStats() {
        const totalCards = rows.length;
        const suspendedCards = rows.filter(row => row.card.suspended).length;
        let dueCards = 0;

        if (window.srsManager?.isReady?.()) {
            sets.forEach(set => {
                const cards = Array.isArray(set.cards) ? set.cards : [];
                dueCards += window.srsManager.getDueCards(cards, {
                    maxNewCards: null,
                    maxDueCards: null,
                    allowMultipleSessions: true,
                    settings: set.srsSettings || {}
                }).length;
            });
        }

        totalCardsEl.textContent = String(totalCards);
        dueCardsEl.textContent = String(dueCards);
        suspendedCardsEl.textContent = String(suspendedCards);
        subtitle.textContent = `${sets.length} decks | ${totalCards} cards | local library`;
    }

    function createCell(text, className = '') {
        const cell = document.createElement('td');
        if (className) cell.className = className;
        cell.textContent = text;
        return cell;
    }

    function createActionButton(iconClass, title, onClick) {
        const button = document.createElement('button');
        button.className = 'browser-action-btn';
        button.title = title;
        button.innerHTML = `<i class="${iconClass}"></i>`;
        button.addEventListener('click', onClick);
        return button;
    }

    function renderRows() {
        tableBody.innerHTML = '';
        const visibleRows = rows.filter(matchesFilters);

        emptyState.classList.toggle('hidden', visibleRows.length > 0);

        visibleRows.forEach(row => {
            const tr = document.createElement('tr');
            const card = row.card;
            const state = getCardState(card);

            tr.appendChild(createCell(row.setName, 'deck-cell'));
            tr.appendChild(createCell(textPreview(card.term, 60), 'term-cell'));
            tr.appendChild(createCell(textPreview(card.definition, 95), 'definition-cell'));

            const stateCell = createCell(state);
            stateCell.appendChild(document.createElement('span'));
            stateCell.className = `state-cell state-${state.toLowerCase()}`;
            stateCell.textContent = state;
            tr.appendChild(stateCell);

            tr.appendChild(createCell(card.suspended ? 'Suspended' : formatDue(card.srs?.due)));
            tr.appendChild(createCell(String(card.srs?.reps || 0)));
            tr.appendChild(createCell(Array.isArray(card.tags) && card.tags.length ? card.tags.join(', ') : '-'));

            const actions = document.createElement('td');
            actions.className = 'browser-actions';
            actions.appendChild(createActionButton('fas fa-edit', 'Edit deck', () => {
                window.location.href = `creator.html?setId=${encodeURIComponent(row.setId)}`;
            }));
            actions.appendChild(createActionButton(card.suspended ? 'fas fa-play' : 'fas fa-pause', card.suspended ? 'Unsuspend card' : 'Suspend card', () => {
                toggleSuspend(row);
            }));
            actions.appendChild(createActionButton('fas fa-rotate-left', 'Reset SRS', () => {
                resetCardSrs(row);
            }));
            actions.appendChild(createActionButton('fas fa-trash', 'Delete card', () => {
                deleteCard(row);
            }));
            tr.appendChild(actions);

            tableBody.appendChild(tr);
        });
    }

    async function saveSetAndRefresh(set, message) {
        if (window.flashcardStore?.saveSet) {
            await window.flashcardStore.saveSet(set);
            sets = await window.flashcardStore.listSets();
        } else {
            const currentSets = JSON.parse(localStorage.getItem('flashcardSets') || '[]');
            sets = currentSets.map(current => String(current.id) === String(set.id) ? set : current);
            localStorage.setItem('flashcardSets', JSON.stringify(sets));
        }

        buildRows();
        updateStats();
        renderRows();
        showToast(message, 'success');
    }

    async function toggleSuspend(row) {
        const set = { ...row.set, cards: [...(row.set.cards || [])] };
        const card = { ...set.cards[row.cardIndex], suspended: !row.card.suspended };
        set.cards[row.cardIndex] = card;
        await saveSetAndRefresh(set, card.suspended ? 'Card suspended' : 'Card unsuspended');
    }

    async function resetCardSrs(row) {
        if (!window.confirm('Reset SRS scheduling for this card? Review history will be cleared.')) return;

        const set = { ...row.set, cards: [...(row.set.cards || [])] };
        const previous = set.cards[row.cardIndex];
        let resetCard = {
            ...previous,
            srs: undefined,
            reviewHistory: []
        };

        if (window.srsManager?.isReady?.()) {
            resetCard = window.srsManager.createSRSCard(resetCard);
        }

        set.cards[row.cardIndex] = resetCard;
        await saveSetAndRefresh(set, 'Card SRS reset');
    }

    async function deleteCard(row) {
        if (!window.confirm('Delete this card from the deck?')) return;

        const set = { ...row.set };
        set.cards = (row.set.cards || []).filter((card, index) => {
            if (row.card.id && card.id) return String(card.id) !== String(row.card.id);
            return index !== row.cardIndex;
        });
        set.lastModified = Date.now();
        await saveSetAndRefresh(set, 'Card deleted');
    }

    async function loadCards() {
        try {
            sets = window.flashcardStore?.listSets
                ? await window.flashcardStore.listSets()
                : JSON.parse(localStorage.getItem('flashcardSets') || '[]');
            buildRows();
            updateStats();
            renderRows();
        } catch (error) {
            console.error('Error loading card browser:', error);
            showToast('Could not load card browser', 'error');
        }
    }

    searchInput.addEventListener('input', renderRows);
    stateFilter.addEventListener('change', renderRows);
    window.addEventListener('erudite-menu-toast', (event) => {
        const { message, type } = event.detail || {};
        if (message) showToast(message, type || 'info');
    });

    await loadCards();
});
