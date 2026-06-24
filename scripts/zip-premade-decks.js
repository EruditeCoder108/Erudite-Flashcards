const fs = require('fs/promises');
const path = require('path');
const JSZip = require('d:/productivity-toolkit/Erudite-flashcards/node_modules/jszip');

const root = path.resolve(__dirname, '..');
const premadeDir = path.join(root, 'premade-cards');

async function exists(filePath) {
  try {
    await fs.access(filePath);
    return true;
  } catch (_error) {
    return false;
  }
}

async function addDirectoryToZip(zip, srcDir, zipPath = '') {
  const entries = await fs.readdir(srcDir, { withFileTypes: true });
  for (const entry of entries) {
    const fullPath = path.join(srcDir, entry.name);
    const relPath = zipPath ? `${zipPath}/${entry.name}` : entry.name;
    if (entry.isDirectory()) {
      await addDirectoryToZip(zip, fullPath, relPath);
    } else if (entry.isFile()) {
      const data = await fs.readFile(fullPath);
      zip.file(relPath, data);
    }
  }
}

function clozeIndexesFromText(value) {
  const indexes = new Set();
  String(value || '').replace(/\{\{c(\d+)::([\s\S]*?)\}\}/gi, (_match, index) => {
    indexes.add(Number(index));
    return '';
  });
  return Array.from(indexes);
}

function calculateExpandedCardCount(deckJson) {
  let totalCards = 0;
  const cards = Array.isArray(deckJson.cards) ? deckJson.cards : [];
  for (const card of cards) {
    const noteType = card.noteType || card.cardType || '';
    
    // 1. Image Occlusion
    const occlusionData = card.occlusion || card.imageOcclusion;
    if (noteType === 'image-occlusion' || occlusionData) {
      const masks = occlusionData && Array.isArray(occlusionData.masks) 
        ? occlusionData.masks 
        : [];
      totalCards += masks.length;
    }
    // 2. Cloze
    else if (noteType === 'cloze' || /\{\{c\d+::[\s\S]*?\}\}/i.test(`${card.text || ''} ${card.cloze || ''} ${card.term || ''} ${card.definition || ''}`)) {
      const indexes = clozeIndexesFromText(`${card.text || ''} ${card.cloze || ''} ${card.term || ''} ${card.definition || ''}`);
      totalCards += indexes.length > 0 ? indexes.length : 1;
    }
    // 3. Basic Reverse / Reverse flag
    else if (noteType === 'basic-reverse' || noteType === 'reverse' || card.generateReverse === true || card.reverse === true) {
      totalCards += 2;
    }
    // 4. Basic
    else {
      totalCards += 1;
    }
  }
  return totalCards;
}

