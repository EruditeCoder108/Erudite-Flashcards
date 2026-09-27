"""Crops the figures for Biology 12 Ch 4 (Principles of Inheritance and Variation). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'bio12', 'lebo104.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Biology', 'class12-biology-ch04-principles-of-inheritance-and-variation', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_4_1_seven_traits': (3, (48, 80, 295, 580)),
    'fig_4_2_making_cross': (4, (262, 70, 512, 555)),
    'fig_4_3_monohybrid': (5, (40, 68, 312, 448)),
    'fig_4_4_punnett_monohybrid': (6, (288, 70, 515, 540)),
    'fig_4_5_test_cross': (8, (30, 70, 540, 328)),
    'fig_4_6_snapdragon': (9, (50, 78, 290, 558)),
    'fig_4_7_dihybrid': (12, (38, 70, 440, 675)),
    'fig_4_8_meiosis_germ_cells': (14, (40, 500, 420, 668)),
    'fig_4_9_independent_assortment': (15, (165, 345, 548, 690)),
    'fig_4_10_drosophila': (16, (385, 80, 520, 200)),
    'fig_4_11_linkage': (17, (70, 110, 520, 650)),
    'fig_4_12_sex_determination': (19, (40, 60, 302, 418)),
    'fig_4_13_honey_bee': (20, (248, 470, 540, 590)),
    'fig_4_13_pedigree_symbols': (21, (55, 222, 260, 550)),
    'fig_4_14_pedigrees': (22, (40, 400, 520, 570)),
    'fig_4_15_sickle_cell': (23, (55, 420, 530, 665)),
    'fig_4_16_down_syndrome': (25, (124, 70, 530, 240)),
    'fig_4_17_klinefelter_turner': (25, (40, 270, 260, 540)),
}, MEDIA, long_side=1000)

# White out page-number tabs and corner ornaments caught in some crops.
from PIL import Image, ImageDraw
for name, box in [('fig_4_11_linkage', (0, 880, 40, 1001)), ('fig_4_12_sex_determination', (0, 0, 200, 48)), ('fig_4_3_monohybrid', (0, 0, 200, 30)), ('fig_4_11_linkage', (150, 0, 834, 28)),
                  ('fig_4_15_sickle_cell', (0, 380, 90, 480)), ('fig_4_5_test_cross', (930, 0, 1001, 22))]:
    p = os.path.join(MEDIA, name + '.webp')
    im = Image.open(p).convert('RGB'); ImageDraw.Draw(im).rectangle(box, fill='white'); im.save(p, quality=85)
