"""Crops the figures for Physics 11 Ch 14 (Waves). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'phy11', 'keph207.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Physics', 'class11-physics-ch14-waves', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_14_1_springs': (1, (293, 158, 522, 206)),
    'fig_14_2_pulse': (2, (97, 400, 300, 521)),
    'fig_14_3_harmonic_wave': (2, (355, 80, 547, 196)),
    'fig_14_4_sound_pipe': (2, (410, 515, 492, 646)),
    'fig_14_5_symbols': (4, (81, 328, 311, 414)),
    'fig_14_6_progressing': (4, (350, 85, 538, 372)),
    'fig_14_7_element_time': (5, (293, 76, 522, 190)),
    'fig_14_8_shift': (6, (339, 144, 548, 246)),
    'tab_14_1_sound_speeds': (8, (95, 478, 300, 706)),
    'fig_14_9_pulses': (9, (293, 78, 522, 306)),
    'fig_14_10_interference': (10, (341, 80, 548, 320)),
    'fig_14_11_reflection': (11, (57, 470, 268, 682)),
    'fig_14_12_stationary': (12, (160, 373, 504, 680)),
    'fig_14_13_string_harmonics': (13, (217, 293, 522, 684)),
    'fig_14_14a_closed_pipe': (14, (340, 484, 540, 712)),
    'fig_14_14b_closed_pipe': (15, (46, 78, 276, 308)),
    'fig_14_15_open_pipe': (15, (293, 74, 522, 212)),
    'fig_14_16_beats': (16, (328, 200, 558, 420)),
    'fig_14_pillars': (16, (129, 90, 271, 289)),
}, MEDIA, long_side=1000)
