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
  // One tile of GRAIN_TILE CSS pixels, drawn at device resolution. Two layers:
  // a faint one-pixel base, and scattered soft specks one to three points
  // wide, which is the scale real paper grain reads at on a phone.
  const GRAIN_TILE = 200;
  function grainTile() {
    if (grainUrl) return grainUrl;
    try {
      const scale = Math.min(3, Math.max(1, window.devicePixelRatio || 1));
      const size = Math.round(GRAIN_TILE * scale);
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
        data[index + 3] = Math.round(Math.pow(Math.abs(value - 0.5) * 2, 2.2) * 18);
      }
      context.putImageData(image, 0, 0);
      const specks = Math.round(GRAIN_TILE * GRAIN_TILE * 0.05);
      for (let count = 0; count < specks; count += 1) {
        const x = Math.random() * size;
        const y = Math.random() * size;
        const radius = (0.5 + Math.pow(Math.random(), 2.4) * 1.1) * scale;
        const light = Math.random() > 0.55;
        const alpha = 0.025 + Math.random() * 0.06;
        context.fillStyle = light ? `rgba(255,255,255,${alpha})` : `rgba(0,0,0,${alpha * 1.15})`;
        context.beginPath();
        // Slightly stretched specks look like fibres rather than dots.
        context.ellipse(x, y, radius * (1 + Math.random() * 0.8), radius, Math.random() * Math.PI, 0, Math.PI * 2);
        context.fill();
      }
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
