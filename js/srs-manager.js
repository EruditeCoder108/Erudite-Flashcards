/**
 * SRS Manager - Handles Spaced Repetition System functionality
 * Integrates with ts-fsrs library for advanced spaced repetition algorithms
 */

class SRSManager {
    constructor() {
        this.fsrs = null;
        this.fsrsCache = new Map();
        this.isInitialized = false;
        this.init();
    }

    /**
     * Initialize the FSRS instance
     */
    init() {
        try {
            // Check if FSRS is available globally
            if (typeof FSRS !== 'undefined' && FSRS.fsrs) {
                // Create FSRS instance with default parameters
                this.fsrs = FSRS.fsrs({
                    request_retention: 0.9,
                    maximum_interval: 36500,
                    enable_fuzz: true,
                    enable_short_term: true
                });
                this.fsrsCache.set('0.9|36500', this.fsrs);
                this.isInitialized = true;
            } else {
                console.warn('FSRS library not loaded. SRS functionality will be disabled.');
                this.isInitialized = false;
            }
        } catch (error) {
            console.error('Failed to initialize SRS Manager:', error);
            this.isInitialized = false;
        }
    }

    normalizeSettings(settings = {}) {
        const finiteNumber = (value, fallback) => {
            const number = Number(value);
            return Number.isFinite(number) ? number : fallback;
        };
        const limitOrNull = (value) => {
            if (value === null || value === undefined || value === '') return null;
            const number = Number(value);
            return Number.isFinite(number) ? Math.max(0, Math.round(number)) : null;
        };
        const requestRetention = finiteNumber(settings.requestRetention, 0.9);
        const maxIntervalDays = finiteNumber(settings.maxIntervalDays, 36500);

        return {
            enabled: settings.enabled !== false,
            requestRetention: Math.min(0.99, Math.max(0.7, requestRetention)),
            maxIntervalDays: Math.max(1, Math.round(maxIntervalDays)),
            newCardsPerDay: limitOrNull(settings.newCardsPerDay),
            reviewsPerDay: limitOrNull(settings.reviewsPerDay)
        };
    }

    getScheduler(settings = {}) {
        if (!this.isInitialized) return null;

        const normalized = this.normalizeSettings(settings);
        const key = `${normalized.requestRetention}|${normalized.maxIntervalDays}`;
        if (!this.fsrsCache.has(key)) {
            this.fsrsCache.set(key, FSRS.fsrs({
                request_retention: normalized.requestRetention,
                maximum_interval: normalized.maxIntervalDays,
                enable_fuzz: true,
                enable_short_term: true
            }));
        }

        return this.fsrsCache.get(key);
    }

    getStateName(state) {
        if (typeof state === 'number') {
            return FSRS.State[state] || 'New';
        }
        return state || 'New';
    }

    getStateValue(state) {
        if (typeof state === 'number') {
            return state;
        }
        return FSRS.State[state] ?? FSRS.State.New;
    }

    toISODate(value) {
        if (!value) return null;

        const date = new Date(value);
        return isNaN(date.getTime()) ? null : date.toISOString();
    }

    isDue(srsData, now = new Date()) {
        if (!srsData || !srsData.due) return true;

        const dueDate = new Date(srsData.due);
        return isNaN(dueDate.getTime()) || dueDate <= now;
    }

    toFSRSCard(card) {
        const now = new Date();
        const dueDate = card.srs?.due ? new Date(card.srs.due) : now;
        const lastReviewDate = card.srs?.lastReview ? new Date(card.srs.lastReview) : undefined;

        return {
            due: isNaN(dueDate.getTime()) ? now : dueDate,
            stability: card.srs?.stability ?? 0,
            difficulty: card.srs?.difficulty ?? 0,
            elapsed_days: card.srs?.elapsedDays ?? 0,
            scheduled_days: card.srs?.scheduledDays ?? 0,
            learning_steps: card.srs?.learningSteps ?? 0,
            reps: card.srs?.reps ?? 0,
            lapses: card.srs?.lapses ?? 0,
            state: this.getStateValue(card.srs?.state),
            last_review: lastReviewDate && !isNaN(lastReviewDate.getTime()) ? lastReviewDate : undefined
        };
    }

