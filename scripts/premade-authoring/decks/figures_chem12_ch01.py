"""Crops the figures for Chemistry 12 Ch 1 (Solutions). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'chem12', 'lech101.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Chemistry', 'class12-chemistry-ch01-solutions', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_1_1_henry_pressure': (6, (38, 228, 340, 366)),
    'fig_1_2_hcl_cyclohexane': (6, (40, 455, 225, 633)),
    'tab_1_2_henry_constants': (7, (58, 62, 540, 207)),
    'fig_1_3_ideal_raoult': (9, (95, 425, 280, 597)),
    'fig_1_4_vp_lowering': (11, (80, 295, 282, 440)),
    'fig_1_5_raoult_solvent': (12, (150, 62, 290, 218)),
    'fig_1_6_deviations': (13, (185, 62, 520, 215)),
    'fig_chcl3_acetone_hbond': (13, (205, 519, 340, 564)),
    'fig_1_7_bp_elevation': (16, (40, 48, 240, 218)),
    'fig_1_8_fp_depression': (17, (55, 340, 265, 545)),
    'tab_1_3_kb_kf': (18, (30, 505, 530, 698)),
    'fig_1_9_thistle_funnel': (19, (170, 530, 380, 700)),
    'fig_1_10_osmotic_pressure': (20, (38, 300, 265, 465)),
    'fig_1_11_reverse_osmosis': (22, (40, 250, 262, 368)),
    'fig_acetic_dimer': (23, (60, 145, 225, 212)),
    'tab_1_4_vant_hoff': (24, (130, 140, 522, 272)),
}, MEDIA, long_side=1000)

# White out the start of the next paragraph beside the acetic acid dimer.
from PIL import Image, ImageDraw
p = os.path.join(MEDIA, 'fig_acetic_dimer.webp')
im = Image.open(p).convert('RGB'); ImageDraw.Draw(im).rectangle((790, 330, im.width, im.height), fill='white'); ImageDraw.Draw(im).rectangle((0, 0, im.width, 18), fill='white'); im.save(p, quality=85)
