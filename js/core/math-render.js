(function (root, factory) {
  const api = factory();
  root.EruditeCore = root.EruditeCore || {};
  root.EruditeCore.math = api;
  root.EruditeMath = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
})(typeof globalThis !== 'undefined' ? globalThis : window, function () {
  const delimiters = [
    { left: '$$', right: '$$', display: true },
    { left: '\\[', right: '\\]', display: true },
    { left: '\\(', right: '\\)', display: false }
  ];

  function renderMath(root) {
    if (!root || typeof renderMathInElement !== 'function') return false;
    try {
      renderMathInElement(root, {
        delimiters,
        throwOnError: false,
        strict: 'ignore',
        trust: false,
        ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
      });
      return true;
    } catch (error) {
      console.warn('[math] render failed:', error);
      return false;
    }
  }

  function inlineFormula(raw) {
    const value = String(raw || '').trim();
    return value ? `\\(${value}\\)` : '';
  }

  function blockFormula(raw) {
    const value = String(raw || '').trim();
    return value ? `\\[${value}\\]` : '';
  }

  return {
    delimiters,
    renderMath,
    inlineFormula,
    blockFormula
  };
});
