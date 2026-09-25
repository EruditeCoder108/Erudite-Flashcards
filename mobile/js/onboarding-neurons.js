(function (root) {
  'use strict';

  // The onboarding neuron scene: a small network drawn in ink, with one
  // chain of neurons that stands for a single memory. Rereading sends a
  // faint signal along it and barely changes it. Each recall sends a bright
  // signal, lights the neurons it passes, and leaves the connections
  // thicker and brighter. A simplified picture, drawn to match the groove.

  const NS = 'http://www.w3.org/2000/svg';
  const NODES = [
    [24, 112], [58, 58], [70, 156], [104, 98], [118, 30], [134, 170],
    [150, 62], [166, 130], [198, 92], [206, 30], [216, 172], [240, 124],
    [258, 60], [276, 162], [296, 100], [302, 34]
  ];
  // The memory: left to right through the middle of the network.
  const MEMORY = [0, 3, 7, 8, 11, 14];
  const PASSES = [
    { phase: 'reread', duration: 1500, gain: 0.05 },
    { phase: 'reread', duration: 1400, gain: 0.05 },
    { phase: 'recall', duration: 1050, gain: 0.25 },
    { phase: 'recall', duration: 950, gain: 0.25 },
    { phase: 'recall', duration: 900, gain: 0.3 }
  ];
  const BASE_STRENGTH = 0.1;

  let running = null;

  function el(name, attrs = {}, parent) {
    const node = document.createElementNS(NS, name);
    Object.entries(attrs).forEach(([key, value]) => node.setAttribute(key, String(value)));
    if (parent) parent.appendChild(node);
    return node;
  }

  // Deterministic "randomness" so the drawing is the same every time.
  function seeded(seed) {
    let value = seed;
    return () => {
      value = (value * 16807) % 2147483647;
      return (value - 1) / 2147483646;
    };
  }

  function distance(a, b) {
    return Math.hypot(a[0] - b[0], a[1] - b[1]);
  }

  // A gently curved connection; the bend direction alternates by index.
  function curve(a, b, index) {
    const mx = (a[0] + b[0]) / 2;
    const my = (a[1] + b[1]) / 2;
    const dx = b[0] - a[0];
    const dy = b[1] - a[1];
    const length = Math.hypot(dx, dy) || 1;
    const bend = (index % 2 ? 1 : -1) * Math.min(10, length * 0.12);
    const cx = mx - (dy / length) * bend;
    const cy = my + (dx / length) * bend;
    return { d: `M${a[0]} ${a[1]} Q${cx.toFixed(1)} ${cy.toFixed(1)} ${b[0]} ${b[1]}`, c: [cx, cy] };
  }

  function edgeKey(a, b) {
    return a < b ? `${a}-${b}` : `${b}-${a}`;
  }

  function build(container) {
    container.replaceChildren();
    const svg = el('svg', { viewBox: '0 0 320 200', class: 'neuron-svg', 'aria-hidden': 'true', focusable: 'false' });
    const random = seeded(7);

    const memoryEdges = new Set();
    for (let index = 0; index < MEMORY.length - 1; index += 1) memoryEdges.add(edgeKey(MEMORY[index], MEMORY[index + 1]));

    // Background connections between near neighbours.
    const web = el('g', { class: 'web' }, svg);
    let edgeIndex = 0;
    for (let a = 0; a < NODES.length; a += 1) {
      for (let b = a + 1; b < NODES.length; b += 1) {
        if (memoryEdges.has(edgeKey(a, b))) continue;
        if (distance(NODES[a], NODES[b]) > 78) continue;
        el('path', { d: curve(NODES[a], NODES[b], edgeIndex).d, class: 'synapse' }, web);
        edgeIndex += 1;
      }
    }

    // The memory path: an ink base and an accent overlay whose strength grows.
    const memoryBase = el('g', { class: 'memory-base' }, svg);
    const memoryGlow = el('g', { class: 'memory-glow' }, svg);
    let traceD = '';
    MEMORY.forEach((node, index) => {
      if (index === MEMORY.length - 1) return;
      const a = NODES[node];
      const b = NODES[MEMORY[index + 1]];
      const shape = curve(a, b, index + 3);
      el('path', { d: shape.d }, memoryBase);
      el('path', { d: shape.d }, memoryGlow);
      traceD += index === 0 ? shape.d : ` Q${shape.c[0].toFixed(1)} ${shape.c[1].toFixed(1)} ${b[0]} ${b[1]}`;
    });
    const trace = el('path', { d: traceD, class: 'trace' }, svg);

    // Neurons: a soma and a few dendrites each.
    const cells = NODES.map((point, index) => {
      const group = el('g', { class: 'neuron', transform: `translate(${point[0]} ${point[1]})` }, svg);
      const count = 3 + Math.floor(random() * 2);
      for (let branch = 0; branch < count; branch += 1) {
        const angle = (branch / count) * Math.PI * 2 + random() * 1.2;
        const reach = 7 + random() * 5;
        const x1 = Math.cos(angle) * 4.5;
        const y1 = Math.sin(angle) * 4.5;
        const x2 = Math.cos(angle) * reach;
        const y2 = Math.sin(angle) * reach;
        const bend = angle + 0.5;
        el('path', {
          d: `M${x1.toFixed(1)} ${y1.toFixed(1)} Q${(Math.cos(bend) * reach * 0.7).toFixed(1)} ${(Math.sin(bend) * reach * 0.7).toFixed(1)} ${x2.toFixed(1)} ${y2.toFixed(1)}`,
          class: 'dendrite'
        }, group);
      }
      const memory = MEMORY.includes(index);
      const radius = memory ? 5.2 : 4.2;
      const soma = el('circle', { r: radius, class: 'soma' }, group);
      let core = null;
      let ring = null;
      if (memory) {
        group.classList.add('is-memory');
        // The core fills in with strength; the ring expands when it fires.
        core = el('circle', { r: radius - 0.6, class: 'core' }, group);
        core.style.opacity = '0';
        ring = el('circle', { r: radius, class: 'ring' }, group);
      }
      return { group, soma, core, ring, index };
    });

    const pulse = el('circle', { r: 3, class: 'pulse' }, svg);
    pulse.style.opacity = '0';

    container.appendChild(svg);

    // Where each memory neuron sits along the trace, for lighting them up.
    const total = trace.getTotalLength();
    const stops = MEMORY.map(node => {
      const [x, y] = NODES[node];
      let best = 0;
      let bestDistance = Infinity;
      for (let step = 0; step <= 120; step += 1) {
        const length = (step / 120) * total;
        const point = trace.getPointAtLength(length);
        const gap = Math.hypot(point.x - x, point.y - y);
        if (gap < bestDistance) {
          bestDistance = gap;
          best = length;
        }
      }
      return { node, at: best / total };
    });

    return { svg, trace, total, pulse, memoryGlow, memoryBase, cells, stops };
  }

  function setStrength(parts, strength) {
    const value = Math.max(0, Math.min(1, strength));
    parts.memoryGlow.style.opacity = String(value);
    parts.memoryGlow.style.strokeWidth = String(1 + value * 2.4);
    parts.memoryBase.style.opacity = String(0.25 + value * 0.2);
    parts.cells.forEach(cell => {
      if (cell.core) cell.core.style.opacity = (value * 0.95).toFixed(3);
    });
  }

  function stop() {
    if (running) {
      running.cancelled = true;
      root.cancelAnimationFrame(running.frame);
      running = null;
    }
  }

  function reset(container, caption) {
    stop();
    if (!container) return;
    const parts = build(container);
    setStrength(parts, BASE_STRENGTH);
    caption?.removeAttribute('data-phase');
  }

  function finish(parts, caption) {
    setStrength(parts, 1);
    parts.pulse.style.opacity = '0';
    parts.svg.classList.add('is-strong');
    caption?.setAttribute('data-phase', 'done');
  }

  function start(container, caption, options = {}) {
    stop();
    if (!container) return;
    const parts = build(container);
    let strength = BASE_STRENGTH;
    setStrength(parts, strength);
    if (options.reducedMotion) {
      finish(parts, caption);
      return;
    }

    const run = { cancelled: false, frame: 0 };
    running = run;
    let passIndex = 0;
    let passStart = 0;
    let lit = new Set();
    caption?.setAttribute('data-phase', PASSES[0].phase);

    const tick = now => {
      if (run.cancelled) return;
      if (!passStart) passStart = now;
      const pass = PASSES[passIndex];
      const t = Math.max(0, Math.min(1, (now - passStart) / pass.duration));
      const recall = pass.phase === 'recall';

      // The signal travels the whole path, easing in and out.
      const eased = t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;
      const point = parts.trace.getPointAtLength(eased * parts.total);
      parts.pulse.setAttribute('cx', point.x.toFixed(2));
      parts.pulse.setAttribute('cy', point.y.toFixed(2));
      parts.pulse.setAttribute('r', recall ? '3.6' : '2.4');
      parts.pulse.classList.toggle('is-recall', recall);
      parts.pulse.style.opacity = String((recall ? 1 : 0.45) * Math.min(1, t * 8, (1 - t) * 8));

      // Neurons flash as the signal reaches them; recall lights them fully.
      parts.stops.forEach(stopPoint => {
        const cell = parts.cells[stopPoint.node];
        if (eased >= stopPoint.at && !lit.has(stopPoint.node)) {
          lit.add(stopPoint.node);
          if (cell.ring) {
            cell.ring.classList.remove('is-firing', 'is-flicker');
            void cell.ring.getBoundingClientRect();
            cell.ring.classList.add(recall ? 'is-firing' : 'is-flicker');
          }
        }
      });

      // Strength grows during the pass, so the path visibly thickens.
      setStrength(parts, strength + pass.gain * eased);

      if (t >= 1) {
        strength += pass.gain;
        passIndex += 1;
        passStart = now;
        lit = new Set();
        if (passIndex >= PASSES.length) {
          running = null;
          finish(parts, caption);
          options.onDone?.();
          return;
        }
        caption?.setAttribute('data-phase', PASSES[passIndex].phase);
        if (PASSES[passIndex].phase === 'recall' && pass.phase === 'reread') passStart = now + 420;
        else passStart = now + 160;
      }
      run.frame = root.requestAnimationFrame(tick);
    };
    run.frame = root.requestAnimationFrame(tick);
  }

  root.EruditeNeurons = { start, reset, stop };
}(window));
