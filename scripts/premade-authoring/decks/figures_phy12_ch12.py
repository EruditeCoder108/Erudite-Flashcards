"""Crops the figures for Physics 12 Ch 12 (Atoms)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'phy12', 'leph204.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Physics', 'class12-physics-ch12-atoms', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_12_1_geiger_marsden': (2, (48, 105, 321, 330)),
    'fig_12_2_schematic': (2, (178, 396, 503, 579)),
    'fig_12_3_scattering_data': (3, (251, 104, 519, 307)),
    'fig_12_4_trajectories': (4, (48, 281, 298, 416)),
    'fig_12_5_h_lines': (7, (211, 170, 519, 251)),
    'fig_12_6_spiral': (8, (287, 94, 398, 236)),
    'fig_12_7_levels': (10, (48, 107, 223, 379)),
    'fig_12_8_standing_wave': (11, (356, 396, 528, 574)),
}, MEDIA, long_side=1000)
