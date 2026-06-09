# Erudite Flashcards Vision And Roadmap

## 1. Product North Star

Erudite Flashcards should become a serious, beautiful, local-first flashcard app for students who want the power of Anki without the friction, and the comfort of Quizlet without the lock-in, noise, or weak scheduling.

The core promise:

> Own your study system. Study beautifully. Remember reliably.

Erudite is not trying to be another generic flashcard app. It is trying to become the best middle path between:

- Anki: powerful, trusted, flexible, excellent for long-term memory, but intimidating and visually dated.
- Quizlet: smooth, familiar, pleasant, and mainstream, but more cloud-first, subscription-driven, and less serious for advanced spaced repetition.

The product should feel calm, fast, trustworthy, and private. A student should be able to install it, create or import cards, study offline, back up their data, sync later, and feel that their learning belongs to them.

## 2. Positioning

### One-line positioning

Erudite Flashcards is a local-first SRS app for serious learners who want modern UX, strong memory science, and full ownership of their study data.

### Short positioning

Erudite combines FSRS-powered review scheduling, a polished creator, a focused study mode, local SQLite storage, desktop/mobile availability, and offline-first sync so students can study seriously without accounts, subscriptions, ads, or cloud lock-in.

### What Erudite should be known for

- Serious studying without Anki's rough edges.
- Modern UI without Quizlet's gimmick-heavy feeling.
- Local-first data ownership.
- Smooth desktop plus mobile workflow.
- Reliable backups and sync.
- Powerful import paths, especially from Anki.
- Calm daily review experience.

### What Erudite should not be

- A clone of Anki.
- A clone of Quizlet.
- A social learning network.
- A noisy gamified app.
- An AI wrapper pretending to be a study system.
- A cloud-first app that happens to have offline mode.
- A beautiful app that risks user data.

## 3. Core Principles

### 3.1 Local-first by default

The app should work without an account and without the internet. The user's library should live on their own device first.

Required implications:

- Desktop data is stored locally in SQLite.
- Mobile data should also be stored locally.
- Cloud should never be required for basic studying.
- Backup and restore should be visible, understandable, and reliable.
- Sync should be additive to local ownership, not a replacement for it.

### 3.2 Trust beats features

Students will only rely on Erudite if they trust it with months or years of learning data.

Trust requires:

- No silent data loss.
- No mysterious progress resets.
- No broken media after restart.
- No accidental overwrite during restore or sync.
- Clear diagnostics.
- Clear backup locations.
- Clear recovery paths.

### 3.3 Memory science should be serious

SRS is not decoration. It is the core learning engine.

Erudite should:

- Use FSRS as the default scheduler.
- Show rating interval previews.
- Track review history.
- Support per-deck SRS settings.
- Make due cards easy to find.
- Avoid vague wording like "smart review" without transparency.
- Eventually support FSRS parameter optimization from user history.

### 3.4 UI should be calm and useful

The app should feel premium through restraint, not through visual noise.

UI direction:

- Study mode should be the calmest screen.
- Creator should be efficient and keyboard-friendly.
- Library should help organize, search, and resume studying quickly.
- Mobile should feel native and thumb-friendly.
- Visual effects should support comprehension, not compete with content.

### 3.5 Desktop and mobile should have different strengths

Desktop is best for creation, bulk editing, imports, backups, diagnostics, and organization.

Mobile is best for quick reviews, daily streaks, touch interactions, offline studying, and carrying the library everywhere.

The product should embrace this split instead of forcing every screen to behave the same on every device.

### 3.6 AI is optional and deferred

AI can be valuable later, but it should not define the product now.

Near-term focus:

- Reliable SRS.
- Mobile.
- Sync.
- Imports.
- Creator polish.
- Study polish.
- Data safety.

Future AI direction:

- Optional local or bring-your-own provider.
- No cloud dependency for core use.
- No AI promises before the foundation is excellent.

## 4. Current State

As of the current development phase, Erudite already has a serious base.

### Existing foundations

- Electron desktop app.
- Windows packaging through electron-builder.
- Local SQLite storage through the app data directory.
- `flashcardStore` storage boundary.
- FSRS scheduling through `ts-fsrs`.
- Library page.
- Creator page.
- Study page.
- Premade library page.
- Card browser page.
- Diagnostics page.
- Classes for organizing sets.
- JSON backup and restore direction.
- CSV/TSV exchange direction.
- Images stored locally.
- Per-deck SRS settings direction.
- Rating interval previews.
- Review due flow across decks.
- Themes through settings.
- Local-first identity.

