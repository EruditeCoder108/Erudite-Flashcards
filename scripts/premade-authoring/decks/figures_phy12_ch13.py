"""Crops the figures for Physics 12 Ch 13 (Nuclei)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'phy12', 'leph205.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Physics', 'class12-physics-ch13-nuclei', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_13_1_binding_energy': (6, (67, 271, 346, 415)),
    'fig_13_2_potential': (7, (366, 435, 519, 588)),
}, MEDIA, long_side=1000)
