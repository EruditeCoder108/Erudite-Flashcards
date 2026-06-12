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
  const DIRECTORY_DATA = 'DATA';
  const DIRECTORY_DOCUMENTS = 'DOCUMENTS';
  const ENCODING_UTF8 = 'utf8';

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

  function rows(sql, params = []) {
    const statement = db.prepare(sql);
    statement.bind(params);
    const result = [];
    while (statement.step()) result.push(statement.getAsObject());
    statement.free();
    return result;
  }

  function run(sql, params = []) {
    const statement = db.prepare(sql);
    statement.run(params);
    statement.free();
  }

  function createSchema() {
    db.exec(`
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

  const DB_TMP_PATH = DB_PATH + '.tmp';
  let _persistTimer = null;
  let _persistInFlight = null;
  let _persistQueued = false;

  async function _doPersist() {
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
  }

  async function persist() {
    // If a write is already scheduled, just mark queued and return the existing promise
    if (_persistTimer) {
      _persistQueued = true;
      return _persistInFlight || Promise.resolve();
    }

    return new Promise((resolve, reject) => {
      _persistTimer = setTimeout(async () => {
        _persistTimer = null;
        _persistQueued = false;

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
            persist().catch(() => {});
          }
        }
      }, 80);
    });
  }

  /** Await any in-flight or scheduled persist. Call before navigation. */
  async function flush() {
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

      // Try main DB file, then temp file as fallback
      db = null;
      for (const path of [DB_PATH, DB_TMP_PATH]) {
        if (db) break;
        try {
          const file = await Filesystem.readFile({ path, directory: DIRECTORY_DATA });
          const candidate = new SQL.Database(base64ToBytes(file.data));
          // Probe query to verify integrity
          candidate.exec('SELECT count(*) FROM sqlite_master;');
          db = candidate;
        } catch (error) {
          console.warn(`[mobile-store] Could not open ${path}:`, error?.message || error);
        }
      }

      const isFresh = !db;
      if (!db) {
        console.warn('[mobile-store] Starting with empty database');
        db = new SQL.Database();
      }

      createSchema();
      // Only persist on first-time setup to avoid a costly full write on every cold start
      if (isFresh) await _doPersist();
      return true;
    })();

    return readyPromise;
  }

  async function ensureReady() {
    await init();
  }

  async function listClasses() {
    await ensureReady();
    return rows('SELECT * FROM classes WHERE deleted_at IS NULL ORDER BY name ASC').map(row => ({
      ...jsonParse(row.payload_json, {}),
      id: row.id,
      name: row.name,
      color: row.color,
      created: Number(row.created),
      lastModified: Number(row.last_modified)
    }));
  }

  function upsertClass(classData) {
    run(`
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
    upsertClass(normalized);
    await persist();
    return normalized;
  }

  async function replaceClasses(classes = [], options = {}) {
    await ensureReady();
    const now = Date.now();
    db.exec(`UPDATE classes SET deleted_at = ${now}, last_modified = ${now} WHERE deleted_at IS NULL;`);
    for (const classData of Array.isArray(classes) ? classes : []) {
      upsertClass(schema.normalizeClass(classData, null, { preserveLastModified: true }));
    }
    if (options.persist !== false) await persist();
    return listClasses();
  }

  async function deleteClass(classId) {
    await ensureReady();
    const now = Date.now();
    run('UPDATE classes SET deleted_at = ?, last_modified = ? WHERE id = ?', [now, now, String(classId)]);
    run('UPDATE sets SET class_id = NULL, last_modified = ? WHERE class_id = ? AND deleted_at IS NULL', [now, String(classId)]);
    await persist();
    return true;
  }

  function upsertSet(set) {
    const payload = { ...set, cards: undefined };
    run(`
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

  function replaceCardsForSet(setId, cards = []) {
    run('DELETE FROM cards WHERE set_id = ?', [String(setId)]);
    cards.forEach((card, index) => {
      run(`
        INSERT INTO cards (
          id, set_id, position, term, definition, term_image, definition_image,
          tags_json, suspended, buried_until, srs_json, review_history_json,
          created, last_modified, deleted_at, payload_json
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, NULL, ?)
      `, [
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
      ]);
    });
  }

  async function listSets() {
    await ensureReady();
    const setRows = rows('SELECT * FROM sets WHERE deleted_at IS NULL ORDER BY last_modified DESC, created DESC');
    return setRows.map(row => hydrateSetRow(row));
  }

  function hydrateSetRow(row) {
    const payload = jsonParse(row.payload_json, {});
    const cards = rows(
      'SELECT * FROM cards WHERE set_id = ? AND deleted_at IS NULL ORDER BY position ASC',
      [row.id]
    ).map(cardRow => hydrateCardRow(cardRow));

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
    const setRows = rows('SELECT * FROM sets WHERE id = ? AND deleted_at IS NULL', [String(id)]);
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

  function buildMetaStatsBySet() {
    const nowMs = Date.now();
    const todayKey = dayKey(nowMs);
    const thirtyDaysAgo = nowMs - 30 * 24 * 60 * 60 * 1000;
    const statsBySet = new Map();
    const dayKeysBySet = new Map();

    rows(`
      SELECT c.set_id, c.srs_json, c.review_history_json, c.suspended, c.buried_until
      FROM cards c
      INNER JOIN sets s ON s.id = c.set_id
      WHERE c.deleted_at IS NULL AND s.deleted_at IS NULL
    `).forEach(row => {
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
    const statsBySet = buildMetaStatsBySet();
    const setRows = rows(`
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
    const setRows = rows('SELECT * FROM sets WHERE id = ? AND deleted_at IS NULL', [String(id)]);
    if (!setRows.length) return null;
    return hydrateSetRow(setRows[0]);
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
    if (metaOnlyUpdate && existing) cleanSet.cards = [];
    const normalized = schema.normalizeSet(cleanSet, existing);
    upsertSet(normalized);
    if (!metaOnlyUpdate) replaceCardsForSet(normalized.id, normalized.cards || []);
    persist(); // fire-and-forget — flush() ensures it completes before navigation
    return normalized;
  }

  async function replaceSets(sets = [], options = {}) {
    await ensureReady();
    const now = Date.now();
    db.exec(`UPDATE sets SET deleted_at = ${now}, last_modified = ${now} WHERE deleted_at IS NULL;`);
    for (const set of Array.isArray(sets) ? sets : []) {
      const normalized = schema.normalizeSet(set, null, { preserveLastModified: true });
      upsertSet(normalized);
      replaceCardsForSet(normalized.id, normalized.cards || []);
    }
    if (options.persist !== false) await persist();
    return listSets();
  }

  async function deleteSet(id) {
    await ensureReady();
    const now = Date.now();
    run('UPDATE sets SET deleted_at = ?, last_modified = ? WHERE id = ?', [now, now, String(id)]);
    run('DELETE FROM progress WHERE set_id = ?', [String(id)]);
    await persist();
    return true;
  }

  async function getSettings() {
    await ensureReady();
    const result = rows('SELECT value_json FROM settings WHERE key = ?', ['app']);
    return schema.normalizeSettings(jsonParse(result[0]?.value_json, {}));
  }

  async function saveSettings(settings = {}) {
    await ensureReady();
    run('INSERT OR REPLACE INTO settings (key, value_json, updated_at) VALUES (?, ?, ?)', [
      'app',
      jsonString(schema.normalizeSettings(settings)),
      Date.now()
    ]);
    await persist();
    return true;
  }

  async function getProgress(setId) {
    await ensureReady();
    const result = rows('SELECT value_json FROM progress WHERE set_id = ?', [String(setId)]);
    return jsonParse(result[0]?.value_json, null);
  }

  async function saveProgress(setId, value) {
    await ensureReady();
    run('INSERT OR REPLACE INTO progress (set_id, value_json, updated_at) VALUES (?, ?, ?)', [
      String(setId),
      jsonString(value),
      Date.now()
    ]);
    persist(); // fire-and-forget — flush() ensures completion before navigation
    return true;
  }

  function getAllProgress() {
    const progress = {};
    rows('SELECT set_id, value_json FROM progress').forEach(row => {
      progress[row.set_id] = jsonParse(row.value_json, null);
    });
    return progress;
  }

  async function replaceProgress(progress = {}, options = {}) {
    db.exec('DELETE FROM progress;');
    for (const [setId, value] of Object.entries(progress || {})) {
      run('INSERT OR REPLACE INTO progress (set_id, value_json, updated_at) VALUES (?, ?, ?)', [
        String(setId),
        jsonString(value),
        Date.now()
      ]);
    }
    if (options.persist !== false) await persist();
    return true;
  }

  async function getState(key) {
    await ensureReady();
    const result = rows('SELECT value_json FROM state WHERE key = ?', [String(key)]);
    return jsonParse(result[0]?.value_json, null);
  }

  async function setState(key, value) {
    await ensureReady();
    run('INSERT OR REPLACE INTO state (key, value_json, updated_at) VALUES (?, ?, ?)', [
      String(key),
      jsonString(value),
      Date.now()
    ]);
    persist();
    return true;
  }

  async function removeState(key) {
    await ensureReady();
    run('DELETE FROM state WHERE key = ?', [String(key)]);
    persist();
    return true;
  }

  function getAllState() {
    const state = {};
    rows('SELECT key, value_json FROM state').forEach(row => {
      state[row.key] = jsonParse(row.value_json, null);
    });
    return state;
  }

  async function replaceState(state = {}, options = {}) {
    db.exec('DELETE FROM state;');
    for (const [key, value] of Object.entries(state || {})) {
      run('INSERT OR REPLACE INTO state (key, value_json, updated_at) VALUES (?, ?, ?)', [
        String(key),
        jsonString(value),
        Date.now()
      ]);
    }
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
      progress: getAllProgress(),
      state: getAllState()
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
      storageEngine: 'SQLite (Capacitor sql.js)',
      paths: {
        database: DB_PATH,
        backupsDir: BACKUP_DIR
      },
      counts: {
        sets: sets.length,
        classes: classes.length,
        cards: sets.reduce((total, set) => total + (Array.isArray(set.cards) ? set.cards.length : 0), 0),
        progressEntries: Object.keys(getAllProgress()).length,
        stateEntries: Object.keys(getAllState()).length
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
    listClasses,
    saveClass,
    deleteClass,
    getProgress,
    saveProgress,
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
