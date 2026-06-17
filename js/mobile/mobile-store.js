(function () {
  const capacitor = window.Capacitor;
  const plugins = capacitor?.Plugins || {};
  const Filesystem = plugins.Filesystem;
  const Share = plugins.Share;
  const schema = window.EruditeCore?.schema;
  const backup = window.EruditeCore?.backup;

  if (!capacitor || !Filesystem || !schema || !backup || typeof initSqlJs === 'undefined') {
    console.warn('[mobile-store] Guard failed — missing:', {
      capacitor: !!capacitor, Filesystem: !!Filesystem,
      schema: !!schema, backup: !!backup,
      initSqlJs: typeof initSqlJs !== 'undefined'
    });
    return;
  }

  const DB_PATH = 'erudite-flashcards/erudite-flashcards.sqlite';
  const BACKUP_DIR = 'erudite-flashcards/backups';
  const STUDY_PATCHES_KEY = 'erudite-mobile-study-card-patches-v1';
  const SET_BACKUP_PREFIX = 'erudite-mobile-set-backup:';
  const SET_BACKUP_INDEX_KEY = 'erudite-mobile-set-backup-index-v1';
  const CLASS_BACKUP_PREFIX = 'erudite-mobile-class-backup:';
  const CLASS_BACKUP_INDEX_KEY = 'erudite-mobile-class-backup-index-v1';
  const DIRECTORY_DATA = 'DATA';
  const DIRECTORY_DOCUMENTS = 'DOCUMENTS';
  const ENCODING_UTF8 = 'utf8';

  const isNative = !!(capacitor && (capacitor.getPlatform() === 'android' || capacitor.getPlatform() === 'ios') && window.CapacitorSqliteHelper);
  const { SQLiteConnection, CapacitorSQLite } = window.CapacitorSqliteHelper || {};

  let readyPromise = null;
  let SQL = null;
  let db = null;

  document.documentElement.classList.add('is-capacitor', 'is-mobile-shell');

  function jsonParse(value, fallback) {
    if (value === null || value === undefined || value === '') return fallback;
    try {
      return JSON.parse(value);
    } catch (_error) {
      return fallback;
    }
  }

  function jsonString(value) {
    return JSON.stringify(value ?? null);
  }

  function readSetBackupIndex() {
    try {
      const parsed = JSON.parse(localStorage.getItem(SET_BACKUP_INDEX_KEY) || '[]');
      return Array.isArray(parsed) ? parsed.map(String) : [];
    } catch (_) {
      return [];
    }
  }

  function readClassBackupIndex() {
    try {
      const parsed = JSON.parse(localStorage.getItem(CLASS_BACKUP_INDEX_KEY) || '[]');
      return Array.isArray(parsed) ? parsed.map(String) : [];
    } catch (_) {
      return [];
    }
  }

  function writeClassBackupIndex(ids) {
    try {
      localStorage.setItem(CLASS_BACKUP_INDEX_KEY, JSON.stringify(Array.from(new Set(ids.map(String)))));
    } catch (_) {}
  }

  function writeSetBackupIndex(ids) {
    try {
      localStorage.setItem(SET_BACKUP_INDEX_KEY, JSON.stringify(Array.from(new Set(ids.map(String)))));
    } catch (_) {}
  }

  function rememberSetBackup(set) {
    if (!set?.id || !Array.isArray(set.cards) || !set.cards.length) return;
    try {
      const normalized = schema.normalizeSet(set, null, { preserveLastModified: true });
      localStorage.setItem(`${SET_BACKUP_PREFIX}${normalized.id}`, JSON.stringify(normalized));
      const ids = readSetBackupIndex();
      if (!ids.includes(String(normalized.id))) {
        ids.push(String(normalized.id));
        writeSetBackupIndex(ids);
      }
      const legacySets = jsonParse(localStorage.getItem('flashcardSets'), []);
      const updated = Array.isArray(legacySets)
        ? legacySets.filter(item => String(item?.id) !== String(normalized.id))
        : [];
      updated.push(normalized);
      localStorage.setItem('flashcardSets', JSON.stringify(updated));
    } catch (error) {
      console.warn('[mobile-store] Could not write emergency deck mirror:', error?.message || error);
    }
  }

  function forgetSetBackup(id) {
    try {
      localStorage.removeItem(`${SET_BACKUP_PREFIX}${id}`);
      writeSetBackupIndex(readSetBackupIndex().filter(item => String(item) !== String(id)));
      const legacySets = jsonParse(localStorage.getItem('flashcardSets'), []);
      if (Array.isArray(legacySets)) {
        localStorage.setItem('flashcardSets', JSON.stringify(legacySets.filter(item => String(item?.id) !== String(id))));
      }
    } catch (_) {}
  }

  function clearSetBackups() {
    try {
      readSetBackupIndex().forEach(id => localStorage.removeItem(`${SET_BACKUP_PREFIX}${id}`));
      localStorage.removeItem(SET_BACKUP_INDEX_KEY);
      localStorage.removeItem('flashcardSets');
    } catch (_) {}
  }

  function rememberClassBackup(classData) {
    if (!classData?.id) return;
    try {
      const normalized = schema.normalizeClass(classData, null, { preserveLastModified: true });
      localStorage.setItem(`${CLASS_BACKUP_PREFIX}${normalized.id}`, JSON.stringify(normalized));
      const ids = readClassBackupIndex();
      if (!ids.includes(String(normalized.id))) {
        ids.push(String(normalized.id));
        writeClassBackupIndex(ids);
      }
      const legacyClasses = jsonParse(localStorage.getItem('flashcardClasses'), []);
      const updated = Array.isArray(legacyClasses)
        ? legacyClasses.filter(item => String(item?.id) !== String(normalized.id))
        : [];
      updated.push(normalized);
      localStorage.setItem('flashcardClasses', JSON.stringify(updated));
    } catch (error) {
      console.warn('[mobile-store] Could not write emergency class mirror:', error?.message || error);
    }
  }

  function forgetClassBackup(id) {
    try {
      localStorage.removeItem(`${CLASS_BACKUP_PREFIX}${id}`);
      writeClassBackupIndex(readClassBackupIndex().filter(item => String(item) !== String(id)));
      const legacyClasses = jsonParse(localStorage.getItem('flashcardClasses'), []);
      if (Array.isArray(legacyClasses)) {
        localStorage.setItem('flashcardClasses', JSON.stringify(legacyClasses.filter(item => String(item?.id) !== String(id))));
      }
    } catch (_) {}
  }

  function clearClassBackups() {
    try {
      readClassBackupIndex().forEach(id => localStorage.removeItem(`${CLASS_BACKUP_PREFIX}${id}`));
      localStorage.removeItem(CLASS_BACKUP_INDEX_KEY);
      localStorage.removeItem('flashcardClasses');
    } catch (_) {}
  }

  function readClassBackups() {
    const mirrored = readClassBackupIndex()
      .map(id => {
        try {
          return JSON.parse(localStorage.getItem(`${CLASS_BACKUP_PREFIX}${id}`) || 'null');
        } catch (_) {
          return null;
        }
      })
      .filter(item => item && item.id);
    const legacyClasses = jsonParse(localStorage.getItem('flashcardClasses'), []);
    const all = [...mirrored, ...(Array.isArray(legacyClasses) ? legacyClasses : [])];
    const unique = new Map();
    all.forEach(item => {
      if (item?.id) unique.set(String(item.id), item);
    });
    return Array.from(unique.values());
  }

  function readSetBackups() {
    return readSetBackupIndex()
      .map(id => {
        try {
          return JSON.parse(localStorage.getItem(`${SET_BACKUP_PREFIX}${id}`) || 'null');
        } catch (_) {
          return null;
        }
      })
      .filter(set => set && Array.isArray(set.cards) && set.cards.length)
      .concat((() => {
        const legacySets = jsonParse(localStorage.getItem('flashcardSets'), []);
        return Array.isArray(legacySets) ? legacySets.filter(set => set && Array.isArray(set.cards) && set.cards.length) : [];
      })());
  }

  async function recoverLocalSetBackupsIfEmpty() {
    try {
      const setsCount = await rows('SELECT COUNT(*) AS count FROM sets WHERE deleted_at IS NULL');
      const currentCount = Number(setsCount[0]?.count || 0);
      if (currentCount > 0) return false;
      const backups = readSetBackups();
      if (!backups.length) return false;
      for (const set of backups) {
        const normalized = schema.normalizeSet(set, null, { preserveLastModified: true });
        await upsertSet(normalized);
        await replaceCardsForSet(normalized.id, normalized.cards || []);
      }
      console.warn(`[mobile-store] Recovered ${backups.length} deck(s) from emergency local mirrors`);
      return true;
    } catch (error) {
      console.warn('[mobile-store] Emergency mirror recovery failed:', error?.message || error);
      return false;
    }
  }

  async function recoverLocalClassBackupsIfEmptyOrMissing() {
    try {
      const currentRows = await rows('SELECT id FROM classes WHERE deleted_at IS NULL');
      const current = currentRows.map(row => String(row.id));
      const currentIds = new Set(current);
      const backups = readClassBackups().filter(item => item?.id && !currentIds.has(String(item.id)));
      if (!backups.length) return false;
      for (const classData of backups) {
        await upsertClass(schema.normalizeClass(classData, null, { preserveLastModified: true }));
      }
      console.warn(`[mobile-store] Recovered ${backups.length} class record(s) from emergency local mirrors`);
      return true;
    } catch (error) {
      console.warn('[mobile-store] Emergency class mirror recovery failed:', error?.message || error);
      return false;
    }
  }

  async function repairOrphanedClassIds() {
    try {
      const classRows = await rows('SELECT id FROM classes WHERE deleted_at IS NULL');
      const validIds = new Set(classRows.map(row => String(row.id)));
      const setRows = await rows('SELECT id, class_id FROM sets WHERE deleted_at IS NULL AND class_id IS NOT NULL');
      const orphaned = setRows.filter(row => row.class_id && !validIds.has(String(row.class_id)));
      if (!orphaned.length) return false;
      for (const row of orphaned) {
        await run('UPDATE sets SET class_id = NULL, last_modified = ? WHERE id = ?', [Date.now(), String(row.id)]);
      }
      console.warn(`[mobile-store] Moved ${orphaned.length} deck(s) with missing classes back to General`);
      return true;
    } catch (error) {
      console.warn('[mobile-store] Could not repair orphaned class ids:', error?.message || error);
      return false;
    }
  }

  function bytesToBase64(bytes) {
    let binary = '';
    const chunkSize = 0x8000;
    for (let index = 0; index < bytes.length; index += chunkSize) {
      const chunk = bytes.subarray(index, index + chunkSize);
      binary += String.fromCharCode.apply(null, chunk);
    }
    return btoa(binary);
  }

  function base64ToBytes(base64) {
    const binary = atob(String(base64 || ''));
    const bytes = new Uint8Array(binary.length);
    for (let index = 0; index < binary.length; index += 1) {
      bytes[index] = binary.charCodeAt(index);
    }
    return bytes;
  }

  async function rows(sql, params = []) {
    if (isNative && db) {
      const res = await db.query(sql, params);
      return res.values || [];
    }
    const statement = db.prepare(sql);
    statement.bind(params);
    const result = [];
    while (statement.step()) result.push(statement.getAsObject());
    statement.free();
    return result;
  }

  async function run(sql, params = []) {
    if (isNative && db) {
      await db.run(sql, params);
      return;
    }
    const statement = db.prepare(sql);
    statement.run(params);
    statement.free();
  }

  async function executeRaw(sql) {
    if (isNative && db) {
      await db.execute(sql);
      return;
    }
    db.exec(sql);
  }

  async function executeSet(set) {
    if (isNative && db) {
      await db.executeSet(set);
      return;
    }
    db.exec('BEGIN TRANSACTION;');
    try {
      for (const item of set) {
        const statement = db.prepare(item.statement);
        statement.run(item.values);
        statement.free();
      }
      db.exec('COMMIT;');
    } catch (error) {
      db.exec('ROLLBACK;');
      throw error;
    }
  }

  async function migrateFromLegacySqlJs() {
    try {
      const exists = await Filesystem.stat({ path: DB_PATH, directory: DIRECTORY_DATA })
        .then(() => true)
        .catch(() => false);
      if (!exists) return;

      console.log('[mobile-store] Legacy SQLite file found. Starting migration...');

      const file = await Filesystem.readFile({ path: DB_PATH, directory: DIRECTORY_DATA });
      if (!file || !file.data) return;

      const bytes = base64ToBytes(file.data);
      const legacyDb = new SQL.Database(bytes);

      const legacyRows = (sql) => {
        const statement = legacyDb.prepare(sql);
        const result = [];
        while (statement.step()) result.push(statement.getAsObject());
        statement.free();
        return result;
      };

      const safeQuery = (sql) => {
        try { return legacyRows(sql); } catch (_) { return []; }
      };

      const legacyClasses = safeQuery('SELECT * FROM classes');
      const legacySets = safeQuery('SELECT * FROM sets');
      const legacyCards = safeQuery('SELECT * FROM cards');
      const legacySettings = safeQuery('SELECT * FROM settings');
      const legacyProgress = safeQuery('SELECT * FROM progress');
      const legacyState = safeQuery('SELECT * FROM state');

      console.log(`[mobile-store] Migration counts: Classes=${legacyClasses.length}, Sets=${legacySets.length}, Cards=${legacyCards.length}`);

      await db.execute('BEGIN TRANSACTION;');
      try {
        for (const item of legacyClasses) {
          await db.run(
            'INSERT INTO classes (id, name, color, created, last_modified, deleted_at, payload_json) VALUES (?, ?, ?, ?, ?, ?, ?)',
            [item.id, item.name, item.color, item.created, item.last_modified, item.deleted_at, item.payload_json]
          );
        }
        for (const item of legacySets) {
          await db.run(
            'INSERT INTO sets (id, name, description, class_id, srs_settings_json, created, opened_count, last_opened, last_modified, deleted_at, payload_json) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            [item.id, item.name, item.description, item.class_id, item.srs_settings_json, item.created, item.opened_count, item.last_opened, item.last_modified, item.deleted_at, item.payload_json]
          );
        }
        for (const item of legacyCards) {
          await db.run(
            'INSERT INTO cards (id, set_id, position, term, definition, term_image, definition_image, tags_json, suspended, buried_until, srs_json, review_history_json, created, last_modified, deleted_at, payload_json) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            [item.id, item.set_id, item.position, item.term, item.definition, item.term_image, item.definition_image, item.tags_json, item.suspended, item.buried_until, item.srs_json, item.review_history_json, item.created, item.last_modified, item.deleted_at, item.payload_json]
          );
        }
        for (const item of legacySettings) {
          await db.run(
            'INSERT INTO settings (key, value_json, updated_at) VALUES (?, ?, ?)',
            [item.key, item.value_json, item.updated_at]
          );
        }
        for (const item of legacyProgress) {
          await db.run(
            'INSERT INTO progress (set_id, value_json, updated_at) VALUES (?, ?, ?)',
            [item.set_id, item.value_json, item.updated_at]
          );
        }
        for (const item of legacyState) {
          await db.run(
            'INSERT INTO state (key, value_json, updated_at) VALUES (?, ?, ?)',
            [item.key, item.value_json, item.updated_at]
          );
        }
        await db.execute('COMMIT;');
        console.log('[mobile-store] Migration transaction committed successfully.');
      } catch (err) {
        await db.execute('ROLLBACK;');
        throw err;
      }

      legacyDb.close();

      // Rename legacy database file to prevent running migration again
      await Filesystem.rename({
        from: DB_PATH,
        to: DB_PATH + '.migrated',
        directory: DIRECTORY_DATA
      });

      // Also delete the tmp file if it exists
      await Filesystem.deleteFile({
        path: DB_TMP_PATH,
        directory: DIRECTORY_DATA
      }).catch(() => {});

      console.log('[mobile-store] Legacy database migration complete!');
    } catch (error) {
      console.error('[mobile-store] Error during legacy database migration:', error);
    }
  }

  async function createSchema() {
    await executeRaw(`
      PRAGMA foreign_keys = ON;

      CREATE TABLE IF NOT EXISTS classes (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        color TEXT NOT NULL,
        created INTEGER NOT NULL,
        last_modified INTEGER NOT NULL,
        deleted_at INTEGER,
        payload_json TEXT NOT NULL
      );

      CREATE TABLE IF NOT EXISTS sets (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT,
        class_id TEXT,
        srs_settings_json TEXT NOT NULL,
        created INTEGER NOT NULL,
        opened_count INTEGER NOT NULL DEFAULT 0,
        last_opened INTEGER,
        last_modified INTEGER NOT NULL,
        deleted_at INTEGER,
        payload_json TEXT NOT NULL
      );

      CREATE TABLE IF NOT EXISTS cards (
        id TEXT PRIMARY KEY,
        set_id TEXT NOT NULL,
        position INTEGER NOT NULL,
        term TEXT,
        definition TEXT,
        term_image TEXT,
        definition_image TEXT,
        tags_json TEXT NOT NULL,
        suspended INTEGER NOT NULL DEFAULT 0,
        buried_until TEXT,
        srs_json TEXT,
        review_history_json TEXT NOT NULL,
        created INTEGER,
        last_modified INTEGER,
        deleted_at INTEGER,
        payload_json TEXT NOT NULL,
        FOREIGN KEY (set_id) REFERENCES sets(id) ON DELETE CASCADE
      );

      CREATE TABLE IF NOT EXISTS settings (
        key TEXT PRIMARY KEY,
        value_json TEXT NOT NULL,
        updated_at INTEGER NOT NULL
      );

      CREATE TABLE IF NOT EXISTS progress (
        set_id TEXT PRIMARY KEY,
        value_json TEXT NOT NULL,
        updated_at INTEGER NOT NULL
      );

      CREATE TABLE IF NOT EXISTS state (
        key TEXT PRIMARY KEY,
        value_json TEXT NOT NULL,
        updated_at INTEGER NOT NULL
      );

      CREATE INDEX IF NOT EXISTS idx_mobile_sets_visible ON sets(deleted_at, last_modified);
      CREATE INDEX IF NOT EXISTS idx_mobile_sets_class ON sets(class_id);
      CREATE INDEX IF NOT EXISTS idx_mobile_cards_set_position ON cards(set_id, position);
    `);
  }

  function isMissingFileError(error) {
    const message = String(error?.message || error || '').toLowerCase();
    return message.includes('not exist')
      || message.includes('not found')
      || message.includes('enoent')
      || message.includes('no such file');
  }

  function probeDatabase(candidate) {
    candidate.exec('SELECT count(*) FROM sqlite_master;');
    const integrity = candidate.exec('PRAGMA integrity_check;');
    const firstValue = integrity?.[0]?.values?.[0]?.[0];
    if (firstValue && String(firstValue).toLowerCase() !== 'ok') {
      throw new Error(`SQLite integrity check failed: ${firstValue}`);
    }
    const tables = candidate.exec("SELECT name FROM sqlite_master WHERE type='table';");
    const tableNames = tables?.[0]?.values?.map(val => val[0]) || [];
    if (tableNames.length === 0 || !tableNames.includes('sets')) {
      throw new Error('Database is empty or missing core tables.');
    }
  }

  const DB_TMP_PATH = DB_PATH + '.tmp';
  let _persistTimer = null;
  let _persistInFlight = null;
  let _persistQueued = false;
  let _clearStudyPatchesAfterPersist = false;

  function shouldDeferHeavyPersist() {
    return document.documentElement.classList.contains('study-session-active') && !document.hidden;
  }

  async function _doPersist() {
    if (isNative) return;
    const bytes = db.export();
    const data = bytesToBase64(bytes);
    // Write to temp file first (safety net if main write is interrupted)
    await Filesystem.writeFile({
      path: DB_TMP_PATH,
      data,
      directory: DIRECTORY_DATA,
      recursive: true
    });
    // Now write the main file
    await Filesystem.writeFile({
      path: DB_PATH,
      data,
      directory: DIRECTORY_DATA,
      recursive: true
    });
    // Clean up temp
    try {
      await Filesystem.deleteFile({ path: DB_TMP_PATH, directory: DIRECTORY_DATA });
    } catch (_) {}
    if (_clearStudyPatchesAfterPersist) {
      try { localStorage.removeItem(STUDY_PATCHES_KEY); } catch (_) {}
      _clearStudyPatchesAfterPersist = false;
    }
  }

  async function persist(delayMs = 2000) {
    if (isNative) return Promise.resolve();
    // If a write is already scheduled, just mark queued and return the existing promise
    if (_persistTimer) {
      _persistQueued = true;
      return _persistInFlight || Promise.resolve();
    }

    return new Promise((resolve, reject) => {
      _persistTimer = setTimeout(async () => {
        _persistTimer = null;
        _persistQueued = false;

        if (shouldDeferHeavyPersist()) {
          persist(Math.max(1800, Math.min(Number(delayMs) || 2000, 2600))).then(resolve, reject);
          return;
        }

        // Wait for any in-flight write to finish first
        if (_persistInFlight) {
          try { await _persistInFlight; } catch (_) {}
        }

        _persistInFlight = _doPersist();
        try {
          await _persistInFlight;
          resolve();
        } catch (error) {
          console.error('[mobile-store] persist failed:', error);
          reject(error);
        } finally {
          _persistInFlight = null;
          // If more writes were queued while this one was running, flush again
          if (_persistQueued) {
            _persistQueued = false;
            persist(delayMs).catch(() => {});
          }
        }
      }, Math.max(0, Number(delayMs) || 2000));
    });
  }

  /** Await any in-flight or scheduled persist. Call before navigation. */
  async function flush() {
    if (isNative) return;
    if (_persistTimer) {
      clearTimeout(_persistTimer);
      _persistTimer = null;
      _persistQueued = false;
      if (_persistInFlight) {
        try { await _persistInFlight; } catch (_) {}
      }
      _persistInFlight = _doPersist();
      try { await _persistInFlight; } catch (_) {}
      _persistInFlight = null;
    } else if (_persistInFlight) {
      try { await _persistInFlight; } catch (_) {}
    }
  }

  async function updateCardProgressRow(setId, cardId, patch = {}) {
    const setKey = String(setId);
    const cardKey = String(cardId);
    const result = await rows(
      'SELECT payload_json FROM cards WHERE id = ? AND set_id = ? AND deleted_at IS NULL',
      [cardKey, setKey]
    );
    if (!result.length) return false;

    const existing = jsonParse(result[0].payload_json, {});
    const updated = {
      ...existing,
      lastModified: Number(patch.lastModified || Date.now())
    };

    if (Object.prototype.hasOwnProperty.call(patch, 'srs')) updated.srs = patch.srs || undefined;
    if (Object.prototype.hasOwnProperty.call(patch, 'reviewHistory')) {
      updated.reviewHistory = Array.isArray(patch.reviewHistory) ? patch.reviewHistory : [];
    }
    if (Object.prototype.hasOwnProperty.call(patch, 'suspended')) updated.suspended = Boolean(patch.suspended);
    if (Object.prototype.hasOwnProperty.call(patch, 'buriedUntil')) updated.buriedUntil = patch.buriedUntil || null;

    await run(`
      UPDATE cards SET
        srs_json = ?,
        review_history_json = ?,
        suspended = ?,
        buried_until = ?,
        last_modified = ?,
        payload_json = ?
      WHERE id = ? AND set_id = ?
    `, [
      jsonString(updated.srs || null),
      jsonString(Array.isArray(updated.reviewHistory) ? updated.reviewHistory : []),
      updated.suspended ? 1 : 0,
      updated.buriedUntil || null,
      updated.lastModified,
      jsonString(updated),
      cardKey,
      setKey
    ]);

    await run('UPDATE sets SET last_modified = ? WHERE id = ? AND deleted_at IS NULL', [updated.lastModified, setKey]);
    return true;
  }

  async function applyPendingStudyPatches() {
    let payload = null;
    try {
      payload = JSON.parse(localStorage.getItem(STUDY_PATCHES_KEY) || 'null');
    } catch (_) {
      payload = null;
    }
    if (!payload || !payload.sets || typeof payload.sets !== 'object') return false;

    let changed = false;
    for (const [setId, setPatch] of Object.entries(payload.sets)) {
      for (const [cardId, cardPatch] of Object.entries(setPatch?.cards || {})) {
        if (await updateCardProgressRow(setId, cardId, cardPatch)) changed = true;
      }
    }

    if (changed) _clearStudyPatchesAfterPersist = true;
    return changed;
  }

  async function init() {
    if (readyPromise) return readyPromise;

    readyPromise = (async () => {
      const scriptBase = (() => {
        try {
          const scripts = document.querySelectorAll('script[src*="mobile-store"]');
          const src = scripts[scripts.length - 1]?.src || '';
          return src.substring(0, src.lastIndexOf('/js/mobile/'));
        } catch (_e) { return ''; }
      })();
      const wasmBase = scriptBase ? `${scriptBase}/vendor/sql.js/` : 'vendor/sql.js/';
      SQL = await initSqlJs({
        locateFile: file => `${wasmBase}${file}`
      });

      db = null;
      let foundExistingFile = false;
      let openedFromTemp = false;
      let lastOpenError = null;

      if (isNative) {
        try {
          const sqlite = new SQLiteConnection(CapacitorSQLite);
          const dbName = 'erudite_flashcards';

          const retCC = (await sqlite.checkConnectionsConsistency()).result;
          const isConn = (await sqlite.isConnection(dbName, false)).result;
          if (retCC && isConn) {
            db = await sqlite.retrieveConnection(dbName, false);
          } else {
            db = await sqlite.createConnection(dbName, false, 'no-encryption', 1, false);
          }
          await db.open();
        } catch (error) {
          console.error('[mobile-store] Failed to open native SQLite database:', error);
          lastOpenError = error;
        }
      }

      if (isNative && db) {
        await createSchema();
        await migrateFromLegacySqlJs();
      } else {
        // Fallback to WebAssembly SQL.js
        for (const path of [DB_PATH, DB_TMP_PATH]) {
          if (db) break;
          try {
            const file = await Filesystem.readFile({ path, directory: DIRECTORY_DATA });
            foundExistingFile = true;
            const candidate = new SQL.Database(base64ToBytes(file.data));
            probeDatabase(candidate);
            db = candidate;
            openedFromTemp = path === DB_TMP_PATH;
          } catch (error) {
            if (!isMissingFileError(error)) {
              foundExistingFile = true;
              lastOpenError = error;
            }
            console.warn(`[mobile-store] Could not open ${path}:`, error?.message || error);
          }
        }

        const isFresh = !db;
        if (!db) {
          if (foundExistingFile) {
            throw new Error(`Local database could not be opened safely. Existing data was not overwritten. ${lastOpenError?.message || ''}`.trim());
          }
          console.warn('[mobile-store] Starting with empty database');
          db = new SQL.Database();
        }

        await createSchema();
        const recoveredClassBackups = await recoverLocalClassBackupsIfEmptyOrMissing();
        const recoveredLocalBackups = await recoverLocalSetBackupsIfEmpty();
        const repairedOrphans = await repairOrphanedClassIds();
        const appliedStudyPatches = await applyPendingStudyPatches();
        // Only persist on first-time setup to avoid a costly full write on every cold start
        if (isFresh) await _doPersist();
        else if (openedFromTemp) await _doPersist();
        else if (recoveredClassBackups || recoveredLocalBackups || repairedOrphans) await _doPersist();
        else if (appliedStudyPatches) persist(2500).catch(() => {});
      }
      return true;
    })();

    return readyPromise;
  }

  async function ensureReady() {
    await init();
  }

  async function listClasses() {
    await ensureReady();
    const result = await rows('SELECT * FROM classes WHERE deleted_at IS NULL ORDER BY name ASC');
    const classes = result.map(row => ({
      ...jsonParse(row.payload_json, {}),
      id: row.id,
      name: row.name,
      color: row.color,
      created: Number(row.created),
      lastModified: Number(row.last_modified)
    }));
    classes.forEach(rememberClassBackup);
    return classes;
  }

  async function upsertClass(classData) {
    await run(`
      INSERT INTO classes (id, name, color, created, last_modified, deleted_at, payload_json)
      VALUES (?, ?, ?, ?, ?, NULL, ?)
      ON CONFLICT(id) DO UPDATE SET
        name = excluded.name,
        color = excluded.color,
        created = excluded.created,
        last_modified = excluded.last_modified,
        deleted_at = NULL,
        payload_json = excluded.payload_json
    `, [
      String(classData.id),
      classData.name,
      classData.color,
      Number(classData.created || Date.now()),
      Number(classData.lastModified || Date.now()),
      jsonString(classData)
    ]);
  }

  async function saveClass(classData) {
    await ensureReady();
    const existing = (await listClasses()).find(item => String(item.id) === String(classData.id));
    const normalized = schema.normalizeClass(classData, existing);
    await upsertClass(normalized);
    rememberClassBackup(normalized);
    await persist();
    return normalized;
  }

  async function replaceClasses(classes = [], options = {}) {
    await ensureReady();
    const now = Date.now();
    await executeRaw(`UPDATE classes SET deleted_at = ${now}, last_modified = ${now} WHERE deleted_at IS NULL;`);
    clearClassBackups();
    for (const classData of Array.isArray(classes) ? classes : []) {
      const normalized = schema.normalizeClass(classData, null, { preserveLastModified: true });
      await upsertClass(normalized);
      rememberClassBackup(normalized);
    }
    if (options.persist !== false) await persist();
    return listClasses();
  }

  async function deleteClass(classId) {
    await ensureReady();
    const now = Date.now();
    await run('UPDATE classes SET deleted_at = ?, last_modified = ? WHERE id = ?', [now, now, String(classId)]);
    await run('UPDATE sets SET class_id = NULL, last_modified = ? WHERE class_id = ? AND deleted_at IS NULL', [now, String(classId)]);
    forgetClassBackup(classId);
    await persist();
    return true;
  }

  async function upsertSet(set) {
    const payload = { ...set, cards: undefined };
    await run(`
      INSERT INTO sets (
        id, name, description, class_id, srs_settings_json, created,
        opened_count, last_opened, last_modified, deleted_at, payload_json
      )
      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, NULL, ?)
      ON CONFLICT(id) DO UPDATE SET
        name = excluded.name,
        description = excluded.description,
        class_id = excluded.class_id,
        srs_settings_json = excluded.srs_settings_json,
        created = excluded.created,
        opened_count = excluded.opened_count,
        last_opened = excluded.last_opened,
        last_modified = excluded.last_modified,
        deleted_at = NULL,
        payload_json = excluded.payload_json
    `, [
      String(set.id),
      set.name,
      set.description || '',
      set.classId || null,
      jsonString(set.srsSettings || {}),
      Number(set.created || Date.now()),
      Number(set.openedCount || 0),
      set.lastOpened ?? null,
      Number(set.lastModified || Date.now()),
      jsonString(payload)
    ]);
  }

  async function replaceCardsForSet(setId, cards = []) {
    const set = [
      { statement: 'DELETE FROM cards WHERE set_id = ?', values: [String(setId)] }
    ];
    for (let index = 0; index < cards.length; index++) {
      const card = cards[index];
      set.push({
        statement: `
          INSERT INTO cards (
            id, set_id, position, term, definition, term_image, definition_image,
            tags_json, suspended, buried_until, srs_json, review_history_json,
            created, last_modified, deleted_at, payload_json
          )
          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, NULL, ?)
        `,
        values: [
          String(card.id),
          String(setId),
          index,
          card.term || '',
          card.definition || '',
          card.termImage || '',
          card.definitionImage || '',
          jsonString(Array.isArray(card.tags) ? card.tags : []),
          card.suspended ? 1 : 0,
          card.buriedUntil || null,
          jsonString(card.srs || null),
          jsonString(Array.isArray(card.reviewHistory) ? card.reviewHistory : []),
          card.created || null,
          card.lastModified || null,
          jsonString(card)
        ]
      });
    }
    await executeSet(set);
  }

  async function listSets() {
    await ensureReady();
    const setRows = await rows('SELECT * FROM sets WHERE deleted_at IS NULL ORDER BY last_modified DESC, created DESC');
    const sets = [];
    for (const row of setRows) {
      sets.push(await hydrateSetRow(row));
    }
    sets.forEach(rememberSetBackup);
    return sets;
  }

  async function hydrateSetRow(row) {
    const payload = jsonParse(row.payload_json, {});
    const cardRows = await rows(
      'SELECT * FROM cards WHERE set_id = ? AND deleted_at IS NULL ORDER BY position ASC',
      [row.id]
    );
    const cards = cardRows.map(cardRow => hydrateCardRow(cardRow));

    return {
      ...payload,
      id: row.id,
      name: row.name,
      description: row.description || '',
      classId: row.class_id || null,
      srsSettings: jsonParse(row.srs_settings_json, {}),
      created: Number(row.created),
      openedCount: Number(row.opened_count || 0),
      lastOpened: row.last_opened ?? null,
      lastModified: Number(row.last_modified),
      cards
    };
  }

  function hydrateSetMetaRow(row) {
    const payload = jsonParse(row.payload_json, {});
    return {
      ...payload,
      id: row.id,
      name: row.name,
      description: row.description || '',
      classId: row.class_id || null,
      srsSettings: jsonParse(row.srs_settings_json, {}),
      created: Number(row.created),
      openedCount: Number(row.opened_count || 0),
      lastOpened: row.last_opened ?? null,
      lastModified: Number(row.last_modified)
    };
  }

  async function getSetMeta(id) {
    await ensureReady();
    const setRows = await rows('SELECT * FROM sets WHERE id = ? AND deleted_at IS NULL', [String(id)]);
    return setRows.length ? hydrateSetMetaRow(setRows[0]) : null;
  }

  function hydrateCardRow(cardRow) {
    return {
      ...jsonParse(cardRow.payload_json, {}),
      id: cardRow.id,
      term: cardRow.term || '',
      definition: cardRow.definition || '',
      termImage: cardRow.term_image || '',
      definitionImage: cardRow.definition_image || '',
      tags: jsonParse(cardRow.tags_json, []),
      suspended: Boolean(cardRow.suspended),
      buriedUntil: cardRow.buried_until || null,
      srs: jsonParse(cardRow.srs_json, null) || undefined,
      reviewHistory: jsonParse(cardRow.review_history_json, [])
    };
  }

  /** Lightweight listing — returns set metadata + card count, NO card data loaded. */
  function createMetaStats() {
    return {
      totalCards: 0,
      newCards: 0,
      dueCards: 0,
      reviewDueCards: 0,
      learningCards: 0,
      reviewCards: 0,
      relearningCards: 0,
      matureCards: 0,
      reviewCount: 0,
      reviewedToday: 0,
      remembered30: 0,
      reviewed30: 0,
      retention: null,
      nextDue: null,
      lastReviewAt: null,
      reviewDayKeys: []
    };
  }

  function normalizeSrsState(value) {
    if (typeof value === 'number') {
      return ['New', 'Learning', 'Review', 'Relearning'][value] || 'New';
    }
    return value || 'New';
  }

  function timeValue(value) {
    if (!value) return 0;
    const number = Number(value);
    if (Number.isFinite(number) && number > 0) return number;
    const date = new Date(value);
    return Number.isNaN(date.getTime()) ? 0 : date.getTime();
  }

  function dayKey(value) {
    const timestamp = timeValue(value);
    if (!timestamp) return null;
    const date = new Date(timestamp);
    date.setHours(0, 0, 0, 0);
    return String(date.getTime());
  }

  function isBuried(buriedUntil, nowMs) {
    const until = timeValue(buriedUntil);
    return until > nowMs;
  }

  function isSrsDue(srs, nowMs) {
    if (!srs || !srs.due) return true;
    const due = timeValue(srs.due);
    return !due || due <= nowMs;
  }

  async function buildMetaStatsBySet() {
    const nowMs = Date.now();
    const todayKey = dayKey(nowMs);
    const thirtyDaysAgo = nowMs - 30 * 24 * 60 * 60 * 1000;
    const statsBySet = new Map();
    const dayKeysBySet = new Map();

    const cardRows = await rows(`
      SELECT c.set_id, c.srs_json, c.review_history_json, c.suspended, c.buried_until
      FROM cards c
      INNER JOIN sets s ON s.id = c.set_id
      WHERE c.deleted_at IS NULL AND s.deleted_at IS NULL
    `);

    cardRows.forEach(row => {
      const setId = String(row.set_id);
      const stats = statsBySet.get(setId) || createMetaStats();
      const dayKeys = dayKeysBySet.get(setId) || new Set();
      const history = jsonParse(row.review_history_json, []);

      (Array.isArray(history) ? history : []).forEach(review => {
        const reviewedAt = timeValue(review.reviewedAt || review.time || review.date);
        if (!reviewedAt) return;
        stats.reviewCount += 1;
        if (!stats.lastReviewAt || reviewedAt > stats.lastReviewAt) stats.lastReviewAt = reviewedAt;
        const key = dayKey(reviewedAt);
        if (key) dayKeys.add(key);
        if (key === todayKey) stats.reviewedToday += 1;
        if (reviewedAt >= thirtyDaysAgo) {
          stats.reviewed30 += 1;
          if (String(review.rating || '').toLowerCase() !== 'again') stats.remembered30 += 1;
        }
      });

      if (!Number(row.suspended || 0) && !isBuried(row.buried_until, nowMs)) {
        stats.totalCards += 1;
        const srs = jsonParse(row.srs_json, null);
        const state = normalizeSrsState(srs?.state);

        if (!srs || state === 'New') {
          stats.newCards += 1;
          stats.dueCards += 1;
        } else {
          if (state === 'Learning') stats.learningCards += 1;
          if (state === 'Review') stats.reviewCards += 1;
          if (state === 'Relearning') stats.relearningCards += 1;

          if (isSrsDue(srs, nowMs)) {
            stats.dueCards += 1;
            stats.reviewDueCards += 1;
          } else if (state === 'Review') {
            stats.matureCards += 1;
          }
        }

        const dueTime = timeValue(srs?.due);
        if (dueTime && (!stats.nextDue || dueTime < stats.nextDue)) stats.nextDue = dueTime;
      }

      statsBySet.set(setId, stats);
      dayKeysBySet.set(setId, dayKeys);
    });

    statsBySet.forEach((stats, setId) => {
      stats.reviewDayKeys = Array.from(dayKeysBySet.get(setId) || []);
      stats.retention = stats.reviewed30 > 0 ? Math.round((stats.remembered30 / stats.reviewed30) * 100) : null;
    });

    return statsBySet;
  }

  function dailyLimit(value) {
    if (value === null || value === undefined || value === '') return null;
    const number = Number(value);
    return Number.isFinite(number) ? Math.max(0, Math.round(number)) : null;
  }

  function limitedDueCount(stats, settings = {}) {
    if (settings.enabled === false) return 0;
    const newLimit = dailyLimit(settings.newCardsPerDay);
    const reviewLimit = dailyLimit(settings.reviewsPerDay);
    const newDue = Number(stats.newCards || 0);
    const reviewDue = Number(stats.reviewDueCards ?? Math.max(0, Number(stats.dueCards || 0) - newDue));
    return (newLimit === null ? newDue : Math.min(newDue, newLimit))
      + (reviewLimit === null ? reviewDue : Math.min(reviewDue, reviewLimit));
  }

  async function listSetsMeta() {
    await ensureReady();
    const statsBySet = await buildMetaStatsBySet();
    const setRows = await rows(`
      SELECT s.*,
        (SELECT COUNT(*) FROM cards c WHERE c.set_id = s.id AND c.deleted_at IS NULL) AS card_count
      FROM sets s
      WHERE s.deleted_at IS NULL
      ORDER BY s.last_modified DESC, s.created DESC
    `);
    return setRows.map(row => {
      const payload = jsonParse(row.payload_json, {});
      const settings = jsonParse(row.srs_settings_json, {});
      const stats = {
        ...createMetaStats(),
        ...(statsBySet.get(String(row.id)) || {}),
        totalCards: Number(row.card_count || 0)
      };
      stats.dueCards = limitedDueCount(stats, settings);
      return {
        ...payload,
        id: row.id,
        name: row.name,
        description: row.description || '',
        classId: row.class_id || null,
        srsSettings: settings,
        created: Number(row.created),
        openedCount: Number(row.opened_count || 0),
        lastOpened: row.last_opened ?? null,
        lastModified: Number(row.last_modified),
        cardCount: Number(row.card_count || 0),
        mobileStats: stats,
        __metaOnly: true,
        cards: [] // empty — use getSet(id) when you need cards
      };
    });
  }

  async function getSet(id) {
    await ensureReady();
    const setRows = await rows('SELECT * FROM sets WHERE id = ? AND deleted_at IS NULL', [String(id)]);
    if (!setRows.length) return null;
    const set = await hydrateSetRow(setRows[0]);
    rememberSetBackup(set);
    return set;
  }

  async function saveSet(set) {
    await ensureReady();
    const hasCardsField = Object.prototype.hasOwnProperty.call(set || {}, 'cards');
    const wantsMetaOnly = Boolean(set?.__metaOnly) || !hasCardsField;
    const existing = set.id
      ? (wantsMetaOnly ? await getSetMeta(set.id) : await getSet(set.id))
      : null;
    const metaOnlyUpdate = Boolean(set?.__metaOnly)
      || (existing && !hasCardsField)
      || (existing && hasCardsField && Array.isArray(set.cards) && set.cards.length === 0 && Number(set.cardCount || 0) > 0);
    const { mobileStats: _mobileStats, __metaOnly: _metaOnly, cardCount: _cardCount, ...cleanSet } = set || {};

    if (metaOnlyUpdate && existing) {
      const hasOwn = key => Object.prototype.hasOwnProperty.call(cleanSet, key);
      const next = {
        ...existing,
        ...cleanSet,
        id: existing.id,
        name: hasOwn('name') ? (String(cleanSet.name || existing.name || 'Untitled Set').trim() || 'Untitled Set') : existing.name,
        description: hasOwn('description') ? (cleanSet.description || '') : (existing.description || ''),
        classId: hasOwn('classId') ? (cleanSet.classId || null) : (existing.classId || null),
        srsSettings: schema.normalizeSrsSettings(cleanSet.srsSettings || existing.srsSettings || {}),
        created: existing.created || Date.now(),
        openedCount: hasOwn('openedCount') ? Number(cleanSet.openedCount || 0) : Number(existing.openedCount || 0),
        lastOpened: hasOwn('lastOpened') ? (cleanSet.lastOpened ?? null) : (existing.lastOpened ?? null),
        lastModified: hasOwn('lastModified') ? Number(cleanSet.lastModified || Date.now()) : Number(existing.lastModified || Date.now())
      };
      const payload = { ...next };
      delete payload.cards;
      delete payload.mobileStats;
      delete payload.cardCount;
      delete payload.__metaOnly;
      await run(`
        UPDATE sets
        SET name = ?, description = ?, class_id = ?, srs_settings_json = ?,
            opened_count = ?, last_opened = ?, last_modified = ?, payload_json = ?, deleted_at = NULL
        WHERE id = ?
      `, [
        next.name,
        next.description || '',
        next.classId || null,
        jsonString(next.srsSettings || {}),
        Number(next.openedCount || 0),
        next.lastOpened ?? null,
        Number(next.lastModified || Date.now()),
        jsonString(payload),
        String(existing.id)
      ]);
      await persist();
      return { ...next, cards: [], __metaOnly: true };
    }

    const normalized = schema.normalizeSet(cleanSet, existing);
    await upsertSet(normalized);
    if (!metaOnlyUpdate) await replaceCardsForSet(normalized.id, normalized.cards || []);
    if (!metaOnlyUpdate) rememberSetBackup(normalized);
    await persist(); // fire-and-forget — flush() ensures it completes before navigation
    return normalized;
  }

  async function replaceSets(sets = [], options = {}) {
    await ensureReady();
    const now = Date.now();
    await executeRaw(`UPDATE sets SET deleted_at = ${now}, last_modified = ${now} WHERE deleted_at IS NULL;`);
    clearSetBackups();
    for (const set of Array.isArray(sets) ? sets : []) {
      const normalized = schema.normalizeSet(set, null, { preserveLastModified: true });
      await upsertSet(normalized);
      await replaceCardsForSet(normalized.id, normalized.cards || []);
      rememberSetBackup(normalized);
    }
    if (options.persist !== false) await persist();
    return listSets();
  }

  async function deleteSet(id) {
    await ensureReady();
    const now = Date.now();
    await run('UPDATE sets SET deleted_at = ?, last_modified = ? WHERE id = ?', [now, now, String(id)]);
    await run('DELETE FROM progress WHERE set_id = ?', [String(id)]);
    forgetSetBackup(id);
    await persist();
    return true;
  }

  async function getSettings() {
    await ensureReady();
    const result = await rows('SELECT value_json FROM settings WHERE key = ?', ['app']);
    return schema.normalizeSettings(jsonParse(result[0]?.value_json, {}));
  }

  async function saveSettings(settings = {}) {
    await ensureReady();
    await run('INSERT OR REPLACE INTO settings (key, value_json, updated_at) VALUES (?, ?, ?)', [
      'app',
      jsonString(schema.normalizeSettings(settings)),
      Date.now()
    ]);
    await persist();
    return true;
  }

  async function getProgress(setId) {
    await ensureReady();
    const result = await rows('SELECT value_json FROM progress WHERE set_id = ?', [String(setId)]);
    return jsonParse(result[0]?.value_json, null);
  }

  async function saveProgress(setId, value) {
    await ensureReady();
    await run('INSERT OR REPLACE INTO progress (set_id, value_json, updated_at) VALUES (?, ?, ?)', [
      String(setId),
      jsonString(value),
      Date.now()
    ]);
    await persist(); // fire-and-forget — flush() ensures completion before navigation
    return true;
  }

  async function saveCardProgress(setId, cardId, patch = {}) {
    await ensureReady();
    await updateCardProgressRow(setId, cardId, patch);
    await persist(12000);
    return true;
  }

  async function getAllProgress() {
    const progress = {};
    const result = await rows('SELECT set_id, value_json FROM progress');
    result.forEach(row => {
      progress[row.set_id] = jsonParse(row.value_json, null);
    });
    return progress;
  }

  async function replaceProgress(progress = {}, options = {}) {
    await ensureReady();
    const set = [
      { statement: 'DELETE FROM progress;', values: [] }
    ];
    for (const [setId, value] of Object.entries(progress || {})) {
      set.push({
        statement: 'INSERT OR REPLACE INTO progress (set_id, value_json, updated_at) VALUES (?, ?, ?)',
        values: [String(setId), jsonString(value), Date.now()]
      });
    }
    await executeSet(set);
    if (options.persist !== false) await persist();
    return true;
  }

  async function getState(key) {
    await ensureReady();
    const result = await rows('SELECT value_json FROM state WHERE key = ?', [String(key)]);
    return jsonParse(result[0]?.value_json, null);
  }

  async function setState(key, value) {
    await ensureReady();
    await run('INSERT OR REPLACE INTO state (key, value_json, updated_at) VALUES (?, ?, ?)', [
      String(key),
      jsonString(value),
      Date.now()
    ]);
    await persist();
    return true;
  }

  async function removeState(key) {
    await ensureReady();
    await run('DELETE FROM state WHERE key = ?', [String(key)]);
    await persist();
    return true;
  }

  async function getAllState() {
    const state = {};
    const result = await rows('SELECT key, value_json FROM state');
    result.forEach(row => {
      state[row.key] = jsonParse(row.value_json, null);
    });
    return state;
  }

  async function replaceState(state = {}, options = {}) {
    await ensureReady();
    const set = [
      { statement: 'DELETE FROM state;', values: [] }
    ];
    for (const [key, value] of Object.entries(state || {})) {
      set.push({
        statement: 'INSERT OR REPLACE INTO state (key, value_json, updated_at) VALUES (?, ?, ?)',
        values: [String(key), jsonString(value), Date.now()]
      });
    }
    await executeSet(set);
    if (options.persist !== false) await persist();
    return true;
  }

  async function createBackupSnapshot(reason = 'snapshot') {
    await ensureReady();
    const payload = await createBackupPayload();
    const fileName = `${reason}-${new Date().toISOString().replace(/[:.]/g, '-')}.json`;
    await Filesystem.writeFile({
      path: `${BACKUP_DIR}/${fileName}`,
      data: JSON.stringify(payload, null, 2),
      directory: DIRECTORY_DATA,
      encoding: ENCODING_UTF8,
      recursive: true
    });
  }

  async function createBackupPayload() {
    await ensureReady();
    return backup.createBackupPayload({
      sets: await listSets(),
      classes: await listClasses(),
      settings: await getSettings(),
      progress: await getAllProgress(),
      state: await getAllState()
    });
  }

  function pickJsonFile() {
    return new Promise((resolve) => {
      const input = document.createElement('input');
      input.type = 'file';
      input.accept = 'application/json,.json';
      input.style.display = 'none';
      input.addEventListener('change', () => {
        const file = input.files?.[0] || null;
        input.remove();
        resolve(file);
      }, { once: true });
      document.body.appendChild(input);
      input.click();
    });
  }

  async function resetDeckSRS(setId, deleteHistory) {
    await ensureReady();
    const cardRows = await rows('SELECT * FROM cards WHERE set_id = ? AND deleted_at IS NULL', [String(setId)]);

    for (const cardRow of cardRows) {
      const card = hydrateCardRow(cardRow);
      card.srs = undefined;
      if (deleteHistory) {
        card.reviewHistory = [];
      }

      await run(
        'UPDATE cards SET srs_json = NULL, review_history_json = ?, payload_json = ?, last_modified = ? WHERE id = ?',
        [
          jsonString(card.reviewHistory),
          jsonString(card),
          Date.now(),
          String(card.id)
        ]
      );
    }

    // Reset SRS progress inside progress table
    const progressRows = await rows('SELECT value_json FROM progress WHERE set_id = ?', [String(setId)]);
    if (progressRows.length) {
      const progress = jsonParse(progressRows[0].value_json, {});
      progress.srsModeIndex = 0;
      progress.srsReviewedCardIds = [];
      progress.timestamp = Date.now();

      await run(
        'UPDATE progress SET value_json = ?, updated_at = ? WHERE set_id = ?',
        [
          jsonString(progress),
          Date.now(),
          String(setId)
        ]
      );
    }

    await persist();
    return true;
  }

  async function exportBackup() {
    const payload = await createBackupPayload();
    const fileName = `erudite-flashcards-backup-${new Date().toISOString().slice(0, 10)}.json`;
    const result = await Filesystem.writeFile({
      path: `${BACKUP_DIR}/${fileName}`,
      data: JSON.stringify(payload, null, 2),
      directory: DIRECTORY_DOCUMENTS,
      encoding: ENCODING_UTF8,
      recursive: true
    });

    if (Share?.share && result?.uri) {
      await Share.share({
        title: 'Erudite Flashcards Backup',
        text: 'Erudite Flashcards backup',
        url: result.uri,
        dialogTitle: 'Save or share backup'
      }).catch(() => {});
    }

    return {
      canceled: false,
      filePath: result?.uri || fileName,
      setCount: payload.data.sets.length
    };
  }

  async function importBackup() {
    const file = await pickJsonFile();
    if (!file) return { canceled: true };

    const raw = await file.text();
    const payload = JSON.parse(raw);
    const data = backup.readBackupData(payload);
    await createBackupSnapshot('before-mobile-restore');
    const restoredClasses = await replaceClasses(data.classes || [], { persist: false });
    const restoredSets = await replaceSets(data.sets || [], { persist: false });
    await saveSettings(data.settings || {});
    await replaceProgress(data.progress || {}, { persist: false });
    await replaceState(data.state || {}, { persist: false });
    await persist();

    return {
      canceled: false,
      filePath: file.name,
      setCount: restoredSets.length,
      classCount: restoredClasses.length
    };
  }

  async function saveImage(dataUrl) {
    return dataUrl;
  }

  async function deleteImage() {
    return true;
  }

  async function saveFont(dataUrl) {
    return dataUrl;
  }

  async function listPremadeSets(classId, subjectId) {
    try {
      const manifest = await fetch(`premade-cards/${classId}/${subjectId}/manifest.json`);
      if (manifest.ok) return manifest.json();
    } catch (_error) {}
    return [];
  }

  async function getPremadeSet(classId, subjectId, fileName) {
    try {
      const response = await fetch(`premade-cards/${classId}/${subjectId}/${fileName}`);
      return response.ok ? response.json() : null;
    } catch (_error) {
      return null;
    }
  }

  async function getDiagnostics() {
    await ensureReady();
    const sets = await listSets();
    const classes = await listClasses();
    return {
      appName: 'Erudite Flashcards',
      appVersion: 'mobile',
      generatedAt: new Date().toISOString(),
      storageEngine: isNative ? 'SQLite (Capacitor Native)' : 'SQLite (Capacitor WebAssembly)',
      paths: {
        database: DB_PATH,
        backupsDir: BACKUP_DIR
      },
      counts: {
        sets: sets.length,
        classes: classes.length,
        cards: sets.reduce((total, set) => total + (Array.isArray(set.cards) ? set.cards.length : 0), 0),
        progressEntries: Object.keys(await getAllProgress()).length,
        stateEntries: Object.keys(await getAllState()).length
      },
      health: {
        status: 'ok',
        issues: []
      },
      recentBackups: [],
      brokenImageLinks: []
    };
  }

  window.eruditeMobileFlashcards = {
    listSets,
    listSetsMeta,
    getSet,
    saveSet,
    replaceSets,
    deleteSet,
    resetDeckSRS,
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
    saveImage,
    deleteImage,
    saveFont,
    listPremadeSets,
    getPremadeSet,
    getDiagnostics,
    exportBackup,
    importBackup,
    exportDelimited: async () => ({ canceled: true, unsupported: true }),
    importDelimited: async () => ({ canceled: true, unsupported: true }),
    flush
  };

  window.eruditeMobileReady = init();
})();
