const { app, BrowserWindow, ipcMain, protocol, session, dialog, Menu, screen } = require('electron');
const fs = require('fs/promises');
const path = require('path');
const { randomUUID } = require('crypto');
const { pathToFileURL, fileURLToPath } = require('url');
const initSqlJs = require('sql.js');
const { SqliteFlashcardStore } = require('./storage/sqlite-flashcard-store');

const isDev = !app.isPackaged;

let mainWindow;
let dataDir;
let imagesDir;
let fontsDir;
let backupsDir;
let windowStatePath;
let flashcardStoreDb;
const smokeTest = process.argv.includes('--smoke-test');

const DEFAULT_SRS_SETTINGS = {
  enabled: true,
  requestRetention: 0.9,
  maxIntervalDays: 36500,
  newCardsPerDay: null,
  reviewsPerDay: null
};

function getPaths() {
  dataDir = path.join(app.getPath('userData'), 'data');
  imagesDir = path.join(dataDir, 'images');
  fontsDir = path.join(dataDir, 'fonts');
  backupsDir = path.join(dataDir, 'backups');
  windowStatePath = path.join(dataDir, 'window-state.json');
  return { dataDir, imagesDir, fontsDir, backupsDir };
}

async function ensureDataDirs() {
  getPaths();
  await fs.mkdir(imagesDir, { recursive: true });
  await fs.mkdir(fontsDir, { recursive: true });
  await fs.mkdir(backupsDir, { recursive: true });
}

async function loadWindowState() {
  const fallback = {
    width: 1280,
    height: 840,
    maximized: false,
    fullScreen: false
  };

  try {
    const raw = await fs.readFile(windowStatePath, 'utf8');
    const saved = JSON.parse(raw);
    const width = Math.max(960, Math.min(3840, Math.round(Number(saved.width) || fallback.width)));
    const height = Math.max(640, Math.min(2160, Math.round(Number(saved.height) || fallback.height)));
    const x = Number.isFinite(Number(saved.x)) ? Math.round(Number(saved.x)) : undefined;
    const y = Number.isFinite(Number(saved.y)) ? Math.round(Number(saved.y)) : undefined;
    const display = x !== undefined && y !== undefined
      ? screen.getDisplayMatching({ x, y, width, height })
      : screen.getPrimaryDisplay();
    const area = display.workArea;
    const visibleEnough = x === undefined || y === undefined || (
      x < area.x + area.width - 120 &&
      y < area.y + area.height - 120 &&
      x + width > area.x + 120 &&
      y + height > area.y + 120
    );

    return {
      ...fallback,
      width,
      height,
      x: visibleEnough ? x : undefined,
      y: visibleEnough ? y : undefined,
      maximized: Boolean(saved.maximized),
      fullScreen: Boolean(saved.fullScreen)
    };
  } catch (_error) {
    return fallback;
  }
}

async function saveWindowState(window) {
  if (!window || window.isDestroyed() || !windowStatePath) return;

  try {
    const bounds = window.isMaximized() || window.isFullScreen()
      ? window.getNormalBounds()
      : window.getBounds();
    await fs.writeFile(windowStatePath, JSON.stringify({
      ...bounds,
      maximized: window.isMaximized(),
      fullScreen: window.isFullScreen(),
      savedAt: new Date().toISOString()
    }, null, 2));
  } catch (error) {
    console.warn('Could not save window state:', error);
  }
}

async function initializeFlashcardStore() {
  await ensureDataDirs();
  if (flashcardStoreDb) return flashcardStoreDb;

  const SQL = await initSqlJs({
    locateFile: (file) => path.join(__dirname, 'node_modules', 'sql.js', 'dist', file)
  });

  flashcardStoreDb = await new SqliteFlashcardStore({
    SQL,
    dataDir,
    backupsDir,
    normalizers: {
      generateId,
      normalizeSet,
      normalizeClass
    }
  }).init();

  return flashcardStoreDb;
}

function getFlashcardStore() {
  if (!flashcardStoreDb) {
    throw new Error('Flashcard store has not been initialized.');
  }
  return flashcardStoreDb;
}

function safeFileName(name, fallback = 'file') {
  const base = String(name || fallback)
    .replace(/[^a-z0-9._-]+/gi, '-')
    .replace(/^-+|-+$/g, '')
    .slice(0, 80);
  return base || fallback;
}

function extensionFromMime(mime, fallback = 'bin') {
  const map = {
    'image/jpeg': 'jpg',
    'image/png': 'png',
    'image/webp': 'webp',
    'image/gif': 'gif',
    'audio/mpeg': 'mp3',
    'audio/mp3': 'mp3',
    'audio/wav': 'wav',
    'audio/x-wav': 'wav',
    'audio/ogg': 'ogg',
    'audio/mp4': 'm4a',
    'audio/aac': 'aac',
    'video/mp4': 'mp4',
    'video/webm': 'webm',
    'video/quicktime': 'mov',
    'video/x-m4v': 'm4v',
    'font/ttf': 'ttf',
    'font/otf': 'otf',
    'font/woff': 'woff',
    'font/woff2': 'woff2',
    'application/x-font-ttf': 'ttf',
    'application/x-font-otf': 'otf',
    'application/font-woff': 'woff',
    'application/font-woff2': 'woff2'
  };
  return map[mime] || fallback;
}

