"""Crops the figures for Biology 12 Ch 6 (Evolution). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'bio12', 'lebo106.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Biology', 'class12-biology-ch06-evolution', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_6_1_miller': (2, (200, 55, 500, 340)),
    'fig_6_2_dinosaur_tree': (4, (55, 70, 535, 538)),
    'fig_6_3_homologous': (5, (246, 65, 535, 548)),
    'fig_6_4_peppered_moth': (6, (50, 80, 535, 225)),
    'fig_6_5_finches': (7, (80, 70, 495, 168)),
    'fig_6_6_marsupial_radiation': (7, (45, 365, 479, 690)),
    'fig_6_7_convergent': (8, (20, 75, 297, 530)),
    'fig_6_8_natural_selection': (10, (55, 240, 535, 680)),
    'fig_6_9_plant_evolution': (12, (50, 120, 530, 520)),
    'fig_6_10_vertebrate_evolution': (13, (35, 70, 525, 588)),
    'fig_6_11_skulls': (15, (100, 65, 480, 500)),
}, MEDIA, long_side=1000)

# White out page-number tabs, running heads and corner ornaments caught in some crops.
from PIL import Image, ImageDraw
for name, box in [('fig_6_8_natural_selection', (0, 740, 95, 870)), ('fig_6_1_miller', (930, 0, 1001, 45)),
                  ('fig_6_6_marsupial_radiation', (980, 540, 1001, 660)), ('fig_6_10_vertebrate_evolution', (870, 0, 947, 22)),
                  ('fig_6_9_plant_evolution', (900, 0, 1001, 20)), ('fig_6_3_homologous', (560, 0, 632, 25))]:
    p = os.path.join(MEDIA, name + '.webp')
    im = Image.open(p).convert('RGB'); ImageDraw.Draw(im).rectangle(box, fill='white'); im.save(p, quality=85)
