(function (root, factory) {
  const api = factory(root.EruditeCore?.stats);
  root.EruditeCore = root.EruditeCore || {};
  root.EruditeCore.reviewSession = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
})(typeof globalThis !== 'undefined' ? globalThis : window, function (stats) {
  function createProgress(setId, cardCount = 0) {
    return {
      setId,
      currentIndex: 0,
      studiedCards: [],
      completed: false,
      cardCount,
      updatedAt: Date.now()
    };
  }

  function normalizeProgress(progress, setId, cardCount = 0) {
    if (!progress || typeof progress !== 'object' || String(progress.setId || '') !== String(setId || '')) {
      return createProgress(setId, cardCount);
    }

    const maxIndex = Math.max(0, cardCount - 1);
    return {
      ...progress,
      setId,
      currentIndex: Math.min(maxIndex, Math.max(0, Number(progress.currentIndex) || 0)),
      studiedCards: Array.isArray(progress.studiedCards) ? progress.studiedCards : [],
      completed: Boolean(progress.completed),
      cardCount,
      updatedAt: progress.updatedAt || Date.now()
    };
  }

  function shouldShowNormalCompletion(currentIndex, direction, cardCount) {
    return direction === 'next' && cardCount > 0 && currentIndex >= cardCount - 1;
  }

  function getDueCardsFromSets(sets = [], options = {}) {
    const now = options.now || new Date();
    const srsManager = options.srsManager;
    const result = [];

    for (const set of sets || []) {
      if (set?.srsSettings?.enabled === false) continue;
      const cards = srsManager?.getDueCards
        ? srsManager.getDueCards(set.cards || [], { settings: set.srsSettings || {} })
        : (set.cards || []).filter(card => !card.suspended && stats?.isDue(card.srs, now));
      for (const card of cards) {
        result.push({ set, card });
      }
    }

    return result;
  }

  function findNextDueSetId(sets = [], currentSetId, options = {}) {
    const due = getDueCardsFromSets(sets, options);
    const next = due.find(item => String(item.set.id) !== String(currentSetId));
    return next?.set?.id || null;
  }

  return {
    createProgress,
    normalizeProgress,
    shouldShowNormalCompletion,
    getDueCardsFromSets,
    findNextDueSetId
  };
});
