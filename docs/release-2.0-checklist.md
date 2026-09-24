# Smriti 2.0 release checklist (owner)

Everything in the code is done and pushed to `claude/stoic-brahmagupta-2464zu`. These are the steps only you can do, in order. Each one is short.

## 1. Merge the work
1. Open a pull request from `claude/stoic-brahmagupta-2464zu` into your main branch and merge it.
2. The **Android build** workflow (GitHub → Actions) runs on every push. Check that it is green.

## 2. Check the name
3. Search the Play Store for "Smriti" and check the Indian trademark register (ipindia.gov.in → Trade Marks → Public Search, class 9 and 41). If there is a clash, tell Claude the new name; the rename is one small change.

## 3. Build the release (.aab)
Your upload keystore is the `.jks` file you used for version 1.0. Without it, Play rejects the update.
4. In GitHub → Settings → Secrets and variables → Actions, add four secrets:
   - `ERUDITE_UPLOAD_KEYSTORE_BASE64`: run `base64 -w0 your-upload-key.jks` (macOS: `base64 -i your-upload-key.jks`) and paste the output.
   - `ERUDITE_UPLOAD_STORE_PASSWORD`
   - `ERUDITE_UPLOAD_KEY_ALIAS`
   - `ERUDITE_UPLOAD_KEY_PASSWORD`
5. Actions → **Android build** → Run workflow. When it finishes, download the **smriti-release** artifact. It contains `app-release.aab`.
   - Alternative on your computer: `npm ci && npm run build:mobile && npx cap sync android`, then in `android/` run `./gradlew bundleRelease` with `android/keystore.properties` filled in.
6. Install the **smriti-debug-apk** artifact on a real phone first and click through: Today, study a deck (swipe, flip, undo), image occlusion, reminders, paper texture, Settings → Smriti Pro.

## 4. Turn on Pro (can wait until after launch)
Without these steps the app ships fine: Pro shows "Coming soon" and every premade chapter still gives 20 free cards.
7. Play Console → your app → Monetize → Products:
   - Subscriptions: `smriti_pro` with base plans `annual` (₹399) and `monthly` (₹79). Add a 7-day free trial on annual.
   - In-app products: `smriti_pro_lifetime` (₹999).
8. Create a RevenueCat account (free) → new project → Google Play app. Connect it with a Play service-account JSON (RevenueCat's guide walks through this).
9. In RevenueCat: create the entitlement `pro`, attach the three products, and put them in the **current** offering as packages Annual, Monthly, and Lifetime.
10. Copy RevenueCat's **public Android SDK key** (starts with `goog_`) into `js/mobile/billing-config.js` → `revenueCatAndroidKey`, commit, and rebuild (step 5). Or send the key to Claude.
11. Add yourself as a licence tester (Play Console → Settings → Licence testing) and buy Pro once in the internal testing track to confirm it unlocks.

## 5. Update the Play listing
12. App name: **Smriti: NEET & JEE Flashcards** (the 30-character limit rules out the longer version).
13. Replace the feature graphic and screenshots with the files in `play-store/assets/2026/`, in the order given in `play-store/PLAY_CONSOLE_SUBMISSION.md` (alt text is there too).
14. Paste the new short description and full description from that same file. It now mentions Smriti Pro.
15. Policy updates:
    - App content → Data safety: add **Purchase history** (collected, app functionality, not shared). Keep "no ads".
    - Monetisation: declare in-app purchases.
    - Privacy policy: deploy the updated `premade-cards/privacy.html` to Netlify (it now covers purchases and the name Smriti).

## 6. Release
16. Upload `app-release.aab` (version 2.0, code 2) to **internal testing** first, then promote to production.
17. Release notes: use "Release notes for 2.0" in `PLAY_CONSOLE_SUBMISSION.md`.
18. Roll out to 20% first and watch the Android vitals (crashes, ANRs) for two days before going to 100%.

## Later (release 2.1)
- Ads (AdMob banners on Library/Premade and a rewarded chapter unlock), with the consent form, AD_ID permission, and privacy and Data safety updates. See `docs/monetization-plan.md`.
- Regenerate store images after any UI change: `npm run store:images`.
