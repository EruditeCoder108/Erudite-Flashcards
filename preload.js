const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('eruditeFlashcards', {
  listSets: () => ipcRenderer.invoke('flashcards:listSets'),
  getSet: (id) => ipcRenderer.invoke('flashcards:getSet', id),
  saveSet: (set) => ipcRenderer.invoke('flashcards:saveSet', set),
  replaceSets: (sets) => ipcRenderer.invoke('flashcards:replaceSets', sets),
  deleteSet: (id) => ipcRenderer.invoke('flashcards:deleteSet', id),
  listClasses: () => ipcRenderer.invoke('flashcards:listClasses'),
  saveClass: (classData) => ipcRenderer.invoke('flashcards:saveClass', classData),
  deleteClass: (classId) => ipcRenderer.invoke('flashcards:deleteClass', classId),
  exportBackup: () => ipcRenderer.invoke('flashcards:exportBackup'),
  importBackup: () => ipcRenderer.invoke('flashcards:importBackup'),
  exportDelimited: (format) => ipcRenderer.invoke('flashcards:exportDelimited', format),
  importDelimited: () => ipcRenderer.invoke('flashcards:importDelimited'),
  getProgress: (setId) => ipcRenderer.invoke('flashcards:getProgress', setId),
  saveProgress: (setId, value) => ipcRenderer.invoke('flashcards:saveProgress', setId, value),
  getSettings: () => ipcRenderer.invoke('flashcards:getSettings'),
  saveSettings: (settings) => ipcRenderer.invoke('flashcards:saveSettings', settings),
  getState: (key) => ipcRenderer.invoke('flashcards:getState', key),
  setState: (key, value) => ipcRenderer.invoke('flashcards:setState', key, value),
  removeState: (key) => ipcRenderer.invoke('flashcards:removeState', key),
  saveImage: (dataUrl, meta) => ipcRenderer.invoke('flashcards:saveImage', dataUrl, meta),
  deleteImage: (fileUrl) => ipcRenderer.invoke('flashcards:deleteImage', fileUrl),
  saveFont: (dataUrl, meta) => ipcRenderer.invoke('flashcards:saveFont', dataUrl, meta),
  listPremadeSets: (classId, subjectId) => ipcRenderer.invoke('flashcards:listPremadeSets', classId, subjectId),
  getPremadeSet: (classId, subjectId, fileName) => ipcRenderer.invoke('flashcards:getPremadeSet', classId, subjectId, fileName),
  getDiagnostics: () => ipcRenderer.invoke('flashcards:getDiagnostics'),
  onMenuCommand: (callback) => {
    const listener = (_event, command) => callback(command);
    ipcRenderer.on('app:menu-command', listener);
    return () => ipcRenderer.removeListener('app:menu-command', listener);
  }
});