function mimeFromExtension(filePath) {
  const ext = path.extname(filePath || '').toLowerCase();
  const map = {
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.png': 'image/png',
    '.webp': 'image/webp',
    '.gif': 'image/gif',
    '.mp3': 'audio/mpeg',
    '.wav': 'audio/wav',
    '.ogg': 'audio/ogg',
    '.m4a': 'audio/mp4',
    '.aac': 'audio/aac',
    '.mp4': 'video/mp4',
    '.webm': 'video/webm',
    '.mov': 'video/quicktime',
    '.m4v': 'video/x-m4v'
  };
  return map[ext] || 'application/octet-stream';
}

function parseDataUrl(dataUrl) {
  const match = /^data:([^;,]+);base64,(.+)$/i.exec(dataUrl || '');
  if (!match) return null;
  return {
    mime: match[1],
    buffer: Buffer.from(match[2], 'base64')
  };
}

function generateId(prefix) {
  return `${prefix}-${randomUUID()}`;
}

function numberOrNull(value, fallback = null) {
  if (value === null || value === undefined || value === '') return fallback;
  const number = Number(value);
  return Number.isFinite(number) ? number : fallback;
}

function normalizeSrsSettings(settings = {}) {
  const requestRetention = numberOrNull(settings.requestRetention, DEFAULT_SRS_SETTINGS.requestRetention);
  const maxIntervalDays = numberOrNull(settings.maxIntervalDays, DEFAULT_SRS_SETTINGS.maxIntervalDays);
  const dailyLimitOrNull = (value) => {
    const number = numberOrNull(value, null);
    return number === null ? null : Math.max(0, Math.round(number));
  };

  return {
    enabled: settings.enabled !== false,
    requestRetention: Math.min(0.99, Math.max(0.7, requestRetention)),
    maxIntervalDays: Math.max(1, Math.round(maxIntervalDays)),
    newCardsPerDay: dailyLimitOrNull(settings.newCardsPerDay),
    reviewsPerDay: dailyLimitOrNull(settings.reviewsPerDay)
  };
}

function normalizeStringArray(value) {
  if (Array.isArray(value)) {
    return value.map(item => String(item).trim()).filter(Boolean);
  }
  if (typeof value === 'string') {
    return value.split(',').map(item => item.trim()).filter(Boolean);
  }
  return [];
}

function normalizeReviewHistory(value) {
  return Array.isArray(value)
    ? value.filter(entry => entry && typeof entry === 'object')
    : [];
}

function normalizeClass(rawClass = {}, existingClass = null) {
  const now = Date.now();
  const name = String(rawClass.name || existingClass?.name || 'Untitled Class').trim() || 'Untitled Class';
  const color = /^#[0-9a-f]{6}$/i.test(String(rawClass.color || ''))
    ? rawClass.color
    : (existingClass?.color || '#3B82F6');

  return {
    ...existingClass,
    ...rawClass,
    id: rawClass.id || existingClass?.id || generateId('class'),
    name,
    color,
    created: rawClass.created || existingClass?.created || now,
    lastModified: rawClass.lastModified || existingClass?.lastModified || now
  };
}

function normalizeCard(card = {}) {
  return {
    ...card,
    id: card.id || generateId('card'),
    term: card.term || '',
    definition: card.definition || '',
    termImage: card.termImage || '',
    definitionImage: card.definitionImage || '',
    tags: normalizeStringArray(card.tags),
    suspended: Boolean(card.suspended),
    buriedUntil: card.buriedUntil || null,
    reviewHistory: normalizeReviewHistory(card.reviewHistory)
  };
}

async function saveDataUrlFile(dataUrl, directory, prefix, originalName) {
  await ensureDataDirs();
  const parsed = parseDataUrl(dataUrl);
  if (!parsed) return dataUrl;

  const originalExt = path.extname(originalName || '').replace('.', '');
  const ext = originalExt || extensionFromMime(parsed.mime);
  const fileName = `${safeFileName(prefix)}-${Date.now()}-${Math.random().toString(36).slice(2, 8)}.${ext}`;
  const filePath = path.join(directory, fileName);
  await fs.writeFile(filePath, parsed.buffer);
  return pathToFileURL(filePath).href;
}

