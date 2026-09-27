// Sanitiser for advanced HTML cards, shared by the app shell and the study page.
// HTML is limited to a small layout allow-list. Inline SVG is allowed for line
// diagrams (arrows, cycles, apparatus sketches), restricted to shape and text
// elements with presentational attributes: no scripts, foreignObject, links,
// <use>, <image>, SMIL animation, event handlers or external references.
(function (root, factory) {
  const api = factory();
  root.EruditeCore = root.EruditeCore || {};
  root.EruditeCore.advancedHtml = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
})(typeof globalThis !== 'undefined' ? globalThis : window, function () {
  const SVG_NS = 'http://www.w3.org/2000/svg';

  const HTML_TAGS = new Set([
    'DIV', 'SECTION', 'ARTICLE', 'HEADER', 'FOOTER', 'MAIN',
    'H1', 'H2', 'H3', 'H4', 'H5', 'H6',
    'P', 'SPAN', 'STRONG', 'B', 'EM', 'I', 'U', 'SMALL',
    'MARK', 'CODE', 'PRE', 'BLOCKQUOTE', 'BR', 'HR',
    'UL', 'OL', 'LI',
    'TABLE', 'THEAD', 'TBODY', 'TFOOT', 'TR', 'TH', 'TD',
    'IMG', 'SUP', 'SUB'
  ]);

  // Removed with their content (compared upper-case).
  const REMOVE_ENTIRELY = new Set([
    'SCRIPT', 'STYLE', 'IFRAME', 'OBJECT', 'EMBED', 'LINK', 'META', 'BASE', 'FORM', 'INPUT',
    'BUTTON', 'SELECT', 'TEXTAREA', 'CANVAS', 'VIDEO', 'AUDIO'
  ]);
  const SVG_REMOVE_ENTIRELY = new Set([
    'FOREIGNOBJECT', 'USE', 'IMAGE', 'A', 'ANIMATE', 'ANIMATEMOTION', 'ANIMATETRANSFORM', 'SET',
    'MPATH', 'FEIMAGE', 'PATTERN', 'FILTER', 'MASK', 'CLIPPATH', 'SYMBOL', 'SWITCH', 'HANDLER', 'LISTENER'
  ]);

  const SVG_TAGS = new Set([
    'svg', 'g', 'path', 'line', 'polyline', 'polygon', 'rect', 'circle', 'ellipse',
    'text', 'tspan', 'defs', 'marker'
  ]);

  // Lower-case lookup -> canonical (case-sensitive) SVG attribute name.
  const SVG_ATTRIBUTES = new Map([
    'viewBox', 'preserveAspectRatio', 'width', 'height',
    'x', 'y', 'x1', 'y1', 'x2', 'y2', 'cx', 'cy', 'r', 'rx', 'ry', 'dx', 'dy',
    'd', 'points', 'transform', 'pathLength',
    'fill', 'fill-opacity', 'fill-rule', 'stroke', 'stroke-width', 'stroke-opacity',
    'stroke-linecap', 'stroke-linejoin', 'stroke-dasharray', 'stroke-dashoffset', 'stroke-miterlimit',
    'opacity', 'font-size', 'font-weight', 'font-style', 'text-anchor', 'dominant-baseline',
    'letter-spacing', 'rotate',
    'marker-start', 'marker-mid', 'marker-end',
    'markerWidth', 'markerHeight', 'markerUnits', 'refX', 'refY', 'orient'
  ].map(name => [name.toLowerCase(), name]));

  // Attributes that may point at a marker or gradient defined in the same card.
  const SVG_URL_ATTRIBUTES = new Set(['fill', 'stroke', 'marker-start', 'marker-mid', 'marker-end']);

  const MAX_SVG_ATTRIBUTE_LENGTH = 4000;

  function sanitizeClassValue(value) {
    return String(value || '')
      .split(/\s+/)
      .map(item => item.replace(/[^\w:-]/g, ''))
      .filter(Boolean)
      .slice(0, 12)
      .join(' ');
  }

  function sanitizeIdValue(value) {
    return String(value || '').replace(/[^\w:-]/g, '').slice(0, 64);
  }

  /**
   * Returns the safe value for an SVG attribute, or null to drop it.
   * `name` is the attribute name as written; case is ignored.
   */
  function sanitizeSvgAttribute(name, value) {
    const lower = String(name || '').toLowerCase();
    if (lower === 'class') return sanitizeClassValue(value) || null;
    if (lower === 'id') return sanitizeIdValue(value) || null;
    const canonical = SVG_ATTRIBUTES.get(lower);
    if (!canonical) return null;
    const raw = String(value ?? '').trim();
    if (!raw || raw.length > MAX_SVG_ATTRIBUTE_LENGTH) return null;
    if (/url\s*\(/i.test(raw)) {
      return SVG_URL_ATTRIBUTES.has(canonical) && /^url\(\s*#[\w-]{1,64}\s*\)$/i.test(raw) ? raw : null;
    }
    // Numbers, path data, colours, keywords and transform lists only.
    if (!/^[\w\s.,#%()+\-]*$/.test(raw)) return null;
    if (/(javascript|vbscript|expression)/i.test(raw)) return null;
    return raw;
  }

  function isSvgElement(node) {
    return node.namespaceURI === SVG_NS;
  }

  function sanitizeHtmlAttribute(node, attr, safeMediaSrc) {
    const name = attr.name.toLowerCase();
    const raw = String(attr.value || '');
    if (name === 'class') return sanitizeClassValue(raw) || null;
    if (name === 'id') return sanitizeIdValue(raw) || null;
    if (node.tagName === 'IMG') {
      if (name === 'src') {
        const src = safeMediaSrc(raw);
        return src && !/^data:image\/svg/i.test(src) ? src : null;
      }
      if (name === 'alt' || name === 'title') return raw.slice(0, 160);
      if ((name === 'width' || name === 'height') && /^(\d{1,4}|[1-9]\d?%)$/.test(raw.trim())) return raw.trim();
    }
    if ((node.tagName === 'TD' || node.tagName === 'TH') && (name === 'colspan' || name === 'rowspan') && /^\d{1,2}$/.test(raw.trim())) {
      return raw.trim();
    }
    return null;
  }

  /**
   * Sanitises advanced-card HTML. Needs a DOM (`document`); `safeMediaSrc`
   * validates image sources and returns '' for anything unsafe.
   */
  function sanitizeAdvancedHtml(value, { maxLength = 30000, safeMediaSrc = () => '', doc = document } = {}) {
    const template = doc.createElement('template');
    template.innerHTML = String(value || '').slice(0, maxLength);
    const walk = doc.createTreeWalker(template.content, 1 /* NodeFilter.SHOW_ELEMENT */);
    const nodes = [];
    while (walk.nextNode()) nodes.push(walk.currentNode);
    nodes.forEach(node => {
      // Skip descendants of an element that was already removed.
      if (!template.content.contains(node)) return;
      const svg = isSvgElement(node);
      const upperName = String(node.localName || node.tagName).toUpperCase();
      if (REMOVE_ENTIRELY.has(upperName) || (svg && SVG_REMOVE_ENTIRELY.has(upperName))) {
        node.remove();
        return;
      }
      const allowed = svg ? SVG_TAGS.has(node.localName) : HTML_TAGS.has(node.tagName);
      if (!allowed) {
        node.replaceWith(...Array.from(node.childNodes));
        return;
      }
      Array.from(node.attributes).forEach(attr => {
        const name = attr.name.toLowerCase();
        if (name.startsWith('on') || name === 'style' || name === 'srcdoc' || name.endsWith('href')) {
          node.removeAttribute(attr.name);
          return;
        }
        const safe = svg ? sanitizeSvgAttribute(attr.name, attr.value) : sanitizeHtmlAttribute(node, attr, safeMediaSrc);
        if (safe === null) node.removeAttribute(attr.name);
        else if (safe !== attr.value) node.setAttribute(attr.name, safe);
      });
    });
    return template.innerHTML.trim();
  }

  return { sanitizeAdvancedHtml, sanitizeSvgAttribute, sanitizeClassValue, SVG_TAGS };
});
