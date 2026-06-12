// ─── Erudite Custom Cursor ───────────────────────────────────────────────────
// Supported styles: 'default' (system), 'fluid', 'context'
// Comet cursor removed.
// ─────────────────────────────────────────────────────────────────────────────

let cursorDot, cursorOutline;
let mouseX = 0, mouseY = 0;
let cursorX = 0, cursorY = 0;
let lastX = 0, lastY = 0;
let angle = 0;
let isCursorHidden = false;
let customCursorEnabled = false;
let currentCursorStyle = 'fluid';
let animationFrameId = null;

// Context cursor state
let orbitX = 0, orbitY = 0;
let orbitScale = 1;
let isMouseDown = false;
let isIBeamActive = false;
let stateResetTimer = null;

// ─── Device guard ─────────────────────────────────────────────────────────────
// Disable the custom cursor ONLY when the device has NO fine pointer (mouse /
// trackpad). Touch-screen laptops, Surface Pros etc. still have a fine pointer
// available, so they should keep the custom cursor.
// The old check used window.innerWidth <= 768 which broke on any small window
// or on any laptop with a built-in touchscreen (very common).
const shouldDisableCustomCursor = () => {
    if (document.documentElement.classList.contains('is-mobile-shell')) return true;
    if (window.Capacitor?.isNativePlatform?.()) return true;
    // If the browser reports a fine pointer exists, keep the cursor.
    if (window.matchMedia('(pointer: fine)').matches) return false;
    // Pure coarse-only devices (phones, tablets without mouse): disable.
    return true;
};

// ─── DOM helpers ─────────────────────────────────────────────────────────────
function removeCursorElements() {
    document.querySelectorAll('#cursor-dot, #cursor-outline').forEach(el => el.remove());
}

function applyNoCursorClass(enable) {
    // Apply cursor:none to BOTH html and body so it covers every pixel of the page,
    // including areas outside the app-container (this fixes the dual-cursor bug).
    document.documentElement.classList.toggle('custom-cursor-active', enable);
    document.body.classList.toggle('custom-cursor-enabled', enable);
    if (enable) {
        document.body.classList.add(`cursor-style-${currentCursorStyle}`);
    } else {
        document.body.classList.remove('cursor-style-fluid', 'cursor-style-context');
    }
}

// ─── Initialise cursor DOM elements ─────────────────────────────────────────
function initCursor() {
    stopCursorAnimation();
    removeCursorElements();

    if (!customCursorEnabled || currentCursorStyle === 'default') return;

    // Always create the dot
    cursorDot = document.createElement('div');
    cursorDot.id = 'cursor-dot';
    document.body.appendChild(cursorDot);

    // Context needs the orbiting outline ring
    if (currentCursorStyle === 'context') {
        cursorOutline = document.createElement('div');
        cursorOutline.id = 'cursor-outline';
        document.body.appendChild(cursorOutline);
    } else {
        cursorOutline = null;
    }

    // Seed position to avoid initial jump
    mouseX = cursorX = lastX = orbitX = window.innerWidth / 2;
    mouseY = cursorY = lastY = orbitY = window.innerHeight / 2;
    isCursorHidden = false;

    startCursorAnimation();
}

// ─── Animation loop ───────────────────────────────────────────────────────────
function startCursorAnimation() {
    if (!animationFrameId) animateCursor();
}

function stopCursorAnimation() {
    if (animationFrameId) {
        cancelAnimationFrame(animationFrameId);
        animationFrameId = null;
    }
}

function animateCursor() {
    if (!customCursorEnabled) return;

    if (currentCursorStyle === 'fluid') {
        animateFluid();
    } else if (currentCursorStyle === 'context') {
        animateContext();
    }

    animationFrameId = requestAnimationFrame(animateCursor);
}

// ─── Fluid cursor ─────────────────────────────────────────────────────────────
function animateFluid() {
    const dx = mouseX - cursorX;
    const dy = mouseY - cursorY;
    cursorX += dx * 0.5;
    cursorY += dy * 0.5;

    const speed = Math.hypot(cursorX - lastX, cursorY - lastY);
    lastX = cursorX;
    lastY = cursorY;

    if (speed > 0.1) angle = Math.atan2(dy, dx);

    const stretch = Math.min(speed * 0.06, 0.4);
    const scaleX = 1 + stretch;
    const scaleY = Math.max(0.4, 1 - stretch);

    if (!cursorDot) return;
    cursorDot.style.left = cursorX + 'px';
    cursorDot.style.top  = cursorY + 'px';

    if (document.body.classList.contains('cursor-mode-text')) {
        cursorDot.style.transform = 'translate(-50%, -50%)';
    } else if (document.body.classList.contains('cursor-mode-pointer')) {
        cursorDot.style.transform = `translate(-50%, -50%) scale(${1 + Math.min(speed * 0.02, 0.1)})`;
    } else {
        cursorDot.style.transform = `translate(-50%, -50%) rotate(${angle}rad) scaleX(${scaleX}) scaleY(${scaleY})`;
    }
}

