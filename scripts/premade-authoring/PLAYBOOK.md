# Premade deck playbook

This is how to build one NCERT chapter into a premade deck for Erudite. It is written for a fresh chat that has no memory of earlier chapters. Read it once, then build.

## 0. Start here

When the owner says "read the playbook and continue":
1. **Read this whole file**, then **continue from the progress table** (section 9): chapters marked "Next" / "Old" / "Not started", in order, as many as you can do well.
2. **Copy the latest script for the same subject** (section 5 lists them). You may read any finished script to see how something was done.
3. **Per chapter:** unzip the book if needed (section 4) → crop figures per the subject rule (2.3) and check the montage → write the deck → check masks → package with `replace_deck.py` (old zip name, or `none.zip`) → commit, push and update the progress table in the same commit.
4. **Rules in one breath:**
   - **Owner update (Physics 12, 2026-09-29): quality over speed; anything is allowed** — crops, occlusion, animated/advanced HTML cards, NEET/JEE/CBSE-board style cards (“how it’s asked”), simplifying overcomplicated NCERT formulas. Sections 2.1/2.3 limits on animation and occlusion are superseded. Keep the warm-ink/paper taste for bespoke HTML except physics animations, which use the blueprint theme in `showcase_phy.py`. Always view the rendered result (`tools/cardview.py`, `maskcheck.py`).
   - Build fast, but every card must teach. Mostly text and cloze with the colour code (2.4).
   - Biology, inorganic and organic: strictly NCERT. Physics, physical chemistry and maths: teacher-style and exam-weighted (2.3, 2.6).
   - Figures: nearly all in biology/organic, selective elsewhere (2.3).
   - "How fancy" (2.1): intuition cards always where students get confused; animations only 1–2 in chapters that genuinely need them; bespoke cards use warm paper/ink, no neon.
   - 5–10% intuition, mnemonic and labelled correction cards; recompute before calling NCERT wrong, and never "correct" a symbol typo seen only in extracted text (section 4).
   - KaTeX `\( … \)` only outside clozes; never `\text{}` (section 6).
5. **Git:** if `index.lock` exists, wait a few seconds and retry. After each commit, check the old zip is gone and the push went through.
6. **Before stopping,** make the progress table say clearly what's next.

## 1. What the app is

**Erudite** is a spaced-repetition flashcard app for Indian students, mainly Class 9–12, NEET and JEE. It is built with Capacitor and ships on Android. Learners study decks in SRS or normal mode.

**Premade decks** are ready-made decks, one per NCERT chapter, that learners import from the in-app *Premade* store. How they are organised:
- Each deck lives in `premade-cards/<class>/<Subject>/<deck-id>/` as a `deck.json` plus a `media/` folder.
- A packaging script zips each deck and writes the `manifest.json` and `premade-cards/premade-catalog.json`.
- Netlify publishes `main`, so a pushed deck is live.

**Pricing** is applied automatically by `scripts/zip-premade-decks.js` from the chapter number:
- Chapters 1–3 of every subject in every class are free.
- Every later chapter gives 20 free sample cards, and Pro unlocks the rest.

Older decks named `erudite_*.zip` or `chapter_*_erudite.zip` were made by an earlier, weaker AI. We are rebuilding every chapter and replacing those zips.

## 2. The owner's rules

These rules come from the owner. Follow them exactly.

### 2.1 Build fast; spend effort where it teaches

The owner said: *"don't waste a lot of tokens onto making each and every card very good… we have to build the content faster."*

Card types, from cheapest to most expensive to build:

| Card type | Cost | When to use |
|---|---|---|
| Text Q/A (`basic`) and `cloze` | cheap | The bulk of every deck. |
| Colour, bold, italics, KaTeX in text | cheap | Use freely. |
| NCERT figure attached to a card (`termImage` / `definitionImage`) | cheap | Depends on the subject (section 2.3): nearly all in biology/organic, selective in physics/physical chemistry/maths. |
| `table_card` / `steps_card` / `quadrant_card` from `deckkit` | cheap (template) | Comparisons, classifications, worked examples. |
| Image occlusion (masking labels on a diagram) | moderate | **Only where needed:** key labelled diagrams students must be able to label, such as the heart, nephron or a cell. Not every figure. |
| Bespoke advanced HTML/SVG/animation (`showcase.py`) | expensive | Rarely: only when one visual truly explains a process better than text plus a figure. Most chapters need zero. |
| Royalty-free photo | moderate | Allowed when relevant and no NCERT figure exists. Use Unsplash or Pixabay only, with a licence that permits commercial use. Note the source in the script. |

