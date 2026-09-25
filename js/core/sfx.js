(function (root) {
  'use strict';

  // Low-latency sound effects. <audio> elements on Android WebView start
  // 50-150 ms late, and several of our files open with 30-160 ms of encoder
  // silence. Here each file is fetched and decoded once, the leading silence
  // is measured and skipped, and playback goes through Web Audio, which starts
  // within a frame. Falls back to <audio> when Web Audio is unavailable.

  const SILENCE = 0.003; // Amplitude below this counts as silence.
  const PRE_ROLL = 0.002; // Keep 2 ms before the onset so the attack is not clipped.

  const AudioContextClass = root.AudioContext || root.webkitAudioContext;
  let context = null;
  let output = null;
  const sounds = new Map();

  function audioContext() {
    if (!AudioContextClass) return null;
    if (!context) {
      try {
        context = new AudioContextClass({ latencyHint: 'interactive' });
        output = context.createGain();
        output.connect(context.destination);
      } catch (_) {
        context = null;
      }
    }
    return context;
  }

  // Browsers start the context suspended until the first gesture. Resume on
  // the first touch so the first real sound is not the one that gets lost.
  function unlock() {
    const ctx = audioContext();
    if (ctx && ctx.state === 'suspended') ctx.resume().catch(() => {});
  }
  ['pointerdown', 'touchstart', 'keydown'].forEach(type => {
    root.addEventListener?.(type, unlock, { capture: true, passive: true });
  });

  function onsetOf(buffer) {
    let first = buffer.length;
    for (let channel = 0; channel < buffer.numberOfChannels; channel += 1) {
      const data = buffer.getChannelData(channel);
      for (let index = 0; index < Math.min(first, data.length); index += 1) {
        if (Math.abs(data[index]) > SILENCE) {
          first = index;
          break;
        }
      }
    }
    if (first >= buffer.length) return 0;
    return Math.max(0, first / buffer.sampleRate - PRE_ROLL);
  }

  function register(name, src, options = {}) {
    if (sounds.has(name)) return sounds.get(name);
    const entry = { src, volume: options.volume ?? 0.85, buffer: null, offset: 0, loading: null, fallback: null };
    sounds.set(name, entry);
    if (options.preload !== false) load(entry);
    return entry;
  }

  function load(entry) {
    const ctx = audioContext();
    if (!ctx || entry.loading) return entry.loading;
    entry.loading = fetch(entry.src)
      .then(response => {
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        return response.arrayBuffer();
      })
      .then(bytes => new Promise((resolve, reject) => {
        // The callback form works on older WebViews where the promise form is missing.
        const result = ctx.decodeAudioData(bytes, resolve, reject);
        if (result && typeof result.then === 'function') result.then(resolve, reject);
      }))
      .then(buffer => {
        entry.buffer = buffer;
        entry.offset = onsetOf(buffer);
        return buffer;
      })
      .catch(error => {
        console.warn('[sfx] falling back to <audio> for', entry.src, error?.message || error);
        entry.buffer = null;
      });
    return entry.loading;
  }

  function playFallback(entry) {
    try {
      if (!entry.fallback) {
        entry.fallback = new Audio(entry.src);
        entry.fallback.preload = 'auto';
      }
      const audio = entry.fallback;
      audio.volume = entry.volume;
      audio.currentTime = 0;
      audio.play().catch(() => {});
    } catch (_) {
      // Sound is decoration; never let it break an interaction.
    }
  }

  function play(name, options = {}) {
    const entry = sounds.get(name);
    if (!entry) return;
    const ctx = audioContext();
    if (!ctx || !entry.buffer) {
      // Not decoded yet: play through <audio> this once and keep loading.
      if (ctx) load(entry);
      playFallback(entry);
      return;
    }
    try {
      if (ctx.state === 'suspended') ctx.resume().catch(() => {});
      const source = ctx.createBufferSource();
      source.buffer = entry.buffer;
      const gain = ctx.createGain();
      gain.gain.value = options.volume ?? entry.volume;
      source.connect(gain);
      gain.connect(output);
      source.start(0, entry.offset);
    } catch (_) {
      playFallback(entry);
    }
  }

  const api = { register, play, unlock };
  root.EruditeSfx = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
}(typeof globalThis !== 'undefined' ? globalThis : window));
