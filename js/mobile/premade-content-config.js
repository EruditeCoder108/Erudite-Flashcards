(function () {
  'use strict';

  // Public premade-deck content is intentionally kept outside the APK.
  // Netlify publishes premade-cards/ as a small static deck library.
  // This URL is public, not a secret. Do not put tokens or passwords here.
  window.ERUDITE_PREMADE_CONTENT = Object.freeze({
    baseUrl: 'https://erudite-flashcards.netlify.app',
    catalogPath: 'premade-catalog.json'
  });
})();
