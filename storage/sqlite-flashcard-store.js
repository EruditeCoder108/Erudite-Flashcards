const fs = require('fs/promises');
const path = require('path');

const DB_SCHEMA_VERSION = 2;

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

function getStatementRows(statement, params = []) {
  statement.bind(params);
  const rows = [];
  while (statement.step()) {
    rows.push(statement.getAsObject());
  }
  statement.free();
  return rows;
}

class SqliteFlashcardStore {
  constructor(options) {
    this.SQL = options.SQL;
    this.dataDir = options.dataDir;
    this.backupsDir = options.backupsDir;
    this.dbPath = path.join(this.dataDir, 'erudite-flashcards.sqlite');
    this.normalizers = options.normalizers;
    this.db = null;
    this.persistPromise = Promise.resolve();
  }

  async init() {
    await fs.mkdir(this.dataDir, { recursive: true });
    await fs.mkdir(this.backupsDir, { recursive: true });

    try {
      const existing = await fs.readFile(this.dbPath);
      this.db = new this.SQL.Database(existing);
    } catch (error) {
      if (error.code !== 'ENOENT') throw error;
      this.db = new this.SQL.Database();
    }

    this.createSchema();
    await this.runMigrationsIfNeeded();
    await this.migrateLegacyJsonIfNeeded();
    await this.persist();
    return this;
  }

  createSchema() {
    this.db.exec(`
      PRAGMA foreign_keys = ON;

      CREATE TABLE IF NOT EXISTS meta (
        key TEXT PRIMARY KEY,
        value TEXT NOT NULL
      );

      CREATE TABLE IF NOT EXISTS classes (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        color TEXT NOT NULL,
        created INTEGER NOT NULL,
        last_modified INTEGER NOT NULL,
        deleted_at INTEGER,
        rev INTEGER NOT NULL DEFAULT 1,
        device_id TEXT,
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
        rev INTEGER NOT NULL DEFAULT 1,
        device_id TEXT,
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
        rev INTEGER NOT NULL DEFAULT 1,
        device_id TEXT,
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

      CREATE TABLE IF NOT EXISTS tombstones (
        id TEXT PRIMARY KEY,
        record_type TEXT NOT NULL,
        deleted_at INTEGER NOT NULL,
        rev INTEGER NOT NULL DEFAULT 1,
        device_id TEXT
      );

      CREATE TABLE IF NOT EXISTS review_log (
        id TEXT PRIMARY KEY,
        card_id TEXT NOT NULL,
        note_id TEXT,
        set_id TEXT NOT NULL,
        session_id TEXT NOT NULL,
        rating TEXT NOT NULL,
        previous_state TEXT,
        next_state TEXT,
        previous_due TEXT,
        next_due TEXT,
        previous_interval INTEGER,
        next_interval INTEGER,
        previous_stability REAL,
        next_stability REAL,
        previous_difficulty REAL,
        next_difficulty REAL,
        elapsed_ms INTEGER,
        reviewed_at INTEGER NOT NULL,
        is_preview INTEGER NOT NULL DEFAULT 0,
        undone INTEGER NOT NULL DEFAULT 0,
        undone_at INTEGER,
        device_id TEXT,
        rev INTEGER NOT NULL DEFAULT 1,
        FOREIGN KEY (card_id) REFERENCES cards(id) ON DELETE CASCADE
      );

      CREATE INDEX IF NOT EXISTS idx_sets_class ON sets(class_id);
      CREATE INDEX IF NOT EXISTS idx_sets_visible ON sets(deleted_at, last_modified);
      CREATE INDEX IF NOT EXISTS idx_cards_set_position ON cards(set_id, position);
      CREATE INDEX IF NOT EXISTS idx_cards_visible ON cards(deleted_at);
      CREATE INDEX IF NOT EXISTS idx_revlog_card ON review_log(card_id);
      CREATE INDEX IF NOT EXISTS idx_revlog_time ON review_log(reviewed_at);
      CREATE INDEX IF NOT EXISTS idx_revlog_set ON review_log(set_id);
      CREATE INDEX IF NOT EXISTS idx_revlog_session ON review_log(session_id);
    `);

    if (!this.getMeta('schemaVersion')) {
      this.setMeta('schemaVersion', String(DB_SCHEMA_VERSION));
    }
  }

