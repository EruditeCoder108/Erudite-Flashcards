"""Crops the figures for Chemistry 12 Ch 3 (Chemical Kinetics). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'chem12', 'lech103.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Chemistry', 'class12-chemistry-ch03-chemical-kinetics', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_3_1_average_instantaneous': (2, (35, 199, 520, 408)),
    'tab_3_1_butyl_chloride': (3, (80, 60, 528, 278)),
    'fig_3_2_tangent': (3, (182, 462, 535, 692)),
    'tab_3_2_no_rates': (6, (40, 440, 518, 572)),
    'fig_3_3_zero_order': (11, (60, 62, 262, 245)),
    'fig_3_4_ln_r_vs_t': (13, (80, 62, 262, 238)),
    'fig_3_5_log_ratio_vs_t': (13, (330, 62, 518, 240)),
    'tab_3_4_integrated_laws': (16, (20, 550, 537, 695)),
    'fig_3_6_hi_intermediate': (18, (342, 146, 520, 208)),
    'fig_3_7_energy_profile': (18, (272, 270, 512, 426)),
    'fig_3_8_maxwell_boltzmann': (18, (268, 520, 518, 662)),
    'fig_3_9_temperature_curve': (19, (60, 60, 335, 198)),
    'fig_3_10_arrhenius_plot': (19, (64, 460, 258, 652)),
    'fig_3_11_catalyst': (21, (60, 395, 285, 515)),
    'fig_3_12_orientation': (22, (243, 370, 520, 472)),
}, MEDIA, long_side=1000)
