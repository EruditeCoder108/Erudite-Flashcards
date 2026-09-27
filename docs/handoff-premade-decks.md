# Handoff: premade NCERT decks for Erudite Flashcards 2.0

Start here in a new chat. This file is the brief, the quality bar, and the technical format for building the premade flashcard library.

## 1. Where things stand

- **App:** Erudite Flashcards (Android, Capacitor 8). Repo `EruditeCoder108/Erudite-Flashcards`, default branch `main`. Version 2.0 (versionCode 2) is merged into `main` and builds on GitHub Actions (`.github/workflows/android.yml`).
- **Play Store:** 1.0 (free) is live. 2.0 adds Erudite Pro and the redesign.
- **Monetisation model:** every premade chapter gives its **first 20 cards free**. Pro unlocks the full chapter, and existing sample decks get the rest of their cards. Ads come later, in 2.1. See `docs/monetization-plan.md` and `docs/release-2.0-checklist.md`.
- **Premade decks are not inside the APK.** They are static files on Netlify (`https://erudite-flashcards.netlify.app`, configured in `js/mobile/premade-content-config.js`). **Adding or fixing decks needs no app update**: commit to `main`, and Netlify rebuilds (`netlify.toml` runs `npm run zip:premade && npm run build:site`).

## 2. Goal and scope

Build the best NCERT flashcards a student has seen. A student should open a chapter and think "these are awesome".

**In scope now**
- Class 10: fix and upgrade what exists. It already has Biology, Chemistry, Physics, Mathematics, Economics, English, Geography, Hindi, History, and Politics.
- Class 11: Physics, Chemistry, Mathematics, Biology. Every chapter.
- Class 12: Physics, Chemistry, Mathematics, Biology. Every chapter.

**NCERT scope, with two levels of strictness** (owner decision):
- **Biology, inorganic chemistry, organic chemistry:** strictly NCERT, in NCERT's words and values.
- **Physics, physical chemistry, mathematics:** NCERT's topics, taught the way a good teacher would. Use the simplest form of each formula, intuitive explanations and simple diagrams; skip NCERT's over-complicated ones. Weight cards towards what NEET and JEE actually ask, and keep rarely asked material to a minimum. A few standard exam results just beyond the text are fine; tag them `exam-extra`.

NEET and JEE use the same Class 11 and 12 PCMB syllabus, so there are **no separate NEET/JEE decks** for now.

**Out of scope for now**
- Arts, humanities, and commerce for 11 and 12.
- SSC: show it as "Coming soon" (see section 7).
- NEET/JEE-only decks.

The owner will provide the NCERT PDF for each chapter.

## 3. Current inventory (as of this handoff)

| Class | Subject folder | Decks | Notes |
|---|---|---|---|
| 10th | Biology | 3 | Ch 6–8 only |
| 10th | Chemistry | 5 | |
| 10th | Physics | 3 | Ch 9–11 ("Remade") |
| 10th | Mathematics | 14 | |
| 10th | Economics, Geography, History, Politics, English, Hindi | 5–12 each | Review quality; no new work needed first |
| 11th | Biology | 19 | Mixed quality |
| 11th | Physical-Chemistry | 5 | Ch 1, 2, 5, … |
| 11th | Inorganic-Chemistry | 2 | Ch 3, 4 |
| 11th | Organic-Chemistry | 2 | Ch 8, 9 |
| 11th | Politics | 1 | Out of scope; leave |
| 11th, 12th | English | 20 | **These are copies of the SSC English decks. Remove them.** |
| 12th | Biology | 13 | "revised_erudite_v2" |
| 12th | organic-chemistry | 1 | Biomolecules only |
| ssc | english | 20 | Hide behind "Coming soon" |

Missing entirely:
- Physics 11 and 12, Mathematics 11 and 12.
- Most of Chemistry 11 and 12.
- Class 10 Biology chapters other than 6–8, and some Physics chapters.

Card types across all current decks: about 32.8k basic, 375 cloze, 96 image occlusion, 488 advanced HTML.

**Check the current NCERT (rationalised) chapter list for each subject before planning.** Chapter numbers changed after 2023, and the file names here use a mix of old and new numbers.

## 4. The quality bar (most important section)

The old AI-made decks fail in a predictable way: they are written to show the work was done, not to help a student remember. Every card must be written for the student.

