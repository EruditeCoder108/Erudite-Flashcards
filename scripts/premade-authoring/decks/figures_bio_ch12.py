"""Crops the figures for Biology 11 Ch 12 (Respiration in Plants). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'bio11', 'kebo112.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch12-respiration-in-plants', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_12_1_glycolysis': (3, (57, 151, 298, 580)),
    'fig_12_2_fermentation': (4, (278, 392, 517, 647)),
    'fig_12_3_krebs': (6, (274, 101, 513, 325)),
    'fig_12_4_ets': (7, (54, 99, 324, 542)),
    'fig_12_5_atp_synthase': (8, (284, 127, 513, 300)),
    'fig_12_6_amphibolic': (10, (43, 98, 510, 460)),
}, MEDIA, long_side=1000)
