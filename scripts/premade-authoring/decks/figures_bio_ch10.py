"""Crops the figures for Biology 11 Ch 10 (Cell Cycle and Cell Division). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'bio11', 'kebo110.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch10-cell-cycle-and-cell-division', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_10_1_cell_cycle': (1, (295, 112, 505, 300)),
    'mitosis_early_prophase': (3, (365, 110, 485, 220)),
    'mitosis_late_prophase': (3, (365, 242, 485, 350)),
    'mitosis_transition_metaphase': (3, (365, 376, 485, 500)),
    'mitosis_metaphase': (3, (365, 528, 485, 636)),
    'mitosis_anaphase': (4, (85, 105, 200, 252)),
    'mitosis_telophase': (4, (85, 285, 200, 440)),
    'mitosis_cytokinesis': (4, (85, 482, 200, 632)),
    'fig_10_3_meiosis_1': (7, (38, 100, 520, 322)),
    'fig_10_4_meiosis_2': (8, (55, 100, 530, 358)),
}, MEDIA, long_side=1000)
