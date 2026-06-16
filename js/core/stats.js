(function (root, factory) {
  const api = factory();
  root.EruditeCore = root.EruditeCore || {};
  root.EruditeCore.stats = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
})(typeof globalThis !== 'undefined' ? globalThis : window, function () {
  function isDue(srsData, now = new Date(), rolloverHour = 4) {
    if (!srsData || !srsData.due) return true;
    const dueDate = new Date(srsData.due);
    if (isNaN(dueDate.getTime())) return true;
    const state = srsData.state || 'New';
    if (state === 'Learning' || state === 'Relearning') {
      return dueDate <= now;
    }
    
    // For mature Review cards, check SRS day boundaries
    const d = new Date(dueDate);
    const adjustedDue = new Date(d.getTime() - rolloverHour * 60 * 60 * 1000);
    const dueY = adjustedDue.getFullYear();
    const dueM = String(adjustedDue.getMonth() + 1).padStart(2, '0');
    const dueD = String(adjustedDue.getDate()).padStart(2, '0');
    const dueStr = `${dueY}-${dueM}-${dueD}`;

    const n = new Date(now);
    const adjustedNow = new Date(n.getTime() - rolloverHour * 60 * 60 * 1000);
    const nowY = adjustedNow.getFullYear();
    const nowM = String(adjustedNow.getMonth() + 1).padStart(2, '0');
    const nowD = String(adjustedNow.getDate()).padStart(2, '0');
    const nowStr = `${nowY}-${nowM}-${nowD}`;

    return dueStr <= nowStr;
  }

  function getCardState(card) {
    if (!card?.srs) return 'New';
    return card.srs.state || 'New';
  }

  function getSetSrsStats(set = {}, now = new Date()) {
    const stats = {
      totalCards: set.cards ? set.cards.length : 0,
      activeCards: 0,
      newCards: 0,
      dueCards: 0,
      learningCards: 0,
      reviewCards: 0,
      relearningCards: 0,
      matureCards: 0,
      suspendedCards: 0,
      buriedCards: 0,
      nextDue: null,
      retention: null
    };

    const history = [];
    for (const card of set.cards || []) {
      if (card.suspended) {
        stats.suspendedCards += 1;
        continue;
      }
      if (card.buriedUntil) {
        const buriedUntil = new Date(card.buriedUntil);
        if (!isNaN(buriedUntil.getTime()) && buriedUntil > now) {
          stats.buriedCards += 1;
          continue;
        }
      }
      stats.activeCards += 1;
      const state = getCardState(card);
      if (Array.isArray(card.reviewHistory)) history.push(...card.reviewHistory);

      if (!card.srs || state === 'New') {
        stats.newCards += 1;
        stats.dueCards += 1;
        continue;
      }

      if (state === 'Learning') stats.learningCards += 1;
      if (state === 'Review') stats.reviewCards += 1;
      if (state === 'Relearning') stats.relearningCards += 1;

      if (isDue(card.srs, now)) {
        stats.dueCards += 1;
      } else if (state === 'Review') {
        stats.matureCards += 1;
      }

      if (card.srs?.due) {
        const dueDate = new Date(card.srs.due);
        if (!isNaN(dueDate.getTime()) && (!stats.nextDue || dueDate < stats.nextDue)) {
          stats.nextDue = dueDate;
        }
      }
    }

    const thirtyDaysAgo = now.getTime() - 30 * 24 * 60 * 60 * 1000;
    const recentReviews = history.filter(review => {
      const reviewedAt = new Date(review.reviewedAt || review.time || review.date || 0);
      return !isNaN(reviewedAt.getTime()) && reviewedAt.getTime() >= thirtyDaysAgo;
    });
    if (recentReviews.length > 0) {
      const remembered = recentReviews.filter(review => review.rating !== 'Again').length;
      stats.retention = Math.round((remembered / recentReviews.length) * 100);
    }

    return stats;
  }

  function getLibraryStats(sets = [], classes = [], now = new Date()) {
    const totals = {
      setCount: Array.isArray(sets) ? sets.length : 0,
      classCount: Array.isArray(classes) ? classes.length : 0,
      cardCount: 0,
      dueCards: 0,
      newCards: 0,
      learningCards: 0,
      reviewCards: 0,
      matureCards: 0,
      retention: null,
      nextDue: null
    };

    const retentionValues = [];
    for (const set of sets || []) {
      const setStats = getSetSrsStats(set, now);
      totals.cardCount += setStats.totalCards;
      totals.dueCards += setStats.dueCards;
      totals.newCards += setStats.newCards;
      totals.learningCards += setStats.learningCards;
      totals.reviewCards += setStats.reviewCards;
      totals.matureCards += setStats.matureCards;
      if (setStats.retention !== null) retentionValues.push(setStats.retention);
      if (setStats.nextDue && (!totals.nextDue || setStats.nextDue < totals.nextDue)) {
        totals.nextDue = setStats.nextDue;
      }
    }

    if (retentionValues.length > 0) {
      totals.retention = Math.round(retentionValues.reduce((sum, value) => sum + value, 0) / retentionValues.length);
    }

    return totals;
  }

  return {
    isDue,
    getCardState,
    getSetSrsStats,
    getLibraryStats
  };
});
