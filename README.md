# Erudite Flashcards

Erudite Flashcards is a local-first spaced repetition system (SRS) flashcard application designed for high-performance learning. It features a responsive web interface running within Electron on desktop platforms and Capacitor on mobile platforms, utilizing native SQLite for robust local-first storage.

## Key Features

- **Local-First Database Architecture**: Completely local storage using SQLite. Fast local reads and writes prevent cloud latency issues.
- **FSRS Spaced Repetition**: Integrates the Free Spaced Repetition Scheduler (FSRS) algorithm for optimal review intervals and high retention.
- **Cross-Platform Syncing & Backups**: Automated backups and manual export/import utilities for deck migration.
- **Undo System**: Session-level undo stack allowing users to easily reverse scheduling mistakes or card ratings.
- **Advanced SRS Controls**: Deck-level settings including maximum interval limits, requested retention tuning, and a clean database reset tool.

## Project Structure

### Desktop & Shared Shell
- `main.js`: Core Electron main process managing desktop window creation, menu setups, and database IPC handlers.
- `preload.js`: IPC bridge between the Electron main process and the browser application context.
- `js/storage-client.js`: IPC client wrapper providing a unified promise-based interface to the storage layer.
- `storage/sqlite-flashcard-store.js`: Desktop storage provider implementing direct SQLite database calls and schemas.
- `js/srs-manager.js`: Spaced repetition state scheduler and queue controller.
- `js/core/`: Core cross-platform logic library:
  - `schema.js`: Set, class, and card validation and normalization.
  - `srs.js`: FSRS mathematical calculations and default parameters.
  - `backup.js`: Database serialization and export helpers.
  - `stats.js`: Aggregate calculations for workload and retention.
  - `math-render.js`: KaTeX-based mathematical markup rendering.

### Mobile Shell
- `mobile/`: Web views, assets, and styling for the Capacitor mobile application.
- `js/mobile/mobile-store.js`: Mobile storage provider utilizing Capacitor SQLite native plugins on Android/iOS, with a WebAssembly SQL.js fallback for development environments.
- `android/`: Native Android project configurations and assets.

### HTML User Interfaces
- `flashcards.html`: Main application interface containing the dashboard, My Sets library, Premade library view, class management, and global settings.
- `study.html`: Study session and card rating interface.
- `creator.html`: Flashcard creation and editor interface.
- `card-browser.html`: Database browser interface for bulk viewing, filtering, and managing cards.
- `diagnostics.html`: Application health checks, database integrity tools, and backup/restore dashboard.

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

2. To build the APK directly from the command line:
   ```bash
   cd android
   ./gradlew assembleDebug      # Builds debug APK (for testing)
   ./gradlew assembleRelease    # Builds release APK (unsigned)
   ```
   The built APKs will be located under `android/app/build/outputs/apk/`.

3. To open the project configuration inside Android Studio:
   ```bash
   npm run cap:open
   ```

---

## Technical Specifications

### Spaced Repetition Schema

Reviews are tracked on desktop using an append-only `review_log` database structure:

```sql
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
```

---

## Author & License

- **Author**: Sambhav Jain
- **Email**: eruditespartan@gmail.com
- **License**: Business Source License 1.1 (BSL 1.1) - see [LICENSE](file:///d:/productivity-toolkit/Erudite-flashcards/LICENSE) for details.
