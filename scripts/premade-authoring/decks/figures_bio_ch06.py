"""Crops the figures for Biology 11 Ch 6 (Anatomy of Flowering Plants). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'bio11', 'kebo106.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch06-anatomy-of-flowering-plants', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_6_1_stomata': (1, (55, 335, 535, 446)),
    'fig_6_2_vascular_bundles': (2, (320, 100, 475, 490)),
    'fig_6_3a_dicot_root': (3, (68, 88, 325, 329)),
    'fig_6_3b_monocot_root': (3, (68, 330, 325, 560)),
    'fig_6_4a_dicot_stem': (4, (45, 228, 490, 492)),
    'fig_6_4b_monocot_stem': (4, (40, 498, 502, 698)),
    'fig_6_5a_dicot_leaf': (5, (55, 288, 332, 494)),
    'fig_6_5b_monocot_leaf': (5, (55, 520, 328, 682)),
}, MEDIA, long_side=1000)