async function normalizeSetImages(set) {
  if (!set || !Array.isArray(set.cards)) return set;

  const normalizedCards = [];
  for (const card of set.cards) {
    const next = { ...card };
    if (next.termImage && next.termImage.startsWith('data:image/')) {
      next.termImage = await saveDataUrlFile(next.termImage, imagesDir, 'term-image');
    }
    if (next.definitionImage && next.definitionImage.startsWith('data:image/')) {
      next.definitionImage = await saveDataUrlFile(next.definitionImage, imagesDir, 'definition-image');
    }
    if (next.media && typeof next.media === 'object') {
      next.media = { ...next.media };
      for (const side of ['term', 'definition']) {
        const items = Array.isArray(next.media[side]) ? next.media[side] : [];
        next.media[side] = [];
        for (const item of items) {
          const normalizedItem = { ...item };
          if (normalizedItem.src && String(normalizedItem.src).startsWith('data:')) {
            normalizedItem.src = await saveDataUrlFile(
              normalizedItem.src,
              imagesDir,
              `${side}-${normalizedItem.kind || 'media'}`,
              normalizedItem.name
            );
          }
          next.media[side].push(normalizedItem);
        }
      }
    }
    if (next.background && typeof next.background === 'object') {
      next.background = { ...next.background };
      for (const side of ['term', 'definition']) {
        const background = next.background[side];
        if (background?.src && String(background.src).startsWith('data:')) {
          next.background[side] = {
            ...background,
            src: await saveDataUrlFile(background.src, imagesDir, `${side}-background`, background.name)
          };
        }
      }
    }
    normalizedCards.push(next);
  }

  return {
    ...set,
    cards: normalizedCards
  };
}

async function normalizeSet(rawSet = {}, existingSet = null, options = {}) {
  const now = Date.now();
  const id = rawSet.id || existingSet?.id || generateId('set');
  const hasClassId = Object.prototype.hasOwnProperty.call(rawSet, 'classId');
  const imageNormalized = await normalizeSetImages({
    ...rawSet,
    cards: Array.isArray(rawSet.cards) ? rawSet.cards : []
  });

  return {
    ...existingSet,
    ...rawSet,
    id,
    name: rawSet.name || existingSet?.name || 'Untitled Set',
    description: rawSet.description || existingSet?.description || '',
    classId: hasClassId ? (rawSet.classId || null) : (existingSet?.classId || null),
    cards: imageNormalized.cards.map(normalizeCard),
    srsSettings: normalizeSrsSettings(rawSet.srsSettings || existingSet?.srsSettings || {}),
    created: rawSet.created || rawSet.createdAt || existingSet?.created || now,
    openedCount: rawSet.openedCount ?? existingSet?.openedCount ?? 0,
    lastOpened: rawSet.lastOpened ?? existingSet?.lastOpened ?? null,
    lastModified: options.preserveLastModified
      ? (rawSet.lastModified || existingSet?.lastModified || now)
      : now
  };
}

async function listSets() {
  return getFlashcardStore().listSets();
}

async function saveSet(rawSet) {
  return getFlashcardStore().saveSet(rawSet);
}

async function listClasses() {
  return getFlashcardStore().listClasses();
}

async function saveClass(rawClass) {
  return getFlashcardStore().saveClass(rawClass);
}

async function replaceClasses(rawClasses = []) {
  return getFlashcardStore().replaceClasses(rawClasses);
}

async function deleteClass(classId) {
  await createSafetySnapshot('delete-class');
  return getFlashcardStore().deleteClass(classId);
}

async function replaceSets(rawSets, options = {}) {
  if (options.snapshot !== false) {
    await createSafetySnapshot('replace-library');
  }
  return getFlashcardStore().replaceSets(rawSets);
}

async function getSet(id) {
  return getFlashcardStore().getSet(id);
}

async function deleteSet(id) {
  await createSafetySnapshot('delete-set');
  return getFlashcardStore().deleteSet(id);
}

async function listPremadeSets(classId, subjectId) {
  const folder = path.join(app.getAppPath(), 'premade-cards', safeFileName(classId), safeFileName(subjectId));
  try {
    const entries = await fs.readdir(folder, { withFileTypes: true });
    const sets = [];
    for (const entry of entries) {
      if (!entry.isFile() || !entry.name.toLowerCase().endsWith('.json')) continue;
      try {
        const raw = await fs.readFile(path.join(folder, entry.name), 'utf8');
        const set = JSON.parse(raw);
        sets.push({ ...set, fileName: entry.name });
      } catch (error) {
        console.warn(`Could not load premade set ${entry.name}:`, error);
      }
    }
    return sets;
  } catch (error) {
    return [];
  }
}

async function getPremadeSet(classId, subjectId, fileName) {
  const folder = path.join(app.getAppPath(), 'premade-cards', safeFileName(classId), safeFileName(subjectId));
  const filePath = path.join(folder, safeFileName(fileName, 'set.json'));
  try {
    const raw = await fs.readFile(filePath, 'utf8');
    return JSON.parse(raw);
  } catch (error) {
    return null;
  }
}

function assertManagedFileUrl(url, directory) {
  if (!url || !url.startsWith('file://')) return null;
  const filePath = fileURLToPath(url);
  const resolved = path.resolve(filePath);
  const allowed = path.resolve(directory);
  if (!resolved.startsWith(allowed + path.sep)) return null;
  return resolved;
}

async function managedFileUrlToDataUrl(fileUrl, directory) {
  const managedPath = assertManagedFileUrl(fileUrl, directory);
  if (!managedPath) return fileUrl;

  try {
    const buffer = await fs.readFile(managedPath);
    return `data:${mimeFromExtension(managedPath)};base64,${buffer.toString('base64')}`;
  } catch (error) {
    console.warn(`Could not embed managed file ${managedPath}:`, error);
    return fileUrl;
  }
}

