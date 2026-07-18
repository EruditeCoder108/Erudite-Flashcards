# Mobile Sound Map

All paths below are relative to the app project root. The app's **Sound Effects** setting mutes every one of these files.

| File | Current use | Replacement direction |
|---|---|---|
| `assets/flashcard-assets/click.mp3` | Standard Library/Create/Settings feedback: tabs, filters, modal choices, save/cancel controls, class selection, imports, and similar normal actions. It is the general UI sound. | Very short, soft wooden/plastic tick; no sharp high-frequency click. Keep it under about 80 ms. |
| `assets/audio/Star.mp3` | Only when a deck is pinned/favourited. Unpin uses the normal click. | Tiny bright sparkle/chime, around 150–250 ms. It should feel like a reward, not a notification. |
| `assets/flashcard-assets/flip-sound.mp3` | When the learner reveals the other side of a study card. | Soft card/paper flick, around 100–180 ms. It needs a little movement but should not resemble a page turn in an ebook. |
| `assets/flashcard-assets/Next-card.mp3` | When a learner moves forward/backward through normal study and when the next card appears after a rating. | Light forward whoosh/tick, around 80–140 ms. Keep the bass low so repeated reviews do not become tiring. |
| `assets/audio/success.mp3` | When any study session reaches its completion screen. | Warm, restrained two- or three-note confirmation, ideally 350–700 ms; this is the one sound allowed to feel celebratory. |
| `assets/flashcard-assets/import.mp3` | After successfully importing cards into the Creator, taking a premade deck, or creating a deck with Paste Import. | Short, confident completion sound, around 180–350 ms. It should communicate “the deck is safely here,” not sound like a reward. |

## Sounds worth adding later

- `assets/audio/milestone.mp3` — use only for meaningful milestones (for example a first completed deck or a streak goal), not for every completed study session. It should be distinct from `success.mp3`.

Do **not** add sounds for typing, scrolling, delete actions, validation errors, every SRS rating, or Android reminders. Those become noisy fast. For future reminders, use the system notification channel sound so the learner keeps device-level control.

## Implementation note

The general click sound now reuses a two-item audio pool instead of creating a new audio object on every tap. You can replace a file at the same path without changing code.
