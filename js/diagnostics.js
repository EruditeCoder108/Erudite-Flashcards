(function () {
  const generatedAt = document.getElementById('generated-at');
  const healthBanner = document.getElementById('health-banner');
  const refreshBtn = document.getElementById('refresh-btn');
  const backBtn = document.getElementById('back-btn');
  const setCount = document.getElementById('set-count');
  const cardCount = document.getElementById('card-count');
  const classCount = document.getElementById('class-count');
  const backupCount = document.getElementById('backup-count');
  const storageDetails = document.getElementById('storage-details');
  const integrityDetails = document.getElementById('integrity-details');
  const pathList = document.getElementById('path-list');
  const brokenImages = document.getElementById('broken-images');
  const backupList = document.getElementById('backup-list');

  function formatBytes(bytes = 0) {
    const value = Number(bytes || 0);
    if (value < 1024) return `${value} B`;
    if (value < 1024 * 1024) return `${(value / 1024).toFixed(1)} KB`;
    return `${(value / (1024 * 1024)).toFixed(1)} MB`;
  }

  function formatDate(value) {
    if (!value) return 'Unknown';
    const date = new Date(value);
    return Number.isNaN(date.getTime()) ? 'Unknown' : date.toLocaleString();
  }

  function escapeHtml(value) {
    const div = document.createElement('div');
    div.textContent = String(value ?? '');
    return div.innerHTML;
  }

  function setDetails(container, rows) {
    container.innerHTML = rows.map(([label, value]) => `
      <dt>${escapeHtml(label)}</dt>
      <dd>${escapeHtml(value)}</dd>
    `).join('');
  }

  function setHealth(status, issues = []) {
    healthBanner.className = `health-banner ${status === 'ok' ? 'ok' : 'warning'}`;
    if (status === 'ok') {
      healthBanner.innerHTML = `
        <i class="fas fa-circle-check"></i>
        <div>
          <strong>Storage looks healthy</strong>
          <span>No database or managed-image issues were found.</span>
        </div>
      `;
      return;
    }

    healthBanner.innerHTML = `
      <i class="fas fa-triangle-exclamation"></i>
      <div>
        <strong>Diagnostics found something to review</strong>
        <span>${escapeHtml(issues.join(' ') || 'Review the integrity section below.')}</span>
      </div>
    `;
  }

  function renderPaths(paths = {}) {
    const labels = {
      userData: 'User Data',
      dataDir: 'Data',
      database: 'Database',
      imagesDir: 'Images',
      fontsDir: 'Fonts',
      backupsDir: 'Backups'
    };

    pathList.innerHTML = Object.entries(labels).map(([key, label]) => {
      const value = paths[key] || '';
      return `
        <div class="path-row">
          <strong>${escapeHtml(label)}</strong>
          <code title="${escapeHtml(value)}">${escapeHtml(value || 'Unavailable')}</code>
          <button class="copy-btn" type="button" data-copy="${escapeHtml(value)}">
            <i class="fas fa-copy"></i>
          </button>
        </div>
      `;
    }).join('');
  }

  function renderBrokenImages(items = []) {
    if (!items.length) {
      brokenImages.innerHTML = '<p class="empty-note">No broken managed image links found.</p>';
      return;
    }

    brokenImages.innerHTML = `
      <table>
        <thead>
          <tr>
            <th>Set</th>
            <th>Card</th>
            <th>Side</th>
            <th>Missing Path</th>
          </tr>
        </thead>
        <tbody>
          ${items.map(item => `
            <tr>
              <td>${escapeHtml(item.setName || item.setId)}</td>
              <td>${escapeHtml(item.cardId || 'Unknown')}</td>
              <td>${escapeHtml(item.side)}</td>
              <td>${escapeHtml(item.path)}</td>
            </tr>
          `).join('')}
        </tbody>
      </table>
    `;
  }

  function renderBackups(items = []) {
    backupCount.textContent = String(items.length);
    if (!items.length) {
      backupList.innerHTML = '<p class="empty-note">No backup snapshots found yet.</p>';
      return;
    }

    backupList.innerHTML = `
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Modified</th>
            <th>Size</th>
            <th>Path</th>
          </tr>
        </thead>
        <tbody>
          ${items.map(item => `
            <tr>
              <td>${escapeHtml(item.name)}</td>
              <td>${escapeHtml(formatDate(item.modifiedAt))}</td>
              <td>${escapeHtml(formatBytes(item.sizeBytes))}</td>
              <td>${escapeHtml(item.path)}</td>
            </tr>
          `).join('')}
        </tbody>
      </table>
    `;
  }

  function renderDiagnostics(data) {
    const counts = data.counts || {};
    setCount.textContent = String(counts.sets || 0);
    cardCount.textContent = String(counts.cards || 0);
    classCount.textContent = String(counts.classes || 0);
    generatedAt.textContent = `Generated ${formatDate(data.generatedAt)}`;

    setHealth(data.health?.status || 'warning', data.health?.issues || []);
    setDetails(storageDetails, [
      ['App version', data.appVersion || 'Unknown'],
      ['Storage engine', data.storageEngine || 'Unknown'],
      ['Schema version', data.schemaVersion || 'Unknown'],
      ['Database exists', data.database?.exists ? 'Yes' : 'No'],
      ['Database size', formatBytes(data.database?.sizeBytes || 0)],
      ['Database modified', formatDate(data.database?.modifiedAt)]
    ]);
    setDetails(integrityDetails, [
      ['Visible sets', counts.sets || 0],
      ['Visible cards', counts.cards || 0],
      ['Deleted sets', counts.deletedSets || 0],
      ['Cards in deleted sets', counts.cardsInDeletedSets || 0],
      ['Orphaned cards', counts.orphanedCards || 0],
      ['Progress entries', counts.progressEntries ?? counts.progressRows ?? 0],
      ['State entries', counts.stateEntries ?? counts.stateRows ?? 0],
      ['Managed image links', data.imageHealth?.managedImageLinks || 0],
      ['Broken image links', data.imageHealth?.brokenCount || 0]
    ]);

    renderPaths(data.paths || {});
    renderBrokenImages(data.brokenImageLinks || []);
    renderBackups(data.recentBackups || []);
  }

  async function loadDiagnostics() {
    healthBanner.className = 'health-banner loading';
    healthBanner.innerHTML = `
      <i class="fas fa-circle-notch fa-spin"></i>
      <div>
        <strong>Checking storage...</strong>
        <span>Please wait.</span>
      </div>
    `;

    try {
      const diagnostics = await window.flashcardStore.getDiagnostics();
      renderDiagnostics(diagnostics);
    } catch (error) {
      console.error('Could not load diagnostics:', error);
      setHealth('warning', [error.message || 'Could not load diagnostics.']);
    }
  }

  refreshBtn?.addEventListener('click', loadDiagnostics);
  backBtn?.addEventListener('click', () => {
    window.location.href = 'flashcards.html';
  });
  pathList?.addEventListener('click', async (event) => {
    const button = event.target.closest('.copy-btn');
    if (!button || !button.dataset.copy) return;

    try {
      await navigator.clipboard.writeText(button.dataset.copy);
      button.innerHTML = '<i class="fas fa-check"></i>';
      setTimeout(() => {
        button.innerHTML = '<i class="fas fa-copy"></i>';
      }, 1200);
    } catch (_error) {
      button.textContent = 'Copy failed';
      setTimeout(() => {
        button.innerHTML = '<i class="fas fa-copy"></i>';
      }, 1200);
    }
  });

  document.addEventListener('DOMContentLoaded', async () => {
    if (window.flashcardLocalReady) await window.flashcardLocalReady;
    if (window.loadAndApplySettings) await window.loadAndApplySettings();
    loadDiagnostics();
  });
})();
