# Erudite Flashcards — God-Level Anki-Level SRS Roadmap

**Document status:** Final product + engineering roadmap  
**App:** Erudite Flashcards  
**Focus:** Spaced Repetition System, review infrastructure, Anki-level features, and future learning intelligence  
**Phase 1 status:** ✅ COMPLETE  
**Prepared for:** Sam Jain  
**Last updated:** 2026-06-19

---

# 1. Executive Summary

Erudite Flashcards is no longer just a normal flashcard app with SRS added on top. With Phase 1 marked complete, the app now has the foundation of a serious learning system.

The goal is not to copy Anki blindly. The goal is to reach Anki-level reliability while building a more modern, beautiful, mobile-first, student-friendly learning platform.

Anki is powerful because it is not only a scheduler. It is an ecosystem around memory:

- Scheduler
- Review queue
- Browser
- Undo
- Reset and repair tools
- Filtered/custom study
- Note/card model
- Templates
- HTML/CSS support
- Analytics
- Sync
- Add-ons

Erudite should keep the same seriousness, but hide complexity from beginners.

---

# 2. Product Philosophy

## 2.1 What Erudite Should Become

Erudite should feel like:

> Anki-level power, but easier, prettier, safer, and more intelligent.

The user should not need to understand SRS deeply to benefit from it.

The app should guide the user:

- What to study today
- What cards are weak
- Which decks are healthy
- Which cards need rewriting
- Whether the review workload is too high
- Whether the user is overloading themselves with new cards

## 2.2 What Erudite Should Avoid

Avoid becoming a confusing clone of Anki.

Do not expose 100 advanced settings to normal users.

Instead:

- Default mode should be simple
- Advanced mode should exist
- Dangerous operations should be protected
- Power tools should be available but not forced

---

# 3. Current System Status

## Phase 1: ✅ COMPLETE

Phase 1 is considered complete in this roadmap.

It includes:

- Review log infrastructure
- Undo stack
- Manual card actions
- Danger Zone deck-level SRS reset
- Progress decoupling between Normal Study and SRS Study
- Safer session behavior
- Better foundation for analytics

This means the app now has a professional SRS foundation.

---

# 4. Core SRS Behavior Rules

These rules define how the app should behave permanently.

## 4.1 Normal Study and SRS Study Must Be Separate

Normal Study and SRS Study are different systems.

Normal Study means:

> I am going through the deck in a chosen order.

SRS Study means:

> The memory system decides what is due.

Therefore, Normal Study progress must not control SRS Study.

### Correct Example

User studies in Normal Mode:

```text
Card 1
Card 2
...
Card 30
```

The app saves:

```text
Normal Study progress = 30/100
```

Then user switches to SRS Mode.

SRS Mode should not start at card 30.

It should build the due queue:

```text
Learning/Relearning due cards
↓
Mature Review due cards
↓
New cards if daily limit allows
```

SRS may start from card 4, card 82, card 13, or any due card.

When the user returns to Normal Mode, it should still resume at card 30.

## 4.2 Each Study Mode Owns Its Own Progress

Ideal progress object:

```js
progress = {
  normal: {
    forwardIndex: 30,
    backwardIndex: 0,
    randomOrder: [],
    randomIndex: 0
  },

  srs: {
    currentCardId: null,
    activeQueueCardIds: [],
    reviewedCardIdsThisSession: [],
    sessionId: null,
    sessionStartedAt: null
  },

  filtered: {
    filterId: null,
    currentCardId: null,
    activeQueueCardIds: [],
    isPreviewMode: false
  }
}
```

Never rely on one shared `currentCardIndex` as the source of truth.

A shared index can be used temporarily for rendering, but not for persistence.

## 4.3 SRS Queue Priority

SRS queue should always prioritize:

```text
1. Learning / Relearning cards due now
2. Mature Review cards due now
3. New cards allowed by daily limit
```

New cards should not appear before due reviews.

## 4.4 Learning Cards Must Bypass Review Limits

Learning and Relearning cards are fragile.

If they are due, they should show even if daily review limit is already reached.

Review limits should apply only to mature Review cards.

## 4.5 Again Cards Must Return

If a user presses Again, the card should not disappear.

The app should either:

- Reinsert the card after a few cards, or
- Preferably reinsert it when its next due time is reached

Ideal behavior:

```text
Again
↓
Update FSRS state
↓
Save review log
↓
Place card in short-term learning queue
↓
Show again when due
```