  async runMigrationsIfNeeded() {
    let currentVersion = Number(this.getMeta('schemaVersion') || 1);
    if (currentVersion < 2) {
      this.db.exec(`
        CREATE TABLE IF NOT EXISTS review_log (
          id TEXT PRIMARY KEY,
          card_id TEXT NOT NULL,
          note_id TEXT,
          set_id TEXT NOT NULL,
          session_id TEXT NOT NULL,
          rating TEXT NOT NULL,
          previous_state TEXT,
          next_state TEXT,
          previous_due TEXT,
          next_due TEXT,
          previous_interval INTEGER,
          next_interval INTEGER,
          previous_stability REAL,
          next_stability REAL,
          previous_difficulty REAL,
          next_difficulty REAL,
          elapsed_ms INTEGER,
          reviewed_at INTEGER NOT NULL,
          is_preview INTEGER NOT NULL DEFAULT 0,
          undone INTEGER NOT NULL DEFAULT 0,
          undone_at INTEGER,
          device_id TEXT,
          rev INTEGER NOT NULL DEFAULT 1,
          FOREIGN KEY (card_id) REFERENCES cards(id) ON DELETE CASCADE
        );
        CREATE INDEX IF NOT EXISTS idx_revlog_card ON review_log(card_id);
        CREATE INDEX IF NOT EXISTS idx_revlog_time ON review_log(reviewed_at);
        CREATE INDEX IF NOT EXISTS idx_revlog_set ON review_log(set_id);
        CREATE INDEX IF NOT EXISTS idx_revlog_session ON review_log(session_id);
      `);

      const selectCardsStatement = this.db.prepare('SELECT id, set_id, review_history_json FROM cards WHERE deleted_at IS NULL');
      const cardRows = getStatementRows(selectCardsStatement);
      
      this.db.exec('BEGIN TRANSACTION');
      try {
        const insertLogStmt = this.db.prepare(`
          INSERT OR IGNORE INTO review_log (
            id, card_id, set_id, session_id, rating,
            previous_state, next_state, previous_due, next_due,
            previous_interval, next_interval, previous_stability, next_stability,
            previous_difficulty, next_difficulty, elapsed_ms, reviewed_at
          ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        `);

        for (const row of cardRows) {
          const history = jsonParse(row.review_history_json, []);
          if (!Array.isArray(history)) continue;

          for (const entry of history) {
            const logId = entry.id || `migration-log-${row.id}-${entry.reviewedAt || entry.time || Date.now()}-${Math.random().toString(36).substring(2, 7)}`;
            const rating = entry.rating || 'Good';
            const reviewedAt = entry.reviewedAt || entry.time || entry.date || Date.now();
            const elapsedMs = entry.elapsedMs || entry.elapsed || 0;
            const sessionId = entry.sessionId || 'migration-session';

            const prevState = entry.previousState || entry.prevState || null;
            const nextState = entry.nextState || entry.state || null;

            const prevDue = entry.previousDue || null;
            const nextDue = entry.nextDue || entry.due || null;

            const prevInterval = entry.previousInterval || entry.prevInterval || 0;
            const nextInterval = entry.nextInterval || entry.interval || 0;

            const prevStability = entry.previousStability || entry.prevStability || 0;
            const nextStability = entry.nextStability || entry.stability || 0;

            const prevDifficulty = entry.previousDifficulty || entry.prevDifficulty || 0;
            const nextDifficulty = entry.nextDifficulty || entry.difficulty || 0;

            insertLogStmt.run([
              logId,
              row.id,
              row.set_id,
              sessionId,
              rating,
              prevState,
              nextState,
              prevDue,
              nextDue,
              prevInterval,
              nextInterval,
              prevStability,
              nextStability,
              prevDifficulty,
              nextDifficulty,
              elapsedMs,
              reviewedAt
            ]);
          }
        }
        insertLogStmt.free();
        this.db.exec('COMMIT');
      } catch (err) {
        this.db.exec('ROLLBACK');
        console.error('Error migrating review history to review_log:', err);
      }

      this.setMeta('schemaVersion', '2');
    }
  }

  getMeta(key) {
    const statement = this.db.prepare('SELECT value FROM meta WHERE key = ?');
    const rows = getStatementRows(statement, [key]);
    return rows[0]?.value ?? null;
  }

  setMeta(key, value) {
    const statement = this.db.prepare('INSERT OR REPLACE INTO meta (key, value) VALUES (?, ?)');
    statement.run([key, String(value)]);
    statement.free();
  }

  countVisibleSets() {
    const statement = this.db.prepare('SELECT COUNT(*) AS count FROM sets WHERE deleted_at IS NULL');
    const rows = getStatementRows(statement);
    return Number(rows[0]?.count || 0);
  }

