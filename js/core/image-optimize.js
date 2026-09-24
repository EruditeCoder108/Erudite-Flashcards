(function (root, factory) {
  const api = factory();
  root.EruditeCore = root.EruditeCore || {};
  root.EruditeCore.images = api;
  root.EruditeImages = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
})(typeof globalThis !== 'undefined' ? globalThis : window, function () {
  // Camera photos arrive at 12+ megapixels. Decoding those on every card flip is
  // the main source of memory pressure and jank on low-end phones, so images are
  // resized and re-encoded once, on the way into the library. 2048 px keeps
  // diagram labels sharp when the learner pinch-zooms.
  const MAX_EDGE = 2048;
  const WEBP_QUALITY = 0.86;
  // Small images are left alone unless they are oversized in pixels.
  const SKIP_BELOW_BYTES = 180 * 1024;
  const PASSTHROUGH_MIMES = new Set(['image/gif', 'image/svg+xml']);

  function dataUrlMime(dataUrl) {
    const match = /^data:([^;,]+)[;,]/i.exec(String(dataUrl || ''));
    return match ? match[1].toLowerCase() : '';
  }

  function dataUrlByteLength(dataUrl) {
    const text = String(dataUrl || '');
    const comma = text.indexOf(',');
    if (comma < 0) return text.length;
    const base64 = text.slice(comma + 1);
    const padding = base64.endsWith('==') ? 2 : base64.endsWith('=') ? 1 : 0;
    return Math.max(0, Math.floor((base64.length * 3) / 4) - padding);
  }

  function readBlobAsDataUrl(blob) {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = () => resolve(reader.result);
      reader.onerror = () => reject(reader.error);
      reader.readAsDataURL(blob);
    });
  }

  async function dataUrlToBlob(dataUrl) {
    const response = await fetch(dataUrl);
    return response.blob();
  }

  async function decode(blob) {
    if (typeof createImageBitmap === 'function') {
      try {
        // Respect EXIF orientation so portrait photos are not stored sideways.
        return await createImageBitmap(blob, { imageOrientation: 'from-image' });
      } catch (_) {
        // Fall through to <img> decoding for formats createImageBitmap rejects.
      }
    }
    const url = URL.createObjectURL(blob);
    try {
      const image = new Image();
      image.decoding = 'async';
      image.src = url;
      await image.decode();
      return image;
    } finally {
      URL.revokeObjectURL(url);
    }
  }

  function sourceSize(source) {
    return {
      width: source.naturalWidth || source.width || 0,
      height: source.naturalHeight || source.height || 0
    };
  }

  function encode(source, width, height) {
    const canvas = document.createElement('canvas');
    canvas.width = width;
    canvas.height = height;
    const context = canvas.getContext('2d');
    context.imageSmoothingEnabled = true;
    context.imageSmoothingQuality = 'high';
    context.drawImage(source, 0, 0, width, height);
    const webp = canvas.toDataURL('image/webp', WEBP_QUALITY);
    // Android WebView encodes WebP; engines without an encoder fall back to PNG,
    // which keeps transparency for diagrams.
    if (webp.startsWith('data:image/webp')) return webp;
    return canvas.toDataURL('image/png');
  }

  /**
   * Resize and re-encode an image for storage.
   * @param {Blob|string} input A File/Blob or an image data URL.
   * @returns {Promise<{dataUrl: string, width: number, height: number, originalWidth: number, originalHeight: number, optimized: boolean}>}
   */
  async function prepareImage(input, options = {}) {
    const maxEdge = Number(options.maxEdge) || MAX_EDGE;
    const isBlob = typeof Blob !== 'undefined' && input instanceof Blob;
    const originalDataUrl = isBlob ? await readBlobAsDataUrl(input) : String(input || '');
    const mime = isBlob ? String(input.type || '').toLowerCase() : dataUrlMime(originalDataUrl);
    const passthrough = {
      dataUrl: originalDataUrl,
      width: 0,
      height: 0,
      originalWidth: 0,
      originalHeight: 0,
      optimized: false
    };
    if (!mime.startsWith('image/') || PASSTHROUGH_MIMES.has(mime) || typeof document === 'undefined') {
      return passthrough;
    }

    let source;
    try {
      source = await decode(isBlob ? input : await dataUrlToBlob(originalDataUrl));
    } catch (_) {
      return passthrough;
    }

    try {
      const { width, height } = sourceSize(source);
      if (!width || !height) return passthrough;
      const scale = Math.min(1, maxEdge / Math.max(width, height));
      const targetWidth = Math.max(1, Math.round(width * scale));
      const targetHeight = Math.max(1, Math.round(height * scale));
      const originalBytes = dataUrlByteLength(originalDataUrl);
      const result = {
        ...passthrough,
        width,
        height,
        originalWidth: width,
        originalHeight: height
      };
      if (scale === 1 && originalBytes <= SKIP_BELOW_BYTES) return result;

      const encoded = encode(source, targetWidth, targetHeight);
      // Keep the original when re-encoding would not save space at the same size.
      if (scale === 1 && dataUrlByteLength(encoded) >= originalBytes) return result;
      return {
        dataUrl: encoded,
        width: targetWidth,
        height: targetHeight,
        originalWidth: width,
        originalHeight: height,
        optimized: true
      };
    } catch (_) {
      return passthrough;
    } finally {
      source?.close?.();
    }
  }

  return {
    MAX_EDGE,
    prepareImage,
    dataUrlByteLength
  };
});
