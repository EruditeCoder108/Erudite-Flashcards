"""Crops the figures for Biology 11 Ch 5 (Morphology of Flowering Plants). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'bio11', 'kebo105.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch05-morphology-of-flowering-plants', 'media')
os.makedirs(MEDIA, exist_ok=True)

# Labelled diagrams (masked in the deck).
export(PDF, {
    'fig_5_1_plant_parts': (3, (90, 100, 318, 400)),
    'fig_5_3_root_tip': (4, (285, 112, 522, 330)),
    'fig_5_4a_leaf_parts': (5, (60, 100, 265, 238)),
    'fig_5_10_flower_parts': (8, (55, 566, 518, 690)),
    'fig_5_13_fruits': (11, (200, 95, 488, 240)),
    'fig_5_14_dicot_seed': (11, (52, 480, 286, 600)),
    'fig_5_15_monocot_seed': (12, (90, 100, 470, 292)),
    'fig_5_12_placentation': (10, (390, 100, 505, 628)),
    'fig_5_9_thalamus': (7, (70, 480, 535, 665)),
    'fig_5_11_aestivation': (9, (125, 100, 468, 300)),
}, MEDIA, long_side=1000)

# Pictures shown on ordinary cards.
export(PDF, {
    'fig_5_2_roots': (3, (60, 440, 545, 655)),
    'fig_5_4bc_venation': (5, (65, 245, 255, 452)),
    'fig_5_5_compound_leaves': (5, (55, 520, 272, 672)),
    'fig_5_6_phyllotaxy': (6, (300, 88, 505, 330)),
    'fig_5_7_racemose': (6, (288, 425, 500, 680)),
    'fig_5_8_cymose': (7, (55, 100, 280, 225)),
    'fig_5_16_floral_diagram': (12, (338, 452, 522, 682)),
    'fig_5_17_solanum': (13, (105, 470, 485, 690)),
}, MEDIA, long_side=800)
