"""Crops the figures for Chemistry 12 Ch 4 (The d- and f-Block Elements). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'chem12', 'lech104.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Chemistry', 'class12-chemistry-ch04-d-and-f-block-elements', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'tab_4_1a_3d_series': (1, (33, 578, 559, 697)),
    'tab_4_1b_4d_5d_6d': (2, (16, 62, 542, 316)),
    'tab_lattice_structures': (3, (55, 268, 540, 443)),
    'fig_4_1_melting_points': (3, (62, 448, 292, 673)),
    'fig_4_2_atomisation': (4, (158, 212, 512, 460)),
    'fig_4_3_atomic_radii': (5, (80, 128, 260, 302)),
    'tab_4_2_first_series': (5, (55, 355, 537, 688)),
    'tab_4_3_oxidation_states': (7, (174, 530, 535, 663)),
    'fig_4_4_electrode_potentials': (9, (185, 190, 460, 428)),
    'tab_4_4_thermochemical': (10, (150, 62, 523, 254)),
    'tab_4_5_halides': (10, (21, 548, 536, 684)),
    'tab_4_6_oxides': (11, (62, 365, 534, 532)),
    'tab_4_7_magnetic_moments': (13, (172, 354, 535, 582)),
    'fig_4_5_ion_colours': (14, (304, 196, 516, 296)),
    'tab_4_8_ion_colours': (14, (152, 343, 522, 628)),
    'fig_chromate_dichromate': (17, (40, 200, 392, 315)),
    'fig_manganate': (18, (45, 160, 140, 292)),
    'fig_permanganate': (18, (45, 310, 140, 442)),
    'fig_4_6_lanthanoid_radii': (20, (62, 160, 275, 462)),
    'tab_4_9_lanthanoids': (21, (60, 62, 535, 352)),
    'fig_4_7_lanthanoid_reactions': (22, (40, 62, 300, 252)),
    'tab_4_10_actinoids': (22, (43, 410, 517, 696)),
    'tab_4_11_actinoid_ox_states': (23, (43, 512, 543, 624)),
}, MEDIA, long_side=1000)
