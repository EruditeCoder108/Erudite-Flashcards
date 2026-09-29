"""Crops the figures for Physics 12 Ch 6 (Electromagnetic Induction). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'phy12', 'leph106.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Physics', 'class12-physics-ch06-electromagnetic-induction', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_6_1_magnet_coil': (1, (330, 470, 440, 615)),
    'fig_6_3_two_coils': (2, (238, 338, 521, 514)),
    'fig_6_6_lenz': (6, (53, 462, 200, 656)),
    'fig_6_7_loops': (7, (100, 166, 340, 365)),
    'fig_6_8_rect_circle': (8, (172, 100, 540, 160)),
    'fig_6_9_capacitor': (8, (262, 206, 520, 272)),
    'fig_6_10_motional': (8, (70, 510, 313, 660)),
    'fig_6_11_rotating_rod': (10, (230, 100, 500, 271)),
    'fig_6_12_coaxial': (12, (75, 100, 260, 284)),
    'fig_6_13_generator': (16, (58, 440, 305, 680)),
    'fig_6_14_ac_emf': (18, (95, 115, 550, 362)),
    # Fig 6.15, one panel per exercise card
    'fig_6_15a': (21, (60, 110, 240, 234)),
    'fig_6_15b': (21, (250, 110, 500, 235)),
    'fig_6_15c': (21, (60, 245, 275, 390)),
    'fig_6_15d': (21, (285, 245, 500, 390)),
    'fig_6_15e': (21, (60, 435, 290, 525)),
    'fig_6_15f': (21, (290, 420, 500, 530)),
    'fig_6_16_deform': (22, (255, 117, 490, 222)),
}, MEDIA, long_side=1000)
