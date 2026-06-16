# Erudite Flashcards

Erudite Flashcards is a local-first spaced repetition system (SRS) flashcard application designed for high-performance learning. It features a responsive web interface running within Electron on desktop platforms and Capacitor on mobile platforms, utilizing native SQLite for robust local-first storage.

## Key Features

- **Local-First Database Architecture**: Completely local storage using SQLite. Fast local reads and writes prevent cloud latency issues.
- **FSRS Spaced Repetition**: Integrates the Free Spaced Repetition Scheduler (FSRS) algorithm for optimal review intervals and high retention.
- **Cross-Platform Syncing & Backups**: Automated backups and manual export/import utilities for deck migration.
- **Undo System**: Session-level undo stack allowing users to easily reverse scheduling mistakes or card ratings.
- **Advanced SRS Controls**: Deck-level settings including maximum interval limits, requested retention tuning, and a clean database reset tool.

## Project Structure

- `main.js`: Core Electron main process managing desktop window creation, menu setups, and database IPC handlers.
- `preload.js`: IPC bridge between the Electron main process and the browser application context.
- `storage/sqlite-flashcard-store.js`: Desktop storage provider implementing direct SQLite database calls and schemas.
- `js/mobile/mobile-store.js`: Mobile storage provider utilizing Capacitor SQLite native plugins on Android/iOS, with a WebAssembly SQL.js fallback for development environments.
- `js/core/`: Core cross-platform logic library:
  - `schema.js`: Set, class, and card validation and normalization.
  - `srs.js`: FSRS mathematical calculations and default parameters.
  - `backup.js`: Database serialization and export helpers.
  - `stats.js`: Aggregate calculations for workload and retention.
  - `math-render.js`: KaTeX-based mathematical markup rendering.
- `js/srs-manager.js`: Spaced repetition state scheduler and queue controller.
- `mobile/`: Web views and asset styling for the Capacitor mobile application.
- `android/`: Native Android project configurations.

## Development Setup

### Prerequisites

- Node.js (v18 or higher recommended)
- Android Studio and Android SDK (for mobile builds)
- C++ build tools (required for local SQLite compilation on desktop)

### Installation

Clone the repository and install dependencies:

```bash
npm install
```

### Running the Desktop App

To run the Electron desktop application locally:

```bash
npm start
```

To build a portable desktop executable:

```bash
npm run package
```

### Building and Deploying to Mobile (Android)

1. Compile the web assets and synchronize them to the Capacitor Android project:
   ```bash
   npm run cap:sync
   ```

2. Open the project in Android Studio:
   ```bash
   npm run cap:open
   ```

3. Run the application from Android Studio to a connected device or an emulator using the run button.

---

## Technical Specifications & Roadmap

The application is undergoing active development to introduce advanced Anki-level spaced repetition features.

### Spaced Repetition Schema

Reviews are tracked using an append-only `review_log` database structure:

```sql
CREATE TABLE IF NOT EXISTS review_log (
  id TEXT PRIMARY KEY,
  card_id TEXT NOT NULL,
  note_id TEXT,
  set_id TEXT NOT NULL,
  session_id TEXT,
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
  device_id TEXT,
  rev INTEGER NOT NULL DEFAULT 1,
  FOREIGN KEY (card_id) REFERENCES cards(id) ON DELETE CASCADE
);
```

### Phased Roadmap

#### Phase 1: Review Log, Undo, and Manual Actions (Completed)
- Transaction-level scheduling integrity via raw SQLite backend.
- Full undo support inside the study session (max stack depth 10) mapped to Ctrl+Z/Z.
- Card actions: Suspend, Bury, and Manual Due Dates.
- Danger Zone settings with deck reset capabilities.

#### Phase 2: Browser Power Tools (Planned)
- Implement bulk operations on the card browser interface.
- Add features for bulk suspending/unsuspending, bulk resetting, bulk deleting, and bulk moving cards to different sets.
- Improve advanced filter categories for card state queries.

#### Phase 3: Analytics Dashboard (Planned)
- Integrate analytical calculations directly from the `review_log` table.
- Calculate True Retention rates across 7-day, 30-day, and 90-day mature card cohorts.
- Display workloads forecasts, daily study durations, and rating button ratios.

#### Phase 4: Filtered Decks & Custom Study (Planned)
- Generate virtual temporary study decks using query strings.
- Add Preview Study Mode logging reviews without modifying base FSRS metadata.

#### Phase 5: Note/Card Separation (Planned)
- Relational schema upgrade separating content fields from practice card templates.
- Support sibling burying to prevent cognitive redundancy within study sessions.

---

## Author & License

- **Author**: Sambhav Jain
- **Email**: eruditespartan@gmail.com
- **License**: Private / Proprietary
