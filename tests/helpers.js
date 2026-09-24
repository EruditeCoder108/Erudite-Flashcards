'use strict';
// Load the browser-global core modules into Node for unit testing.
const path = require('path');

function loadCore() {
  globalThis.window = globalThis;
  globalThis.FSRS = require('ts-fsrs');
  const root = path.resolve(__dirname, '..');
  const load = file => {
    const resolved = require.resolve(path.join(root, file));
    delete require.cache[resolved];
    return require(resolved);
  };
  load('js/core/schema.js');
  load('js/core/stats.js');
  const SRSManager = load('js/srs-manager.js');
  return { SRSManager, srsManager: globalThis.srsManager, core: globalThis.EruditeCore };
}

module.exports = { loadCore };
