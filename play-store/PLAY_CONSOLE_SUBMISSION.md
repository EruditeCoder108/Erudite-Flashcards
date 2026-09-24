# Google Play Console submission

Use this document as the source of truth when creating the first production listing.

## Store settings

- Set the default language to **English (United States) — en-US**.
- Set the app name to **Smriti: Flashcards for NEET & JEE** (30 characters maximum; this is 34, so if Play rejects it use **Smriti: NEET & JEE Flashcards**, 29 characters).
- Select **Education** as the app category.
- Declare that the app is an app, not a game.
- Declare that the app contains no ads (true for release 2.0; ads arrive in a later release).
- Declare in-app purchases: Smriti Pro (subscription and lifetime) through Google Play billing.
- Set the support email to **eruditespartan@gmail.com**.
- Set the privacy policy URL to **https://erudite-flashcards.netlify.app/privacy.html**.

## Store listing

### Short description

Create, study, and review powerful flashcards—privately, even offline.

### Full description

Learn deeply. Remember for longer.

Smriti is a private, local-first study app built for active recall and long-term retention. Create flexible flashcards, review them with spaced repetition, and understand your progress without creating an account.

STUDY YOUR WAY

• Use simple front-and-back cards, reversed cards, cloze deletions, image occlusion, or custom HTML/CSS cards.
• Choose focused study sessions or let spaced repetition schedule the right cards for today.
• Rate each answer as Again, Hard, Good, or Easy to shape future reviews.

BUILD BETTER MATERIAL

• Organize cards into classes and decks.
• Add formatted text, images, audio, math, diagrams, and code-friendly content.
• Import or export backups so you stay in control of your study library.
• Browse optional premade decks and import only the ones you choose.

GO FURTHER WITH SMRITI PRO

• Every premade chapter comes with free sample cards.
• Smriti Pro unlocks complete NEET, JEE, and board chapters, and fills in the decks you already study without losing progress.

SEE YOUR PROGRESS

• Review daily activity and retention insights.
• Check upcoming workload forecasts.
• Identify difficult cards and improve weak areas.

PRIVATE BY DESIGN

Your flashcards, review history, and settings stay on your device. Smriti requires no account, includes no advertising, and contains no tracking SDKs. Network access is used only for optional features you initiate, such as browsing premade decks or opening an external AI service.

Whether you are learning vocabulary, preparing for exams, mastering technical subjects, or building lifelong knowledge, Smriti gives you serious study tools in a focused mobile experience.

## Graphic assets

The 2026 redesign images live in `assets/2026/`. Regenerate them after UI changes with `npm run store:images` (it seeds a mock study library, captures the real app at 3x, and frames each screen). Set `APP_NAME="New Name"` in front of the command if the app is renamed.

Upload the assets in this order:

1. Use `assets/app-icon-512.png` as the 512 × 512 app icon.
2. Use `assets/2026/feature-graphic-1024x500.png` as the 1024 × 500 feature graphic.
3. Upload the phone screenshots in this order:
   1. `assets/2026/phone-01-today.png`
   2. `assets/2026/phone-02-swipe.png`
   3. `assets/2026/phone-03-library.png`
   4. `assets/2026/phone-04-occlusion.png`
   5. `assets/2026/phone-05-insights.png`
   6. `assets/2026/phone-06-ai.png`
   7. `assets/2026/phone-07-complete.png`
   8. `assets/2026/phone-08-paper.png`

Use these screenshot alt-text descriptions in the same order:

1. `Today screen with a daily goal ring at 38 percent, a 63-day streak, and a Review button showing 21 cards left.`
2. `Flashcard being swiped right mid-review, labelled Good, showing the answer about lysosomes.`
3. `Library of decks grouped into classes such as NEET Biology and JEE Chemistry.`
4. `Image occlusion card hiding one label on an animal cell diagram.`
5. `Insights showing 96 percent retention, due load, weak cards, and a rating breakdown.`
6. `AI Deck Maker offering study goals such as Quick Revision and Competitive Exam.`
7. `Session complete screen with a check mark, cards reviewed, percent remembered, and next due date.`
8. `Today screen in the light theme with the paper texture turned on.`