async function embedSetImages(set) {
  if (!set || !Array.isArray(set.cards)) return set;

  const cards = [];
  for (const card of set.cards) {
    const next = {
      ...card,
      termImage: await managedFileUrlToDataUrl(card.termImage, imagesDir),
      definitionImage: await managedFileUrlToDataUrl(card.definitionImage, imagesDir)
    };

    if (next.media && typeof next.media === 'object') {
      next.media = { ...next.media };
      for (const side of ['term', 'definition']) {
        const items = Array.isArray(next.media[side]) ? next.media[side] : [];
        next.media[side] = [];
        for (const item of items) {
          next.media[side].push({
            ...item,
            src: await managedFileUrlToDataUrl(item?.src, imagesDir)
          });
        }
      }
    }

    if (next.background && typeof next.background === 'object') {
      next.background = { ...next.background };
      for (const side of ['term', 'definition']) {
        const background = next.background[side];
        next.background[side] = background?.src
          ? {
              ...background,
              src: await managedFileUrlToDataUrl(background.src, imagesDir)
            }
          : null;
      }
    }

    cards.push({
      ...next
    });
  }

  return {
    ...set,
    cards
  };
}

function isPlainObject(value) {
  return value !== null && typeof value === 'object' && !Array.isArray(value);
}

async function createBackupPayload() {
  await ensureDataDirs();
  const [sets, classes, settings, progress, state] = await Promise.all([
    listSets(),
    listClasses(),
    getFlashcardStore().getSettings(),
    getFlashcardStore().getAllProgress(),
    getFlashcardStore().getAllState()
  ]);

  const embeddedSets = [];
  for (const set of sets) {
    embeddedSets.push(await embedSetImages(set));
  }

  return {
    app: 'Erudite Flashcards',
    schemaVersion: 1,
    exportedAt: new Date().toISOString(),
    data: {
      sets: embeddedSets,
      classes,
      settings: isPlainObject(settings) ? settings : {},
      progress: isPlainObject(progress) ? progress : {},
      state: isPlainObject(state) ? state : {}
    }
  };
}

async function createSafetySnapshot(reason = 'snapshot') {
  await ensureDataDirs();
  const payload = await createBackupPayload();
  const stamp = new Date().toISOString().replace(/[:.]/g, '-');
  const fileName = `${safeFileName(reason, 'snapshot')}-${stamp}.json`;
  const filePath = path.join(backupsDir, fileName);
  await fs.writeFile(filePath, JSON.stringify(payload, null, 2), 'utf8');
  return filePath;
}

async function statIfExists(filePath) {
  try {
    return await fs.stat(filePath);
  } catch (_error) {
    return null;
  }
}

async function listRecentBackups(limit = 8) {
  await ensureDataDirs();

  try {
    const entries = await fs.readdir(backupsDir, { withFileTypes: true });
    const backups = [];

    for (const entry of entries) {
      if (!entry.isFile() || !entry.name.toLowerCase().endsWith('.json')) continue;
      const filePath = path.join(backupsDir, entry.name);
      const stat = await statIfExists(filePath);
      backups.push({
        name: entry.name,
        path: filePath,
        sizeBytes: stat?.size || 0,
        modifiedAt: stat?.mtime ? stat.mtime.toISOString() : null
      });
    }

    return backups
      .sort((a, b) => new Date(b.modifiedAt || 0) - new Date(a.modifiedAt || 0))
      .slice(0, limit);
  } catch (_error) {
    return [];
  }
}

async function findBrokenManagedImages(sets = []) {
  const broken = [];
  let managedImageLinks = 0;
  let unmanagedFileLinks = 0;

  for (const set of sets) {
    for (const card of set.cards || []) {
      const managedLinks = [
        ['term', card.termImage],
        ['definition', card.definitionImage]
      ];

      for (const side of ['term', 'definition']) {
        const mediaItems = Array.isArray(card.media?.[side]) ? card.media[side] : [];
        mediaItems.forEach((item, index) => {
          managedLinks.push([`${side}-media-${index + 1}`, item?.src]);
        });
        managedLinks.push([`${side}-background`, card.background?.[side]?.src]);
      }

      for (const [side, fileUrl] of managedLinks) {
        if (!fileUrl || !String(fileUrl).startsWith('file://')) continue;

        const managedPath = assertManagedFileUrl(fileUrl, imagesDir);
        if (!managedPath) {
          unmanagedFileLinks += 1;
          continue;
        }

        managedImageLinks += 1;
        const stat = await statIfExists(managedPath);
        if (!stat) {
          broken.push({
            setId: set.id,
            setName: set.name,
            cardId: card.id || null,
            side,
            path: managedPath
          });
        }
      }
    }
  }

  return {
    managedImageLinks,
    unmanagedFileLinks,
    broken
  };
}