### What a great card looks like
- **One idea per card.** If the answer has "and", ask whether it should be two cards.
- **Short answers.** Usually 1–12 words; a list of at most 4 items. Never a paragraph.
- **A question that has exactly one right answer.** "What does the medulla control?" is vague. "Which part of the brain controls blood pressure and salivation?" is precise.
- **NCERT's own words and values** for definitions, names, numbers, and units. No outside facts.
- **Natural student language.** Write it the way a good teacher would say it out loud.
- **Covers the whole chapter.** Every exam-relevant fact in the chapter ends up on some card: text, boxes, diagrams, tables, and in-text examples.
- **Follows the chapter's order,** and tags carry the section name so students can study one topic.

### Never write
- Meta text such as "According to NCERT…", "This card tests…", "Key concept:", "Important:", "Note that…", "Recall that…".
- Filler questions ("What is discussed in section 2.1?") or trivia that no exam asks.
- Long definitions copied as the answer. Break them into cloze cards or several precise questions.
- Two cards that ask the same thing in different words.
- Anything not in the NCERT chapter.

### How dense
A chapter becomes a deck of **roughly 50–150 cards**, depending on how much it contains (for example, Biological Classification is about 100–130). Aim for complete coverage in the fewest, sharpest cards, not a target number.

### Diagrams and tables: use judgement
- **Every labelled NCERT diagram that exams ask about → image occlusion.** Examples: neuron, human brain, reflex arc, nephron, flower LS, the heart, a dicot vs monocot seed, electric circuit symbols, ray diagrams, apparatus set-ups.
  - One card per figure, with every label as a mask.
  - Crop the figure tightly, remove the printed labels or cover them with masks, and export as `.webp`.
- **Important tables → cards.** Examples: hormones and their glands, the five kingdoms, periodic trends, SI units, s/p/d/f blocks, plant hormones and their functions.
  - Either one advanced HTML card that shows the table with one cell hidden, or several basic cards (one row each).
  - Tables that only give background detail (long data tables, historical lists nobody asks) are skipped or reduced to the one fact that matters.
- **In-text examples** that exams ask ("Example of a saprophytic fungus?") become their own cards.

### Styling that helps memory (not decoration)
Use one consistent colour code across all decks:
- **Blue:** terms.
- **Green:** examples.
- **Red:** exceptions and "not" facts.
- **Orange:** numbers and values.

Use bold only for the single word the answer hinges on. Use the colour on the key word, never whole sentences.

- **Formulas:** always use KaTeX (`\( … \)` inline, `\[ … \]` display). Chemistry formulas can use Unicode subscripts (H₂SO₄) in basic cards; `<sub>`/`<sup>` do not survive in basic cards (see section 5).
- **Advanced HTML cards** are for what plain text cannot show well:
  - comparison tables (mitosis vs meiosis, C3 vs C4);
  - step sequences (Krebs cycle steps, electron transport);
  - flow and process diagrams built from boxes and arrows;
  - worked numericals where one step is hidden;
  - reaction mechanisms laid out in stages;
  - small CSS animations, used sparingly, for processes (for example an arrow that moves through a cycle, or a step that highlights in turn).

  They must still be **one question with one answer**. A beautiful poster is not a flashcard.
- **Maths and Physics numericals:** cards for each formula (what it is, what each symbol means, units), each standard result, and the key step of each worked NCERT example. Put derivations in cloze form, one step blanked at a time.

### Card types and when to use them
| Type | Use for |
|---|---|
| basic | Most facts: question → short answer |
| cloze (`{{c1::…}}`) | Definitions, laws, ordered lists, sentence-shaped facts; one blank per idea (c1, c2… each become a card) |
| basic-reverse / `reverse: true` | Only true two-way pairs: term ↔ symbol, hormone ↔ gland, scientist ↔ discovery |
| image-occlusion | Labelled diagrams |
| advanced-html | Tables, comparisons, sequences, worked steps, visual processes |

### Pilot first
Before doing volume, build **one chapter per subject** (for example Biology 11 Ch 2 Biological Classification, Chemistry 11 Ch 4 Chemical Bonding, Physics 11 Ch 4 Laws of Motion, Maths 11 Ch 3 Trigonometric Functions). Have the owner review them in the app, agree the style, then scale.

## 5. Technical format

### Folder layout (source of truth)
```
premade-cards/<class>/<Subject>/<deck-id>/deck.json
premade-cards/<class>/<Subject>/<deck-id>/media/<files>.webp
```
- `npm run zip:premade` (see `scripts/zip-premade-decks.js`) zips each folder to `<deck-id>.zip`. It also counts the cards that will be created (cloze and occlusion expand into several cards) and updates that subject's `manifest.json` and the top-level `premade-catalog.json`.
- Use one consistent subject folder name per class: `Physics`, `Chemistry`, `Mathematics`, `Biology`.
- Chemistry is one `Chemistry` folder per class (merged in the pilot; the old physical, inorganic and organic folders are gone).
- Deck ids: `class11-biology-ch02-biological-classification`.
- Keep the unzipped folders in git so decks can be reviewed and edited. The zip is generated.

