"""Crops the figures for Physics 11 Ch 12 (Kinetic Theory). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'phy11', 'keph205.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Physics', 'class11-physics-ch12-kinetic-theory', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_12_1_real_gas': (2, (334, 403, 566, 560)),
    'fig_12_2_boyle_steam': (3, (56, 420, 264, 612)),
    'fig_12_3_charles_co2': (3, (302, 276, 506, 466)),
    'fig_12_4_wall_collision': (5, (72, 419, 251, 560)),
    'fig_12_5_porous_wall': (7, (322, 80, 451, 274)),
    'fig_12_6_diatomic_axes': (8, (338, 196, 548, 325)),
    'tab_12_1_predicted_heats': (10, (80, 254, 314, 382)),
    'tab_12_2_measured_heats': (10, (80, 404, 312, 610)),
    'tab_12_3_solids': (10, (326, 508, 560, 612)),
    'fig_12_7_mean_free_path': (11, (48, 177, 272, 380)),
    'fig_12_8_ex_pv_t': (13, (216, 495, 384, 634)),
}, MEDIA, long_side=1000)
