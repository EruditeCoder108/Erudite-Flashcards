"""Crops the figures for Biology 11 Ch 7 (Structural Organisation in Animals: the frog). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'bio11', 'kebo107.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch07-structural-organisation-in-animals', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_7_1_frog_external': (1, (55, 550, 276, 695)),
    'fig_7_2_frog_internal': (2, (60, 352, 515, 685)),
    'fig_7_3_male_reproductive': (4, (285, 180, 530, 398)),
    'fig_7_4_female_reproductive': (4, (285, 440, 535, 692)),
}, MEDIA, long_side=1000)
