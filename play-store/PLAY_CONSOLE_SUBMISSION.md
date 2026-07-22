# Google Play Console submission

Use this document as the source of truth when creating the first production listing.

## Store settings

- Set the default language to **English (United States) — en-US**.
- Set the app name to **Erudite Flashcards**.
- Select **Education** as the app category.
- Declare that the app is an app, not a game.
- Declare that the app contains no ads.
- Set the support email to **eruditespartan@gmail.com**.
- Set the privacy policy URL to **https://erudite-flashcards.netlify.app/privacy.html**.

## Store listing

### Short description

Create, study, and review powerful flashcards—privately, even offline.

### Full description

Learn deeply. Remember for longer.

Erudite Flashcards is a private, local-first study app built for active recall and long-term retention. Create flexible flashcards, review them with spaced repetition, and understand your progress without creating an account.

STUDY YOUR WAY

• Use simple front-and-back cards, reversed cards, cloze deletions, image occlusion, or custom HTML/CSS cards.
• Choose focused study sessions or let spaced repetition schedule the right cards for today.
• Rate each answer as Again, Hard, Good, or Easy to shape future reviews.

BUILD BETTER MATERIAL

• Organize cards into classes and decks.
• Add formatted text, images, audio, math, diagrams, and code-friendly content.
• Import or export backups so you stay in control of your study library.
• Browse optional premade decks and import only the ones you choose.

SEE YOUR PROGRESS

• Review daily activity and retention insights.
• Check upcoming workload forecasts.
• Identify difficult cards and improve weak areas.

PRIVATE BY DESIGN

Your flashcards, review history, and settings stay on your device. Erudite Flashcards requires no account, includes no advertising, and contains no tracking SDKs. Network access is used only for optional features you initiate, such as browsing premade decks or opening an external AI service.

Whether you are learning vocabulary, preparing for exams, mastering technical subjects, or building lifelong knowledge, Erudite Flashcards gives you serious study tools in a focused mobile experience.

## Graphic assets

Upload the assets in this order:

1. Use `assets/app-icon-512.png` as the 512 × 512 app icon.
2. Use `assets/feature-graphic-1024x500.png` as the 1024 × 500 feature graphic.
3. Upload `assets/phone-screenshot-01-today-dashboard.png` first.
4. Upload `assets/phone-screenshot-02-srs-review.png` second.
5. Upload `assets/phone-screenshot-03-study-card.png` third.
6. Upload `assets/phone-screenshot-04-retention-insights.png` fourth.
7. Upload `assets/phone-screenshot-05-premade-decks.png` fifth.
8. Upload `assets/phone-screenshot-06-card-creator.png` sixth.
9. Upload `assets/phone-screenshot-07-image-occlusion.png` seventh.
10. Upload `assets/phone-screenshot-08-onboarding.png` eighth.

Use these screenshot alt-text descriptions in the same order:

1. `Study dashboard showing deck progress, daily activity, streak, pace, and study heatmap.`
2. `Spaced-repetition review screen showing a card transition and Again, Hard, Good, and Easy rating controls.`
3. `Flashcard study screen showing a chemistry definition card and study progress.`
4. `Retention and review forecast screen with response rates, workload bars, and a study heatmap.`
5. `Premade deck browser showing Class 11 biology chapters available to add.`
6. `Flashcard creator with deck settings, formatting tools, card types, and an attached image.`
7. `Image occlusion editor placing study masks over a biology diagram.`
8. `Erudite onboarding screen introducing recall, creation, and review tools.`

Keep `assets/feature-graphic-background.png` as the editable source background; do not upload it instead of the final feature graphic.

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
- State that user-initiated backup exports are handled as files selected by the user and are not sent to the developer.
- State that opening an external AI provider is user initiated and happens outside Erudite; the external provider's own terms apply.

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
- Declare that the app does not sell digital goods and has no in-app purchases.
- Declare that the app does not request location, camera, microphone, contacts, phone, SMS, storage, biometric, or fingerprint permissions.
- Use the standard Android App Bundle upload flow and enroll in Play App Signing.

## Initial release notes

Initial release of Erudite Flashcards. Create and study local flashcards, use spaced repetition and custom review sessions, track progress, import or export backups, and browse optional premade decks.

## Closed testing for a new personal account

If Play Console marks the account as a new personal developer account, complete its required closed test before applying for production access. Invite eligible testers, keep the test running for the duration shown in Play Console, gather feedback, and answer the production-access questions accurately.
