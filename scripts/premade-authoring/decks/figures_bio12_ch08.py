"""Crops the figures for Biology 12 Ch 8 (Microbes in Human Welfare). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'bio12', 'lebo108.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Biology', 'class12-biology-ch08-microbes-in-human-welfare', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_8_1_bacteria': (1, (50, 76, 219, 380)),
    'fig_8_2_viruses': (1, (270, 80, 535, 385)),
    'fig_8_3_colonies': (1, (94, 460, 540, 676)),
    'fig_8_4_fermentors': (3, (58, 80, 274, 250)),
    'fig_8_5_fermentation_plant': (3, (58, 275, 263, 455)),
    'fig_8_6_secondary_treatment': (5, (57, 80, 296, 265)),
    'fig_8_7_sewage_plant': (6, (298, 80, 513, 222)),
    'fig_8_8_biogas_plant': (7, (55, 75, 368, 350)),
}, MEDIA, long_side=1000)
