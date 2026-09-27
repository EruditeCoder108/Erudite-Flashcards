"""Crops the figures for Biology 11 Ch 13 (Plant Growth and Development). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'bio11', 'kebo113.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch13-plant-growth-and-development', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_13_1_germination': (1, (56, 92, 498, 374)),
    'fig_13_2_meristems': (2, (55, 94, 292, 374)),
    'fig_13_3_parallel_lines': (2, (83, 521, 248, 663)),
    'fig_13_4_arithmetic_geometric': (3, (92, 317, 460, 676)),
    'fig_13_5_linear_growth': (4, (60, 107, 266, 364)),
    'fig_13_6_sigmoid': (4, (70, 466, 262, 660)),
    'fig_13_7_absolute_relative': (5, (109, 104, 438, 303)),
    'fig_13_8_development': (7, (53, 116, 505, 286)),
    'fig_13_9_heterophylly': (7, (114, 426, 476, 696)),
    'fig_13_10_coleoptile': (8, (60, 550, 308, 662)),
    'fig_13_11_apical_dominance': (10, (63, 99, 299, 290)),
}, MEDIA, long_side=1000)
