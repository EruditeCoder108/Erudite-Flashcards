"""Crops the figures for Biology 12 Ch 13 (Biodiversity and Conservation). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'bio12', 'lebo113.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Biology', 'class12-biology-ch13-biodiversity-and-conservation', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_13_1_global_biodiversity': (2, (170, 236, 527, 577)),
    'fig_13_2_species_area': (4, (56, 225, 325, 460)),
}, MEDIA, long_side=1000)