The images in `assets/` from July 2026 show the previous design; keep them only for reference.

## App access

- Select **All functionality is available without special access**.
- State that no login, membership, location, or special instructions are required.

## Target audience and content

- Select **13–15**, **16–17**, and **18 and over**.
- Do not select an age group below 13 for this release.
- Explain, if asked, that the app is a reading-heavy independent study tool with advanced authoring, search, and user-initiated external-service links.
- Complete the content-rating questionnaire truthfully using these expected answers:
  - No violence, sexual content, profanity, gambling, controlled substances, or simulated gambling.
  - No public chat, public user-generated-content feed, or social sharing system.
  - Users can create private flashcard content stored on their own device.
  - The app can open external web services only after a deliberate user action.

Treat the resulting rating as Google's decision; do not manually advertise a rating before the questionnaire is accepted.

## Data safety draft

Confirm the production hosting configuration before submitting this form.

### App data

- State that flashcards, study history, media, and settings are processed and stored locally on the device.
- State that the developer does not receive this local study data.
- State that the app has no account system, advertising SDK, analytics SDK, crash-reporting SDK, or tracking SDK.
- Purchases (Smriti Pro): declare **Purchase history** as collected, for app functionality, not shared for advertising. Google Play processes the payment; RevenueCat (a service provider acting for the developer) receives the purchase receipt and an anonymous app user ID to confirm Pro.
- Android backup: flashcards and settings are included in the user's own Google device backup (declared in the privacy policy).
- State that user-initiated backup exports are handled as files selected by the user and are not sent to the developer.
- State that opening an external AI provider is user initiated and happens outside Smriti; the external provider's own terms apply.

### Premade-deck host

Verify the Netlify site's logging, analytics, and retention settings immediately before answering the collection questions:

- If the host only processes request metadata ephemerally to deliver the catalog and does not retain or use it, answer according to Google's ephemeral-processing flow.
- If IP addresses, device identifiers, request logs, or derived approximate location are retained or used, declare every applicable data type, the app-functionality/security purposes, whether processing is ephemeral, and the applicable retention/deletion behavior.
- Treat infrastructure providers acting only on the developer's behalf as service providers when answering whether data is shared, but still disclose collection where Google requires it.
- Declare that network traffic is encrypted in transit.
- Link the published privacy policy and make its wording match the final answers.

Do not guess on the final Data safety form; compare it with the active Netlify configuration first.

## Other declarations

- Declare that the app does not contain ads.
- Declare that the app is not a news app, government app, health app, financial app, VPN, dating app, or real-money gambling app.
- Declare that the app sells digital goods through Google Play billing: Smriti Pro (subscriptions and a one-time lifetime unlock).
- Declare that the app does not request location, camera, microphone, contacts, phone, SMS, storage, biometric, or fingerprint permissions.
- Use the standard Android App Bundle upload flow and enroll in Play App Signing.

## Release notes for 2.0

Erudite Flashcards is now Smriti, redesigned from the ground up.
• A new study screen: swipe to rate, cards that follow your finger, and a Show answer button right under your thumb.
• Smarter scheduling: FSRS fixes, daily new-card limits, and daily reminders.
• Sharper image occlusion and faster, smaller images.
• Paper texture mode for long sessions, plus refreshed dark and light themes.
• Premade chapters now include free sample cards, and Smriti Pro unlocks the complete library.

## Closed testing for a new personal account

If Play Console marks the account as a new personal developer account, complete its required closed test before applying for production access. Invite eligible testers, keep the test running for the duration shown in Play Console, gather feedback, and answer the production-access questions accurately.
