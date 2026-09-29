"""Crops the figures for Physics 12 Ch 14 (Semiconductor Electronics)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'phy12', 'leph206.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Physics', 'class12-physics-ch14-semiconductor-electronics-materials-devices-and-simple-circuits', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_14_1_bands_0K': (3, (48, 104, 247, 292)),
    'fig_14_2a_metal': (3, (357, 444, 521, 525)),
    'fig_14_2b_insulator': (3, (97, 562, 283, 670)),
    'fig_14_2c_semiconductor': (3, (376, 591, 501, 671)),
    'fig_14_3_diamond': (4, (329, 339, 519, 491)),
    'fig_14_4_bonds': (5, (56, 106, 189, 254)),
    'fig_14_5a_hole': (5, (73, 452, 285, 623)),
    'fig_14_5b_hole_motion': (5, (335, 463, 500, 616)),
    'fig_14_6a_intrinsic_0K': (6, (241, 124, 362, 231)),
    'fig_14_6b_intrinsic_T': (6, (397, 109, 519, 231)),
    'fig_14_7a_donor': (7, (50, 103, 289, 257)),
    'fig_14_7b_n_type': (7, (80, 292, 200, 382)),
    'fig_14_8a_acceptor': (8, (372, 104, 519, 257)),
    'fig_14_8b_p_type': (8, (374, 285, 512, 392)),
    'fig_14_9a_n_bands': (9, (65, 374, 247, 541)),
    'fig_14_9b_p_bands': (9, (307, 381, 504, 515)),
    'fig_14_10_formation': (10, (341, 575, 519, 670)),
    'fig_14_11a_equilibrium': (11, (57, 108, 199, 193)),
    'fig_14_11b_barrier': (11, (71, 222, 183, 269)),
    'fig_14_12a_diode': (11, (59, 448, 234, 509)),
    'fig_14_13a_forward': (12, (378, 104, 519, 180)),
    'fig_14_13b_forward_barrier': (12, (392, 219, 512, 269)),
    'fig_14_14_injection': (12, (359, 375, 518, 463)),
    'fig_14_15a_reverse': (13, (48, 104, 191, 179)),
    'fig_14_15b_reverse_barrier': (13, (63, 202, 186, 268)),
    'fig_14_16a_forward_circuit': (13, (54, 420, 221, 543)),
    'fig_14_16b_reverse_circuit': (13, (53, 558, 220, 685)),
    'fig_14_16c_vi': (13, (278, 447, 516, 662)),
    'fig_14_18_half_wave': (15, (76, 190, 262, 257)),
    'fig_14_18b_half_waveforms': (15, (50, 271, 256, 417)),
    'fig_14_19_full_wave': (16, (270, 104, 519, 489)),
    'fig_14_20a_filter': (17, (51, 106, 262, 202)),
    'fig_14_20b_filter_wave': (17, (290, 100, 520, 220)),
}, MEDIA, long_side=1000)
