# Erudite Flashcards Landing Page

A responsive, dependency-free landing page built with plain HTML, CSS and JavaScript.

## Files

- `index.html` — page structure and copy
- `styles.css` — responsive visual system
- `script.js` — interactive study console, FSRS retention control, image occlusion demo, deck drawers and mobile navigation
- `assets/erudite-icon.png` — supplied Erudite icon, resized for the web
- `assets/screenshots/` — optimized screenshots captured from the Android release build

## Publish the website

Run `npm run build:site` from the project root. The build combines this landing page with the existing premade-deck catalog and privacy policy in `site/`, so the Android app's current download URLs remain valid.

When the Play Store listing becomes public, replace the non-interactive "Coming soon" labels in `index.html` with links to the final listing URL.

## Run locally

Open `index.html` directly, or serve this folder with any static web server.
