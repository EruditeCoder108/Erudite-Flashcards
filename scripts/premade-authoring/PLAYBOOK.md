# Premade deck playbook

This is how to build one NCERT chapter into a premade deck for Erudite. It is written for a fresh chat that has no memory of earlier chapters. Read it once, then build.

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
| NCERT figure attached to a card (`termImage` / `definitionImage`) | cheap | Use freely. Crop every useful figure. |
| `table_card` / `steps_card` / `quadrant_card` from `deckkit` | cheap (template) | Comparisons, classifications, worked examples. |
| Image occlusion (masking labels on a diagram) | moderate | **Only where needed:** key labelled diagrams students must be able to label, such as the heart, nephron or a cell. Not every figure. |
| Bespoke advanced HTML/SVG/animation (`showcase.py`) | expensive | Rarely: only when one visual truly explains a process better than text plus a figure. Most chapters need zero. |
| Royalty-free photo | moderate | Allowed when relevant and no NCERT figure exists. Use Unsplash or Pixabay only, with a licence that permits commercial use. Note the source in the script. |

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

**Physics figures (owner, Physics 11):** NCERT physics diagrams are often cluttered and use uncommon units or symbols. Use the notation and units students commonly use. Crop NCERT figures when they are clear; otherwise draw a clean one with `draw.py` (free-body diagrams, graphs, vectors, ray diagrams) or use a royalty-free image, but only if it is precise and correct.

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

NCERT books are in `NCERT-pdfs/` (gitignored) as zips. Unzip a book into its own folder when you start it. For example, `bio11th.zip` and `bio12th.zip` have already been unzipped to `NCERT-pdfs/bio11/` and `NCERT-pdfs/bio12/`.

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

Remaining zips: `chempart11th`, `chempart211th`, `chempart112th`, `chempart212th`, `physics11th`, `physicspart2` (11th part 2), `physics12thpart1`, `physicspart212th`, `maths11th`, `mathspart1 12th`, `mathspart212th`.

## 5. Per-chapter workflow

Use Biology 11 Ch 10 as the example. Copy the shape of `decks/bio_ch09.py` and `decks/figures_bio_ch09.py`.

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
6. **Package and replace the old zip.** Look up the old zip name in the subject folder; if the chapter never had an old deck, run `npm run zip:premade` instead.
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
- Every figure worth knowing is used, with occlusion only where labelling is examinable.
- No leaking captions.
- All masks are verified with `maskcheck`.
- No `\text{}` in formulas.
- The description is set.
- There are a few intuition, mnemonic or correction cards.

Don't polish endlessly: move on to the next chapter.

## 8. Context tips for long runs

- **Work chapter by chapter** and commit each one. Nothing from a finished chapter needs to stay in memory.
- **Don't read back large deck scripts or `deck.json` files** you've already written. Read only the chapter text and tool output you need.
- **One chat can usually do about 4–6 biology chapters.** Hand off at a chapter boundary with the progress table updated.
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
| Physics 11 | 1–3, 5 | Done (PDFs unzipped to `NCERT-pdfs/phy11/`: Ch 1–7 = `keph101–107`, Ch 8–14 = `keph201–207`; decks in `premade-cards/11th/Physics/`, scripts `phy_chNN.py`; no old zips, so run `replace_deck.py premade-cards/11th/Physics none.zip <new id>`) |
| Physics 11 | 4 | Pilot |
| Physics 11 | 6–14 | **Next: Ch 6 Systems of Particles and Rotational Motion (`keph106`).** Teacher-style: formulas, `steps_card` numericals, units, traps; intuition cards and animated `showcase_phy.py` cards where concepts confuse students; self-drawn `draw.py` figures where NCERT's are cluttered. |
| Physics 12 | all | Not started |
| Maths 11 | 3 | Pilot |
| Maths 11 | others | Not started |
| Maths 12 | all | Not started |

Suggested order: Biology 11, Biology 12, Chemistry 11 and 12, Physics 11 and 12, Maths 11 and 12.
