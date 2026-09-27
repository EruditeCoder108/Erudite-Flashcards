"""Crops the figures for Biology 12 Ch 1 (Sexual Reproduction in Flowering Plants). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'bio12', 'lebo101.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Biology', 'class12-biology-ch01-sexual-reproduction-in-flowering-plants', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_1_1_flower_ls': (3, (125, 67, 515, 398)),
    'fig_1_2_stamen_anther': (4, (285, 135, 515, 470)),
    'fig_1_3ab_anther_ts': (5, (50, 66, 532, 262)),
    'fig_1_3c_dehisced_anther': (5, (100, 262, 500, 468)),
    'fig_1_4_pollen_sem': (6, (39, 80, 400, 200)),
    'fig_1_5_pollen_maturation': (6, (348, 241, 535, 560)),
    'fig_1_7_pistil_ovule': (8, (37, 76, 515, 378)),
    'fig_1_8_embryo_sac': (9, (55, 70, 530, 493)),
    'fig_1_9a_self': (11, (95, 80, 225, 215)),
    'fig_1_9b_cross': (11, (90, 235, 230, 370)),
    'fig_1_9c_cleistogamous': (11, (98, 385, 265, 605)),
    'fig_1_10_wind': (12, (280, 80, 515, 405)),
    'fig_1_11a_vallisneria': (13, (55, 70, 335, 300)),
    'fig_1_11b_insect': (13, (78, 315, 290, 553)),
    'fig_1_12abc_pollen_tube': (15, (55, 70, 530, 312)),
    'fig_1_12de_egg_apparatus': (15, (55, 313, 530, 455)),
    'fig_1_13_embryo_stages': (17, (60, 273, 530, 535)),
    'fig_1_14_embryos': (18, (355, 70, 535, 560)),
    'fig_1_15a_seeds': (20, (20, 85, 530, 385)),
    'fig_1_15b_false_fruits': (20, (15, 395, 530, 575)),
}, MEDIA, long_side=1000)

# White out a stray text fragment that sits beside the first pollen circle.
from PIL import Image, ImageDraw
# Also whites out the page-corner leaf ornament that some crops catch.
for name, box in [('fig_1_5_pollen_maturation', (0, 0, 175, 75)), ('fig_1_3ab_anther_ts', (0, 0, 130, 24)),
                  ('fig_1_8_embryo_sac', (0, 0, 130, 24)), ('fig_1_12abc_pollen_tube', (0, 0, 130, 20)),
                  ('fig_1_14_embryos', (220, 0, 368, 22))]:
    p = os.path.join(MEDIA, name + '.webp')
    im = Image.open(p).convert('RGB'); ImageDraw.Draw(im).rectangle(box, fill='white'); im.save(p, quality=85)
