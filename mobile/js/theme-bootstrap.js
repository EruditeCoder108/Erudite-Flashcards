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

  // Paper texture: a static grain tile drawn once on a canvas. A single cached
  // bitmap on a fixed layer costs almost nothing per frame, unlike an SVG
  // filter or a blend mode.
  let grainUrl = '';
  function grainTile() {
    if (grainUrl) return grainUrl;
    try {
      // Drawn at device resolution so each speck is one physical pixel.
      const size = Math.round(160 * Math.min(3, Math.max(1, window.devicePixelRatio || 1)));
      const canvas = document.createElement('canvas');
      canvas.width = size;
      canvas.height = size;
      const context = canvas.getContext('2d');
      const image = context.createImageData(size, size);
      const data = image.data;
      for (let index = 0; index < data.length; index += 4) {
        const value = Math.random();
        const shade = value > 0.5 ? 255 : 0;
        data[index] = shade;
        data[index + 1] = shade;
        data[index + 2] = shade;
        // Most pixels stay nearly clear; a few carry the fibre-like speckle.
        data[index + 3] = Math.round(Math.pow(Math.abs(value - 0.5) * 2, 1.6) * 34);
      }
      context.putImageData(image, 0, 0);
      grainUrl = canvas.toDataURL('image/png');
    } catch (_) {
      grainUrl = '';
    }
    return grainUrl;
  }

  function applyPaper(enabled) {
    root.classList.toggle('paper-texture', Boolean(enabled));
    if (enabled) {
      const url = grainTile();
      if (url) root.style.setProperty('--grain-image', `url("${url}")`);
    }
    try {
      window.localStorage.setItem('erudite-paper', enabled ? 'on' : 'off');
    } catch (_) {
      // Storage is optional; the saved setting is applied again after load.
    }
  }
  window.EruditePaper = { apply: applyPaper };

  try {
    if (window.localStorage.getItem('erudite-paper') === 'on') applyPaper(true);
    if (window.localStorage.getItem('erudite-theme') === 'light') {
      root.classList.add('theme-light');
    }

    const onboardingComplete = window.localStorage.getItem('erudite-mobile-onboarding-complete-v2') === 'true';
    const forceOnboarding = new URLSearchParams(window.location.search || '').get('onboarding') === '1';
    if (!onboardingComplete || forceOnboarding) {
      root.classList.add('onboarding-pending');
    }
    // Onboarding is always printed on paper, whatever the app setting.
    const tile = grainTile();
    if (tile) root.style.setProperty('--onboarding-grain', `url("${tile}")`);
  } catch (_) {
    // Use the default theme when storage is unavailable.
  }
}());
