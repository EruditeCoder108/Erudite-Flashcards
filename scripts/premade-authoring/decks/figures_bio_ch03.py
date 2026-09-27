"""Crops the figures for Biology 11 Ch 3 (Plant Kingdom).

Usage: python scripts/premade-authoring/decks/figures_bio_ch03.py   (PDF in NCERT-pdfs/bio11/)
Rects are (page index, (x0, y0, x1, y1)) in PDF points. Mask boxes in bio_ch03.py
are pixels of these exact crops; re-measure if a crop changes.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export
from grid import grid

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'bio11', 'kebo103.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch03-plant-kingdom', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_3_1_volvox': (2, (112, 104, 292, 240)),
    'fig_3_1_laminaria': (2, (58, 266, 172, 474)),
    'fig_3_1_fucus': (2, (176, 288, 345, 474)),
    'fig_3_2_marchantia': (5, (115, 230, 506, 420)),
    'fig_3_2_funaria': (5, (70, 430, 290, 652)),
    'fig_3_2_sphagnum': (5, (318, 426, 542, 650)),
    'fig_3_3_selaginella': (8, (52, 115, 290, 306)),
    'fig_3_3_equisetum': (8, (310, 110, 506, 428)),
    'fig_3_4_ginkgo': (10, (318, 502, 515, 650)),
}, MEDIA, long_side=1000)

# Name-the-organism figures as 2-column grids with a label strip under each panel.
print('algae', grid(PDF, 2, [
    ('a', (112, 104, 292, 240)), ('b', (343, 106, 395, 270)), ('c', (58, 266, 172, 474)), ('d', (176, 288, 345, 474)),
    ('e', (340, 284, 494, 474)), ('f', (118, 500, 242, 648)), ('g', (285, 493, 462, 660))],
    os.path.join(MEDIA, 'fig_3_1_algae_grid.webp'), cell=(340, 420), cols=3))
print('pterido', grid(PDF, 8, [
    ('a', (52, 115, 290, 306)), ('b', (310, 110, 506, 428)), ('c', (70, 447, 227, 652)), ('d', (340, 442, 470, 655))],
    os.path.join(MEDIA, 'fig_3_3_pteridophytes_grid.webp')))
print('gymno', grid(PDF, 10, [
    ('a', (317, 103, 517, 254)), ('b', (335, 270, 497, 484)), ('c', (320, 502, 515, 650))],
    os.path.join(MEDIA, 'fig_3_4_gymnosperms_grid.webp')))
