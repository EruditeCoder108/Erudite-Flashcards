(function () {
  'use strict';

  const root = document.documentElement;
  root.classList.add('startup-stabilizing');

  let startupReleased = false;
  const releaseStartupFrame = () => {
    if (startupReleased) return;
    startupReleased = true;
    root.classList.remove('startup-stabilizing');
  };
  const scheduleStartupRelease = () => {
    // Capacitor applies Android safe-area insets at DOM-ready. Keep the first
    // visible content covered until those measurements have settled.
    window.requestAnimationFrame(() => {
      window.requestAnimationFrame(() => {
        window.setTimeout(releaseStartupFrame, 48);
      });
    });
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', scheduleStartupRelease, { once: true });
  } else {
    scheduleStartupRelease();
  }
  // Never leave the cover in place if an unrelated startup script fails.
  window.setTimeout(releaseStartupFrame, 2000);

  try {
    if (window.localStorage.getItem('erudite-theme') === 'light') {
      root.classList.add('theme-light');
    }

    const onboardingComplete = window.localStorage.getItem('erudite-mobile-onboarding-complete-v2') === 'true';
    const forceOnboarding = new URLSearchParams(window.location.search || '').get('onboarding') === '1';
    if (!onboardingComplete || forceOnboarding) {
      root.classList.add('onboarding-pending');
    }
  } catch (_) {
    // Use the default theme when storage is unavailable.
  }
}());
