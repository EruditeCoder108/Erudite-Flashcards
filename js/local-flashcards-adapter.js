(function () {
  const store = window.flashcardStore;

  if (!store) {
    console.warn('Local flashcard store was not loaded.');
    return;
  }

  const localUser = {
    uid: 'local-user',
    displayName: 'Local User',
    email: 'local@erudite'
  };

  window.auth = {
    onAuthStateChanged(callback) {
      setTimeout(() => callback(localUser), 0);
      return () => {};
    },
    currentUser: localUser
  };

  class LocalFlashcardsManager {
    constructor() {
      this.user = localUser;
      this.authInitialized = true;
    }

    isAuthenticated() {
      return true;
    }

    isAuthInitialized() {
      return true;
    }

    async saveFlashcardSet(flashcardSet) {
      await store.saveSet(flashcardSet);
      return true;
    }

    async loadFlashcardSets() {
      return store.listSets();
    }

    async loadFlashcardSet(setId) {
      const set = await store.getSet(setId);
      if (!set) throw new Error('Flashcard set not found');
      return set;
    }

    async deleteFlashcardSet(setId) {
      await store.deleteSet(setId);
      return true;
    }

    async updateFlashcardSet(setId, updates) {
      const set = await store.getSet(setId);
      if (!set) throw new Error('Flashcard set not found');
      await store.saveSet({
        ...set,
        ...updates,
        lastModified: Date.now()
      });
      return true;
    }

    async saveStudyProgress(setId, cardIndex, totalCards, normalModeIndex, srsModeIndex) {
      await store.saveProgress(setId, {
        setId,
        cardIndex,
        totalCards,
        normalModeIndex: normalModeIndex !== undefined ? normalModeIndex : cardIndex,
        srsModeIndex: srsModeIndex !== undefined ? srsModeIndex : cardIndex,
        lastStudied: Date.now(),
        completionPercentage: totalCards ? Math.round(((cardIndex + 1) / totalCards) * 100) : 0
      });
      return true;
    }

    async loadStudyProgress(setId) {
      return store.getProgress(setId);
    }

    async uploadFlashcardImage(file, setId, cardId, imageType) {
      const downloadURL = await store.saveImageFromFile(file, {
        prefix: `flashcard-${setId || 'new'}-${cardId || 'card'}-${imageType || 'image'}`
      });
      return {
        filename: file.name,
        downloadURL,
        path: downloadURL,
        size: file.size,
        type: file.type,
        uploadedAt: Date.now()
      };
    }

    async deleteFlashcardImage(imagePath) {
      await store.deleteImage(imagePath);
      return true;
    }

    async migrateLocalFlashcardSets() {
      return true;
    }

    hasMigrationCompleted() {
      return true;
    }

    async cleanupOrphanedStudyProgress() {
      return true;
    }
  }

  window.firebaseFlashcardsManager = new LocalFlashcardsManager();
})();