**How fancy, in one line (resolves the older "creative freedom", "build fast" and "animated intuition" notes):** intuition cards (text + figure) always, wherever students get confused; animations only 1–2, in chapters that genuinely need them (most need none); bespoke HTML cards only rarely, and then in warm paper/ink themes (cream #fbf8f1, ink #1f2430, deep blue #1d5fd6), never neon glows or "cyber" styling.

### 2.2 Teach, don't just copy NCERT

The owner said: *"we are not just mimicking what NCERT says… use your own knowledge in between the cards… NCERT might say something wrong or outdated, you can correct it on the next card… intuitive examples… or a mnemonic."*

- **Add a few intuition cards:** "Why does…?", or an everyday analogy.
- **Add mnemonics** where students traditionally struggle.
- **When NCERT has an error, a typo, an outdated name or a misleading simplification,** keep NCERT's version on one card, because exams follow NCERT. Put the correction on the next card, labelled clearly, e.g. "Correction:" or "Update:".
- **Keep this to about 5–10% of the deck.** It seasons the deck; it is not the bulk.

### 2.3 How strictly to follow NCERT, by subject

| Subject | Style |
|---|---|
| Biology, inorganic chemistry, organic chemistry | **Strictly NCERT.** Use NCERT wording, examples, tables and figures. NEET asks line-by-line. |
| Physics, physical chemistry, maths | **Teacher-style and exam-weighted** (JEE/NEET/boards). Include formulas, derivation steps that matter, standard traps, units and worked examples. Skip fluff. |

**Animations and occlusion (owner, Physics 11 Ch 10, reaffirmed Physics 12):** the priority is to ship every chapter fast with great text, cloze and figure cards. Animated `showcase_phy` cards only rarely, where motion genuinely teaches something a figure cannot: most chapters need none, a few may need 1–2. Occlusion likewise only for diagrams students must label; skip it when in doubt. Both can be added later as upgrades. Spend the effort on card content, diagrams (cropped or `draw.py`), colour and styling instead.

**Which diagrams matter, by subject (owner, Physics 12):**

| Subject | Figures |
|---|---|
| Biology | **Core.** Crop nearly every figure; NEET asks from diagrams. Occlusion for key labelled diagrams. |
| Organic chemistry | **Core.** Crop nearly every structure and reaction scheme (one card each). |
| Inorganic chemistry | **Sometimes.** Structures, shapes, trend graphs and apparatus that are examined; skip decorative ones. |
| Physics, physical chemistry, maths | **Selective.** Not all diagrams matter. Use only figures that teach or are examined: field-line and equipotential patterns, ray diagrams, circuit symbols and circuits students must draw or analyse, key graphs (V–I, ρ–T, E–r), derivation geometry. Skip decorative figures, photos, and example/exercise setup pictures whose question can be stated in words; attach a setup figure only when the problem can’t be understood without it (e.g. a resistor network). |

**Physics figures (owner, Physics 11):** NCERT physics diagrams are often cluttered and use uncommon units or symbols. Use the notation and units students commonly use. Crop NCERT figures when they are clear; otherwise draw a clean one with `draw.py` (free-body diagrams, graphs, vectors, ray diagrams) or use a royalty-free image, but only if it is precise and correct.

**Exam weighting (owner):** for physics, physical chemistry and maths, web search for previous-year NEET/JEE/board question patterns is allowed, to decide what to emphasise and what to minimise. Stay within the chapter's syllabus.

### 2.4 Colour code

The helpers are in `deckkit.py`. Colour only the key word, not whole sentences.

| Helper | Colour | Use for |
|---|---|---|
| `T()` | blue | terms |
| `E()` | green | examples (`EI()` = italic organism) |
| `X()` | red | exceptions / "not" |
| `N()` | orange | numbers / values |
| `I()` | italics | genus and species names |

### 2.5 Card-writing style

- **One fact per card.**
- **Short questions,** e.g. "Function of X?" or "X vs Y?".
- **Answers of one line where possible.**
- **Cloze** for definitions, lists and sequences. Use `{{c1::…}}` and `{{c2::…}}`; each cN becomes a separate card.
- **Cover the whole chapter in section order,** including box items, tables and figure captions. Call `d.sec('10.2-mitosis')` before each section so it is tagged.
- **Size the deck to the chapter:** about 80–250 cards, which works out to about one card per examinable fact. Short chapters produce short decks; that's fine.
- **"Identify this" cards:** a figure on the front, with the name or labels on the back. Trim captions off crops when they would give the answer away.
- **Add a closing summary section** with one or two `table_card` comparisons.
- **Banned cards (owner):** nothing about the book or chapter itself: no "What is this chapter about?", "What will this chapter teach?", "Name of this chapter?", "What does section X cover?". Also nothing a student could answer without learning the topic. Every card must test physics, chemistry, biology or maths that could be examined. Motivational or historical fluff only when exams ask it (e.g. who discovered what, and when).

### 2.6 Maths

Maths is teacher-style and exam-weighted (JEE/boards), like physics. Only the pilot exists (`decks/math_ch03.py`, Class 11 Ch 3). Each chapter should have:
- **Standard formulas and results as cloze cards.** Write the formula in Unicode inside the cloze (`{{c1::sin²x + cos²x = 1}}`); use KaTeX only in `basic` cards or outside the cloze (section 6).
- **The patterns behind NCERT solved examples:** one card per pattern ("What is the trick in Example 5?"), not one card per example.
- **Common mistakes:** e.g. sign errors, forgotten domain restrictions, dividing by a variable that can be zero. Label them "Trap:".
- **A short "method" card per problem type:** "How do you solve …?" → 2–4 steps.
- **Step-by-step worked problems with one step hidden:** `steps_card` (set `hide` to the step students most often get wrong).
- **Figures:** selective (2.3): graphs, unit circles, Venn diagrams and geometry the question needs; skip the rest.

Folders: Class 11 decks go in `premade-cards/11th/Mathematics/` (manifest exists; only the Ch 3 pilot is there). Class 12 has **no** `Mathematics` folder yet: create `premade-cards/12th/Mathematics/`, run `npm run zip:premade` for the first chapter, then set the manifest `tags` (see 5.6). Deck id: `class11-mathematics-ch04-complex-numbers-and-quadratic-equations`; tags `['class-11', 'mathematics', 'ch-4']`.

## 3. Toolkit

Everything lives in `scripts/premade-authoring/`. Needs Python 3 with `pymupdf` and `Pillow`.

| File | Purpose |
|---|---|
| `deckkit.py` | `Deck`, colour helpers, `pad`, `rot`, `poly`, `table_card`, `steps_card`, `quadrant_card`, `mo_card`. |
| `showcase.py` | Themed bespoke HTML cards. Use rarely. |
| `showcase_phy.py` | Animated physics cards: `anim(deck, tag, q, svg_front, svg_back, note, term, definition, css)` on the blueprint theme, plus `keyframes(name, pts, dur)` to move an SVG group through points (projectiles, oscillations). Put each chapter's cards here under a `# Ch N` header; `front_only=` holds a static object that moves on the back. NCERT answer keys: `NCERT-pdfs/phy11/keph1an.pdf` (Ch 1–7) and `keph2an.pdf` (Ch 8–14). |
| `draw.py` | Self-drawn diagrams → `.webp` (`Fig(w,h)` with `arrow`, `line`, `poly`, `curve`, `axes`, `text`, `label`, `arc`; `save(media, name)`). PyMuPDF rasterises the SVG; it ignores `<marker>`, so `arrow` draws its own head. Check every drawn figure in the montage like a crop. |
| `figcrop.py` | `export(pdf, {name: (page, (x0,y0,x1,y1))}, outdir, long_side=1000)`. Saves `.webp` crops and **prints every printed word with its pixel box inside the crop**; use those boxes for occlusion masks. |
| `grid.py` | Rebuilds a tall multi-panel figure as a 2-column grid (phone-friendly). |
| `clean_pdf.py` | Opens an NCERT PDF with the watermark removed. |
| `replace_deck.py` | Retires the old zip, repackages, fixes the manifest. |
| `tools/extract.py <pdf>` | Chapter text into `.work/<name>.txt`. |
| `tools/figs.py <pdf>` | Lists figure bounding boxes (PDF points) and captions per page. **Start here** for crop rects. |
| `tools/sheet.py <pdf> <a-b> <name>` | Contact sheet of pages with a 50-pt grid, to eyeball rects. |
| `tools/ptgrid.py <pdf> <page> x0 y0 x1 y1 [step]` | Zoomed region with a fine point grid, to refine a rect. |
| `tools/pg.py <pdf> <pages> [dpi]` | Renders pages. |
| `tools/montage.py <media folder> <name>` | Montage of all crops, to check them in one look. |
| `tools/maskcheck.py <deck folder> <name>` | Draws every occlusion mask in red on its image. **Always check this before publishing.** |
| `tools/shot.py <deck.json> [filter] [page]` | **Fast visual check:** headless-Edge screenshot sheet (`.work/shot_N.png`, 8 faces per page, animations at their final state). Open the PNG with Read. Prefer this to cardview. |
| `tools/lint.py <deck.json>` | Flags `	ext{}`, KaTeX inside cloze/advanced HTML, unbalanced delimiters, oversized HTML, duplicate questions. Run before packaging. |
| `showcase_math.py` | Maths cards on the paper theme: `mcard`, `Plane` (graphs), `mkeyframes` from `showcase.py`; Venn/interval/number-line helpers per chapter under `# Maths N Ch M`. |
| `tools/cardview.py <deck.json> [filter]` | Renders advanced-HTML cards to `.work/cards.html` for a browser look. Only needed if you made bespoke HTML. Open it in the browser pane (file:// URL); cards sit in shadow roots, so `document.getAnimations()` cannot pause them — take screenshots at a few moments instead. |
| `tools/capacitor-stub.js` | Only for testing the full app in a browser. See the app-testing note in section 8. |

Tool output goes to `scripts/premade-authoring/.work/`, which is gitignored. Open the PNGs with the Read tool to look at them.

**Getting crop rects right (lesson learned):**
- Use `figs.py` for rough boxes. Its boxes can be too wide, because clipping paths make vector art report oversized bounds.
- Then run `ptgrid.py` on the region. It renders the region with the same clip mechanism `export` uses, so its grid labels are exact.
- Read the grid label values, not image pixels.
- Don't trust `sheet.py` for final numbers; it is for seeing the page layout.
- After cropping, always run `montage.py` and fix any clipped edges or stray neighbouring text.
- Figure labels are often part of the image, not PDF text. In that case `export` prints no word boxes: estimate mask positions from the montage (each tile is the image thumbnailed to fit 300×280, so tile scale = min(300 / width, 280 / height)) and confirm with `maskcheck.py`.

## 4. Source PDFs

NCERT books are in `NCERT-pdfs/` (gitignored) as zips. Unzip a book into its own folder when you start it (`unzip -o -j <zip> -d NCERT-pdfs/<folder>`), then check page 0 of each PDF for the chapter title. Already unzipped: `bio11/`, `bio12/`, `chem11/`, `chem12/`, `phy11/`, `phy12/`.

| Prefix | Book |
|---|---|
| `kebo1NN.pdf` | Class 11 Biology, chapter NN |
| `lebo1NN.pdf` | Class 12 Biology |
| `kech1NN` / `kech2NN` | Class 11 Chemistry parts 1 and 2 |
| `lech1NN` / `lech2NN` | Class 12 Chemistry parts 1 and 2 |
| `keph1NN` / `keph2NN` | Class 11 Physics |
| `leph1NN` / `leph2NN` | Class 12 Physics |
| `kemh1NN` | Class 11 Maths |
| `lemh1NN` / `lemh2NN` | Class 12 Maths |

Files ending in `ps` or `an` are prelims and answers. Some PDFs (e.g. `kech202`) extract as Caesar-shifted text (capitals and lowercase swapped, letters shifted by 29): decode each garbled word with lowercase→uppercase and other chars chr(ord+29). Check the chapter title on page 0.

**Symbol-font artifacts (lesson from Physics 12 Ch 7):** extracted text turns Greek symbols into Latin letters: **Ω → W**, **µ → m**, often θ → q, φ → F, ε → e, π → p. So "a 100 W resistor" or "15.0 mF" in `.work/*.txt` is really 100 Ω and 15.0 µF in the book. Before writing any "Correction:" card about a symbol, unit or letter, render that line (`tools/pg.py`, or a `page.get_pixmap(clip=…)`) and confirm the typo is really printed.

Still zipped (maths only): `maths11th.zip` → `maths11/`, `mathspart1 12th.zip` and `mathspart212th.zip` → `maths12/`. (`NCERT-pdfs/kemh103.pdf` is a loose copy of the Maths 11 Ch 3 pilot's PDF.)

## 5. Per-chapter workflow

The steps below use Biology 11 Ch 10 as the example. For each subject, copy the latest good script (and its `figures_…` twin):

| Subject | Reference script(s) |
|---|---|
| Biology | `bio12_ch13.py` (latest), `bio_ch09.py` (occlusion-heavy) |
| Organic chemistry | `chem12_ch06.py` (one card per reaction scheme) |
| Inorganic chemistry | `chem12_ch04.py`; animated intuition cards: `chem12_ch05.py` |
| Physical chemistry | `chem12_ch02.py` |
| Physics | `phy12_ch05.py` (latest), `phy12_ch01.py`; drawn figures in `figures_phy12_ch01.py` |
| Maths | `math_ch03.py` (pilot) plus section 2.6 |

1. **Read the chapter.**
   ```
   python scripts/premade-authoring/tools/extract.py NCERT-pdfs/bio11/kebo110.pdf
   ```
   Then read `.work/kebo110.txt`. The first page's heading gives the title.
2. **Find the figures.**
   ```
   python scripts/premade-authoring/tools/figs.py NCERT-pdfs/bio11/kebo110.pdf
   ```
   Use `sheet.py` or `ptgrid.py` for any figure whose bbox looks off.
3. **Crop.** Write `decks/figures_bio_ch10.py`, which calls `export(...)` into `premade-cards/11th/Biology/<deck-id>/media/`, and run it.
   - Run `montage.py` on the media folder to confirm each crop is whole, with no neighbouring text and no answer-leaking caption.
   - Keep the printed word boxes from the output for the masks.
4. **Write the deck.** Create `decks/bio_ch10.py`:
   ```python
   d = Deck('Chapter 10: Cell Cycle and Cell Division', 'Class 11', ['class-11', 'biology', 'ch-10'])
   d.description = 'one line, ~12 words, lists the chapter topics'
   d.sec('10.1-cell-cycle')
   d.basic(q, a)                                    # optional termImage= / definitionImage='media/x.webp'
   d.cloze('... {{c1::...}} ...', extra='optional back note')
   d.occlusion('Figure 10.2 · Mitosis', 'media/fig.webp', (w, h), [
       ('Label', pad([x, y, w, h], 4), True),       # True = label printed under the mask (see 6)
   ], guess='hide-all')                             # or 'hide-one'
   table_card(d, 'eyebrow', 'question?', [(label, answer_html, is_negative), ...], term='...')
   d.write(os.path.join(OUT, 'deck.json'))
   ```
   Deck id format: `class11-biology-ch10-cell-cycle-and-cell-division`. Name format: `Chapter 10: Title`.
5. **Check the masks.** Run the command below and look at the PNG. Every mask should cover its label fully and nothing else important.
   ```
   python scripts/premade-authoring/tools/maskcheck.py premade-cards/11th/Biology/<deck-id> chk10
   ```
6. **Package and replace the old zip.** Look up the old zip name in the subject folder; if the chapter never had an old deck, pass `none.zip` as the old name. If the subject folder has no `manifest.json` yet (a brand-new subject), `replace_deck.py` fails: run `npm run zip:premade` instead, then set the new manifest entry's `tags` (e.g. `["class-12", "physics", "neet"]`), since the script leaves them empty.
   ```
   python scripts/premade-authoring/replace_deck.py premade-cards/11th/Biology erudite_chapter_10_cell_cycle_and_cell_division.zip class11-biology-ch10-cell-cycle-and-cell-division
   ```
7. **Commit and push one chapter at a time,** so every chapter goes live as soon as it is done.
   - Stage the deck folder, its zip, the subject's `manifest.json`, `premade-cards/premade-catalog.json`, the two scripts and the removed old zip.
   - Never stage `android/*.gradle`.
   - Revert any file whose only change is a timestamp.
   ```
   git -c user.name="Sambhav Jain" -c user.email="eruditespartan@gmail.com" commit -m "Biology 11 Ch 10: Cell Cycle and Cell Division, rebuilt" -m "<the Co-Authored-By line your system prompt specifies>"
   git push
   ```
8. **Update the progress table** in section 9 of this file, in the same commit.

## 6. Rules the app imposes

Getting any of these wrong breaks cards on real phones.

**Math and cloze**
- **KaTeX:** use `\( … \)` inline in basic and cloze text.
  - Never put a cloze inside math, and don't wrap math in a cloze either: write cloze formulas in Unicode (`{{c1::v = v₀ + at}}`).
  - Avoid `\text{…}` in formulas: installed builds break it letter by letter. Keep words outside the math.
  - KaTeX does **not** render inside advanced HTML; use Unicode, `<sub>` and `<sup>` there.
- **Cloze extra:** `extra=` shows on the back. Use it for the "why" or the NCERT correction.

**Occlusion masks**
- `bboxPx` is `[x, y, w, h]` in pixels of the saved crop, and `size` must be the crop's actual pixel size (printed by `export`).
- Use `pad(box, 4–6)` around the word boxes from `export`, or `wbox(left, top, right, bottom, size)` to span a multi-word label.
- A label printed on a slant: `rot([x, y, w, h], degrees)`. A negative angle turns it anticlockwise.
- An odd shape: `poly([(x, y), …])`.
- Keep these rare: older app builds show them as plain boxes.
- **The printed flag:** `('Label', box, True)`, i.e. `labelInImage`, means the diagram prints that word under the mask, so the reveal doesn't repeat it.
  - Leave it off when the mask hides a letter like (a) or (b), or a leader line.
  - Leave it off when the answer says more than the figure prints.
- **Guess mode:** `hide-all` tests the whole diagram at once. `hide-one` makes one card per label. Prefer `hide-all` for diagrams with 4–10 labels.
- The occlusion card's `term` is the prompt shown on the front, e.g. `'Figure 10.2 · Stages of mitosis'`.

**Advanced HTML**
- It is display-only. Taps flip the card and scripts never run.
- CSS animations replay when that face comes into view.
- Inline SVG works: style it with classes, never `style=` attributes on SVG.
- Use paper, blueprint, chalkboard or lab backgrounds so the card reads on both themes.

**Media**
- Images are `.webp`, with a long side of about 1000 px.
- Keep a deck's media under a few MB.

## 7. Quality bar

Before committing, check all of the following:
- Every section of the chapter is covered.
- Figures follow the subject rule in section 2.3 (nearly all in biology/organic, selective in physics/physical chemistry/maths), with occlusion only where labelling is examinable.
- No leaking captions.
- All masks are verified with `maskcheck`.
- No `\text{}` in formulas.
- The description is set.
- There are a few intuition, mnemonic or correction cards.

Don't polish endlessly: move on to the next chapter.

## 8. Context tips for long runs

- **Work chapter by chapter** and commit each one. Nothing from a finished chapter needs to stay in memory.
- **Don't read back large deck scripts or `deck.json` files** you've already written. Read only the chapter text and tool output you need.
- **Rough chapters per chat:** biology 4–6; physics about 4 (numericals and recomputed exercises take longer); chemistry about 3–5; maths untested, probably 3–5. Hand off at a chapter boundary with the progress table updated.
- **Testing the app itself is rarely needed.** If you do:
  1. Run `npm run build:mobile`, then `git checkout -- mobile/css/icons.css`.
  2. Copy `tools/capacitor-stub.js` to `www/capacitor.js`.
  3. Serve `www/`.
  4. Delete the stub before any `npm run cap:sync`.

## 9. Progress

"Old" means an `erudite_*` or `*_erudite` zip still needs replacing. Update this table in every chapter commit.

**Status legend**
- **Done:** rebuilt with this playbook.
- **Pilot:** built early as a showcase and kept.

| Book | Chapters | Status |
|---|---|---|
| Biology 11 | 1–19 | Done (2 = pilot) — complete |
| Biology 12 | 1–13 — complete | Done (PDFs unzipped to `NCERT-pdfs/bio12/`) |
| Chemistry 11 | 1–3, 5–9 — complete | Done (PDFs unzipped to `NCERT-pdfs/chem11/`: Ch 1–6 = `kech101–106`, Ch 7–9 = `kech201–203`) |
| Chemistry 11 | 4 | Pilot |
| Chemistry 12 | 1–10 — complete | Done (PDFs unzipped to `NCERT-pdfs/chem12/`: Ch 1–5 = `lech101–105`, Ch 6–10 = `lech201–205`; decks go in `premade-cards/12th/Chemistry/`, scripts `chem12_chNN.py`) |
| Physics 11 | 1–3, 5–14 — complete | Done (PDFs unzipped to `NCERT-pdfs/phy11/`: Ch 1–7 = `keph101–107`, Ch 8–14 = `keph201–207`; answer keys `keph1an.pdf`, `keph2an.pdf`; decks in `premade-cards/11th/Physics/`, scripts `phy_chNN.py` + `figures_phy_chNN.py`, animations in `showcase_phy.py`, drawn figures via `draw.py`) |
| Physics 11 | 4 | Pilot |
| Physics 12 | 1–14 | Done: **the whole book is complete** (PDFs unzipped to `NCERT-pdfs/phy12/`: Ch 1–8 = `leph101–108`, Ch 9–14 = `leph201–206`; answer keys `leph1an.pdf`, `leph2an.pdf`; decks in `premade-cards/12th/Physics/` (manifest exists, so use `replace_deck.py premade-cards/12th/Physics none.zip <deck-id>`), scripts `phy12_chNN.py` + `figures_phy12_chNN.py`; animations in `showcase_phy.py` under the `# Physics 12 Ch N` headers) |
| Maths 11 | 1, 2, 4, 5, 6 | Done (PDFs unzipped to `NCERT-pdfs/maths11/`: Ch N = `kemh1NN`; decks in `premade-cards/11th/Mathematics/`, scripts `math11_chNN.py`, animations in `showcase_math.py`) |
| Maths 11 | 3 | Pilot |
| Maths 11 | 7–14 | Not started; **next: Ch 7** (Ch 4 and 5 note: this NCERT edition has no polar form / quadratic-equation section in Ch 4 and no two-variable inequalities in Ch 5, so those are added as "beyond the textbook" cards; Ch 4 note: this NCERT edition has no polar form or quadratic-equation section, so those are added as "beyond the textbook" cards; then revisit the Ch 3 pilot: add unit-circle/graph animations, how-it's-asked cards) |
| Maths 12 | all | Not started (PDFs unzipped to `NCERT-pdfs/maths12/`: Ch 1–6 = `lemh101–106`, Ch 7–13 = `lemh201–207`; answer keys `lemh1an.pdf`, `lemh2an.pdf`; create `premade-cards/12th/Mathematics/`) |

Suggested order: Biology 11, Biology 12, Chemistry 11 and 12, Physics 11 and 12, Maths 11 and 12.
