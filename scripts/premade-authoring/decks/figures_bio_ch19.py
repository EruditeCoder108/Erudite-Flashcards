"""Crops the figures for Biology 11 Ch 19 (Chemical Coordination and Integration). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'bio11', 'kebo119.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch19-chemical-coordination-and-integration', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_19_1_endocrine_glands': (1, (55, 105, 322, 445)),
    'fig_19_2_pituitary': (2, (280, 96, 520, 368)),
    'fig_19_3_thyroid': (3, (55, 205, 260, 650)),
    'fig_19_4_adrenal': (5, (90, 244, 540, 522)),
    'fig_19_5a_protein_hormone': (9, (71, 367, 534, 628)),
    'fig_19_5b_steroid_hormone': (10, (36, 76, 517, 423)),
}, MEDIA, long_side=1000)
