// Cursor elements
let cursorDot, cursorOutline;
let mouseX = 0;
let mouseY = 0;
let cursorX = 0;
let cursorY = 0;
let lastX = 0;
let lastY = 0;
let angle = 0;
let isCursorHidden = false;
let customCursorEnabled = true;
let currentCursorStyle = 'fluid'; // Default style
let animationFrameId = null;

// Touch device detection - disable custom cursors on mobile
const isTouchDevice = () => {
    return (('ontouchstart' in window) ||
        (navigator.maxTouchPoints > 0) ||
        (navigator.msMaxTouchPoints > 0));
};

const isMobileDevice = () => {
    return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ||
           (window.innerWidth <= 768 && window.innerHeight <= 1024);
};

// Disable custom cursors completely on touch devices
const shouldDisableCustomCursor = () => {
    return isTouchDevice() || isMobileDevice();
};

// Context-aware cursor variables
let orbitX = 0, orbitY = 0;
let orbitScale = 1;
let isMouseDown = false;
let isIBeamActive = false;
let stateResetTimer = null;

// Comet cursor variables
let trailCount = 15;
let trails = [];

// Initialize cursor elements
function initCursor() {
    // Remove any existing cursor elements
    const existingDots = document.querySelectorAll('#cursor-dot');
    const existingOutlines = document.querySelectorAll('#cursor-outline');
    const existingTrails = document.querySelectorAll('.trail');
    
    existingDots.forEach(el => el.remove());
    existingOutlines.forEach(el => el.remove());
    existingTrails.forEach(el => el.remove());
    
    // Create new cursor elements based on style
    cursorDot = document.createElement('div');
    cursorDot.id = 'cursor-dot';
    document.body.appendChild(cursorDot);
    
    // Create outline for context-aware cursor
    if (currentCursorStyle === 'context') {
        cursorOutline = document.createElement('div');
        cursorOutline.id = 'cursor-outline';
        document.body.appendChild(cursorOutline);
    }
    
    // Create trails for comet cursor
    if (currentCursorStyle === 'comet') {
        trails = [];
        for (let i = 0; i < trailCount; i++) {
            const trail = document.createElement('div');
            trail.classList.add('trail');
            document.body.appendChild(trail);
            trails.push({ el: trail, x: 0, y: 0 });
        }
    }
    
    // Reset cursor state
    isCursorHidden = false;
    
    // Initialize cursor position to center of screen
    mouseX = window.innerWidth / 2;
    mouseY = window.innerHeight / 2;
    cursorX = mouseX;
    cursorY = mouseY;
    lastX = mouseX;
    lastY = mouseY;
    orbitX = mouseX;
    orbitY = mouseY;
    
    // Start animation if cursor is enabled
    if (customCursorEnabled) {
        startCursorAnimation();
    }
}

// Toggle cursor on/off
function toggleCustomCursor(enable) {
    // Always disable custom cursors on touch devices
    if (shouldDisableCustomCursor()) {
        customCursorEnabled = false;
        localStorage.setItem('customCursorEnabled', 'false');

        // Remove custom cursor class and hide elements
        document.body.classList.remove('custom-cursor-enabled');
        if (cursorDot) {
            cursorDot.style.display = 'none';
            if (cursorOutline) cursorOutline.style.display = 'none';
            stopCursorAnimation();
        }

        // Clean up comet cursor trails
        const trails = document.querySelectorAll('.trail');
        trails.forEach(trail => {
            trail.style.display = 'none';
            trail.style.opacity = '0';
        });

        // Disable cursor style selector
        const cursorStyleSelect = document.getElementById('cursor-style-select');
        if (cursorStyleSelect) {
            cursorStyleSelect.disabled = true;
            cursorStyleSelect.parentElement.style.opacity = '0.5';
        }

        // Also disable the toggle
        const cursorToggle = document.getElementById('custom-cursor-toggle');
        if (cursorToggle) {
            cursorToggle.checked = false;
            cursorToggle.disabled = true;
        }

        return;
    }

    customCursorEnabled = enable;
    localStorage.setItem('customCursorEnabled', enable ? 'true' : 'false');

    // Get cursor style selector to enable/disable it
    const cursorStyleSelect = document.getElementById('cursor-style-select');

    if (enable) {
        // Enable custom cursor
        document.body.classList.add('custom-cursor-enabled');
        if (cursorDot) {
            cursorDot.style.display = 'block';
            if (cursorOutline) cursorOutline.style.display = 'block';
            startCursorAnimation();
        } else {
            initCursor();
        }

        // Enable cursor style selector
        if (cursorStyleSelect) {
            cursorStyleSelect.disabled = false;
            cursorStyleSelect.parentElement.style.opacity = '1';
        }
    } else {
        // Disable custom cursor
        document.body.classList.remove('custom-cursor-enabled');

        // Hide custom cursor elements
        if (cursorDot) {
            cursorDot.style.display = 'none';
            if (cursorOutline) cursorOutline.style.display = 'none';
            stopCursorAnimation();
        }

        // Clean up comet cursor trails
        const trails = document.querySelectorAll('.trail');
        trails.forEach(trail => {
            trail.style.display = 'none';
            trail.style.opacity = '0';
        });

        // Disable cursor style selector
        if (cursorStyleSelect) {
            cursorStyleSelect.disabled = true;
            cursorStyleSelect.parentElement.style.opacity = '0.5';
        }
    }
}

