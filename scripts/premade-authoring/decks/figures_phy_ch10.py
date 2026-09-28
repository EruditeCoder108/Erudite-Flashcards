"""Crops the figures for Physics 11 Ch 10 (Thermal Properties of Matter). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'phy11', 'keph203.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Physics', 'class11-physics-ch10-thermal-properties-of-matter', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_10_1_f_vs_c': (1, (298, 80, 512, 248)),
    'fig_10_2_p_vs_t': (2, (80, 80, 315, 186)),
    'fig_10_3_absolute_zero': (2, (332, 80, 555, 187)),
    'fig_10_4_scales': (2, (330, 300, 556, 481)),
    'tab_10_1_linear_expansion': (3, (290, 80, 522, 246)),
    'fig_10_5_expansion': (3, (200, 306, 281, 372)),
    'fig_10_6_copper_alpha_v': (3, (316, 450, 490, 592)),
    'fig_10_7_water_anomaly': (4, (130, 505, 530, 657)),
    'fig_10_8_area_expansion': (5, (290, 104, 525, 237)),
    'tab_10_3_specific_heats': (7, (44, 80, 522, 236)),
    'tab_10_4_molar_heats': (7, (44, 374, 276, 520)),
    'fig_10_9_heating_curve': (8, (326, 86, 551, 241)),
    'fig_10_10_regelation': (9, (56, 86, 269, 236)),
    'fig_10_phase_diagrams': (9, (60, 518, 512, 700)),
    'fig_10_11_boiling': (10, (133, 268, 271, 548)),
    'tab_10_5_latent_heats': (11, (44, 80, 522, 244)),
    'fig_10_12_temp_vs_heat': (11, (46, 554, 277, 681)),
    'fig_10_13_modes': (12, (334, 160, 556, 308)),
    'tab_10_6_conductivities': (13, (290, 176, 523, 560)),
    'fig_10_14_conducting_bar': (13, (70, 80, 257, 202)),
    'fig_10_15_steel_copper': (14, (113, 80, 291, 147)),
    'fig_10_16_iron_brass': (14, (75, 638, 313, 686)),
    'fig_10_17_convection': (15, (80, 525, 486, 693)),
    'fig_10_18_blackbody': (16, (342, 340, 540, 503)),
    'fig_10_19_cooling_curve': (18, (108, 118, 277, 245)),
    'fig_10_20_newton_cooling': (18, (331, 350, 551, 516)),
}, MEDIA, long_side=1000)