    formatIntervalLabel(due, from = new Date()) {
        const dueDate = new Date(due);
        if (isNaN(dueDate.getTime())) return 'soon';

        const diffMs = Math.max(0, dueDate.getTime() - from.getTime());
        const minutes = Math.round(diffMs / 60000);
        if (minutes < 1) return 'now';
        if (minutes < 60) return `${minutes}m`;

        const hours = Math.round(minutes / 60);
        if (hours < 24) return `${hours}h`;

        const days = Math.round(hours / 24);
        if (days < 30) return `${days}d`;

        const months = Math.round(days / 30);
        if (months < 12) return `${months}mo`;

        const years = Math.round(months / 12);
        return `${years}y`;
    }

    getRatingPreviews(card, settings = {}) {
        if (!this.isInitialized) return {};

        try {
            const scheduler = this.getScheduler(settings);
            const srsCard = card.srs ? this.toFSRSCard(card) : FSRS.createEmptyCard();
            const now = new Date();
            const preview = scheduler.repeat(srsCard, now);
            const ratings = ['Again', 'Hard', 'Good', 'Easy'];

            return ratings.reduce((result, rating) => {
                const ratingResult = preview[FSRS.Rating[rating]];
                const nextCard = ratingResult?.card;

                result[rating] = {
                    intervalLabel: nextCard?.due ? this.formatIntervalLabel(nextCard.due, now) : 'soon',
                    due: this.toISODate(nextCard?.due),
                    state: this.getStateName(nextCard?.state),
                    scheduledDays: nextCard?.scheduled_days ?? 0
                };

                return result;
            }, {});
        } catch (error) {
            console.error('Error previewing SRS ratings:', error);
            return {};
        }
    }

    /**
     * Create a new card with default SRS fields
     * @param {Object} cardData - Basic card data (term, definition, etc.)
     * @returns {Object} Card with SRS fields initialized
     */
    createSRSCard(cardData) {
        if (!this.isInitialized) {
            console.warn('SRS not initialized, returning card without SRS fields');
            return cardData;
        }

        try {
            // Create empty FSRS card
            const fsrsCard = FSRS.createEmptyCard();
            
            // Convert FSRS card to our format
            const srsData = {
                stability: fsrsCard.stability,
                difficulty: fsrsCard.difficulty,
                elapsedDays: fsrsCard.elapsed_days || 0,
                scheduledDays: fsrsCard.scheduled_days,
                reps: fsrsCard.reps,
                lapses: fsrsCard.lapses,
                state: this.getStateName(fsrsCard.state),
                lastReview: this.toISODate(fsrsCard.last_review),
                due: this.toISODate(fsrsCard.due),
                interval: fsrsCard.scheduled_days,
                learningSteps: fsrsCard.learning_steps
            };

            return {
                ...cardData,
                srs: srsData
            };
        } catch (error) {
            console.error('Error creating SRS card:', error);
            return cardData;
        }
    }

    /**
     * Process a card review with rating
     * @param {Object} card - Card with SRS data
     * @param {string} rating - Rating: 'Again', 'Hard', 'Good', 'Easy'
     * @returns {Object} Updated card with new SRS data
     */
    reviewCard(card, rating, settings = {}) {
        if (!this.isInitialized) {
            console.warn('SRS not initialized');
            return card;
        }

        // If card doesn't have SRS data, create it
        if (!card.srs) {
            card = this.createSRSCard(card);
        }

        try {
            const scheduler = this.getScheduler(settings);
            // Convert our card format to FSRS format
            const fsrsCard = this.toFSRSCard(card);

            // Get rating enum
            const ratingEnum = FSRS.Rating[rating];
            if (ratingEnum === undefined) {
                throw new Error(`Invalid rating: ${rating}`);
            }

            // Process the review
            const result = scheduler.next(fsrsCard, new Date(), ratingEnum);
            
            // Convert back to our format
            const updatedSRS = {
                stability: result.card.stability,
                difficulty: result.card.difficulty,
                elapsedDays: result.card.elapsed_days || 0,
                scheduledDays: result.card.scheduled_days,
                reps: result.card.reps,
                lapses: result.card.lapses,
                state: this.getStateName(result.card.state),
                lastReview: this.toISODate(result.card.last_review) || new Date().toISOString(),
                due: this.toISODate(result.card.due),
                interval: result.card.scheduled_days,
                learningSteps: result.card.learning_steps
            };

            // Debug logging

            return {
                ...card,
                srs: updatedSRS
            };
        } catch (error) {
            console.error('Error reviewing card:', error);
            return card;
        }
    }

