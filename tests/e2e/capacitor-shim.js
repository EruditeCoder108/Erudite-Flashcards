// Minimal stand-in for the Capacitor runtime so the mobile web build can run in a
// desktop browser for smoke tests. Files persist in localStorage so data survives
// the navigation between index.html and mobile/study.html, just like on a device.
(function () {
  const PREFIX = 'erudite-e2e-fs:';
  const key = (directory, path) => `${PREFIX}${directory || 'DATA'}:${String(path).replace(/^\/+/, '')}`;
  const notFound = () => Object.assign(new Error('File does not exist'), { code: 'OS-PLUG-FILE-0008' });

  const Filesystem = {
    async readFile({ path, directory }) {
      const value = localStorage.getItem(key(directory, path));
      if (value === null) throw notFound();
      return { data: value };
    },
    async writeFile({ path, directory, data }) {
      localStorage.setItem(key(directory, path), data);
      return { uri: `file:///${directory}/${path}` };
    },
    async appendFile({ path, directory, data }) {
      const existing = localStorage.getItem(key(directory, path)) || '';
      localStorage.setItem(key(directory, path), existing + data);
    },
    async deleteFile({ path, directory }) {
      if (localStorage.getItem(key(directory, path)) === null) throw notFound();
      localStorage.removeItem(key(directory, path));
    },
    async stat({ path, directory }) {
      const value = localStorage.getItem(key(directory, path));
      if (value === null) throw notFound();
      return { type: 'file', size: value.length, uri: `file:///${directory}/${path}` };
    },
    async rename({ from, to, directory, toDirectory }) {
      const value = localStorage.getItem(key(directory, from));
      if (value === null) throw notFound();
      localStorage.setItem(key(toDirectory || directory, to), value);
      localStorage.removeItem(key(directory, from));
    },
    async getUri({ path, directory }) {
      return { uri: `file:///${directory}/${path}` };
    },
    async mkdir() {},
    async rmdir({ path, directory }) {
      const prefix = key(directory, path);
      Object.keys(localStorage).filter(item => item.startsWith(prefix)).forEach(item => localStorage.removeItem(item));
    },
    async readdir({ path, directory }) {
      const prefix = `${key(directory, path)}/`;
      const files = Object.keys(localStorage)
        .filter(item => item.startsWith(prefix))
        .map(item => ({ name: item.slice(prefix.length).split('/')[0], type: 'file' }));
      return { files };
    }
  };

  const listeners = {};
  window.Capacitor = {
    isNativePlatform: () => false,
    getPlatform: () => 'web',
    convertFileSrc: uri => uri,
    Plugins: {
      Filesystem,
      Share: { async share() { return {}; } },
      App: {
        addListener(event, handler) {
          (listeners[event] = listeners[event] || []).push(handler);
          return Promise.resolve({ remove() {} });
        },
        exitApp() {}
      },
      SystemBars: { async setStyle() {}, async show() {}, async hide() {} },
      // Records scheduled notifications so tests can inspect them.
      LocalNotifications: {
        scheduled: [],
        async checkPermissions() { return { display: 'granted' }; },
        async requestPermissions() { return { display: 'granted' }; },
        async createChannel() {},
        async cancel({ notifications }) {
          const ids = new Set(notifications.map(item => item.id));
          this.scheduled = this.scheduled.filter(item => !ids.has(item.id));
        },
        async schedule({ notifications }) {
          this.scheduled.push(...notifications);
          return { notifications: notifications.map(item => ({ id: item.id })) };
        }
      },
      StatusBar: { async setStyle() {}, async setBackgroundColor() {} }
    }
  };
})();
