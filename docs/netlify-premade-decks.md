# Publish premade decks with Netlify

Netlify hosts the contents of `premade-cards/` as a static public library. The Android app downloads a deck only when a student chooses it, so the full library is not included in the APK.

## Current site

The app reads its premade library from:

```text
https://erudite-flashcards.netlify.app
```

The required app configuration is already saved in `js/mobile/premade-content-config.js`.

## Netlify project settings

The repository includes `netlify.toml`, which keeps the deployment settings correct:

```text
Branch to deploy: main
Base directory:  (leave blank)
Build command:   (leave blank)
Publish directory: premade-cards
Functions directory: (leave blank)
```

The `_headers` file in `premade-cards/` allows the Android app to fetch the public catalog and ZIP files from the Netlify site.

## Publish the library

1. Make sure the deck metadata is up to date:

   ```powershell
   npm.cmd run zip:premade
   ```

2. Commit and push the changes to the `main` branch.
3. Netlify automatically creates a new production deploy.
4. Open the **Deploys** tab in Netlify and wait for the green **Published** status.
5. Confirm that this catalog URL displays JSON in a browser:

   ```text
   https://erudite-flashcards.netlify.app/premade-catalog.json
   ```

6. Rebuild the Android app after changing its source:

   ```powershell
   npm.cmd run cap:sync
   ```

## Add or update decks later

1. Add the ZIP to `premade-cards/<class>/<subject>/`.
2. Run `npm.cmd run zip:premade`.
3. Commit and push to `main`.
4. Netlify publishes it automatically. Students see the new catalog without installing a new APK.

Use a new ZIP filename, such as `living-world-v2.zip`, when substantially revising a deck. Then update its `manifest.json`. This avoids a cached download being reused.

## Free-plan behavior

Netlify Free has a fixed monthly credit limit. It does not auto-charge a card; if the limit is reached, the hosted deck library pauses until the next billing period. Decks students have already imported remain available offline. See [Netlify credit-based pricing](https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/credit-based-pricing-plans/).