    getSRSDay(dateVal, rolloverHour = 4) {
        const d = new Date(dateVal);
        if (isNaN(d.getTime())) return null;
        // Subtract rollover hours to align with the SRS day rollover boundary (default 4:00 AM)
        const adjusted = new Date(d.getTime() - rolloverHour * 60 * 60 * 1000);
        const yyyy = adjusted.getFullYear();
        const mm = String(adjusted.getMonth() + 1).padStart(2, '0');
        const dd = String(adjusted.getDate()).padStart(2, '0');
        return `${yyyy}-${mm}-${dd}`;
    }

    getReviewsStatsToday(cards, settings = {}) {
        const rolloverHour = 4; // default 4 AM rollover
        const todaySRS = this.getSRSDay(new Date(), rolloverHour);

        let newCardsToday = 0;
        let reviewsToday = 0;

        cards.forEach(card => {
            if (!Array.isArray(card.reviewHistory) || card.reviewHistory.length === 0) return;

            // Sort review history by time ascending to inspect the first review
            const sortedHistory = [...card.reviewHistory].sort((a, b) => {
                const timeA = new Date(a.reviewedAt || a.time || a.timestamp || a.date || 0).getTime();
                const timeB = new Date(b.reviewedAt || b.time || b.timestamp || b.date || 0).getTime();
                return timeA - timeB;
            });

            // Find first review of this card (when it was introduced)
            const firstReview = sortedHistory[0];
            const firstReviewTime = firstReview.reviewedAt || firstReview.time || firstReview.timestamp || firstReview.date;
            const firstReviewDay = this.getSRSDay(firstReviewTime, rolloverHour);
            if (firstReviewDay === todaySRS && (firstReview.previousState === 'New' || !firstReview.previousState)) {
                newCardsToday++;
            }

            // Count mature reviews completed today
            sortedHistory.forEach(review => {
                const reviewTime = review.reviewedAt || review.time || review.timestamp || review.date;
                const reviewDay = this.getSRSDay(reviewTime, rolloverHour);
                if (reviewDay === todaySRS) {
                    if (review.previousState === 'Review') {
                        reviewsToday++;
                    }
                }
            });
        });

        return { newCardsToday, reviewsToday };
    }

    /**
     * Get cards that are due for review
     * @param {Array} cards - Array of cards with SRS data
     * @param {Object} options - Options for filtering cards
     * @returns {Array} Cards that are due for review
     */
    getDueCards(cards, options = {}) {
        if (!this.isInitialized) {
            return cards; // Return all cards if SRS not initialized
        }

        const {
            maxNewCards = null,      // Maximum new cards to show (null = unlimited)
            maxDueCards = null,      // Maximum due cards to show (null = unlimited)
            allowMultipleSessions = true,  // Allow multiple sessions per day
            settings = {}
        } = options;

        const normalizedSettings = this.normalizeSettings(settings);
        if (!normalizedSettings.enabled) return [];

        const now = new Date();

        // 1. Calculate how many reviews/new cards have already been done today on this deck
        const { newCardsToday, reviewsToday } = this.getReviewsStatsToday(cards, settings);

        // 2. Determine remaining limits
        const effectiveMaxNewCards = maxNewCards ?? normalizedSettings.newCardsPerDay;
        const effectiveMaxDueCards = maxDueCards ?? normalizedSettings.reviewsPerDay;

        const allowedNew = effectiveMaxNewCards === null ? null : Math.max(0, effectiveMaxNewCards - newCardsToday);
        const allowedReviews = effectiveMaxDueCards === null ? null : Math.max(0, effectiveMaxDueCards - reviewsToday);

        // 3. Separate cards into categories
        let dueLearningRelearning = [];
        let dueReviews = [];
        let newCards = [];

        cards.forEach(card => {
            if (card.suspended) return;
            if (card.buriedUntil) {
                const buriedUntil = new Date(card.buriedUntil);
                if (!isNaN(buriedUntil.getTime()) && buriedUntil > now) return;
            }

            // Determine if card is New
            const isCardNew = !card.srs || card.srs.state === 'New';
            if (isCardNew) {
                newCards.push(card);
                return;
            }

            const state = card.srs.state;
            if (state === 'Learning' || state === 'Relearning') {
                if (this.isDue(card.srs, now)) {
                    dueLearningRelearning.push(card);
                }
            } else if (state === 'Review') {
                if (this.isDue(card.srs, now)) {
                    dueReviews.push(card);
                }
            }
        });

        // 4. Sort reviews and learning cards by due date (ascending)
        dueLearningRelearning.sort((a, b) => {
            const dueA = new Date(a.srs?.due || 0).getTime();
            const dueB = new Date(b.srs?.due || 0).getTime();
            return dueA - dueB;
        });

        dueReviews.sort((a, b) => {
            const dueA = new Date(a.srs?.due || 0).getTime();
            const dueB = new Date(b.srs?.due || 0).getTime();
            return dueA - dueB;
        });

        // 5. Apply limits to categories
        // Learning/Relearning cards are never capped!
        if (allowedReviews !== null) {
            dueReviews = dueReviews.slice(0, allowedReviews);
        }

        if (allowedNew !== null) {
            newCards = newCards.slice(0, allowedNew);
        }

        // 6. Concatenate in prioritized order:
        // Due Learning/Relearning first, then due mature Review cards, then New cards.
        return [...dueLearningRelearning, ...dueReviews, ...newCards];
    }

