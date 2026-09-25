(function () {
  'use strict';

  // Billing settings for Erudite Pro. RevenueCat's public SDK key is designed to
  // ship inside the app; it is not a secret. Leave it empty until the RevenueCat
  // project exists: the app then shows Pro as "coming soon" and keeps every
  // purchase button disabled.
  window.ERUDITE_BILLING = Object.freeze({
    revenueCatAndroidKey: '',
    // Entitlement identifier configured in the RevenueCat dashboard.
    entitlementId: 'pro',
    // Cards of each premade chapter that free users can import. A deck in the
    // premade manifest can override this with "freeCards", or set
    // "tier": "free" to stay fully free.
    freeSampleCards: 20
  });
})();
