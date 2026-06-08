(function () {
  if (window.Sortable) return;

  window.Sortable = class SortableFallback {
    constructor() {
      console.warn('SortableJS is not installed. Card drag-reordering is disabled.');
    }
  };
})();
