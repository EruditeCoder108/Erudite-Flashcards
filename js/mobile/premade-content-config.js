(function () {
  'use strict';

  // Public premade-deck content is intentionally kept outside the APK.
  // Cloudflare Pages publishes premade-cards/ as a static deck library (free,
  // unmetered bandwidth). Coupon redemption still runs as a Netlify function.
  // This URL is public, not a secret. Do not put tokens or passwords here.
  window.ERUDITE_PREMADE_CONTENT = Object.freeze({
    baseUrl: 'https://erudite-flashcards.pages.dev',
    couponBaseUrl: 'https://erudite-flashcards.netlify.app',
    catalogPath: 'premade-catalog.json'
  });
})();
