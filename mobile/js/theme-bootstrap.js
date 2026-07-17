(function () {
  'use strict';

  try {
    if (window.localStorage.getItem('erudite-theme') === 'light') {
      document.documentElement.classList.add('theme-light');
    }
  } catch (_) {
    // Use the default theme when storage is unavailable.
  }
}());
