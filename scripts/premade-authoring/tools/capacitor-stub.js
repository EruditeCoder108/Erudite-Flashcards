// Preview-only stand-in for Capacitor in a desktop browser. Files live in
// IndexedDB and in memory, so the real mobile store can run. Never shipped.
(function () {
  const files = new Map();
  const MIME = { webp: 'image/webp', png: 'image/png', jpg: 'image/jpeg', jpeg: 'image/jpeg', svg: 'image/svg+xml', gif: 'image/gif', mp3: 'audio/mpeg' };
  const key = (path, directory) => `${directory || 'DATA'}:${String(path).replace(/^\/+/, '')}`;
  const openDb = () => new Promise((resolve, reject) => {
    const request = indexedDB.open('capacitor-stub', 1);
    request.onupgradeneeded = () => request.result.createObjectStore('files');
    request.onsuccess = () => resolve(request.result);
    request.onerror = () => reject(request.error);
  });
  const dbReady = openDb();
  const ready = dbReady.then(db => new Promise(resolve => {
    const tx = db.transaction('files', 'readonly');
    const cursorRequest = tx.objectStore('files').openCursor();
    cursorRequest.onsuccess = () => {
      const cursor = cursorRequest.result;
      if (!cursor) return resolve();
      files.set(cursor.key, cursor.value);
      cursor.continue();
    };
    cursorRequest.onerror = () => resolve();
  }));
  const persist = (k, value) => dbReady.then(db => new Promise(resolve => {
    const tx = db.transaction('files', 'readwrite');
    if (value === undefined) tx.objectStore('files').delete(k);
    else tx.objectStore('files').put(value, k);
    tx.oncomplete = resolve;
    tx.onerror = resolve;
  }));
  const notFound = () => Object.assign(new Error('File does not exist'), { code: 'OS-PLUG-FILE-0008' });

  const Filesystem = {
    async readFile({ path, directory }) {
      await ready;
      const k = key(path, directory);
      if (!files.has(k)) throw notFound();
      return { data: files.get(k) };
    },
    async writeFile({ path, directory, data }) {
      await ready;
      const k = key(path, directory);
      files.set(k, data);
      await persist(k, data);
      return { uri: `stub://${k}` };
    },
    async deleteFile({ path, directory }) {
      await ready;
      const k = key(path, directory);
      if (!files.has(k)) throw notFound();
      files.delete(k);
      await persist(k);
    },
    async rename({ from, to, directory, toDirectory }) {
      await ready;
      const source = key(from, directory);
      if (!files.has(source)) throw notFound();
      const target = key(to, toDirectory || directory);
      files.set(target, files.get(source));
      files.delete(source);
      await persist(target, files.get(target));
      await persist(source);
    },
    async stat({ path, directory }) {
      await ready;
      const k = key(path, directory);
      if (!files.has(k)) throw notFound();
      return { type: 'file', size: String(files.get(k)).length, uri: `stub://${k}` };
    },
    async getUri({ path, directory }) {
      return { uri: `stub://${key(path, directory)}` };
    },
    async rmdir({ path, directory }) {
      await ready;
      const prefix = `${key(path, directory)}/`;
      for (const k of [...files.keys()]) {
        if (k.startsWith(prefix)) {
          files.delete(k);
          await persist(k);
        }
      }
    },
    async mkdir() {},
    async readdir() { return { files: [] }; }
  };

  window.Capacitor = {
    getPlatform: () => 'web',
    isNativePlatform: () => false,
    isPluginAvailable: name => name === 'Filesystem',
    convertFileSrc(uri) {
      const k = String(uri || '').replace(/^stub:\/\//, '');
      const data = files.get(k);
      if (typeof data !== 'string') return uri;
      if (data.startsWith('data:')) return data;
      const ext = (k.split('.').pop() || '').toLowerCase();
      return `data:${MIME[ext] || 'application/octet-stream'};base64,${data}`;
    },
    Plugins: { Filesystem }
  };
}());
