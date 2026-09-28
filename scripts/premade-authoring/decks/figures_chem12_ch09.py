"""Crops the figures for Chemistry 12 Ch 9 (Amines).
Most rects were read off contact-sheet display pixels (tile-relative) and converted to PDF points by `sd`; plain tuples are already points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'chem12', 'lech204.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Chemistry', 'class12-chemistry-ch09-amines', 'media')
os.makedirs(MEDIA, exist_ok=True)


def sd(page, x0, y0, x1, y1, pad=4):
    fx = lambda d: 50 + (d - 48) / 0.876
    fy = lambda d: 50 + (d - 60) / 0.844
    return (page, (round(fx(x0)) - pad, round(fy(y0)) - pad, round(fx(x1)) + pad, round(fy(y1)) + pad))


RECTS = {
    'fig_amine_examples': (0, (235, 540, 515, 578)),
    'fig_9_1_trimethylamine': (1, (225, 88, 470, 296)),
    'fig_1_2_3_amines': sd(1, 185, 390, 420, 445),
    'tab_9_1_names': (2, (40, 185, 525, 698)),
    'fig_nitro_reduction': (3, (180, 322, 440, 420)),
    'fig_ammonolysis_step': (3, (255, 640, 470, 688)),
    'fig_ammonolysis_series': sd(4, 140, 60, 390, 90),
    'fig_free_amine': (4, (160, 152, 510, 174)),
    'fig_ex91_solution': (4, (40, 325, 545, 454)),
    'fig_nitrile_reduction': (4, (145, 560, 420, 596)),
    'fig_amide_reduction': sd(4, 145, 555, 320, 590),
    'fig_gabriel_1': (5, (60, 158, 530, 248)),
    'fig_gabriel_2': (5, (60, 262, 530, 354)),
    'fig_hoffmann': (5, (140, 466, 545, 502)),
    'fig_ex92_solution': sd(5, 45, 460, 460, 585),
    'fig_9_2_hbond': sd(7, 200, 85, 380, 175),
    'tab_9_2_bp': (7, (58, 270, 540, 418)),
    'fig_amine_salt': sd(7, 170, 520, 380, 590),
    'fig_amine_water_base': (8, (155, 222, 400, 246)),
    'fig_kb_expression': sd(8, 140, 215, 300, 330),
    'tab_9_3_pkb': (8, (34, 482, 512, 698)),
    'fig_protonation': (9, (240, 235, 460, 368)),
    'fig_solvation_order': sd(9, 160, 485, 460, 590),
    'fig_aniline_resonance': sd(10, 140, 330, 450, 425),
    'fig_acetylation': sd(11, 140, 305, 460, 500),
    'fig_benzoylation': (11, (140, 605, 520, 636)),
    'fig_carbylamine': (12, (125, 140, 475, 164)),
    'fig_nitrous_primary': (12, (155, 255, 545, 282)),
    'fig_diazotisation_aniline': (12, (170, 332, 545, 362)),
    'fig_hinsberg_primary': sd(12, 150, 425, 460, 490),
    'fig_hinsberg_secondary': sd(12, 150, 545, 460, 605),
    'fig_tribromoaniline': sd(13, 180, 255, 420, 325),
    'fig_protection_bromination': sd(13, 160, 430, 460, 525),
    'fig_acetanilide_resonance': sd(13, 180, 575, 400, 605),
    'fig_aniline_nitration': sd(14, 150, 150, 460, 245),
    'fig_protected_nitration': sd(14, 130, 290, 460, 375),
    'fig_sulphanilic': sd(14, 150, 430, 460, 525),
    'fig_diazonium_resonance': (15, (200, 492, 470, 588)),
    'fig_diazotisation': (15, (165, 670, 525, 696)),
    'fig_sandmeyer': (16, (180, 288, 440, 362)),
    'fig_gattermann': (16, (180, 433, 410, 478)),
    'fig_iodide': (16, (150, 552, 440, 576)),
    'fig_fluoride': (16, (150, 615, 450, 642)),
    'fig_replace_h': (17, (205, 62, 545, 110)),
    'fig_replace_oh': (17, (180, 148, 470, 172)),
    'fig_replace_no2': sd(17, 150, 185, 460, 245),
    'fig_coupling_phenol': sd(17, 50, 380, 460, 430),
    'fig_coupling_aniline': sd(17, 40, 440, 460, 490),
    'fig_ex95_solution': (18, (40, 130, 505, 368)),
}
export(PDF, RECTS, MEDIA, long_side=1000)
