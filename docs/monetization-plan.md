# Monetization and ads plan

Status: proposal. Nothing here is implemented yet; the decisions at the end need the owner.

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
| Class 10 premade decks and a sample chapter from every premium library | Automatic backup to Google Drive, and sync once it exists |
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
- **Premade locks:** add `"tier": "free" | "pro"` per deck in `premade-catalog.json` and the subject manifests. Locked decks show a lock icon and a preview of 10 cards; the download stays gated in the app. The hosted files are public, so this is a convenience gate, not DRM. Stronger protection would need signed, expiring download URLs from a small server.

## Where the upgrade prompt appears (and where it never does)

- Opening a Pro premade deck: a preview screen, a rewarded-ad option, and the upgrade button.
- Settings: a single "Erudite Pro" row.
- After the 7th consecutive study day: one dismissible card on Today ("You have studied 7 days in a row..."), shown once.
- Never during study, never as a launch pop-up, and never more than once per week unprompted.

## Build order

1. Entitlement module, a Pro screen, and RevenueCat purchase and restore (no ads yet).
2. Premade `tier` field, preview and lock UI, and the rewarded-ad unlock.
3. Banner ads for free users, UMP consent, privacy policy and Data safety updates.
4. Pro-only features as they land: Drive backup, advanced insights, in-app AI.

## Decisions needed from the owner

1. Ads at all, or Pro-only monetisation? Recommendation: ads, but only as described above.
2. Which premade libraries become Pro? Recommendation: keep Class 10 free; make 11th and 12th, NEET, and SSC Pro, each with a free sample chapter.
3. Price points and whether to offer lifetime.
4. Create the accounts only the owner can create: AdMob app and ad unit IDs, Play Console subscription products, and a RevenueCat project.
