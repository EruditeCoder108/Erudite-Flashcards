"""Crops the figures for Physics 11 Ch 13 (Oscillations). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'phy11', 'keph206.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Physics', 'class11-physics-ch13-oscillations', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_13_1_periodic': (1, (58, 392, 312, 676)),
    'fig_13_2a_spring_block': (2, (298, 108, 514, 218)),
    'fig_13_2b_pendulum': (2, (318, 293, 492, 412)),
    'fig_13_4_positions': (4, (46, 78, 278, 264)),
    'fig_13_5_x_vs_t': (4, (56, 440, 248, 546)),
    'fig_13_8_two_periods': (5, (80, 376, 312, 488)),
    'fig_13_9_ball_circle': (5, (340, 456, 500, 558)),
    'fig_13_10_reference_circle': (6, (62, 82, 251, 271)),
    'fig_13_12_acceleration_projection': (7, (366, 358, 531, 518)),
    'fig_13_13_x_v_a': (8, (56, 244, 260, 470)),
    'fig_13_14_two_springs': (9, (60, 75, 280, 172)),
    'fig_13_16_energy': (10, (66, 406, 246, 634)),
    'fig_13_17_pendulum_forces': (11, (345, 135, 530, 455)),
    'tab_13_1_sin_theta': (12, (292, 80, 522, 206)),
    'fig_13_18_ex_xt': (15, (208, 298, 430, 690)),
    'fig_13_19_ex_spring': (16, (164, 536, 410, 653)),
    'fig_13_20_ex_circles': (17, (212, 216, 426, 342)),
    'fig_13_21_ex_springs': (17, (118, 553, 520, 660)),
}, MEDIA, long_side=1000)
