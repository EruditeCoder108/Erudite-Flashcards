/**
 * Shared Erudite Flashcards settings.
 * Settings live in the local Electron store and are mirrored to localStorage for
 * compatibility with older page code.
 */

const DEFAULT_FLASHCARD_SETTINGS = {
    theme: 'dark',
    fonts: {
        content: "'Plus Jakarta Sans', sans-serif"
    }
};

const THEME_ALIASES = {
    theme1: 'dark',
    theme2: 'blue-gray',
    theme3: 'dark',
    theme4: 'dark'
};

const VALID_THEMES = new Set(['dark', 'light', 'high-contrast', 'blue-gray']);

function normalizeTheme(theme) {
    const normalized = THEME_ALIASES[theme] || theme || DEFAULT_FLASHCARD_SETTINGS.theme;
    return VALID_THEMES.has(normalized) ? normalized : DEFAULT_FLASHCARD_SETTINGS.theme;
}

function normalizeFlashcardSettings(settings = {}) {
    const normalized = {
        ...DEFAULT_FLASHCARD_SETTINGS,
        ...settings,
        theme: normalizeTheme(settings.theme || localStorage.getItem('flashcards-theme')),
        matteTexture: false,
        fonts: {
            ...DEFAULT_FLASHCARD_SETTINGS.fonts,
            ...(settings.fonts || {})
        }
    };
    delete normalized.studyCard;
    return normalized;
}

function readLocalSettings() {
    try {
        return JSON.parse(localStorage.getItem('flashcards-settings') || '{}');
    } catch (_error) {
        return {};
    }
}

async function getFlashcardSettings() {
    let storedSettings = readLocalSettings();

    if (window.flashcardStore?.getSettings) {
        try {
            storedSettings = await window.flashcardStore.getSettings();
        } catch (error) {
            console.warn('Could not read local settings store:', error);
        }
    }

    return normalizeFlashcardSettings(storedSettings || {});
}

async function saveFlashcardSettings(settings) {
    const normalized = normalizeFlashcardSettings(settings);
    localStorage.setItem('flashcards-settings', JSON.stringify(normalized));
    localStorage.setItem('flashcards-theme', normalized.theme);

    if (window.flashcardStore?.saveSettings) {
        await window.flashcardStore.saveSettings(normalized);
    }

    applySettings(normalized);
    return normalized;
}

function applySettings(settings = readLocalSettings()) {
    const normalized = normalizeFlashcardSettings(settings);
    const root = document.documentElement;

    root.setAttribute('data-theme', normalized.theme);
    root.removeAttribute('data-matte');
    root.style.removeProperty('--study-card-width');
    root.style.removeProperty('--study-card-aspect');

    window.__eruditeApplyingSettings = true;
    try {
        localStorage.setItem('flashcards-settings', JSON.stringify(normalized));
        localStorage.setItem('flashcards-theme', normalized.theme);
    } finally {
        window.__eruditeApplyingSettings = false;
    }

    root.classList.add('theme-transition');
    setTimeout(() => root.classList.remove('theme-transition'), 300);

    applyFontSettings(normalized.fonts);
    return normalized;
}

async function loadAndApplySettings(settingsOverride = null) {
    const settings = settingsOverride || await getFlashcardSettings();
    return applySettings(settings);
}

function applyTheme(theme) {
    const current = normalizeFlashcardSettings(readLocalSettings());
    current.theme = normalizeTheme(theme);
    return saveFlashcardSettings(current);
}

function applyFontSettings(fonts = DEFAULT_FLASHCARD_SETTINGS.fonts) {
    let fontStyle = document.getElementById('custom-fonts');
    if (!fontStyle) {
        fontStyle = document.createElement('style');
        fontStyle.id = 'custom-fonts';
        document.head.appendChild(fontStyle);
    }

    const defaultFont = DEFAULT_FLASHCARD_SETTINGS.fonts.content;
    const contentFontFamily = fonts.content || defaultFont;

    fontStyle.textContent = `
        body, h1, h2, h3, h4, h5, h6, p, button, input, textarea, select, .set-name,
        .card-title, .preview-card, .form-group input, .form-group textarea,
        .import-instructions, .toast, .modal-content, .header-content, .card-count {
            font-family: ${defaultFont} !important;
        }

        .study-container .flashcard .card-face .term-text,
        .study-container .flashcard .card-face .definition-text,
        .card-face .term-text,
        .card-face .definition-text {
            font-family: ${contentFontFamily} !important;
        }
    `;
}

document.addEventListener('DOMContentLoaded', async () => {
    if (window.flashcardLocalReady) await window.flashcardLocalReady;
    const settings = await getFlashcardSettings();
    applySettings(settings);
});

window.DEFAULT_FLASHCARD_SETTINGS = DEFAULT_FLASHCARD_SETTINGS;
window.normalizeFlashcardSettings = normalizeFlashcardSettings;
window.getFlashcardSettings = getFlashcardSettings;
window.saveFlashcardSettings = saveFlashcardSettings;
window.applySettings = applySettings;
window.applyTheme = applyTheme;
window.applyFontSettings = applyFontSettings;
window.loadAndApplySettings = loadAndApplySettings;
