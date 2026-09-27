# Premade deck authoring kit

Python helpers used to write the premade NCERT decks. The `deck.json` files under `premade-cards/` are what ships; these scripts are how they were written, so later chapters stay consistent.

Requires Python 3 with `pymupdf` and `Pillow`.

| File | What it does |
|---|---|
| `deckkit.py` | Card builders (`basic`, `cloze`, `occlusion`, `advanced`), the colour code (`T` terms, `E` examples, `X` exceptions, `N` numbers), and advanced-HTML templates: `table_card` (hidden column), `mo_card` (MO diagram), `steps_card` (worked example with one step hidden), `quadrant_card` (2×2 grid). |
| `clean_pdf.py` | Opens an NCERT PDF with the watermark and header/footer layers blanked. |
| `figcrop.py` | Crops a figure at a given long side, saves `.webp`, and prints the pixel boxes of the printed labels (for masks). |
| `grid.py` | Rebuilds a tall multi-panel figure as a 2-column grid with a label strip under each panel (easier to read on a phone). |
| `showcase.py` | Themed advanced-HTML cards with inline SVG and CSS animation: blueprint (physics), chalkboard (maths), petri (biology), lab (chemistry), kingdom tiles. |
| `decks/*.py` | One script per chapter, plus `figures_*.py` that crop that chapter's NCERT figures. Run them, then `npm run zip:premade`. |

```bash
python scripts/premade-authoring/decks/bio_ch02.py
npm run zip:premade
```

Put the NCERT PDFs in `NCERT-pdfs/` (not committed).

## Rules the app imposes (learned from the pilot)

- **Never put a cloze inside a formula.** `{{c1::…}}` inside `\( … \)` breaks KaTeX, and the raw LaTeX shows.
- **Avoid `\text{…}` in formulas.** Until the `mobile-study.css` fix ships in an app build, installed apps split it one letter per line. Write words outside the math: `Bond order \(= \tfrac12(N_b - N_a)\)`.
- **KaTeX renders only in basic and cloze text,** not inside advanced HTML. Use Unicode, `<sub>` and `<sup>` there.
- **CSS animations play when their side comes into view.** The app rewinds a face's animations when the card becomes the front card and when it flips, so an animation on the answer side runs as the learner turns the card. Scripts never run, and taps always flip the card.
- **Inline SVG works in the 2.0 build** (shapes, text, markers; style it with classes, never `style=`). Builds before 2.0 strip it.
- **Occlusion mode is `occlusion.guessMode`** (`hide-all` or `hide-one`); the importer ignores `mode`. The card's `term` is the prompt on the front.
- **Masks can turn and take any shape.** `rot([x, y, w, h], degrees)` covers a label printed on a slant (the box is the unrotated box around the text, turned about its centre; negative is anticlockwise). `poly([(x, y), ...])` covers an odd shape with a polygon in image pixels. Both need the 2.0 app build; check the fit by drawing the shape on a copy of the crop.
- **`labelInImage: true` on a mask** (the `printed` option in `deckkit`) when the diagram already prints that label under the mask, so the reveal does not repeat it. Leave it off when the mask hides only a letter like (a) or when the answer adds something the figure does not print.
- **Use diagrams generously.** Crop, recrop, combine or redraw NCERT figures, or ask the owner for new assets: whatever makes the card clearest. Images on basic cards go in `termImage` / `definitionImage`.
- Advanced cards carry their own background (paper, blueprint, chalkboard, lab), so they read the same on the dark and light app themes.
