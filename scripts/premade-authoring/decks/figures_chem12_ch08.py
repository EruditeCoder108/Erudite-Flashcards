"""Crops the figures for Chemistry 12 Ch 8 (Aldehydes, Ketones and Carboxylic Acids).
Most rects were read off contact-sheet display pixels (tile-relative) and converted to PDF points by `sd`; plain tuples are already points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'chem12', 'lech203.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Chemistry', 'class12-chemistry-ch08-aldehydes-ketones-and-carboxylic-acids', 'media')
os.makedirs(MEDIA, exist_ok=True)


def sd(page, x0, y0, x1, y1, pad=4):
    fx = lambda d: 50 + (d - 48) / 0.876
    fy = lambda d: 50 + (d - 60) / 0.844
    return (page, (round(fx(x0)) - pad, round(fy(y0)) - pad, round(fx(x1)) + pad, round(fy(y1)) + pad))


RECTS = {
    'fig_general_formulas': sd(0, 205, 495, 460, 612),
    'fig_ester_anhydride': sd(1, 200, 55, 380, 110),
    'fig_fragrant_aldehydes': sd(1, 155, 165, 445, 262),
    'fig_common_aldehydes': sd(1, 155, 540, 460, 590),
    'fig_common_ketones': sd(2, 130, 155, 455, 225),
    'fig_iupac_examples': (2, (100, 506, 570, 690)),
    'fig_iupac_examples2': sd(3, 130, 55, 500, 200),
    'tab_8_1_names': (3, (55, 275, 540, 700)),
    'fig_8_1_carbonyl_orbitals': (4, (100, 160, 520, 262)),
    'fig_carbonyl_resonance': sd(4, 40, 270, 195, 340),
    'fig_rosenmund': sd(5, 160, 180, 450, 225),
    'fig_stephen': sd(5, 160, 285, 450, 318),
    'fig_dibal_nitrile': sd(5, 130, 360, 480, 410),
    'fig_dibal_ester': (5, (160, 496, 505, 536)),
    'fig_etard': sd(6, 95, 55, 460, 110),
    'fig_cro3_acetic_anhydride': (6, (25, 197, 524, 275)),
    'fig_side_chain_chlorination': sd(6, 130, 300, 450, 355),
    'fig_gattermann_koch': sd(6, 170, 425, 450, 480),
    'fig_dialkylcadmium': (6, (140, 634, 500, 700)),
    'fig_nitrile_grignard': sd(7, 50, 90, 460, 145),
    'fig_friedel_crafts_acylation': sd(7, 170, 235, 460, 300),
    'fig_bp_table': (8, (190, 210, 490, 312)),
    'fig_carbonyl_water_hbond': (8, (215, 360, 455, 415)),
    'fig_8_2_nucleophilic_addition': (9, (0, 175, 370, 425)),
    'fig_benzaldehyde_resonance': sd(9, 100, 560, 280, 600),
    'fig_hcn_addition': (10, (37, 82, 258, 226)),
    'fig_bisulphite': (10, (35, 260, 420, 345)),
    'fig_acetal': sd(10, 40, 445, 330, 510),
    'fig_ketal': sd(10, 40, 540, 330, 590),
    'fig_ammonia_derivatives': sd(11, 50, 145, 460, 200),
    'tab_8_2_derivatives': (11, (55, 255, 540, 565)),
    'fig_clemmensen': (12, (135, 100, 522, 133)),
    'fig_wolff_kishner': (12, (135, 145, 512, 204)),
    'fig_ketone_oxidation': sd(12, 160, 315, 460, 390),
    'fig_tollens': sd(12, 130, 475, 460, 492),
    'fig_fehling': sd(12, 180, 580, 460, 605),
    'fig_haloform': (13, (48, 104, 398, 226)),
    'fig_ex84_dnp': sd(13, 90, 510, 460, 595),
    'fig_ex84_iodoform': sd(14, 60, 50, 450, 110),
    'fig_alpha_h_acidity': sd(14, 150, 235, 400, 290),
    'fig_aldol_ethanal': sd(14, 130, 340, 460, 395),
    'fig_aldol_propanone': sd(14, 100, 420, 460, 490),
    'fig_cross_aldol': sd(15, 110, 105, 460, 280),
    'fig_claisen_schmidt': sd(15, 140, 325, 460, 375),
    'fig_cannizzaro_hcho': sd(15, 100, 480, 460, 540),
    'fig_cannizzaro_benzaldehyde': sd(15, 100, 550, 460, 595),
    'fig_benzaldehyde_nitration': sd(16, 170, 88, 400, 155),
    'tab_8_3_acid_names': (17, (60, 470, 540, 702)),
    'tab_8_3_aromatic_acids': (18, (40, 45, 520, 213)),
    'fig_carboxyl_resonance': sd(18, 150, 245, 400, 295),
    'fig_jones': sd(18, 180, 540, 460, 590),
    'fig_alkylbenzene_oxidation': sd(19, 110, 175, 460, 290),
    'fig_nitrile_amide_hydrolysis': (19, (197, 407, 524, 545)),
    'fig_grignard_co2': sd(19, 110, 525, 460, 570),
    'fig_acyl_halide_anhydride_hydrolysis': sd(20, 150, 150, 450, 275),
    'fig_ester_hydrolysis': sd(20, 130, 340, 460, 460),
    'fig_ex85_solution': sd(21, 50, 60, 460, 500),
    'fig_acid_dimer_hbond': sd(22, 40, 90, 190, 300),
    'fig_acid_metals_bases': sd(22, 130, 410, 460, 485),
    'fig_carboxylate_resonance': (22, (165, 596, 515, 674)),
    'fig_ewg_edg': sd(23, 170, 530, 460, 600),
    'fig_vinyl_phenyl_acid': sd(24, 150, 255, 400, 285),
    'fig_substituted_benzoic_pka': sd(24, 150, 335, 400, 420),
    'fig_anhydride_formation': sd(24, 160, 500, 450, 545),
    'fig_esterification_mechanism': sd(25, 70, 60, 460, 285),
    'fig_pcl5_socl2': (25, (197, 428, 513, 494)),
    'fig_acid_ammonia': sd(25, 150, 490, 460, 590),
    'fig_phthalimide': sd(26, 110, 60, 460, 235),
    'fig_acid_reduction': sd(26, 160, 318, 460, 337),
    'fig_decarboxylation': sd(26, 160, 402, 460, 422),
    'fig_hvz': sd(26, 150, 545, 460, 605),
    'fig_ring_substitution_acid': sd(27, 100, 150, 460, 200),
}
export(PDF, RECTS, MEDIA, long_side=1000)
