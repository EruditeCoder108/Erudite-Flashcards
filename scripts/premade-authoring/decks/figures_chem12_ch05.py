"""Crops the figures for Chemistry 12 Ch 5 (Coordination Compounds). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'chem12', 'lech105.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Chemistry', 'class12-chemistry-ch05-coordination-compounds', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'tab_5_1_cobalt_ammines': (1, (153, 262, 518, 376)),
    'fig_5_1_polyhedra': (4, (55, 302, 530, 410)),
    'fig_5_2_cis_trans_pt': (7, (35, 478, 240, 547)),
    'fig_5_3_cis_trans_co': (7, (35, 582, 265, 674)),
    'fig_5_4_cis_trans_en': (8, (60, 58, 320, 148)),
    'fig_5_5_fac_mer': (8, (170, 192, 340, 278)),
    'fig_5_6_optical_coen3': (8, (55, 430, 335, 553)),
    'fig_5_7_optical_ptcl2en2': (8, (138, 580, 405, 695)),
    'fig_ex55_fe_isomers': (9, (150, 95, 440, 190)),
    'fig_ex56_crcl2ox2': (9, (150, 263, 440, 390)),
    'tab_5_2_hybridisation': (10, (174, 575, 535, 695)),
    'fig_vbt_co_nh3_6': (11, (32, 90, 375, 238)),
    'fig_vbt_cof6': (11, (40, 350, 505, 475)),
    'fig_vbt_nicl4': (11, (35, 502, 372, 634)),
    'fig_vbt_ni_cn_4': (12, (175, 112, 532, 240)),
    'fig_5_8_octahedral_splitting': (14, (45, 62, 372, 297)),
    'fig_5_9_tetrahedral_splitting': (15, (52, 82, 284, 218)),
    'tab_5_3_colours': (15, (40, 385, 520, 548)),
    'fig_5_10_ti_transition': (16, (55, 62, 340, 190)),
    'fig_5_11_ni_en_colours': (16, (190, 390, 540, 570)),
    'fig_5_12_ruby_emerald': (17, (262, 62, 512, 145)),
    'fig_5_13_carbonyls': (18, (160, 50, 520, 250)),
    'fig_5_14_synergic': (18, (78, 262, 250, 362)),
}, MEDIA, long_side=1000)