async function getDiagnostics() {
  await ensureDataDirs();
  const store = getFlashcardStore();
  const [storeDiagnostics, sets, classes, settings, progress, state, recentBackups] = await Promise.all([
    store.getDiagnostics(),
    listSets(),
    listClasses(),
    store.getSettings(),
    store.getAllProgress(),
    store.getAllState(),
    listRecentBackups()
  ]);
  const dbStat = await statIfExists(storeDiagnostics.dbPath);
  const imageHealth = await findBrokenManagedImages(sets);
  const issues = [];

  if (storeDiagnostics.counts.orphanedCards > 0) {
    issues.push(`${storeDiagnostics.counts.orphanedCards} card row(s) reference missing sets.`);
  }
  if (imageHealth.broken.length > 0) {
    issues.push(`${imageHealth.broken.length} managed image link(s) are missing files.`);
  }
  if (!storeDiagnostics.legacyJsonMigrated) {
    issues.push('Legacy JSON migration marker has not been written.');
  }

  return {
    appName: app.getName(),
    appVersion: app.getVersion(),
    electronVersion: process.versions.electron,
    nodeVersion: process.versions.node,
    generatedAt: new Date().toISOString(),
    storageEngine: 'SQLite',
    schemaVersion: storeDiagnostics.schemaVersion,
    paths: {
      userData: app.getPath('userData'),
      dataDir,
      database: storeDiagnostics.dbPath,
      imagesDir,
      fontsDir,
      backupsDir
    },
    database: {
      exists: Boolean(dbStat),
      sizeBytes: dbStat?.size || 0,
      modifiedAt: dbStat?.mtime ? dbStat.mtime.toISOString() : null
    },
    counts: {
      ...storeDiagnostics.counts,
      sets: sets.length,
      classes: classes.length,
      cards: sets.reduce((total, set) => total + (Array.isArray(set.cards) ? set.cards.length : 0), 0),
      progressEntries: Object.keys(progress || {}).length,
      stateEntries: Object.keys(state || {}).length
    },
    settings: {
      theme: settings?.theme || 'dark',
      contentFont: settings?.fonts?.content || null
    },
    health: {
      status: issues.length > 0 ? 'warning' : 'ok',
      issues
    },
    imageHealth: {
      managedImageLinks: imageHealth.managedImageLinks,
      unmanagedFileLinks: imageHealth.unmanagedFileLinks,
      brokenCount: imageHealth.broken.length
    },
    brokenImageLinks: imageHealth.broken.slice(0, 50),
    recentBackups
  };
}

function readBackupData(payload) {
  const data = Array.isArray(payload) ? { sets: payload } : (payload?.data || payload || {});
  const sets = data.sets;

  if (!Array.isArray(sets)) {
    throw new Error('Backup file does not contain a flashcard set list.');
  }

  return {
    sets,
    classes: Array.isArray(data.classes) ? data.classes : [],
    settings: isPlainObject(data.settings) ? data.settings : null,
    progress: isPlainObject(data.progress) ? data.progress : null,
    state: isPlainObject(data.state) ? data.state : null
  };
}

async function restoreBackupPayload(payload) {
  const data = readBackupData(payload);
  await createSafetySnapshot('before-restore');
  const restoredClasses = await replaceClasses(data.classes || []);
  const restoredSets = await replaceSets(data.sets, { snapshot: false });

  if (data.settings) await getFlashcardStore().saveSettings(data.settings);
  if (data.progress) await getFlashcardStore().replaceProgress(data.progress);
  if (data.state) await getFlashcardStore().replaceState(data.state);

  return {
    setCount: restoredSets.length,
    classCount: restoredClasses.length
  };
}

async function exportBackup() {
  const payload = await createBackupPayload();
  const dateStamp = new Date().toISOString().slice(0, 10);
  const result = await dialog.showSaveDialog(mainWindow, {
    title: 'Export Flashcards Backup',
    defaultPath: `erudite-flashcards-backup-${dateStamp}.json`,
    filters: [
      { name: 'Erudite Flashcards Backup', extensions: ['json'] }
    ]
  });

  if (result.canceled || !result.filePath) {
    return { canceled: true };
  }

  await fs.writeFile(result.filePath, JSON.stringify(payload, null, 2), 'utf8');
  return {
    canceled: false,
    filePath: result.filePath,
    setCount: payload.data.sets.length
  };
}

async function importBackup() {
  const result = await dialog.showOpenDialog(mainWindow, {
    title: 'Restore Flashcards Backup',
    properties: ['openFile'],
    filters: [
      { name: 'Erudite Flashcards Backup', extensions: ['json'] }
    ]
  });

  if (result.canceled || !result.filePaths?.[0]) {
    return { canceled: true };
  }

  const raw = await fs.readFile(result.filePaths[0], 'utf8');
  const payload = JSON.parse(raw);
  const restoreResult = await restoreBackupPayload(payload);

  return {
    canceled: false,
    filePath: result.filePaths[0],
    ...restoreResult
  };
}

function stripHtml(value) {
  return String(value || '')
    .replace(/<br\s*\/?>/gi, '\n')
    .replace(/<\/p>/gi, '\n')
    .replace(/<[^>]+>/g, '')
    .replace(/&nbsp;/g, ' ')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .trim();
}

