'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const { buildDeckPrompt } = require('../js/core/ai-prompt.js');

const base = {
  preset: 'revision',
  studiedState: 'yes',
  detailLevel: 'standard',
  mediaMode: 'important',
  examTarget: 'school',
  answerStyle: 'compact',
  cardMix: 'balanced',
  language: 'same',
  deckName: 'Chapter "6": Control & Coordination',
  className: '',
  avoidLazyCards: true,
  aiProvider: 'chatgpt',
  outputFormat: 'zip'
};

function exampleDeck(prompt, startMarker, endMarker) {
  const start = prompt.indexOf(startMarker) + startMarker.length;
  const end = prompt.indexOf(endMarker, start);
  return JSON.parse(prompt.slice(start, end));
}

test('ZIP example deck is valid JSON and escapes the deck name', () => {
  const prompt = buildDeckPrompt(base);
  const deck = exampleDeck(prompt, 'shaped like this:\n', '\n- media/');
  assert.equal(deck.name, base.deckName);
  assert.ok(deck.cards.some(card => card.type === 'image-occlusion'));
});

test('JSON example deck is valid JSON', () => {
  const prompt = buildDeckPrompt({ ...base, outputFormat: 'json' });
  const deck = exampleDeck(prompt, 'comments, or explanations.\n', '\n- Embedded');
  assert.equal(deck.version, 1);
});

test('every ZIP provider can fall back to a defined package-source format', () => {
  for (const aiProvider of ['chatgpt', 'claude', 'gemini', 'other']) {
    const prompt = buildDeckPrompt({ ...base, aiProvider });
    assert.match(prompt, /Start the reply with the line ERUDITE_PACKAGE_SOURCE_V1/, aiProvider);
    assert.match(prompt, /"encoding": "base64"/, aiProvider);
  }
});

test('occlusion protocol requires measured boxes and is omitted where it cannot work', () => {
  assert.match(buildDeckPrompt(base), /measured, never estimated by eye/);
  for (const variant of [{ aiProvider: 'gemini' }, { mediaMode: 'none' }, { outputFormat: 'txt' }, { outputFormat: 'html' }]) {
    const prompt = buildDeckPrompt({ ...base, ...variant });
    assert.doesNotMatch(prompt, /IMAGE OCCLUSION/, JSON.stringify(variant));
    assert.doesNotMatch(prompt, /"type":"image-occlusion"/, JSON.stringify(variant));
  }
});

test('TXT prompt never asks for features TXT import cannot carry', () => {
  const prompt = buildDeckPrompt({ ...base, outputFormat: 'txt' });
  assert.doesNotMatch(prompt, /\{\{c1::/);
  assert.doesNotMatch(prompt, /<b>/);
  assert.doesNotMatch(prompt, /Advanced HTML/);
});
