# Erudite Flashcards

Erudite Flashcards is a local-first, offline flashcard app for desktop and Android. It combines normal deck study, FSRS spaced repetition, analytics, rich card creation, and mobile-first workflows without requiring an account or cloud service.

The goal is not to clone Anki screen-for-screen. The goal is Anki-level seriousness with a simpler, more modern interface for students who want to create, review, inspect, and repair their cards locally.

## Current Status

Erudite is now a feature-rich local flashcard system with the major learning workflows in place:

- Desktop app through Electron.
- Android app through Capacitor.
- Local SQLite storage.
- FSRS-based SRS reviews.
- Normal non-SRS study mode.
- Card browser and bulk management tools.
- Today dashboard, insights, failed-card previews, review forecast, streaks, and study analytics.
- Rich creator with formatting, media, math, cloze, image occlusion, reverse cards, and advanced HTML/CSS cards.
- Backup, import, export, and local migration tools.

It is still a local-first independent app, not a mature ecosystem like Anki with years of add-ons, public deck tooling, and battle-tested sync.

## Product Philosophy

Erudite is built around three study modes:

- **Normal study**: Move through a deck in order, reverse order, or random order without SRS pressure.
- **SRS study**: Let FSRS decide which cards are due and when they should return.
- **Custom study**: Focus on failed, weak, overdue, tagged, leech, or filtered groups.

The app intentionally keeps SRS optional. A user can turn SRS off and still use Erudite as a clean local flashcard app. When SRS is on, the app exposes review-focused tools such as due cards, forecast, retention, button distribution, failed cards, and deck health.

## Major Features

### Local And Offline

- Stores decks, cards, classes, settings, review history, and study sessions locally.
- Does not require login, cloud sync, or a server.
- Uses SQLite on desktop and mobile.
- Supports backup/export/import for moving data manually.

### FSRS Spaced Repetition

- Uses FSRS scheduling for SRS reviews.
- Supports Again, Hard, Good, and Easy ratings.
- Tracks card state, due time, interval, stability, difficulty, reps, lapses, and review history.
- Keeps Normal mode progress separate from SRS progress.
- Includes deck-level SRS settings such as requested retention, max interval, daily new limit, and review limit.

### Today And Insights

The Today screen summarizes what matters:

- Due review workload.
- Failed-today preview.
- Weak card count.
- Upcoming review forecast.
- Study streak.
- Review time and session activity.
- Retention/pass-rate style stats.
- Button distribution.
- Study heatmap.
- Leech count.
- Deck health indicators.

SRS-specific stats are intended to appear only when SRS is enabled. SRS-independent stats, such as real study sessions and streak progress, still make sense when SRS is off.

### Card Browser

The card browser is the power-user repair room:

- Search across cards and decks.
- Filter by due, overdue, new, learning, review, relearning, suspended, buried, failed, leech, reverse, cloze, image occlusion, HTML/CSS, no tags, images, and audio.
- Select visible cards.
- Bulk suspend, unsuspend, reset SRS, set due date, move deck, add tags, remove tags, and delete.
- Uses metadata-oriented loading so it can stay usable with large libraries.

### Creator

The creator supports practical mobile card authoring:

- Rich text term and definition editors.
- Bold, italic, underline, highlight, inline code, code block, formula, media, background image, and cloze tools.
- Math/physics formula entry with symbol palette and KaTeX rendering.
- Reverse-card generation.
- Image occlusion card generation from images.
- Advanced HTML/CSS card type with separate front HTML, front CSS, back HTML, and back CSS.
- Copyable AI prompt for asking an external tool like ChatGPT to generate card HTML/CSS.
- Bulk blank-card creation from 1 to 999 cards.
- Insert a card after any card.
- Move cards up/down.
- Delete a single card, or long-press delete to remove that card and every card below it.
- TXT import into the current draft.

### Advanced HTML/CSS Cards

Advanced cards let users paste sanitized HTML/CSS for custom visual flashcards.

Important constraints:

- JavaScript is not allowed inside cards.
- External URLs and imports are stripped.
- Dangerous tags and event attributes are removed.
- Front and back can have separate HTML and CSS.
- The study view renders the card inside an isolated card frame.
- Oversized custom designs can scroll inside the card area.

This gives creative card design power without turning the app into a general-purpose web runtime.

### Study Screen

- Normal mode can study cards without SRS ratings.
- SRS mode shows rating buttons and schedules cards.
- Failed/weak/custom sessions help focus on problem cards.
- Supports media, math, cloze, image occlusion, and HTML/CSS cards.
- Tracks real study sessions so streaks are based on meaningful activity, not only long SRS sessions.

### Backup And Import

- Desktop and mobile storage layers support backup/import flows.
- TXT import supports simple separator-based card creation.
- Copy/export tools help move decks without cloud dependency.
- Deleted premade deck JSON files are not required for user decks.

## Project Structure

```text
.
|-- android/                     Native Android project
|-- assets/                      Shared visual assets
|-- css/                         Desktop CSS
|-- js/
|   |-- core/                    Shared schema, SRS, backup, stats, math helpers
|   |-- mobile/                  Mobile SQLite/storage bridge
|   |-- storage-client.js        Desktop storage client
|   `-- srs-manager.js           SRS queue and scheduling logic
|-- mobile/                      Capacitor mobile HTML/CSS/JS
|-- scripts/                     Build scripts
|-- storage/                     Desktop SQLite storage implementation
|-- www/                         Built mobile web assets
|-- main.js                      Electron main process
|-- preload.js                   Electron preload bridge
`-- package.json
```

## Development

Use `npm.cmd` on Windows.

### Install

```powershell
npm.cmd install
```

### Run Desktop

```powershell
npm.cmd start
```

### Build Mobile Web Assets

```powershell
npm.cmd run build:mobile
```

### Sync Android

Run this after any mobile code change:

```powershell
npm.cmd run cap:sync
```

### Open Android Studio

```powershell
npm.cmd run cap:open
```

### Build Android Debug APK

```powershell
cd android
$env:JAVA_HOME='C:\Program Files\Android\Android Studio\jbr'
.\gradlew.bat :app:assembleDebug
```

## Useful Verification Commands

```powershell
node --check mobile\js\mobile-app.js
node --check mobile\js\mobile-study.js
node --check js\core\schema.js
npm.cmd run build:mobile
npm.cmd run cap:sync
```

## Anki Comparison

Erudite is better than Anki in some specific ways:

- More modern mobile-first interface.
- Simpler normal vs SRS study choice.
- Better built-in dashboard for failed cards, forecast, deck health, and study sessions.
- Easier local card creation for media, formulas, and custom HTML/CSS visuals.
- Offline-first with no account requirement.

Anki is still stronger in other ways:

- Much older and more battle-tested.
- Huge add-on ecosystem.
- Mature sync service.
- Enormous public deck ecosystem.
- Mature template system with broad community knowledge.
- Proven reliability across many years and edge cases.

The honest positioning is:

> Erudite can be a better personal study app for a mobile-first local learner, but it is not yet globally "better than Anki" as an ecosystem.

## License

Business Source License 1.1. See [LICENSE](LICENSE).

## Author

Sambhav Jain  
eruditespartan@gmail.com
