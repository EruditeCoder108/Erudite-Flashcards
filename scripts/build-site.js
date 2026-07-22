const fs = require('fs/promises');
const path = require('path');

const root = path.resolve(__dirname, '..');
const landingDir = path.join(root, 'erudite-landing');
const deckDir = path.join(root, 'premade-cards');
const outDir = path.join(root, 'site');

async function copyEntry(source, target) {
  const stat = await fs.stat(source);
  if (stat.isDirectory()) {
    await fs.mkdir(target, { recursive: true });
    const entries = await fs.readdir(source);
    await Promise.all(entries.map((entry) => copyEntry(path.join(source, entry), path.join(target, entry))));
    return;
  }
  await fs.mkdir(path.dirname(target), { recursive: true });
  await fs.copyFile(source, target);
}

async function copySelectedLandingFiles() {
  const files = ['index.html', 'styles.css', 'script.js', 'assets'];
  await Promise.all(files.map((entry) => copyEntry(path.join(landingDir, entry), path.join(outDir, entry))));
}

async function copyDeckLibrary() {
  const entries = await fs.readdir(deckDir);
  await Promise.all(entries.map((entry) => copyEntry(path.join(deckDir, entry), path.join(outDir, entry))));
}

async function build() {
  if (path.dirname(outDir) !== root || path.basename(outDir) !== 'site') {
    throw new Error(`Refusing to clean unexpected output directory: ${outDir}`);
  }

  await fs.rm(outDir, { recursive: true, force: true });
  await fs.mkdir(outDir, { recursive: true });
  await copySelectedLandingFiles();
  await copyDeckLibrary();
  console.log('Built website and premade-deck library in site/.');
}

build().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
