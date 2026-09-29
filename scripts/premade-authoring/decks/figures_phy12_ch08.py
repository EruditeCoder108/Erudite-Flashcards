"""Crops the figures for Physics 12 Ch 8 (Electromagnetic Waves)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'phy12', 'leph108.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Physics', 'class12-physics-ch08-electromagnetic-waves', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_8_1a': (2, (432, 103, 532, 186)),
    'fig_8_1b': (2, (447, 218, 534, 314)),
    'fig_8_1c': (2, (432, 336, 529, 436)),
    'fig_8_2a': (3, (83, 102, 192, 184)),
    'fig_8_2b': (3, (79, 254, 209, 383)),
    'fig_8_3_wave': (5, (70, 580, 385, 668)),
    'fig_8_4_spectrum': (8, (67, 102, 414, 420)),
    'fig_8_5_capacitor': (12, (174, 615, 306, 675)),
    'fig_8_6_capacitor': (13, (321, 159, 424, 232)),
    'x2': (4, (60, 198, 420, 354)),
}, MEDIA, long_side=1000)