## 4.6 Undo Must Be Available

Misclicks happen.

If user presses Easy instead of Again, they must be able to undo.

Undo should restore:

- Card SRS state
- Review log status
- Queue order
- Session stats
- Reviewed IDs
- Current card position

## 4.7 Bury, Suspend, Reset, Set Due

Every serious SRS app needs card control tools.

In Study Mode, the More menu should include:

- Bury Card
- Suspend Card
- Reset Card
- Set Due Date
- View Card Info

In Browser Mode, these should exist as bulk actions.

## 4.8 Deck-Level SRS Reset

Users should be able to reset SRS for one deck/set.

This should not delete card content.

The app should offer:

```text
Reset scheduling only
Reset scheduling + delete review history
```

Recommended safer wording:

```text
Reset SRS Data for this Set
```

Confirmation should require typing:

```text
RESET
```

or the deck name.

Before reset, the app should create an automatic backup snapshot.

---

# 5. Phase Roadmap Overview

| Phase | Status | Main Purpose |
|---|---:|---|
| Phase 1 | ✅ COMPLETE | Safety, review logs, undo, manual actions, progress decoupling |
| Phase 2 | ⏳ NEXT | Browser power tools and bulk operations |
| Phase 3 | ⏳ NEXT | Analytics, heatmap, leech detection, deck health |
| Phase 4 | 🔜 LATER | Filtered decks and custom study |
| Phase 5 | 🔜 LATER | Note/card separation, templates, cloze, image occlusion |
| Phase 6 | 🔮 FUTURE | Rich content engine, HTML/CSS mode, Math, code, tables |
| Phase 7 | 🔮 FUTURE | Sync, backup, conflict handling |
| Phase 8 | 🔮 FUTURE | AI Deck Doctor and intelligent learning insights |
| Phase 9 | 🔮 FUTURE | Plugin/add-on ecosystem |

---

# 6. Phase 1 — ✅ COMPLETE

## 6.1 Purpose

Phase 1 turns the SRS from a simple scheduling feature into a reliable review system.

It fixes dangerous issues:

- Misclicks cannot be corrected
- Normal/SRS progress confusion
- No manual card actions
- No deck-level reset
- No proper review event logging

## 6.2 What Changed

### Review Log Added

The app now has or should have an append-only review log.

This means every review can be recorded as an event.

Example:

```text
Card reviewed
Rating: Good
Previous state: Learning
Next state: Review
Previous due: today
Next due: 3 days later
Reviewed at: timestamp
```

This enables:

- Undo
- Analytics
- Debugging
- Sync safety
- Session history
- Retention calculations

### Undo Added

User can undo the last review action.

Recommended keyboard shortcuts:

```text
Z
Ctrl + Z
```

### Manual Actions Added

From the Study page:

```text
More
↓
Bury Card
Suspend Card
Reset Card
Set Due Date
```

### Danger Zone Reset Added

Deck settings now include:

```text
Reset SRS Data...
```

This makes all cards in the set behave like New cards again.

Optional choices:

```text
Keep review history for analytics
Delete review history too
```

### Progress Decoupling Added

Normal Study and SRS Study now save separate progress.

Example:

```text
Normal Mode = card 30/100
SRS Mode = 12 due cards
```

SRS Mode does not start at Normal card 30.

Normal Mode does not get overwritten by SRS progress.

## 6.3 Phase 1 Acceptance Criteria

Phase 1 is complete only if all these pass:

- Normal Mode at card 30 stays card 30 after switching to SRS and back
- SRS Mode starts from due queue, not normal index
- Undo restores the previous card state
- Bury removes card until next rollover day
- Suspend removes card indefinitely
- Reset card returns it to New
- Set Due changes card due date
- Deck-level reset clears SRS state without deleting content
- Review logs are written for reviews
- SRS session progress survives closing and reopening
- Normal progress and SRS progress do not overwrite each other

---

# 7. Phase 2 — Browser Power Tools

## 7.1 Purpose

Phase 2 makes Erudite usable for large decks.

A student with 50 cards can manage manually.

A student with 5,000 cards needs power tools.

## 7.2 What It Adds

### Bulk Selection

Card Browser should support checkboxes:

```text
☑ Card 1
☑ Card 2
☑ Card 3
```

### Bulk Actions

Selected cards can be modified together:

