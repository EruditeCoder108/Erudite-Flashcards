const fs = require('fs/promises');
const path = require('path');

const root = path.resolve(__dirname, '..');
const outDir = path.join(root, 'www');

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

async function writeIndex() {
  const index = await fs.readFile(path.join(root, 'mobile', 'index.html'), 'utf8');
  await fs.writeFile(path.join(outDir, 'index.html'), index, 'utf8');
}

async function copyMobileRuntime() {
  await copyDir(path.join(root, 'js', 'core'), path.join(outDir, 'js', 'core'));
  await copyDir(path.join(root, 'js', 'mobile'), path.join(outDir, 'js', 'mobile'));
  await copyFile(path.join(root, 'js', 'storage-client.js'), path.join(outDir, 'js', 'storage-client.js'));
  await copyFile(path.join(root, 'js', 'srs-manager.js'), path.join(outDir, 'js', 'srs-manager.js'));
  await copyFile(path.join(root, 'css', 'color-picker.css'), path.join(outDir, 'css', 'color-picker.css'));
  await copyDir(path.join(root, 'mobile', 'css'), path.join(outDir, 'mobile', 'css'));
  await copyDir(path.join(root, 'mobile', 'js'), path.join(outDir, 'mobile', 'js'));
  await copyFile(path.join(root, 'mobile', 'study.html'), path.join(outDir, 'mobile', 'study.html'));
  await copyFile(path.join(root, 'mobile', 'privacy.html'), path.join(outDir, 'mobile', 'privacy.html'));
}

async function copyMobileAssets() {
  await copyFile(path.join(root, 'assets', 'icons', 'icon.png'), path.join(outDir, 'assets', 'icons', 'icon.png'));
  await copyFile(path.join(root, 'assets', 'audio', 'Star.mp3'), path.join(outDir, 'assets', 'audio', 'Star.mp3'));
  await copyFile(path.join(root, 'assets', 'audio', 'success.mp3'), path.join(outDir, 'assets', 'audio', 'success.mp3'));
  await copyFile(path.join(root, 'assets', 'flashcard-assets', 'click.mp3'), path.join(outDir, 'assets', 'flashcard-assets', 'click.mp3'));
  await copyFile(path.join(root, 'assets', 'flashcard-assets', 'flip-sound.mp3'), path.join(outDir, 'assets', 'flashcard-assets', 'flip-sound.mp3'));
  await copyFile(path.join(root, 'assets', 'flashcard-assets', 'Next-card.mp3'), path.join(outDir, 'assets', 'flashcard-assets', 'Next-card.mp3'));
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
  await writeIndex();
  await copyMobileRuntime();
  await copyMobileAssets();
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
