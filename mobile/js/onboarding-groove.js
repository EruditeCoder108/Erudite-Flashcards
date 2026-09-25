(function (root) {
  'use strict';

  // The onboarding groove: a slab drawn in an engraving style, a rubbing
  // stone, and a groove whose depth is real geometry. Two light passes
  // (rereading) barely mark it; three firm passes (recall) cut it deep.
  //
  // The slab is a block seen from the front and a little above. The groove
  // runs from the front edge towards the back, so its depth shows as a notch
  // in the front face.

  const NS = 'http://www.w3.org/2000/svg';
  const FRONT = { x: 132, y: 104 }; // Groove mouth on the front edge.
  const BACK = { x: 204, y: 66 }; // Groove end on the back edge.
  const PASSES = [
    { depth: 1.2, width: 7, duration: 1150, phase: 'reread' },
    { depth: 2, width: 9, duration: 1050, phase: 'reread' },
    { depth: 8, width: 26, duration: 900, phase: 'recall' },
    { depth: 13, width: 38, duration: 850, phase: 'recall' },
    { depth: 18, width: 50, duration: 800, phase: 'recall' }
  ];

  let running = null;

  function el(name, attrs = {}, parent) {
    const node = document.createElementNS(NS, name);
    Object.entries(attrs).forEach(([key, value]) => node.setAttribute(key, String(value)));
    if (parent) parent.appendChild(node);
    return node;
  }

  function lerp(a, b, t) {
    return a + (b - a) * t;
  }

  function easeInOut(t) {
    return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
  }

  function frontPath(depth, width) {
    const half = width / 2;
    // Rounded V: the stone wears a soft trough, not a knife cut.
    return [
      'M20 104',
      `L${FRONT.x - half} 104`,
      `C${FRONT.x - half * 0.45} 104 ${FRONT.x - half * 0.35} ${104 + depth} ${FRONT.x} ${104 + depth}`,
      `C${FRONT.x + half * 0.35} ${104 + depth} ${FRONT.x + half * 0.45} 104 ${FRONT.x + half} 104`,
      'L244 104 L244 168 L20 168 Z'
    ].join(' ');
  }

  function groovePath(depth, width) {
    // The trough on the top face narrows towards the back (perspective).
    const half = width / 2;
    const backHalf = half * 0.62;
    const sink = depth * 0.55;
    return [
      `M${FRONT.x - half} ${FRONT.y}`,
      `L${BACK.x - backHalf} ${BACK.y}`,
      `Q${BACK.x} ${BACK.y + sink * 0.5} ${BACK.x + backHalf} ${BACK.y}`,
      `L${FRONT.x + half} ${FRONT.y}`,
      `Q${FRONT.x} ${FRONT.y + sink} ${FRONT.x - half} ${FRONT.y}`,
      'Z'
    ].join(' ');
  }

  function valleyPath(depth) {
    const sink = depth * 0.55;
    return `M${FRONT.x} ${FRONT.y + sink * 0.9} L${BACK.x} ${BACK.y + sink * 0.45}`;
  }

  function build(container) {
    container.replaceChildren();
    const svg = el('svg', { viewBox: '0 0 320 200', class: 'groove-svg', 'aria-hidden': 'true', focusable: 'false' });
    const defs = el('defs', {}, svg);
    const uid = `groove-${Math.random().toString(36).slice(2, 8)}`;

    const hatchFront = el('pattern', { id: `${uid}-hf`, width: 6, height: 6, patternUnits: 'userSpaceOnUse' }, defs);
    el('path', { d: 'M0 3 H6', class: 'hatch' }, hatchFront);
    const hatchSide = el('pattern', { id: `${uid}-hs`, width: 5, height: 5, patternUnits: 'userSpaceOnUse', patternTransform: 'rotate(-35)' }, defs);
    el('path', { d: 'M0 2.5 H5', class: 'hatch' }, hatchSide);
    const hatchGroove = el('pattern', { id: `${uid}-hg`, width: 3, height: 3, patternUnits: 'userSpaceOnUse', patternTransform: 'rotate(28)' }, defs);
    el('path', { d: 'M0 1.5 H3', class: 'hatch dense' }, hatchGroove);
    const stipple = el('pattern', { id: `${uid}-st`, width: 14, height: 9, patternUnits: 'userSpaceOnUse' }, defs);
    el('circle', { cx: 3, cy: 2, r: 0.7, class: 'dot' }, stipple);
    el('circle', { cx: 10, cy: 6.5, r: 0.6, class: 'dot' }, stipple);
    const clip = el('clipPath', { id: `${uid}-clip` }, defs);
    const clipFront = el('path', { d: frontPath(0, 0) }, clip);

    // Ground shadow.
    el('ellipse', { cx: 160, cy: 176, rx: 150, ry: 9, class: 'ground' }, svg);

    // Right face.
    const right = el('path', { d: 'M244 104 L300 66 L300 130 L244 168 Z', class: 'face side' }, svg);
    right.setAttribute('fill', `url(#${uid}-hs)`);
    el('path', { d: 'M244 104 L300 66 L300 130 L244 168 Z', class: 'edge' }, svg);

    // Top face.
    el('path', { d: 'M20 104 L76 66 L300 66 L244 104 Z', class: 'face top' }, svg);
    el('path', { d: 'M20 104 L76 66 L300 66 L244 104 Z', class: 'stipple', fill: `url(#${uid}-st)` }, svg);

    // Groove on the top face.
    const groove = el('path', { d: groovePath(0, 0), class: 'groove' }, svg);
    const grooveHatch = el('path', { d: groovePath(0, 0), class: 'groove-hatch', fill: `url(#${uid}-hg)` }, svg);
    const valley = el('path', { d: valleyPath(0), class: 'valley' }, svg);
    el('path', { d: 'M20 104 L76 66 L300 66 L244 104 Z', class: 'edge' }, svg);

    // Front face with the notch, hatched and clipped to its outline.
    const front = el('path', { d: frontPath(0, 0), class: 'face front' }, svg);
    const hatchGroup = el('g', { 'clip-path': `url(#${uid}-clip)` }, svg);
    el('rect', { x: 20, y: 104, width: 224, height: 64, fill: `url(#${uid}-hf)`, class: 'front-hatch' }, hatchGroup);
    const frontEdge = el('path', { d: frontPath(0, 0), class: 'edge' }, svg);

    // Dust falls from the groove mouth.
    const dust = el('g', { class: 'dust' }, svg);

    // The rubbing stone.
    const stone = el('g', { class: 'stone' }, svg);
    el('path', { d: 'M-24 2 C-24 -9 -10 -15 3 -14 C16 -13 25 -7 24 2 C23 10 10 13 -2 13 C-15 13 -24 10 -24 2 Z', class: 'stone-body' }, stone);
    el('path', { d: 'M-24 2 C-24 -9 -10 -15 3 -14 C16 -13 25 -7 24 2 C23 10 10 13 -2 13 C-15 13 -24 10 -24 2 Z', class: 'stone-stipple', fill: `url(#${uid}-st)` }, stone);
    el('path', { d: 'M-15 -6 C-9 -11 2 -12 9 -10', class: 'stone-shine' }, stone);
    el('path', { d: 'M-24 2 C-24 -9 -10 -15 3 -14 C16 -13 25 -7 24 2 C23 10 10 13 -2 13 C-15 13 -24 10 -24 2 Z', class: 'edge' }, stone);

    container.appendChild(svg);
    return { svg, groove, grooveHatch, valley, front, frontEdge, clipFront, stone, dust };
  }

  function setDepth(parts, depth, width) {
    parts.groove.setAttribute('d', groovePath(depth, width));
    parts.grooveHatch.setAttribute('d', groovePath(depth, width));
    parts.valley.setAttribute('d', valleyPath(depth));
    parts.valley.style.opacity = String(Math.min(1, depth / 10));
    const d = frontPath(depth, width);
    parts.front.setAttribute('d', d);
    parts.frontEdge.setAttribute('d', d);
    parts.clipFront.setAttribute('d', d);
  }

  function placeStone(parts, t, depth) {
    const x = lerp(FRONT.x, BACK.x, t);
    const y = lerp(FRONT.y, BACK.y, t) - 12 + depth * 0.45;
    const scale = lerp(1, 0.74, t);
    parts.stone.setAttribute('transform', `translate(${x.toFixed(2)} ${y.toFixed(2)}) scale(${scale.toFixed(3)})`);
  }

  function dropDust(parts, amount) {
    for (let index = 0; index < amount; index += 1) {
      const grain = el('circle', {
        cx: (FRONT.x + (Math.random() - 0.5) * 18).toFixed(1),
        cy: 106,
        r: (0.8 + Math.random() * 1.1).toFixed(2),
        class: 'grain'
      }, parts.dust);
      grain.style.setProperty('--dx', `${((Math.random() - 0.5) * 26).toFixed(1)}px`);
      grain.style.setProperty('--dy', `${(40 + Math.random() * 24).toFixed(1)}px`);
      grain.style.animationDelay = `${Math.round(Math.random() * 180)}ms`;
      root.setTimeout(() => grain.remove(), 1400);
    }
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
    setDepth(parts, 0, 0);
    placeStone(parts, 0, 0);
    parts.stone.style.opacity = '0';
    caption?.removeAttribute('data-phase');
  }

  function finish(parts, caption, options = {}) {
    const last = PASSES[PASSES.length - 1];
    setDepth(parts, last.depth, last.width);
    parts.svg.classList.add('is-cut');
    caption?.setAttribute('data-phase', 'done');
    // Park the stone at the far end so the cut at the front stays visible.
    if (!options.animate) {
      placeStone(parts, 1, last.depth);
      return;
    }
    const run = { cancelled: false, frame: 0 };
    running = run;
    let startedAt = 0;
    const glide = now => {
      if (run.cancelled) return;
      if (!startedAt) startedAt = now;
      const t = Math.min(1, (now - startedAt) / 900);
      placeStone(parts, easeInOut(t), last.depth);
      if (t < 1) run.frame = root.requestAnimationFrame(glide);
      else running = null;
    };
    run.frame = root.requestAnimationFrame(glide);
  }

  function start(container, caption, options = {}) {
    stop();
    if (!container) return;
    const parts = build(container);
    setDepth(parts, 0, 0);
    if (options.reducedMotion) {
      finish(parts, caption);
      return;
    }
    const run = { cancelled: false, frame: 0 };
    running = run;
    let passIndex = 0;
    let passStart = 0;
    let previous = { depth: 0, width: 0 };
    placeStone(parts, 0, 0);
    parts.stone.style.opacity = '1';
    caption?.setAttribute('data-phase', PASSES[0].phase);

    const tick = now => {
      if (run.cancelled) return;
      if (!passStart) passStart = now;
      const pass = PASSES[passIndex];
      const t = Math.max(0, Math.min(1, (now - passStart) / pass.duration));
      // One pass is there and back. The groove deepens on the way out.
      const outward = t < 0.5;
      const travel = easeInOut(outward ? t * 2 : 2 - t * 2);
      const cut = outward ? easeInOut(t * 2) : 1;
      const depth = lerp(previous.depth, pass.depth, cut);
      const width = lerp(previous.width, pass.width, cut);
      setDepth(parts, depth, width);
      // A firm pass presses the stone in; a light one skims.
      const press = pass.phase === 'recall' ? Math.sin(t * Math.PI) * 2.5 : 0;
      placeStone(parts, travel, depth + press);

      if (t >= 1) {
        if (pass.phase === 'recall') dropDust(parts, 7);
        else dropDust(parts, 2);
        previous = { depth: pass.depth, width: pass.width };
        passIndex += 1;
        passStart = now;
        if (passIndex >= PASSES.length) {
          running = null;
          finish(parts, caption, { animate: true });
          options.onDone?.();
          return;
        }
        caption?.setAttribute('data-phase', PASSES[passIndex].phase);
        if (PASSES[passIndex].phase === 'recall' && pass.phase === 'reread') {
          // A beat between the two kinds of pass so the change is noticed.
          passStart = now + 380;
        }
      }
      run.frame = root.requestAnimationFrame(tick);
    };
    run.frame = root.requestAnimationFrame(tick);
  }

  root.EruditeGroove = { start, reset, stop };
}(window));
