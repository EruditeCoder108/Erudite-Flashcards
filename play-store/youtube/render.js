'use strict';
// Renders thumbnail.html to thumbnail-1280x720.png (YouTube's size).
//   CHROMIUM=/path/to/chrome node play-store/youtube/render.js
const path = require('path');
const { pathToFileURL } = require('url');
const { chromium } = require('playwright-core');

(async () => {
  const browser = await chromium.launch({ executablePath: process.env.CHROMIUM });
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1 });
  await page.goto(pathToFileURL(path.join(__dirname, 'thumbnail.html')).href);
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(300);
  await page.screenshot({ path: path.join(__dirname, 'thumbnail-1280x720.png') });
  await browser.close();
  console.log('wrote thumbnail-1280x720.png');
})();
