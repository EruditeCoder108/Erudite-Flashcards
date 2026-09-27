"""Crops the figures for Biology 12 Ch 9 (Biotechnology: Principles and Processes). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'bio12', 'lebo109.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Biology', 'class12-biology-ch09-biotechnology-principles-and-processes', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_9_1_ecori_action': (5, (60, 318, 530, 578)),
    'fig_9_2_rdna_technology': (6, (38, 335, 405, 690)),
    'fig_9_3_gel_electrophoresis': (7, (60, 300, 300, 437)),
    'fig_9_4_pbr322': (8, (285, 325, 510, 505)),
    'fig_9_5_dna_spooling': (10, (370, 295, 515, 570)),
    'fig_9_6_pcr': (11, (60, 330, 530, 678)),
    'fig_9_7_bioreactors': (13, (55, 265, 530, 492)),
}, MEDIA, long_side=1000)

# White out the page-number tab caught in Figure 9.6.
from PIL import Image, ImageDraw
p = os.path.join(MEDIA, 'fig_9_6_pcr.webp')
im = Image.open(p).convert('RGB'); ImageDraw.Draw(im).rectangle((0, 585, 78, 692), fill='white'); im.save(p, quality=85)