function escapeDelimited(value, delimiter) {
  const text = String(value ?? '');
  const mustQuote = text.includes(delimiter) || text.includes('"') || text.includes('\n') || text.includes('\r');
  const escaped = text.replace(/"/g, '""');
  return mustQuote ? `"${escaped}"` : escaped;
}

function parseDelimitedLine(line, delimiter) {
  const cells = [];
  let current = '';
  let inQuotes = false;

  for (let index = 0; index < line.length; index++) {
    const char = line[index];
    const next = line[index + 1];

    if (char === '"' && inQuotes && next === '"') {
      current += '"';
      index++;
    } else if (char === '"') {
      inQuotes = !inQuotes;
    } else if (char === delimiter && !inQuotes) {
      cells.push(current);
      current = '';
    } else {
      current += char;
    }
  }

  cells.push(current);
  return cells;
}

function parseDelimited(raw, delimiter) {
  const lines = String(raw || '').replace(/\r\n/g, '\n').replace(/\r/g, '\n').split('\n').filter(line => line.trim());
  if (lines.length === 0) return [];

  const headers = parseDelimitedLine(lines[0], delimiter).map(header => header.trim().toLowerCase());
  const rows = [];

  for (const line of lines.slice(1)) {
    const cells = parseDelimitedLine(line, delimiter);
    const row = {};
    headers.forEach((header, index) => {
      row[header] = cells[index] || '';
    });
    rows.push(row);
  }

  return rows;
}

function uniqueSetName(baseName, usedNames) {
  const cleanBase = String(baseName || 'Imported Set').trim() || 'Imported Set';
  if (!usedNames.has(cleanBase.toLowerCase())) {
    usedNames.add(cleanBase.toLowerCase());
    return cleanBase;
  }

  let counter = 2;
  while (usedNames.has(`${cleanBase} ${counter}`.toLowerCase())) {
    counter++;
  }

  const name = `${cleanBase} ${counter}`;
  usedNames.add(name.toLowerCase());
  return name;
}

async function exportDelimited(format = 'csv') {
  const delimiter = format === 'tsv' ? '\t' : ',';
  const sets = await listSets();
  const classes = await listClasses();
  const classNameById = new Map(classes.map((classItem) => [String(classItem.id), classItem.name]));
  const rows = [['deck', 'class', 'term', 'definition', 'tags']];

  for (const set of sets) {
    for (const card of set.cards || []) {
      rows.push([
        set.name || 'Untitled Set',
        set.classId ? (classNameById.get(String(set.classId)) || '') : '',
        stripHtml(card.term),
        stripHtml(card.definition),
        Array.isArray(card.tags) ? card.tags.join(', ') : ''
      ]);
    }
  }

  const text = rows.map(row => row.map(cell => escapeDelimited(cell, delimiter)).join(delimiter)).join('\n');
  const extension = format === 'tsv' ? 'tsv' : 'csv';
  const result = await dialog.showSaveDialog(mainWindow, {
    title: `Export Flashcards ${extension.toUpperCase()}`,
    defaultPath: `erudite-flashcards-${new Date().toISOString().slice(0, 10)}.${extension}`,
    filters: [
      { name: `${extension.toUpperCase()} Flashcards`, extensions: [extension] }
    ]
  });

  if (result.canceled || !result.filePath) return { canceled: true };
  await fs.writeFile(result.filePath, text, 'utf8');
  return { canceled: false, filePath: result.filePath, cardCount: Math.max(0, rows.length - 1) };
}

async function importDelimited() {
  const result = await dialog.showOpenDialog(mainWindow, {
    title: 'Import CSV or TSV Flashcards',
    properties: ['openFile'],
    filters: [
      { name: 'CSV or TSV Flashcards', extensions: ['csv', 'tsv'] }
    ]
  });

  if (result.canceled || !result.filePaths?.[0]) return { canceled: true };

  const filePath = result.filePaths[0];
  const raw = await fs.readFile(filePath, 'utf8');
  const delimiter = path.extname(filePath).toLowerCase() === '.tsv' ? '\t' : ',';
  const rows = parseDelimited(raw, delimiter);
  const grouped = new Map();

  for (const row of rows) {
    const term = row.term || row.front || '';
    const definition = row.definition || row.back || '';
    if (!term && !definition) continue;

    const deck = row.deck || row.set || row.setname || path.basename(filePath, path.extname(filePath));
    const className = String(row.class || row.classname || '').trim();
    const groupKey = `${className.toLowerCase()}::${deck}`;
    if (!grouped.has(groupKey)) grouped.set(groupKey, { deck, className, cards: [] });
    grouped.get(groupKey).cards.push({
      term,
      definition,
      tags: normalizeStringArray(row.tags)
    });
  }

  if (grouped.size === 0) {
    throw new Error('No valid cards found in import file.');
  }

  const existingSets = await listSets();
  const existingClasses = await listClasses();
  const nextClasses = [...existingClasses];
  const classByName = new Map(existingClasses.map((classItem) => [String(classItem.name || '').trim().toLowerCase(), classItem]));
  function getClassIdForName(name) {
    const cleanName = String(name || '').trim();
    if (!cleanName) return null;
    const key = cleanName.toLowerCase();
    if (classByName.has(key)) return classByName.get(key).id;

    const newClass = normalizeClass({
      name: cleanName,
      color: '#3B82F6'
    });
    classByName.set(key, newClass);
    nextClasses.push(newClass);
    return newClass.id;
  }

  const usedNames = new Set(existingSets.map(set => String(set.name || '').toLowerCase()));
  const importedSets = Array.from(grouped.values()).map(({ deck, className, cards }) => ({
    id: generateId('set'),
    name: uniqueSetName(deck, usedNames),
    classId: getClassIdForName(className),
    description: `Imported from ${path.basename(filePath)}`,
    cards,
    created: Date.now(),
    openedCount: 0
  }));

  await replaceClasses(nextClasses);
  await replaceSets([...existingSets, ...importedSets]);
  return {
    canceled: false,
    setCount: importedSets.length,
    cardCount: importedSets.reduce((total, set) => total + set.cards.length, 0)
  };
}

function sendMenuCommand(command) {
  if (mainWindow && !mainWindow.isDestroyed()) {
    mainWindow.webContents.send('app:menu-command', command);
  }
}

function createAppMenu() {
  const template = [
    {
      label: 'File',
      submenu: [
        { label: 'New Set', accelerator: 'Ctrl+Alt+N', click: () => sendMenuCommand('new-set') },
        { label: 'Import Flashcards', accelerator: 'Ctrl+I', click: () => sendMenuCommand('import-flashcards') },
        { label: 'Card Browser', accelerator: 'Ctrl+B', click: () => sendMenuCommand('open-card-browser') },
        { type: 'separator' },
        { label: 'Export Backup', accelerator: 'Ctrl+Shift+E', click: () => sendMenuCommand('export-backup') },
        { label: 'Restore Backup', accelerator: 'Ctrl+Shift+O', click: () => sendMenuCommand('restore-backup') },
        { label: 'Export CSV', click: () => sendMenuCommand('export-csv') },
        { label: 'Export TSV', click: () => sendMenuCommand('export-tsv') },
        { label: 'Import CSV/TSV', click: () => sendMenuCommand('import-delimited') },
        { type: 'separator' },
        { role: 'quit' }
      ]
    },
    {
      label: 'Edit',
      submenu: [
        { role: 'undo' },
        { role: 'redo' },
        { type: 'separator' },
        { role: 'cut' },
        { role: 'copy' },
        { role: 'paste' },
        { role: 'selectAll' }
      ]
    },
    {
      label: 'View',
      submenu: [
        { role: 'reload' },
        ...(isDev ? [{ role: 'toggleDevTools' }] : []),
        { type: 'separator' },
        { role: 'resetZoom' },
        { role: 'zoomIn' },
        { role: 'zoomOut' },
        { type: 'separator' },
        { label: 'Diagnostics', click: () => sendMenuCommand('open-diagnostics') }
      ]
    },
    {
      label: 'Study',
      submenu: [
        { label: 'Start Review Due', accelerator: 'Ctrl+R', click: () => sendMenuCommand('review-due') },
        { label: 'Toggle SRS', accelerator: 'Ctrl+Shift+S', click: () => sendMenuCommand('toggle-srs') }
      ]
    }
  ];

  Menu.setApplicationMenu(Menu.buildFromTemplate(template));
}

async function createWindow() {
  const windowState = await loadWindowState();
  mainWindow = new BrowserWindow({
    width: windowState.width,
    height: windowState.height,
    x: windowState.x,
    y: windowState.y,
    minWidth: 960,
    minHeight: 640,
    title: 'Erudite Flashcards',
    icon: path.join(__dirname, 'assets', 'icons', 'icon.png'),
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: true,
      nodeIntegration: false,
      sandbox: false
    }
  });

  if (windowState.maximized) {
    mainWindow.maximize();
  } else if (windowState.fullScreen) {
    mainWindow.setFullScreen(true);
  }

  let windowStateTimer = null;
  const saveWindowStateSoon = () => {
    if (windowStateTimer) clearTimeout(windowStateTimer);
    windowStateTimer = setTimeout(() => saveWindowState(mainWindow), 350);
  };

  ['resize', 'move', 'maximize', 'unmaximize', 'enter-full-screen', 'leave-full-screen'].forEach((eventName) => {
    mainWindow.on(eventName, saveWindowStateSoon);
  });

  mainWindow.on('close', () => {
    if (windowStateTimer) clearTimeout(windowStateTimer);
    saveWindowState(mainWindow);
  });

  if (smokeTest) {
    const fail = (message) => {
      console.error(`SMOKE_FAIL ${message}`);
      app.exit(1);
    };

    mainWindow.webContents.on('did-fail-load', (_event, code, description) => {
      if (code === -3) return;
      fail(`${code} ${description}`);
    });

    mainWindow.webContents.once('did-finish-load', () => {
      console.log('SMOKE_READY flashcards.html');
      setTimeout(() => app.exit(0), 1000);
    });

    mainWindow.webContents.on('render-process-gone', (_event, details) => {
      fail(`renderer gone: ${details.reason}`);
    });
  }

  mainWindow.loadFile(path.join(__dirname, 'flashcards.html'));

  if (isDev) {
    mainWindow.webContents.on('before-input-event', (event, input) => {
      if (input.control && input.shift && input.key.toLowerCase() === 'i') {
        mainWindow.webContents.openDevTools({ mode: 'detach' });
      }
    });
  }
}

