(function (root) {
  'use strict';

  // Haptics with intent. Callers say what happened (a tick, a toggle, a swipe
  // crossing its commit point, a success) and this picks the feel. Plain taps
  // on ordinary buttons get nothing: feedback on every touch stops meaning
  // anything.
  //
  // On Android the native Tactile plugin (MainActivity) uses
  // View.performHapticFeedback, which matches the system keyboard feel and
  // respects the phone's touch-feedback setting. Without it we fall back to
  // @capacitor/haptics, then navigator.vibrate.

  const STORAGE_KEY = 'erudite-haptics';
  // Fallback patterns for @capacitor/haptics. Its style names are uppercase;
  // anything else silently becomes HEAVY.
  const FALLBACK = {
    tick: { impact: 'LIGHT' },
    tap: { impact: 'LIGHT' },
    'toggle-on': { impact: 'LIGHT' },
    'toggle-off': { impact: 'LIGHT' },
    threshold: { impact: 'MEDIUM' },
    'long-press': { impact: 'MEDIUM' },
    confirm: { notification: 'SUCCESS' },
    reject: { notification: 'WARNING' }
  };
  const VIBRATE_MS = { tick: 6, tap: 8, 'toggle-on': 8, 'toggle-off': 6, threshold: 12, 'long-press': 18, confirm: [10, 60, 14], reject: [16, 50, 16] };
  // Rapid events (scrolling through chips, fast ratings) share one budget so
  // the motor never queues a buzz train.
  const MIN_GAP_MS = 55;

  let enabled = readEnabled();
  let lastAt = 0;
  let tactile;
  let tactileBroken = false;

  function readEnabled() {
    try {
      return root.localStorage?.getItem(STORAGE_KEY) !== 'off';
    } catch (_) {
      return true;
    }
  }

  function setEnabled(value) {
    enabled = value !== false;
    try {
      root.localStorage?.setItem(STORAGE_KEY, enabled ? 'on' : 'off');
    } catch (_) {
      // The in-memory flag still applies for this session.
    }
  }

  function isNative() {
    try {
      return root.Capacitor?.isNativePlatform?.() === true;
    } catch (_) {
      return false;
    }
  }

  function tactilePlugin() {
    if (tactileBroken || !isNative()) return null;
    if (tactile === undefined) {
      tactile = root.Capacitor?.Plugins?.Tactile
        || (typeof root.Capacitor?.registerPlugin === 'function' ? root.Capacitor.registerPlugin('Tactile') : null);
    }
    return tactile;
  }

  function fallback(kind) {
    const haptics = root.Capacitor?.Plugins?.Haptics;
    const spec = FALLBACK[kind] || FALLBACK.tick;
    if (isNative() && haptics) {
      const call = spec.notification
        ? haptics.notification?.({ type: spec.notification })
        : haptics.impact?.({ style: spec.impact });
      call?.catch?.(() => {});
      return;
    }
    if (typeof root.navigator?.vibrate === 'function') {
      try {
        root.navigator.vibrate(VIBRATE_MS[kind] || 6);
      } catch (_) {
        // Some browsers throw before a user gesture.
      }
    }
  }

  function perform(kind) {
    if (!enabled) return;
    const now = root.performance?.now?.() ?? Date.now();
    // Outcomes (confirm, reject) always play; they end a gesture.
    if (kind !== 'confirm' && kind !== 'reject' && now - lastAt < MIN_GAP_MS) return;
    lastAt = now;
    const plugin = tactilePlugin();
    if (plugin?.perform) {
      Promise.resolve(plugin.perform({ kind })).catch(() => {
        tactileBroken = true;
        fallback(kind);
      });
      return;
    }
    fallback(kind);
  }

  const api = {
    isEnabled: () => enabled,
    setEnabled,
    perform,
    /** Selection moved: tabs, chips, segmented controls, steppers. */
    tick: () => perform('tick'),
    /** The one main action on a screen: start review, play a deck. */
    tap: () => perform('tap'),
    toggle: on => perform(on ? 'toggle-on' : 'toggle-off'),
    /** A drag crossed the point where letting go will commit. */
    threshold: () => perform('threshold'),
    longPress: () => perform('long-press'),
    success: () => perform('confirm'),
    warning: () => perform('reject')
  };

  root.EruditeHaptics = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
}(typeof globalThis !== 'undefined' ? globalThis : window));
