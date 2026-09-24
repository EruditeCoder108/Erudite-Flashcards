'use strict';
// Browser smoke test for the mobile web build (www/). Run `npm run build:mobile`
// first; this script serves www/ with a Capacitor shim and drives it in Chromium.
//   node tests/e2e/smoke.js
const fs = require('fs');
const http = require('http');
const path = require('path');

const { chromium } = require(process.env.PLAYWRIGHT_CORE || 'playwright-core');

const root = path.resolve(__dirname, '../../www');
const MIME = {
  '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.wasm': 'application/wasm',
  '.png': 'image/png', '.webp': 'image/webp', '.mp3': 'audio/mpeg', '.woff2': 'font/woff2',
  '.woff': 'font/woff', '.ttf': 'font/ttf', '.json': 'application/json', '.svg': 'image/svg+xml'
};

function serve() {
  const server = http.createServer((req, res) => {
    const url = new URL(req.url, 'http://localhost');
    // Serve the shim in place of the native bridge without writing it into www/,
    // which `cap sync` would otherwise copy into the Android app.
    const file = url.pathname === '/capacitor.js'
      ? path.join(__dirname, 'capacitor-shim.js')
      : path.join(root, decodeURIComponent(url.pathname === '/' ? '/index.html' : url.pathname));
    if ((!file.startsWith(root) && !file.endsWith('capacitor-shim.js')) || !fs.existsSync(file)) {
      res.writeHead(404);
      res.end();
      return;
    }
    res.writeHead(200, { 'Content-Type': MIME[path.extname(file)] || 'application/octet-stream' });
    fs.createReadStream(file).pipe(res);
  });
  return new Promise(resolve => server.listen(0, () => resolve(server)));
}

function deck(id, count) {
  return {
    id,
    name: `Deck ${id}`,
    cards: Array.from({ length: count }, (_, index) => ({
      id: `${id}-card-${index}`,
      term: `Question ${index + 1} of ${id}`,
      definition: `Answer ${index + 1}`
    }))
  };
}

async function main() {
  const server = await serve();
  const base = `http://localhost:${server.address().port}`;
  const browser = await chromium.launch({ executablePath: process.env.CHROMIUM || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const context = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, hasTouch: true });
  const errors = [];
  const results = [];
  const check = (name, ok, detail = '') => {
    results.push({ name, ok, detail });
    console.log(`${ok ? 'PASS' : 'FAIL'} ${name}${detail ? ` - ${detail}` : ''}`);
  };

  try {
    await run(context, base, check, errors);
  } finally {
    await browser.close();
    server.close();
  }
  process.exitCode = results.every(item => item.ok) ? 0 : 1;
}

async function run(context, base, check, errors) {
  const page = await context.newPage();
  page.on('pageerror', error => errors.push(`pageerror: ${error.message}`));
  page.on('console', message => {
    if (message.type() === 'error') errors.push(`console: ${message.text()}`);
  });

  await page.addInitScript(() => {
    localStorage.setItem('erudite-mobile-onboarding-complete-v2', 'true');
    localStorage.setItem('srsModeEnabled', 'true');
  });
  await page.goto(`${base}/index.html`);
  await page.waitForFunction(() => document.body.classList.contains('app-ready'), null, { timeout: 20000 });

  await page.evaluate(async decks => {
    for (const item of decks) await window.flashcardStore.saveSet(item);
    await window.flashcardStore.flush?.();
  }, [deck('alpha', 60), deck('beta', 8)]);
  await page.reload();
  await page.waitForFunction(() => document.body.classList.contains('app-ready'), null, { timeout: 20000 });
  await page.waitForTimeout(1500);

  const heroLabel = await page.locator('#today-hero .primary-action').innerText();
  // alpha is capped at the default 20 new cards, beta has 8.
  check('new-card default caps due count', /Review 28 Left/.test(heroLabel), heroLabel.trim());

  if (process.env.SCREENSHOTS) await page.screenshot({ path: path.join(process.env.SCREENSHOTS, 'today.png') });

  await page.goto(`${base}/mobile/study.html?setId=alpha&srs=true&from=today`);
  await page.waitForSelector('#card-stage .study-card.slot-active', { timeout: 20000 });
  await page.waitForTimeout(600);
  const total = await page.locator('#progress-total').innerText();
  check('study queue respects limit', total.trim() === '20', `total=${total}`);

  await page.locator('#card-stage .study-card.slot-active').click();
  await page.waitForSelector('#rating-dock:not(.hidden)', { timeout: 5000 });
  const goodLabel = await page.locator('#interval-good').innerText();
  check('rating intervals shown', goodLabel.trim().length > 0, `good=${goodLabel}`);
  await page.locator('.rating-button.good').click();
  await page.waitForTimeout(700);
  await page.locator('#card-stage .study-card.slot-active').click();
  await page.waitForSelector('#rating-dock:not(.hidden)', { timeout: 5000 });
  await page.locator('.rating-button.easy').click();
  await page.waitForTimeout(700);

  const undo = page.locator('#srs-undo-btn');
  if (await undo.count()) {
    const beforeUndo = await page.locator('#card-stage .study-card.slot-active .card-face.front').innerText();
    await undo.click({ force: true });
    await page.waitForTimeout(500);
    const afterUndo = await page.locator('#card-stage .study-card.slot-active .card-face.front').innerText();
    check('undo restores previous card', beforeUndo !== afterUndo && /Question 2 of alpha/.test(afterUndo), afterUndo.replace(/\s+/g, ' ').slice(0, 60));
  }

  if (process.env.SCREENSHOTS) await page.screenshot({ path: path.join(process.env.SCREENSHOTS, 'study.png') });

  // Finish a whole deck in review-due mode: the completion screen should offer the
  // other deck that still has due cards.
  await page.goto(`${base}/mobile/study.html?setId=beta&srs=true&reviewDue=true&from=today`);
  await page.waitForSelector('#card-stage .study-card.slot-active', { timeout: 20000 });
  await page.waitForTimeout(600);
  for (let index = 0; index < 8; index += 1) {
    await page.locator('#card-stage .study-card.slot-active').click();
    await page.waitForSelector('#rating-dock:not(.hidden)', { timeout: 5000 });
    await page.locator('.rating-button.easy').click();
    await page.waitForTimeout(450);
  }
  await page.waitForSelector('#completion-modal:not(.hidden)', { timeout: 5000 });
  const continueLabel = await page.locator('#continue-button').innerText();
  check('completion offers next due deck', /Continue Review/.test(continueLabel), continueLabel.trim());

  check('no page errors', errors.length === 0, errors.slice(0, 5).join(' | '));
}

main().catch(error => {
  console.error(error);
  process.exitCode = 1;
});