const gotTheLock = app.requestSingleInstanceLock();

if (!gotTheLock) {
  app.quit();
} else {
  app.on('second-instance', () => {
    if (mainWindow) {
      if (mainWindow.isMinimized()) mainWindow.restore();
      mainWindow.focus();
    }
  });

  app.whenReady().then(async () => {
    await ensureDataDirs();
    await initializeFlashcardStore();
    createAppMenu();

    session.defaultSession.setPermissionRequestHandler((webContents, permission, callback) => {
      callback(permission === 'media');
    });

    await createWindow();

    app.on('activate', async () => {
      if (BrowserWindow.getAllWindows().length === 0) await createWindow();
    });
  });

  app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit();
  });
}

ipcMain.handle('flashcards:listSets', listSets);
ipcMain.handle('flashcards:listSetsMeta', () => getFlashcardStore().listSetsMeta());
ipcMain.handle('flashcards:getSet', (_event, id) => getSet(id));
ipcMain.handle('flashcards:saveSet', (_event, set) => saveSet(set));
ipcMain.handle('flashcards:replaceSets', (_event, sets) => replaceSets(sets));
ipcMain.handle('flashcards:deleteSet', (_event, id) => deleteSet(id));
ipcMain.handle('flashcards:listClasses', listClasses);
ipcMain.handle('flashcards:saveClass', (_event, classData) => saveClass(classData));
ipcMain.handle('flashcards:deleteClass', (_event, classId) => deleteClass(classId));
ipcMain.handle('flashcards:exportBackup', exportBackup);
ipcMain.handle('flashcards:importBackup', importBackup);
ipcMain.handle('flashcards:exportDelimited', (_event, format) => exportDelimited(format));
ipcMain.handle('flashcards:importDelimited', importDelimited);
ipcMain.handle('flashcards:recordReview', (_event, params) => getFlashcardStore().recordReview(params));
ipcMain.handle('flashcards:undoReviewLog', (_event, cardId, logId) => getFlashcardStore().undoReviewLog(cardId, logId));
ipcMain.handle('flashcards:resetDeckSRS', (_event, setId, deleteHistory) => getFlashcardStore().resetDeckSRS(setId, deleteHistory));
ipcMain.handle('flashcards:createDeckBackup', (_event, setId) => getFlashcardStore().createDeckBackup(setId));
ipcMain.handle('flashcards:saveStudySession', (_event, session) => getFlashcardStore().saveStudySession(session));
ipcMain.handle('flashcards:getStudySessions', (_event, sinceMs) => getFlashcardStore().getStudySessions(sinceMs));
ipcMain.handle('flashcards:getProgress', async (_event, setId) => {
  return getFlashcardStore().getProgress(setId);
});
ipcMain.handle('flashcards:getAllProgress', async () => {
  return getFlashcardStore().getAllProgress();
});
ipcMain.handle('flashcards:saveProgress', async (_event, setId, value) => {
  return getFlashcardStore().saveProgress(setId, value);
});
ipcMain.handle('flashcards:getSettings', () => getFlashcardStore().getSettings());
ipcMain.handle('flashcards:saveSettings', async (_event, settings) => {
  return getFlashcardStore().saveSettings(settings || {});
});
ipcMain.handle('flashcards:getState', async (_event, key) => {
  return getFlashcardStore().getState(key);
});
ipcMain.handle('flashcards:setState', async (_event, key, value) => {
  return getFlashcardStore().setState(key, value);
});
ipcMain.handle('flashcards:removeState', async (_event, key) => {
  return getFlashcardStore().removeState(key);
});
ipcMain.handle('flashcards:getDiagnostics', getDiagnostics);
ipcMain.handle('flashcards:saveImage', (_event, dataUrl, meta = {}) => {
  return saveDataUrlFile(dataUrl, imagesDir, meta.prefix || 'flashcard-image', meta.fileName);
});
ipcMain.handle('flashcards:deleteImage', async (_event, fileUrl) => {
  const managed = assertManagedFileUrl(fileUrl, imagesDir);
  if (managed) await fs.rm(managed, { force: true });
  return true;
});
ipcMain.handle('flashcards:saveFont', (_event, dataUrl, meta = {}) => {
  return saveDataUrlFile(dataUrl, fontsDir, meta.prefix || 'font', meta.fileName);
});
ipcMain.handle('flashcards:listPremadeSets', (_event, classId, subjectId) => {
  return listPremadeSets(classId, subjectId);
});
ipcMain.handle('flashcards:getPremadeSet', (_event, classId, subjectId, fileName) => {
  return getPremadeSet(classId, subjectId, fileName);
});
