(function () {
  async function runStoreAction(action, successMessage) {
    if (!window.flashcardStore) return;

    try {
      const result = await action();
      if (result?.canceled) return;
      if (successMessage) {
        window.dispatchEvent(new CustomEvent('erudite-menu-toast', {
          detail: { message: successMessage(result), type: 'success' }
        }));
      }
    } catch (error) {
      console.error('Menu action failed:', error);
      window.dispatchEvent(new CustomEvent('erudite-menu-toast', {
        detail: { message: error.message || 'Menu action failed', type: 'error' }
      }));
    }
  }

  window.addEventListener('erudite-menu-command', async (event) => {
    const command = event.detail;

    switch (command) {
      case 'new-set':
        window.location.href = 'creator.html?new=true';
        break;
      case 'open-card-browser':
        window.location.href = 'card-browser.html';
        break;
      case 'open-diagnostics':
        window.location.href = 'diagnostics.html';
        break;
      case 'import-flashcards':
        if (!window.location.pathname.endsWith('flashcards.html')) {
          window.location.href = 'flashcards.html#import';
        }
        break;
      case 'export-backup':
        await runStoreAction(
          () => window.flashcardStore.exportBackup(),
          result => `Backup exported (${result.setCount || 0} sets)`
        );
        break;
      case 'restore-backup':
        if (window.confirm('Restore backup will replace the current local library. Continue?')) {
          await runStoreAction(
            () => window.flashcardStore.importBackup(),
            result => `Backup restored (${result.setCount || 0} sets)`
          );
          window.location.reload();
        }
        break;
      case 'export-csv':
        await runStoreAction(
          () => window.flashcardStore.exportDelimited('csv'),
          result => `CSV exported (${result.cardCount || 0} cards)`
        );
        break;
      case 'export-tsv':
        await runStoreAction(
          () => window.flashcardStore.exportDelimited('tsv'),
          result => `TSV exported (${result.cardCount || 0} cards)`
        );
        break;
      case 'import-delimited':
        await runStoreAction(
          () => window.flashcardStore.importDelimited(),
          result => `Imported ${result.cardCount || 0} cards`
        );
        window.location.reload();
        break;
      case 'toggle-srs': {
        const current = window.flashcardStore?.getState
          ? await window.flashcardStore.getState('srsModeEnabled')
          : localStorage.getItem('srsModeEnabled');
        const next = !(current === true || current === 'true');
        if (window.setSRSMode) {
          await window.setSRSMode(next);
        } else if (window.flashcardStore?.setState) {
          await window.flashcardStore.setState('srsModeEnabled', next);
        } else {
          localStorage.setItem('srsModeEnabled', String(next));
        }
        break;
      }
      case 'review-due':
        if (!window.location.pathname.endsWith('flashcards.html')) {
          window.location.href = 'flashcards.html#review-due';
        }
        break;
      default:
        break;
    }
  });
})();