```text
Bulk Suspend
Bulk Unsuspend
Bulk Reset SRS
Bulk Delete
Bulk Move to Set
Bulk Set Due Date
Bulk Add Tag
Bulk Remove Tag
```

### Filters

Browser should support quick filters:

```text
New
Learning
Review
Relearning
Due
Overdue
Suspended
Buried
Failed recently
Leeches
No tags
Has image
Has audio
```

## 7.3 Why It Matters

Without Browser Power Tools, a user must fix cards one by one.

That becomes painful and makes the app feel weak.

With Phase 2, Erudite becomes serious for real exam preparation.

## 7.4 Recommended UX

At bottom of browser:

```text
12 selected

Suspend | Reset SRS | Move | Delete | Set Due
```

Use a sticky action bar.

## 7.5 Phase 2 Acceptance Criteria

- User can select multiple cards
- User can select all visible cards
- Bulk suspend works
- Bulk reset SRS works
- Bulk delete works
- Bulk move works
- Bulk set due works
- Filters combine safely
- Browser remains fast with thousands of cards

---

# 8. Phase 3 — Analytics Dashboard

## 8.1 Purpose

Phase 3 makes learning visible.

Most users do not know if they are learning well.

Analytics should answer:

```text
Am I remembering?
Am I overloaded?
Which deck is weak?
Which cards are causing problems?
How much work is coming tomorrow?
```

## 8.2 Core Metrics

### True Retention

Retention should not be a simple pass rate on all cards.

Better:

```text
Mature card retention
Young card retention
Learning card success rate
```

Recommended windows:

```text
7 days
30 days
90 days
All time
```

### Workload Forecast

Show cards due in the next 30 days.

Example:

```text
Tomorrow: 82 cards
In 2 days: 64 cards
In 3 days: 91 cards
```

This helps users avoid overload.

### Review Time

Track:

```text
Study time today
Average seconds per card
Total review time this week
```

### Button Distribution

Show:

```text
Again: 12%
Hard: 18%
Good: 60%
Easy: 10%
```

If Again is too high, cards may be poor or workload too heavy.

If Easy is too high, deck may be too simple.

### Study Heatmap

A calendar heatmap showing daily activity.

Example:

```text
Light square = few reviews
Dark square = many reviews
Empty square = no study
```

Students love streak visibility.

## 8.3 Leech Detection

A leech is a card the user keeps failing.

Example:

```text
Failed 8 times
```

The app should flag it:

```text
⚠ Difficult Card
```

Options:

```text
Rewrite card
Suspend card
Tag as Leech
Move to Weak Cards
Ask AI to improve
```

## 8.4 Deck Health Score

Each deck should show a simple health summary:

```text
Biology
Retention: 91%
Workload: Healthy
Weak cards: 12
Backlog: Low
```

Bad deck example:

```text
Chemistry
Retention: 68%
Workload: Heavy
Weak cards: 41
Backlog: Growing
```

## 8.5 Phase 3 Acceptance Criteria

- Dashboard loads quickly
- Stats are calculated from review_log
- Retention shows meaningful categories
- Heatmap renders correctly
- Due forecast works
- Leech cards are detected
- Deck health summary is understandable
- Analytics are helpful, not overwhelming

---

# 9. Phase 4 — Filtered Decks and Custom Study

## 9.1 Purpose

Phase 4 gives users flexible study sessions outside normal daily SRS.

This is important for exams, revision, weak topics, and cramming.

## 9.2 Main Use Cases

### Failed Cards Today

```text
Study only cards I failed today
```

### Review Ahead

```text
Study cards due tomorrow today
```

### Tag-Based Study

```text
Study only cards tagged Photosynthesis
```

### Exam Cram

```text
Study all cards from this chapter regardless of due date
```

### Preview Mode

```text
Practice without changing SRS schedule
```

## 9.3 Two Important Modes

### Reschedule Mode

Answers affect FSRS schedule.

Use when user wants real reviews.

### Preview Mode

Answers do not affect long-term scheduling.

Use when user is just browsing/practicing.

## 9.4 Filtered Deck Examples

```text
Due cards from Biology
Failed cards from Chemistry
Cards tagged "Polity"
Cards due in next 3 days
Cards not reviewed in 30 days
```

## 9.5 Phase 4 Acceptance Criteria

