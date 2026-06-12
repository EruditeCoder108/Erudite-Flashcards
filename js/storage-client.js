(function () {
  const api = window.eruditeFlashcards || window.eruditeMobileFlashcards;
  const mirroredStateKeys = new Set([
    'flashcardSetDraft',
    'currentStudyProgress',
    'srsModeEnabled',
    'customCursorEnabled',
    'cursorStyle'
  ]);
  const legacyDurableKeys = [
    'flashcardSets',
    'flashcardClasses',
    'flashcardSetDraft',
    'currentStudyProgress',
    'srsModeEnabled',
    'studyProgress'
  ];
  let isHydrating = false;

  function readLocal(key, fallback) {
    try {
      const raw = localStorage.getItem(key);
      return raw ? JSON.parse(raw) : fallback;
    } catch (error) {
      return fallback;
    }
  }

  function writeLocal(key, value) {
    localStorage.setItem(key, JSON.stringify(value));
    return value;
  }

  function readFileAsDataUrl(file) {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = () => resolve(reader.result);
      reader.onerror = () => reject(reader.error);
      reader.readAsDataURL(file);
    });
  }

  async function listSets() {
    if (api) return api.listSets();
    return readLocal('flashcardSets', []);
  }

  async function listSetsMeta() {
    if (api?.listSetsMeta) return api.listSetsMeta();
    return listSets(); // fallback: load full sets
  }

  async function getSet(id) {
    if (api) return api.getSet(id);
    const sets = await listSets();
    return sets.find((set) => String(set.id) === String(id)) || null;
  }

  async function saveSet(set) {
    if (api) return api.saveSet(set);
    const sets = await listSets();
    const existing = sets.find((item) => String(item.id) === String(set.id));
    const next = {
      ...set,
      id: set.id || Date.now(),
      created: set.created || existing?.created || Date.now(),
      openedCount: set.openedCount ?? existing?.openedCount ?? 0,
      lastOpened: set.lastOpened ?? existing?.lastOpened ?? null,
      lastModified: Date.now()
    };
    const updated = sets.filter((item) => String(item.id) !== String(next.id));
    updated.push(next);
    writeLocal('flashcardSets', updated);
    return next;
  }

  async function replaceSets(sets) {
    if (api) return api.replaceSets(sets);
    writeLocal('flashcardSets', Array.isArray(sets) ? sets : []);
    return Array.isArray(sets) ? sets : [];
  }

  async function deleteSet(id) {
    if (api) return api.deleteSet(id);
    const sets = await listSets();
    writeLocal('flashcardSets', sets.filter((set) => String(set.id) !== String(id)));
    return true;
  }

  async function listClasses() {
    if (api) return api.listClasses();
    return readLocal('flashcardClasses', []);
  }

  async function saveClass(classData) {
    if (api) return api.saveClass(classData);
    const classes = await listClasses();
    const now = Date.now();
    const next = {
      ...classData,
      id: classData.id || `class-${now}`,
      name: String(classData.name || 'Untitled Class').trim() || 'Untitled Class',
      color: /^#[0-9a-f]{6}$/i.test(String(classData.color || '')) ? classData.color : '#3B82F6',
      created: classData.created || now,
      lastModified: now
    };
    const updated = classes.filter((item) => String(item.id) !== String(next.id));
    updated.push(next);
    writeLocal('flashcardClasses', updated);
    return next;
  }

  async function deleteClass(classId) {
    if (api) return api.deleteClass(classId);
    const classes = await listClasses();
    writeLocal('flashcardClasses', classes.filter((item) => String(item.id) !== String(classId)));
    const sets = await listSets();
    writeLocal('flashcardSets', sets.map((set) => (
      String(set.classId || '') === String(classId) ? { ...set, classId: null, lastModified: Date.now() } : set
    )));
    return true;
  }

  async function getProgress(setId) {
    if (api) return api.getProgress(setId);
    const progress = readLocal('studyProgress', {});
    return progress[String(setId)] || null;
  }

  async function saveProgress(setId, value) {
    if (api) return api.saveProgress(setId, value);
    const progress = readLocal('studyProgress', {});
    progress[String(setId)] = value;
    writeLocal('studyProgress', progress);
    return true;
  }

  async function saveCardProgress(setId, cardId, patch) {
    if (api?.saveCardProgress) return api.saveCardProgress(setId, cardId, patch);
    return false;
  }

  async function getSettings() {
    if (api) return api.getSettings();
    return readLocal('flashcards-settings', {});
  }

  async function saveSettings(settings) {
    if (api) return api.saveSettings(settings);
    writeLocal('flashcards-settings', settings || {});
    return true;
  }

  async function mirrorLocalStorageWrite(key, value) {
    if (isHydrating || window.__eruditeApplyingSettings || !api) return;

    try {
      if (key === 'flashcardSets' || key === 'flashcardClasses') {
        return;
      } else if (key === 'flashcards-settings') {
        const current = await getSettings();
        await saveSettings({ ...current, ...(JSON.parse(value || '{}')) });
      } else if (key === 'flashcards-theme') {
        const current = await getSettings();
        await saveSettings({ ...current, theme: value || 'dark' });
      } else if (mirroredStateKeys.has(key)) {
        const parsedValue = key === 'srsModeEnabled'
          ? value === 'true'
          : (() => {
              try { return JSON.parse(value); } catch (_error) { return value; }
            })();
        await setState(key, parsedValue);

        if (key === 'currentStudyProgress' && parsedValue && parsedValue.setId !== undefined) {
          await saveProgress(parsedValue.setId, parsedValue);
        }
      }
    } catch (error) {
      console.warn(`Could not mirror localStorage key "${key}" to local store:`, error);
    }
  }

  async function mirrorLocalStorageRemove(key) {
    if (isHydrating || !api) return;
    if (mirroredStateKeys.has(key)) {
      await removeState(key);
    }
  }

  function installLocalStorageMirror() {
    if (window.__eruditeLocalStorageMirrorInstalled) return;
    window.__eruditeLocalStorageMirrorInstalled = true;

    const originalSetItem = localStorage.setItem.bind(localStorage);
    const originalRemoveItem = localStorage.removeItem.bind(localStorage);

    localStorage.setItem = (key, value) => {
      originalSetItem(key, value);
      mirrorLocalStorageWrite(key, value);
    };

    localStorage.removeItem = (key) => {
      originalRemoveItem(key);
      mirrorLocalStorageRemove(key);
    };
  }

  async function migrateLegacyBrowserStorage() {
    if (!api) return;

    try {
      const localSets = readLocal('flashcardSets', null);
      const storedSets = await listSets();
      if (Array.isArray(localSets) && localSets.length > 0 && (!Array.isArray(storedSets) || storedSets.length === 0)) {
        await replaceSets(localSets);
      }

      const localClasses = readLocal('flashcardClasses', null);
      const storedClasses = await listClasses();
      if (Array.isArray(localClasses) && localClasses.length > 0 && (!Array.isArray(storedClasses) || storedClasses.length === 0)) {
        for (const classData of localClasses) {
          await saveClass(classData);
        }
      }

      const localSettings = readLocal('flashcards-settings', null);
      const storedSettings = await getSettings();
      if (localSettings && typeof localSettings === 'object' && (!storedSettings || Object.keys(storedSettings).length === 0)) {
        await saveSettings(localSettings);
      }

      for (const key of mirroredStateKeys) {
        const currentValue = await getState(key);
        const localRaw = localStorage.getItem(key);
        if ((currentValue === null || currentValue === undefined) && localRaw !== null) {
          const parsedValue = key === 'srsModeEnabled'
            ? localRaw === 'true'
            : (() => {
                try { return JSON.parse(localRaw); } catch (_error) { return localRaw; }
              })();
          await setState(key, parsedValue);

          if (key === 'currentStudyProgress' && parsedValue && parsedValue.setId !== undefined) {
            await saveProgress(parsedValue.setId, parsedValue);
          }
        }
      }
    } catch (error) {
      console.warn('Could not migrate legacy browser flashcard storage:', error);
    }
  }

  function clearLegacyBrowserStorage() {
    if (!api) return;
    legacyDurableKeys.forEach(key => localStorage.removeItem(key));
  }

  async function hydrateLocalStorage() {
    installLocalStorageMirror();
    isHydrating = true;

    try {
      await migrateLegacyBrowserStorage();

      if (api) {
        const settings = await getSettings();
        if (settings && typeof settings === 'object') {
          localStorage.setItem('flashcards-settings', JSON.stringify(settings));
          if (settings.theme) {
            localStorage.setItem('flashcards-theme', settings.theme);
          }
        }
        clearLegacyBrowserStorage();
        return;
      }

      const [sets, settings, srsMode, draft, progress, cursorEnabled, cursorStyle] = await Promise.all([
        listSets(),
        getSettings(),
        getState('srsModeEnabled'),
        getState('flashcardSetDraft'),
        getState('currentStudyProgress'),
        getState('customCursorEnabled'),
        getState('cursorStyle')
      ]);

      if (Array.isArray(sets)) {
        localStorage.setItem('flashcardSets', JSON.stringify(sets));
      }

      const classes = await listClasses();
      if (Array.isArray(classes)) {
        localStorage.setItem('flashcardClasses', JSON.stringify(classes));
      }

      if (settings && typeof settings === 'object') {
        localStorage.setItem('flashcards-settings', JSON.stringify(settings));
        if (settings.theme) {
          localStorage.setItem('flashcards-theme', settings.theme);
        }
      }

      if (srsMode !== null && srsMode !== undefined) {
        localStorage.setItem('srsModeEnabled', String(Boolean(srsMode)));
      }
      if (draft) {
        localStorage.setItem('flashcardSetDraft', JSON.stringify(draft));
      }
      if (progress) {
        localStorage.setItem('currentStudyProgress', JSON.stringify(progress));
      }
      if (cursorEnabled !== null && cursorEnabled !== undefined) {
        localStorage.setItem('customCursorEnabled', String(Boolean(cursorEnabled)));
      }
      if (cursorStyle) {
        localStorage.setItem('cursorStyle', cursorStyle);
      }
    } catch (error) {
      console.warn('Could not hydrate local flashcard state:', error);
    } finally {
      isHydrating = false;
    }
  }

  async function getState(key) {
    if (api) return api.getState(key);
    return readLocal(`erudite-state-${key}`, null);
  }

  async function setState(key, value) {
    if (api) return api.setState(key, value);
    writeLocal(`erudite-state-${key}`, value);
    return true;
  }

  async function removeState(key) {
    if (api) return api.removeState(key);
    localStorage.removeItem(`erudite-state-${key}`);
    return true;
  }

  async function saveImageFromFile(file, meta = {}) {
    const dataUrl = await readFileAsDataUrl(file);
    if (api) return api.saveImage(dataUrl, { ...meta, fileName: file.name });
    return dataUrl;
  }

  async function saveImageDataUrl(dataUrl, meta = {}) {
    if (api) return api.saveImage(dataUrl, meta);
    return dataUrl;
  }

  async function deleteImage(fileUrl) {
    if (api?.deleteImage) return api.deleteImage(fileUrl);
    return true;
  }

  async function saveFontFromFile(file) {
    const dataUrl = await readFileAsDataUrl(file);
    if (api) return api.saveFont(dataUrl, { fileName: file.name, prefix: 'content-font' });
    return dataUrl;
  }

  async function listPremadeSets(classId, subjectId) {
    if (api) return api.listPremadeSets(classId, subjectId);
    return [];
  }

  async function getPremadeSet(classId, subjectId, fileName) {
    if (api) return api.getPremadeSet(classId, subjectId, fileName);
    try {
      const response = await fetch(`premade-cards/${classId}/${subjectId}/${fileName}`);
      return response.ok ? response.json() : null;
    } catch (error) {
      return null;
    }
  }

  async function getDiagnostics() {
    if (api?.getDiagnostics) return api.getDiagnostics();

    const sets = await listSets();
    const classes = await listClasses();
    const settings = await getSettings();
    return {
      appVersion: 'web-preview',
      storageEngine: 'browser-localStorage',
      generatedAt: new Date().toISOString(),
      paths: {},
      counts: {
        sets: Array.isArray(sets) ? sets.length : 0,
        classes: Array.isArray(classes) ? classes.length : 0,
        cards: Array.isArray(sets)
          ? sets.reduce((total, set) => total + (Array.isArray(set.cards) ? set.cards.length : 0), 0)
          : 0
      },
      settings,
      health: {
        status: 'warning',
        issues: ['Browser preview storage is not the production SQLite store.']
      },
      recentBackups: [],
      brokenImageLinks: []
    };
  }

  async function exportBackup() {
    if (api?.exportBackup) return api.exportBackup();

    const sets = await listSets();
    const classes = await listClasses();
    const settings = await getSettings();
    const payload = {
      app: 'Erudite Flashcards',
      schemaVersion: 1,
      exportedAt: new Date().toISOString(),
      data: {
        sets,
        classes,
        settings,
        progress: readLocal('studyProgress', {}),
        state: {}
      }
    };
    const blob = new Blob([JSON.stringify(payload, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `erudite-flashcards-backup-${new Date().toISOString().slice(0, 10)}.json`;
    link.click();
    URL.revokeObjectURL(url);

    return {
      canceled: false,
      setCount: sets.length
    };
  }

  async function importBackup() {
    if (api?.importBackup) return api.importBackup();
    return {
      canceled: true,
      unsupported: true
    };
  }

  async function exportDelimited(format) {
    if (api?.exportDelimited) return api.exportDelimited(format);
    return {
      canceled: true,
      unsupported: true
    };
  }

  async function importDelimited() {
    if (api?.importDelimited) return api.importDelimited();
    return {
      canceled: true,
      unsupported: true
    };
  }

  window.flashcardStore = {
    listSets,
    listSetsMeta,
    getSet,
    saveSet,
    replaceSets,
    deleteSet,
    listClasses,
    saveClass,
    deleteClass,
    getProgress,
    saveProgress,
    saveCardProgress,
    getSettings,
    saveSettings,
    getState,
    setState,
    removeState,
    saveImageFromFile,
    saveImageDataUrl,
    deleteImage,
    saveFontFromFile,
    listPremadeSets,
    getPremadeSet,
    getDiagnostics,
    exportBackup,
    importBackup,
    exportDelimited,
    importDelimited
  };

  window.flashcardMenuReady = api?.onMenuCommand
    ? api.onMenuCommand(command => {
        window.dispatchEvent(new CustomEvent('erudite-menu-command', { detail: command }));
      })
    : null;

  window.flashcardLocalReady = hydrateLocalStorage();
})();
