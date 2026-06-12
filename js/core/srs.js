(function (root, factory) {
  const api = factory(root.EruditeCore?.stats);
  root.EruditeCore = root.EruditeCore || {};
  root.EruditeCore.srs = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
})(typeof globalThis !== 'undefined' ? globalThis : window, function (stats) {
  function manager() {
    return typeof window !== 'undefined' ? window.srsManager : null;
  }

  function normalizeSettings(settings = {}) {
    const srsManager = manager();
    if (srsManager?.normalizeSettings) return srsManager.normalizeSettings(settings);
    return {
      enabled: settings.enabled !== false,
      requestRetention: Math.min(0.99, Math.max(0.7, Number(settings.requestRetention) || 0.9)),
      maxIntervalDays: Math.max(1, Math.round(Number(settings.maxIntervalDays) || 36500)),
      newCardsPerDay: settings.newCardsPerDay ?? null,
      reviewsPerDay: settings.reviewsPerDay ?? null
    };
  }

  function getRatingPreviews(card, settings = {}) {
    return manager()?.getRatingPreviews?.(card, settings) || {};
  }

  function reviewCard(card, rating, settings = {}) {
    return manager()?.reviewCard?.(card, rating, settings) || card;
  }

  function getDueCards(cards = [], options = {}) {
    const srsManager = manager();
    if (srsManager?.getDueCards) return srsManager.getDueCards(cards, options);

    const now = options.now || new Date();
    return cards.filter(card => {
      if (card.suspended) return false;
      if (card.buriedUntil) {
        const buriedUntil = new Date(card.buriedUntil);
        if (!isNaN(buriedUntil.getTime()) && buriedUntil > now) return false;
      }
      return stats?.isDue ? stats.isDue(card.srs, now) : true;
    });
  }

  function getStatistics(cards = []) {
    return manager()?.getSRSStatistics?.(cards) || {
      totalCards: cards.length,
      newCards: cards.length,
      dueCards: cards.length,
      learningCards: 0,
      reviewCards: 0,
      relearningCards: 0,
      masteredCards: 0
    };
  }

  return {
    normalizeSettings,
    getRatingPreviews,
    reviewCard,
    getDueCards,
    getStatistics
  };
});