// ─── Context-aware cursor ─────────────────────────────────────────────────────
function animateContext() {
    orbitX += (mouseX - orbitX) * 0.65;
    orbitY += (mouseY - orbitY) * 0.65;

    if (cursorDot) {
        cursorDot.style.transform = `translate(${mouseX}px, ${mouseY}px) translate(-50%, -50%)`;
    }

    if (cursorOutline) {
        const scale = orbitScale * (isMouseDown ? 0.8 : 1);
        if (isIBeamActive) {
            cursorOutline.style.transform = `translate(${orbitX}px, ${orbitY}px) translate(-50%, -50%)`;
        } else {
            cursorOutline.style.transform = `translate(${orbitX}px, ${orbitY}px) translate(-50%, -50%) scale(${scale})`;
        }
    }
}

// ─── Click ripple (fluid only) ────────────────────────────────────────────────
function createClickRipple(x, y) {
    if (currentCursorStyle !== 'fluid') return;
    const ripple = document.createElement('div');
    ripple.className = 'click-ripple';
    ripple.style.cssText = `width:50px;height:50px;left:${x}px;top:${y}px`;
    document.body.appendChild(ripple);
    setTimeout(() => ripple?.parentNode && ripple.remove(), 500);
}

// ─── Context cursor semantic states ──────────────────────────────────────────
function setCursorState(state) {
    if (currentCursorStyle !== 'context') return;
    if (stateResetTimer) clearTimeout(stateResetTimer);
    document.body.classList.remove('cursor-state-copy', 'cursor-state-paste', 'cursor-state-typing', 'cursor-state-disabled');

    let duration = 0;
    if (state === 'copy')    { document.body.classList.add('cursor-state-copy');    duration = 1000; }
    if (state === 'paste')   { document.body.classList.add('cursor-state-paste');   duration = 1000; }
    if (state === 'typing')  { document.body.classList.add('cursor-state-typing');  duration = 1500; }
    if (state === 'disabled'){ document.body.classList.add('cursor-state-disabled'); }

    if (duration > 0) stateResetTimer = setTimeout(() => setCursorState('default'), duration);
}

// ─── Public API ───────────────────────────────────────────────────────────────
/**
 * Activate or deactivate the custom cursor.
 * @param {boolean} enable
 */
function toggleCustomCursor(enable) {
    if (shouldDisableCustomCursor()) enable = false;

    customCursorEnabled = enable;
    localStorage.setItem('customCursorEnabled', enable ? 'true' : 'false');

    if (!enable || currentCursorStyle === 'default') {
        stopCursorAnimation();
        removeCursorElements();
        applyNoCursorClass(false);
        return;
    }

    applyNoCursorClass(true);
    initCursor();
}

/**
 * Switch between cursor styles.
 * @param {'default'|'fluid'|'context'} style
 */
function changeCursorStyle(style) {
    currentCursorStyle = style;
    localStorage.setItem('cursorStyle', style);

    // Remove old body classes
    document.body.classList.remove('cursor-style-fluid', 'cursor-style-context');

    if (style === 'default') {
        stopCursorAnimation();
        removeCursorElements();
        applyNoCursorClass(false);
        return;
    }

    applyNoCursorClass(customCursorEnabled);
    if (customCursorEnabled) {
        document.body.classList.add(`cursor-style-${style}`);
        initCursor();
    }
}

