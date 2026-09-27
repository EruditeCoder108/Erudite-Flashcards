// Redeems an Erudite Pro coupon code.
//
// POST { code, deviceId } -> { ok: true, remaining } or { ok: false, error }.
// Codes are stored only as SHA-256 hashes, so the repository never holds a
// usable code. Each code unlocks Pro on at most `maxUses` devices; the same
// device redeeming again does not use up another slot. Redemptions are kept
// in Netlify Blobs (store "coupons", one entry per code hash).
import { getStore } from '@netlify/blobs';
import { createHash } from 'node:crypto';

const COUPONS = {
  // Launch coupon, created 2026-09-27.
  '0c0ec05dbdbe25651b93bb7a5d5dc35c4fe0b0983ab5d4b87e12f04d6698fe30': { maxUses: 5 }
};

const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type'
};

function reply(status, body) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { ...CORS, 'Content-Type': 'application/json', 'Cache-Control': 'no-store' }
  });
}

export function normalizeCode(code) {
  return String(code || '').trim().toUpperCase().replace(/\s+/g, '');
}

export function hashCode(code) {
  return createHash('sha256').update(normalizeCode(code)).digest('hex');
}

export default async (req) => {
  if (req.method === 'OPTIONS') return new Response(null, { status: 204, headers: CORS });
  if (req.method !== 'POST') return reply(405, { ok: false, error: 'Use POST' });

  let body;
  try {
    body = await req.json();
  } catch (_) {
    return reply(400, { ok: false, error: 'Invalid request' });
  }
  const deviceId = String(body?.deviceId || '').slice(0, 80);
  if (!/^[\w-]{8,80}$/.test(deviceId)) return reply(400, { ok: false, error: 'Invalid request' });

  const hash = hashCode(body?.code);
  const coupon = COUPONS[hash];
  if (!coupon) return reply(404, { ok: false, error: 'That code is not valid' });

  const store = getStore({ name: 'coupons', consistency: 'strong' });
  // Compare-and-set so two phones redeeming at once cannot both take the last slot.
  for (let attempt = 0; attempt < 5; attempt++) {
    const existing = await store.getWithMetadata(hash, { type: 'json' });
    const devices = Array.isArray(existing?.data?.devices) ? existing.data.devices : [];
    if (devices.includes(deviceId)) {
      return reply(200, { ok: true, remaining: Math.max(0, coupon.maxUses - devices.length) });
    }
    if (devices.length >= coupon.maxUses) {
      return reply(410, { ok: false, error: 'This code has already been used the maximum number of times' });
    }
    const next = { devices: [...devices, deviceId], updatedAt: new Date().toISOString() };
    const condition = existing ? { onlyIfMatch: existing.etag } : { onlyIfNew: true };
    const result = await store.setJSON(hash, next, condition);
    if (result?.modified !== false) {
      return reply(200, { ok: true, remaining: coupon.maxUses - next.devices.length });
    }
  }
  return reply(409, { ok: false, error: 'Please try again' });
};

export const config = { path: '/api/redeem-coupon' };
