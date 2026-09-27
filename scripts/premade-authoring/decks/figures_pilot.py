"""Crops the figures for the Chemistry 11 Ch 4, Physics 11 Ch 4 and Maths 11 Ch 3 pilot decks.

Usage: python scripts/premade-authoring/decks/figures_pilot.py   (PDFs in NCERT-pdfs/)
Rects are (page index, (x0, y0, x1, y1)) in PDF points. Mask boxes in the deck
scripts are pixels of these exact crops; re-measure if a crop changes.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from PIL import Image
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = lambda name: os.path.join(ROOT, 'NCERT-pdfs', name)
MEDIA = lambda cls, subject, deck: os.path.join(ROOT, 'premade-cards', cls, subject, deck, 'media')

CHEM = MEDIA('11th', 'Chemistry', 'class11-chemistry-ch04-chemical-bonding')
PHY = MEDIA('11th', 'Physics', 'class11-physics-ch04-laws-of-motion')
MATH = MEDIA('11th', 'Mathematics', 'class11-mathematics-ch03-trigonometric-functions')
for folder in (CHEM, PHY, MATH):
    os.makedirs(folder, exist_ok=True)

export(PDF('kech104.pdf'), {
    'tab_4_1_lewis_o3': (3, (358, 564, 530, 593)), 'tab_4_1_lewis_nf3': (3, (358, 593, 530, 623)),
    'tab_4_1_lewis_co3': (3, (358, 623, 530, 659)), 'tab_4_1_lewis_hno3': (3, (358, 659, 530, 691)),
    'fig_4_2_cl2_radii': (7, (303, 483, 533, 652)), 'rock_salt': (6, (315, 380, 525, 552)),
    'fig_4_3_o3_resonance': (9, (303, 88, 537, 268)), 'fig_4_4_co3_resonance': (10, (58, 340, 287, 423)),
    'fig_4_5_co2_resonance': (10, (303, 95, 533, 137)), 'h2o_dipole': (11, (330, 250, 515, 337)),
    'bf3_dipole': (11, (315, 555, 532, 647)), 'nh3_nf3_dipole': (12, (55, 240, 302, 377)),
    'tab_4_6_geometry': (14, (295, 160, 525, 672)), 'tab_4_7_shapes': (15, (60, 120, 532, 714)),
    'fig_4_8_h2_energy': (18, (305, 270, 532, 416)), 'fig_4_9_overlaps': (19, (303, 88, 535, 427)),
    'ss_overlap': (20, (60, 368, 292, 417)), 'sp_overlap': (20, (55, 480, 297, 528)),
    'pp_overlap': (20, (55, 578, 297, 617)), 'pi_overlap': (20, (303, 118, 537, 217)),
    'fig_4_10_becl2_sp': (21, (303, 195, 537, 362)), 'fig_4_11_bcl3_sp2': (21, (303, 512, 537, 690)),
    'fig_4_12_ch4_sp3': (22, (58, 360, 292, 600)), 'fig_4_13_nh3': (22, (328, 280, 512, 396)),
    'fig_4_14_h2o': (22, (328, 598, 512, 702)), 'fig_4_15_ethene': (23, (95, 355, 482, 697)),
    'fig_4_16_ethyne': (24, (58, 335, 215, 690)), 'fig_4_17_pcl5': (25, (58, 175, 287, 333)),
    'fig_4_18_sf6': (25, (303, 300, 533, 463)), 'fig_4_19_lcao': (26, (303, 330, 533, 537)),
    'fig_4_20_mo_contours': (28, (58, 95, 533, 607)), 'fig_4_22_o_nitrophenol': (32, (330, 205, 507, 307)),
}, CHEM, long_side=1000)

# s–s, s–p and p–p sigma overlaps stacked into one image.
parts = [Image.open(os.path.join(CHEM, f'{n}.webp')).convert('RGB') for n in ('ss_overlap', 'sp_overlap', 'pp_overlap')]
width, gap = max(p.width for p in parts), 24
sheet = Image.new('RGB', (width, sum(p.height for p in parts) + gap * 2), 'white')
y = 0
for part in parts:
    sheet.paste(part, ((width - part.width) // 2, y))
    y += part.height + gap
sheet.save(os.path.join(CHEM, 'sigma_overlaps.webp'), 'WEBP', quality=82, method=6)
for n in ('ss_overlap', 'sp_overlap', 'pp_overlap'):
    os.remove(os.path.join(CHEM, f'{n}.webp'))

export(PDF('keph104.pdf'), {
    'fig_4_1a_galileo_planes': (1, (330, 255, 555, 323)), 'fig_4_1b_double_incline': (1, (365, 540, 515, 660)),
    'fig_4_3_catch': (4, (338, 285, 492, 442)), 'fig_4_4_stone_string': (5, (108, 315, 305, 482)),
    'fig_4_6_billiard': (8, (47, 235, 287, 347)), 'fig_4_7_force_triangle': (9, (330, 72, 557, 167)),
    'fig_4_8_hanging_mass': (9, (330, 515, 557, 627)), 'fig_4_10_friction': (11, (95, 515, 300, 592)),
    'fig_4_11_incline': (12, (55, 592, 265, 692)), 'fig_4_12_block_trolley': (12, (295, 450, 547, 667)),
    'fig_4_13_bearings': (13, (175, 505, 462, 657)), 'fig_4_14b_banked_components': (14, (379, 280, 522, 383)),
    'fig_4_15_fbd': (16, (295, 285, 517, 492)),
}, PHY, long_side=1000)

export(PDF('kemh103.pdf'), {
    'fig_3_4_radian': (2, (40, 185, 168, 307)), 'fig_3_6_unit_circle': (6, (222, 407, 428, 592)),
    'fig_3_8_sin': (11, (60, 245, 410, 332)), 'fig_3_9_cos': (11, (60, 356, 410, 437)),
    'fig_3_10_tan': (11, (40, 455, 235, 598)), 'fig_3_11_cot': (11, (235, 455, 425, 600)),
    'fig_3_12_sec': (12, (40, 90, 215, 252)), 'fig_3_13_cosec': (12, (240, 90, 428, 252)),
}, MATH, long_side=900)
