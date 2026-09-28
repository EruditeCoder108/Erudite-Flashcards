"""Crops the figures for Chemistry 11 Ch 2 (Structure of Atom). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'chem11', 'kech102.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Chemistry', 'class11-chemistry-ch02-structure-of-atom', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_2_1a_cathode_tube': (1, (305, 92, 530, 201)),
    'fig_2_1b_perforated_anode': (1, (305, 240, 530, 347)),
    'fig_2_2_thomson_em': (2, (120, 515, 480, 704)),
    'fig_2_3_millikan': (3, (310, 390, 532, 546)),
    'fig_2_4_thomson_model': (4, (60, 452, 292, 546)),
    'fig_2_5a_rutherford': (5, (55, 295, 292, 402)),
    'fig_2_5b_gold_foil': (5, (55, 452, 292, 620)),
    'fig_2_6_em_wave': (8, (306, 436, 535, 569)),
    'fig_2_7_em_spectrum': (9, (60, 466, 540, 692)),
    'fig_2_8_blackbody_curve': (11, (324, 389, 515, 555)),
    'fig_2_9_photoelectric': (12, (62, 514, 288, 645)),
    'fig_2_10_emission_absorption': (16, (95, 92, 505, 295)),
    'tab_2_3_hydrogen_series': (16, (305, 612, 538, 716)),
    'fig_2_11_h_transitions': (17, (58, 93, 289, 371)),
    'fig_2_12_psi_plots': (28, (306, 93, 535, 305)),
    'fig_2_13_1s_2s': (29, (306, 93, 535, 273)),
    'fig_2_14_p_orbitals': (29, (306, 357, 535, 566)),
    'fig_2_15_d_orbitals': (30, (60, 243, 290, 686)),
    'fig_2_16_energy_levels': (31, (59, 312, 287, 585)),
    'fig_2_17_filling_order': (33, (100, 365, 272, 700)),
    'fig_2_18_exchange': (36, (335, 143, 500, 548)),
}, MEDIA, long_side=1000)
