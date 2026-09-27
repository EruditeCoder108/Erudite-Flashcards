"""Crops the figures for Biology 12 Ch 7 (Human Health and Disease). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'bio12', 'lebo107.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Biology', 'class12-biology-ch07-human-health-and-disease', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_7_1_plasmodium': (5, (54, 75, 535, 612)),
    'fig_7_2_elephantiasis': (6, (320, 78, 512, 344)),
    'fig_7_3_ringworm': (6, (270, 410, 510, 530)),
    'fig_7_4_antibody': (8, (210, 290, 522, 530)),
    'fig_7_5_lymph_nodes': (11, (25, 80, 207, 300)),
    'fig_7_6_retrovirus': (12, (85, 80, 468, 532)),
    'fig_7_7_morphine': (15, (100, 545, 300, 695)),
    'fig_7_8_opium_poppy': (15, (300, 545, 500, 695)),
    'fig_7_9_cannabinoid': (16, (50, 210, 262, 365)),
    'fig_7_10_cannabis': (16, (340, 210, 475, 365)),
    'fig_7_11_datura': (16, (315, 389, 510, 585)),
}, MEDIA, long_side=1000)

# White out the corner ornament caught in Figure 7.1.
from PIL import Image, ImageDraw
p = os.path.join(MEDIA, 'fig_7_1_plasmodium.webp')
im = Image.open(p).convert('RGB'); ImageDraw.Draw(im).rectangle((0, 0, 70, 18), fill='white'); im.save(p, quality=85)
