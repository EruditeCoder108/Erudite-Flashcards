(function (root, factory) {
  const api = factory();
  root.EruditeCore = root.EruditeCore || {};
  root.EruditeCore.draft = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
})(typeof globalThis !== 'undefined' ? globalThis : window, function () {
  function hasMeaningfulDraft(draft) {
    if (!draft || typeof draft !== 'object') return false;
    if (String(draft.name || '').trim()) return true;
    if (draft.classId) return true;
    return Array.isArray(draft.cards) && draft.cards.some(card => (
      String(card.term || '').trim() ||
      String(card.definition || '').trim() ||
      card.termImage ||
      card.definitionImage
    ));
  }

  function isDraftSameAsSavedSet(draft, savedSet) {
    if (!draft || !savedSet) return false;
    const comparableDraft = {
      name: draft.name || '',
      classId: draft.classId || null,
      cards: (draft.cards || []).map(card => ({
        term: card.term || '',
        definition: card.definition || '',
        termImage: card.termImage || '',
        definitionImage: card.definitionImage || ''
      }))
    };
    const comparableSaved = {
      name: savedSet.name || '',
      classId: savedSet.classId || null,
      cards: (savedSet.cards || []).map(card => ({
        term: card.term || '',
        definition: card.definition || '',
        termImage: card.termImage || '',
        definitionImage: card.definitionImage || ''
      }))
    };
    return JSON.stringify(comparableDraft) === JSON.stringify(comparableSaved);
  }

  function markDraftSaved(draft, savedSet) {
    return {
      ...(draft || {}),
      savedSetId: savedSet?.id || draft?.savedSetId || null,
      savedAt: Date.now()
    };
  }

  return {
    hasMeaningfulDraft,
    isDraftSameAsSavedSet,
    markDraftSaved
  };
});
