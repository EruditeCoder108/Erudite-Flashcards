(function (root, factory) {
  const api = factory(root);
  root.EruditeCore = root.EruditeCore || {};
  root.EruditeCore.motion = api;
  root.EruditeMotion = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
})(typeof globalThis !== 'undefined' ? globalThis : window, function (root) {
  // Spring physics compiled to CSS linear() easing, so every animation runs on the
  // compositor through the Web Animations API instead of a JavaScript frame loop.
  // A gesture's release velocity feeds straight into the spring, which is what
  // makes a flicked card keep its momentum.

  const PRESETS = {
    // Buttons, chips, small UI.
    snappy: { stiffness: 420, damping: 30, mass: 1 },
    // Cards moving across the screen.
    swipe: { stiffness: 260, damping: 28, mass: 1 },
    // Card flip: firm with a whisper of overshoot.
    flip: { stiffness: 300, damping: 26, mass: 1 },
    // Sheets and modals.
    sheet: { stiffness: 340, damping: 34, mass: 1 },
    // Returning a dragged card to rest: soft and bouncy.
    settle: { stiffness: 380, damping: 22, mass: 1 }
  };

  const cache = new Map();

  function prefersReducedMotion() {
    try {
      return Boolean(root.matchMedia && root.matchMedia('(prefers-reduced-motion: reduce)').matches);
    } catch (_) {
      return false;
    }
  }

  function supportsLinearEasing() {
    try {
      return Boolean(root.CSS && root.CSS.supports && root.CSS.supports('animation-timing-function', 'linear(0, 1)'));
    } catch (_) {
      return false;
    }
  }

  /**
   * Position of a unit spring (0 -> 1) at time t seconds.
   * velocity is in "distances per second": a card flicked at 2 widths/s over a
   * 1-width travel has velocity 2.
   */
  function springAt(t, { stiffness, damping, mass, velocity = 0 }) {
    const omega = Math.sqrt(stiffness / mass);
    const zeta = damping / (2 * Math.sqrt(stiffness * mass));
    // Displacement from rest starts at -1 with velocity v (towards the target).
    const x0 = -1;
    const v0 = velocity;
    if (zeta < 1) {
      const omegaD = omega * Math.sqrt(1 - zeta * zeta);
      const envelope = Math.exp(-zeta * omega * t);
      const displacement = envelope * (
        x0 * Math.cos(omegaD * t)
        + ((v0 + zeta * omega * x0) / omegaD) * Math.sin(omegaD * t)
      );
      return 1 + displacement;
    }
    const envelope = Math.exp(-omega * t);
    return 1 + envelope * (x0 + (v0 + omega * x0) * t);
  }

  /**
   * Compile a spring to { easing, duration } for element.animate().
   * The duration ends when the spring stays within 0.1% of rest.
   */
  function spring(options = {}) {
    const params = {
      ...PRESETS.snappy,
      ...(typeof options === 'string' ? PRESETS[options] : options)
    };
    params.velocity = Math.max(-40, Math.min(40, Number(params.velocity) || 0));
    const key = `${params.stiffness}|${params.damping}|${params.mass}|${params.velocity.toFixed(1)}`;
    if (cache.has(key)) return cache.get(key);

    const step = 1 / 120;
    let settleTime = 0;
    for (let t = 0; t < 4; t += step) {
      const position = springAt(t, params);
      const ahead = springAt(t + step, params);
      if (Math.abs(1 - position) > 0.001 || Math.abs(ahead - position) > 0.001) settleTime = t + step;
    }
    const duration = Math.max(0.12, Math.min(2, settleTime));
    const samples = Math.max(12, Math.min(60, Math.round(duration * 60)));
    const points = [];
    for (let index = 0; index <= samples; index += 1) {
      const value = index === samples ? 1 : springAt((duration * index) / samples, params);
      points.push(Number(value.toFixed(4)));
    }
    const result = {
      easing: supportsLinearEasing() ? `linear(${points.join(', ')})` : 'cubic-bezier(0.22, 1, 0.36, 1)',
      duration: Math.round(duration * 1000),
      points
    };
    cache.set(key, result);
    return result;
  }

  /**
   * Animate an element with a spring. Resolves when finished or cancelled.
   * keyframes follow element.animate(). The final keyframe is committed as an
   * inline style so the element stays where the animation left it.
   */
  function animate(element, keyframes, options = {}) {
    if (!element || typeof element.animate !== 'function') return Promise.resolve();
    const { preset = 'snappy', velocity = 0, delay = 0, commit = true, duration: fixedDuration } = options;
    const reduced = prefersReducedMotion();
    const curve = spring({ ...(PRESETS[preset] || PRESETS.snappy), velocity });
    const animation = element.animate(keyframes, {
      duration: reduced ? Math.min(160, curve.duration) : (fixedDuration || curve.duration),
      easing: reduced ? 'ease-out' : curve.easing,
      delay,
      fill: 'both'
    });
    return animation.finished.then(() => {
      if (commit) {
        try {
          animation.commitStyles();
        } catch (_) {
          // Detached elements cannot commit styles.
        }
      }
      animation.cancel();
    }, () => undefined);
  }

  /**
   * Track pointer velocity over the last ~80 ms of a drag, in px per second.
   */
  function createVelocityTracker() {
    let samples = [];
    return {
      reset() {
        samples = [];
      },
      add(x, y, time = performance.now()) {
        samples.push({ x, y, time });
        const cutoff = time - 100;
        while (samples.length > 2 && samples[0].time < cutoff) samples.shift();
      },
      velocity() {
        if (samples.length < 2) return { x: 0, y: 0 };
        const first = samples[0];
        const last = samples[samples.length - 1];
        const elapsed = Math.max(1, last.time - first.time) / 1000;
        return { x: (last.x - first.x) / elapsed, y: (last.y - first.y) / elapsed };
      }
    };
  }

  // Low-end detection: few cores or little memory means we drop blur, shadows
  // under motion, and parallax. The class lets CSS do the rest.
  function isLowEndDevice() {
    const nav = root.navigator || {};
    const cores = Number(nav.hardwareConcurrency) || 8;
    const memory = Number(nav.deviceMemory) || 8;
    return cores <= 4 || memory <= 3;
  }

  if (root.document && root.document.documentElement) {
    const docEl = root.document.documentElement;
    if (isLowEndDevice()) docEl.classList.add('is-low-end');
    if (prefersReducedMotion()) docEl.classList.add('reduce-motion');
  }

  return {
    PRESETS,
    spring,
    springAt,
    animate,
    createVelocityTracker,
    prefersReducedMotion,
    isLowEndDevice
  };
});
