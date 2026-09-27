"""Crops the figures for Biology 11 Ch 15 (Body Fluids and Circulation). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'bio11', 'kebo115.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch15-body-fluids-and-circulation', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_15_1_formed_elements': (1, (64, 585, 531, 694)),
    'fig_15_2_heart': (5, (135, 395, 532, 690)),
    'fig_15_3_ecg': (8, (279, 102, 519, 211)),
    'fig_15_4_circulation': (9, (133, 174, 470, 408)),
}, MEDIA, long_side=1000)