// Change cursor style
function changeCursorStyle(style) {
    currentCursorStyle = style;
    localStorage.setItem('cursorStyle', style);
    
    // Update body classes
    document.body.classList.remove('cursor-style-fluid', 'cursor-style-context', 'cursor-style-comet');
    document.body.classList.add(`cursor-style-${style}`);
    
    // Reinitialize cursor with new style
    initCursor();
}

// Start cursor animation
function startCursorAnimation() {
    if (!animationFrameId) {
        animateCursor();
    }
}

// Stop cursor animation
function stopCursorAnimation() {
    if (animationFrameId) {
        cancelAnimationFrame(animationFrameId);
        animationFrameId = null;
    }
}

// Fluid cursor animation function
function animateFluidCursor() {
    // Smooth following with easing
    const dx = mouseX - cursorX;
    const dy = mouseY - cursorY;
    cursorX += dx * 0.5;
    cursorY += dy * 0.5;

    // Keep cursor within viewport bounds to prevent scrollbars
    const cursorSize = 25; // Size of fluid cursor dot
    const halfSize = cursorSize / 2;
    cursorX = Math.max(halfSize, Math.min(window.innerWidth - halfSize, cursorX));
    cursorY = Math.max(halfSize, Math.min(window.innerHeight - halfSize, cursorY));

    // Calculate follow speed for stretching effect
    const followSpeed = Math.hypot(cursorX - lastX, cursorY - lastY);
    lastX = cursorX;
    lastY = cursorY;

    // Update angle for rotation
    if (followSpeed > 0.1) {
        angle = Math.atan2(dy, dx);
    }

    // Calculate stretch based on movement speed
    const stretch = Math.min(followSpeed * 0.06, 0.4);
    const scaleX = 1 + stretch;
    const scaleY = Math.max(0.4, 1 - stretch);

    // Apply transform to cursor
    if (cursorDot) {
        cursorDot.style.left = cursorX + 'px';
        cursorDot.style.top = cursorY + 'px';
        
        // Don't apply rotation/scaling when in text mode (I-beam) or pointer mode (precise)
        if (document.body.classList.contains('cursor-mode-text')) {
            cursorDot.style.transform = 'translate(-50%, -50%)';
        } else if (document.body.classList.contains('cursor-mode-pointer')) {
            // In pointer mode, use minimal animation for precision
            const preciseScale = Math.min(followSpeed * 0.02, 0.1);
            cursorDot.style.transform = `translate(-50%, -50%) scale(${1 + preciseScale})`;
        } else {
            cursorDot.style.transform = `translate(-50%, -50%) rotate(${angle}rad) scaleX(${scaleX}) scaleY(${scaleY})`;
        }
    }
}

