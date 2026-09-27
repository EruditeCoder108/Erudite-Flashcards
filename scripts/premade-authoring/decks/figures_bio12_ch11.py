"""Crops the figures for Biology 12 Ch 11 (Organisms and Populations). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'bio12', 'lebo111.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Biology', 'class12-biology-ch11-organisms-and-populations', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_11_1_age_pyramids': (4, (95, 78, 530, 178)),
    'fig_11_2_population_density': (5, (39, 250, 510, 535)),
    'fig_11_3_growth_curves': (6, (50, 357, 275, 524)),
    'fig_11_4_fig_wasp': (13, (35, 370, 480, 555)),
    'fig_11_5_orchid_bee': (14, (52, 330, 250, 544)),
}, MEDIA, long_side=1000)
