# Monetization and ads plan

Status: agreed direction, not implemented yet. The owner confirmed ads and the free-sample model on 2026-09-24.

## Principles

1. **Never interrupt recall.** No ads between cards, on the rating screen, or when a session opens. An interstitial in the middle of a review breaks the retrieval effort that makes SRS work, and learners quit apps that do it. This rule is what separates Erudite from ad-heavy quiz apps.
2. **Keep the learning core free forever.** Creating cards, unlimited decks, FSRS scheduling, image occlusion, the AI prompt hand-off, and manual backup stay free. Students evaluate SRS apps by their core loop; paywalling it hands the market to Anki.
3. **Charge for things that cost us money or save the learner serious time.** Curated exam libraries, automatic cloud backup and sync, and (later) in-app AI generation all fit.
4. **Price for Indian students.** They pay through Google Play with UPI. A low annual price converts better than a monthly one.

## What is free and what is Pro

| Free | Erudite Pro |
| --- | --- |
| Unlimited decks and cards, all card types, image occlusion | Everything in Free |
| FSRS scheduling, daily limits, custom study, basic insights | Full premium premade libraries (complete NEET, JEE, and board chapter sets with occlusion diagrams) |
| The first cards of every premade library (a free sample) | Automatic backup to Google Drive, and sync once it exists |
| AI prompt builder (copy and paste hand-off) | In-app AI generation from a PDF or photo, when it ships (covers the API cost) |
| Manual JSON backup | Advanced insights: per-deck retention trends, FSRS parameter optimisation, forecast by deck |
| Small banner ads outside study | No ads, extra themes, and custom fonts |

The premade library is the strongest paid asset: it is hard to copy, directly tied to exam results, and already hosted on Netlify outside the APK.

## Ads (free tier only)

- **SDK:** Google AdMob through `@capacitor-community/admob`.
- **Placement:** one adaptive banner at the bottom of the Library and Premade tabs. None on Today, Create, Study, or Settings.
- **Rewarded ads (opt-in only):** "Watch a short video to unlock this premium chapter for 3 days." The learner chooses it, it never auto-plays, and it gives a real taste of Pro.
- **No interstitials.** If revenue data later justifies one, it may appear only after the "session complete" screen is dismissed, at most once a day, and never within the first 3 days after install.
- **Minors:** many users are 13 to 17. Set the Play target audience to 13+, request non-personalised ads for users under the age of consent (AdMob `tagForUnderAgeOfConsent`), and use Google's UMP consent form for regions that require it.

### Compliance work that ships with ads

- Rewrite the privacy policy (in-app `mobile/privacy.html` and hosted `premade-cards/privacy.html`). Both currently state that Erudite "does not run advertising or tracking SDKs", which becomes false.
- Update the Play Data safety form: AdMob collects device identifiers and app interactions and shares them with Google.
- Add the `com.google.android.gms.permission.AD_ID` permission and the AdMob app ID to `AndroidManifest.xml`.
- Add an `app-ads.txt` file to the developer website listed in Play Console.

## Billing

- **Provider:** Google Play Billing through RevenueCat (`@revenuecat/purchases-capacitor`). It validates receipts server-side, handles grace periods and refunds, and is free below USD 2,500 monthly tracked revenue. The alternative is `cordova-plugin-purchase`, which means validating receipts yourself.
- **Starting prices** (test with Play price experiments):
  - Annual: ₹399 per year (headline offer, shown as "about ₹33 per month")
  - Monthly: ₹79 per month
  - Lifetime: ₹999 (one purchase for students wary of subscriptions)
  - 7-day free trial on the annual plan
- **Entitlement layer:** one small module, `js/core/entitlements.js`, exposes `isPro()` and `onChange()`. The app gates features only through it, so ads, the premade locks, and Pro insights all read one source of truth. The last known entitlement is cached in SQLite so Pro keeps working offline.
- **Premade locks (decided):** every premade library keeps its first few cards free and puts the rest behind Pro. Add `"freeCards": <n>` per library in `premade-catalog.json` (default 20 when missing), or `"tier": "free"` for a library that stays fully free. Free users download and study the sample normally; the remaining cards show as locked in the deck view with an upgrade button. Cards are ordered by chapter, so the sample is the start of the first chapter. The hosted files are public, so this is a convenience gate, not DRM. Stronger protection would need signed, expiring download URLs from a small server.

## Where the upgrade prompt appears (and where it never does)

- Opening a Pro premade deck: a preview screen, a rewarded-ad option, and the upgrade button.
- Settings: a single "Erudite Pro" row.
- After the 7th consecutive study day: one dismissible card on Today ("You have studied 7 days in a row..."), shown once.
- Never during study, never as a launch pop-up, and never more than once per week unprompted.

## Build order

1. Entitlement module, a Pro screen, and RevenueCat purchase and restore.
2. Premade `freeCards` field and the lock UI. **Release 1 ships here, without ads.**
3. Release 2: banner ads for free users, the rewarded-ad unlock, UMP consent, and the privacy policy and Data safety updates.
4. Pro-only features as they land: Drive backup, advanced insights, in-app AI.

## Why ads wait for the second release

- Ratings from the first users set the store rating for months. A redesigned app with no ads earns better first reviews.
- Ads need a new privacy policy, a new Data safety form, a consent form, and the AD_ID permission. Shipping them later keeps the first release review simple.
- Without ads, the first release measures one thing cleanly: how many free-sample users buy Pro. That number decides how aggressive ads need to be.
- Banner ads earn little at the start (a few rupees per 1,000 views in India), so waiting one release costs almost nothing.

## Decisions still needed from the owner

1. The number of free cards per library (recommendation: 20, or the whole first chapter when it is shorter than 40 cards).
2. Price points and whether to offer lifetime.
3. Create the accounts only the owner can create: AdMob app and ad unit IDs, Play Console subscription products, and a RevenueCat project.
