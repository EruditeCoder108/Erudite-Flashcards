"""Crops the figures for Chemistry 11 Ch 6 (Equilibrium). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'chem11', 'kech106.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Chemistry', 'class11-chemistry-ch06-equilibrium', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_6_1_vapour_pressure': (2, (100, 93, 505, 229)),
    'fig_6_2_attainment': (4, (305, 93, 535, 276)),
    'fig_6_4_haber_equilibrium': (6, (59, 92, 290, 291)),
    'fig_6_5_hi_either_side': (6, (305, 317, 534, 520)),
    'tab_6_2_h2_i2_data': (7, (67, 527, 528, 718)),
    'fig_6_6_extent_vs_k': (14, (58, 362, 290, 429)),
    'fig_6_7_q_vs_k': (14, (305, 444, 535, 546)),
    'fig_6_8_add_h2': (17, (305, 388, 536, 613)),
    'fig_6_9_no2_temperature': (19, (303, 583, 536, 689)),
    'fig_6_10_nacl_hydration': (21, (305, 285, 535, 442)),
    'fig_6_11_ph_paper': (26, (305, 306, 542, 393)),
    'tab_6_5_ph_common': (27, (85, 105, 500, 239)),
    'tab_6_6_ka_weak_acids': (27, (305, 513, 536, 689)),
    'tab_6_7_kb_weak_bases': (29, (305, 522, 536, 651)),
    'tab_6_8_polyprotic': (32, (59, 218, 289, 326)),
    'tab_6_9a_ksp': (37, (306, 128, 536, 425)),
    'tab_6_9b_ksp': (37, (306, 423, 536, 717)),
}, MEDIA, long_side=1000)
