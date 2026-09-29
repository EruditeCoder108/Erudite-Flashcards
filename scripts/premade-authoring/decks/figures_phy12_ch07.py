"""Crops the figures for Physics 12 Ch 7 (Alternating Current). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'phy12', 'leph107.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Physics', 'class12-physics-ch07-alternating-current', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_7_1_resistor': (1, (317, 262, 532, 358)),
    'fig_7_2_vi_resistor': (1, (75, 530, 225, 622)),
    'fig_7_3_rms': (2, (132, 501, 275, 608)),
    'fig_7_4_phasor_R': (4, (305, 200, 530, 296)),
    'fig_7_5_inductor': (4, (339, 513, 534, 609)),
    'fig_7_6_phasor_L': (6, (116, 102, 346, 212)),
    'fig_7_7_capacitor': (7, (79, 166, 276, 268)),
    'fig_7_8_phasor_C': (8, (296, 102, 533, 196)),
    'fig_7_10_lcr': (9, (90, 581, 291, 692)),
    'fig_7_11_phasors': (10, (322, 262, 540, 385)),
    'fig_7_12_impedance': (11, (79, 102, 221, 232)),
    'fig_7_13_lcr_phasor': (11, (79, 378, 322, 502)),
    'fig_7_14_resonance': (12, (314, 289, 528, 439)),
    'fig_7_15_power_comp': (15, (232, 100, 515, 265)),
    'fig_7_16_transformer': (17, (80, 246, 548, 427)),
}, MEDIA, long_side=1000)
