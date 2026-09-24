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

  const heroLabel = await page.locator('#today-hero .stack-button').getAttribute('aria-label');
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

  const lastDuration = await page.evaluate(async () => {
    await new Promise(resolve => setTimeout(resolve, 600));
    const set = await window.flashcardStore.getSet('alpha');
    const reviewed = set.cards.find(card => (card.reviewHistory || []).length);
    return reviewed?.reviewHistory?.[0]?.durationMs ?? null;
  });
  check('review records time taken', Number.isFinite(lastDuration) && lastDuration > 0, `durationMs=${lastDuration}`);

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

  await checkSwipe(page, base, check);
  await checkOcclusion(page, base, check);
  await checkPackageImport(page, base, check);
  await checkReminder(page, base, check);
  await checkPremadeSample(page, base, check);

  check('no page errors', errors.length === 0, errors.slice(0, 5).join(' | '));
}

async function drag(page, from, dx, dy, steps, stepMs) {
  await page.mouse.move(from.x, from.y);
  await page.mouse.down();
  for (let index = 1; index <= steps; index += 1) {
    await page.mouse.move(from.x + (dx * index) / steps, from.y + (dy * index) / steps);
    await page.waitForTimeout(stepMs);
  }
  await page.mouse.up();
}

async function checkSwipe(page, base, check) {
  await page.evaluate(async item => {
    await window.flashcardStore.saveSet(item);
    await window.flashcardStore.flush?.();
  }, deck('gamma', 6));
  await page.goto(`${base}/mobile/study.html?setId=gamma&srs=true&from=library`);
  await page.waitForSelector('#card-stage .study-card.slot-active', { timeout: 20000 });
  await page.waitForTimeout(500);
  await page.locator('#reveal-button').click();
  await page.waitForSelector('#rating-dock:not(.hidden)', { timeout: 5000 });
  const revealHidden = await page.locator('#reveal-button').evaluate(element => element.classList.contains('hidden'));
  check('reveal button flips and gives way to ratings', revealHidden);

  const box = await page.locator('#card-stage .study-card.slot-active').boundingBox();
  const center = { x: box.x + box.width / 2, y: box.y + box.height / 2 };
  const ratings = async () => page.evaluate(async () => {
    await window.flashcardStore.flush?.();
    const set = await window.flashcardStore.getSet('gamma');
    return set.cards.flatMap(card => (card.reviewHistory || []).map(entry => entry.rating));
  });

  // A slow, short drag is not a swipe: the card springs back and nothing is rated.
  await drag(page, center, 30, 0, 6, 40);
  await page.waitForTimeout(900);
  const afterSlow = await ratings();
  const restored = await page.locator('#card-stage .study-card.slot-active').evaluate(element => element.style.transform || 'none');
  check('slow short drag springs back without rating', afterSlow.length === 0 && !/translate3d\((?!0px, 0px)/.test(restored), `ratings=${afterSlow.length} transform=${restored}`);

  // A quick flick commits even though it travels less than the swipe distance.
  await drag(page, center, 44, 0, 3, 8);
  await page.waitForTimeout(1200);
  const afterFlick = await ratings();
  check('quick flick right rates Good', afterFlick.length === 1 && afterFlick[0] === 'Good', afterFlick.join(','));
}

function occlusionDeck(id, guessMode, image) {
  const masks = [
    { id: 'm1', shape: 'rect', x: 0.1, y: 0.1, w: 0.2, h: 0.1, answer: 'Nucleus', hint: 'Control centre' },
    { id: 'm2', shape: 'rect', x: 0.5, y: 0.4, w: 0.2, h: 0.1, answer: 'Vacuole' },
    { id: 'm3', shape: 'ellipse', x: 0.3, y: 0.7, w: 0.2, h: 0.1, answer: 'Wall' }
  ];
  return {
    id,
    name: `Occlusion ${guessMode}`,
    cards: masks.map((mask, index) => ({
      id: `${id}-${mask.id}`,
      noteId: `${id}-note`,
      noteType: 'image-occlusion',
      cardTemplate: 'image-occlusion-mask',
      term: '<strong>Guess the hidden part.</strong>',
      definition: mask.answer,
      termImage: image,
      definitionImage: image,
      noteFields: { answer: mask.answer, hint: mask.hint || '', maskId: mask.id },
      imageOcclusion: { version: 1, image, guessMode, masks, targetMaskId: mask.id, targetMaskIndex: index }
    }))
  };
}

async function checkOcclusion(page, base, check) {
  // Seed from the main page: the study page holds heavy writes until it closes.
  await page.goto(`${base}/index.html`);
  await page.waitForFunction(() => document.body.classList.contains('app-ready'), null, { timeout: 20000 });
  const image = await page.evaluate(() => {
    const canvas = document.createElement('canvas');
    canvas.width = 600;
    canvas.height = 400;
    const context = canvas.getContext('2d');
    context.fillStyle = '#e2e8f0';
    context.fillRect(0, 0, 600, 400);
    context.fillStyle = '#1e293b';
    context.fillRect(60, 40, 120, 40);
    return canvas.toDataURL('image/png');
  });
  await page.evaluate(async decks => {
    for (const item of decks) await window.flashcardStore.saveSet(item);
    await window.flashcardStore.flush?.();
  }, [occlusionDeck('occ-all', 'hide-all', image), occlusionDeck('occ-one', 'hide-one', image)]);

  for (const [deckId, expectedMasks] of [['occ-all', 3], ['occ-one', 1]]) {
    // Normal (non-SRS) mode shows cards in order, so the first card asks mask m1.
    await page.goto(`${base}/mobile/study.html?setId=${deckId}&srs=false&from=library`);
    await page.waitForSelector('#card-stage .study-card.slot-active .occlusion-mask-layer.is-positioned', { timeout: 20000 });
    const front = page.locator('#card-stage .study-card.slot-active .card-face.front');
    const maskCount = await front.locator('.occlusion-mask').count();
    const label = await front.locator('.occlusion-mask.target .occlusion-mask-label').innerText();
    check(`${deckId} front masks`, maskCount === expectedMasks && label === 'Control centre', `masks=${maskCount} label=${label}`);
    await page.locator('#card-stage .study-card.slot-active').click({ position: { x: 20, y: 20 } });
    await page.waitForTimeout(500);
    const tag = await page.locator('#card-stage .study-card.slot-active .card-face.back .occlusion-answer-tag').innerText();
    check(`${deckId} back answer tag`, tag === 'Nucleus', tag);
  }

  if (process.env.SCREENSHOTS) await page.screenshot({ path: path.join(process.env.SCREENSHOTS, 'occlusion-back.png') });

  await page.locator('#card-stage .study-card.slot-active .card-face.back [data-image-side]').first().click();
  await page.waitForSelector('#image-modal:not(.hidden)', { timeout: 5000 });
  const viewport = page.locator('#zoom-viewport');
  const box = await viewport.boundingBox();
  await page.mouse.click(box.x + box.width / 2, box.y + box.height / 2, { clickCount: 1 });
  await page.mouse.click(box.x + box.width / 2, box.y + box.height / 2, { clickCount: 1 });
  await page.waitForTimeout(350);
  const zoomed = await viewport.evaluate(element => element.classList.contains('is-zoomed'));
  const zoomMasks = await page.locator('#zoom-stage .zoom-occlusion-layer .occlusion-mask').count();
  check('double-tap zooms image with masks', zoomed && zoomMasks === 1, `zoomed=${zoomed} masks=${zoomMasks}`);
  if (process.env.SCREENSHOTS) await page.screenshot({ path: path.join(process.env.SCREENSHOTS, 'zoom.png') });
}

// Imports an AI-style ZIP whose declared image size is wrong (the AI measured
// boxes on the real 1400x900 file but declared 1000x1000). Masks must land on the
// labels, and the stored image must be downscaled to the 2048 px limit or less.
async function checkPackageImport(page, base, check) {
  await page.goto(`${base}/index.html`);
  await page.waitForFunction(() => document.body.classList.contains('app-ready'), null, { timeout: 20000 });
  const zipBase64 = await page.evaluate(async () => {
    const canvas = document.createElement('canvas');
    canvas.width = 1400;
    canvas.height = 900;
    const context = canvas.getContext('2d');
    context.fillStyle = '#ffffff';
    context.fillRect(0, 0, 1400, 900);
    const png = canvas.toDataURL('image/png').split(',')[1];
    const zip = new window.JSZip();
    zip.file('deck.json', JSON.stringify({
      version: 1,
      name: 'Imported diagram',
      cards: [
        { type: 'basic', term: 'Q1', definition: 'A1' },
        {
          type: 'image-occlusion',
          term: 'Label the cell',
          image: 'media/cell.png',
          occlusion: {
            units: 'px',
            imageWidth: 1000,
            imageHeight: 1000,
            masks: [
              { shape: 'rect', bboxPx: [1200, 700, 140, 70], answer: 'Wall' },
              { shape: 'rect', bboxPx: [140, 90, 280, 90], answer: 'Nucleus' }
            ]
          }
        }
      ]
    }));
    zip.folder('media').file('cell.png', png, { base64: true });
    return zip.generateAsync({ type: 'base64' });
  });
  await page.locator('.tab-button[data-tab="create"]').click();
  await page.waitForTimeout(500);
  const skip = page.locator('text=Skip Guide');
  if (await skip.count()) await skip.first().click();
  await page.setInputFiles('#mobile-txt-input', { name: 'deck.zip', mimeType: 'application/zip', buffer: Buffer.from(zipBase64, 'base64') });
  await page.waitForFunction(() => document.getElementById('mobile-create-title')?.value === 'Imported diagram', null, { timeout: 10000 });
  await page.locator('#header-creator-save-btn').click();
  await page.waitForTimeout(1500);
  const result = await page.evaluate(async () => {
    const sets = await window.flashcardStore.listSets();
    const set = sets.find(item => item.name === 'Imported diagram');
    const card = set?.cards.find(item => item.noteType === 'image-occlusion' && item.definition.includes('Wall'));
    const mask = card?.imageOcclusion?.masks?.find(item => String(item.answer).includes('Wall'));
    const image = new Image();
    image.src = card?.termImage || '';
    await image.decode().catch(() => {});
    return { cards: set?.cards.length || 0, mask, width: image.naturalWidth, src: String(card?.termImage || '').slice(0, 16) };
  });
  const mask = result.mask || {};
  const onLabel = Math.abs(mask.x - 1200 / 1400) < 0.01 && Math.abs(mask.y - 700 / 900) < 0.01;
  check('package import places masks on real image size', result.cards === 3 && onLabel, JSON.stringify({ cards: result.cards, x: mask.x, y: mask.y }));
  check('imported image stored within size limit', result.width > 0 && result.width <= 2048, `${result.width}px ${result.src}`);
}

async function checkReminder(page, base, check) {
  await page.goto(`${base}/index.html`);
  await page.waitForFunction(() => document.body.classList.contains('app-ready'), null, { timeout: 20000 });
  await page.locator('.tab-button[data-tab="more"]').click();
  await page.locator('[data-action="open-reminder-settings"]').click();
  await page.locator('#reminder-enabled').check();
  await page.locator('#reminder-time').fill('21:30');
  await page.locator('#reminder-save').click();
  // Scheduling re-runs after the stats refresh that saving triggers; wait for it to settle.
  await page.waitForFunction(() => window.Capacitor.Plugins.LocalNotifications.scheduled.length === 7, null, { timeout: 5000 }).catch(() => {});
  const scheduled = await page.evaluate(() => window.Capacitor.Plugins.LocalNotifications.scheduled.map(item => ({
    title: item.title,
    hour: new Date(item.schedule.at).getHours(),
    minute: new Date(item.schedule.at).getMinutes(),
    exact: item.isExactNotification
  })));
  const allAtTime = scheduled.every(item => item.hour === 21 && item.minute === 30 && item.exact === false);
  check('daily reminder schedules a week of inexact notifications', scheduled.length === 7 && allAtTime, `${scheduled.length} ${scheduled[0]?.title || ''}`);
  const label = await page.locator('#more-reminder-label').innerText();
  check('reminder label shows the time', /9:30/.test(label), label);
}

// Free users import the first 20 cards of a premade chapter; Pro fills in the
// rest of the same deck. The premade server is served from memory.
async function checkPremadeSample(page, base, check) {
  const JSZip = require('jszip');
  const zip = new JSZip();
  zip.file('deck.json', JSON.stringify({
    version: 1,
    name: 'Chapter 1: Life Processes',
    cards: Array.from({ length: 30 }, (_, index) => ({ type: 'basic', term: `Premade Q${index + 1}`, definition: `A${index + 1}` }))
  }));
  const zipBuffer = await zip.generateAsync({ type: 'nodebuffer' });
  await page.route('https://erudite-flashcards.netlify.app/**', route => {
    const url = route.request().url();
    if (url.endsWith('premade-catalog.json')) {
      return route.fulfill({ contentType: 'application/json', body: JSON.stringify({ classes: [{ id: '10th', name: 'Class 10', subjects: [{ id: 'Biology', name: 'Biology' }] }] }) });
    }
    if (url.endsWith('/10th/Biology/manifest.json')) {
      return route.fulfill({ contentType: 'application/json', body: JSON.stringify([{ id: 'ch1', name: 'Chapter 1: Life Processes', fileName: 'ch1.zip', cardCount: 30 }]) });
    }
    if (url.endsWith('/10th/Biology/ch1.zip')) {
      return route.fulfill({ contentType: 'application/zip', headers: { 'content-length': String(zipBuffer.length) }, body: zipBuffer });
    }
    return route.fulfill({ status: 404, body: '' });
  });

  await page.goto(`${base}/index.html`);
  await page.waitForFunction(() => document.body.classList.contains('app-ready'), null, { timeout: 20000 });
  await page.locator('.tab-button[data-tab="library"]').click();
  await page.locator('.source-option[data-action="open-premade"]').click();
  await page.waitForSelector('.premade-row .sample-pill', { timeout: 10000 });
  const pill = await page.locator('.premade-row .sample-pill').innerText();
  check('premade chapter shows its free sample size', /20 free/.test(pill), pill.trim());
  await page.locator('[data-action="import-premade"]').first().click();
  await page.waitForSelector('#take-deck-overlay:not(.hidden) #take-deck-sample:not(.hidden)', { timeout: 10000 });
  await page.locator('#mobile-take-deck-confirm').click();
  await page.waitForTimeout(1500);
  const sampled = await page.evaluate(async () => {
    const sets = await window.flashcardStore.listSets();
    const set = sets.find(item => item.premadeSource?.fileName === 'ch1.zip');
    return { cards: set?.cards.length || 0, source: set?.premadeSource || null };
  });
  check('free import keeps the first 20 cards', sampled.cards === 20 && sampled.source?.sample === true, JSON.stringify(sampled));

  // Pro preview in a browser build, then the sample fills in on next launch.
  await page.evaluate(async () => {
    await window.flashcardStore.flush?.();
    localStorage.setItem('erudite-pro-debug', 'on');
  });
  await page.reload();
  await page.waitForFunction(() => document.body.classList.contains('app-ready'), null, { timeout: 20000 });
  await page.waitForFunction(async () => {
    const sets = await window.flashcardStore.listSets();
    const set = sets.find(item => item.premadeSource?.fileName === 'ch1.zip');
    return set && set.premadeSource.sample === false;
  }, null, { timeout: 15000, polling: 500 }).catch(() => {});
  const unlocked = await page.evaluate(async () => {
    const sets = await window.flashcardStore.listSets();
    const set = sets.find(item => item.premadeSource?.fileName === 'ch1.zip');
    return { cards: set?.cards.length || 0, sample: set?.premadeSource?.sample, first: set?.cards?.[0]?.term || '' };
  });
  check('Pro fills in the rest of a sample deck', unlocked.cards === 30 && unlocked.sample === false && /Premade Q1\b/.test(unlocked.first), JSON.stringify(unlocked));
  await page.evaluate(() => localStorage.removeItem('erudite-pro-debug'));
  await page.unroute('https://erudite-flashcards.netlify.app/**');
}

main().catch(error => {
  console.error(error);
  process.exitCode = 1;
});
