'use strict';
// Generates mobile/css/icons.css: Lucide icons drawn through CSS masks, keyed by
// the Font Awesome class names (drawn on ::before, so the element itself can
// still carry a background chip) the app already uses (fa-gear, fa-brain, ...).
// Markup such as <i class="fas fa-gear"></i> keeps working without shipping the
// Font Awesome font. Run: node scripts/build-icons.js
const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const iconDir = path.join(root, 'node_modules', 'lucide-static', 'icons');
const outFile = path.join(root, 'mobile', 'css', 'icons.css');

// Font Awesome name -> Lucide name.
const MAP = {
  'align-center': 'text-align-center', 'align-justify': 'text-align-justify', 'align-left': 'text-align-start', 'align-right': 'text-align-end',
  'arrow-down': 'arrow-down', 'arrow-down-1-9': 'arrow-down-1-0', 'arrow-down-wide-short': 'arrow-down-wide-narrow',
  'arrow-left': 'arrow-left', 'arrow-left-right': 'arrow-left-right', 'arrow-right': 'arrow-right',
  'arrow-rotate-left': 'rotate-ccw', 'arrow-up': 'arrow-up', 'arrow-up-9-1': 'arrow-up-1-0',
  'arrow-up-right-from-square': 'external-link', 'arrows-left-right': 'arrow-left-right', 'arrows-rotate': 'refresh-cw',
  atom: 'atom', ban: 'ban', bell: 'bell', bold: 'bold', book: 'book', 'book-open': 'book-open', 'box-archive': 'archive',
  brain: 'brain', bullseye: 'target', calculator: 'calculator', 'calendar-alt': 'calendar-days', 'calendar-day': 'calendar',
  'calendar-days': 'calendar-days', 'calendar-plus': 'calendar-plus', 'calendar-xmark': 'calendar-x',
  'chalkboard-user': 'presentation', 'chart-line': 'chart-line', 'chart-simple': 'chart-column',
  check: 'check', 'check-double': 'check-check', 'chevron-down': 'chevron-down', 'chevron-right': 'chevron-right',
  circle: 'circle', 'circle-check': 'circle-check', 'circle-dot': 'circle-dot', 'circle-exclamation': 'circle-alert',
  'circle-notch': 'loader-circle', 'circle-question': 'circle-question-mark', 'circle-xmark': 'circle-x',
  clipboard: 'clipboard', clock: 'clock', 'clock-rotate-left': 'history', clone: 'copy', 'cloud-arrow-down': 'cloud-download',
  code: 'code', cog: 'settings', compass: 'compass', compress: 'shrink', copy: 'copy', database: 'database', divide: 'divide',
  dna: 'dna', edit: 'pencil', 'ellipsis-h': 'ellipsis', 'ellipsis-vertical': 'ellipsis-vertical', eraser: 'eraser',
  'exchange-alt': 'arrow-left-right', 'exclamation-circle': 'circle-alert', 'exclamation-triangle': 'triangle-alert',
  expand: 'expand', 'eye-dropper': 'pipette', 'eye-slash': 'eye-off', 'file-circle-question': 'file-question-mark',
  'file-code': 'file-code', 'file-export': 'file-output', 'file-import': 'file-input', 'file-text': 'file-text',
  'file-zipper': 'file-archive', film: 'film', filter: 'list-filter', fire: 'flame', flask: 'flask-conical',
  'folder-open': 'folder-open', font: 'type', gear: 'settings', 'gauge-high': 'gauge', globe: 'globe',
  'graduation-cap': 'graduation-cap', 'grip-lines': 'grip-horizontal', 'hand-pointer': 'pointer', heading: 'heading',
  highlighter: 'highlighter', home: 'house', 'hourglass-half': 'hourglass', image: 'image', 'info-circle': 'info',
  italic: 'italic', landmark: 'landmark', language: 'languages', 'layer-group': 'layers', 'list-check': 'list-checks',
  lock: 'lock', magic: 'wand-sparkles', 'magnifying-glass': 'search', 'magnifying-glass-plus': 'zoom-in', minus: 'minus',
  microscope: 'microscope', 'mobile-screen': 'smartphone', 'mobile-screen-button': 'smartphone', monument: 'landmark',
  moon: 'moon', music: 'music', 'object-ungroup': 'square-dashed-mouse-pointer', palette: 'palette', panorama: 'image',
  paperclip: 'paperclip', pause: 'pause', pen: 'pen', play: 'play', plus: 'plus', 'quote-left': 'quote',
  'rectangle-list': 'rectangle-horizontal', redo: 'redo-2', 'right-left': 'arrow-right-left', rotate: 'refresh-cw',
  'rotate-left': 'rotate-ccw', route: 'route', running: 'footprints', save: 'save', 'screwdriver-wrench': 'wrench',
  search: 'search', 'search-plus': 'zoom-in', seedling: 'sprout', 'shield-halved': 'shield', shuffle: 'shuffle',
  sliders: 'sliders-horizontal', spinner: 'loader', square: 'square', 'square-check': 'square-check',
  'square-root-variable': 'radical', star: 'star', stop: 'square', stopwatch: 'timer', sun: 'sun', sync: 'refresh-cw',
  'table-cells-large': 'layout-grid', 'table-list': 'table', tag: 'tag', terminal: 'terminal', 'text-height': 'type',
  times: 'x', 'trash': 'trash', 'trash-can': 'trash-2', 'trash-restore': 'archive-restore', 'triangle-exclamation': 'triangle-alert',
  trophy: 'trophy', underline: 'underline', undo: 'undo-2', 'user-shield': 'shield-user', 'vector-square': 'square-dashed',
  vial: 'test-tube', 'volume-high': 'volume-2', 'volume-up': 'volume-2', 'vote-yea': 'vote',
  'wand-magic-sparkles': 'wand-sparkles', 'wifi-slash': 'wifi-off', xmark: 'x'
};
// Icons whose Font Awesome version is solid and reads better filled.
const FILLED = new Set(['play', 'pause', 'stop', 'circle', 'star-filled']);

