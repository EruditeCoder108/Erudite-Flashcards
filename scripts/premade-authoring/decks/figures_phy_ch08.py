"""Crops the figures for Physics 11 Ch 8 (Mechanical Properties of Solids). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'phy11', 'keph201.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Physics', 'class11-physics-ch08-mechanical-properties-of-solids', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_8_1_stress_types': (1, (100, 536, 552, 662)),
    'fig_8_2_stress_strain': (2, (318, 203, 500, 382)),
    'fig_8_3_aorta': (3, (95, 80, 290, 252)),
    'tab_8_1_youngs_moduli': (3, (98, 466, 545, 692)),
    'fig_8_4_pyramid': (4, (345, 512, 468, 704)),
    'tab_8_2_shear_moduli': (5, (326, 80, 558, 283)),
    'fig_8_5_lead_slab': (5, (330, 503, 556, 634)),
    'tab_8_3_bulk_moduli': (6, (290, 80, 524, 438)),
    'tab_8_4_moduli_summary': (6, (44, 452, 524, 707)),
    'fig_8_6_beam': (8, (68, 570, 261, 680)),
    'fig_8_7_beam_sections': (8, (368, 362, 526, 540)),
    'fig_8_8_pillars': (9, (200, 88, 272, 232)),
    'fig_8_9_ex_curve': (10, (166, 525, 380, 692)),
    'fig_8_10_two_materials': (11, (216, 108, 422, 204)),
    'fig_8_11_two_wires': (11, (255, 352, 366, 500)),
}, MEDIA, long_side=1000)
