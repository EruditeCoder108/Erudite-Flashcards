# Mobile Storage & Security Release Audit

**Scope:** Android/Capacitor mobile build only  
**Status:** Core storage/security remediation is implemented. The user has confirmed that the public privacy page is live on Netlify. Do not submit this build to Google Play yet: a protected upload key and physical-device validation still remain.

## Verification completed

- Build the mobile web assets with `npm run build:mobile`.
- Parse all first-party mobile JavaScript with `node --check`.
- Build `:app:bundleRelease` successfully with target SDK 36.
- Query the live npm advisory service with `npm audit --omit=dev`; report zero known production dependency vulnerabilities at the time of the audit.
- Inspect the generated Android release manifest and release AAB.
- Rebuild the narrowed Capacitor web bundle and compile `:app:assembleDebug` successfully after the changes.
- Verify that `:app:bundleRelease` now stops early with a clear error when protected signing values are absent.

## Release blockers

| Priority | Require this action | Evidence and release risk |
|---|---|---|
| P0 | Supply a dedicated upload key outside version control, build a signed AAB/APK, and verify its certificate before upload. | Implemented a release signing configuration in `android/app/build.gradle` that accepts an ignored `android/keystore.properties` or `ERUDITE_UPLOAD_*` environment variables. `android/keystore.properties.example` documents the required values. A release build now fails early without them, so an unsigned AAB cannot be produced by mistake. The existing prior AAB is unsigned and must not be uploaded. |
| P0 | Enter the exact live Netlify privacy-policy URL in Play Console and verify it from a physical device. | Implemented an in-app page at `mobile/privacy.html`, a More-tab entry, user-visible data erasure, and a deployable static policy at `premade-cards/privacy.html`. The user confirmed Netlify deployment is live on 2026-07-17; device and Play Console checks remain. |

## Storage and recovery findings

| Priority | Require this action | Evidence and risk |
|---|---|---|
| P1 | Test the native recovery path at each crash boundary. | Implemented native startup recovery for pending study patches, emergency class/deck mirrors, and orphaned class references. SQLite remains the source of truth; localStorage is retained only as bounded recovery state. Validate with force-close tests before release. |
| P1 | Keep recovery mirrors bounded and document them. | Deck mirrors retain their existing bounded per-deck limit, while deletion now clears known mirrors, progress patches, and caches. Diagnostics/retention UI remains a P2 improvement. |
| P1 | Test managed-media cleanup and full device-data deletion on a physical device. | Implemented media ownership records, removal of unreferenced attachments on save, deck-media cleanup on delete, and a two-step **Delete All Local Data** setting that clears SQLite, app-data media, app-data snapshots, Erudite Documents backups, and known localStorage recovery data. Portable JSON backup/export now embeds supported media (500 files / 56 MiB raw-media cap) and import restores it to private media storage. |
| P1 | Test import and download limits with hostile fixtures. | Implemented limits before reading input: text import size, ZIP bytes, entry count, deck JSON bytes, decompressed bytes, card/media counts, premade Content-Length/streamed bytes, and a 30-second download timeout. |
| P2 | Retain a small, documented number of automatic app-data snapshots, show their age/result, and keep manual exports opt-in. | Snapshots are made before destructive restore/bulk actions but have no retention policy, browse/restore UI, or diagnostics visibility. `getDiagnostics()` reports an empty backup list. |
| P2 | State clearly that exported backups are plaintext user files and require the user's chosen share destination to protect them. | Export writes a complete JSON backup to Documents and offers Android Share. This is a good user-controlled feature but needs privacy wording and a confirmation before sharing sensitive study material. |

## Security findings

| Priority | Require this action | Evidence and risk |
|---|---|---|
| P1 | Validate mutable premade content on a device and decide whether to add signed catalog metadata. | Implemented a fixed icon allow-list, escaped rendering, strict package/download byte limits, and timeout handling. The premade catalog remains mutable at the Netlify host; signed metadata is a future defense-in-depth option. |
| P1 | Verify CSP behavior and external AI hand-off on a physical device. | Added a production CSP to each mobile document, moved the early theme bootstrap out of inline script, and persisted a Netlify-only Cordova access allow-list through `capacitor.config.json`. |
| P1 | Verify Android Share works with narrowed FileProvider paths. | Restricted the external FileProvider root to `Documents/erudite-flashcards/backups/`; app cache remains shareable for plugin compatibility. |
| P2 | Centralize rich-text/advanced-HTML sanitization in one tested core module and fuzz it with hostile HTML, CSS, URL, and malformed-import fixtures. | Similar sanitizers appear independently in `mobile/js/mobile-app.js` and `mobile/js/mobile-study.js`. The current allowlists are a strong start, but duplicated security code will drift. |
| P2 | Enable R8/resource shrinking after a compatibility pass and remove production console logging that can reveal file names or error details. | The release build still explicitly sets `minifyEnabled false`. Treat obfuscation as defense in depth, not a substitute for input validation. |
| P2 | Keep the release bundle mobile-only. | Implemented a targeted mobile asset build: only the root mobile shell, study/privacy pages, mobile runtime, required core scripts, media sounds, icon, and vendor libraries are copied. The generated web payload reduced from about 17.8 MB to 6.2 MB. Verify final signed AAB size after the upload key is configured. |

## Permissions and data inventory

- Keep notification permission out of this release until local study reminders are implemented and the user opts in at a meaningful moment.
- Keep camera, microphone, location, contacts, storage-manager, and broad media permissions out of the app.
- Record that the final merged manifest declares `INTERNET`; native SQLite transitively declares `USE_BIOMETRIC` and `USE_FINGERPRINT`, neither of which is a runtime prompt or currently used by Erudite features.
- Treat local card content, progress, media, settings, emergency mirrors, app-data backups, exported backup files, the Netlify deck request, and the user-initiated external-AI hand-off as the evidence set for the privacy policy and Play Data Safety review.
- Run a physical-device network capture before declaring "no data collected or shared"; do not infer the Data Safety answer solely from source inspection.

## Strengths to retain

- Keep `android:allowBackup="false"`, `android:fullBackupContent="false"`, and `android:usesCleartextTraffic="false"`.
- Keep parameterized SQLite queries and transactional multi-row writes.
- Keep the existing rich-card allowlists, local-first storage architecture, 80 MB backup import cap, card-count caps, and user-triggered backup sharing.
- Keep the current small manifest permission surface; do not add permissions merely for future features.

## Required remediation order

1. Create the protected upload key, add its ignored configuration, build a signed AAB/APK, and verify the certificate fingerprint.
2. Enter the already-live Netlify privacy-policy URL in Play Console and verify it from a physical device.
3. Run physical-device recovery, portable-backup, delete-all, import-abuse, Android Share, offline, and CSP/external-AI tests.
4. Enable/test R8 and resource shrinking, then measure the final signed AAB.
5. Complete the polished onboarding, identity, reminder, and accessibility work before store listing screenshots and submission.
