const fs = require('fs/promises');
const path = require('path');

const root = path.resolve(__dirname, '..');
const outDir = path.join(root, 'www');

const htmlFiles = [
  'flashcards.html',
  'study.html',
  'creator.html',
  'card-browser.html',
  'diagnostics.html'
];

const sharedCoreScripts = [
  '<script src="js/core/schema.js"></script>',
  '<script src="js/core/backup.js"></script>',
  '<script src="js/core/stats.js"></script>',
  '<script src="js/core/srs.js"></script>',
  '<script src="js/core/review-session.js"></script>',
  '<script src="js/core/draft.js"></script>',
  '<script src="js/core/card-media.js"></script>',
  '<script src="js/core/math-render.js"></script>'
].join('\n    ');

const mobileBootstrapScripts = [
  '<script src="capacitor.js"></script>',
  '<script src="vendor/sql.js/sql-wasm.js"></script>',
  '<script src="js/mobile/premade-content-config.js"></script>',
  '<script src="js/mobile/mobile-store.js"></script>'
].join('\n    ');

async function exists(filePath) {
  try {
    await fs.access(filePath);
    return true;
  } catch (_error) {
    return false;
  }
}

async function copyFile(source, target) {
  await fs.mkdir(path.dirname(target), { recursive: true });
  await fs.copyFile(source, target);
}

async function copyDir(source, target) {
  if (!(await exists(source))) return;
  await fs.mkdir(target, { recursive: true });
  const entries = await fs.readdir(source, { withFileTypes: true });
  for (const entry of entries) {
    const from = path.join(source, entry.name);
    const to = path.join(target, entry.name);
    if (entry.isDirectory()) {
      await copyDir(from, to);
    } else if (entry.isFile()) {
      await copyFile(from, to);
    }
  }
}

function transformHtml(html) {
  let next = html
    .replace(/node_modules\/@fortawesome\/fontawesome-free\/css\/all\.min\.css/g, 'vendor/fontawesome/css/all.min.css')
    .replace(/node_modules\/katex\/dist\/katex\.min\.css/g, 'vendor/katex/katex.min.css')
    .replace(/node_modules\/katex\/dist\/katex\.min\.js/g, 'vendor/katex/katex.min.js')
    .replace(/node_modules\/katex\/dist\/contrib\/auto-render\.min\.js/g, 'vendor/katex/auto-render.min.js')
    .replace(/node_modules\/ts-fsrs\/dist\/index\.umd\.js/g, 'vendor/ts-fsrs/index.umd.js')
    .replace(/node_modules\/sortablejs\/Sortable\.min\.js/g, 'vendor/sortablejs/Sortable.min.js');

  if (!next.includes('css/mobile.css')) {
    if (next.includes('css/toast-notifications.css')) {
      next = next.replace(
        /(<link rel="stylesheet" href="css\/toast-notifications\.css">\s*)/,
        '$1\n    <link rel="stylesheet" href="css/mobile.css">\n'
      );
    } else {
      next = next.replace('</head>', '    <link rel="stylesheet" href="css/mobile.css">\n</head>');
    }
  }

  if (!next.includes('js/core/schema.js')) {
    next = next.replace(
      /<script src="js\/storage-client\.js"><\/script>/,
      `${sharedCoreScripts}\n    <script src="js/storage-client.js"></script>`
    );
  }

  if (!next.includes('js/mobile/mobile-store.js')) {
    next = next.replace(
      /<script src="js\/storage-client\.js"><\/script>/,
      `${mobileBootstrapScripts}\n    <script src="js/storage-client.js"></script>`
    );
  }

  return next;
}

async function writeIndex() {
  const index = await fs.readFile(path.join(root, 'mobile', 'index.html'), 'utf8');
  await fs.writeFile(path.join(outDir, 'index.html'), index, 'utf8');
}

async function copyHtml() {
  for (const file of htmlFiles) {
    const source = path.join(root, file);
    if (!(await exists(source))) continue;
    const html = await fs.readFile(source, 'utf8');
    await fs.writeFile(path.join(outDir, file), transformHtml(html), 'utf8');
  }
}

async function copyVendor() {
  await copyFile(
    path.join(root, 'node_modules', '@fortawesome', 'fontawesome-free', 'css', 'all.min.css'),
    path.join(outDir, 'vendor', 'fontawesome', 'css', 'all.min.css')
  );
  await copyDir(
    path.join(root, 'node_modules', '@fortawesome', 'fontawesome-free', 'webfonts'),
    path.join(outDir, 'vendor', 'fontawesome', 'webfonts')
  );
  await copyFile(
    path.join(root, 'node_modules', 'ts-fsrs', 'dist', 'index.umd.js'),
    path.join(outDir, 'vendor', 'ts-fsrs', 'index.umd.js')
  );
  await copyFile(
    path.join(root, 'node_modules', 'sortablejs', 'Sortable.min.js'),
    path.join(outDir, 'vendor', 'sortablejs', 'Sortable.min.js')
  );
  await copyFile(
    path.join(root, 'node_modules', 'jszip', 'dist', 'jszip.min.js'),
    path.join(outDir, 'vendor', 'jszip', 'jszip.min.js')
  );
  await copyFile(
    path.join(root, 'node_modules', 'katex', 'dist', 'katex.min.css'),
    path.join(outDir, 'vendor', 'katex', 'katex.min.css')
  );
  await copyFile(
    path.join(root, 'node_modules', 'katex', 'dist', 'katex.min.js'),
    path.join(outDir, 'vendor', 'katex', 'katex.min.js')
  );
  await copyFile(
    path.join(root, 'node_modules', 'katex', 'dist', 'contrib', 'auto-render.min.js'),
    path.join(outDir, 'vendor', 'katex', 'auto-render.min.js')
  );
  await copyDir(
    path.join(root, 'node_modules', 'katex', 'dist', 'fonts'),
    path.join(outDir, 'vendor', 'katex', 'fonts')
  );
  await copyFile(
    path.join(root, 'node_modules', 'sql.js', 'dist', 'sql-wasm.js'),
    path.join(outDir, 'vendor', 'sql.js', 'sql-wasm.js')
  );
  await copyFile(
    path.join(root, 'node_modules', 'sql.js', 'dist', 'sql-wasm.wasm'),
    path.join(outDir, 'vendor', 'sql.js', 'sql-wasm.wasm')
  );
}

async function main() {
  await fs.rm(outDir, { recursive: true, force: true });
  await fs.mkdir(outDir, { recursive: true });
  await copyHtml();
  await writeIndex();
  await copyDir(path.join(root, 'css'), path.join(outDir, 'css'));
  await copyDir(path.join(root, 'js'), path.join(outDir, 'js'));
  await copyDir(path.join(root, 'mobile'), path.join(outDir, 'mobile'));
  await copyDir(path.join(root, 'assets'), path.join(outDir, 'assets'));
  await copyVendor();
  
  // Bundle Capacitor SQLite plugin
  console.log('Bundling Capacitor SQLite plugin...');
  const { execSync } = require('child_process');
  execSync('npx esbuild node_modules/@capacitor-community/sqlite/dist/esm/index.js --bundle --minify --format=iife --global-name=CapacitorSqliteHelper --outfile=www/vendor/sqlite/sqlite.js', { stdio: 'inherit', cwd: root });

  console.log(`Mobile web build written to ${outDir}`);
}

main().catch(error => {
  console.error(error);
  process.exitCode = 1;
});