function svgFor(name, filled) {
  const file = path.join(iconDir, `${name}.svg`);
  if (!fs.existsSync(file)) throw new Error(`Lucide icon missing: ${name}`);
  let svg = fs.readFileSync(file, 'utf8')
    .replace(/<!--[\s\S]*?-->/g, '')
    .replace(/\sclass="[^"]*"/, '')
    .replace(/\s+/g, ' ')
    .replace(/> </g, '><')
    .trim();
  if (filled) svg = svg.replace('fill="none"', 'fill="#000"');
  return svg;
}

function dataUri(svg) {
  return `url("data:image/svg+xml,${svg.replace(/"/g, "'").replace(/#/g, '%23').replace(/</g, '%3C').replace(/>/g, '%3E')}")`;
}

function build() {
  const rules = Object.entries(MAP).map(([fa, lucide]) => `.fa-${fa}{--icon:${dataUri(svgFor(lucide, FILLED.has(fa)))}}`);
  const css = `/* Generated by scripts/build-icons.js from lucide-static (ISC). Do not edit. */
.fa,.fas,.far,.fab,.fa-solid,.fa-regular{--icon:${dataUri(svgFor('circle-small', false))};display:inline-grid;place-items:center;flex:none;min-width:1em;min-height:1em;font-style:normal;line-height:1;vertical-align:-0.14em}
.fa::before,.fas::before,.far::before,.fab::before,.fa-solid::before,.fa-regular::before{content:"";display:block;width:1em;height:1em;background-color:currentColor;-webkit-mask:var(--icon) center/contain no-repeat;mask:var(--icon) center/contain no-repeat}
.fa-fw{width:1.25em}
.fa-spin{animation:icon-spin 900ms linear infinite}
@keyframes icon-spin{to{transform:rotate(360deg)}}
@media (prefers-reduced-motion:reduce){.fa-spin{animation-duration:2.4s}}
${rules.join('\n')}
`;
  fs.writeFileSync(outFile, css);
  return { count: rules.length, bytes: Buffer.byteLength(css) };
}

if (require.main === module) {
  const { count, bytes } = build();
  console.log(`icons.css: ${count} icons, ${(bytes / 1024).toFixed(1)} KB`);
}
module.exports = { build, MAP };
