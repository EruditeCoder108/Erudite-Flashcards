(function (root) {
  'use strict';

  // One source of truth for Erudite Pro. Everything that is gated (premade
  // decks now; ads and Pro-only features later) asks isPro() and listens with
  // onChange(). Purchases go through Google Play via RevenueCat. The last known
  // state is cached so Pro keeps working offline.

  const CACHE_KEY = 'erudite-pro-entitlement-v1';
  const DEBUG_KEY = 'erudite-pro-debug';
  // A redeemed coupon is stored apart from the Play entitlement, so a Play
  // check that finds no purchase never switches coupon Pro off.
  const COUPON_KEY = 'erudite-pro-coupon-v1';
  const DEVICE_KEY = 'erudite-device-id';
  // An offline device keeps a cached Pro entitlement for this long past its
  // expiry before falling back to free, so a flaky connection never locks a
  // paying student out mid-revision.
  const OFFLINE_GRACE_MS = 3 * 24 * 60 * 60 * 1000;

  const listeners = new Set();
  let state = readCache();
  let configured = false;
  let configuring = null;

  function config() {
    return root.ERUDITE_BILLING || {};
  }

  function plugin() {
    return root.Capacitor?.Plugins?.Purchases || null;
  }

  function isNativeAndroid() {
    try {
      return root.Capacitor?.getPlatform?.() === 'android';
    } catch (_) {
      return false;
    }
  }

  function readCache() {
    try {
      const saved = JSON.parse(root.localStorage.getItem(CACHE_KEY) || 'null');
      if (saved && typeof saved === 'object') return saved;
    } catch (_) {
      // Fall through to the free state.
    }
    return { active: false, productId: null, expiresAt: null, checkedAt: 0 };
  }

  function writeCache(next) {
    try {
      root.localStorage.setItem(CACHE_KEY, JSON.stringify(next));
    } catch (_) {
      // Storage is optional; the store re-reports the entitlement on launch.
    }
  }

  // Development builds in a browser can preview Pro with
  // localStorage['erudite-pro-debug'] = 'on'. Ignored on Android.
  function debugPro() {
    if (isNativeAndroid()) return false;
    try {
      return root.localStorage.getItem(DEBUG_KEY) === 'on';
    } catch (_) {
      return false;
    }
  }

  function couponPro() {
    try {
      const saved = JSON.parse(root.localStorage.getItem(COUPON_KEY) || 'null');
      return Boolean(saved?.active);
    } catch (_) {
      return false;
    }
  }

  function isPro() {
    if (debugPro()) return true;
    if (couponPro()) return true;
    if (!state.active) return false;
    if (!state.expiresAt) return true;
    return Date.now() < Number(state.expiresAt) + OFFLINE_GRACE_MS;
  }

  function setState(next) {
    const wasPro = isPro();
    state = { ...state, ...next, checkedAt: Date.now() };
    writeCache(state);
    const nowPro = isPro();
    if (wasPro !== nowPro) listeners.forEach(listener => {
      try {
        listener(nowPro);
      } catch (error) {
        console.warn('[entitlements] listener failed:', error);
      }
    });
  }

  function applyCustomerInfo(customerInfo) {
    const entitlement = customerInfo?.entitlements?.active?.[config().entitlementId || 'pro'];
    setState({
      active: Boolean(entitlement),
      productId: entitlement?.productIdentifier || null,
      expiresAt: entitlement?.expirationDate ? new Date(entitlement.expirationDate).getTime() : null
    });
  }

  /** True when Google Play billing can be used in this build. */
  function isAvailable() {
    return Boolean(plugin() && isNativeAndroid() && config().revenueCatAndroidKey);
  }

  async function init() {
    if (configured || !isAvailable()) return isPro();
    if (configuring) return configuring;
    configuring = (async () => {
      const purchases = plugin();
      try {
        await purchases.configure({ apiKey: config().revenueCatAndroidKey });
        configured = true;
        await purchases.addCustomerInfoUpdateListener?.(customerInfo => applyCustomerInfo(customerInfo));
        const { customerInfo } = await purchases.getCustomerInfo();
        applyCustomerInfo(customerInfo);
      } catch (error) {
        console.warn('[entitlements] could not reach billing:', error);
      }
      return isPro();
    })();
    return configuring;
  }

  function periodLabel(item) {
    const type = String(item?.packageType || '').toUpperCase();
    if (type === 'ANNUAL') return 'year';
    if (type === 'MONTHLY') return 'month';
    if (type === 'LIFETIME') return 'lifetime';
    return '';
  }

  /** Packages from the current RevenueCat offering, cheapest period first. */
  async function getPackages() {
    await init();
    if (!configured) return [];
    try {
      const offerings = await plugin().getOfferings();
      const packages = offerings?.current?.availablePackages || [];
      const order = { ANNUAL: 0, MONTHLY: 1, LIFETIME: 2 };
      return packages
        .map(item => ({
          id: item.identifier,
          period: periodLabel(item),
          type: String(item.packageType || '').toUpperCase(),
          price: item.product?.priceString || '',
          amount: Number(item.product?.price) || 0,
          title: item.product?.title || '',
          raw: item
        }))
        .sort((a, b) => (order[a.type] ?? 9) - (order[b.type] ?? 9));
    } catch (error) {
      console.warn('[entitlements] could not load offerings:', error);
      return [];
    }
  }

  /**
   * Buy a package. Resolves { ok: true } on success, { cancelled: true } when
   * the learner backs out of the Play sheet, or { error } otherwise.
   */
  async function purchase(packageItem) {
    if (!configured || !packageItem?.raw) return { error: 'Billing is not available' };
    try {
      const { customerInfo } = await plugin().purchasePackage({ aPackage: packageItem.raw });
      applyCustomerInfo(customerInfo);
      return isPro() ? { ok: true } : { error: 'Purchase did not unlock Pro' };
    } catch (error) {
      if (error?.userCancelled || String(error?.code) === '1') return { cancelled: true };
      return { error: error?.message || 'Purchase failed' };
    }
  }

  async function restore() {
    await init();
    if (!configured) return { error: 'Billing is not available' };
    try {
      const { customerInfo } = await plugin().restorePurchases();
      applyCustomerInfo(customerInfo);
      return { ok: true, pro: isPro() };
    } catch (error) {
      return { error: error?.message || 'Restore failed' };
    }
  }

  function deviceId() {
    try {
      let id = root.localStorage.getItem(DEVICE_KEY);
      if (!id) {
        id = root.crypto?.randomUUID?.() || `d-${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 12)}`;
        root.localStorage.setItem(DEVICE_KEY, id);
      }
      return id;
    } catch (_) {
      return `d-${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 12)}`;
    }
  }

  function couponUrl() {
    const base = String(root.ERUDITE_PREMADE_CONTENT?.baseUrl || '').replace(/\/+$/, '');
    return /^https:\/\//i.test(base) ? `${base}/api/redeem-coupon` : '';
  }

  /** Redeem a Pro coupon code. Resolves { ok: true } or { error }. */
  async function redeemCoupon(code) {
    const clean = String(code || '').trim();
    if (!clean) return { error: 'Enter a code' };
    const url = couponUrl();
    if (!url) return { error: 'Coupons are not available in this build' };
    let result;
    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code: clean, deviceId: deviceId() })
      });
      result = await response.json().catch(() => ({}));
    } catch (_) {
      return { error: 'Could not reach the server. Check your connection.' };
    }
    if (!result?.ok) return { error: result?.error || 'That code is not valid' };
    const wasPro = isPro();
    try {
      root.localStorage.setItem(COUPON_KEY, JSON.stringify({ active: true, redeemedAt: Date.now() }));
    } catch (_) {
      return { error: 'Could not save Pro on this device' };
    }
    if (!wasPro) listeners.forEach(listener => {
      try {
        listener(true);
      } catch (error) {
        console.warn('[entitlements] listener failed:', error);
      }
    });
    return { ok: true };
  }

  function onChange(listener) {
    listeners.add(listener);
    return () => listeners.delete(listener);
  }

  const api = { init, isPro, isCouponPro: couponPro, isAvailable, getPackages, purchase, restore, redeemCoupon, onChange };
  root.EruditeEntitlements = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
}(typeof globalThis !== 'undefined' ? globalThis : window));
