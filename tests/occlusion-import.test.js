'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('fs');
const path = require('path');

// The occlusion helpers live inside the mobile app bundle; extract the pure
// functions they need and evaluate them in isolation.
function loadOcclusionHelpers() {
  const source = fs.readFileSync(path.resolve(__dirname, '../mobile/js/mobile-app.js'), 'utf8');
  const names = [
    'firstPresent', 'parseCoordinateNumber', 'normalizeCoordinateUnits', 'readPixelDimension',
    'readOcclusionBox', 'resolveOcclusionDimensions'
  ];
  const bodies = names.map(name => {
    const start = source.indexOf(`  function ${name}(`);
    assert.ok(start >= 0, `missing ${name}`);
    const end = source.indexOf('\n  }\n', start);
    return source.slice(start, end + 4);
  });
  return new Function(`${bodies.join('\n')}\nreturn { resolveOcclusionDimensions };`)();
}

const { resolveOcclusionDimensions } = loadOcclusionHelpers();

test('declared size wins when it matches the real aspect ratio (scaled measurement)', () => {
  const result = resolveOcclusionDimensions({
    declaredWidth: 600,
    declaredHeight: 400,
    actual: { width: 1200, height: 800 },
    masks: [{ bboxPx: [500, 300, 80, 40] }],
    units: 'px'
  });
  assert.deepEqual(result, { imageWidth: 600, imageHeight: 400 });
});

test('real size wins when the declared size is wrong and boxes fit the real image', () => {
  const result = resolveOcclusionDimensions({
    declaredWidth: 1000,
    declaredHeight: 1000,
    actual: { width: 1400, height: 900 },
    masks: [{ bboxPx: [1200, 700, 150, 60] }],
    units: 'px'
  });
  assert.deepEqual(result, { imageWidth: 1400, imageHeight: 900 });
});

test('real size is used when the AI declared no size', () => {
  const result = resolveOcclusionDimensions({
    actual: { width: 800, height: 600 },
    masks: [{ bboxPx: [10, 10, 50, 20] }],
    units: 'px'
  });
  assert.deepEqual(result, { imageWidth: 800, imageHeight: 600 });
});

test('declared size is kept when boxes only fit the declared size', () => {
  const result = resolveOcclusionDimensions({
    declaredWidth: 2000,
    declaredHeight: 1000,
    actual: { width: 700, height: 700 },
    masks: [{ bboxPx: [1500, 800, 200, 100] }],
    units: 'px'
  });
  assert.deepEqual(result, { imageWidth: 2000, imageHeight: 1000 });
});