- User can create temporary study sessions
- Filters work by tag, deck, due state, failed state
- Preview mode does not modify SRS
- Reschedule mode updates SRS properly
- Cards return to original deck after session
- Custom sessions do not corrupt normal or SRS progress

---

# 10. Phase 5 — Note/Card Separation

## 10.1 Purpose

Phase 5 is the biggest architecture upgrade.

It separates content from practice cards.

This is how Anki works internally.

## 10.2 Current Simple Model

```text
Card
- Front
- Back
- SRS state
```

Good for simple flashcards.

Limited for advanced learning.

## 10.3 Advanced Model

```text
Note
- Fields
- Tags
- Media

Card Templates
- Front template
- Back template

Generated Cards
- Each card has its own SRS state
```

## 10.4 Example

One note:

```text
Country: France
Capital: Paris
```

Can generate two cards:

```text
France → Paris
Paris → France
```

Both come from one note.

## 10.5 Why This Matters

This enables:

- Multiple cards from one note
- Cloze deletion
- Image occlusion
- Sibling burying
- Better editing
- Better browser
- Better import/export
- Templates

## 10.6 Sibling Burying

If two cards come from the same note, showing both on the same day may be cheating.

Example:

```text
France → Paris
Paris → France
```

If the user studies one, the other should be temporarily hidden.

This is sibling burying.

## 10.7 Cloze Deletion

User writes:

```text
The capital of France is {{c1::Paris}}.
```

Card shows:

```text
The capital of France is ____.
```

Back shows:

```text
The capital of France is Paris.
```

## 10.8 Image Occlusion

User uploads a diagram and hides labels.

Example:

```text
Heart diagram with hidden parts
```

The app generates cards asking for each hidden label.

Very useful for:

- Biology
- Anatomy
- Geography maps
- Diagrams
- Flowcharts

## 10.9 Phase 5 Warning

Do this late.

This phase is powerful but risky.

It affects:

- Database
- Creator
- Import/export
- Browser
- Study mode
- Sync
- Mobile
- Backup compatibility

Do not rush it.

## 10.10 Phase 5 Acceptance Criteria

- Old decks migrate safely
- Notes and cards both exist
- One note can generate multiple cards
- Editing a note updates generated cards
- Sibling burying works
- Cloze cards work
- Basic templates work
- Legacy simple cards still work

---

# 11. Phase 6 — Rich Content Engine

## 11.1 Purpose

Phase 6 makes cards more powerful and beautiful.

This is where HTML, CSS, math, tables, code, and rich formatting matter.

## 11.2 What Anki Allows

Anki allows HTML/CSS in cards and templates.

That means users can create:

- Bold text
- Colors
- Tables
- Images
- Audio
- Custom layouts
- Styled templates
- Cloze cards
- Complex visual cards

## 11.3 Why HTML Is Powerful

HTML allows cards like:

```html
<div class="formula-card">
  <h2>Ohm's Law</h2>
  <p><b>V = IR</b></p>
</div>
```

With CSS:

```css
.formula-card {
  font-size: 24px;
  text-align: center;
}
```

This gives users full design control.

## 11.4 Why HTML Is Dangerous

Arbitrary HTML can cause:

- Broken layouts
- Bad mobile rendering
- Security issues
- JavaScript abuse
- Inconsistent imports
- Cards that look different on different devices
- AI-generated malformed markup

## 11.5 Recommended Erudite Approach

Do not start with unrestricted HTML for everyone.

Use layers.

### Layer 1: Safe Rich Text

For normal users:

```text
Bold
Italic
Highlight
Color
Lists
Tables
Images
Audio
Math
Code blocks
```

Store as structured JSON or sanitized HTML.

### Layer 2: Markdown Support

Support simple authoring:

```markdown
**Bold**
*Italic*
==Highlight==
- list item
```

### Layer 3: Advanced HTML Mode

For power users only:

```text
Enable Advanced HTML/CSS Mode
```

Show warning:

```text
Advanced HTML can break cards or render differently on mobile.
```

### Layer 4: Templates

After Note/Card separation:

```text
Front Template
Back Template
Styling
```

## 11.6 Must-Have Rich Content Features

Before arbitrary HTML, build:

- Rich text editor
- Image support
- Audio support
- LaTeX/math support
- Code blocks
- Tables
- Syntax highlighting
- Cloze deletion
- Image occlusion

These cover most student needs.

## 11.7 Phase 6 Acceptance Criteria

