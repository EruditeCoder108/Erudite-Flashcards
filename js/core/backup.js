(function (root, factory) {
  const api = factory(root.EruditeCore?.schema);
  root.EruditeCore = root.EruditeCore || {};
  root.EruditeCore.backup = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
})(typeof globalThis !== 'undefined' ? globalThis : window, function (schema) {
  function isPlainObject(value) {
    return value !== null && typeof value === 'object' && !Array.isArray(value);
  }

  function readBackupData(payload) {
    const data = Array.isArray(payload) ? { sets: payload } : (payload?.data || payload || {});
    if (!Array.isArray(data.sets)) {
      throw new Error('Backup file does not contain a flashcard set list.');
    }

    const normalized = schema?.normalizeCollection
      ? schema.normalizeCollection(data.sets, Array.isArray(data.classes) ? data.classes : [])
      : { sets: data.sets, classes: Array.isArray(data.classes) ? data.classes : [] };

    return {
      sets: normalized.sets,
      classes: normalized.classes,
      settings: isPlainObject(data.settings) ? data.settings : {},
      progress: isPlainObject(data.progress) ? data.progress : {},
      state: isPlainObject(data.state) ? data.state : {}
    };
  }

  function createBackupPayload(input = {}) {
    const normalized = schema?.normalizeCollection
      ? schema.normalizeCollection(input.sets || [], input.classes || [])
      : { sets: input.sets || [], classes: input.classes || [] };

    return {
      app: 'Erudite Flashcards',
      schemaVersion: 1,
      exportedAt: new Date().toISOString(),
      data: {
        sets: normalized.sets,
        classes: normalized.classes,
        settings: isPlainObject(input.settings) ? input.settings : {},
        progress: isPlainObject(input.progress) ? input.progress : {},
        state: isPlainObject(input.state) ? input.state : {}
      }
    };
  }

  function validateBackupPayload(payload) {
    const data = readBackupData(payload);
    return {
      ok: true,
      setCount: data.sets.length,
      classCount: data.classes.length,
      cardCount: data.sets.reduce((total, set) => total + (Array.isArray(set.cards) ? set.cards.length : 0), 0)
    };
  }

  return {
    isPlainObject,
    readBackupData,
    createBackupPayload,
    validateBackupPayload
  };
});
