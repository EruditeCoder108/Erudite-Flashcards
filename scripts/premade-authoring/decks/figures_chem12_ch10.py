"""Crops the figures for Chemistry 12 Ch 10 (Biomolecules).
Rects read off 4-page contact sheets (display pixels, tile = position 0–3 on the sheet) and converted to PDF points by `c`; plain tuples are points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'chem12', 'lech205.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Chemistry', 'class12-chemistry-ch10-biomolecules', 'media')
os.makedirs(MEDIA, exist_ok=True)


def c(page, tile, x0, y0, x1, y1, pad=5):
    fx = lambda d: 50 + (d - tile * 500 - 50) * 1.145
    fy = lambda d: 50 + (d - 50) * 1.155
    return (page, (round(fx(x0)) - pad, round(fy(y0)) - pad, round(fx(x1)) + pad, round(fy(y1)) + pad))


RECTS = {
    'tab_10_1_monosaccharides': (1, (155, 486, 551, 610)),
    'fig_glucose_from_sucrose_starch': c(2, 1, 630, 60, 900, 150),
    'fig_glucose_hi': c(2, 1, 660, 257, 880, 302),
    'fig_glucose_oxime_hcn': c(2, 1, 645, 349, 955, 395),
    'fig_glucose_br2': c(2, 1, 660, 437, 820, 483),
    'fig_glucose_acetylation': c(2, 1, 660, 545, 880, 600),
    'fig_glucose_hno3': c(3, 2, 1175, 93, 1405, 165),
    'fig_glucose_fischer': c(3, 2, 1175, 215, 1420, 300),
    'fig_glyceraldehyde': c(3, 2, 1175, 450, 1440, 515),
    'fig_d_glucose_config': c(4, 3, 1650, 138, 1880, 218),
    'fig_glucose_cyclic': c(4, 3, 1650, 450, 1945, 570),
    'fig_pyranose_haworth': c(5, 0, 130, 125, 460, 220),
    'fig_fructose_open': c(5, 0, 395, 270, 462, 358),
    'fig_fructofuranose': c(5, 0, 160, 420, 465, 490),
    'fig_fructose_haworth': c(5, 0, 170, 520, 460, 605),
    'fig_sucrose': c(6, 1, 660, 262, 910, 368),
    'fig_maltose': c(6, 1, 670, 495, 910, 605),
    'fig_lactose': c(7, 2, 1180, 120, 1440, 230),
    'fig_amylose': c(7, 2, 1165, 430, 1450, 540),
    'fig_amylopectin': c(8, 3, 1530, 50, 1945, 215),
    'fig_cellulose': c(8, 3, 1640, 255, 1890, 440),
    'fig_alpha_amino_acid': c(9, 0, 382, 336, 470, 390),
    'tab_10_2_amino_acids_a': (9, (140, 590, 549, 694)),
    'tab_10_2_amino_acids_b': (10, (85, 60, 535, 520)),
    'fig_zwitter_ion': c(11, 2, 1050, 95, 1240, 145),
    'fig_peptide_bond': c(11, 2, 1050, 340, 1240, 395),
    'fig_10_1_alpha_helix': (12, (42, 125, 111, 403)),
    'fig_10_2_beta_sheet': (12, (60, 462, 235, 612)),
    'fig_10_3_protein_levels': (13, (60, 90, 535, 300)),
    'fig_10_4_haemoglobin': (13, (60, 335, 535, 610)),
    'tab_10_3_vitamins_a': (15, (164, 355, 566, 772)),
    'tab_10_3_vitamins_b': c(16, 3, 1640, 70, 1945, 120),
    'fig_ribose_deoxyribose': c(16, 3, 1660, 500, 1930, 585),
    'fig_bases': c(17, 0, 185, 92, 470, 285),
    'fig_10_5_nucleoside_nucleotide': (17, (185, 445, 525, 585)),
    'fig_10_6_dinucleotide': (18, (60, 60, 505, 300)),
    'fig_nucleic_chain': c(18, 1, 650, 308, 950, 352),
    'fig_10_7_dna_helix': (18, (62, 330, 160, 628)),
}
export(PDF, RECTS, MEDIA, long_side=1000)