### Current weaknesses

- Mobile app does not exist yet.
- Sync does not exist yet.
- Anki `.apkg` import/export does not exist yet.
- Cloze deletion does not exist yet.
- Image occlusion does not exist yet.
- Typed answer mode does not exist yet.
- Advanced review history and stats are still incomplete.
- Some legacy code remains from extraction.
- Automated test coverage is limited.
- Public onboarding and documentation are missing.
- Product identity is not yet packaged into a public release story.

## 5. Target Users

### Primary users

Serious students who want long-term retention but dislike Anki's complexity.

Examples:

- Medical students.
- Law students.
- Language learners.
- Competitive exam students.
- STEM students.
- Self-learners working through books or courses.

### Secondary users

- Students who use Quizlet but want better SRS.
- Students who use Anki but want a nicer creator and mobile experience.
- Privacy-conscious learners who dislike account-first products.
- Teachers or tutors who want to distribute local decks later.

### Early adopter profile

The first ideal user is not everyone. The first ideal user is:

- Already convinced flashcards work.
- Frustrated with Anki or Quizlet.
- Values offline access.
- Has enough technical patience for an early product.
- Wants a polished study experience.
- Is willing to pay for ownership and reliability.

## 6. Market Gap

The market is crowded, but the gap is still real.

### Anki's strengths

- Trusted.
- Powerful.
- Mature ecosystem.
- Huge deck compatibility.
- Excellent long-term memory workflows.
- Advanced customization.

### Anki's weaknesses

- Intimidating for beginners.
- UI feels dated to many users.
- Creator can feel technical.
- Mobile experience is not as friendly as mainstream study apps.
- Many workflows require add-ons or configuration.

### Quizlet's strengths

- Smooth and familiar.
- Easy for beginners.
- Large content network.
- Good mobile experience.
- Strong brand among students.

### Quizlet's weaknesses

- Less serious for advanced SRS users.
- More cloud/account/subscription oriented.
- More gimmicky.
- Less ownership-centered.
- Not ideal for students who want full control of long-term review data.

### Erudite's opportunity

Erudite can win by being:

- Easier than Anki.
- More serious than Quizlet.
- More private than both.
- More ownership-centered than cloud-first tools.
- Better designed than hobby flashcard clones.

## 7. Product Pillars

### 7.1 Study

Study mode is the heart of the app. If this screen feels wrong, the product fails.

Study mode should provide:

- Normal study mode.
- SRS review mode.
- Clear progress.
- Smooth flip.
- Keyboard shortcuts.
- Touch gestures.
- Image zoom.
- Long text handling.
- No rating button overlap.
- Session summary.
- Continue due review across decks.
- No unnecessary toasts or interruptions.

Future study additions:

- Typed answer.
- Cloze review.
- Image occlusion review.
- Audio cards.
- Reverse cards.
- Bury/suspend/reset actions.
- Session goals.
- Review queue preview.

### 7.2 Create

Creator should make card creation faster and less painful than Anki.

Creator should provide:

- Rich text.
- Images on term and definition.
- Bulk import.
- Class assignment.
- Draft recovery.
- Autosave.
- Keyboard shortcuts.
- Easy add/delete/reorder.
- Good focus handling.
- Import/export help.

Future creator additions:

- Cloze creation.
- Image occlusion editor.
- Card templates.
- Reverse card toggle.
- Typed-answer toggle.
- Tags.
- Better table/spreadsheet paste.
- PDF/text extraction later.
- AI generation later only after core reliability.

### 7.3 Organize

Library should make it easy to understand and manage the study system.

Library should provide:

- All sets view.
- General view.
- Classes view.
- Search.
- Sort.
- Set cards.
- Class cards.
- SRS dashboard when SRS is on.
- Due review entry point.
- Settings.
- Backup/restore.
- Diagnostics.

Future organization additions:

- Tags.
- Folders or nested decks.
- Favorites.
- Archived decks.
- Suspended cards summary.
- Duplicate detector.
- Bulk deck operations.

### 7.4 Browse

Card browser is essential for serious users.

Card browser should provide:

- Search across all cards.
- Filter by deck/class/state/tag.
- Edit individual cards.
- Delete individual cards.
- Suspend/unsuspend.
- Reset SRS.
- Sort by due date, reps, state, deck, last review.

Future browser additions:

