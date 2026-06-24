const fs = require('fs/promises');
const path = require('path');
const JSZip = require('jszip');

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
  let manifest = [];
  let manifestExists = await exists(manifestPath);

  if (manifestExists) {
    console.log(`Processing subject directory: ${path.relative(root, subjectPath)}`);
    const manifestRaw = await fs.readFile(manifestPath, 'utf8');
    try {
      manifest = JSON.parse(manifestRaw);
    } catch (error) {
      console.error(`Error parsing manifest in ${subjectPath}:`, error);
      return;
    }
  } else {
    console.log(`Creating new manifest.json and processing subject directory: ${path.relative(root, subjectPath)}`);
  }

  if (!Array.isArray(manifest)) {
    console.error(`Manifest is not an array in ${subjectPath}`);
    return;
  }

  // Find all deck sources in this directory
  const entries = await fs.readdir(subjectPath, { withFileTypes: true });
  let updated = false;

  for (const entry of entries) {
    if (entry.name === 'manifest.json') continue;

    let isDirectory = entry.isDirectory() && entry.name !== 'media' && !entry.name.startsWith('.');
    let isJsonFile = entry.isFile() && entry.name.toLowerCase().endsWith('.json');
    let isZipFile = entry.isFile() && entry.name.toLowerCase().endsWith('.zip');

    if (!isDirectory && !isJsonFile && !isZipFile) continue;

    const baseName = entry.name.replace(/\.(json|zip)$/i, '');
    const zipName = `${baseName}.zip`;
    let itemPath = path.join(subjectPath, entry.name);
    let deckJson = null;
    let needsZipping = false;
    const zip = new JSZip();

    if (isDirectory) {
      const deckJsonPath = path.join(itemPath, 'deck.json');
      if (!(await exists(deckJsonPath))) {
        continue; // Skip folders that do not have deck.json
      }
      try {
        const deckJsonData = await fs.readFile(deckJsonPath, 'utf8');
        deckJson = JSON.parse(deckJsonData);
        zip.file('deck.json', deckJsonData);

        const mediaPath = path.join(itemPath, 'media');
        if (await exists(mediaPath)) {
          const mediaFolder = zip.folder('media');
          await addDirectoryToZip(mediaFolder, mediaPath);
        }
        needsZipping = true;
      } catch (error) {
        console.error(`Error reading deck.json in folder ${itemPath}:`, error);
        continue;
      }
    } else if (isJsonFile) {
      try {
        const fileData = await fs.readFile(itemPath, 'utf8');
        deckJson = JSON.parse(fileData);
        // Verify it looks like a deck
        if (!deckJson.cards && !deckJson.version) {
          console.warn(`File ${entry.name} does not look like a valid deck JSON. Skipping.`);
          continue;
        }
        zip.file('deck.json', JSON.stringify(deckJson, null, 2));
        needsZipping = true;
      } catch (error) {
        console.error(`Error processing JSON file ${itemPath}:`, error);
        continue;
      }
    } else if (isZipFile) {
      try {
        const zipData = await fs.readFile(itemPath);
        const loadedZip = await JSZip.loadAsync(zipData);
        const deckEntry = Object.values(loadedZip.files).find(e => e.name === 'deck.json' || e.name.endsWith('/deck.json'));
        if (deckEntry) {
          deckJson = JSON.parse(await deckEntry.async('string'));
        } else {
          console.warn(`ZIP file ${entry.name} has no deck.json. Skipping.`);
          continue;
        }
      } catch (error) {
        console.error(`Error reading ZIP file ${itemPath}:`, error);
        continue;
      }
    }

    if (deckJson) {
      const expandedCount = calculateExpandedCardCount(deckJson);
      console.log(`Calculated expanded cards for ${entry.name}: ${expandedCount}`);

      // Find or create manifest entry
      let manifestItem = manifest.find(item => {
        const itemFileName = item.fileName || item.filename || item.file || '';
        const itemCleanFileName = itemFileName.replace(/\.zip$/i, '');
        return item.id === baseName || itemCleanFileName === baseName;
      });

      if (!manifestItem) {
        const cleanName = deckJson.name || baseName.replace(/[-_]+/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
        manifestItem = {
          id: baseName,
          name: cleanName,
          description: deckJson.description || '',
          difficulty: deckJson.difficulty || 'intermediate',
          estimatedTime: deckJson.estimatedTime || `${Math.max(5, Math.round(expandedCount * 0.25))} minutes`,
          fileName: zipName,
          cardCount: expandedCount,
          tags: deckJson.tags || []
        };
        manifest.push(manifestItem);
        updated = true;
        console.log(`Added new manifest entry for ${zipName}`);
      } else {
        if (manifestItem.cardCount !== expandedCount || manifestItem.fileName !== zipName) {
          manifestItem.cardCount = expandedCount;
          manifestItem.fileName = zipName;
          updated = true;
        }
        // Fill in missing metadata fields if available in deckJson
        if (!manifestItem.name && deckJson.name) { manifestItem.name = deckJson.name; updated = true; }
        if (!manifestItem.description && deckJson.description) { manifestItem.description = deckJson.description; updated = true; }
        if ((!manifestItem.tags || !manifestItem.tags.length) && deckJson.tags) { manifestItem.tags = deckJson.tags; updated = true; }
      }

      if (needsZipping) {
        console.log(`Zipping ${entry.name} -> ${zipName}...`);
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

  // Always write manifest if updated or if manifest.json did not exist (since we created it)
  if (updated || !manifestExists) {
    await fs.writeFile(manifestPath, JSON.stringify(manifest, null, 2), 'utf8');
    console.log(`Saved manifest.json in ${path.relative(root, subjectPath)}`);
  }
}

async function isSubjectDirectory(dirPath) {
  const entries = await fs.readdir(dirPath, { withFileTypes: true });
  for (const entry of entries) {
    if (entry.name === 'manifest.json') {
      return true;
    }
    if (entry.isFile()) {
      const ext = path.extname(entry.name).toLowerCase();
      if (ext === '.zip' || (ext === '.json' && entry.name !== 'manifest.json')) {
        return true;
      }
    }
    if (entry.isDirectory() && entry.name !== 'media' && !entry.name.startsWith('.')) {
      // Check if this subdirectory has a deck.json
      const deckJsonPath = path.join(dirPath, entry.name, 'deck.json');
      if (await exists(deckJsonPath)) {
        return true;
      }
    }
  }
  return false;
}

async function walkDirectories(dir) {
  const isSubject = await isSubjectDirectory(dir);

  if (isSubject) {
    await processSubjectDirectory(dir);
  } else {
    const entries = await fs.readdir(dir, { withFileTypes: true });
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
