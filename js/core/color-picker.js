/**
 * EruditeColorPicker — Custom canvas-based HSV color picker.
 * Works on mobile (touch) and desktop (mouse).
 * No external dependencies.
 *
 * Usage:
 *   EruditeColorPicker.open({ initial: '#3b82f6', title: 'Class Color' })
 *     .then(hex => { if (hex) doSomethingWith(hex); });
 */

(function(global) {
  'use strict';

  // ─── HSV / HEX helpers ───────────────────────────────────────────────────

  function hexToRgb(hex) {
    const clean = String(hex || '').replace(/^#/, '').trim();
    if (clean.length === 3) {
      const r = parseInt(clean[0] + clean[0], 16);
      const g = parseInt(clean[1] + clean[1], 16);
      const b = parseInt(clean[2] + clean[2], 16);
      return { r, g, b };
    }
    if (clean.length === 6) {
      return {
        r: parseInt(clean.substring(0, 2), 16),
        g: parseInt(clean.substring(2, 4), 16),
        b: parseInt(clean.substring(4, 6), 16)
      };
    }
    return null;
  }

  function rgbToHex(r, g, b) {
    return '#' + [r, g, b].map(v => Math.round(Math.max(0, Math.min(255, v))).toString(16).padStart(2, '0')).join('');
  }

  function rgbToHsv(r, g, b) {
    r /= 255; g /= 255; b /= 255;
    const max = Math.max(r, g, b), min = Math.min(r, g, b);
    const d = max - min;
    let h = 0, s = max === 0 ? 0 : d / max, v = max;
    if (d !== 0) {
      switch (max) {
        case r: h = ((g - b) / d + (g < b ? 6 : 0)) / 6; break;
        case g: h = ((b - r) / d + 2) / 6; break;
        case b: h = ((r - g) / d + 4) / 6; break;
      }
    }
    return { h, s, v };
  }

  function hsvToRgb(h, s, v) {
    const i = Math.floor(h * 6);
    const f = h * 6 - i;
    const p = v * (1 - s);
    const q = v * (1 - f * s);
    const t = v * (1 - (1 - f) * s);
    let r, g, b;
    switch (i % 6) {
      case 0: r = v; g = t; b = p; break;
      case 1: r = q; g = v; b = p; break;
      case 2: r = p; g = v; b = t; break;
      case 3: r = p; g = q; b = v; break;
      case 4: r = t; g = p; b = v; break;
      case 5: r = v; g = p; b = q; break;
      default: r = 0; g = 0; b = 0;
    }
    return { r: Math.round(r * 255), g: Math.round(g * 255), b: Math.round(b * 255) };
  }

  function isValidHex(str) {
    return /^#[0-9a-fA-F]{6}$/.test(String(str || ''));
  }

  // ─── Curated swatches ────────────────────────────────────────────────────

  const SWATCHES = [
    '#3b82f6', '#8b5cf6', '#ec4899', '#ef4444',
    '#f97316', '#eab308', '#22c55e', '#06b6d4',
    '#10b981', '#6366f1', '#f43f5e', '#84cc16',
    '#0ea5e9', '#a855f7'
  ];

  // ─── Canvas drawing ──────────────────────────────────────────────────────

  const WHEEL_R = 60; // outer radius px (canvas logical)
  const INNER_R = 40; // inner radius (the solid saturation area)
  const CANVAS_SIZE = 130;

  function drawWheel(canvas, hue, saturation) {
    const ctx = canvas.getContext('2d');
    const cx = CANVAS_SIZE / 2, cy = CANVAS_SIZE / 2;

    ctx.clearRect(0, 0, CANVAS_SIZE, CANVAS_SIZE);

    // Outer hue ring
    const ringOuter = WHEEL_R;
    const ringInner = INNER_R + 2;
    for (let angle = 0; angle < 360; angle++) {
      const startAngle = (angle - 1) * Math.PI / 180;
      const endAngle = (angle + 1) * Math.PI / 180;
      const gradient = ctx.createConicalGradient
        ? null // fallback below
        : null;
      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.arc(cx, cy, ringOuter, startAngle, endAngle);
      ctx.closePath();
      // Convert hue to a fully-saturated color
      const { r, g, b } = hsvToRgb(angle / 360, 1, 1);
      ctx.fillStyle = `rgb(${r},${g},${b})`;
      ctx.fill();
    }

    // Cut inner hole (ring effect)
    ctx.beginPath();
    ctx.arc(cx, cy, ringInner, 0, Math.PI * 2);
    ctx.fillStyle = getComputedStyle(canvas.closest('.erudite-picker-card') || document.body).backgroundColor || '#111e30';
    ctx.fill();

    // Inner saturation disc (at current hue, from white center to full-sat edge)
    const centerRgb = hsvToRgb(hue, 0, 1);
    const edgeRgb = hsvToRgb(hue, 1, 1);
    const satGrad = ctx.createRadialGradient(cx, cy, 0, cx, cy, ringInner);
    satGrad.addColorStop(0, `rgb(${centerRgb.r},${centerRgb.g},${centerRgb.b})`);
    satGrad.addColorStop(1, `rgb(${edgeRgb.r},${edgeRgb.g},${edgeRgb.b})`);
    ctx.beginPath();
    ctx.arc(cx, cy, ringInner, 0, Math.PI * 2);
    ctx.fillStyle = satGrad;
    ctx.fill();

    // Hue selector dot on ring
    const ringMidR = (ringOuter + ringInner) / 2;
    const hueAngle = hue * 2 * Math.PI - Math.PI / 2;
    const dotX = cx + ringMidR * Math.cos(hueAngle);
    const dotY = cy + ringMidR * Math.sin(hueAngle);
    ctx.beginPath();
    ctx.arc(dotX, dotY, 5.5, 0, Math.PI * 2);
    ctx.strokeStyle = '#fff';
    ctx.lineWidth = 2.5;
    ctx.stroke();
    ctx.fillStyle = `hsl(${Math.round(hue * 360)}, 100%, 50%)`;
    ctx.fill();

    // Saturation selector dot inside disc
    const satAngle = hue * 2 * Math.PI - Math.PI / 2;
    const satDotDist = saturation * ringInner;
    const satDotX = cx + satDotDist * Math.cos(satAngle);
    const satDotY = cy + satDotDist * Math.sin(satAngle);
    ctx.beginPath();
    ctx.arc(satDotX, satDotY, 5.5, 0, Math.PI * 2);
    ctx.strokeStyle = '#fff';
    ctx.lineWidth = 2.5;
    ctx.stroke();
    const { r: pr, g: pg, b: pb } = hsvToRgb(hue, saturation, 1);
    ctx.fillStyle = `rgb(${pr},${pg},${pb})`;
    ctx.fill();
  }

  function polarFromEvent(canvas, e) {
    const rect = canvas.getBoundingClientRect();
    const scaleX = CANVAS_SIZE / rect.width;
    const scaleY = CANVAS_SIZE / rect.height;
    const clientX = e.touches ? e.touches[0].clientX : e.clientX;
    const clientY = e.touches ? e.touches[0].clientY : e.clientY;
    const x = (clientX - rect.left) * scaleX - CANVAS_SIZE / 2;
    const y = (clientY - rect.top) * scaleY - CANVAS_SIZE / 2;
    const dist = Math.sqrt(x * x + y * y);
    const angle = Math.atan2(y, x); // -PI to PI
    const hue = ((angle + Math.PI / 2 + 2 * Math.PI) % (2 * Math.PI)) / (2 * Math.PI);
    return { dist, hue, x, y };
  }

  // ─── Main open function ──────────────────────────────────────────────────

  function open(options = {}) {
    return new Promise(resolve => {
      const initial = isValidHex(options.initial) ? options.initial : '#3b82f6';
      const title = options.title || 'Choose Color';

      // Parse initial color to HSV
      const initRgb = hexToRgb(initial) || { r: 59, g: 130, b: 246 };
      let { h: currentHue, s: currentSat, v: currentVal } = rgbToHsv(initRgb.r, initRgb.g, initRgb.b);

      let selectedHex = initial;

      function currentHex() {
        const { r, g, b } = hsvToRgb(currentHue, currentSat, currentVal);
        return rgbToHex(r, g, b);
      }

      // ── Build DOM ─────────────────────────────────────────────────────
      const overlay = document.createElement('div');
      overlay.className = 'erudite-picker-overlay';
      overlay.setAttribute('role', 'dialog');
      overlay.setAttribute('aria-modal', 'true');
      overlay.setAttribute('aria-label', title);

      const swatchesHtml = SWATCHES.map(sw => {
        const sel = sw.toLowerCase() === initial.toLowerCase() ? ' selected' : '';
        return `<button type="button" class="erudite-picker-swatch${sel}" data-swatch="${sw}" style="background:${sw}" aria-label="${sw}"></button>`;
      }).join('');

      overlay.innerHTML = `
        <div class="erudite-picker-card" role="document">
          <div class="erudite-picker-handle"></div>
          <div class="erudite-picker-title">
            <h3><i class="fas fa-palette"></i> ${title}</h3>
            <button type="button" class="erudite-picker-close" id="ecp-close" aria-label="Close">
              <i class="fas fa-times"></i>
            </button>
          </div>
          <div class="erudite-picker-swatches" id="ecp-swatches">${swatchesHtml}</div>
          <div class="erudite-picker-wheel-row">
            <div class="erudite-picker-wheel-wrap" id="ecp-wheel-wrap">
              <canvas id="ecp-canvas" class="erudite-picker-canvas" width="${CANVAS_SIZE}" height="${CANVAS_SIZE}"></canvas>
              <div class="erudite-picker-wheel-dot" id="ecp-dot"></div>
            </div>
            <div class="erudite-picker-controls">
              <div class="erudite-picker-preview-row">
                <div class="erudite-picker-preview" id="ecp-preview" style="background:${initial}"></div>
                <div class="erudite-picker-hex-wrap">
                  <span>#</span>
                  <input class="erudite-picker-hex" id="ecp-hex" type="text" maxlength="6"
                         value="${initial.replace('#', '')}" spellcheck="false"
                         autocomplete="off" inputmode="text"
                         aria-label="Hex color value"/>
                </div>
              </div>
              <div class="erudite-picker-brightness-label">
                <span>Brightness</span>
                <span id="ecp-bright-pct">${Math.round(currentVal * 100)}%</span>
              </div>
              <div class="erudite-picker-brightness-track" id="ecp-bright-track">
                <div class="erudite-picker-brightness-fill" id="ecp-bright-fill"
                     style="--swatch-hue:${`hsl(${Math.round(currentHue*360)},100%,50%)`}"></div>
                <input type="range" id="ecp-bright-slider" min="0" max="100"
                       value="${Math.round(currentVal * 100)}" aria-label="Brightness"/>
              </div>
            </div>
          </div>
          <div class="erudite-picker-actions">
            <button type="button" class="erudite-picker-btn erudite-picker-btn-cancel" id="ecp-cancel">Cancel</button>
            <button type="button" class="erudite-picker-btn erudite-picker-btn-apply" id="ecp-apply">Apply Color</button>
          </div>
        </div>
      `;

      document.body.appendChild(overlay);

      // ── Element refs ─────────────────────────────────────────────────
      const canvas    = overlay.querySelector('#ecp-canvas');
      const dot       = overlay.querySelector('#ecp-dot');
      const preview   = overlay.querySelector('#ecp-preview');
      const hexInput  = overlay.querySelector('#ecp-hex');
      const slider    = overlay.querySelector('#ecp-bright-slider');
      const brightFill= overlay.querySelector('#ecp-bright-fill');
      const brightPct = overlay.querySelector('#ecp-bright-pct');
      const swatchContainer = overlay.querySelector('#ecp-swatches');

      // ── Update helpers ───────────────────────────────────────────────

      function syncUiFromHsv() {
        const hex = currentHex();
        preview.style.background = hex;
        hexInput.value = hex.replace('#', '');
        slider.value = Math.round(currentVal * 100);
        brightPct.textContent = Math.round(currentVal * 100) + '%';
        // Update brightness track background
        const hueColor = `hsl(${Math.round(currentHue * 360)},100%,50%)`;
        brightFill.style.setProperty('--swatch-hue', hueColor);
        brightFill.style.background = `linear-gradient(to right, #000, ${hueColor})`;
        // Deselect swatches unless exact match
        swatchContainer.querySelectorAll('.erudite-picker-swatch').forEach(sw => {
          sw.classList.toggle('selected', sw.dataset.swatch.toLowerCase() === hex.toLowerCase());
        });
        // Redraw wheel & reposition dot
        drawWheel(canvas, currentHue, currentSat);
        updateDotPosition();
        selectedHex = hex;
      }

      function updateDotPosition() {
        // Place inner sat dot correctly
        const rect = canvas.getBoundingClientRect();
        const pxCx = rect.width / 2;
        const pxCy = rect.height / 2;
        const pxRingInner = (INNER_R / CANVAS_SIZE) * rect.width;
        const angle = currentHue * 2 * Math.PI - Math.PI / 2;
        const dist = currentSat * pxRingInner;
        const dotX = pxCx + dist * Math.cos(angle);
        const dotY = pxCy + dist * Math.sin(angle);
        dot.style.left = dotX + 'px';
        dot.style.top = dotY + 'px';
        // Color the dot
        const { r, g, b } = hsvToRgb(currentHue, currentSat, currentVal);
        dot.style.background = rgbToHex(r, g, b);
      }

      // Initial draw
      requestAnimationFrame(() => syncUiFromHsv());

      // ── Canvas interaction ───────────────────────────────────────────
      let dragging = null; // 'hue' | 'sat'

      function handleCanvasPick(e, isStart) {
        const { dist, hue } = polarFromEvent(canvas, e);
        const pxRingOuter = (WHEEL_R / CANVAS_SIZE) * canvas.getBoundingClientRect().width;
        const pxRingInner = (INNER_R / CANVAS_SIZE) * canvas.getBoundingClientRect().width;

        if (isStart) {
          if (dist > pxRingInner) {
            dragging = 'hue';
          } else {
            dragging = 'sat';
          }
        }

        if (dragging === 'hue') {
          currentHue = hue;
          syncUiFromHsv();
        } else if (dragging === 'sat') {
          const sat = Math.min(1, Math.max(0, dist / pxRingInner));
          // Also update hue to match angle when inside disc
          currentHue = hue;
          currentSat = sat;
          syncUiFromHsv();
        }
        e.preventDefault();
      }

      canvas.addEventListener('mousedown', e => { handleCanvasPick(e, true); });
      document.addEventListener('mousemove', e => { if (dragging) handleCanvasPick(e, false); });
      document.addEventListener('mouseup', () => { dragging = null; });

      canvas.addEventListener('touchstart', e => { handleCanvasPick(e, true); }, { passive: false });
      document.addEventListener('touchmove', e => { if (dragging) { handleCanvasPick(e, false); } }, { passive: false });
      document.addEventListener('touchend', () => { dragging = null; });

      // ── Slider ───────────────────────────────────────────────────────
      slider.addEventListener('input', () => {
        currentVal = parseInt(slider.value, 10) / 100;
        syncUiFromHsv();
      });

      // ── Hex input ────────────────────────────────────────────────────
      hexInput.addEventListener('input', () => {
        const raw = '#' + hexInput.value.replace(/[^0-9a-fA-F]/g, '');
        if (isValidHex(raw)) {
          const rgb = hexToRgb(raw);
          if (rgb) {
            const { h, s, v } = rgbToHsv(rgb.r, rgb.g, rgb.b);
            currentHue = h; currentSat = s; currentVal = v;
            syncUiFromHsv();
          }
        }
      });

      // ── Swatches ─────────────────────────────────────────────────────
      swatchContainer.addEventListener('click', e => {
        const sw = e.target.closest('[data-swatch]');
        if (!sw) return;
        const hex = sw.dataset.swatch;
        const rgb = hexToRgb(hex);
        if (!rgb) return;
        const { h, s, v } = rgbToHsv(rgb.r, rgb.g, rgb.b);
        currentHue = h; currentSat = s; currentVal = v;
        syncUiFromHsv();
      });

      // ── Close / backdrop ─────────────────────────────────────────────
      function closeAndResolve(value) {
        overlay.style.opacity = '0';
        overlay.style.transition = 'opacity 160ms';
        const card = overlay.querySelector('.erudite-picker-card');
        if (card) {
          card.style.transform = 'translateY(100%)';
          card.style.transition = 'transform 200ms cubic-bezier(0.55, 0, 0.55, 0.2)';
        }
        setTimeout(() => {
          overlay.remove();
          resolve(value);
        }, 210);
      }

      overlay.querySelector('#ecp-close').addEventListener('click', () => closeAndResolve(null));
      overlay.querySelector('#ecp-cancel').addEventListener('click', () => closeAndResolve(null));
      overlay.querySelector('#ecp-apply').addEventListener('click', () => closeAndResolve(currentHex()));

      overlay.addEventListener('click', e => {
        if (e.target === overlay) closeAndResolve(null);
      });
    });
  }

  // ── Expose ────────────────────────────────────────────────────────────────
  global.EruditeColorPicker = { open };

})(window);
