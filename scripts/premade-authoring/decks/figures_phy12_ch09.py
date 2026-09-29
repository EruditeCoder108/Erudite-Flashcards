"""Crops the figures for Physics 12 Ch 9 (Ray Optics and Optical Instruments)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'phy12', 'leph201.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Physics', 'class12-physics-ch09-ray-optics-and-optical-instruments', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_9_1_reflection': (1, (49, 230, 270, 368)),
    'fig_9_2_sign': (1, (49, 535, 319, 674)),
    'fig_9_3a_concave_focus': (2, (45, 361, 227, 456)),
    'fig_9_3b_convex_focus': (2, (296, 362, 482, 477)),
    'fig_9_3c_focal_plane': (2, (170, 486, 352, 584)),
    'fig_9_4a_geometry': (3, (48, 110, 175, 192)),
    'fig_9_4b_geometry': (3, (50, 210, 205, 302)),
    'fig_9_5_concave_real': (3, (50, 393, 256, 546)),
    'fig_9_6a_concave_virtual': (5, (102, 276, 338, 366)),
    'fig_9_6b_convex_virtual': (5, (355, 276, 521, 351)),
    'fig_9_7_phone': (5, (224, 597, 459, 719)),
    'fig_9_8_refraction': (7, (46, 457, 262, 629)),
    'fig_9_9_slab': (8, (287, 104, 516, 218)),
    'fig_9_10_apparent_depth': (8, (306, 264, 519, 505)),
    'fig_9_11_tir': (9, (51, 103, 295, 243)),
    'fig_9_12a_laser': (10, (443, 104, 495, 161)),
    'fig_9_12b_laser': (10, (424, 184, 512, 230)),
    'fig_9_13a_prism90': (10, (273, 464, 389, 583)),
    'fig_9_13b_prism180': (10, (408, 478, 519, 583)),
    'fig_9_13c_prism_invert': (10, (316, 613, 510, 671)),
    'fig_9_14_fibre': (11, (51, 118, 282, 194)),
    'fig_9_15_spherical': (12, (308, 108, 520, 227)),
    'fig_9_16a_lens': (13, (76, 252, 281, 353)),
    'fig_9_16b_first_surface': (13, (79, 378, 291, 486)),
    'fig_9_16c_second_surface': (13, (56, 522, 298, 614)),
    'fig_9_17a_convex_rays': (14, (300, 440, 519, 553)),
    'fig_9_17b_concave_rays': (14, (298, 580, 515, 687)),
    'fig_9_18_power': (15, (48, 340, 228, 453)),
    'fig_9_19_contact': (16, (312, 403, 519, 478)),
    'fig_9_21_prism': (18, (298, 373, 516, 501)),
    'fig_9_22_deviation_curve': (19, (48, 95, 266, 266)),
    'fig_9_23a_magnifier_near': (20, (91, 106, 358, 250)),
    'fig_9_23b_magnifier_angle': (20, (145, 292, 321, 332)),
    'fig_9_23c_magnifier_inf': (20, (95, 344, 360, 538)),
    'fig_9_24_compound': (22, (64, 103, 372, 316)),
    'fig_9_25_telescope': (24, (69, 264, 380, 441)),
    'fig_9_26_cassegrain': (25, (187, 104, 505, 258)),
    'fig_9_27a': (28, (84, 345, 172, 442)),
    'fig_9_27b': (28, (199, 345, 286, 443)),
    'fig_9_27c': (28, (303, 345, 392, 443)),
    'fig_9_28_lightpipe': (29, (241, 659, 455, 721)),
    'fig_9_29_galvo': (32, (131, 104, 335, 197)),
    'fig_9_30_liquid_lens': (32, (143, 326, 324, 479)),
}, MEDIA, long_side=1000)
