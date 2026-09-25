'use strict';
// Play Store image generator.
//   npm run store:images
// Builds www/, seeds a mock study library, captures real app screens at 3x,
// and frames each one with a headline at 1080 x 1920. Also renders the
// 1024 x 500 feature graphic. Output: play-store/assets/2026/.
const fs = require('fs');
const http = require('http');
const path = require('path');
const { chromium } = require(process.env.PLAYWRIGHT_CORE || 'playwright-core');

const repo = path.resolve(__dirname, '../..');
const www = path.join(repo, 'www');
const outDir = path.join(repo, 'play-store', 'assets', '2026');
const rawDir = path.join(__dirname, '.raw');
const APP_NAME = process.env.APP_NAME || 'Erudite Flashcards';

const MIME = {
  '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.wasm': 'application/wasm',
  '.png': 'image/png', '.mp3': 'audio/mpeg', '.woff2': 'font/woff2', '.json': 'application/json', '.svg': 'image/svg+xml'
};

// Order matches the Play listing. Headlines stay short enough for two lines.
const SHOTS = [
  { id: '01-today', eyebrow: 'Daily goal', title: 'Know exactly what to study today', copy: 'Your goal ring fills as you review.' },
  { id: '02-swipe', eyebrow: 'Spaced repetition', title: 'Swipe to rate. It schedules the rest.', copy: 'FSRS brings each card back just before you forget it.' },
  { id: '03-library', eyebrow: 'Your library', title: 'Every chapter in one place', copy: 'Decks and classes for NEET, JEE, boards, and more.' },
  { id: '04-occlusion', eyebrow: 'Image occlusion', title: 'Label diagrams from memory', copy: 'One figure becomes a card for every label.', shift: 150 },
  { id: '05-insights', eyebrow: 'Insights', title: 'Watch your memory get stronger', copy: 'Retention, streaks, and your upcoming workload.' },
  { id: '06-ai', eyebrow: 'Create faster', title: 'Turn any PDF into flashcards', copy: 'Build a precise prompt for your AI, then import in one tap.' },
  { id: '07-complete', eyebrow: 'Every session', title: 'Finish with a clear picture', copy: 'See what you remembered and when cards come back.' },
  { id: '08-paper', eyebrow: 'Comfortable', title: 'Easy on the eyes', copy: 'Dark, light, and a paper texture for long sessions.', light: true }
];

// In-memory file store for the Capacitor shim. The seeded library is larger
// than the ~5 MB localStorage limit the smoke tests use.
const fileStore = new Map();

function handleStore(req, res, url) {
  const key = url.searchParams.get('key');
  if (req.method === 'GET' && url.searchParams.has('list')) {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify([...fileStore.keys()]));
    return;
  }
  if (req.method === 'GET') {
    const found = fileStore.has(key);
    res.writeHead(found ? 200 : 204, { 'Content-Type': 'text/plain' });
    res.end(found ? fileStore.get(key) : '');
    return;
  }
  let body = '';
  req.setEncoding('utf8');
  req.on('data', chunk => { body += chunk; });
  req.on('end', () => {
    if (req.method === 'DELETE') fileStore.delete(key);
    else fileStore.set(key, body);
    res.writeHead(204);
    res.end();
  });
}

// Runs in the page before the shim: a synchronous Storage-like object backed by
// the generator's server.
function installShimStorage() {
  const call = (method, query, body) => {
    const request = new XMLHttpRequest();
    request.open(method, `/__store?${query}`, false);
    request.send(body ?? null);
    return request;
  };
  window.__eruditeShimStorage = {
    getItem(key) {
      const response = call('GET', `key=${encodeURIComponent(key)}`);
      return response.status === 200 ? response.responseText : null;
    },
    setItem(key, value) {
      call('POST', `key=${encodeURIComponent(key)}`, String(value));
    },
    removeItem(key) {
      call('DELETE', `key=${encodeURIComponent(key)}`);
    },
    keys() {
      return JSON.parse(call('GET', 'list=1').responseText || '[]');
    }
  };
}

