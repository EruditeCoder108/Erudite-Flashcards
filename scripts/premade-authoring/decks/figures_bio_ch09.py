"""Crops the figures for Biology 11 Ch 9 (Biomolecules). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'bio11', 'kebo109.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch09-biomolecules', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_9_1_small_biomolecules': (3, (40, 95, 525, 672)),
    'fig_9_2_glycogen': (6, (55, 465, 525, 680)),
    'fig_9_3_protein_structure': (8, (40, 95, 318, 414)),
    'fig_9_4_activation_energy': (11, (281, 88, 510, 318)),
    'fig_9_5_enzyme_activity': (12, (40, 510, 545, 680)),
}, MEDIA, long_side=1000)