- Bulk edit.
- Bulk suspend.
- Bulk tag.
- Review history per card.
- Duplicate detection.
- Import cleanup tools.

### 7.5 Protect

Data safety is a feature.

Protection should include:

- SQLite source of truth.
- JSON full backup.
- Automatic safety snapshots before destructive actions.
- Restore preview.
- Diagnostics page.
- Broken media detection.
- Clear data path display.
- Export all library.

Future protection additions:

- Scheduled automatic backups.
- Backup rotation.
- Backup verification.
- Manual repair tools.
- Sync conflict review.

## 8. Technical Architecture Direction

### 8.1 Source of truth

SQLite should remain the production storage engine for desktop and should strongly influence mobile storage.

Guidelines:

- `flashcardStore` remains the app-facing storage API.
- Renderer code should not know raw SQLite details.
- Browser `localStorage` remains fallback only.
- Data writes should go through the store boundary.
- Legacy compatibility shims may exist temporarily, but new features should avoid old Firebase-style manager paths.

### 8.2 Stable IDs

Stable IDs are mandatory for sync, review history, import/export, and card browser reliability.

Entities requiring stable IDs:

- Set/deck.
- Card.
- Class.
- Image/media.
- Review log entry.
- Backup snapshot.
- Future sync operation.

### 8.3 Data model direction

Core set fields:

- `id`
- `name`
- `classId`
- `cards`
- `srsSettings`
- `created`
- `lastModified`
- `openedCount`
- `lastOpened`

Core card fields:

- `id`
- `term`
- `definition`
- `termImage`
- `definitionImage`
- `tags`
- `suspended`
- `buriedUntil`
- `srs`
- `reviewHistory`

Core class fields:

- `id`
- `name`
- `color`
- `created`
- `lastModified`

Future sync fields:

- `rev`
- `deviceId`
- `deletedAt`
- `updatedAt`
- operation metadata where needed.

### 8.4 Backup strategy

JSON backup is the trusted full-fidelity format.

It should include:

- Sets.
- Cards.
- Classes.
- Settings.
- SRS progress.
- Review history.
- State.
- Media references.
- Backup schema version.
- Export timestamp.

CSV/TSV should remain convenience formats and should not be treated as full backup formats.

### 8.5 Import/export strategy

Priority order:

1. JSON backup.
2. CSV/TSV import/export.
3. Anki `.apkg` import.
4. Anki `.apkg` export.
5. Quizlet-compatible text/CSV import improvements.

Anki compatibility is strategically important because it lowers switching cost for serious users.

## 9. SRS Direction

FSRS is already the right direction. The goal is not to replace it. The goal is to make the surrounding experience serious and transparent.

### Current SRS strengths

- FSRS engine through `ts-fsrs`.
- Again/Hard/Good/Easy ratings.
- Interval previews.
- Per-deck settings direction.
- Due card dashboard.
- Mixed due review flow across sets.

### Required improvements

- Store richer review history.
- Show retention over time.
- Show daily review count.
- Show upcoming due workload.
- Show per-deck due/new/learning/review/mature counts.
- Support suspend/bury/reset cleanly.
- Ensure SRS and normal progress are independent.
- Ensure completion behavior is mode-aware.

### Future advanced SRS

- FSRS parameter optimization from review logs.
- Desired retention presets.
- Workload simulation.
- Review load warnings.
- Leech detection.
- Forgotten card recovery.
- Deck-specific learning steps if supported cleanly.

## 10. Mobile Vision

Mobile is not just a smaller desktop app. Mobile is where daily retention happens.

### Mobile north star

Open app, see due cards, review smoothly, close app. No friction.

### Android first

Initial mobile target should be Android.

Reasons:

- Easier testing and sideloading.
- Lower distribution friction.
- Better fit for early local-first experimentation.
- User currently focuses Windows/Android style workflow.

### Mobile v1 capabilities

- Open local library.
- Study normal mode.
- Study SRS due mode.
- View classes and sets.
- Basic settings.
- Import backup.
- Export backup.
- Local SQLite storage.
- Smooth touch and swipe.
- Image rendering.
- Offline use.

### Mobile v1 non-goals

- Full creator parity.
- Advanced diagnostics.
- Full `.apkg` support on mobile.
- AI.
- Complex sync UI.
- Heavy desktop-style table browser.

### Mobile v2 capabilities

- Better creator.
- Manual sync with desktop.
- Local Wi-Fi sync.
- Card browser.
- Cloze and image occlusion review.
- Push/local notifications for due reviews.
- Widgets or quick review entry later.