- Rich text works on desktop and mobile
- Images render safely
- Audio works
- Math works
- Tables work
- Code blocks work
- HTML is sanitized
- Advanced HTML mode is optional
- Broken card recovery exists

---

# 12. Phase 7 — Sync, Backup, and Conflict Handling

## 12.1 Purpose

Users must trust that their data is safe.

A flashcard app can have beautiful UI, but if users fear data loss, they will not trust it.

## 12.2 Required Backup Types

### Full Collection Backup

Everything:

```text
Decks
Cards
Media
SRS data
Review logs
Settings
```

### Single Deck Export

One deck only.

Options:

```text
With SRS data
Without SRS data
With media
Without media
```

### Plain Text Export

For simple sharing.

Example:

```text
term;definition@term;definition
```

### Anki-Compatible Export Later

Long-term option:

```text
.apkg export/import
```

This is difficult but powerful.

## 12.3 Sync Requirements

Sync should handle:

- Desktop to mobile
- Mobile to desktop
- Conflict detection
- Deleted cards
- Edited cards
- Review logs
- Media files
- Offline-first usage

## 12.4 Conflict Types

### Easy Conflict

Review log from mobile and new card from desktop.

Auto-merge.

### Medium Conflict

Same card edited on two devices.

Ask user or choose latest safely.

### Hard Conflict

Database schema changed or deck deleted on one device.

Require clear recovery UI.

## 12.5 Required Recovery Options

```text
Force Upload
Force Download
Restore Backup
Export Emergency Backup
```

## 12.6 Phase 7 Acceptance Criteria

- Backups are reliable
- Restore preview exists
- Sync does not duplicate cards
- Sync does not resurrect deleted cards
- Review logs merge safely
- Media sync works
- User can recover from sync conflict

---

# 13. Phase 8 — AI Deck Doctor

## 13.1 Purpose

This is where Erudite can become better than Anki.

Anki gives tools.

Erudite can give diagnosis.

## 13.2 AI Deck Health

Example:

```text
Chemistry Deck

Retention: 72%
Problem: Too many cards are overloaded.
Recommendation: Split 18 cards.
```

## 13.3 Weak Card Diagnosis

AI can inspect failed cards and say:

```text
This card may be difficult because:
- It asks multiple facts at once
- The wording is vague
- The answer is too long
- Similar cards are interfering
```

## 13.4 Suggested Fixes

For a bad card:

```text
Original:
Explain photosynthesis.

Problem:
Too broad.

Suggested split:
1. What gas is absorbed during photosynthesis?
2. What gas is released during photosynthesis?
3. Which pigment captures sunlight?
```

## 13.5 Interference Detection

If two cards are too similar, the app can warn:

```text
These cards may confuse you.
```

Example:

```text
Article 32
Article 226
```

## 13.6 Workload Coaching

The app can say:

```text
You are adding 50 new cards daily but reviewing only 80 cards.
Your backlog will grow in 6 days.
Recommended new card limit: 20/day.
```

## 13.7 Phase 8 Acceptance Criteria

- AI identifies weak cards
- AI suggests better cards
- AI detects overloaded cards
- AI detects duplicate/confusing cards
- AI gives workload advice
- User can accept/reject AI suggestions
- No automatic destructive changes

---

# 14. Phase 9 — Plugin/Add-On Ecosystem

## 14.1 Purpose

Anki became powerful partly because of add-ons.

Erudite can support controlled extensions later.

## 14.2 Possible Plugin Types

- New card templates
- Importers
- Exporters
- Browser columns
- Study mode widgets
- Analytics panels
- AI processors
- Themes
- Custom review actions

## 14.3 Security Warning

Plugins are risky.

They may access user data.

Use permission system:

```text
Can read decks
Can modify cards
Can access files
Can access network
```

## 14.4 Recommended Approach

Do not build plugins early.

First stabilize:

- SRS
- Browser
- Analytics
- Sync
- Note/Card model

Then build plugins.

## 14.5 Phase 9 Acceptance Criteria

- Plugin manifest exists
- Permission system exists
- Plugin sandbox exists
- User can enable/disable plugins
- Broken plugin cannot destroy app
- Plugin API is versioned

---

# 15. HTML, CSS, and Templates Strategy

## 15.1 Should Erudite Support HTML?

Yes, eventually.

But not as the first rich content system.

## 15.2 Recommended Order