    /**
     * Get SRS statistics for a set of cards
     * @param {Array} cards - Array of cards with SRS data
     * @returns {Object} SRS statistics
     */
    getSRSStatistics(cards) {
        if (!this.isInitialized) {
            return {
                totalCards: cards.length,
                activeCards: cards.length,
                newCards: cards.length,
                dueCards: cards.length,
                learningCards: 0,
                reviewCards: 0,
                relearningCards: 0,
                masteredCards: 0
            };
        }

        const stats = {
            totalCards: cards.length,
            activeCards: 0,
            newCards: 0,
            dueCards: 0,
            learningCards: 0,
            reviewCards: 0,
            relearningCards: 0,
            masteredCards: 0
        };

        const now = new Date();

        cards.forEach(card => {
            if (card.suspended) return;
            if (card.buriedUntil) {
                const buriedUntil = new Date(card.buriedUntil);
                if (!isNaN(buriedUntil.getTime()) && buriedUntil > now) return;
            }

            stats.activeCards++;

            if (!card.srs) {
                stats.newCards++;
                stats.dueCards++;
                return;
            }

            // Count by state
            switch (card.srs.state) {
                case 'New':
                    stats.newCards++;
                    stats.dueCards++; // New cards are always due
                    break;
                case 'Learning':
                    stats.learningCards++;
                    if (this.isDue(card.srs, now)) {
                        stats.dueCards++;
                    }
                    break;
                case 'Review':
                    stats.reviewCards++;
                    // Check if this review card is due
                    if (this.isDue(card.srs, now)) {
                        stats.dueCards++;
                    } else {
                        stats.masteredCards++; // Card is mastered (not due yet)
                    }
                    break;
                case 'Relearning':
                    stats.relearningCards++;
                    if (this.isDue(card.srs, now)) {
                        stats.dueCards++;
                    }
                    break;
            }
        });

        // Log detailed statistics

        return stats;
    }

    /**
     * Log detailed SRS information for debugging
     * @param {Array} cards - Array of cards with SRS data
     */
    logSRSDetails(cards) {
        if (!this.isInitialized) {
            return;
        }

        cards.forEach((card, index) => {
            const cardInfo = {
                index: index,
                term: card.term?.substring(0, 30) + (card.term?.length > 30 ? '...' : '') || 'No term',
                hasSRS: !!card.srs,
                state: card.srs?.state || 'None',
                due: card.srs?.due || 'None',
                difficulty: card.srs?.difficulty || 'None',
                interval: card.srs?.interval || 'None'
            };
        });
    }

    /**
     * Check if SRS is available and initialized
     * @returns {boolean} True if SRS is ready to use
     */
    isReady() {
        return this.isInitialized && this.fsrs !== null;
    }

    /**
     * Get the current FSRS instance
     * @returns {Object|null} FSRS instance or null if not initialized
     */
    getFSRSInstance() {
        return this.fsrs;
    }
}

// Create global instance
window.srsManager = new SRSManager();

// Export for module systems
if (typeof module !== 'undefined' && module.exports) {
    module.exports = SRSManager;
}