## 11. Sync Vision

Sync should be introduced carefully. Bad sync is worse than no sync.

### Sync philosophy

The user should never feel that sync can destroy their library.

Rules:

- Local data remains primary.
- Backup before restore or sync merge.
- Conflicts should be recoverable.
- Silent overwrite is forbidden.
- Sync should show what happened in simple language.

### Sync stages

Stage 1: Manual backup transfer

- Export backup on desktop.
- Import backup on mobile.
- Export backup on mobile.
- Import backup on desktop.
- Simple and safe.

Stage 2: Local Wi-Fi pairing

- Desktop shows QR code.
- Mobile scans QR code.
- Devices connect over local network.
- User manually starts sync.
- Both sides create safety snapshot first.

Stage 3: Smarter conflict handling

- Merge by stable IDs.
- Use updated timestamps and review history.
- Preserve newer review progress.
- Move deleted/restored conflicts into recoverable state.

Stage 4: Optional paid sync later

- Encrypted relay or private account sync may become a paid feature.
- Basic local use must not require it.

## 12. Design Direction

### Visual personality

The app should feel:

- Calm.
- Premium.
- Focused.
- Trustworthy.
- Modern.
- Slightly warm, not sterile.

It should not feel:

- Gimmicky.
- Noisy.
- Overly blue everywhere.
- Like a marketing landing page.
- Like a developer tool.
- Like a toy.

### Library design

Library should prioritize:

- Resume due review.
- Understand library health.
- Find sets quickly.
- Manage classes.
- Avoid too many boxed panels.
- Make search/sort compact.

### Creator design

Creator should prioritize:

- Fast entry.
- Clear formatting state.
- Stable layout.
- No jumping add buttons.
- Good image controls.
- Draft recovery.
- Bulk creation.

### Study design

Study should prioritize:

- Readability.
- Centered attention.
- No overlap.
- Smooth touch/keyboard.
- Card content intelligently adapting to text and images.
- Calm SRS rating controls.
- Clear completion summary.

### Mobile design

Mobile should prioritize:

- Large tap targets.
- Thumb reach.
- Swipe.
- Fast resume.
- Minimal setup.
- Battery-friendly rendering.
- Readable cards in portrait.

## 13. Feature Roadmap

### Phase 1: Desktop stability

Goal: make the current Windows app trustworthy.

Required work:

- Finish storage cleanup.
- Verify SQLite source of truth.
- Remove misleading legacy Firebase/auth comments where safe.
- Ensure draft behavior is correct.
- Ensure class reassignment is correct.
- Ensure images persist across restart, backup, and restore.
- Ensure SRS progress persists across mode switches.
- Improve diagnostics.
- Repackage Windows portable and installer builds.

Exit criteria:

- No known data-loss bugs.
- Create/edit/delete/import/export pass manual test.
- Image cards pass restart and backup/restore test.
- SRS due review works across sets.
- Draft behavior is predictable.
- Packaged app opens on a clean machine.

### Phase 2: Mobile foundation

Goal: create the first Android app that can study real Erudite decks offline.

Required work:

- Choose mobile shell approach.
- Reuse shared storage and SRS logic where practical.
- Add mobile SQLite storage.
- Build mobile library.
- Build mobile study.
- Add backup import/export.
- Test on real device.

Exit criteria:

- Android app installs.
- App opens offline.
- Imported backup displays sets/classes.
- Study mode works smoothly.
- SRS ratings persist.
- Exported mobile backup can restore on desktop.

### Phase 3: Manual sync

Goal: make desktop-mobile transfer safe before real-time sync.

Required work:

- Normalize backup schema.
- Add backup import preview.
- Add safety snapshot before restore.
- Add clear conflict messaging.
- Add "replace" and "merge" paths only if safe.

Exit criteria:

- Desktop to mobile backup transfer works.
- Mobile to desktop backup transfer works.
- User cannot accidentally erase data without warning.
- Restore failure leaves original library intact.

### Phase 4: Local Wi-Fi sync

Goal: allow direct device-to-device sync without cloud.

Required work:

- Pair devices by QR code.
- Establish local network connection.
- Exchange device metadata.
- Create safety snapshots.
- Merge sets/cards/classes/progress.
- Show sync result summary.

Exit criteria:

- Desktop and Android can pair.
- New set created on one device appears on the other.
- Reviews done on mobile update desktop.
- Reviews done on desktop update mobile.
- Conflict cases are recoverable.