```text
1. Rich text editor
2. Markdown-style shortcuts
3. Math / LaTeX
4. Tables
5. Code blocks
6. Cloze
7. Image occlusion
8. Safe HTML
9. Advanced HTML/CSS templates
10. Optional JavaScript only if sandboxed
```

## 15.3 HTML Storage Strategy

Recommended:

```text
Store sanitized HTML or structured JSON.
Never store unsafe raw pasted HTML without cleaning.
```

## 15.4 Template Example

Fields:

```text
Question
Answer
Extra
```

Front Template:

```html
<div class="question">
  {{Question}}
</div>
```

Back Template:

```html
<div class="question">
  {{Question}}
</div>

<hr>

<div class="answer">
  {{Answer}}
</div>

<div class="extra">
  {{Extra}}
</div>
```

Styling:

```css
.question {
  font-size: 24px;
  font-weight: 700;
}

.answer {
  font-size: 22px;
}
```

## 15.5 Safe HTML Rules

Allow:

```text
b, strong, i, em, u
p, div, span
ul, ol, li
table, tr, td, th
img
audio
code, pre
math containers
```

Block:

```text
script
iframe
external remote scripts
dangerous event handlers like onclick
unknown embedded objects
```

---

# 16. Data Model Direction

## 16.1 Current Model

```text
Set
↓
Cards
```

## 16.2 Target Model

```text
Collection
↓
Deck / Set
↓
Notes
↓
Cards generated from templates
↓
Review logs
```

## 16.3 Review Log Model

Recommended fields:

```sql
CREATE TABLE IF NOT EXISTS review_log (
  id TEXT PRIMARY KEY,
  card_id TEXT NOT NULL,
  note_id TEXT,
  set_id TEXT NOT NULL,
  session_id TEXT,

  rating TEXT NOT NULL,

  previous_state TEXT,
  next_state TEXT,

  previous_due TEXT,
  next_due TEXT,

  previous_interval INTEGER,
  next_interval INTEGER,

  previous_stability REAL,
  next_stability REAL,

  previous_difficulty REAL,
  next_difficulty REAL,

  elapsed_ms INTEGER,
  reviewed_at INTEGER NOT NULL,

  is_preview INTEGER NOT NULL DEFAULT 0,
  undone INTEGER NOT NULL DEFAULT 0,
  undone_at INTEGER,

  device_id TEXT,
  rev INTEGER NOT NULL DEFAULT 1
);
```

Important: Prefer marking review logs as undone rather than deleting them.

## 16.4 Why Not Delete Undo Logs?

If undo deletes logs permanently, debugging and sync become harder.

Better:

```text
undone = 1
undone_at = timestamp
```

This preserves event history.

---

# 17. Safety and Danger Zone Rules

Any destructive feature should follow these rules.

## 17.1 Destructive Actions

- Delete deck
- Delete cards
- Reset SRS
- Delete review history
- Bulk reset
- Bulk suspend
- Restore backup
- Force sync upload/download

## 17.2 Required Protections

Use:

- Confirmation modal
- Clear warning
- Automatic backup
- Undo if possible
- Require typing RESET or deck name for dangerous actions

## 17.3 Good Warning Copy

```text
This will reset SRS scheduling for all cards in this set.
Your card text, images, tags, and deck structure will not be deleted.
Cards will behave like new cards again.
```

If deleting history:

```text
This will permanently remove review history used for analytics.
This cannot be fully recovered unless you restore a backup.
```

---

# 18. Ideal Study Page Behavior

## 18.1 Normal Mode

Shows:

```text
Card 30 / 100
```

Controls:

```text
Previous
Next
Flip
Shuffle if enabled
```

Saves normal progress only.

## 18.2 SRS Mode

Shows:

```text
12 due
Learning: 3
Review: 7
New: 2
```

Controls:

```text
Again
Hard
Good
Easy
Undo
More
```

Saves SRS progress only.

## 18.3 Filtered Mode

Shows:

```text
Filtered Study
Tag: Biology
Mode: Preview
```

Controls depend on preview/reschedule mode.

## 18.4 Completion Screens

### Normal Completion

```text
You completed this deck in Normal Study.
```

Do not say SRS is complete.

### SRS Completion

```text
All due reviews are complete.
Next review due: Tomorrow 8:30 AM
```

Do not change Normal Mode progress.

### Filtered Completion

```text
Filtered session complete.
Cards studied: 50
Schedule changed: No
```