async function processSubjectDirectory(subjectPath) {
  const manifestPath = path.join(subjectPath, 'manifest.json');
  if (!(await exists(manifestPath))) return;

  console.log(`Processing subject directory: ${path.relative(root, subjectPath)}`);
  const manifestRaw = await fs.readFile(manifestPath, 'utf8');
  let manifest;
  try {
    manifest = JSON.parse(manifestRaw);
  } catch (error) {
    console.error(`Error parsing manifest in ${subjectPath}:`, error);
    return;
  }

  if (!Array.isArray(manifest)) {
    console.error(`Manifest is not an array in ${subjectPath}`);
    return;
  }

  let updated = false;

  for (const item of manifest) {
    const originalFileName = item.fileName || item.filename || item.file || '';
    if (!originalFileName) continue;

    const zip = new JSZip();
    let zipName = '';
    let itemPath = path.join(subjectPath, originalFileName);
    let isDirectory = false;
    let isJsonFile = false;
    let deckJson = null;
    let needsZipping = false;

    if (await exists(itemPath)) {
      const stats = await fs.stat(itemPath);
      isDirectory = stats.isDirectory();
      isJsonFile = stats.isFile() && originalFileName.toLowerCase().endsWith('.json');
    } else if (!originalFileName.toLowerCase().endsWith('.zip')) {
      // Try appending .json if not a zip
      const altPath = `${itemPath}.json`;
      if (await exists(altPath)) {
        itemPath = altPath;
        isJsonFile = true;
      }
    }

    if (isDirectory) {
      zipName = `${originalFileName}.zip`;
      needsZipping = true;
      const deckJsonPath = path.join(itemPath, 'deck.json');
      if (!(await exists(deckJsonPath))) {
        console.error(`Missing deck.json in premade folder: ${itemPath}`);
        continue;
      }
      const deckJsonData = await fs.readFile(deckJsonPath, 'utf8');
      deckJson = JSON.parse(deckJsonData);
      zip.file('deck.json', deckJsonData);

      const mediaPath = path.join(itemPath, 'media');
      if (await exists(mediaPath)) {
        const mediaFolder = zip.folder('media');
        await addDirectoryToZip(mediaFolder, mediaPath);
      }
    } else if (isJsonFile) {
      const cleanName = originalFileName.replace(/\.json$/i, '');
      zipName = `${cleanName}.zip`;
      needsZipping = true;
      const fileData = await fs.readFile(itemPath, 'utf8');
      try {
        deckJson = JSON.parse(fileData);
        zip.file('deck.json', JSON.stringify(deckJson, null, 2));
      } catch (error) {
        console.error(`Invalid JSON file: ${itemPath}`);
        continue;
      }
    } else {
      // Already zipped
      const cleanName = originalFileName.replace(/\.zip$/i, '');
      const zipPath = path.join(subjectPath, `${cleanName}.zip`);
      if (await exists(zipPath)) {
        zipName = `${cleanName}.zip`;
        const zipData = await fs.readFile(zipPath);
        const loadedZip = await JSZip.loadAsync(zipData);
        const deckEntry = Object.values(loadedZip.files).find(entry => entry.name === 'deck.json' || entry.name.endsWith('/deck.json'));
        if (deckEntry) {
          deckJson = JSON.parse(await deckEntry.async('string'));
        }
      } else {
        console.warn(`File/Folder/ZIP not found: ${itemPath}`);
        continue;
      }
    }

    if (deckJson) {
      const expandedCount = calculateExpandedCardCount(deckJson);
      console.log(`Calculated expanded cards for ${originalFileName}: ${expandedCount}`);
      item.cardCount = expandedCount;
      item.fileName = zipName;
      updated = true;

      if (needsZipping) {
        console.log(`Zipping ${originalFileName} -> ${zipName}...`);
        const buffer = await zip.generateAsync({ type: 'nodebuffer', compression: 'DEFLATE' });
        const zipPath = path.join(subjectPath, zipName);
        await fs.writeFile(zipPath, buffer);

        // Clean up original folder/file
        if (isDirectory) {
          await fs.rm(itemPath, { recursive: true, force: true });
        } else if (isJsonFile) {
          await fs.rm(itemPath, { force: true });
        }
      }
    }
  }

  if (updated) {
    await fs.writeFile(manifestPath, JSON.stringify(manifest, null, 2), 'utf8');
    console.log(`Updated manifest.json in ${path.relative(root, subjectPath)}`);
  }
}

async function walkDirectories(dir) {
  const entries = await fs.readdir(dir, { withFileTypes: true });
  let hasManifest = false;

  for (const entry of entries) {
    if (entry.name === 'manifest.json') {
      hasManifest = true;
    }
  }

  if (hasManifest) {
    await processSubjectDirectory(dir);
  } else {
    for (const entry of entries) {
      if (entry.isDirectory() && entry.name !== 'node_modules' && !entry.name.startsWith('.')) {
        await walkDirectories(path.join(dir, entry.name));
      }
    }
  }
}

async function main() {
  if (!(await exists(premadeDir))) {
    console.error('premade-cards directory not found');
    process.exitCode = 1;
    return;
  }
  console.log('Starting premade decks packaging to ZIP and manifest card counts update...');
  await walkDirectories(premadeDir);
  console.log('ZIP packaging and manifests update complete.');
}

main().catch(error => {
  console.error(error);
  process.exitCode = 1;
});