  async readLegacyJson(name, fallback) {
    try {
      const raw = await fs.readFile(path.join(this.dataDir, name), 'utf8');
      return JSON.parse(raw);
    } catch (_error) {
      return fallback;
    }
  }

  async migrateLegacyJsonIfNeeded() {
    if (this.getMeta('legacyJsonMigrated') === 'true') return;

    const legacySets = await this.readLegacyJson('sets.json', []);
    const legacyClasses = await this.readLegacyJson('classes.json', []);
    const legacySettings = await this.readLegacyJson('settings.json', {});
    const legacyProgress = await this.readLegacyJson('progress.json', {});
    const legacyState = await this.readLegacyJson('state.json', {});
    const hasLegacyData = (
      (Array.isArray(legacySets) && legacySets.length > 0) ||
      (Array.isArray(legacyClasses) && legacyClasses.length > 0) ||
      Object.keys(legacySettings || {}).length > 0 ||
      Object.keys(legacyProgress || {}).length > 0 ||
      Object.keys(legacyState || {}).length > 0
    );

    if (!hasLegacyData || this.countVisibleSets() > 0) {
      this.setMeta('legacyJsonMigrated', 'true');
      return;
    }

    const stamp = new Date().toISOString().replace(/[:.]/g, '-');
    const backupPath = path.join(this.backupsDir, `before-sqlite-migration-${stamp}.json`);
    await fs.writeFile(backupPath, JSON.stringify({
      app: 'Erudite Flashcards',
      schemaVersion: 1,
      exportedAt: new Date().toISOString(),
      reason: 'before-sqlite-migration',
      data: {
        sets: Array.isArray(legacySets) ? legacySets : [],
        classes: Array.isArray(legacyClasses) ? legacyClasses : [],
        settings: legacySettings && typeof legacySettings === 'object' ? legacySettings : {},
        progress: legacyProgress && typeof legacyProgress === 'object' ? legacyProgress : {},
        state: legacyState && typeof legacyState === 'object' ? legacyState : {}
      }
    }, null, 2), 'utf8');

    await this.replaceClasses(Array.isArray(legacyClasses) ? legacyClasses : [], { persist: false });
    await this.replaceSets(Array.isArray(legacySets) ? legacySets : [], { persist: false });

    if (legacySettings && typeof legacySettings === 'object') {
      await this.saveSettings(legacySettings, { persist: false });
    }
    if (legacyProgress && typeof legacyProgress === 'object') {
      for (const [setId, value] of Object.entries(legacyProgress)) {
        await this.saveProgress(setId, value, { persist: false });
      }
    }
    if (legacyState && typeof legacyState === 'object') {
      for (const [key, value] of Object.entries(legacyState)) {
        await this.setState(key, value, { persist: false });
      }
    }

    this.setMeta('legacyJsonMigrated', 'true');
  }

  async persist() {
    this.persistPromise = this.persistPromise.then(async () => {
      const bytes = this.db.export();
      const temp = `${this.dbPath}.${process.pid}.${Date.now()}.${Math.random().toString(36).substring(2, 7)}.tmp`;
      await fs.writeFile(temp, Buffer.from(bytes));
      try {
        await fs.rename(temp, this.dbPath);
      } catch (error) {
        if (error && (error.code === 'EEXIST' || error.code === 'EPERM' || error.code === 'EBUSY')) {
          await fs.copyFile(temp, this.dbPath);
          await fs.rm(temp, { force: true });
          return;
        }
        await fs.rm(temp, { force: true }).catch(() => {});
        throw error;
      }
    });
    return this.persistPromise;
  }

  begin() {
    this.db.exec('BEGIN TRANSACTION;');
  }

  commit() {
    this.db.exec('COMMIT;');
  }

  rollback() {
    try {
      this.db.exec('ROLLBACK;');
    } catch (_error) {}
  }

  upsertClass(classData) {
    const statement = this.db.prepare(`
      INSERT INTO classes (id, name, color, created, last_modified, deleted_at, rev, device_id, payload_json)
      VALUES (?, ?, ?, ?, ?, NULL, COALESCE((SELECT rev + 1 FROM classes WHERE id = ?), 1), ?, ?)
      ON CONFLICT(id) DO UPDATE SET
        name = excluded.name,
        color = excluded.color,
        created = excluded.created,
        last_modified = excluded.last_modified,
        deleted_at = NULL,
        rev = classes.rev + 1,
        device_id = excluded.device_id,
        payload_json = excluded.payload_json
    `);
    statement.run([
      String(classData.id),
      classData.name,
      classData.color,
      Number(classData.created || Date.now()),
      Number(classData.lastModified || Date.now()),
      String(classData.id),
      classData.deviceId || null,
      jsonString(classData)
    ]);
    statement.free();
  }

