(function () {
  const STORAGE_KEY = 'erudite-mobile-performance-v1';
  const TRACE_KEY = 'erudite-mobile-performance-trace-v1';
  const CAPTURE_ENABLED_KEY = 'erudite-mobile-performance-capture-enabled-v1';
  const MAX_EVENTS = 800;
  const MAX_EVENT_AGE_MS = 48 * 60 * 60 * 1000;
  const PERSIST_DELAY_MS = 250;
  const page = /(?:^|\/)study\.html$/i.test(window.location.pathname) ? 'study' : 'library';
  const pageSessionId = `${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 8)}`;
  let traceId = '';
  let events = [];
  let persistTimer = null;
  let nextSpanId = 1;
  let captureEnabled = false;

  function round(value) {
    return Math.round(Number(value || 0) * 10) / 10;
  }

  function hash(value) {
    const input = String(value ?? '');
    let result = 2166136261;
    for (let index = 0; index < input.length; index += 1) {
      result ^= input.charCodeAt(index);
      result = Math.imul(result, 16777619);
    }
    return `hash-${(result >>> 0).toString(16)}`;
  }

  function initializeTraceId() {
    try {
      traceId = sessionStorage.getItem(TRACE_KEY) || '';
      if (!traceId) {
        traceId = `${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 10)}`;
        sessionStorage.setItem(TRACE_KEY, traceId);
      }
    } catch (_) {
      traceId = pageSessionId;
    }
  }

  function sanitizeError(error) {
    if (!error) return null;
    return {
      name: String(error.name || 'Error').slice(0, 80),
      message: String(error.message || error).slice(0, 500),
      stack: String(error.stack || '').slice(0, 1600)
    };
  }

  function sanitize(value, key = '', depth = 0, seen = new WeakSet()) {
    if (value === null || value === undefined) return value ?? null;
    if (typeof value === 'number') return Number.isFinite(value) ? value : String(value);
    if (typeof value === 'boolean') return value;
    if (typeof value === 'string') {
      if (/(?:deck|set|card)[_-]?id$|^(?:id|setId|cardId|deckId)$/i.test(key)) return hash(value);
      if (/(?:term|definition|question|answer|prompt|content|html|css|media|image|audio|video|dataUrl|clipboard|payload|fileName|deckName|setName|title|label|tag|search|query)/i.test(key)) {
        return `[redacted:${value.length}]`;
      }
      return value.slice(0, 500);
    }
    if (typeof value === 'bigint') return String(value);
    if (typeof value === 'function' || typeof value === 'symbol') return undefined;
    if (value instanceof Error) return sanitizeError(value);
    if (depth >= 4) return '[max-depth]';
    if (typeof value === 'object') {
      if (seen.has(value)) return '[circular]';
      seen.add(value);
    }
    if (Array.isArray(value)) {
      return value.slice(0, 30).map(item => sanitize(item, key, depth + 1, seen));
    }
    const output = {};
    Object.entries(value).slice(0, 40).forEach(([childKey, childValue]) => {
      const sanitized = sanitize(childValue, childKey, depth + 1, seen);
      if (sanitized !== undefined) output[childKey] = sanitized;
    });
    return output;
  }

  function loadEvents() {
    try {
      const parsed = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
      const cutoff = Date.now() - MAX_EVENT_AGE_MS;
      events = (Array.isArray(parsed) ? parsed : [])
        .filter(event => Number(event?.timestamp || 0) >= cutoff)
        .slice(-MAX_EVENTS);
    } catch (_) {
      events = [];
    }
  }

  function loadCapturePreference() {
    try {
      captureEnabled = localStorage.getItem(CAPTURE_ENABLED_KEY) === 'true';
    } catch (_) {
      captureEnabled = false;
    }
  }

  function isCaptureEnabled() {
    return captureEnabled;
  }

  function setCaptureEnabled(enabled) {
    captureEnabled = Boolean(enabled);
    try {
      localStorage.setItem(CAPTURE_ENABLED_KEY, String(captureEnabled));
    } catch (_) {}
    if (captureEnabled) {
      mark('diagnostics.capture_started');
      startEventLoopMonitor();
    } else {
      stopEventLoopMonitor();
    }
    return captureEnabled;
  }

  function persistNow() {
    clearTimeout(persistTimer);
    persistTimer = null;
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(events.slice(-MAX_EVENTS)));
    } catch (_) {
      events = events.slice(-Math.floor(MAX_EVENTS / 2));
      try { localStorage.setItem(STORAGE_KEY, JSON.stringify(events)); } catch (_error) {}
    }
  }

  function schedulePersist() {
    if (persistTimer) return;
    persistTimer = window.setTimeout(persistNow, PERSIST_DELAY_MS);
  }

  function consoleEvent(event) {
    const duration = Number(event.durationMs || 0);
    if (event.kind !== 'error' && event.kind !== 'longtask' && duration < 20) return;
    const suffix = duration ? ` ${duration.toFixed(1)}ms` : '';
    const method = event.kind === 'error' ? 'error' : 'info';
    try { console[method](`[mobile-perf] ${event.name}${suffix}`, event.data || ''); } catch (_) {}
  }

  function record(kind, name, data = {}, durationMs = null, startedAt = null) {
    if (!captureEnabled) return null;
    const event = {
      timestamp: Date.now(),
      traceId,
      pageSessionId,
      page,
      kind,
      name: String(name || 'unnamed').slice(0, 120),
      atMs: round(performance.now()),
      data: sanitize(data)
    };
    if (durationMs !== null) event.durationMs = round(durationMs);
    if (startedAt !== null) event.startedAtMs = round(startedAt);
    events.push(event);
    if (events.length > MAX_EVENTS) events.splice(0, events.length - MAX_EVENTS);
    schedulePersist();
    consoleEvent(event);
    return event;
  }

  function mark(name, data = {}) {
    return record('mark', name, data);
  }

  function start(name, data = {}) {
    if (!captureEnabled) return null;
    return {
      id: nextSpanId++,
      name: String(name || 'unnamed'),
      startedAt: performance.now(),
      data: sanitize(data)
    };
  }

  function end(span, data = {}) {
    if (!span || !Number.isFinite(span.startedAt)) return null;
    return record('span', span.name, {
      ...(span.data || {}),
      ...(sanitize(data) || {})
    }, performance.now() - span.startedAt, span.startedAt);
  }

  async function measure(name, work, data = {}) {
    const span = start(name, data);
    try {
      const result = await work();
      end(span, { status: 'ok' });
      return result;
    } catch (error) {
      end(span, { status: 'error', error: sanitizeError(error) });
      throw error;
    }
  }

  function clear() {
    events = [];
    persistNow();
    mark('diagnostics.history_cleared');
    persistNow();
  }

  function runtimeInfo() {
    const navigation = performance.getEntriesByType?.('navigation')?.[0];
    const memory = performance.memory;
    return sanitize({
      generatedAt: new Date().toISOString(),
      traceId,
      currentPage: page,
      eventCount: events.length,
      capacitorPlatform: window.Capacitor?.getPlatform?.() || 'web',
      userAgent: navigator.userAgent,
      language: navigator.language,
      hardwareConcurrency: navigator.hardwareConcurrency || null,
      deviceMemoryGb: navigator.deviceMemory || null,
      viewport: {
        width: window.innerWidth,
        height: window.innerHeight,
        devicePixelRatio: window.devicePixelRatio
      },
      navigation: navigation ? {
        type: navigation.type,
        domInteractiveMs: round(navigation.domInteractive),
        domContentLoadedMs: round(navigation.domContentLoadedEventEnd),
        loadEventMs: round(navigation.loadEventEnd),
        transferSize: navigation.transferSize || null
      } : null,
      heap: memory ? {
        usedBytes: memory.usedJSHeapSize,
        totalBytes: memory.totalJSHeapSize,
        limitBytes: memory.jsHeapSizeLimit
      } : null
    });
  }

  function summarizeEvents() {
    const totals = new Map();
    const slowestEvents = [];
    let spanCount = 0;
    let longTaskCount = 0;
    let errorCount = 0;
    let firstTimestamp = null;
    let lastTimestamp = null;

    events.forEach(event => {
      const timestamp = Number(event.timestamp || 0);
      if (timestamp) {
        firstTimestamp = firstTimestamp === null ? timestamp : Math.min(firstTimestamp, timestamp);
        lastTimestamp = lastTimestamp === null ? timestamp : Math.max(lastTimestamp, timestamp);
      }
      if (event.kind === 'span') spanCount += 1;
      if (event.kind === 'longtask') longTaskCount += 1;
      if (event.kind === 'error') errorCount += 1;

      const durationMs = Number(event.durationMs || 0);
      if (!durationMs) return;

      const key = String(event.name || 'unnamed');
      const bucket = totals.get(key) || {
        name: key,
        count: 0,
        totalMs: 0,
        maxMs: 0,
        page: event.page || null,
        kind: event.kind || null
      };
      bucket.count += 1;
      bucket.totalMs += durationMs;
      bucket.maxMs = Math.max(bucket.maxMs, durationMs);
      totals.set(key, bucket);

      slowestEvents.push({
        name: event.name,
        kind: event.kind,
        page: event.page,
        durationMs: event.durationMs,
        data: event.data || {}
      });
    });

    return sanitize({
      eventCount: events.length,
      spanCount,
      longTaskCount,
      errorCount,
      windowMs: firstTimestamp && lastTimestamp ? Math.max(0, lastTimestamp - firstTimestamp) : 0,
      slowestEvents: slowestEvents
        .sort((a, b) => Number(b.durationMs || 0) - Number(a.durationMs || 0))
        .slice(0, 25),
      totalsByName: Array.from(totals.values())
        .map(item => ({
          ...item,
          totalMs: round(item.totalMs),
          maxMs: round(item.maxMs),
          avgMs: round(item.totalMs / Math.max(1, item.count))
        }))
        .sort((a, b) => Number(b.totalMs || 0) - Number(a.totalMs || 0))
        .slice(0, 25)
    });
  }

  function report(extra = {}) {
    persistNow();
    return JSON.stringify({
      format: 'erudite-mobile-performance-report',
      version: 1,
      privacy: 'No card terms, definitions, HTML, media, deck names, or raw deck/card IDs are intentionally recorded.',
      runtime: runtimeInfo(),
      diagnosticCaptureEnabled: captureEnabled,
      summary: summarizeEvents(),
      extra: sanitize(extra),
      events: events.slice()
    }, null, 2);
  }

  initializeTraceId();
  loadEvents();
  loadCapturePreference();

  window.EruditeMobilePerf = {
    mark,
    start,
    end,
    measure,
    clear,
    report,
    snapshot: () => events.slice(),
    isCaptureEnabled,
    setCaptureEnabled,
    sanitizeError,
    flush: persistNow
  };

  mark('runtime.page_session_started', {
    readyState: document.readyState,
    eventCountBeforeStart: Math.max(0, events.length - 1)
  });

  window.addEventListener('error', event => {
    record('error', 'runtime.window_error', {
      error: sanitizeError(event.error || new Error(event.message || 'Window error')),
      sourceLine: Number(event.lineno || 0),
      sourceColumn: Number(event.colno || 0)
    });
  });

  window.addEventListener('unhandledrejection', event => {
    const reason = event.reason instanceof Error ? event.reason : new Error(String(event.reason || 'Unhandled rejection'));
    record('error', 'runtime.unhandled_rejection', { error: sanitizeError(reason) });
  });

  let eventLoopTimer = null;

  function stopEventLoopMonitor() {
    if (!eventLoopTimer) return;
    window.clearInterval(eventLoopTimer);
    eventLoopTimer = null;
  }

  function startEventLoopMonitor() {
    if (!captureEnabled || eventLoopTimer || document.hidden) return;
    let expectedTick = performance.now() + 1000;
    eventLoopTimer = window.setInterval(() => {
      const now = performance.now();
      const lag = now - expectedTick;
      expectedTick = now + 1000;
      if (lag >= 120) {
        record('longtask', 'runtime.event_loop_stall', {}, lag, now - lag);
      }
    }, 1000);
  }

  document.addEventListener('visibilitychange', () => {
    mark('runtime.visibility_changed', { hidden: document.hidden });
    if (document.hidden) {
      stopEventLoopMonitor();
      persistNow();
    } else {
      startEventLoopMonitor();
    }
  });
  window.addEventListener('pagehide', () => {
    stopEventLoopMonitor();
    persistNow();
  });

  window.addEventListener('load', () => {
    window.setTimeout(() => {
      const navigation = performance.getEntriesByType?.('navigation')?.[0];
      mark('runtime.window_loaded', navigation ? {
        domInteractiveMs: round(navigation.domInteractive),
        domContentLoadedMs: round(navigation.domContentLoadedEventEnd),
        loadEventMs: round(navigation.loadEventEnd)
      } : {});
    }, 0);
  }, { once: true });

  if (typeof PerformanceObserver === 'function') {
    try {
      const observer = new PerformanceObserver(list => {
        list.getEntries().forEach(entry => {
          record('longtask', 'runtime.long_task', {
            startTimeMs: round(entry.startTime)
          }, entry.duration, entry.startTime);
        });
      });
      observer.observe({ type: 'longtask', buffered: true });
    } catch (_) {}
  }

  startEventLoopMonitor();
})();
