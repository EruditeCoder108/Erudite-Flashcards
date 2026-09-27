"""Crops the figures for Biology 11 Ch 2 from the NCERT PDF (watermark layer removed).

Usage: python scripts/premade-authoring/decks/figures_bio_ch02.py path/to/kebo102.pdf
Mask boxes in bio_ch02.py are in pixels of these exact crops; re-measure if a crop changes.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export
from grid import grid

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch02-biological-classification', 'media')
pdf = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'NCERT-pdfs', 'kebo102.pdf')
os.makedirs(MEDIA, exist_ok=True)

# (page index, clip rect in PDF points)
export(pdf, {'fig_2_1_bacteria_shapes': (2, (40, 558, 540, 684)), 'fig_2_6b_bacteriophage': (10, (302, 85, 535, 312))}, MEDIA, long_side=1000)
export(pdf, {'fig_2_2_nostoc': (3, (338, 452, 512, 662)), 'fig_2_6a_tmv': (10, (40, 120, 302, 300))}, MEDIA, long_side=900)
# Identify-the-organism figures are rebuilt as 2-column grids with a label strip under each panel.
print(grid(pdf, 5, [('a', (330, 88, 540, 264)), ('b', (330, 284, 540, 352)), ('c', (401, 384, 540, 510)), ('d', (330, 530, 540, 636))],
           os.path.join(MEDIA, 'fig_2_4_protists.webp')))
print(grid(pdf, 7, [('a', (324, 248, 500, 354)), ('b', (324, 372, 500, 480)), ('c', (324, 497, 500, 655))],
           os.path.join(MEDIA, 'fig_2_5_fungi.webp')))
