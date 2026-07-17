(function () {
  'use strict';

  document.getElementById('privacy-back')?.addEventListener('click', () => {
    if (window.history.length > 1) {
      window.history.back();
      return;
    }
    window.location.assign('../index.html');
  });
}());
