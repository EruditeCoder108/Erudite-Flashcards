"""Crops the figures for Physics 11 Ch 9 (Mechanical Properties of Fluids). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'phy11', 'keph202.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Physics', 'class11-physics-ch09-mechanical-properties-of-fluids', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_9_1_normal_force': (1, (64, 408, 264, 536)),
    'tab_9_1_densities': (1, (322, 537, 488, 684)),
    'fig_9_2_pascal_prism': (2, (106, 343, 290, 478)),
    'fig_9_3_fluid_column': (3, (77, 80, 245, 279)),
    'fig_9_4_hydrostatic_paradox': (3, (315, 80, 509, 183)),
    'fig_9_5b_manometer': (4, (396, 80, 512, 237)),
    'fig_9_5a_barometer': (4, (80, 416, 286, 694)),
    'fig_9_6a_pascal_transmission': (5, (36, 466, 278, 537)),
    'fig_9_6b_hydraulic_lift': (5, (303, 343, 502, 482)),
    'fig_9_7_streamlines': (6, (343, 443, 548, 572)),
    'fig_9_8_laminar_turbulent': (7, (295, 104, 520, 182)),
    'fig_9_9_bernoulli_pipe': (8, (82, 504, 312, 664)),
    'fig_9_10_torricelli': (9, (100, 80, 260, 236)),
    'fig_9_11_lift': (10, (80, 98, 547, 212)),
    'fig_9_12_viscous_layers': (11, (42, 216, 257, 514)),
    'fig_9_13_viscosity_block': (11, (322, 340, 491, 464)),
    'tab_9_2_viscosities': (12, (80, 302, 312, 476)),
    'fig_9_14_surface_molecules': (13, (44, 508, 524, 640)),
    'fig_9_15_film': (14, (80, 122, 310, 216)),
    'tab_9_3_surface_tension': (14, (325, 502, 559, 708)),
    'fig_9_16_balance': (15, (64, 297, 259, 432)),
    'fig_9_17_contact_angle': (15, (290, 180, 523, 382)),
    'fig_9_18_drop_bubble': (16, (323, 182, 566, 272)),
    'fig_9_19_capillary': (16, (342, 556, 532, 648)),
    'fig_9_20_flow_ex': (21, (172, 82, 393, 177)),
    'fig_9_21_films_ex': (21, (192, 346, 383, 452)),
}, MEDIA, long_side=1000)