function serve() {
  const server = http.createServer((req, res) => {
    const url = new URL(req.url, 'http://localhost');
    if (url.pathname === '/__store') {
      handleStore(req, res, url);
      return;
    }
    let file;
    if (url.pathname === '/capacitor.js') file = path.join(repo, 'tests', 'e2e', 'capacitor-shim.js');
    else if (url.pathname.startsWith('/generator/')) file = path.join(__dirname, url.pathname.slice('/generator/'.length));
    else file = path.join(www, decodeURIComponent(url.pathname === '/' ? '/index.html' : url.pathname));
    if (!fs.existsSync(file) || fs.statSync(file).isDirectory()) {
      res.writeHead(404);
      res.end();
      return;
    }
    res.writeHead(200, { 'Content-Type': MIME[path.extname(file)] || 'application/octet-stream' });
    fs.createReadStream(file).pipe(res);
  });
  return new Promise(resolve => server.listen(0, () => resolve(server)));
}

async function ready(page) {
  await page.waitForFunction(() => document.body.classList.contains('app-ready'), null, { timeout: 30000 });
}

// ONLY=04,08 re-captures just those screens (seeding still runs).
const only = new Set(String(process.env.ONLY || '').split(',').filter(Boolean));
const want = id => !only.size || only.has(id.slice(0, 2));

async function capture(page, id) {
  if (!want(id)) return;
  await page.screenshot({ path: path.join(rawDir, `${id}.png`) });
}

async function captureApp(browser, base) {
  const context = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 3, hasTouch: false });
  const page = await context.newPage();
  page.on('pageerror', error => console.warn('pageerror:', error.message));
  await page.addInitScript(installShimStorage);
  await page.addInitScript(() => {
    localStorage.setItem('erudite-mobile-onboarding-complete-v2', 'true');
    localStorage.setItem('erudite_creator_tour_completed', 'skipped');
    localStorage.setItem('srsModeEnabled', 'true');
  });

  await page.goto(`${base}/index.html`);
  await ready(page);
  await page.addScriptTag({ url: `${base}/generator/seed.js` });
  await page.evaluate(() => window.EruditeStoreSeed.seedStoreData());
  await page.reload();
  await ready(page);
  await page.waitForTimeout(2600);
  await capture(page, '01-today');

  await page.evaluate(() => document.getElementById('analytics-dashboard')?.scrollIntoView({ block: 'start' }));
  await page.evaluate(() => window.scrollBy(0, -70));
  await page.waitForTimeout(700);
  await capture(page, '05-insights');

  await page.evaluate(() => window.scrollTo(0, 0));
  await page.locator('.tab-button[data-tab="library"]').click();
  await page.waitForTimeout(900);
  await capture(page, '03-library');

  await page.locator('.tab-button[data-tab="create"]').click();
  await page.waitForTimeout(500);
  await page.locator('#header-creator-ai-btn').click();
  await page.waitForTimeout(900);
  await capture(page, '06-ai');

  await page.addScriptTag({ url: `${base}/generator/seed.js` });
  await page.evaluate(async () => {
    await window.EruditeStoreSeed.seedShowcaseStudy();
    await window.EruditeStoreSeed.seedOcclusion();
  });

  await page.goto(`${base}/mobile/study.html?setId=showcase&srs=true&from=today`);
  await page.waitForSelector('#card-stage .study-card.slot-active', { timeout: 30000 });
  await page.waitForTimeout(700);
  await page.locator('#reveal-button').click();
  await page.waitForTimeout(900);
  const box = await page.locator('#card-stage .study-card.slot-active').boundingBox();
  const x = box.x + box.width / 2;
  const y = box.y + box.height * 0.4;
  await page.mouse.move(x, y);
  await page.mouse.down();
  for (let step = 1; step <= 10; step += 1) {
    await page.mouse.move(x + step * 5.5, y + step * 1);
    await page.waitForTimeout(16);
  }
  await page.waitForTimeout(160);
  await capture(page, '02-swipe');
  await page.mouse.move(x, y);
  await page.mouse.up();
  await page.waitForTimeout(700);

  for (let index = 0; index < 6; index += 1) {
    if (await page.locator('#completion-modal:not(.hidden)').count()) break;
    if (!(await page.locator('#rating-dock:not(.hidden)').count())) {
      await page.locator('#reveal-button').click();
      await page.waitForTimeout(450);
    }
    await page.locator('.rating-button.easy').click();
    await page.waitForTimeout(500);
  }
  await page.waitForSelector('#completion-modal:not(.hidden)', { timeout: 10000 }).catch(() => {});
  await page.waitForTimeout(760);
  await capture(page, '07-complete');

  await page.goto(`${base}/mobile/study.html?setId=cell-diagram&srs=false&from=library`);
  await page.waitForSelector('#card-stage .study-card.slot-active .occlusion-mask-layer.is-positioned', { timeout: 30000 });
  await page.waitForTimeout(900);
  await capture(page, '04-occlusion');
  if (process.env.DEBUG_STORE) {
    console.log(await page.evaluate(() => {
      const wrap = document.querySelector('#card-stage .study-card.slot-active .card-face.front .occlusion-study-canvas');
      const image = wrap.querySelector('img');
      const a = wrap.getBoundingClientRect();
      const b = image.getBoundingClientRect();
      const style = getComputedStyle(wrap);
      return JSON.stringify({ wrap: [a.top, a.height], img: [b.top, b.height], display: style.display, rows: style.gridTemplateRows, imgStyle: image.getAttribute('style') });
    }));
  }

  await page.goto(`${base}/index.html`);
  await ready(page);
  await page.evaluate(async () => {
    const settings = await window.flashcardStore.getSettings();
    await window.flashcardStore.saveSettings({ ...settings, theme: 'light', paperTexture: true });
    await window.flashcardStore.deleteSet('showcase');
    await window.flashcardStore.deleteSet('cell-diagram');
    await window.flashcardStore.flush?.();
    localStorage.setItem('erudite-theme', 'light');
    localStorage.setItem('erudite-goal-ring-last', 'null');
  });
  await page.reload();
  await ready(page);
  await page.waitForTimeout(2600);
  if (process.env.DEBUG_STORE) {
    console.log(await page.evaluate(async () => JSON.stringify({
      theme: (await window.flashcardStore.getSettings()).theme,
      sets: (await window.flashcardStore.listSetsMeta?.() || []).length,
      cls: document.documentElement.className
    })));
  }
  await capture(page, '08-paper');

  await context.close();
}