// Context-aware cursor animation function
function animateContextCursor() {
    orbitX += (mouseX - orbitX) * 0.65;
    orbitY += (mouseY - orbitY) * 0.65;

    // Keep cursor elements within viewport bounds to prevent scrollbars
    const dotSize = 8; // Size of context cursor dot
    const outlineSize = 30; // Size of context cursor outline
    const halfDotSize = dotSize / 2;
    const halfOutlineSize = outlineSize / 2;

    const clampedMouseX = Math.max(halfDotSize, Math.min(window.innerWidth - halfDotSize, mouseX));
    const clampedMouseY = Math.max(halfDotSize, Math.min(window.innerHeight - halfDotSize, mouseY));
    const clampedOrbitX = Math.max(halfOutlineSize, Math.min(window.innerWidth - halfOutlineSize, orbitX));
    const clampedOrbitY = Math.max(halfOutlineSize, Math.min(window.innerHeight - halfOutlineSize, orbitY));

    if (cursorDot) {
        cursorDot.style.transform = `translate(${clampedMouseX}px, ${clampedMouseY}px) translate(-50%, -50%)`;
    }

    if (cursorOutline) {
        const currentClickScale = isMouseDown ? 0.8 : 1;
        const totalScale = orbitScale * currentClickScale;

        if (isIBeamActive) {
            cursorOutline.style.transform = `translate(${clampedOrbitX}px, ${clampedOrbitY}px) translate(-50%, -50%)`;
        } else {
            cursorOutline.style.transform = `translate(${clampedOrbitX}px, ${clampedOrbitY}px) translate(-50%, -50%) scale(${totalScale})`;
        }
    }
}

// Comet cursor animation function
function animateCometCursor() {
    // Keep cursor elements within viewport bounds to prevent scrollbars
    const dotSize = 20; // Size of comet cursor dot
    const trailSize = 8; // Size of comet trail elements
    const halfDotSize = dotSize / 2;
    const halfTrailSize = trailSize / 2;

    const clampedMouseX = Math.max(halfDotSize, Math.min(window.innerWidth - halfDotSize, mouseX));
    const clampedMouseY = Math.max(halfDotSize, Math.min(window.innerHeight - halfDotSize, mouseY));

    if (cursorDot) {
        cursorDot.style.left = `${clampedMouseX - cursorDot.offsetWidth / 2}px`;
        cursorDot.style.top = `${clampedMouseY - cursorDot.offsetHeight / 2}px`;
    }

    let prevX = clampedMouseX, prevY = clampedMouseY;
    trails.forEach((t, index) => {
        const currentX = t.x, currentY = t.y;
        t.x += (prevX - currentX) * 0.4;
        t.y += (prevY - currentY) * 0.4;

        // Keep trail elements within viewport bounds
        const clampedTrailX = Math.max(halfTrailSize, Math.min(window.innerWidth - halfTrailSize, t.x));
        const clampedTrailY = Math.max(halfTrailSize, Math.min(window.innerHeight - halfTrailSize, t.y));

        t.el.style.left = `${clampedTrailX - t.el.offsetWidth / 2}px`;
        t.el.style.top = `${clampedTrailY - t.el.offsetHeight / 2}px`;
        const opacity = 1 - (index / trailCount) * 0.8;
        const scale = 1 - (index / trailCount) * 0.5;
        t.el.style.opacity = opacity;
        t.el.style.transform = `scale(${scale})`;
        prevX = clampedTrailX; prevY = clampedTrailY;
    });
}

// Main cursor animation function
function animateCursor() {
    if (!customCursorEnabled) return;
    
    switch (currentCursorStyle) {
        case 'fluid':
            animateFluidCursor();
            break;
        case 'context':
            animateContextCursor();
            break;
        case 'comet':
            animateCometCursor();
            break;
    }
    
    animationFrameId = requestAnimationFrame(animateCursor);
}

// Create click ripple effect (for fluid cursor)
function createClickRipple(x, y) {
    if (currentCursorStyle !== 'fluid') return;
    
    const ripple = document.createElement('div');
    ripple.className = 'click-ripple';
    ripple.style.width = '50px';
    ripple.style.height = '50px';
    ripple.style.left = x + 'px';
    ripple.style.top = y + 'px';
    document.body.appendChild(ripple);
    
    // Remove ripple after animation completes
    setTimeout(() => {
        if (ripple && ripple.parentNode) {
            ripple.remove();
        }
    }, 500);
}