### manifest.json entry (per deck)
```json
{
  "id": "class11-biology-ch02-biological-classification",
  "name": "Chapter 2: Biological Classification",
  "description": "Five kingdoms, Monera to Fungi, viruses and lichens",
  "difficulty": "intermediate",
  "estimatedTime": "30 minutes",
  "fileName": "class11-biology-ch02-biological-classification.zip",
  "cardCount": 124,
  "tags": ["class-11", "biology", "neet"],
  "freeCards": 20
}
```
- `freeCards` overrides the default of 20 free cards.
- `"tier": "free"` makes a deck fully free. Use it for one showcase chapter per subject, so new users see the full quality.
- The zip script fills `cardCount` and `fileName`; it keeps the other fields you write.

### deck.json
```json
{ "version": 1, "name": "Chapter 2: Biological Classification", "className": "Class 11", "cards": [ ... ] }
```

**Basic card**
```json
{ "noteType": "basic",
  "term": "Which kingdom contains all prokaryotes?",
  "definition": "<span style=\"color:#3457f0\">Monera</span>",
  "tags": ["class-11","biology","ch-2","kingdom-monera"] }
```
- Rich text in `term`/`definition` allows only: `b strong i em u br p div ul ol li span mark code pre blockquote hr`.
- `span style="color:…"` is allowed, and so is `mark class="highlight-yellow|green|blue|pink"`.
- **No tables, `sub`, `sup`, or images inline.** Use `termImage`/`definitionImage` for a picture.
- KaTeX works: `$$…$$`, `\[…\]`, `\(…\)`.

**Cloze card**
```json
{ "noteType": "cloze", "text": "Nitrogen-fixing cyanobacteria have specialised cells called {{c1::heterocysts}}.", "tags": [...] }
```

**Image occlusion**
```json
{ "noteType": "image-occlusion", "term": "Structure of a neuron", "image": "media/neuron.webp",
  "occlusion": { "mode": "hide-one", "units": "px", "imageWidth": 900, "imageHeight": 620,
    "masks": [ { "shape": "rect", "bboxPx": [x, y, w, h], "answer": "Dendrite" } ] } }
```
- Mask boxes are measured in pixels of the final cropped image.
- The app turns each mask into its own card. **The mode is read from `occlusion.guessMode`**, not `mode`: `hide-all` (default) hides every label and asks one; `hide-one` hides only the asked label.
- The study front shows "Guess the hidden part", not the card's `term`.

**Advanced HTML**
```json
{ "noteType": "advanced-html", "term": "C3 vs C4: first stable product", "definition": "3-PGA vs OAA",
  "advancedHtml": { "frontHtml": "...", "backHtml": "...", "frontCss": "...", "backCss": "..." } }
```
- `term` and `definition` are still required. They show in lists and search, and serve as the fallback text.
- The canvas is 340 × 470 px, rendered in a shadow root.
- Allowed tags: `div section article header footer main h1–h6 p span strong b em i u small mark code pre blockquote br hr ul ol li table thead tbody tfoot tr th td img sup sub`.
- Allowed attributes: `class`, `id`, `img src/alt/width/height`, `td/th colspan/rowspan`.
- **Stripped:**
  - inline `style` attributes, so style with classes in `frontCss`/`backCss`;
  - scripts, forms, and buttons;
  - **SVG** (see section 7);
  - external URLs;
  - `position: fixed` and `z-index`.
- CSS `@keyframes` animations work. Limits: 30,000 characters of HTML and 18,000 of CSS per side.
- Support dark mode: the app is dark by default. Either design a paper-coloured card that looks right on both themes (like the existing examples), or use `@media (prefers-color-scheme: dark)`.
- **Check in the app** that `<img src="media/…">` inside advanced HTML resolves from the deck zip before relying on it. There is no existing example. The existing image cards use `termImage`/`image`.

The full list of what the importer accepts is in the in-app AI format guide (`mobile/index.html`, `#code-ai-format-guide`) and in `js/core/ai-prompt.js`, the copy-paste prompt users get. `js/core/schema.js` normalises cards on import. `mobile/js/mobile-study.js` holds the sanitisers (`sanitizeRichText`, `sanitizeAdvancedHtml`, `sanitizeAdvancedCss`).

