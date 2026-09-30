(function () {
  'use strict';

  const root = document.documentElement;
  // Arriving from the study screen or the library: the page we left was already
  // showing the same loading cover, so show ours from the first frame instead of
  // the blank startup layer. That makes the move read as one loader, not two.
  let routeHandoff = false;
  try {
    routeHandoff = window.sessionStorage.getItem('erudite-route-handoff') === '1';
    if (routeHandoff) window.sessionStorage.removeItem('erudite-route-handoff');
  } catch (_) {
    routeHandoff = false;
  }
  if (routeHandoff) root.classList.add('route-handoff');
  else root.classList.add('startup-stabilizing');

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
  // The original matte noise (random light and dark pixels, mostly clear),
  // drawn at half resolution and scaled up smoothly, so each grain covers
  // about two device pixels instead of one: the same feel, slightly coarser.
  const GRAIN_TILE = 160;
  const GRAIN_CELL = 2;
  function grainTile() {
    if (grainUrl) return grainUrl;
    try {
      const size = Math.round(GRAIN_TILE * Math.min(3, Math.max(1, window.devicePixelRatio || 1)));
      const small = Math.ceil(size / GRAIN_CELL);
      const noise = document.createElement('canvas');
      noise.width = small;
      noise.height = small;
      const noiseContext = noise.getContext('2d');
      const image = noiseContext.createImageData(small, small);
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
      noiseContext.putImageData(image, 0, 0);
      const canvas = document.createElement('canvas');
      canvas.width = size;
      canvas.height = size;
      const context = canvas.getContext('2d');
      context.imageSmoothingEnabled = true;
      context.drawImage(noise, 0, 0, size, size);
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
  window.EruditePaper = {
    apply(enabled) {
      applyPaper(enabled);
      syncSystemChrome();
    }
  };

  // The Android window and system bars take the colour of whatever fills the
  // screen: onboarding while it is showing, otherwise the theme background.
  // Otherwise the native launch colour shows as a band above and below.
  function toHex(color) {
    const match = String(color || '').match(/rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)/i);
    if (!match) return /^#[0-9a-f]{6}$/i.test(String(color).trim()) ? String(color).trim() : '';
    return '#' + match.slice(1, 4).map(value => Number(value).toString(16).padStart(2, '0')).join('');
  }

  function syncSystemChrome() {
    const plugin = window.Capacitor?.Plugins?.SystemChrome;
    if (!plugin?.setColor) return;
    window.requestAnimationFrame(() => {
      const onboarding = document.getElementById('onboarding-shell');
      const source = onboarding && !onboarding.classList.contains('hidden') && onboarding.offsetParent !== null
        ? getComputedStyle(onboarding).backgroundColor
        : getComputedStyle(root).getPropertyValue('--bg');
      const color = toHex(source);
      if (color) plugin.setColor({ color }).catch(() => {});
    });
  }
  window.EruditeSystemChrome = { sync: syncSystemChrome };

  // Phone font size: scale the root font size, so every rem-based size (text
  // and the boxes around it) grows together. Clamped so very large settings
  // still leave a usable layout. The last value is cached so later launches
  // apply it before the first frame.
  const FONT_SCALE_KEY = 'erudite-font-scale';
  function applyFontScale(scale) {
    const value = Math.min(1.3, Math.max(0.85, Number(scale) || 1));
    root.style.fontSize = value === 1 ? '' : `${(value * 100).toFixed(1)}%`;
    root.style.setProperty('--font-scale', String(value));
    fontScaleNow = value;
    markShortScreen();
    return value;
  }
  // "Short" in layout terms: the height left after scaling up the text. CSS
  // media queries cannot see the root font size, so this class stands in.
  let fontScaleNow = 1;
  function markShortScreen() {
    const height = window.innerHeight / fontScaleNow;
    root.classList.toggle('is-short-screen', height < 760);
    root.classList.toggle('is-very-short-screen', height < 640);
  }
  window.addEventListener('resize', markShortScreen);
  markShortScreen();
  try {
    const cached = Number(window.localStorage.getItem(FONT_SCALE_KEY));
    if (cached) applyFontScale(cached);
  } catch (_) {}
  function syncFontScale() {
    const plugin = window.Capacitor?.Plugins?.SystemChrome;
    if (!plugin?.getFontScale) return;
    plugin.getFontScale().then(result => {
      const value = applyFontScale(result?.scale);
      try {
        window.localStorage.setItem(FONT_SCALE_KEY, String(value));
      } catch (_) {}
    }).catch(() => {});
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', syncFontScale, { once: true });
  else syncFontScale();

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