// Context-aware cursor state management
function setCursorState(state) {
    if (currentCursorStyle !== 'context') return;
    
    if (stateResetTimer) clearTimeout(stateResetTimer);
    let duration = 0;
    
    switch(state) {
        case 'copy': 
            document.body.classList.add('cursor-state-copy');
            duration = 1000; 
            break;
        case 'paste': 
            document.body.classList.add('cursor-state-paste');
            duration = 1000; 
            break;
        case 'typing': 
            document.body.classList.add('cursor-state-typing');
            duration = 1500; 
            break;
        case 'disabled': 
            document.body.classList.add('cursor-state-disabled');
            break;
        default: 
            document.body.classList.remove('cursor-state-copy', 'cursor-state-paste', 'cursor-state-typing', 'cursor-state-disabled');
            break;
    }
    
    if (duration > 0) {
        stateResetTimer = setTimeout(() => setCursorState('default'), duration);
    }
}

// Initialize cursor when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Load cursor preferences from localStorage
    const savedCursorPref = localStorage.getItem('customCursorEnabled');
    const savedCursorStyle = localStorage.getItem('cursorStyle');

    customCursorEnabled = savedCursorPref === null ? true : savedCursorPref === 'true';
    currentCursorStyle = savedCursorStyle || 'fluid';

    // Skip cursor initialization on touch devices
    if (shouldDisableCustomCursor()) {
        customCursorEnabled = false;
        // Don't initialize cursor at all on touch devices

        // Disable cursor controls in settings
        const cursorToggle = document.getElementById('custom-cursor-toggle');
        const cursorStyleSelect = document.getElementById('cursor-style-select');

        if (cursorToggle) {
            cursorToggle.checked = false;
            cursorToggle.disabled = true;
        }

        if (cursorStyleSelect) {
            cursorStyleSelect.disabled = true;
            cursorStyleSelect.parentElement.style.opacity = '0.5';
        }

        return; // Exit early, don't set up cursor event listeners
    }

    // Initialize cursor for non-touch devices
    initCursor();

    // Set initial state based on preference
    if (customCursorEnabled) {
        document.body.classList.add('custom-cursor-enabled');
        document.body.classList.add(`cursor-style-${currentCursorStyle}`);
    } else {
        document.body.classList.remove('custom-cursor-enabled');
    }
    toggleCustomCursor(customCursorEnabled);
    
    // Update the toggle in settings if it exists
    const cursorToggle = document.getElementById('custom-cursor-toggle');
    if (cursorToggle) {
        cursorToggle.checked = customCursorEnabled;
        cursorToggle.addEventListener('change', (e) => {
            toggleCustomCursor(e.target.checked);
        });
    }
    
    // Update cursor style selector if it exists
    const cursorStyleSelect = document.getElementById('cursor-style-select');
    if (cursorStyleSelect) {
        cursorStyleSelect.value = currentCursorStyle;
        cursorStyleSelect.addEventListener('change', (e) => {
            changeCursorStyle(e.target.value);
        });
        
        // Set initial disabled state if custom cursor is off
        if (!customCursorEnabled) {
            cursorStyleSelect.disabled = true;
            cursorStyleSelect.parentElement.style.opacity = '0.5';
        }
    }

    // Simplified modal cursor handling - cursor stays visible but modals handle their own cursor
    // This ensures cursor appears properly over all modals without complex hide/show logic

    // Update cursor position
    document.addEventListener('mousemove', (e) => {
        if (!customCursorEnabled) return;
        
        mouseX = e.clientX;
        mouseY = e.clientY;
        
        // Show cursor if it was hidden
        if (isCursorHidden && cursorDot) {
            cursorDot.style.opacity = '1';
            if (cursorOutline) cursorOutline.style.opacity = '1';
            isCursorHidden = false;
        }
    });

    // Hide cursor when leaving window
    document.addEventListener('mouseleave', () => {
        if (customCursorEnabled && cursorDot) {
            cursorDot.style.opacity = '0';
            if (cursorOutline) cursorOutline.style.opacity = '0';
            isCursorHidden = true;
        }
    });

    // Show cursor when entering window
    document.addEventListener('mouseenter', () => {
        if (customCursorEnabled && cursorDot && !isCursorHidden) {
            cursorDot.style.opacity = '1';
            if (cursorOutline) cursorOutline.style.opacity = '1';
        }
    });

    // Click effect with ripple
    document.addEventListener('mousedown', (e) => {
        if (customCursorEnabled) {
            document.body.classList.add('cursor-clicking');
            isMouseDown = true;
            createClickRipple(e.clientX, e.clientY);
        }
    });

    document.addEventListener('mouseup', () => {
        document.body.classList.remove('cursor-clicking');
        isMouseDown = false;
    });

    // Update cursor mode based on hovered elements
    document.addEventListener('mousemove', (e) => {
        const target = e.target;
        
        // Reset all cursor modes
        document.body.classList.remove('cursor-mode-pointer', 'cursor-mode-text');
        
        // Check if we're hovering over a clickable element or precise UI element
        if (target.closest('a, button, [role="button"], [onclick], [tabindex="0"], input[type="range"], input[type="slider"], .slider, .range, .clean-slider, .settings-slider, .compact-slider, .toggle-slider, .slider-container, .slider-with-value, [data-slider], [data-range]')) {
            document.body.classList.add('cursor-mode-pointer');
            
            // Context cursor hover effects
            if (currentCursorStyle === 'context') {
                orbitScale = 1.5;
            }
        } 
        // Check if we're hovering over text
        else if (target.closest('p, h1, h2, h3, h4, h5, h6, span, div, label, input[type="text"], textarea, [contenteditable]')) {
            const style = window.getComputedStyle(target);
            const isTextElement = style.cursor === 'text' || 
                                target.isContentEditable ||
                                target.nodeName === 'INPUT' || 
                                target.nodeName === 'TEXTAREA';
            
            if (isTextElement) {
                document.body.classList.add('cursor-mode-text');
                
                // Context cursor text mode
                if (currentCursorStyle === 'context') {
                    isIBeamActive = true;
                    if (cursorDot) cursorDot.style.opacity = '0';
                    if (cursorOutline) {
                        cursorOutline.style.width = '1px';
                        cursorOutline.style.height = '28px';
                        cursorOutline.style.borderRadius = '2px';
                    }
                }
                // Fluid cursor text mode - I-beam transformation is handled by CSS
            }
        } else {
            // Reset context cursor states
            if (currentCursorStyle === 'context') {
                orbitScale = 1;
                isIBeamActive = false;
                if (cursorDot) cursorDot.style.opacity = '1';
                if (cursorOutline) {
                    cursorOutline.style.width = '30px';
                    cursorOutline.style.height = '30px';
                    cursorOutline.style.borderRadius = '50%';
                }
            }
            // Fluid cursor reset is handled by CSS class removal
        }
    });

    // Context cursor event listeners
    document.addEventListener('copy', () => setCursorState('copy'));
    document.addEventListener('paste', () => setCursorState('paste'));
    document.addEventListener('keydown', () => setCursorState('typing'));

    // Handle window resize to update cursor bounds
    window.addEventListener('resize', () => {
        // Ensure cursor stays within new viewport bounds after resize
        if (customCursorEnabled && cursorDot) {
            const cursorSize = currentCursorStyle === 'fluid' ? 25 :
                              currentCursorStyle === 'comet' ? 20 : 8;
            const halfSize = cursorSize / 2;

            // Clamp current cursor position to new viewport
            mouseX = Math.max(halfSize, Math.min(window.innerWidth - halfSize, mouseX));
            mouseY = Math.max(halfSize, Math.min(window.innerHeight - halfSize, mouseY));
            cursorX = Math.max(halfSize, Math.min(window.innerWidth - halfSize, cursorX));
            cursorY = Math.max(halfSize, Math.min(window.innerHeight - halfSize, cursorY));
        }
    });

    // Handle touch devices
    document.addEventListener('touchstart', () => {
        if (cursorDot) {
            cursorDot.style.opacity = '0';
            if (cursorOutline) cursorOutline.style.opacity = '0';
        }
    });

    // Re-enable cursor after touch end
    document.addEventListener('touchend', () => {
        if (cursorDot) {
            cursorDot.style.opacity = '1';
            if (cursorOutline) cursorOutline.style.opacity = '1';
        }
    });
});