  upsertSet(set) {
    const payload = { ...set, cards: undefined };
    const statement = this.db.prepare(`
      INSERT INTO sets (
        id, name, description, class_id, srs_settings_json, created, opened_count,
        last_opened, last_modified, deleted_at, rev, device_id, payload_json
      )
      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, NULL, COALESCE((SELECT rev + 1 FROM sets WHERE id = ?), 1), ?, ?)
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
        rev = sets.rev + 1,
        device_id = excluded.device_id,
        payload_json = excluded.payload_json
    `);
    statement.run([
      String(set.id),
      set.name,
      set.description || '',
      set.classId || null,
      jsonString(set.srsSettings || {}),
      Number(set.created || Date.now()),
      Number(set.openedCount || 0),
      set.lastOpened ?? null,
      Number(set.lastModified || Date.now()),
      String(set.id),
      set.deviceId || null,
      jsonString(payload)
    ]);
    statement.free();
  }

  replaceCardsForSet(setId, cards = []) {
    let statement = this.db.prepare('DELETE FROM cards WHERE set_id = ?');
    statement.run([String(setId)]);
    statement.free();

    statement = this.db.prepare(`
      INSERT INTO cards (
        id, set_id, position, term, definition, term_image, definition_image,
        tags_json, suspended, buried_until, srs_json, review_history_json,
        created, last_modified, deleted_at, rev, device_id, payload_json
      )
      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, NULL, COALESCE((SELECT rev + 1 FROM cards WHERE id = ?), 1), ?, ?)
    `);

    cards.forEach((card, index) => {
      statement.run([
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
        String(card.id),
        card.deviceId || null,
        jsonString(card)
      ]);
    });

    statement.free();

    // Backfill review_log rows for the newly replaced cards
    const insertLogStmt = this.db.prepare(`
      INSERT OR IGNORE INTO review_log (
        id, card_id, set_id, session_id, rating,
        previous_state, next_state, previous_due, next_due,
        previous_interval, next_interval, previous_stability, next_stability,
        previous_difficulty, next_difficulty, elapsed_ms, reviewed_at
      ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    `);

    cards.forEach((card) => {
      const history = Array.isArray(card.reviewHistory) ? card.reviewHistory : [];
      for (const entry of history) {
        const logId = entry.id || `import-log-${card.id}-${entry.reviewedAt || entry.time || Date.now()}-${Math.random().toString(36).substring(2, 7)}`;
        const rating = entry.rating || 'Good';
        const reviewedAt = entry.reviewedAt || entry.time || entry.date || Date.now();
        const elapsedMs = entry.elapsedMs || entry.elapsed || 0;
        const sessionId = entry.sessionId || 'import-session';

        const prevState = entry.previousState || entry.prevState || null;
        const nextState = entry.nextState || entry.state || null;

        const prevDue = entry.previousDue || null;
        const nextDue = entry.nextDue || entry.due || null;

        const prevInterval = entry.previousInterval || entry.prevInterval || 0;
        const nextInterval = entry.nextInterval || entry.interval || 0;

        const prevStability = entry.previousStability || entry.prevStability || 0;
        const nextStability = entry.nextStability || entry.stability || 0;

        const prevDifficulty = entry.previousDifficulty || entry.prevDifficulty || 0;
        const nextDifficulty = entry.nextDifficulty || entry.difficulty || 0;

        insertLogStmt.run([
          logId,
          String(card.id),
          String(setId),
          sessionId,
          rating,
          prevState,
          nextState,
          prevDue,
          nextDue,
          prevInterval,
          nextInterval,
          prevStability,
          nextStability,
          prevDifficulty,
          nextDifficulty,
          elapsedMs,
          reviewedAt
        ]);
      }
    });

    insertLogStmt.free();
  }

  rows(sql, params = []) {
    return getStatementRows(this.db.prepare(sql), params);
  }

  count(sql, params = []) {
    const rows = this.rows(sql, params);
    return Number(rows[0]?.count || 0);
  }

