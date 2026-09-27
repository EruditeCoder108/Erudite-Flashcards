'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const { sanitizeSvgAttribute, SVG_TAGS } = require('../js/core/advanced-html.js');

test('SVG allow-list holds only shape and text elements', () => {
  for (const tag of ['svg', 'g', 'path', 'line', 'polyline', 'polygon', 'rect', 'circle', 'ellipse', 'text', 'tspan', 'defs', 'marker']) {
    assert.ok(SVG_TAGS.has(tag), tag);
  }
  for (const tag of ['script', 'foreignObject', 'use', 'image', 'a', 'animate', 'set', 'style']) {
    assert.ok(!SVG_TAGS.has(tag), tag);
  }
});

test('presentational attributes pass through', () => {
  assert.equal(sanitizeSvgAttribute('viewBox', '0 0 340 200'), '0 0 340 200');
  assert.equal(sanitizeSvgAttribute('viewbox', '0 0 10 10'), '0 0 10 10');
  assert.equal(sanitizeSvgAttribute('d', 'M10 20 L30 40 Z'), 'M10 20 L30 40 Z');
  assert.equal(sanitizeSvgAttribute('points', '0,0 10,5 0,10'), '0,0 10,5 0,10');
  assert.equal(sanitizeSvgAttribute('transform', 'rotate(-45 10 10) translate(2,3)'), 'rotate(-45 10 10) translate(2,3)');
  assert.equal(sanitizeSvgAttribute('fill', '#3457f0'), '#3457f0');
  assert.equal(sanitizeSvgAttribute('stroke', 'currentColor'), 'currentColor');
  assert.equal(sanitizeSvgAttribute('stroke-dasharray', '4 2'), '4 2');
  assert.equal(sanitizeSvgAttribute('class', 'arrow  step-1 bad!"'), 'arrow step-1 bad');
});

test('marker and paint references only point inside the card', () => {
  assert.equal(sanitizeSvgAttribute('marker-end', 'url(#arrowhead)'), 'url(#arrowhead)');
  assert.equal(sanitizeSvgAttribute('fill', 'url(#grad)'), 'url(#grad)');
  assert.equal(sanitizeSvgAttribute('marker-end', 'url(https://evil.test/x.svg#a)'), null);
  assert.equal(sanitizeSvgAttribute('fill', 'url(data:image/svg+xml,x)'), null);
  assert.equal(sanitizeSvgAttribute('d', 'url(#a)'), null);
});

test('scripts, events, links and unknown attributes are dropped', () => {
  assert.equal(sanitizeSvgAttribute('onload', 'alert(1)'), null);
  assert.equal(sanitizeSvgAttribute('href', '#a'), null);
  assert.equal(sanitizeSvgAttribute('xlink:href', 'javascript:alert(1)'), null);
  assert.equal(sanitizeSvgAttribute('style', 'fill:red'), null);
  assert.equal(sanitizeSvgAttribute('values', '0;1'), null);
  assert.equal(sanitizeSvgAttribute('fill', 'javascript(1)'), null);
  assert.equal(sanitizeSvgAttribute('fill', 'red;background:url(x)'), null);
  assert.equal(sanitizeSvgAttribute('fill', '<b>'), null);
  assert.equal(sanitizeSvgAttribute('d', 'M0 0'.repeat(2000)), null);
});