### Images
- Crop NCERT figures from the PDF at good resolution. NCERT PDFs carry a "not to be republished" watermark on an optional-content layer; `scripts/premade-authoring/clean_pdf.py` blanks it before rendering. The owner chose to use NCERT figures.
- Export `.webp` at about 900–1200 px on the long side, and keep each file under about 200 KB.
- Name files after the figure: `fig_2_3_bacteria_shapes.webp`.

## 6. Process per chapter

1. Read the whole chapter PDF, including boxes, figure captions, tables, and in-text questions and examples.
2. Outline the sections, and list every figure and table with a keep/skip decision.
3. Write the cards, section by section.
4. Crop and mask the figures, and build the HTML tables.
5. Self-review against section 4. Check for:
   - duplicates;
   - vague questions;
   - long answers;
   - meta text;
   - anything not in NCERT;
   - facts in the chapter with no card.
6. Run `npm run zip:premade`, then import the zip in the app (Library → Import) and study 20 cards. Check the dark and light themes, and a 360 px wide screen.
7. Commit the deck folder, the zip, `manifest.json`, and `premade-catalog.json`. Netlify publishes on merge to `main`.

Suggested order:
1. Biology 11 and 12: the biggest NEET audience, and the existing decks give a base to upgrade.
2. Chemistry 11 and 12.
3. Physics 11 and 12.
4. Mathematics 11 and 12.
5. The Class 10 fixes: Biology and Physics gaps first.

## 7. Small app changes this work needs

These do need an app release, so bundle them into 2.0 before production if possible.
- **"Coming soon" for SSC.** Let a class in `premade-catalog.json` carry `"comingSoon": true`. The Premade screen then shows it greyed out with a "Coming soon" label instead of its decks.
- **Remove the SSC English copies** from `premade-cards/11th/English` and `premade-cards/12th/English`.
- **Optional: allow inline SVG in advanced HTML.** Add safe SVG elements (`svg g path line polyline polygon rect circle ellipse text tspan defs marker`) and presentational attributes, with no scripts, `foreignObject`, `href` or events. Line diagrams, arrows, and animated cycles become much easier. This is a sanitizer change in `mobile/js/mobile-study.js`. Keep it strict and add a test.
- KaTeX renders only in basic and cloze text, not inside advanced HTML (checked in the pilot).

## 8. Release plan (owner)

- **Unlock monetisation now, without waiting for the decks.** Play only lets you create in-app products after a build that contains billing has been uploaded. Build 2.0 includes RevenueCat, which adds the Play Billing permission.
  - Upload the signed 2.0 `.aab` to **Internal testing**. It does not need to go to production.
  - Then Monetize → Products opens. Continue with section 3 of `docs/release-2.0-checklist.md`: the products, RevenueCat, and the `goog_` key in `js/mobile/billing-config.js`.
- The key change needs one more app build: versionCode 3, or rebuild 2.0 before it leaves testing.
- Because decks live on Netlify, 2.0 can go to production as soon as the showcase chapters are good. More chapters appear for everyone the moment they are merged.

## 9. Questions to ask the owner at the start

1. Which chapter PDFs are ready, and in what order?
2. Keep Class 11 chemistry split into physical, inorganic, and organic, or merge it into one Chemistry folder?
3. Is the colour code in section 4 right?
4. Which chapter per subject should be the fully free showcase?
5. Should the SVG support in section 7 be added now?

## 10. Pilot status and lessons (September 2026)

Pilot decks built, all `"tier": "free"` showcases, and imported and studied in the app at 360 px:

| Deck | Notes | Cards | Card types |
|---|---|---|---|
| Biology 11 Ch 2 Biological Classification | 175 | 210 | basic, cloze, 6 image occlusion, 7 tables |
| Chemistry 11 Ch 4 Chemical Bonding | 139 | 151 | basic, cloze, tables, 3 MO diagrams |
| Physics 11 Ch 4 Laws of Motion | 76 | 79 | basic, cloze, tables, 3 worked examples |
| Mathematics 11 Ch 3 Trigonometric Functions | 69 | 70 | basic (KaTeX), tables, quadrant grid |

The authoring kit, one script per chapter, and the rules the app imposes are in `scripts/premade-authoring/README.md`. Read it before writing a deck. The main traps:
- a cloze inside `\( … \)` breaks KaTeX;
- `\text{}` inside KaTeX broke letter by letter in installed builds (CSS fixed in `mobile-study.css`, so it needs an app build);
- no SVG in decks until the SVG-capable build is widespread.

The chemistry PDF's text layer uses a shifted font encoding. Characters below 0x20 are digits shifted by −29; add 29 to recover them. Letters like c/p/v/x show up as F/S/Y/[.
