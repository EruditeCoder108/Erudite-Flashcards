# Premade deck authoring kit

Python helpers used to write the premade NCERT decks. The `deck.json` files under `premade-cards/` are what ships; these scripts are how they were written, so later chapters stay consistent.

Requires Python 3 with `pymupdf` and `Pillow`.

| File | What it does |
|---|---|
| `deckkit.py` | Card builders (`basic`, `cloze`, `occlusion`, `advanced`), the colour code (`T` terms, `E` examples, `X` exceptions, `N` numbers), and advanced-HTML templates: `table_card` (hidden column), `mo_card` (MO diagram), `steps_card` (worked example with one step hidden), `quadrant_card` (2×2 grid). |
| `clean_pdf.py` | Opens an NCERT PDF with the watermark and header/footer layers blanked. |
| `figcrop.py` | Crops a figure at a given long side, saves `.webp`, and prints the pixel boxes of the printed labels (for masks). |
| `grid.py` | Rebuilds a tall multi-panel figure as a 2-column grid with a label strip under each panel (easier to read on a phone). |
| `decks/*.py` | One script per chapter. Run it, then `npm run zip:premade`. |

```bash
python scripts/premade-authoring/decks/bio_ch02.py
npm run zip:premade
```

Put the NCERT PDFs in `NCERT-pdfs/` (not committed).

## Rules the app imposes (learned from the pilot)

- **Never put a cloze inside a formula.** `{{c1::…}}` inside `\( … \)` breaks KaTeX, and the raw LaTeX shows.
- **Avoid `\text{…}` in formulas.** Until the `mobile-study.css` fix ships in an app build, installed apps split it one letter per line. Write words outside the math: `Bond order \(= \tfrac12(N_b - N_a)\)`.
- **KaTeX renders only in basic and cloze text,** not inside advanced HTML. Use Unicode, `<sub>` and `<sup>` there.
- **No SVG in advanced HTML yet.** The sanitiser allows it from this release on, but decks go live to every installed build. Draw with divs and CSS until the SVG build is widespread.
- **Occlusion mode is `occlusion.guessMode`** (`hide-all` or `hide-one`); the importer ignores `mode`. The front shows "Guess the hidden part", not the card's `term`.
- Advanced cards use a paper-coloured background, so they read the same on dark and light themes.
