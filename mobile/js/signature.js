(function (root) {
  'use strict';

  // Hand-built moments used in a few places only: the daily goal ring, the
  // session-complete check, and the flashcard burst. Everything runs through
  // the Web Animations API on transform, opacity, and stroke-dashoffset.

  const motion = () => root.EruditeMotion;
  const reduced = () => Boolean(motion()?.prefersReducedMotion?.());
  const SVG_NS = 'http://www.w3.org/2000/svg';
  const TICKS = 60;
  const GOAL_STORE_KEY = 'erudite-goal-ring-last';

  function clamp(value, min, max) {
    return Math.min(max, Math.max(min, value));
  }

  // ------------------------------------------------------------------
  // Goal ring
  // ------------------------------------------------------------------

  function tickPath(index) {
    const angle = (index / TICKS) * Math.PI * 2;
    const major = index % 5 === 0;
    const outer = 57;
    const inner = major ? 51.5 : 53.5;
    const sin = Math.sin(angle);
    const cos = Math.cos(angle);
    const x1 = (60 + sin * inner).toFixed(2);
    const y1 = (60 - cos * inner).toFixed(2);
    const x2 = (60 + sin * outer).toFixed(2);
    const y2 = (60 - cos * outer).toFixed(2);
    return `<line class="goal-tick${major ? ' major' : ''}" data-tick="${index}" x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" />`;
  }

  function litTicks(progress) {
    return Math.round((clamp(progress, 0, 100) / 100) * TICKS);
  }

  /** Static markup; animateGoalRing brings it to life. */
  function goalRingMarkup({ progress = 0, label = 'Goal' } = {}) {
    const value = clamp(Math.round(progress), 0, 100);
    const ticks = Array.from({ length: TICKS }, (_, index) => tickPath(index)).join('');
    return `
      <div class="goal-ring${value >= 100 ? ' is-complete' : ''}" data-progress="${value}" role="img" aria-label="${value}% of today's goal">
        <svg class="goal-ring-art" viewBox="0 0 120 120" aria-hidden="true">
          <g class="goal-ticks">${ticks}</g>
          <circle class="goal-track" cx="60" cy="60" r="43" />
          <circle class="goal-arc" cx="60" cy="60" r="43" pathLength="100" transform="rotate(-90 60 60)"
                  style="stroke-dashoffset:${100 - value}" />
          <g class="goal-tip" style="transform:rotate(${value * 3.6}deg)">
            <circle class="goal-tip-halo" cx="60" cy="17" r="6" />
            <circle class="goal-tip-dot" cx="60" cy="17" r="3.1" />
          </g>
        </svg>
        <div class="goal-ring-copy">
          <strong><span class="goal-value">${value}</span><span class="goal-unit">%</span></strong>
          <span class="goal-label">${label}</span>
        </div>
      </div>
    `;
  }

  function dayToken() {
    const now = new Date(Date.now() - 4 * 60 * 60 * 1000);
    return `${now.getFullYear()}-${now.getMonth()}-${now.getDate()}`;
  }

  function lastShownProgress() {
    try {
      const saved = JSON.parse(root.localStorage.getItem(GOAL_STORE_KEY) || 'null');
      return saved && saved.day === dayToken() ? Number(saved.value) || 0 : 0;
    } catch (_) {
      return 0;
    }
  }

  function rememberProgress(value) {
    try {
      root.localStorage.setItem(GOAL_STORE_KEY, JSON.stringify({ day: dayToken(), value }));
    } catch (_) {
      // Optional: without storage the ring animates from zero.
    }
  }

  function setTicks(ring, count) {
    ring.querySelectorAll('.goal-tick').forEach(tick => {
      tick.classList.toggle('lit', Number(tick.dataset.tick) < count);
    });
  }

  // Where along a spring (0 -> 1) a fraction is first reached, as a share of the
  // duration. Used to light each tick exactly as the arc sweeps past it.
  function timeAtFraction(points, fraction) {
    for (let index = 0; index < points.length; index += 1) {
      if (points[index] >= fraction) return index / (points.length - 1);
    }
    return 1;
  }

  function countUp(element, from, to, curve) {
    if (!element) return;
    const start = performance.now();
    const { points, duration } = curve;
    const step = now => {
      const t = clamp((now - start) / duration, 0, 1);
      const position = t * (points.length - 1);
      const lower = Math.floor(position);
      const upper = Math.min(points.length - 1, lower + 1);
      const eased = points[lower] + (points[upper] - points[lower]) * (position - lower);
      element.textContent = String(clamp(Math.round(from + (to - from) * eased), 0, 100));
      if (t < 1) root.requestAnimationFrame(step);
    };
    root.requestAnimationFrame(step);
  }

  function bloom(ring) {
    const art = ring.querySelector('.goal-ring-art');
    if (!art) return;
    const ripple = document.createElementNS(SVG_NS, 'circle');
    ripple.setAttribute('class', 'goal-ripple');
    ripple.setAttribute('cx', '60');
    ripple.setAttribute('cy', '60');
    ripple.setAttribute('r', '43');
    art.appendChild(ripple);
    ripple.animate([
      { transform: 'scale(1)', opacity: 0.55, strokeWidth: 6 },
      { transform: 'scale(1.28)', opacity: 0, strokeWidth: 1 }
    ], { duration: 900, easing: 'cubic-bezier(0.22, 1, 0.36, 1)' }).finished.then(() => ripple.remove(), () => ripple.remove());
    ring.animate([
      { transform: 'scale(1)' },
      { transform: 'scale(1.045)' },
      { transform: 'scale(1)' }
    ], { duration: 520, easing: 'cubic-bezier(0.34, 1.4, 0.64, 1)' });
    root.EruditeHaptics?.success();
  }

  /**
   * Sweep the ring from the value shown last time today to the new value.
   * Returning from a study session therefore visibly adds the work just done.
   */
  function animateGoalRing(ring, progress, options = {}) {
    if (!ring) return;
    const to = clamp(Math.round(progress), 0, 100);
    const from = clamp(lastShownProgress(), 0, 100);
    if (options.remember !== false) rememberProgress(to);
    const arc = ring.querySelector('.goal-arc');
    const tip = ring.querySelector('.goal-tip');
    const valueEl = ring.querySelector('.goal-value');
    ring.classList.toggle('has-tip', to > 0 && to < 100);

    if (from === to || reduced() || !motion() || !arc?.animate) {
      setTicks(ring, litTicks(to));
      return;
    }

    const curve = motion().spring('gentle');
    const fromTicks = litTicks(from);
    const toTicks = litTicks(to);
    ring.classList.toggle('is-complete', from >= 100);
    setTicks(ring, fromTicks);
    valueEl.textContent = String(from);

    const timing = { duration: curve.duration, easing: curve.easing, fill: 'both' };
    arc.animate([{ strokeDashoffset: 100 - from }, { strokeDashoffset: 100 - to }], timing);
    tip?.animate([{ transform: `rotate(${from * 3.6}deg)` }, { transform: `rotate(${to * 3.6}deg)` }], timing);
    countUp(valueEl, from, to, curve);

    const low = Math.min(fromTicks, toTicks);
    const high = Math.max(fromTicks, toTicks);
    ring.querySelectorAll('.goal-tick').forEach(tick => {
      const index = Number(tick.dataset.tick);
      if (index < low || index >= high) return;
      const fraction = ((index + 1) / TICKS * 100 - from) / (to - from);
      const delay = timeAtFraction(curve.points, clamp(fraction, 0, 1)) * curve.duration;
      root.setTimeout(() => tick.classList.toggle('lit', to > from), delay);
    });

    if (to >= 100 && from < 100) {
      root.setTimeout(() => {
        ring.classList.add('is-complete');
        const label = ring.querySelector('.goal-label');
        if (label) label.textContent = 'Done';
        bloom(ring);
      }, curve.duration * 0.55);
    } else if (to < 100) {
      ring.classList.remove('is-complete');
    }
  }

  // ------------------------------------------------------------------
  // Session complete: a check that draws itself and a burst of tiny cards
  // ------------------------------------------------------------------

  function checkMarkup() {
    return `
      <svg class="done-check" viewBox="0 0 64 64" aria-hidden="true">
        <circle class="done-check-ring" cx="32" cy="32" r="28" pathLength="100" />
        <path class="done-check-mark" d="M20 33.5 28.5 42 45 24" pathLength="100" />
      </svg>
    `;
  }

  function drawCheck(host) {
    if (!host) return;
    host.innerHTML = checkMarkup();
    const ring = host.querySelector('.done-check-ring');
    const mark = host.querySelector('.done-check-mark');
    if (reduced() || !ring.animate) return;
    ring.animate([{ strokeDashoffset: 100 }, { strokeDashoffset: 0 }], {
      duration: 620, easing: 'cubic-bezier(0.65, 0, 0.35, 1)', fill: 'both'
    });
    mark.animate([{ strokeDashoffset: 100 }, { strokeDashoffset: 0 }], {
      duration: 380, delay: 480, easing: 'cubic-bezier(0.22, 1, 0.36, 1)', fill: 'both'
    });
    host.animate([
      { transform: 'scale(0.6)', opacity: 0 },
      { transform: 'scale(1)', opacity: 1 }
    ], { ...motion().spring('settle'), fill: 'both' });
  }

  /**
   * Throw a handful of miniature flashcards from an element. Each follows a
   * real ballistic arc (sampled into keyframes) and tumbles as it falls.
   */
  function cardBurst(anchor, options = {}) {
    if (!anchor || reduced() || !document.body.animate) return;
    const lowEnd = document.documentElement.classList.contains('is-low-end');
    const count = options.count || (lowEnd ? 9 : 16);
    const rect = anchor.getBoundingClientRect();
    const originX = rect.left + rect.width / 2;
    const originY = rect.top + rect.height / 2;
    const colors = ['var(--again)', 'var(--hard)', 'var(--good)', 'var(--easy)', 'var(--primary)', 'var(--text)'];
    const layer = document.createElement('div');
    layer.className = 'card-burst';
    document.body.appendChild(layer);

    const flights = [];
    for (let index = 0; index < count; index += 1) {
      const card = document.createElement('span');
      card.className = 'burst-card';
      card.style.setProperty('--burst-color', colors[index % colors.length]);
      card.style.left = `${originX}px`;
      card.style.top = `${originY}px`;
      layer.appendChild(card);

      // Fan the launch upwards, a little wider on each side.
      const spread = (index / (count - 1) - 0.5) * 2;
      const angle = (-90 + spread * 62 + (Math.random() - 0.5) * 14) * (Math.PI / 180);
      const speed = 520 + Math.random() * 360;
      const vx = Math.cos(angle) * speed;
      const vy = Math.sin(angle) * speed;
      const gravity = 1500;
      const spin = (Math.random() - 0.5) * 900;
      const tilt = (Math.random() - 0.5) * 70;
      const life = 1.15 + Math.random() * 0.35;
      const frames = [];
      const steps = 14;
      for (let step = 0; step <= steps; step += 1) {
        const t = (life * step) / steps;
        const drag = 1 - Math.min(0.45, t * 0.32);
        const x = vx * t * drag;
        const y = vy * t * drag + 0.5 * gravity * t * t;
        const progress = step / steps;
        frames.push({
          transform: `translate(${x.toFixed(1)}px, ${y.toFixed(1)}px) rotate(${(spin * t).toFixed(1)}deg) rotateX(${(tilt * progress * 4).toFixed(1)}deg) scale(${(0.6 + Math.min(1, progress * 5) * 0.4).toFixed(3)})`,
          opacity: progress < 0.75 ? 1 : 1 - (progress - 0.75) / 0.25
        });
      }
      flights.push(card.animate(frames, {
        duration: life * 1000,
        delay: index * 12,
        easing: 'linear',
        fill: 'both'
      }).finished.catch(() => undefined));
    }
    Promise.all(flights).then(() => layer.remove());
  }

  function countUpNumber(element, to, duration = 700) {
    if (!element) return;
    const target = Number(to) || 0;
    if (reduced() || target <= 0) {
      element.textContent = String(target);
      return;
    }
    const start = performance.now();
    const step = now => {
      const t = clamp((now - start) / duration, 0, 1);
      const eased = 1 - Math.pow(1 - t, 3);
      element.textContent = String(Math.round(target * eased));
      if (t < 1) root.requestAnimationFrame(step);
    };
    root.requestAnimationFrame(step);
  }

  root.EruditeSignature = {
    goalRingMarkup,
    animateGoalRing,
    lastShownProgress,
    drawCheck,
    cardBurst,
    countUpNumber
  };
}(typeof globalThis !== 'undefined' ? globalThis : window));
