"""Crops the figures for Physics 12 Ch 11 (Dual Nature of Radiation and Matter)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'phy12', 'leph203.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Physics', 'class12-physics-ch11-dual-nature-of-radiation-and-matter', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_11_1_apparatus': (3, (331, 500, 519, 670)),
    'fig_11_2_current_intensity': (4, (61, 105, 211, 254)),
    'fig_11_3_current_potential': (4, (62, 497, 307, 690)),
    'fig_11_4_frequencies': (5, (286, 353, 523, 477)),
    'fig_11_5_v0_vs_nu': (5, (290, 546, 518, 680)),
}, MEDIA, long_side=1000)
