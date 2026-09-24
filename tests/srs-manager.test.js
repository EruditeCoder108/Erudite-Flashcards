'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const { loadCore } = require('./helpers');

const { srsManager } = loadCore();

function newCard(id) {
  return { id, term: `t-${id}`, definition: `d-${id}` };
}

function reviewedCard(id, daysAgo, stability) {
  const last = new Date(Date.now() - daysAgo * 86400000);
  return {
    id,
    srs: {
      state: 'Review',
      stability,
      difficulty: 5,
      reps: 6,
      lapses: 0,
      scheduledDays: daysAgo,
      elapsedDays: daysAgo,
      learningSteps: 0,
      lastReview: last.toISOString(),
      due: new Date(Date.now() - 3600000).toISOString()
    }
  };
}

test('rating preview matches the interval that is actually saved', () => {
  for (let index = 0; index < 40; index += 1) {
    const card = reviewedCard(`card-${index}`, 20 + index, 30 + index * 3);
    const previews = srsManager.getRatingPreviews(card);
    for (const rating of ['Hard', 'Good', 'Easy']) {
      const reviewed = srsManager.reviewCard(card, rating);
      assert.equal(
        reviewed.srs.scheduledDays,
        previews[rating].scheduledDays,
        `${rating} preview differs for ${card.id}`
      );
    }
  }
});

test('blank deck new-card limit inherits the app default', () => {
  srsManager.setDefaults({ newCardsPerDay: 20 });
  const cards = Array.from({ length: 150 }, (_, index) => newCard(`n-${index}`));
  assert.equal(srsManager.getDueCards(cards, { settings: {} }).length, 20);
  assert.equal(srsManager.getDueCards(cards, { settings: { newCardsPerDay: 5 } }).length, 5);
  assert.equal(srsManager.getDueCards(cards, { settings: { newCardsPerDay: 0 } }).length, 0);
  srsManager.setDefaults({ newCardsPerDay: 50 });
  assert.equal(srsManager.getDueCards(cards, { settings: { newCardsPerDay: null } }).length, 50);
  srsManager.setDefaults({ newCardsPerDay: 20 });
});

test('new cards introduced today count against the daily limit', () => {
  srsManager.setDefaults({ newCardsPerDay: 10 });
  const now = new Date().toISOString();
  const cards = Array.from({ length: 30 }, (_, index) => newCard(`m-${index}`));
  for (let index = 0; index < 4; index += 1) {
    cards[index] = {
      ...srsManager.reviewCard(cards[index], 'Good'),
      reviewHistory: [{ reviewedAt: now, rating: 'Good', previousState: 'New' }]
    };
  }
  const due = srsManager.getDueCards(cards, { settings: {} });
  const newDue = due.filter(card => !card.srs || card.srs.state === 'New');
  assert.equal(newDue.length, 6);
  srsManager.setDefaults({ newCardsPerDay: 20 });
});

test('learning cards are never capped and come before new cards', () => {
  const learning = srsManager.reviewCard(newCard('learn'), 'Again');
  learning.srs.due = new Date(Date.now() - 1000).toISOString();
  const due = srsManager.getDueCards([newCard('a'), learning], { settings: { newCardsPerDay: 0 } });
  assert.deepEqual(due.map(card => card.id), ['learn']);
});

test('retention counts only reviews of graduated cards and weights decks by volume', () => {
  const { core } = loadCore();
  const now = new Date();
  const at = new Date(now.getTime() - 86400000).toISOString();
  const review = (rating, previousState) => ({ reviewedAt: at, rating, previousState });
  const bigDeck = {
    cards: [{
      id: 'a',
      reviewHistory: [
        ...Array.from({ length: 9 }, () => review('Good', 'Review')),
        review('Again', 'Review'),
        ...Array.from({ length: 20 }, () => review('Again', 'Learning'))
      ]
    }]
  };
  const tinyDeck = { cards: [{ id: 'b', reviewHistory: [review('Again', 'Review')] }] };
  assert.equal(core.stats.getSetSrsStats(bigDeck, now).retention, 90);
  // 9 remembered of 11 mature reviews overall, not the average of 90% and 0%.
  assert.equal(core.stats.getLibraryStats([bigDeck, tinyDeck], [], now).retention, 82);
});
