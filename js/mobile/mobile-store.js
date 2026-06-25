(function () {
  const capacitor = window.Capacitor;
  const plugins = capacitor?.Plugins || {};
  const Filesystem = plugins.Filesystem;
  const Share = plugins.Share;
  const schema = window.EruditeCore?.schema;
  const backup = window.EruditeCore?.backup;
  const perf = window.EruditeMobilePerf;

  if (!capacitor || !Filesystem || !schema || !backup || typeof initSqlJs === 'undefined') {
    perf?.mark('store.guard_failed', {
      capacitor: Boolean(capacitor),
      filesystem: Boolean(Filesystem),
      schema: Boolean(schema),
      backup: Boolean(backup),
      sqlJs: typeof initSqlJs !== 'undefined'
    });
    console.warn('[mobile-store] Guard failed — missing:', {
      capacitor: !!capacitor, Filesystem: !!Filesystem,
      schema: !!schema, backup: !!backup,
      initSqlJs: typeof initSqlJs !== 'undefined'
    });
    return;
  }

  const DB_PATH = 'erudite-flashcards/erudite-flashcards.sqlite';
  const BACKUP_DIR = 'erudite-flashcards/backups';
  const MEDIA_DIR = 'erudite-flashcards/media';
  const STUDY_PATCHES_KEY = 'erudite-mobile-study-card-patches-v1';
  const SET_BACKUP_PREFIX = 'erudite-mobile-set-backup:';
  const SET_BACKUP_INDEX_KEY = 'erudite-mobile-set-backup-index-v1';
  const CLASS_BACKUP_PREFIX = 'erudite-mobile-class-backup:';
  const CLASS_BACKUP_INDEX_KEY = 'erudite-mobile-class-backup-index-v1';
  const SET_STATS_CACHE_KEY = 'erudite-mobile-set-stats-cache-v1';
  const DIRECTORY_DATA = 'DATA';
  const DIRECTORY_DOCUMENTS = 'DOCUMENTS';
  const ENCODING_UTF8 = 'utf8';
  const MAX_LOCAL_SET_MIRROR_BYTES = 384 * 1024;
  const MAX_IMPORT_CARD_COUNT = 200000;

  const isNative = !!(capacitor && (capacitor.getPlatform() === 'android' || capacitor.getPlatform() === 'ios') && window.CapacitorSqliteHelper);
  const { SQLiteConnection, CapacitorSQLite } = window.CapacitorSqliteHelper || {};

  let readyPromise = null;
  let SQL = null;
  let db = null;
  let transactionDepth = 0;

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

  function readSetStatsCache() {
    try {
      const parsed = JSON.parse(localStorage.getItem(SET_STATS_CACHE_KEY) || '{}');
      return parsed && typeof parsed === 'object' ? parsed : {};
    } catch (_) {
      return {};
    }
  }

  function writeSetStatsCache(cache) {
    try {
      localStorage.setItem(SET_STATS_CACHE_KEY, JSON.stringify(cache || {}));
    } catch (_) {}
  }

  function statsCacheDayToken(nowMs = Date.now()) {
    return `${dayKey(nowMs) || ''}:${srsDayKey(nowMs) || ''}`;
  }

  function cachedStatsForSet(cache, setId, lastModified, dayToken) {
    const cached = cache?.[String(setId)];
    if (!cached) return null;
    if (Number(cached.lastModified || 0) !== Number(lastModified || 0)) return null;
    if (String(cached.dayToken || '') !== String(dayToken || '')) return null;
    return cached.stats && typeof cached.stats === 'object' ? cached.stats : null;
  }

  function removeSetStatsCacheEntry(setId) {
    const cache = readSetStatsCache();
    if (!Object.prototype.hasOwnProperty.call(cache, String(setId))) return;
    delete cache[String(setId)];
    writeSetStatsCache(cache);
  }

  function clearSetStatsCache() {
    try { localStorage.removeItem(SET_STATS_CACHE_KEY); } catch (_) {}
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
      const sampleSize = Math.min(20, set.cards.length);
      const sampleBytes = JSON.stringify(set.cards.slice(0, sampleSize)).length;
      const estimatedBytes = sampleSize
        ? Math.ceil((sampleBytes / sampleSize) * set.cards.length) + 4096
        : 0;
      if (estimatedBytes > MAX_LOCAL_SET_MIRROR_BYTES) {
        forgetSetBackup(set.id);
        return;
      }
      const normalized = schema.normalizeSet(set, null, { preserveLastModified: true });
      const serialized = JSON.stringify(normalized);
      if (serialized.length > MAX_LOCAL_SET_MIRROR_BYTES) {
        forgetSetBackup(normalized.id);
        return;
      }
      localStorage.setItem(`${SET_BACKUP_PREFIX}${normalized.id}`, serialized);
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
      const legacySerialized = JSON.stringify(updated);
      if (legacySerialized.length <= MAX_LOCAL_SET_MIRROR_BYTES) {
        localStorage.setItem('flashcardSets', legacySerialized);
      } else {
        localStorage.removeItem('flashcardSets');
      }
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

  function parseDataUrl(dataUrl) {
    const match = /^data:([^;,]+)?(?:;[^,]*)?;base64,(.*)$/i.exec(String(dataUrl || ''));
    if (!match) throw new Error('Unsupported media payload.');
    return {
      mime: String(match[1] || 'application/octet-stream').toLowerCase(),
      base64: match[2] || ''
    };
  }

  function extensionForMime(mime) {
    const clean = String(mime || '').toLowerCase();
    if (clean === 'image/jpeg') return 'jpg';
    if (clean === 'image/png') return 'png';
    if (clean === 'image/gif') return 'gif';
    if (clean === 'image/webp') return 'webp';
    if (clean === 'image/svg+xml') return 'svg';
    if (clean === 'audio/mpeg') return 'mp3';
    if (clean === 'audio/wav') return 'wav';
    if (clean === 'audio/ogg') return 'ogg';
    if (clean === 'video/mp4') return 'mp4';
    if (clean === 'video/webm') return 'webm';
    return 'bin';
  }

  function safePathPart(value, fallback) {
    const clean = String(value || '').replace(/[^a-z0-9._-]+/gi, '-').replace(/^-+|-+$/g, '').slice(0, 60);
    return clean || fallback;
  }

  async function saveDataUrlFile(dataUrl, meta = {}) {
    if (!isNative) return dataUrl;
    const parsed = parseDataUrl(dataUrl);
    const ext = extensionForMime(parsed.mime);
    const deckId = safePathPart(meta.deckId || 'global', 'global');
    const prefix = safePathPart(meta.prefix || 'media', 'media');
    const random = Math.random().toString(36).slice(2, 9);
    const path = `${MEDIA_DIR}/${deckId}/${prefix}-${Date.now()}-${random}.${ext}`;

    await Filesystem.writeFile({
      path,
      data: parsed.base64,
      directory: DIRECTORY_DATA,
      recursive: true
    });

    const uriResult = await Filesystem.getUri?.({ path, directory: DIRECTORY_DATA }).catch(() => null);
    const uri = uriResult?.uri;
    if (!uri) return dataUrl;
    return capacitor.convertFileSrc ? capacitor.convertFileSrc(uri) : uri;
  }

  function sqlSummary(sql) {
    const text = String(sql || '').replace(/\s+/g, ' ').trim();
    const verb = (text.match(/^([a-z]+)/i)?.[1] || 'sql').toLowerCase();
    const table = text.match(/\b(?:FROM|INTO|UPDATE|TABLE)\s+([a-z0-9_]+)/i)?.[1] || 'unknown';
    return `${verb}.${table}`;
  }

  async function rows(sql, params = []) {
    const span = perf?.start('store.sql.read', { operation: sqlSummary(sql) });
    try {
      let result;
      if (isNative && db) {
        const res = await db.query(sql, params);
        result = res.values || [];
      } else {
        const statement = db.prepare(sql);
        statement.bind(params);
        result = [];
        while (statement.step()) result.push(statement.getAsObject());
        statement.free();
      }
      if (span && performance.now() - span.startedAt >= 25) {
        perf.end(span, { rowCount: result.length });
      }
      return result;
    } catch (error) {
      perf?.end(span, { status: 'error', error: perf?.sanitizeError(error) });
      throw error;
    }
  }

  async function run(sql, params = []) {
    const span = perf?.start('store.sql.write', { operation: sqlSummary(sql) });
    try {
      if (isNative && db) {
        await db.run(sql, params, transactionDepth === 0);
      } else {
        const statement = db.prepare(sql);
        statement.run(params);
        statement.free();
      }
      if (span && performance.now() - span.startedAt >= 25) perf.end(span, { status: 'ok' });
    } catch (error) {
      perf?.end(span, { status: 'error', error: perf?.sanitizeError(error) });
      throw error;
    }
  }

  async function executeRaw(sql) {
    if (isNative && db) {
      await db.execute(sql, transactionDepth === 0);
      return;
    }
    db.exec(sql);
  }

  async function executeSet(set) {
    const span = perf?.start('store.sql.batch', { statementCount: set.length });
    try {
      if (isNative && db) {
        await db.executeSet(set, transactionDepth === 0);
      } else if (transactionDepth > 0) {
        for (const item of set) {
          const statement = db.prepare(item.statement);
          statement.run(item.values);
          statement.free();
        }
      } else {
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
      if (span && performance.now() - span.startedAt >= 25) perf.end(span, { status: 'ok' });
    } catch (error) {
      perf?.end(span, { status: 'error', error: perf?.sanitizeError(error) });
      throw error;
    }
  }

  async function withTransaction(work) {
    if (isNative && db) {
      const nested = transactionDepth > 0;
      transactionDepth += 1;
      try {
        if (!nested) await db.beginTransaction();
        const result = await work();
        if (!nested) {
          const active = await db.isTransactionActive().catch(() => ({ result: false }));
          if (active?.result) await db.commitTransaction();
        }
        return result;
      } catch (error) {
        if (!nested) {
          try {
            const active = await db.isTransactionActive().catch(() => ({ result: false }));
            if (active?.result) await db.rollbackTransaction();
          } catch (rollbackError) {
            console.warn('[mobile-store] native transaction rollback failed:', rollbackError?.message || rollbackError);
          }
        }
        throw error;
      } finally {
        transactionDepth = Math.max(0, transactionDepth - 1);
      }
    }

    const nested = transactionDepth > 0;
    const savepoint = `sp_${transactionDepth + 1}`;
    transactionDepth += 1;
    try {
      await executeRaw(nested ? `SAVEPOINT ${savepoint};` : 'BEGIN IMMEDIATE TRANSACTION;');
      const result = await work();
      await executeRaw(nested ? `RELEASE SAVEPOINT ${savepoint};` : 'COMMIT;');
      return result;
    } catch (error) {
      try {
        if (nested) {
          await executeRaw(`ROLLBACK TO SAVEPOINT ${savepoint};`);
          await executeRaw(`RELEASE SAVEPOINT ${savepoint};`);
        } else {
          await executeRaw('ROLLBACK;');
        }
      } catch (rollbackError) {
        console.warn('[mobile-store] transaction rollback failed:', rollbackError?.message || rollbackError);
      }
      throw error;
    } finally {
      transactionDepth = Math.max(0, transactionDepth - 1);
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

      CREATE TABLE IF NOT EXISTS study_sessions (
        id TEXT PRIMARY KEY,
        set_id TEXT,
        started_at INTEGER NOT NULL,
        duration_ms INTEGER NOT NULL,
        cards_viewed INTEGER NOT NULL,
        mode TEXT NOT NULL
      );

      CREATE INDEX IF NOT EXISTS idx_mobile_sets_visible ON sets(deleted_at, last_modified);
      CREATE INDEX IF NOT EXISTS idx_mobile_sets_class ON sets(class_id);
      CREATE INDEX IF NOT EXISTS idx_mobile_cards_set_position ON cards(set_id, position);
      CREATE INDEX IF NOT EXISTS idx_mobile_cards_visible ON cards(deleted_at, set_id, last_modified);
      CREATE INDEX IF NOT EXISTS idx_mobile_cards_flags ON cards(set_id, suspended, buried_until);
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
    const span = perf?.start('store.flush', {
      native: isNative,
      scheduled: Boolean(_persistTimer),
      inFlight: Boolean(_persistInFlight)
    });
    try {
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
    } finally {
      perf?.end(span, { status: 'ok' });
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

    await withTransaction(async () => {
      await run(`
        UPDATE cards SET
          srs_json = ?,
          review_history_json = ?,
          suspended = ?,
          buried_until = ?,
          last_modified = ?,
          payload_json = ?
        WHERE id = ? AND set_id = ? AND deleted_at IS NULL
      `, [
        updated.srs ? jsonString(updated.srs) : null,
        jsonString(Array.isArray(updated.reviewHistory) ? updated.reviewHistory : []),
        updated.suspended ? 1 : 0,
        updated.buriedUntil || null,
        updated.lastModified,
        jsonString(updated),
        cardKey,
        setKey
      ]);

      await run('UPDATE sets SET last_modified = ? WHERE id = ? AND deleted_at IS NULL', [updated.lastModified, setKey]);
    });
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

    if (changed) {
      if (isNative) {
        try { localStorage.removeItem(STUDY_PATCHES_KEY); } catch (_) {}
      } else {
        _clearStudyPatchesAfterPersist = true;
      }
    }
    return changed;
  }

  async function init() {
    if (readyPromise) return readyPromise;
    const initSpan = perf?.start('store.init', { native: isNative });

    readyPromise = (async () => {
      const scriptBase = (() => {
        try {
          const scripts = document.querySelectorAll('script[src*="mobile-store"]');
          const src = scripts[scripts.length - 1]?.src || '';
          return src.substring(0, src.lastIndexOf('/js/mobile/'));
        } catch (_e) { return ''; }
      })();

      db = null;
      let foundExistingFile = false;
      let openedFromTemp = false;
      let lastOpenError = null;

      if (isNative) {
        const openSpan = perf?.start('store.native.open');
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
          perf?.end(openSpan, { status: 'ok', reusedConnection: Boolean(retCC && isConn) });
        } catch (error) {
          perf?.end(openSpan, { status: 'error', error: perf?.sanitizeError(error) });
          console.error('[mobile-store] Failed to open native SQLite database:', error);
          lastOpenError = error;
        }
      }

      if (isNative && db) {
        if (perf?.measure) await perf.measure('store.schema.ensure', () => createSchema());
        else await createSchema();
        if (perf?.measure) await perf.measure('store.legacy_migration.check', () => migrateFromLegacySqlJs());
        else await migrateFromLegacySqlJs();
      } else {
        // Load SQL.js WebAssembly only as a fallback
        const wasmBase = scriptBase ? `${scriptBase}/vendor/sql.js/` : 'vendor/sql.js/';
        const wasmSpan = perf?.start('store.webassembly.load');
        SQL = await initSqlJs({ locateFile: file => `${wasmBase}${file}` });
        perf?.end(wasmSpan, { status: 'ok' });

        const openSpan = perf?.start('store.webassembly.open_database');
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
        perf?.end(openSpan, {
          status: db ? 'ok' : (foundExistingFile ? 'error' : 'fresh'),
          openedFromTemp
        });

        const isFresh = !db;
        if (!db) {
          if (foundExistingFile) {
            throw new Error(`Local database could not be opened safely. Existing data was not overwritten. ${lastOpenError?.message || ''}`.trim());
          }
          console.warn('[mobile-store] Starting with empty database');
          db = new SQL.Database();
        }

        if (perf?.measure) await perf.measure('store.schema.ensure', () => createSchema());
        else await createSchema();
        const recoverySpan = perf?.start('store.recovery_checks');
        const recoveredClassBackups = await recoverLocalClassBackupsIfEmptyOrMissing();
        const recoveredLocalBackups = await recoverLocalSetBackupsIfEmpty();
        const repairedOrphans = await repairOrphanedClassIds();
        const appliedStudyPatches = await applyPendingStudyPatches();
        perf?.end(recoverySpan, {
          recoveredClassBackups: Boolean(recoveredClassBackups),
          recoveredLocalBackups: Boolean(recoveredLocalBackups),
          repairedOrphans: Boolean(repairedOrphans),
          appliedStudyPatches: Boolean(appliedStudyPatches)
        });
        // Only persist on first-time setup to avoid a costly full write on every cold start
        if (isFresh) await _doPersist();
        else if (openedFromTemp) await _doPersist();
        else if (recoveredClassBackups || recoveredLocalBackups || repairedOrphans) await _doPersist();
        else if (appliedStudyPatches) persist(2500).catch(() => {});
      }
      return true;
    })();
    readyPromise.then(
      () => perf?.end(initSpan, { status: 'ok' }),
      error => perf?.end(initSpan, { status: 'error', error: perf?.sanitizeError(error) })
    );

    return readyPromise;
  }

  async function ensureReady() {
    await init();
  }

  async function listClasses() {
    const span = perf?.start('store.classes.list');
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
    perf?.end(span, { classCount: classes.length });
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
    await withTransaction(async () => {
      await upsertClass(normalized);
    });
    rememberClassBackup(normalized);
    await persist();
    return normalized;
  }

  async function replaceClasses(classes = [], options = {}) {
    await ensureReady();
    const normalizedClasses = (Array.isArray(classes) ? classes : [])
      .map(classData => schema.normalizeClass(classData, null, { preserveLastModified: true }));
    await withTransaction(async () => {
      await run('DELETE FROM classes');
      for (const normalized of normalizedClasses) {
        await upsertClass(normalized);
      }
    });
    clearClassBackups();
    normalizedClasses.forEach(rememberClassBackup);
    if (options.persist !== false) await persist();
    return listClasses();
  }

  async function deleteClass(classId) {
    await ensureReady();
    const now = Date.now();
    await withTransaction(async () => {
      await run('DELETE FROM classes WHERE id = ?', [String(classId)]);
      await run('UPDATE sets SET class_id = NULL, last_modified = ? WHERE class_id = ? AND deleted_at IS NULL', [now, String(classId)]);
    });
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

  async function replaceCardsForSet(setId, cards = [], options = {}) {
    const setKey = String(setId);
    const existingRows = await rows(
      'SELECT id, position, last_modified, payload_json FROM cards WHERE set_id = ? AND deleted_at IS NULL',
      [setKey]
    );
    const existingById = new Map(existingRows.map(row => [String(row.id), row]));
    const changedCardIds = Array.isArray(options.changedCardIds)
      ? new Set(options.changedCardIds.map(String))
      : null;
    const nextIds = new Set();
    const set = [];

    for (let index = 0; index < cards.length; index++) {
      const card = cards[index];
      const cardId = String(card.id);
      const existing = existingById.get(cardId);
      nextIds.add(cardId);

      let serializedCard = null;
      const knownUnchanged = existing && changedCardIds && !changedCardIds.has(cardId);
      const contentUnchanged = existing && !changedCardIds && (() => {
        serializedCard = jsonString(card);
        return existing.payload_json === serializedCard;
      })();
      if (knownUnchanged || contentUnchanged) {
        if (Number(existing.position) !== index) {
          set.push({
            statement: 'UPDATE cards SET position = ? WHERE id = ? AND set_id = ?',
            values: [index, cardId, setKey]
          });
        }
        continue;
      }
      if (serializedCard === null) serializedCard = jsonString(card);

      set.push({
        statement: `
          INSERT INTO cards (
            id, set_id, position, term, definition, term_image, definition_image,
            tags_json, suspended, buried_until, srs_json, review_history_json,
            created, last_modified, deleted_at, payload_json
          )
          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, NULL, ?)
          ON CONFLICT(id) DO UPDATE SET
            set_id = excluded.set_id,
            position = excluded.position,
            term = excluded.term,
            definition = excluded.definition,
            term_image = excluded.term_image,
            definition_image = excluded.definition_image,
            tags_json = excluded.tags_json,
            suspended = excluded.suspended,
            buried_until = excluded.buried_until,
            srs_json = excluded.srs_json,
            review_history_json = excluded.review_history_json,
            created = excluded.created,
            last_modified = excluded.last_modified,
            deleted_at = NULL,
            payload_json = excluded.payload_json
        `,
        values: [
          cardId,
          setKey,
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
          serializedCard
        ]
      });
    }

    const removedIds = existingRows
      .map(row => String(row.id))
      .filter(id => !nextIds.has(id));
    for (const idChunk of chunkArray(removedIds)) {
      const placeholders = idChunk.map(() => '?').join(',');
      set.push({
        statement: `DELETE FROM cards WHERE set_id = ? AND id IN (${placeholders})`,
        values: [setKey, ...idChunk]
      });
    }

    if (set.length) await executeSet(set);
  }

  async function repairCardIdsForSet(setId, cards = []) {
    const setKey = String(setId);
    const used = new Set();
    const nextCards = [];

    function nextCardId() {
      let id = schema.createId('card');
      while (used.has(String(id))) id = schema.createId('card');
      used.add(String(id));
      return id;
    }

    for (const card of Array.isArray(cards) ? cards : []) {
      const currentId = String(card?.id || '').trim();
      const isDuplicate = !currentId || used.has(currentId);
      const id = isDuplicate ? nextCardId() : currentId;
      used.add(String(id));
      nextCards.push({ ...card, id });
    }

    const ids = nextCards.map(card => String(card.id)).filter(Boolean);
    const conflicts = new Set();
    for (const idChunk of chunkArray(ids)) {
      const placeholders = idChunk.map(() => '?').join(',');
      const conflictRows = await rows(`
        SELECT id
        FROM cards
        WHERE deleted_at IS NULL
          AND set_id != ?
          AND id IN (${placeholders})
      `, [setKey, ...idChunk]);
      conflictRows.forEach(row => conflicts.add(String(row.id)));
    }

    if (!conflicts.size) return nextCards;

    for (const card of nextCards) {
      if (!conflicts.has(String(card.id))) continue;
      card.id = nextCardId();
      card.lastModified = Date.now();
    }
    return nextCards;
  }

  function repairCardIdsAcrossSets(sets = []) {
    const used = new Set();

    function nextCardId() {
      let id = schema.createId('card');
      while (used.has(String(id))) id = schema.createId('card');
      used.add(String(id));
      return id;
    }

    return (Array.isArray(sets) ? sets : []).map(set => ({
      ...set,
      cards: (Array.isArray(set.cards) ? set.cards : []).map(card => {
        const currentId = String(card?.id || '').trim();
        if (currentId && !used.has(currentId)) {
          used.add(currentId);
          return card;
        }
        return {
          ...card,
          id: nextCardId(),
          lastModified: Date.now()
        };
      })
    }));
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
    const span = perf?.start('store.set.hydrate');
    const payload = jsonParse(row.payload_json, {});
    const cardRows = await rows(
      'SELECT * FROM cards WHERE set_id = ? AND deleted_at IS NULL ORDER BY position ASC',
      [row.id]
    );
    const cards = cardRows.map(cardRow => hydrateCardRow(cardRow));
    perf?.end(span, { cardCount: cards.length });

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
      learningDueCards: 0,
      reviewDueCards: 0,
      learningCards: 0,
      reviewCards: 0,
      relearningCards: 0,
      matureCards: 0,
      reviewCount: 0,
      reviewedToday: 0,
      newCardsIntroducedToday: 0,
      reviewsDoneToday: 0,
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

  function chunkArray(items, size = 400) {
    const chunks = [];
    for (let index = 0; index < items.length; index += size) {
      chunks.push(items.slice(index, index + size));
    }
    return chunks;
  }

  function uniqueStringIds(values) {
    return Array.from(new Set((Array.isArray(values) ? values : [])
      .map(value => String(value || '').trim())
      .filter(Boolean)));
  }

  function normalizeTagInput(value) {
    if (Array.isArray(value)) return schema.normalizeStringArray(value);
    return schema.normalizeStringArray(String(value || ''));
  }

  function normalizeBulkDueIso(value) {
    const raw = String(value || '').trim();
    if (!raw) return null;
    const dateOnly = /^\d{4}-\d{2}-\d{2}$/.test(raw)
      ? new Date(`${raw}T04:00:00`)
      : new Date(raw);
    return Number.isFinite(dateOnly.getTime()) ? dateOnly.toISOString() : null;
  }

  function mediaItemsForPayload(payload = {}) {
    const media = payload.media || {};
    return [
      ...(Array.isArray(media.term) ? media.term : []),
      ...(Array.isArray(media.definition) ? media.definition : [])
    ];
  }

  function rowHasBrowserMedia(row, payload, kind) {
    if (kind === 'image' && (row.term_image || row.definition_image)) return true;
    return mediaItemsForPayload(payload).some(item => {
      const itemKind = String(item?.kind || item?.mediaType || '').toLowerCase();
      const mime = String(item?.mime || item?.type || '').toLowerCase();
      if (kind === 'audio') return itemKind === 'audio' || mime.startsWith('audio/');
      if (kind === 'image') return itemKind === 'image' || mime.startsWith('image/');
      return false;
    });
  }

  function normalizedRatingName(value) {
    const rating = String(value || '').trim().toLowerCase();
    if (rating === 'again' || rating === '1') return 'Again';
    if (rating === 'hard' || rating === '2') return 'Hard';
    if (rating === 'good' || rating === '3') return 'Good';
    if (rating === 'easy' || rating === '4') return 'Easy';
    return '';
  }

  function emptyRatingCounts() {
    return { Again: 0, Hard: 0, Good: 0, Easy: 0 };
  }

  function createRatingWindows() {
    return {
      '7': emptyRatingCounts(),
      '30': emptyRatingCounts(),
      '90': emptyRatingCounts(),
      all: emptyRatingCounts()
    };
  }

  function reviewStats(history, nowMs = Date.now()) {
    const todayKey = dayKey(nowMs);
    const sevenDaysAgo = nowMs - (7 * 24 * 60 * 60 * 1000);
    const thirtyDaysAgo = nowMs - (30 * 24 * 60 * 60 * 1000);
    const ninetyDaysAgo = nowMs - (90 * 24 * 60 * 60 * 1000);
    let lastReviewedAt = null;
    let againCount = 0;
    let failedRecently = false;
    let failedToday = false;
    const ratingCounts = emptyRatingCounts();
    const ratingWindows = createRatingWindows();
    for (const review of Array.isArray(history) ? history : []) {
      const rating = normalizedRatingName(review?.rating || review?.grade);
      const reviewedAt = timeValue(review?.reviewedAt || review?.time || review?.date);
      if (reviewedAt && (!lastReviewedAt || reviewedAt > lastReviewedAt)) lastReviewedAt = reviewedAt;
      if (rating) {
        ratingCounts[rating] += 1;
        ratingWindows.all[rating] += 1;
        if (reviewedAt >= sevenDaysAgo) ratingWindows['7'][rating] += 1;
        if (reviewedAt >= thirtyDaysAgo) ratingWindows['30'][rating] += 1;
        if (reviewedAt >= ninetyDaysAgo) ratingWindows['90'][rating] += 1;
      }
      if (rating === 'Again') {
        againCount += 1;
        if (reviewedAt && reviewedAt >= sevenDaysAgo) failedRecently = true;
        if (reviewedAt && dayKey(reviewedAt) === todayKey) failedToday = true;
      }
    }
    return { againCount, failedRecently, failedToday, lastReviewedAt, ratingCounts, ratingWindows };
  }

  function browserCardFromRow(row, nowMs = Date.now()) {
    const payload = jsonParse(row.payload_json, {});
    const srs = row.srs_json && row.srs_json !== 'null' ? jsonParse(row.srs_json, null) : null;
    const tags = jsonParse(row.tags_json, []);
    const history = jsonParse(row.review_history_json, []);
    const state = normalizeSrsState(srs?.state);
    const dueTime = timeValue(srs?.due);
    const suspended = Boolean(Number(row.suspended || 0));
    const buriedUntil = row.buried_until || null;
    const buried = isBuried(buriedUntil, nowMs);
    const scheduledDue = Boolean(srs && state !== 'New' && isSrsDue(srs, nowMs));
    const overdue = Boolean(srs && state !== 'New' && dueTime && srsDayKey(dueTime) < srsDayKey(nowMs));
    const reviews = reviewStats(history, nowMs);
    const hasImage = rowHasBrowserMedia(row, payload, 'image');
    const hasAudio = rowHasBrowserMedia(row, payload, 'audio');

    return {
      id: row.id,
      setId: row.set_id,
      noteId: payload.noteId || null,
      noteType: payload.noteType || 'basic',
      cardTemplate: payload.cardTemplate || 'front-back',
      clozeIndex: payload.clozeIndex || null,
      deck: row.deck_name || 'Untitled Set',
      classId: row.class_id || null,
      className: row.class_name || 'General',
      position: Number(row.position || 0),
      term: row.term || '',
      definition: row.definition || '',
      tags,
      srsState: state,
      due: srs?.due || null,
      dueTime,
      isDue: !suspended && !buried && scheduledDue,
      isOverdue: !suspended && !buried && overdue,
      suspended,
      buriedUntil,
      buried,
      failedRecently: reviews.failedRecently,
      failedToday: reviews.failedToday,
      leech: reviews.againCount >= 8 || Number(srs?.lapses || 0) >= 8,
      noTags: !tags.length,
      hasImage,
      hasAudio,
      reviewCount: Array.isArray(history) ? history.length : 0,
      againCount: reviews.againCount,
      ratingCounts: reviews.ratingCounts,
      ratingWindows: reviews.ratingWindows,
      reps: Number(srs?.reps || 0),
      lapses: Number(srs?.lapses || 0),
      intervalDays: Number(srs?.scheduled_days || srs?.elapsed_days || 0),
      lastReviewedAt: reviews.lastReviewedAt,
      lastModified: Number(row.last_modified || 0)
    };
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

  function srsDayKey(value, rolloverHour = 4) {
    const timestamp = timeValue(value);
    if (!timestamp) return null;
    const adjusted = new Date(timestamp - rolloverHour * 60 * 60 * 1000);
    adjusted.setHours(0, 0, 0, 0);
    return String(adjusted.getTime());
  }

  function isBuried(buriedUntil, nowMs) {
    const until = timeValue(buriedUntil);
    return until > nowMs;
  }

  function isSrsDue(srs, nowMs) {
    if (!srs || !srs.due) return true;
    const due = timeValue(srs.due);
    if (!due) return true;
    const state = normalizeSrsState(srs.state);
    if (state === 'Learning' || state === 'Relearning') return due <= nowMs;
    return srsDayKey(due) <= srsDayKey(nowMs);
  }

  async function buildMetaStatsBySet(setIds = []) {
    const span = perf?.start('store.stats.recompute', {
      requestedDeckCount: uniqueStringIds(setIds).length
    });
    const nowMs = Date.now();
    const todayCalendarKey = dayKey(nowMs);
    const todaySrsKey = srsDayKey(nowMs);
    const thirtyDaysAgo = nowMs - 30 * 24 * 60 * 60 * 1000;
    const statsBySet = new Map();
    const dayKeysBySet = new Map();

    const ids = uniqueStringIds(setIds);
    const idChunks = ids.length ? chunkArray(ids, 350) : [[]];
    const cardRows = [];
    for (const idChunk of idChunks) {
      const idFilter = idChunk.length
        ? ` AND c.set_id IN (${idChunk.map(() => '?').join(',')})`
        : '';
      cardRows.push(...await rows(`
        SELECT c.set_id, c.srs_json, c.review_history_json, c.suspended, c.buried_until
        FROM cards c
        INNER JOIN sets s ON s.id = c.set_id
        WHERE c.deleted_at IS NULL AND s.deleted_at IS NULL
        ${idFilter}
      `, idChunk));
    }

    for (let rowIndex = 0; rowIndex < cardRows.length; rowIndex += 1) {
      const row = cardRows[rowIndex];
      const setId = String(row.set_id);
      const stats = statsBySet.get(setId) || createMetaStats();
      const dayKeys = dayKeysBySet.get(setId) || new Set();

      const historyJson = row.review_history_json;
      if (historyJson && historyJson !== '[]') {
        const history = jsonParse(historyJson, []);
        (Array.isArray(history) ? history : []).forEach(review => {
          const reviewedAt = timeValue(review.reviewedAt || review.time || review.date);
          if (!reviewedAt) return;
          stats.reviewCount += 1;
          if (!stats.lastReviewAt || reviewedAt > stats.lastReviewAt) stats.lastReviewAt = reviewedAt;
          const key = dayKey(reviewedAt);
          if (key) dayKeys.add(key);
          if (key === todayCalendarKey) {
            stats.reviewedToday += 1;
          }
          if (srsDayKey(reviewedAt) === todaySrsKey) {
            const previousState = normalizeSrsState(review.previousState);
            if (previousState === 'New') stats.newCardsIntroducedToday += 1;
            if (previousState === 'Review') stats.reviewsDoneToday += 1;
          }
          if (reviewedAt >= thirtyDaysAgo) {
            stats.reviewed30 += 1;
            if (String(review.rating || '').toLowerCase() !== 'again') stats.remembered30 += 1;
          }
        });
      }

      if (!Number(row.suspended || 0) && !isBuried(row.buried_until, nowMs)) {
        stats.totalCards += 1;
        const srs = row.srs_json && row.srs_json !== 'null' ? jsonParse(row.srs_json, null) : null;
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
            if (state === 'Review') stats.reviewDueCards += 1;
            else stats.learningDueCards += 1;
          } else if (state === 'Review') {
            stats.matureCards += 1;
          }
        }

        const dueTime = timeValue(srs?.due);
        if (dueTime && (!stats.nextDue || dueTime < stats.nextDue)) stats.nextDue = dueTime;
      }

      statsBySet.set(setId, stats);
      dayKeysBySet.set(setId, dayKeys);
      if (rowIndex > 0 && rowIndex % 500 === 0) {
        await new Promise(resolve => window.setTimeout(resolve, 0));
      }
    }

    statsBySet.forEach((stats, setId) => {
      stats.reviewDayKeys = Array.from(dayKeysBySet.get(setId) || []);
      stats.retention = stats.reviewed30 > 0 ? Math.round((stats.remembered30 / stats.reviewed30) * 100) : null;
    });

    perf?.end(span, {
      cardRowsScanned: cardRows.length,
      deckCount: statsBySet.size
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
    const learningDue = Number(stats.learningDueCards || 0);
    const reviewDue = Number(stats.reviewDueCards || 0);
    const remainingNew = newLimit === null
      ? newDue
      : Math.min(newDue, Math.max(0, newLimit - Number(stats.newCardsIntroducedToday || 0)));
    const remainingReviews = reviewLimit === null
      ? reviewDue
      : Math.min(reviewDue, Math.max(0, reviewLimit - Number(stats.reviewsDoneToday || 0)));
    return learningDue + remainingNew + remainingReviews;
  }

  async function getSetStatsMeta(setIds = []) {
    const span = perf?.start('store.stats.list', {
      requestedDeckCount: uniqueStringIds(setIds).length
    });
    await ensureReady();
    const ids = uniqueStringIds(setIds);
    const idFilter = ids.length
      ? ` AND s.id IN (${ids.map(() => '?').join(',')})`
      : '';
    const setRows = await rows(`
      SELECT s.id, s.last_modified, s.srs_settings_json, COUNT(c.id) AS card_count
      FROM sets s
      LEFT JOIN cards c ON c.set_id = s.id AND c.deleted_at IS NULL
      WHERE s.deleted_at IS NULL
      ${idFilter}
      GROUP BY s.id
      ORDER BY s.last_modified DESC, s.created DESC
    `, ids);

    const cache = readSetStatsCache();
    const dayToken = statsCacheDayToken();
    const staleIds = [];
    const staleIdSet = new Set();
    const statsBySet = new Map();

    setRows.forEach(row => {
      const cached = cachedStatsForSet(cache, row.id, row.last_modified, dayToken);
      if (cached) statsBySet.set(String(row.id), cached);
      else {
        staleIds.push(String(row.id));
        staleIdSet.add(String(row.id));
      }
    });

    if (staleIds.length) {
      const recomputed = await buildMetaStatsBySet(staleIds);
      setRows.forEach(row => {
        const setId = String(row.id);
        if (!staleIdSet.has(setId)) return;
        const settings = jsonParse(row.srs_settings_json, {});
        const stats = {
          ...createMetaStats(),
          ...(recomputed.get(setId) || {}),
          totalCards: Number(row.card_count || 0)
        };
        stats.dueCards = limitedDueCount(stats, settings);
        statsBySet.set(setId, stats);
        cache[setId] = {
          lastModified: Number(row.last_modified || 0),
          dayToken,
          stats
        };
      });
    }

    if (!ids.length) {
      const visibleIds = new Set(setRows.map(row => String(row.id)));
      Object.keys(cache).forEach(setId => {
        if (!visibleIds.has(setId)) delete cache[setId];
      });
    }
    writeSetStatsCache(cache);

    const result = setRows.map(row => ({
      setId: String(row.id),
      lastModified: Number(row.last_modified || 0),
      stats: statsBySet.get(String(row.id)) || {
        ...createMetaStats(),
        totalCards: Number(row.card_count || 0)
      }
    }));
    perf?.end(span, {
      deckCount: result.length,
      cacheHitCount: Math.max(0, result.length - staleIds.length),
      recomputedDeckCount: staleIds.length
    });
    return result;
  }

  async function listSetsMeta(options = {}) {
    const span = perf?.start('store.sets.list_meta', {
      includeStats: options.includeStats !== false,
      useCachedStats: options.useCachedStats !== false
    });
    await ensureReady();
    const includeStats = options.includeStats !== false;
    const useCachedStats = options.useCachedStats !== false;
    const setRows = await rows(`
      SELECT s.*, COUNT(c.id) AS card_count
      FROM sets s
      LEFT JOIN cards c ON c.set_id = s.id AND c.deleted_at IS NULL
      WHERE s.deleted_at IS NULL
      GROUP BY s.id
      ORDER BY s.last_modified DESC, s.created DESC
    `);
    const cache = useCachedStats ? readSetStatsCache() : {};
    const dayToken = statsCacheDayToken();
    let statsEntries = [];
    if (includeStats) {
      statsEntries = await getSetStatsMeta(setRows.map(row => row.id));
    }
    const refreshedStats = new Map(statsEntries.map(item => [String(item.setId), item.stats]));

    const result = setRows.map(row => {
      const payload = jsonParse(row.payload_json, {});
      const settings = jsonParse(row.srs_settings_json, {});
      const cached = cachedStatsForSet(cache, row.id, row.last_modified, dayToken);
      const stats = refreshedStats.get(String(row.id))
        || cached
        || {
          ...createMetaStats(),
          totalCards: Number(row.card_count || 0)
        };
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
    perf?.end(span, {
      deckCount: result.length,
      cardCount: result.reduce((total, set) => total + Number(set.cardCount || 0), 0)
    });
    return result;
  }

  async function listCardsForBrowser() {
    await ensureReady();
    const nowMs = Date.now();
    const result = await rows(`
      SELECT
        c.id,
        c.set_id,
        c.position,
        c.term,
        c.definition,
        c.term_image,
        c.definition_image,
        c.tags_json,
        c.suspended,
        c.buried_until,
        c.srs_json,
        c.review_history_json,
        c.last_modified,
        c.payload_json,
        s.name AS deck_name,
        s.class_id,
        cl.name AS class_name
      FROM cards c
      INNER JOIN sets s ON s.id = c.set_id
      LEFT JOIN classes cl ON cl.id = s.class_id AND cl.deleted_at IS NULL
      WHERE c.deleted_at IS NULL AND s.deleted_at IS NULL
      ORDER BY s.last_modified DESC, c.position ASC
    `);
    return result.map(row => browserCardFromRow(row, nowMs));
  }

  async function getCardRowsByIds(cardIds) {
    const ids = uniqueStringIds(cardIds);
    if (!ids.length) return [];
    const result = [];
    for (const idChunk of chunkArray(ids)) {
      const placeholders = idChunk.map(() => '?').join(',');
      const chunkRows = await rows(`
        SELECT c.*
        FROM cards c
        INNER JOIN sets s ON s.id = c.set_id
        WHERE c.deleted_at IS NULL
          AND s.deleted_at IS NULL
          AND c.id IN (${placeholders})
      `, idChunk);
      result.push(...chunkRows);
    }
    return result;
  }

  function updateCardStatement(card, setId, position = null) {
    return {
      statement: `
        UPDATE cards SET
          set_id = ?,
          position = COALESCE(?, position),
          term = ?,
          definition = ?,
          term_image = ?,
          definition_image = ?,
          tags_json = ?,
          suspended = ?,
          buried_until = ?,
          srs_json = ?,
          review_history_json = ?,
          last_modified = ?,
          payload_json = ?
        WHERE id = ? AND deleted_at IS NULL
      `,
      values: [
        String(setId),
        position === null ? null : Number(position),
        card.term || '',
        card.definition || '',
        card.termImage || '',
        card.definitionImage || '',
        jsonString(Array.isArray(card.tags) ? card.tags : []),
        card.suspended ? 1 : 0,
        card.buriedUntil || null,
        card.srs ? jsonString(card.srs) : null,
        jsonString(Array.isArray(card.reviewHistory) ? card.reviewHistory : []),
        Number(card.lastModified || Date.now()),
        jsonString(card),
        String(card.id)
      ]
    };
  }

  function clearStudyPatchesForCardRows(cardRows) {
    try {
      const patchesRaw = localStorage.getItem(STUDY_PATCHES_KEY);
      if (!patchesRaw) return;
      const patches = JSON.parse(patchesRaw);
      if (!patches?.sets) return;
      for (const row of cardRows) {
        const setId = String(row.set_id);
        const cardId = String(row.id);
        if (!patches.sets[setId]?.cards?.[cardId]) continue;
        delete patches.sets[setId].cards[cardId];
        if (Object.keys(patches.sets[setId].cards).length === 0) {
          delete patches.sets[setId];
        }
      }
      localStorage.setItem(STUDY_PATCHES_KEY, JSON.stringify(patches));
    } catch (_) {}
  }

  async function refreshSetBackupsForIds(setIds) {
    const ids = uniqueStringIds(Array.from(setIds || []));
    for (const setId of ids.slice(0, 40)) {
      try {
        const setRows = await rows('SELECT * FROM sets WHERE id = ? AND deleted_at IS NULL', [setId]);
        if (setRows.length) rememberSetBackup(await hydrateSetRow(setRows[0]));
      } catch (_) {}
    }
  }

  async function bulkUpdateCards(cardIds = [], action = '', options = {}) {
    await ensureReady();
    const ids = uniqueStringIds(cardIds);
    if (!ids.length) return { updated: 0, deleted: 0, moved: 0, touchedSetIds: [] };

    const normalizedAction = String(action || '').trim().toLowerCase();
    const allowedActions = new Set([
      'suspend',
      'unsuspend',
      'reset-srs',
      'delete',
      'move',
      'set-due',
      'add-tag',
      'remove-tag'
    ]);
    if (!allowedActions.has(normalizedAction)) {
      throw new Error(`Unsupported bulk card action: ${action}`);
    }

    const cardRows = await getCardRowsByIds(ids);
    if (!cardRows.length) return { updated: 0, deleted: 0, moved: 0, touchedSetIds: [] };

    const now = Date.now();
    const batch = [];
    const touchedSetIds = new Set(cardRows.map(row => String(row.set_id)));
    let updated = 0;
    let deleted = 0;
    let moved = 0;
    let targetSetId = null;
    let nextTargetPosition = null;
    let dueIso = null;
    let tagList = [];

    if (normalizedAction === 'move') {
      targetSetId = String(options.targetSetId || '').trim();
      if (!targetSetId) throw new Error('Choose a destination deck.');
      const targetRows = await rows('SELECT id FROM sets WHERE id = ? AND deleted_at IS NULL', [targetSetId]);
      if (!targetRows.length) throw new Error('Destination deck was not found.');
      const positionRows = await rows('SELECT MAX(position) AS max_position FROM cards WHERE set_id = ? AND deleted_at IS NULL', [targetSetId]);
      nextTargetPosition = Number(positionRows[0]?.max_position ?? -1) + 1;
      touchedSetIds.add(targetSetId);
    } else if (normalizedAction === 'set-due') {
      dueIso = normalizeBulkDueIso(options.due || options.dueDate);
      if (!dueIso) throw new Error('Choose a valid due date.');
    } else if (normalizedAction === 'add-tag' || normalizedAction === 'remove-tag') {
      tagList = normalizeTagInput(options.tags || options.tag);
      if (!tagList.length) throw new Error('Enter at least one tag.');
    }

    for (const row of cardRows) {
      if (normalizedAction === 'delete') {
        batch.push({
          statement: 'DELETE FROM cards WHERE id = ? AND deleted_at IS NULL',
          values: [String(row.id)]
        });
        deleted += 1;
        continue;
      }

      const card = hydrateCardRow(row);
      card.lastModified = now;
      let nextSetId = String(row.set_id);
      let nextPosition = null;

      if (normalizedAction === 'suspend') {
        card.suspended = true;
      } else if (normalizedAction === 'unsuspend') {
        card.suspended = false;
      } else if (normalizedAction === 'reset-srs') {
        card.srs = undefined;
        if (options.deleteHistory) card.reviewHistory = [];
      } else if (normalizedAction === 'set-due') {
        const baseSrs = card.srs && typeof card.srs === 'object' ? card.srs : {};
        const nextState = baseSrs.state && normalizeSrsState(baseSrs.state) !== 'New'
          ? baseSrs.state
          : 'Review';
        card.srs = {
          ...baseSrs,
          state: nextState,
          due: dueIso,
          elapsed_days: Number(baseSrs.elapsed_days || 0),
          scheduled_days: Number(baseSrs.scheduled_days || 0),
          reps: Number(baseSrs.reps || 0),
          lapses: Number(baseSrs.lapses || 0),
          stability: Number(baseSrs.stability || 0),
          difficulty: Number(baseSrs.difficulty || 0)
        };
      } else if (normalizedAction === 'add-tag') {
        const currentTags = schema.normalizeStringArray(card.tags || []);
        const lower = new Set(currentTags.map(tag => tag.toLowerCase()));
        card.tags = [
          ...currentTags,
          ...tagList.filter(tag => !lower.has(tag.toLowerCase()))
        ];
      } else if (normalizedAction === 'remove-tag') {
        const remove = new Set(tagList.map(tag => tag.toLowerCase()));
        card.tags = schema.normalizeStringArray(card.tags || [])
          .filter(tag => !remove.has(tag.toLowerCase()));
      } else if (normalizedAction === 'move') {
        nextSetId = targetSetId;
        nextPosition = nextTargetPosition++;
        moved += 1;
      }

      batch.push(updateCardStatement(card, nextSetId, nextPosition));
      updated += 1;
    }

    await withTransaction(async () => {
      if (batch.length > 0) await executeSet(batch);
      for (const setId of touchedSetIds) {
        await run('UPDATE sets SET last_modified = ? WHERE id = ? AND deleted_at IS NULL', [now, setId]);
      }
    });

    clearStudyPatchesForCardRows(cardRows);
    await refreshSetBackupsForIds(touchedSetIds);
    await persist();

    return {
      updated,
      deleted,
      moved,
      touchedSetIds: Array.from(touchedSetIds)
    };
  }

  async function getSet(id) {
    const span = perf?.start('store.set.get');
    await ensureReady();
    const setRows = await rows('SELECT * FROM sets WHERE id = ? AND deleted_at IS NULL', [String(id)]);
    if (!setRows.length) {
      perf?.end(span, { found: false });
      return null;
    }
    const set = await hydrateSetRow(setRows[0]);
    rememberSetBackup(set);
    perf?.end(span, { found: true, cardCount: set.cards?.length || 0 });
    return set;
  }

  async function saveSet(set) {
    const span = perf?.start('store.set.save', {
      hasCards: Object.prototype.hasOwnProperty.call(set || {}, 'cards'),
      cardCount: Array.isArray(set?.cards) ? set.cards.length : null,
      changedCardCount: Array.isArray(set?.__changedCardIds) ? set.__changedCardIds.length : null,
      requestedMetaOnly: Boolean(set?.__metaOnly)
    });
    await ensureReady();
    const hasCardsField = Object.prototype.hasOwnProperty.call(set || {}, 'cards');
    const wantsMetaOnly = Boolean(set?.__metaOnly) || !hasCardsField;
    const existing = set.id ? await getSetMeta(set.id) : null;
    const metaOnlyUpdate = Boolean(set?.__metaOnly)
      || (existing && !hasCardsField)
      || (existing && hasCardsField && Array.isArray(set.cards) && set.cards.length === 0 && Number(set.cardCount || 0) > 0);
    const {
      mobileStats: _mobileStats,
      __metaOnly: _metaOnly,
      __changedCardIds: changedCardIds,
      cardCount: _cardCount,
      ...cleanSet
    } = set || {};

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
      await withTransaction(async () => {
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
      });
      await persist();
      perf?.end(span, { status: 'ok', mode: 'metadata' });
      return { ...next, cards: [], __metaOnly: true };
    }

    const normalized = schema.normalizeSet(cleanSet, existing);
    normalized.cards = await repairCardIdsForSet(normalized.id, normalized.cards || []);
    await withTransaction(async () => {
      await upsertSet(normalized);
      if (!metaOnlyUpdate) {
        await replaceCardsForSet(normalized.id, normalized.cards || [], {
          changedCardIds
        });
      }
    });
    if (!metaOnlyUpdate) rememberSetBackup(normalized);
    await persist(); // fire-and-forget — flush() ensures it completes before navigation
    perf?.end(span, {
      status: 'ok',
      mode: 'cards',
      cardCount: normalized.cards?.length || 0
    });
    return normalized;
  }

  async function replaceSets(sets = [], options = {}) {
    await ensureReady();
    const normalizedSets = repairCardIdsAcrossSets((Array.isArray(sets) ? sets : [])
      .map(set => schema.normalizeSet(set, null, { preserveLastModified: true })));
    await withTransaction(async () => {
      await run('DELETE FROM cards');
      await run('DELETE FROM sets');
      await run('DELETE FROM progress');
      await run('DELETE FROM study_sessions');
      for (const normalized of normalizedSets) {
        await upsertSet(normalized);
        await replaceCardsForSet(normalized.id, normalized.cards || []);
      }
    });
    clearSetBackups();
    clearSetStatsCache();
    for (const normalized of normalizedSets) {
      rememberSetBackup(normalized);
    }
    if (options.persist !== false) await persist();
    return options.metaOnly ? listSetsMeta() : listSets();
  }

  async function deleteSet(id) {
    await ensureReady();
    await withTransaction(async () => {
      await run('DELETE FROM cards WHERE set_id = ?', [String(id)]);
      await run('DELETE FROM progress WHERE set_id = ?', [String(id)]);
      await run('DELETE FROM study_sessions WHERE set_id = ?', [String(id)]);
      await run('DELETE FROM sets WHERE id = ?', [String(id)]);
    });
    forgetSetBackup(id);
    removeSetStatsCacheEntry(id);
    await persist();
    return true;
  }

  async function getSettings() {
    const span = perf?.start('store.settings.get');
    await ensureReady();
    const result = await rows('SELECT value_json FROM settings WHERE key = ?', ['app']);
    const settings = schema.normalizeSettings(jsonParse(result[0]?.value_json, {}));
    perf?.end(span, { found: Boolean(result.length) });
    return settings;
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
    const span = perf?.start('store.progress.get');
    await ensureReady();
    const result = await rows('SELECT value_json FROM progress WHERE set_id = ?', [String(setId)]);
    const progress = jsonParse(result[0]?.value_json, null);
    perf?.end(span, { found: Boolean(progress) });
    return progress;
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
    if (isNative) {
      try {
        const patchesRaw = localStorage.getItem(STUDY_PATCHES_KEY);
        if (patchesRaw) {
          const patches = JSON.parse(patchesRaw);
          if (patches?.sets?.[setId]?.cards?.[cardId]) {
            delete patches.sets[setId].cards[cardId];
            if (Object.keys(patches.sets[setId].cards).length === 0) {
              delete patches.sets[setId];
            }
            localStorage.setItem(STUDY_PATCHES_KEY, JSON.stringify(patches));
          }
        }
      } catch (_) {}
    } else {
      await persist(12000);
    }
    return true;
  }

  async function saveCardProgressBatch(setId, patches = {}) {
    await ensureReady();
    const batch = [];
    for (const [cardId, patch] of Object.entries(patches)) {
      const setKey = String(setId);
      const cardKey = String(cardId);
      const result = await rows(
        'SELECT payload_json FROM cards WHERE id = ? AND set_id = ? AND deleted_at IS NULL',
        [cardKey, setKey]
      );
      if (!result.length) continue;

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

      batch.push({
        statement: `
          UPDATE cards SET
            srs_json = ?,
            review_history_json = ?,
            suspended = ?,
            buried_until = ?,
            last_modified = ?,
            payload_json = ?
          WHERE id = ? AND set_id = ? AND deleted_at IS NULL
        `,
        values: [
          updated.srs ? jsonString(updated.srs) : null,
          jsonString(Array.isArray(updated.reviewHistory) ? updated.reviewHistory : []),
          updated.suspended ? 1 : 0,
          updated.buriedUntil || null,
          updated.lastModified,
          jsonString(updated),
          cardKey,
          setKey
        ]
      });
    }

    if (batch.length > 0) {
      await withTransaction(async () => {
        await executeSet(batch);
        const now = Date.now();
        await run('UPDATE sets SET last_modified = ? WHERE id = ? AND deleted_at IS NULL', [now, String(setId)]);
      });
    }

    if (isNative) {
      try {
        const patchesRaw = localStorage.getItem(STUDY_PATCHES_KEY);
        if (patchesRaw) {
          const patchesData = JSON.parse(patchesRaw);
          if (patchesData?.sets?.[setId]?.cards) {
            for (const cardId of Object.keys(patches)) {
              delete patchesData.sets[setId].cards[cardId];
            }
            if (Object.keys(patchesData.sets[setId].cards).length === 0) {
              delete patchesData.sets[setId];
            }
            localStorage.setItem(STUDY_PATCHES_KEY, JSON.stringify(patchesData));
          }
        }
      } catch (_) {}
    } else {
      await persist(12000);
    }
    return true;
  }

  async function getAllProgress() {
    const span = perf?.start('store.progress.list_all');
    await ensureReady();
    const progress = {};
    const result = await rows('SELECT set_id, value_json FROM progress');
    result.forEach(row => {
      progress[row.set_id] = jsonParse(row.value_json, null);
    });
    perf?.end(span, { progressCount: result.length });
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
      let settled = false;
      let clickAt = 0;
      let timeoutId = null;
      const input = document.createElement('input');
      const cleanup = () => {
        window.removeEventListener('focus', onWindowFocus);
        document.removeEventListener('visibilitychange', onVisibilityChange);
        if (timeoutId) clearTimeout(timeoutId);
        input.remove();
      };
      const finish = (file = null) => {
        if (settled) return;
        settled = true;
        cleanup();
        resolve(file);
      };
      const finishIfEmpty = () => {
        if (!settled && !(input.files && input.files.length)) finish(null);
      };
      const onChange = () => finish(input.files?.[0] || null);
      const onCancel = () => finish(null);
      const onWindowFocus = () => {
        const waitMs = Math.max(350, 700 - (Date.now() - clickAt));
        window.setTimeout(finishIfEmpty, waitMs);
      };
      const onVisibilityChange = () => {
        if (document.visibilityState === 'visible') onWindowFocus();
      };

      input.type = 'file';
      input.accept = 'application/json,.json';
      input.style.display = 'none';
      input.addEventListener('change', onChange, { once: true });
      input.addEventListener('cancel', onCancel, { once: true });
      window.addEventListener('focus', onWindowFocus);
      document.addEventListener('visibilitychange', onVisibilityChange);
      document.body.appendChild(input);
      timeoutId = window.setTimeout(() => finish(null), 2 * 60 * 1000);
      clickAt = Date.now();
      try {
        input.click();
      } catch (_) {
        finish(null);
      }
    });
  }

  async function resetDeckSRS(setId, deleteHistory) {
    await ensureReady();
    const cardRows = await rows('SELECT * FROM cards WHERE set_id = ? AND deleted_at IS NULL', [String(setId)]);

    const batch = [];
    for (const cardRow of cardRows) {
      const card = hydrateCardRow(cardRow);
      card.srs = undefined;
      if (deleteHistory) {
        card.reviewHistory = [];
      }

      batch.push({
        statement: 'UPDATE cards SET srs_json = NULL, review_history_json = ?, payload_json = ?, last_modified = ? WHERE id = ?',
        values: [
          jsonString(card.reviewHistory),
          jsonString(card),
          Date.now(),
          String(card.id)
        ]
      });
    }

    await withTransaction(async () => {
      if (batch.length > 0) {
        await executeSet(batch);
      }

      // Reset SRS progress inside progress table
      await run('DELETE FROM progress WHERE set_id = ?', [String(setId)]);
      await run('UPDATE sets SET last_modified = ? WHERE id = ? AND deleted_at IS NULL', [Date.now(), String(setId)]);
    });

    // Clear progress mirror from localStorage
    try {
      localStorage.removeItem('erudite-mobile-progress:' + setId);
    } catch (_) {}

    // Clear study patches for this deck from localStorage
    try {
      const patchesRaw = localStorage.getItem(STUDY_PATCHES_KEY);
      if (patchesRaw) {
        const patches = JSON.parse(patchesRaw);
        if (patches?.sets && patches.sets[setId]) {
          delete patches.sets[setId];
          localStorage.setItem(STUDY_PATCHES_KEY, JSON.stringify(patches));
        }
      }
    } catch (_) {}

    // Update emergency backups in localStorage
    try {
      const setRows = await rows('SELECT * FROM sets WHERE id = ? AND deleted_at IS NULL', [String(setId)]);
      if (setRows.length) {
        const set = await hydrateSetRow(setRows[0]);
        rememberSetBackup(set);
      }
    } catch (_) {}

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
    if (file.size && file.size > 80 * 1024 * 1024) {
      throw new Error('Backup is too large to import safely on this device.');
    }

    const raw = await file.text();
    const payload = JSON.parse(raw);
    const data = backup.readBackupData(payload);
    const cardCount = (data.sets || []).reduce((total, set) => total + (Array.isArray(set.cards) ? set.cards.length : 0), 0);
    if (cardCount > MAX_IMPORT_CARD_COUNT) {
      throw new Error(`Backup contains ${cardCount} cards, above the ${MAX_IMPORT_CARD_COUNT} card safety limit.`);
    }
    await createBackupSnapshot('before-mobile-restore');

    const restoredClasses = Array.isArray(data.classes) ? data.classes : [];
    const restoredSets = Array.isArray(data.sets) ? data.sets : [];
    await withTransaction(async () => {
      await run('DELETE FROM classes');
      await run('DELETE FROM cards');
      await run('DELETE FROM sets');
      await run('DELETE FROM progress');
      await run('DELETE FROM state');
      await run('DELETE FROM study_sessions');

      for (const classData of restoredClasses) {
        await upsertClass(schema.normalizeClass(classData, null, { preserveLastModified: true }));
      }
      for (const set of restoredSets) {
        const normalized = schema.normalizeSet(set, null, { preserveLastModified: true });
        await upsertSet(normalized);
        await replaceCardsForSet(normalized.id, normalized.cards || []);
      }

      await run('INSERT OR REPLACE INTO settings (key, value_json, updated_at) VALUES (?, ?, ?)', [
        'app',
        jsonString(schema.normalizeSettings(data.settings || {})),
        Date.now()
      ]);

      for (const [setId, value] of Object.entries(data.progress || {})) {
        await run('INSERT OR REPLACE INTO progress (set_id, value_json, updated_at) VALUES (?, ?, ?)', [
          String(setId),
          jsonString(value),
          Date.now()
        ]);
      }

      for (const [key, value] of Object.entries(data.state || {})) {
        await run('INSERT OR REPLACE INTO state (key, value_json, updated_at) VALUES (?, ?, ?)', [
          String(key),
          jsonString(value),
          Date.now()
        ]);
      }
    });

    clearClassBackups();
    clearSetBackups();
    clearSetStatsCache();
    restoredClasses.forEach(classData => rememberClassBackup(schema.normalizeClass(classData, null, { preserveLastModified: true })));
    restoredSets.forEach(set => rememberSetBackup(schema.normalizeSet(set, null, { preserveLastModified: true })));
    await persist();

    return {
      canceled: false,
      filePath: file.name,
      setCount: restoredSets.length,
      classCount: restoredClasses.length
    };
  }

  async function saveStudySession(session) {
    await ensureReady();
    const { id, setId, startedAt, durationMs, cardsViewed, mode } = session;
    await run('INSERT OR REPLACE INTO study_sessions (id, set_id, started_at, duration_ms, cards_viewed, mode) VALUES (?, ?, ?, ?, ?, ?)', [
      String(id),
      setId ? String(setId) : null,
      Number(startedAt),
      Number(durationMs),
      Number(cardsViewed),
      String(mode)
    ]);
    await persist();
    return true;
  }

  async function getStudySessions(sinceMs) {
    const span = perf?.start('store.study_sessions.list', {
      filteredByStart: sinceMs !== undefined && sinceMs !== null
    });
    await ensureReady();
    let sql = 'SELECT * FROM study_sessions';
    const params = [];
    if (sinceMs !== undefined && sinceMs !== null) {
      sql += ' WHERE started_at >= ?';
      params.push(Number(sinceMs));
    }
    sql += ' ORDER BY started_at ASC';
    const result = await rows(sql, params);
    const sessions = result.map(row => ({
      id: row.id,
      setId: row.set_id,
      startedAt: Number(row.started_at),
      durationMs: Number(row.duration_ms),
      cardsViewed: Number(row.cards_viewed),
      mode: row.mode
    }));
    perf?.end(span, { sessionCount: sessions.length });
    return sessions;
  }

  async function saveImage(dataUrl, meta = {}) {
    return saveDataUrlFile(dataUrl, meta);
  }

  async function deleteImage() {
    return true;
  }

  async function saveFont(dataUrl, meta = {}) {
    return saveDataUrlFile(dataUrl, { ...meta, prefix: meta.prefix || 'font', deckId: meta.deckId || 'fonts' });
  }

  async function listPremadeSets(classId, subjectId) {
    try {
      const manifest = await fetch(`premade-cards/${classId}/${subjectId}/manifest.json`);
      if (manifest.ok) return manifest.json();
    } catch (_error) {}
    return [];
  }


  async function getDiagnostics() {
    const span = perf?.start('store.diagnostics.snapshot');
    await ensureReady();
    const countRows = await rows(`
      SELECT
        (SELECT COUNT(*) FROM sets WHERE deleted_at IS NULL) AS set_count,
        (SELECT COUNT(*) FROM classes WHERE deleted_at IS NULL) AS class_count,
        (SELECT COUNT(*) FROM cards WHERE deleted_at IS NULL) AS card_count,
        (SELECT COUNT(*) FROM progress) AS progress_count,
        (SELECT COUNT(*) FROM state) AS state_count,
        (SELECT COUNT(*) FROM study_sessions) AS study_session_count
    `);
    const counts = countRows[0] || {};
    const result = {
      appName: 'Erudite Flashcards',
      appVersion: 'mobile',
      generatedAt: new Date().toISOString(),
      storageEngine: isNative ? 'SQLite (Capacitor Native)' : 'SQLite (Capacitor WebAssembly)',
      paths: {
        database: DB_PATH,
        backupsDir: BACKUP_DIR
      },
      counts: {
        sets: Number(counts.set_count || 0),
        classes: Number(counts.class_count || 0),
        cards: Number(counts.card_count || 0),
        progressEntries: Number(counts.progress_count || 0),
        stateEntries: Number(counts.state_count || 0),
        studySessions: Number(counts.study_session_count || 0)
      },
      persistence: {
        scheduled: Boolean(_persistTimer),
        inFlight: Boolean(_persistInFlight),
        queued: Boolean(_persistQueued)
      },
      health: {
        status: 'ok',
        issues: []
      },
      recentBackups: [],
      brokenImageLinks: []
    };
    perf?.end(span, { status: 'ok', ...result.counts });
    return result;
  }

  window.eruditeMobileFlashcards = {
    listSets,
    listSetsMeta,
    getSetStatsMeta,
    listCardsForBrowser,
    bulkUpdateCards,
    getSet,
    saveSet,
    replaceSets,
    deleteSet,
    resetDeckSRS,
    saveStudySession,
    getStudySessions,
    listClasses,
    saveClass,
    deleteClass,
    getProgress,
    getAllProgress,
    saveProgress,
    saveCardProgress,
    saveCardProgressBatch,
    getSettings,
    saveSettings,
    getState,
    setState,
    removeState,
    saveImage,
    deleteImage,
    saveFont,
    listPremadeSets,
    getDiagnostics,
    exportBackup,
    createBackupSnapshot,
    importBackup,
    exportDelimited: async () => ({ canceled: true, unsupported: true }),
    importDelimited: async () => ({ canceled: true, unsupported: true }),
    flush
  };

  window.eruditeMobileReady = init();
})();