### Phase 5: Serious learning features

Goal: reach serious Anki-alternative credibility.

Required work:

- `.apkg` import.
- Cloze deletion.
- Image occlusion.
- Typed answer mode.
- Tags.
- Better card browser.
- Better stats.
- Review history.

Exit criteria:

- Anki users can move at least basic decks into Erudite.
- Students can make cloze and image occlusion cards.
- Users can search and fix individual cards quickly.
- Stats are useful for daily decisions.

### Phase 6: Public beta

Goal: release a credible first version.

Required work:

- Write README.
- Write backup/data-location docs.
- Write import docs.
- Add release notes.
- Add website or simple landing page.
- Add feedback link.
- Add privacy statement.
- Add known limitations.

Exit criteria:

- A new user understands what the app is.
- A new user can install it.
- A new user can back up their library.
- A new user can report issues.
- The app has a clear identity.

### Phase 7: Optional AI backlog

Goal: add AI only after the app is already valuable without it.

Possible paths:

- Bring-your-own Ollama.
- Bring-your-own LM Studio.
- Local model download later.
- AI-assisted card cleanup.
- AI-assisted cloze generation.
- AI-assisted duplicate detection.

Rules:

- AI cannot be required.
- AI cannot send private data to cloud by default.
- AI cannot compromise offline-first identity.
- AI should output reviewable drafts, not silently create trusted cards.

## 14. Business Direction

The preferred business model is paid indie software.

### Why paid indie fits

- The app is privacy-first.
- Users value ownership.
- Offline-first reduces cloud costs.
- One-time purchase is easier to trust than subscription.
- Mobile paid app is familiar in this category.

### Possible pricing paths

Option A: Paid desktop and mobile

- Desktop stable release: paid one-time.
- Mobile app: paid one-time.
- Sync later: optional paid add-on if cloud relay exists.

Option B: Free desktop beta, paid mobile

- Desktop grows trust and users.
- Mobile creates first revenue.
- Similar psychology to AnkiMobile.

Option C: Free core, paid pro

- More growth potential.
- More complexity.
- Requires careful feature split.

Recommended early path:

- Free private/internal alpha.
- Free or low-cost public beta.
- Paid stable mobile or paid stable bundle later.

### What users might pay for

- Reliable mobile companion.
- Desktop plus mobile bundle.
- Encrypted sync convenience.
- Advanced import/export.
- Premium premade packs.
- Advanced stats.
- Specialized study workflows.

### What should remain core

- Local library.
- FSRS study.
- Create/edit/delete.
- Backup/restore.
- Basic import/export.
- No account required.

## 15. Release Strategy

### Private alpha

Audience:

- Developer/user only.
- A few trusted testers.

Goal:

- Catch data-loss and UX bugs.

### Public beta

Audience:

- Serious students.
- Reddit/Discord communities carefully, not spam.
- People frustrated with Anki UI.

Goal:

- Validate whether users understand the value.
- Validate whether users trust the local-first model.

### Stable v1

Audience:

- Paying early adopters.

Goal:

- Reliable desktop/mobile app with backup and import story.

## 16. Quality Bar

Erudite must be held to a higher quality bar than a normal side project because it stores learning history.

### Data quality bar

- No feature ships if it can easily corrupt sets.
- Destructive actions need confirmation.
- Restore needs safety snapshot.
- Sync needs safety snapshot.
- Migrations need backward compatibility.

### Study quality bar

- No overlapping controls.
- No broken keyboard shortcuts.
- No accidental double review.
- No transparent card artifacts.
- No progress reset between modes.
- No completion modal at the wrong time.

### Creator quality bar

- Drafts must not reopen already saved decks.
- Back button behavior must be understandable.
- Formatting state must be visible.
- Images must be removable and zoomable later.
- Bulk import must be predictable.

### Mobile quality bar

- Touch gestures must not fight scrolling.
- Study cards must be readable on small screens.
- App must work offline.
- App must survive close/reopen.
- Mobile backup import/export must be safe.

## 17. Testing Strategy

### Manual desktop test checklist

- Create a deck.
- Add text cards.
- Add image cards.
- Save.
- Restart app.
- Verify deck persists.
- Edit deck.
- Move deck between classes.
- Move deck back to General.
- Delete deck.
- Restore from backup.
- Verify images render.
- Toggle SRS.
- Review due cards.
- Switch SRS off.
- Verify normal progress remains independent.
- Open card browser.
- Search/edit/delete/reset/suspend.
- Export CSV/TSV.
- Import CSV/TSV.
- Package and open portable build.

