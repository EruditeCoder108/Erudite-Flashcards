"""Crops the figures for Biology 12 Ch 2 (Human Reproduction). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'bio12', 'lebo102.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Biology', 'class12-biology-ch02-human-reproduction', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_2_1a_male_pelvis': (1, (211, 70, 528, 262)),
    'fig_2_1b_male_system': (1, (213, 300, 520, 524)),
    'fig_2_2_seminiferous_tubule': (2, (150, 70, 500, 350)),
    'fig_2_3a_female_pelvis': (3, (38, 68, 510, 332)),
    'fig_2_3b_female_system': (3, (30, 466, 440, 688)),
    'fig_2_4_mammary_gland': (4, (150, 440, 530, 688)),
    'fig_2_5_spermatogenesis_tubule': (5, (270, 358, 520, 558)),
    'fig_2_6_sperm': (6, (50, 78, 296, 355)),
    'fig_2_7_ovary': (7, (240, 75, 515, 272)),
    'fig_2_8_gametogenesis': (7, (39, 343, 514, 570)),
    'fig_2_9_menstrual_cycle': (8, (75, 75, 530, 488)),
    'fig_2_10_ovum_sperms': (9, (226, 430, 508, 683)),
    'fig_2_11_cleavage_implantation': (10, (55, 362, 531, 688)),
    'fig_2_12_foetus': (11, (188, 440, 480, 680)),
}, MEDIA, long_side=1000)

# White out page-number tabs that sit inside two crops.
from PIL import Image, ImageDraw
for name, box in [('fig_2_10_ovum_sperms', (900, 600, 1001, 924)), ('fig_2_12_foetus', (970, 570, 1001, 740)), ('fig_2_3a_female_pelvis', (870, 0, 1001, 40)), ('fig_2_1a_male_pelvis', (780, 0, 1001, 30)), ('fig_2_7_ovary', (850, 0, 1001, 30)), ('fig_2_11_cleavage_implantation', (0, 520, 95, 711))]:
    p = os.path.join(MEDIA, name + '.webp')
    im = Image.open(p).convert('RGB'); ImageDraw.Draw(im).rectangle(box, fill='white'); im.save(p, quality=85)