if preview mode.

---

# 19. Better Than Anki Ideas

These are the features that can make Erudite feel more modern than Anki.

## 19.1 AI Deck Doctor

Diagnoses weak cards and suggests fixes.

## 19.2 Smart New Card Limit

App recommends new card limit based on workload.

Example:

```text
Recommended: 20 new cards/day
Reason: Your review load is rising.
```

## 19.3 Card Quality Score

Each card gets a quality estimate.

```text
Good card
Too broad
Too long
Ambiguous
Duplicate
Likely confusing
```

## 19.4 Auto-Split Long Cards

AI suggests splitting long answers into focused cards.

## 19.5 Exam Mode

Temporary high-intensity revision plan before exam.

## 19.6 Recovery Mode

For users with huge backlog.

```text
You have 2,300 overdue reviews.
Recommended recovery plan:
300/day for 8 days.
```

## 19.7 Beautiful Mobile Review

One-handed gestures:

```text
Swipe left = Again
Swipe down = Hard
Swipe right = Good
Swipe up = Easy
```

Optional.

## 19.8 Voice Review

User speaks answer, then reveals card.

Could be useful later.

## 19.9 Smart Notifications

Instead of random reminders:

```text
You have 42 reviews due.
Estimated time: 9 minutes.
Best time: before 9 PM.
```

---

# 20. Final Priority Order

## Immediate

Already complete:

```text
Phase 1
```

## Next Build

```text
Phase 2: Browser Power Tools
Phase 3: Analytics Dashboard
```

## Then

```text
Phase 4: Filtered Decks and Custom Study
```

## Later

```text
Phase 5: Note/Card Separation
Phase 6: Rich Content / HTML / Templates
```

## Future

```text
Phase 7: Sync
Phase 8: AI Deck Doctor
Phase 9: Plugins
```

---

# 21. Final Product Vision

Erudite should not become a clone of Anki.

It should become:

```text
A modern learning system with Anki-level seriousness,
beautiful review experience,
safe SRS infrastructure,
clear analytics,
AI-powered deck improvement,
and mobile-first simplicity.
```

Anki is powerful but intimidating.

Erudite can be powerful and welcoming.

The final goal:

```text
Beginner-friendly by default.
Powerful when needed.
Safe always.
Intelligent where Anki is silent.
```

---

# 22. Master Checklist

## Completed

- [x] Phase 1 marked complete
- [x] Review log infrastructure planned/implemented
- [x] Undo planned/implemented
- [x] Manual actions planned/implemented
- [x] Deck-level SRS reset planned/implemented
- [x] Normal/SRS progress decoupling planned/implemented
- [x] SRS queue behavior corrected
- [x] Learning/relearning priority corrected
- [x] Daily limit logic corrected

## Next

- [ ] Browser bulk selection
- [ ] Bulk suspend/unsuspend
- [ ] Bulk reset SRS
- [ ] Bulk delete
- [ ] Bulk move cards
- [ ] Bulk set due date
- [ ] Browser filters

## Analytics

- [ ] True retention
- [ ] Workload forecast
- [ ] Review time tracking
- [ ] Button distribution
- [ ] Study heatmap
- [ ] Leech detection
- [ ] Deck health score

## Custom Study

- [ ] Failed today session
- [ ] Review ahead
- [ ] Tag filtered study
- [ ] Exam cram mode
- [ ] Preview mode
- [ ] Reschedule mode

## Architecture

- [ ] Note/card separation
- [ ] Templates
- [ ] Cloze deletion
- [ ] Image occlusion
- [ ] Sibling burying

## Rich Content

- [ ] Rich text editor
- [ ] Markdown shortcuts
- [ ] Math/LaTeX
- [ ] Tables
- [ ] Code blocks
- [ ] Safe HTML
- [ ] Advanced HTML/CSS mode

## Future

- [ ] Sync
- [ ] Conflict handling
- [ ] AI Deck Doctor
- [ ] Plugin system
- [ ] Anki import/export compatibility

---

# 23. Closing Note

Phase 1 gives Erudite a serious SRS foundation.

Phases 2–4 make it powerful for real students.

Phases 5–6 make it architecturally Anki-level.

Phases 7–9 can make it better than Anki for modern users.

The most important rule going forward:

> Do not add features that make the app feel powerful but unsafe.  
> Every advanced feature must be reversible, understandable, and recoverable.
