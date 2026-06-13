(function (root, factory) {
  const api = factory();
  root.EruditeCore = root.EruditeCore || {};
  root.EruditeCore.cardMedia = api;
  root.EruditeMedia = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
})(typeof globalThis !== 'undefined' ? globalThis : window, function () {
  const SIDES = ['term', 'definition'];

  function createId(prefix = 'media') {
    const random = typeof crypto !== 'undefined' && crypto.randomUUID
      ? crypto.randomUUID()
      : `${Date.now()}-${Math.random().toString(36).slice(2, 10)}`;
    return `${prefix}-${random}`;
  }

  function mediaKind(mime = '', src = '') {
    const type = String(mime || '').toLowerCase();
    const url = String(src || '').toLowerCase();
    if (type.startsWith('audio/') || /\.(mp3|wav|ogg|m4a|aac)(\?|#|$)/.test(url)) return 'audio';
    if (type.startsWith('video/') || /\.(mp4|webm|mov|m4v)(\?|#|$)/.test(url)) return 'video';
    return 'image';
  }

  function normalizeMediaItem(item = {}) {
    if (!item) return null;
    const src = String(item.src || item.url || item.dataUrl || '').trim();
    if (!src) return null;
    const mime = String(item.mime || item.type || '').trim();
    const kind = ['image', 'audio', 'video'].includes(item.kind || item.mediaType)
      ? (item.kind || item.mediaType)
      : mediaKind(mime, src);
    return {
      id: item.id || createId('media'),
      kind,
      mime,
      name: String(item.name || item.fileName || kind).trim() || kind,
      src,
      created: item.created || Date.now()
    };
  }

  function normalizeSideList(value) {
    return Array.isArray(value)
      ? value.map(normalizeMediaItem).filter(Boolean)
      : [];
  }

  function normalizeCardMedia(media = {}) {
    return {
      term: normalizeSideList(media.term),
      definition: normalizeSideList(media.definition)
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
      created: value.created || Date.now()
    };
  }

  function normalizeCardBackground(background = {}, card = {}) {
    return {
      term: normalizeBackgroundSide(background.term || card.termBackgroundImage || card.termBackground),
      definition: normalizeBackgroundSide(background.definition || card.definitionBackgroundImage || card.definitionBackground)
    };
  }

  function getSideMedia(card = {}, side = 'term', options = {}) {
    const normalized = normalizeCardMedia(card.media || {});
    const list = [...(normalized[side] || [])];
    if (options.includeLegacy !== false) {
      const legacy = side === 'definition' ? card.definitionImage : card.termImage;
      if (legacy && !list.some(item => item.src === legacy)) {
        list.unshift({
          id: `${side}-legacy-image`,
          kind: 'image',
          mime: '',
          name: side === 'definition' ? 'Definition image' : 'Term image',
          src: legacy,
          legacy: true
        });
      }
    }
    return list;
  }

  function getSideBackground(card = {}, side = 'term') {
    return normalizeCardBackground(card.background || {}, card)[side] || null;
  }

  function mediaItemFromSource(src, file = {}, overrides = {}) {
    return normalizeMediaItem({
      src,
      mime: file.type || overrides.mime || '',
      name: file.name || overrides.name || '',
      kind: overrides.kind,
      ...overrides
    });
  }

  return {
    SIDES,
    createId,
    mediaKind,
    normalizeMediaItem,
    normalizeCardMedia,
    normalizeCardBackground,
    getSideMedia,
    getSideBackground,
    mediaItemFromSource
  };
});
