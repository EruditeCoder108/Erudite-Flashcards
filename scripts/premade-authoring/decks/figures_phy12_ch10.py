"""Crops the figures for Physics 12 Ch 10 (Wave Optics)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'phy12', 'leph202.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Physics', 'class12-physics-ch10-wave-optics', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_10_1a_spherical': (2, (417, 126, 509, 218)),
    'fig_10_1b_plane': (2, (411, 340, 520, 398)),
    'fig_10_2_huygens': (2, (118, 541, 328, 657)),
    'fig_10_3_plane_huygens': (3, (59, 104, 127, 275)),
    'fig_10_4_refraction': (3, (206, 506, 429, 663)),
    'fig_10_5_rarer': (5, (219, 362, 464, 513)),
    'fig_10_6_reflection': (6, (123, 103, 327, 196)),
    'fig_10_7_wavefronts': (6, (43, 580, 485, 710)),
    'fig_10_8b_ripple': (7, (180, 447, 283, 536)),
    'fig_10_9a_constructive': (8, (416, 103, 513, 204)),
    'fig_10_9b_destructive': (8, (416, 235, 519, 333)),
    'fig_10_10_hyperbolas': (8, (409, 576, 518, 644)),
    'fig_10_11_two_lamps': (10, (333, 198, 425, 288)),
    'fig_10_12_young': (10, (75, 553, 468, 688)),
    'fig_10_13_fringes': (11, (250, 351, 438, 516)),
    'fig_10_14_single_slit': (12, (278, 293, 504, 424)),
    'fig_10_15_diffraction': (12, (396, 483, 519, 650)),
    'fig_10_16_blades': (13, (58, 389, 144, 481)),
    'fig_10_17a_string': (14, (53, 203, 394, 287)),
    'fig_10_17b_string': (14, (51, 334, 402, 419)),
    'fig_10_18a_polaroids': (16, (193, 103, 304, 180)),
    'fig_10_18b_polaroids': (16, (147, 203, 217, 261)),
}, MEDIA, long_side=1000)