  async getDiagnostics() {
    return {
      schemaVersion: this.getMeta('schemaVersion'),
      legacyJsonMigrated: this.getMeta('legacyJsonMigrated') === 'true',
      dbPath: this.dbPath,
      dataDir: this.dataDir,
      backupsDir: this.backupsDir,
      counts: {
        sets: this.count('SELECT COUNT(*) AS count FROM sets WHERE deleted_at IS NULL'),
        deletedSets: this.count('SELECT COUNT(*) AS count FROM sets WHERE deleted_at IS NOT NULL'),
        classes: this.count('SELECT COUNT(*) AS count FROM classes WHERE deleted_at IS NULL'),
        deletedClasses: this.count('SELECT COUNT(*) AS count FROM classes WHERE deleted_at IS NOT NULL'),
        cards: this.count(`
          SELECT COUNT(*) AS count
          FROM cards
          JOIN sets ON sets.id = cards.set_id
          WHERE cards.deleted_at IS NULL AND sets.deleted_at IS NULL
        `),
        cardsInDeletedSets: this.count(`
          SELECT COUNT(*) AS count
          FROM cards
          JOIN sets ON sets.id = cards.set_id
          WHERE cards.deleted_at IS NULL AND sets.deleted_at IS NOT NULL
        `),
        orphanedCards: this.count(`
          SELECT COUNT(*) AS count
          FROM cards
          LEFT JOIN sets ON sets.id = cards.set_id
          WHERE sets.id IS NULL
        `),
        progressRows: this.count('SELECT COUNT(*) AS count FROM progress'),
        stateRows: this.count('SELECT COUNT(*) AS count FROM state'),
        tombstones: this.count('SELECT COUNT(*) AS count FROM tombstones')
      }
    };
  }

