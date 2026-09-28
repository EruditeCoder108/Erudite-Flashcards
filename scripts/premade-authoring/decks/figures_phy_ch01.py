"""Crops the figures for Physics 11 Ch 1 (Units and Measurement). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'phy11', 'keph101.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Physics', 'class11-physics-ch01-units-and-measurement', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_1_1_angles': (1, (385, 76, 540, 238)),
    'tab_1_2_units_outside_si': (2, (104, 97, 470, 298)),
}, MEDIA, long_side=1000)