function dataUrl(file) {
  return `data:image/png;base64,${fs.readFileSync(file).toString('base64')}`;
}

async function frame(browser, base) {
  const context = await browser.newContext({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  const page = await context.newPage();
  await page.goto(`${base}/generator/frame.html`);
  for (const shot of SHOTS) {
    await page.evaluate(({ shot, image }) => window.renderFrame({ ...shot, image }), {
      shot,
      image: dataUrl(path.join(rawDir, `${shot.id}.png`))
    });
    await page.waitForTimeout(250);
    await page.screenshot({ path: path.join(outDir, `phone-${shot.id}.png`) });
  }

  await page.setViewportSize({ width: 1024, height: 500 });
  await page.goto(`${base}/generator/feature.html`);
  await page.evaluate(({ name, today, swipe }) => window.renderFeature({ name, today, swipe }), {
    name: APP_NAME,
    today: dataUrl(path.join(rawDir, '01-today.png')),
    swipe: dataUrl(path.join(rawDir, '02-swipe.png'))
  });
  await page.waitForTimeout(300);
  await page.screenshot({ path: path.join(outDir, 'feature-graphic-1024x500.png') });
  await context.close();
}

async function main() {
  fs.mkdirSync(outDir, { recursive: true });
  fs.mkdirSync(rawDir, { recursive: true });
  const server = await serve();
  const base = `http://localhost:${server.address().port}`;
  const browser = await chromium.launch({ executablePath: process.env.CHROMIUM || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  try {
    if (!process.env.FRAME_ONLY) await captureApp(browser, base);
    await frame(browser, base);
  } finally {
    await browser.close();
    server.close();
  }
  console.log(`Store images written to ${path.relative(repo, outDir)}`);
}

main().catch(error => {
  console.error(error);
  process.exitCode = 1;
});