  _rowToSet(row, cards) {
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
      lastModified: Number(row.last_modified),
      cards
    };
  }

  _rowToCard(cardRow) {
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

  _loadCardsForSet(setId) {
    return this.rows(
      'SELECT * FROM cards WHERE set_id = ? AND deleted_at IS NULL ORDER BY position ASC',
      [setId]
    ).map(cardRow => this._rowToCard(cardRow));
  }

  async listSets() {
    const setRows = this.rows('SELECT * FROM sets WHERE deleted_at IS NULL ORDER BY last_modified DESC, created DESC');
    return setRows.map(row => this._rowToSet(row, this._loadCardsForSet(row.id)));
  }

  /**
   * Returns set metadata and card counts without loading card content.
   * Much faster than listSets() for the library screen.
   */
  async listSetsMeta() {
    const setRows = this.rows(`
      SELECT s.*, COUNT(c.id) AS card_count
      FROM sets s
      LEFT JOIN cards c ON c.set_id = s.id AND c.deleted_at IS NULL
      WHERE s.deleted_at IS NULL
      GROUP BY s.id
      ORDER BY s.last_modified DESC, s.created DESC
    `);
    return setRows.map(row => {
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
        lastModified: Number(row.last_modified),
        cardCount: Number(row.card_count || 0)
      };
    });
  }

  async getSet(id) {
    const setRows = this.rows('SELECT * FROM sets WHERE id = ? AND deleted_at IS NULL LIMIT 1', [String(id)]);
    if (!setRows.length) return null;
    const row = setRows[0];
    const cards = this._loadCardsForSet(row.id);
    return this._rowToSet(row, cards);
  }

  async saveSet(rawSet) {
    const id = rawSet.id || this.normalizers.generateId('set');
    const existing = await this.getSet(id);
    const normalized = await this.normalizers.normalizeSet({ ...rawSet, id }, existing);

    this.begin();
    try {
      this.upsertSet(normalized);
      this.replaceCardsForSet(normalized.id, normalized.cards || []);
      this.commit();
    } catch (error) {
      this.rollback();
      throw error;
    }

    await this.persist();
    return normalized;
  }

  async replaceSets(rawSets = [], options = {}) {
    const normalizedSets = [];
    const seen = new Set();

    for (const rawSet of Array.isArray(rawSets) ? rawSets : []) {
      if (!rawSet) continue;
      const id = rawSet.id || this.normalizers.generateId('set');
      if (seen.has(String(id))) continue;
      seen.add(String(id));
      normalizedSets.push(await this.normalizers.normalizeSet({ ...rawSet, id }, null, { preserveLastModified: true }));
    }

    const now = Date.now();
    this.begin();
    try {
      this.db.exec(`UPDATE sets SET deleted_at = ${now}, last_modified = ${now} WHERE deleted_at IS NULL;`);
      for (const set of normalizedSets) {
        this.upsertSet(set);
        this.replaceCardsForSet(set.id, set.cards || []);
      }
      this.commit();
    } catch (error) {
      this.rollback();
      throw error;
    }

    if (options.persist !== false) await this.persist();
    return this.listSets();
  }

  async deleteSet(id) {
    const now = Date.now();
    this.begin();
    try {
      let statement = this.db.prepare('UPDATE sets SET deleted_at = ?, last_modified = ?, rev = rev + 1 WHERE id = ?');
      statement.run([now, now, String(id)]);
      statement.free();
      statement = this.db.prepare('INSERT OR REPLACE INTO tombstones (id, record_type, deleted_at, rev) VALUES (?, ?, ?, COALESCE((SELECT rev + 1 FROM tombstones WHERE id = ?), 1))');
      statement.run([String(id), 'set', now, String(id)]);
      statement.free();
      statement = this.db.prepare('DELETE FROM progress WHERE set_id = ?');
      statement.run([String(id)]);
      statement.free();
      this.commit();
    } catch (error) {
      this.rollback();
      throw error;
    }
    await this.persist();
    return true;
  }

  async listClasses() {
    return this.rows('SELECT * FROM classes WHERE deleted_at IS NULL ORDER BY name ASC').map(row => ({
      ...jsonParse(row.payload_json, {}),
      id: row.id,
      name: row.name,
      color: row.color,
      created: Number(row.created),
      lastModified: Number(row.last_modified)
    }));
  }

  async saveClass(rawClass) {
    const classes = await this.listClasses();
    const id = rawClass.id || this.normalizers.generateId('class');
    const existing = classes.find(classItem => String(classItem.id) === String(id));
    const normalized = this.normalizers.normalizeClass({ ...rawClass, id }, existing);
    normalized.lastModified = Date.now();

    this.begin();
    try {
      this.upsertClass(normalized);
      this.commit();
    } catch (error) {
      this.rollback();
      throw error;
    }
    await this.persist();
    return normalized;
  }

  async replaceClasses(rawClasses = [], options = {}) {
    const normalizedClasses = [];
    const seen = new Set();

    for (const rawClass of Array.isArray(rawClasses) ? rawClasses : []) {
      if (!rawClass) continue;
      const normalized = this.normalizers.normalizeClass(rawClass);
      if (seen.has(String(normalized.id))) continue;
      seen.add(String(normalized.id));
      normalizedClasses.push(normalized);
    }

    const now = Date.now();
    this.begin();
    try {
      this.db.exec(`UPDATE classes SET deleted_at = ${now}, last_modified = ${now} WHERE deleted_at IS NULL;`);
      normalizedClasses.forEach(classData => this.upsertClass(classData));
      this.commit();
    } catch (error) {
      this.rollback();
      throw error;
    }

    if (options.persist !== false) await this.persist();
    return this.listClasses();
  }

  async deleteClass(classId) {
    const now = Date.now();
    this.begin();
    try {
      let statement = this.db.prepare('UPDATE classes SET deleted_at = ?, last_modified = ?, rev = rev + 1 WHERE id = ?');
      statement.run([now, now, String(classId)]);
      statement.free();
      statement = this.db.prepare('UPDATE sets SET class_id = NULL, last_modified = ?, rev = rev + 1 WHERE class_id = ? AND deleted_at IS NULL');
      statement.run([now, String(classId)]);
      statement.free();
      statement = this.db.prepare('INSERT OR REPLACE INTO tombstones (id, record_type, deleted_at, rev) VALUES (?, ?, ?, COALESCE((SELECT rev + 1 FROM tombstones WHERE id = ?), 1))');
      statement.run([String(classId), 'class', now, String(classId)]);
      statement.free();
      this.commit();
    } catch (error) {
      this.rollback();
      throw error;
    }
    await this.persist();
    return true;
  }

  async getSettings() {
    const rows = this.rows('SELECT value_json FROM settings WHERE key = ?', ['app']);
    return jsonParse(rows[0]?.value_json, {});
  }

  async saveSettings(settings = {}, options = {}) {
    const statement = this.db.prepare('INSERT OR REPLACE INTO settings (key, value_json, updated_at) VALUES (?, ?, ?)');
    statement.run(['app', jsonString(settings || {}), Date.now()]);
    statement.free();
    if (options.persist !== false) await this.persist();
    return true;
  }

  async getProgress(setId) {
    const rows = this.rows('SELECT value_json FROM progress WHERE set_id = ?', [String(setId)]);
    return jsonParse(rows[0]?.value_json, null);
  }

  async saveProgress(setId, value, options = {}) {
    const statement = this.db.prepare('INSERT OR REPLACE INTO progress (set_id, value_json, updated_at) VALUES (?, ?, ?)');
    statement.run([String(setId), jsonString(value), Date.now()]);
    statement.free();
    if (options.persist !== false) await this.persist();
    return true;
  }

  async getAllProgress() {
    const progress = {};
    this.rows('SELECT set_id, value_json FROM progress').forEach(row => {
      progress[row.set_id] = jsonParse(row.value_json, null);
    });
    return progress;
  }

  async replaceProgress(progress = {}, options = {}) {
    this.db.exec('DELETE FROM progress;');
    for (const [setId, value] of Object.entries(progress || {})) {
      await this.saveProgress(setId, value, { persist: false });
    }
    if (options.persist !== false) await this.persist();
    return true;
  }

  async getState(key) {
    const rows = this.rows('SELECT value_json FROM state WHERE key = ?', [String(key)]);
    return jsonParse(rows[0]?.value_json, null);
  }

  async setState(key, value, options = {}) {
    const statement = this.db.prepare('INSERT OR REPLACE INTO state (key, value_json, updated_at) VALUES (?, ?, ?)');
    statement.run([String(key), jsonString(value), Date.now()]);
    statement.free();
    if (options.persist !== false) await this.persist();
    return true;
  }

  async removeState(key) {
    const statement = this.db.prepare('DELETE FROM state WHERE key = ?');
    statement.run([String(key)]);
    statement.free();
    await this.persist();
    return true;
  }

  async getAllState() {
    const state = {};
    this.rows('SELECT key, value_json FROM state').forEach(row => {
      state[row.key] = jsonParse(row.value_json, null);
    });
    return state;
  }

  async replaceState(state = {}, options = {}) {
    this.db.exec('DELETE FROM state;');
    for (const [key, value] of Object.entries(state || {})) {
      await this.setState(key, value, { persist: false });
    }
    if (options.persist !== false) await this.persist();
    return true;
  }

  async recordReview({ cardId, rating, previousSrs, nextSrs, reviewedAt, elapsedMs, sessionId }) {
    const cardRows = this.rows('SELECT * FROM cards WHERE id = ? LIMIT 1', [String(cardId)]);
    if (!cardRows.length) throw new Error('Card not found: ' + cardId);
    const cardRow = cardRows[0];
    const card = this._rowToCard(cardRow);

    const newHistoryEntry = {
      id: `log-${cardId}-${reviewedAt}-${Math.random().toString(36).substring(2, 7)}`,
      rating,
      time: reviewedAt,
      elapsed: elapsedMs,
      sessionId,
      previousState: previousSrs?.state || 'New',
      nextState: nextSrs?.state || 'New',
      previousDue: previousSrs?.due || null,
      nextDue: nextSrs?.due || null,
      previousInterval: previousSrs?.interval || 0,
      nextInterval: nextSrs?.interval || 0,
      previousStability: previousSrs?.stability || 0,
      nextStability: nextSrs?.stability || 0,
      previousDifficulty: previousSrs?.difficulty || 0,
      nextDifficulty: nextSrs?.difficulty || 0
    };

    const reviewHistory = Array.isArray(card.reviewHistory) ? [...card.reviewHistory, newHistoryEntry] : [newHistoryEntry];
    card.srs = nextSrs;
    card.reviewHistory = reviewHistory;

    this.begin();
    try {
      let stmt = this.db.prepare('UPDATE cards SET srs_json = ?, review_history_json = ?, payload_json = ?, last_modified = ?, rev = rev + 1 WHERE id = ?');
      stmt.run([
        jsonString(nextSrs),
        jsonString(reviewHistory),
        jsonString(card),
        Date.now(),
        String(cardId)
      ]);
      stmt.free();

      stmt = this.db.prepare(`
        INSERT INTO review_log (
          id, card_id, set_id, session_id, rating,
          previous_state, next_state, previous_due, next_due,
          previous_interval, next_interval, previous_stability, next_stability,
          previous_difficulty, next_difficulty, elapsed_ms, reviewed_at,
          is_preview, undone, rev
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0, 0, 1)
      `);
      stmt.run([
        newHistoryEntry.id,
        String(cardId),
        String(cardRow.set_id),
        String(sessionId),
        String(rating),
        newHistoryEntry.previousState,
        newHistoryEntry.nextState,
        newHistoryEntry.previousDue,
        newHistoryEntry.nextDue,
        newHistoryEntry.previousInterval,
        newHistoryEntry.nextInterval,
        newHistoryEntry.previousStability,
        newHistoryEntry.nextStability,
        newHistoryEntry.previousDifficulty,
        newHistoryEntry.nextDifficulty,
        elapsedMs,
        reviewedAt
      ]);
      stmt.free();

      this.commit();
    } catch (error) {
      this.rollback();
      throw error;
    }

    await this.persist();
    return card;
  }

  async undoReviewLog(cardId, logId) {
    const logRows = this.rows('SELECT * FROM review_log WHERE id = ? AND card_id = ? LIMIT 1', [String(logId), String(cardId)]);
    if (!logRows.length) throw new Error('Review log not found: ' + logId);
    const log = logRows[0];

    const cardRows = this.rows('SELECT * FROM cards WHERE id = ? LIMIT 1', [String(cardId)]);
    if (!cardRows.length) throw new Error('Card not found: ' + cardId);
    const cardRow = cardRows[0];
    const card = this._rowToCard(cardRow);

    const previousSrs = log.previous_state ? {
      state: log.previous_state,
      due: log.previous_due || null,
      interval: Number(log.previous_interval || 0),
      stability: Number(log.previous_stability || 0),
      difficulty: Number(log.previous_difficulty || 0)
    } : null;

    const reviewHistory = Array.isArray(card.reviewHistory)
      ? card.reviewHistory.filter(entry => String(entry.id) !== String(logId))
      : [];

    card.srs = previousSrs || undefined;
    card.reviewHistory = reviewHistory;

    this.begin();
    try {
      let stmt = this.db.prepare('UPDATE cards SET srs_json = ?, review_history_json = ?, payload_json = ?, last_modified = ?, rev = rev + 1 WHERE id = ?');
      stmt.run([
        jsonString(previousSrs),
        jsonString(reviewHistory),
        jsonString(card),
        Date.now(),
        String(cardId)
      ]);
      stmt.free();

      stmt = this.db.prepare('UPDATE review_log SET undone = 1, undone_at = ?, rev = rev + 1 WHERE id = ?');
      stmt.run([Date.now(), String(logId)]);
      stmt.free();

      this.commit();
    } catch (error) {
      this.rollback();
      throw error;
    }

    await this.persist();
    return card;
  }

  async createDeckBackup(setId) {
    const set = await this.getSet(setId);
    if (!set) throw new Error('Set not found: ' + setId);

    const stamp = new Date().toISOString().replace(/[:.]/g, '-');
    const backupPath = path.join(this.backupsDir, `set_backup_RESET_${setId}-${stamp}.json`);

    const backupContent = {
      app: 'Erudite Flashcards',
      backupType: 'reset-deck-srs',
      exportedAt: new Date().toISOString(),
      setData: set
    };

    await fs.writeFile(backupPath, JSON.stringify(backupContent, null, 2), 'utf8');
    return backupPath;
  }

  async resetDeckSRS(setId, deleteHistory) {
    const cardRows = this.rows('SELECT * FROM cards WHERE set_id = ? AND deleted_at IS NULL', [String(setId)]);

    this.begin();
    try {
      for (const cardRow of cardRows) {
        const card = this._rowToCard(cardRow);
        card.srs = undefined;
        if (deleteHistory) {
          card.reviewHistory = [];
        }

        let stmt = this.db.prepare('UPDATE cards SET srs_json = NULL, review_history_json = ?, payload_json = ?, last_modified = ?, rev = rev + 1 WHERE id = ?');
        stmt.run([
          jsonString(card.reviewHistory),
          jsonString(card),
          Date.now(),
          String(card.id)
        ]);
        stmt.free();
      }

      if (deleteHistory) {
        let stmt = this.db.prepare('DELETE FROM review_log WHERE set_id = ?');
        stmt.run([String(setId)]);
        stmt.free();
      }

      // Reset SRS progress inside progress table
      const progressRows = this.rows('SELECT value_json FROM progress WHERE set_id = ? LIMIT 1', [String(setId)]);
      if (progressRows.length) {
        const progress = jsonParse(progressRows[0].value_json, {});
        progress.srsModeIndex = 0;
        progress.srsReviewedCardIds = [];
        progress.timestamp = Date.now();

        let stmtProgress = this.db.prepare('UPDATE progress SET value_json = ?, updated_at = ? WHERE set_id = ?');
        stmtProgress.run([
          jsonString(progress),
          Date.now(),
          String(setId)
        ]);
        stmtProgress.free();
      }

      this.commit();
    } catch (error) {
      this.rollback();
      throw error;
    }

    await this.persist();
    return true;
  }
}

module.exports = {
  SqliteFlashcardStore
};
