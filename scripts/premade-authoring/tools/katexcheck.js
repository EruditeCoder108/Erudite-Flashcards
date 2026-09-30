// Validates every \[..\] and \(..\) formula in every premade deck.json with the app's KaTeX (strict).
// Usage: node katexcheck.js
const fs = require('fs'), path = require('path');
const root = path.resolve(__dirname, '..', '..', '..');
const katex = require(path.join(root, 'www', 'vendor', 'katex', 'katex.min.js'));
let total = 0, bad = 0;
function walk(dir) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) walk(p);
    else if (e.name === 'deck.json') check(p);
  }
}
function check(file) {
  const deck = JSON.parse(fs.readFileSync(file, 'utf8'));
  for (const c of deck.cards) {
    if (c.noteType === 'advanced-html') continue;
    for (const v of Object.values(c)) {
      if (typeof v !== 'string') continue;
      for (const m of v.matchAll(/\\\[([\s\S]*?)\\\]|\\\(([\s\S]*?)\\\)/g)) {
        total++;
        const tex = m[1] ?? m[2];
        try { katex.renderToString(tex, { throwOnError: true, strict: 'error', displayMode: m[1] !== undefined }); }
        catch (err) { bad++; if (bad < 10) console.log(path.basename(path.dirname(file)), '|', err.message.slice(0, 80), '|', tex.slice(0, 80)); }
      }
    }
  }
}
walk(path.join(root, 'premade-cards'));
console.log(total, 'formulas,', bad, 'failed');