### Manual mobile test checklist

- Install app.
- Import backup.
- Open library.
- Study normal deck.
- Study SRS deck.
- Close app.
- Reopen app.
- Verify progress persists.
- Export backup.
- Restore mobile backup on desktop.

### Future automated tests

- Storage schema tests.
- Backup round-trip tests.
- SRS transition tests.
- Import/export tests.
- Sync merge tests.
- Renderer smoke tests.
- Packaged app smoke tests.

## 18. Risks

### Product risks

- Market is crowded.
- Users may compare directly to Anki and expect every advanced feature.
- Users may compare directly to Quizlet and expect AI/content network.
- Without mobile, daily usage is limited.
- Without Anki import, switching is hard.

### Technical risks

- Sync can cause data loss if rushed.
- Mobile and desktop storage can diverge.
- Image/media paths can break across backup and sync.
- Legacy extraction code can create hidden bugs.
- SRS state can become inconsistent if cards lack stable IDs.

### Business risks

- One-time purchase revenue may be small.
- Free competitors reduce willingness to pay.
- Paid sync requires infrastructure and support.
- App store distribution adds friction.

### Mitigation

- Focus on trust and polish.
- Ship small, stable releases.
- Build backup before sync.
- Build import before marketing to Anki users.
- Avoid AI distraction.
- Choose a clear niche.

## 19. Public Identity Later

Possible tagline options:

- Own your memory.
- Serious flashcards, beautifully local.
- Anki power without Anki friction.
- Private SRS for serious learners.
- Study beautifully. Remember reliably.

Preferred public identity:

> Erudite Flashcards is a local-first SRS app for serious learners who want modern design, reliable memory science, and full ownership of their study data.

## 20. Beta Readiness Checklist

Before public beta:

- Windows installer works.
- Portable build works.
- Data location is documented.
- Backup/restore works.
- Diagnostics page is useful.
- SRS mode is reliable.
- Normal mode is reliable.
- Creator draft behavior is reliable.
- Classes work reliably.
- Card browser works reliably.
- No major UI glitches remain.
- README exists.
- Known limitations are documented.
- Feedback route exists.

Before paid release:

- Mobile app exists.
- Backup transfer between desktop and mobile works.
- `.apkg` import exists or is clearly on near-term roadmap.
- Crash/data-loss risk is low.
- App has basic onboarding.
- App has stable branding.
- App has a privacy statement.

## 21. Non-Goals

Near-term non-goals:

- AI generation.
- Social sharing network.
- Cloud-first accounts.
- Marketplace.
- Teacher dashboard.
- Collaboration.
- Web SaaS version.
- Complex gamification.
- Full Anki add-on compatibility.

Long-term possible but not core:

- Cloud sync.
- Shared deck hub.
- Paid content packs.
- AI generation.
- Teacher tools.
- Browser extension.

## 22. Decision Defaults

These defaults should guide future implementation unless deliberately changed:

- Desktop platform: Windows first.
- Mobile platform: Android first.
- Storage: SQLite.
- Scheduler: FSRS.
- Backup: JSON full fidelity.
- Exchange: CSV/TSV convenience.
- Anki compatibility: `.apkg` import first, export later.
- Sync: manual backup transfer first, local Wi-Fi sync second.
- Business: paid indie app.
- AI: deferred backlog.
- Account requirement: none for local use.
- Theme: calm professional UI, not playful/gimmicky.

## 23. Immediate Next Steps

The next implementation sequence should be:

1. Finish desktop reliability audit.
2. Fix remaining known UI bugs.
3. Repackage Windows app.
4. Create mobile architecture plan.
5. Build Android shell.
6. Port core library/study flow.
7. Add mobile SQLite.
8. Add backup import/export on mobile.
9. Test desktop-mobile backup transfer.
10. Add `.apkg` import.
11. Add cloze deletion.
12. Add image occlusion.
13. Prepare public beta docs.

## 24. Final Product Belief

Erudite is worth continuing if it stays focused.

The opportunity is not to make "another flashcard app." The opportunity is to make the calm, local-first, serious study tool that many students wish existed between Anki and Quizlet.

The app can earn trust before it earns money. If it earns trust, money becomes possible.

The path forward is not more gimmicks. It is reliability, mobile, sync, import compatibility, and a study experience that feels excellent every single day.
