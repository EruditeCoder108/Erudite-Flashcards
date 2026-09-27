"""Crops the figures for Biology 12 Ch 12 (Ecosystem). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'bio12', 'lebo112.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Biology', 'class12-biology-ch12-ecosystem', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_12_1_decomposition': (3, (40, 80, 545, 475)),
    'fig_12_2_trophic_levels': (5, (100, 385, 530, 690)),
    'fig_12_3_energy_flow': (6, (30, 310, 515, 603)),
    'fig_12_4a_pyramid_numbers': (7, (95, 178, 525, 348)),
    'fig_12_4b_pyramid_biomass': (7, (95, 383, 525, 558)),
    'fig_12_4c_inverted_biomass': (7, (150, 580, 440, 675)),
    'fig_12_4d_pyramid_energy': (8, (95, 78, 400, 258)),
}, MEDIA, long_side=1000)
