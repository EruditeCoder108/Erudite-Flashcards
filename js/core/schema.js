(function (root, factory) {
  const api = factory();
  root.EruditeCore = root.EruditeCore || {};
  root.EruditeCore.schema = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
})(typeof globalThis !== 'undefined' ? globalThis : window, function () {
  const DEFAULT_SRS_SETTINGS = {
    enabled: true,
    requestRetention: 0.9,
    maxIntervalDays: 36500,
    newCardsPerDay: null,
    reviewsPerDay: null
  };

  const DEFAULT_SETTINGS = {
    theme: 'dark',
    normalStudyOrder: 'forward',
    fonts: {},
    cursor: {
      enabled: true,
      style: 'fluid'
    }
  };

  function now() {
    return Date.now();
  }

  function createId(prefix) {
    const random = typeof crypto !== 'undefined' && crypto.randomUUID
      ? crypto.randomUUID()
      : `${Date.now()}-${Math.random().toString(36).slice(2, 10)}`;
    return `${prefix}-${random}`;
  }

  function numberOrNull(value, fallback = null) {
    if (value === null || value === undefined || value === '') return fallback;
    const number = Number(value);
    return Number.isFinite(number) ? number : fallback;
  }

  function normalizeStringArray(value) {
    if (Array.isArray(value)) {
      return value.map(item => String(item).trim()).filter(Boolean);
    }
    if (typeof value === 'string') {
      return value.split(',').map(item => item.trim()).filter(Boolean);
    }
    return [];
  }

  function normalizeReviewHistory(value) {
    return Array.isArray(value)
      ? value.filter(entry => entry && typeof entry === 'object')
      : [];
  }

  function normalizeMediaItem(item = {}) {
    const src = String(item?.src || item?.url || item?.dataUrl || '').trim();
    if (!src) return null;
    const mime = String(item.mime || item.type || '').trim();
    const kind = ['image', 'audio', 'video'].includes(item.kind || item.mediaType)
      ? (item.kind || item.mediaType)
      : (mime.startsWith('audio/') ? 'audio' : mime.startsWith('video/') ? 'video' : 'image');
    return {
      id: item.id || createId('media'),
      kind,
      mime,
      name: String(item.name || item.fileName || kind).trim() || kind,
      src,
      created: item.created || now()
    };
  }

  function normalizeCardMedia(media = {}) {
    const side = value => Array.isArray(value)
      ? value.map(normalizeMediaItem).filter(Boolean)
      : [];
    return {
      term: side(media.term),
      definition: side(media.definition)
    };
  }

  function normalizeBackgroundSide(value = {}) {
    if (!value) return null;
    if (typeof value === 'string') {
      const src = value.trim();
      return src ? { src, fit: 'cover', opacity: 0.32 } : null;
    }
    const src = String(value.src || value.url || value.dataUrl || '').trim();
    if (!src) return null;
    return {
      id: value.id || createId('background'),
      src,
      mime: String(value.mime || value.type || '').trim(),
      name: String(value.name || value.fileName || 'Background').trim() || 'Background',
      fit: ['cover', 'contain'].includes(value.fit) ? value.fit : 'cover',
      opacity: Math.min(0.7, Math.max(0.08, Number(value.opacity ?? 0.32) || 0.32)),
      created: value.created || now()
    };
  }

  function normalizeCardBackground(background = {}, card = {}) {
    return {
      term: normalizeBackgroundSide(background.term || card.termBackgroundImage || card.termBackground),
      definition: normalizeBackgroundSide(background.definition || card.definitionBackgroundImage || card.definitionBackground)
    };
  }

  function normalizeSrsSettings(settings = {}) {
    const requestRetention = numberOrNull(settings.requestRetention, DEFAULT_SRS_SETTINGS.requestRetention);
    const maxIntervalDays = numberOrNull(settings.maxIntervalDays, DEFAULT_SRS_SETTINGS.maxIntervalDays);
    const dailyLimitOrNull = (value) => {
      const number = numberOrNull(value, null);
      return number === null ? null : Math.max(0, Math.round(number));
    };

    return {
      enabled: settings.enabled !== false,
      requestRetention: Math.min(0.99, Math.max(0.7, requestRetention)),
      maxIntervalDays: Math.max(1, Math.round(maxIntervalDays)),
      newCardsPerDay: dailyLimitOrNull(settings.newCardsPerDay),
      reviewsPerDay: dailyLimitOrNull(settings.reviewsPerDay)
    };
  }

  function normalizeCard(card = {}, options = {}) {
    const timestamp = options.now || now();
    return {
      ...card,
      id: card.id || createId('card'),
      term: card.term || '',
      definition: card.definition || '',
      termImage: card.termImage || '',
      definitionImage: card.definitionImage || '',
      media: normalizeCardMedia(card.media || {}),
      background: normalizeCardBackground(card.background || {}, card),
      tags: normalizeStringArray(card.tags),
      suspended: Boolean(card.suspended),
      buriedUntil: card.buriedUntil || null,
      reviewHistory: normalizeReviewHistory(card.reviewHistory),
      created: card.created || timestamp,
      lastModified: card.lastModified || timestamp
    };
  }

  function normalizeClass(classData = {}, existingClass = null, options = {}) {
    const timestamp = options.now || now();
    const color = /^#[0-9a-f]{6}$/i.test(String(classData.color || ''))
      ? classData.color
      : (existingClass?.color || '#3B82F6');
    const name = String(classData.name || existingClass?.name || 'Untitled Class').trim() || 'Untitled Class';

    return {
      ...existingClass,
      ...classData,
      id: classData.id || existingClass?.id || createId('class'),
      name,
      color,
      icon: classData.icon || existingClass?.icon || 'fa-graduation-cap',
      created: classData.created || existingClass?.created || timestamp,
      lastModified: options.preserveLastModified
        ? (classData.lastModified || existingClass?.lastModified || timestamp)
        : timestamp
    };
  }

  function normalizeSet(set = {}, existingSet = null, options = {}) {
    const timestamp = options.now || now();
    const hasClassId = Object.prototype.hasOwnProperty.call(set, 'classId');
    const cards = Array.isArray(set.cards) ? set.cards : [];

    return {
      ...existingSet,
      ...set,
      id: set.id || existingSet?.id || createId('set'),
      name: String(set.name || existingSet?.name || 'Untitled Set').trim() || 'Untitled Set',
      description: set.description || existingSet?.description || '',
      classId: hasClassId ? (set.classId || null) : (existingSet?.classId || null),
      pinned: Boolean(set.pinned ?? existingSet?.pinned),
      cards: cards.map(card => normalizeCard(card, { now: timestamp })),
      srsSettings: normalizeSrsSettings(set.srsSettings || existingSet?.srsSettings || {}),
      created: set.created || set.createdAt || existingSet?.created || timestamp,
      openedCount: set.openedCount ?? existingSet?.openedCount ?? 0,
      lastOpened: set.lastOpened ?? existingSet?.lastOpened ?? null,
      lastModified: options.preserveLastModified
        ? (set.lastModified || existingSet?.lastModified || timestamp)
        : timestamp
    };
  }

  function normalizeSettings(settings = {}) {
    const theme = ['dark', 'light', 'high-contrast', 'blue-gray'].includes(settings.theme)
      ? settings.theme
      : DEFAULT_SETTINGS.theme;
    const normalStudyOrder = ['forward', 'backward', 'random'].includes(settings.normalStudyOrder)
      ? settings.normalStudyOrder
      : DEFAULT_SETTINGS.normalStudyOrder;
    return {
      ...DEFAULT_SETTINGS,
      ...settings,
      theme,
      normalStudyOrder,
      fonts: {
        ...DEFAULT_SETTINGS.fonts,
        ...(settings.fonts || {})
      },
      cursor: {
        ...DEFAULT_SETTINGS.cursor,
        ...(settings.cursor || {})
      }
    };
  }

  function normalizeCollection(sets = [], classes = []) {
    const normalizedClasses = Array.isArray(classes)
      ? classes.map(classData => normalizeClass(classData, null, { preserveLastModified: true }))
      : [];
    const classIds = new Set(normalizedClasses.map(classData => String(classData.id)));
    const normalizedSets = Array.isArray(sets)
      ? sets.map(set => {
          const normalized = normalizeSet(set, null, { preserveLastModified: true });
          if (normalized.classId && !classIds.has(String(normalized.classId))) normalized.classId = null;
          return normalized;
        })
      : [];

    return {
      sets: normalizedSets,
      classes: normalizedClasses
    };
  }

  return {
    DEFAULT_SRS_SETTINGS,
    DEFAULT_SETTINGS,
    createId,
    numberOrNull,
    normalizeStringArray,
    normalizeReviewHistory,
    normalizeMediaItem,
    normalizeCardMedia,
    normalizeCardBackground,
    normalizeSrsSettings,
    normalizeCard,
    normalizeClass,
    normalizeSet,
    normalizeSettings,
    normalizeCollection
  };
});