// ─── Initialise on DOMContentLoaded ──────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
    if (shouldDisableCustomCursor()) return;

    // Load saved prefs
    const savedEnabled = localStorage.getItem('customCursorEnabled');
    const savedStyle   = localStorage.getItem('cursorStyle') || 'fluid';

    // Map legacy 'comet' to 'fluid' so old saves don't break
    currentCursorStyle = (savedStyle === 'comet') ? 'fluid' : savedStyle;
    customCursorEnabled = savedEnabled === null ? true : savedEnabled === 'true';

    // Reflect style onto body immediately (needed for CSS scoping)
    if (customCursorEnabled && currentCursorStyle !== 'default') {
        applyNoCursorClass(true);
        initCursor();
    }

    // ── Mouse tracking ────────────────────────────────────────────────────────
    document.addEventListener('mousemove', e => {
        if (!customCursorEnabled) return;
        mouseX = e.clientX;
        mouseY = e.clientY;

        if (isCursorHidden && cursorDot) {
            cursorDot.style.opacity = '1';
            if (cursorOutline) cursorOutline.style.opacity = '1';
            isCursorHidden = false;
        }

        // ── Cursor mode detection ─────────────────────────────────────────
        document.body.classList.remove('cursor-mode-pointer', 'cursor-mode-text');
        const target = e.target;

        if (target.closest('a, button, [role="button"], [onclick], [tabindex="0"], input[type="checkbox"], input[type="radio"], select, label')) {
            document.body.classList.add('cursor-mode-pointer');
            if (currentCursorStyle === 'context') orbitScale = 1.5;
        } else {
            const style = window.getComputedStyle(target);
            const isText = style.cursor === 'text' ||
                           target.isContentEditable ||
                           target.nodeName === 'INPUT' ||
                           target.nodeName === 'TEXTAREA';
            if (isText) {
                document.body.classList.add('cursor-mode-text');
                if (currentCursorStyle === 'context') {
                    isIBeamActive = true;
                    if (cursorDot) cursorDot.style.opacity = '0';
                    if (cursorOutline) {
                        cursorOutline.style.width  = '1px';
                        cursorOutline.style.height = '28px';
                        cursorOutline.style.borderRadius = '2px';
                    }
                }
            } else {
                if (currentCursorStyle === 'context') {
                    orbitScale = 1;
                    isIBeamActive = false;
                    if (cursorDot) cursorDot.style.opacity = '1';
                    if (cursorOutline) {
                        cursorOutline.style.width  = '30px';
                        cursorOutline.style.height = '30px';
                        cursorOutline.style.borderRadius = '50%';
                    }
                }
            }
        }
    });

    document.addEventListener('mouseleave', () => {
        if (customCursorEnabled && cursorDot) {
            cursorDot.style.opacity = '0';
            if (cursorOutline) cursorOutline.style.opacity = '0';
            isCursorHidden = true;
        }
    });

    document.addEventListener('mouseenter', () => {
        if (customCursorEnabled && cursorDot && !isCursorHidden) {
            cursorDot.style.opacity = '1';
            if (cursorOutline) cursorOutline.style.opacity = '1';
        }
    });

    document.addEventListener('mousedown', e => {
        if (!customCursorEnabled) return;
        document.body.classList.add('cursor-clicking');
        isMouseDown = true;
        createClickRipple(e.clientX, e.clientY);
    });

    document.addEventListener('mouseup', () => {
        document.body.classList.remove('cursor-clicking');
        isMouseDown = false;
    });

    // Semantic state hooks for context cursor
    document.addEventListener('copy',    () => setCursorState('copy'));
    document.addEventListener('paste',   () => setCursorState('paste'));
    document.addEventListener('keydown', () => setCursorState('typing'));

    // Sync the radio buttons in settings if they exist on this page
    syncCursorRadios();
});

// ─── Radio button sync helper (called after DOM ready) ───────────────────────
function syncCursorRadios() {
    const radios = document.querySelectorAll('input[name="cursor-style"]');
    if (!radios.length) return;

    // Set initial state
    const activeValue = customCursorEnabled ? currentCursorStyle : 'default';
    radios.forEach(r => { r.checked = (r.value === activeValue); });

    // Listen for changes
    radios.forEach(r => r.addEventListener('change', () => {
        const val = r.value;
        if (val === 'default') {
            customCursorEnabled = false;
            localStorage.setItem('customCursorEnabled', 'false');
            changeCursorStyle('default');
        } else {
            customCursorEnabled = true;
            localStorage.setItem('customCursorEnabled', 'true');
            changeCursorStyle(val);
        }
    }));
}

// Expose globally so other pages (study.html etc.) can call these
window.toggleCustomCursor  = toggleCustomCursor;
window.changeCursorStyle   = changeCursorStyle;
window.syncCursorRadios    = syncCursorRadios;
