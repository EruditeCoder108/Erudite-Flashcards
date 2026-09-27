"""Crops the figures for Biology 11 Ch 16 (Excretory Products and their Elimination). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'bio11', 'kebo116.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch16-excretory-products-and-their-elimination', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_16_1_urinary_system': (1, (63, 403, 305, 640)),
    'fig_16_2_kidney_ls': (2, (274, 100, 520, 310)),
    'fig_16_3_nephron': (2, (57, 404, 437, 684)),
    'fig_16_4_malpighian_body': (3, (80, 96, 315, 336)),
    'fig_16_5_reabsorption': (5, (99, 103, 509, 497)),
    'fig_16_6_counter_current': (6, (49, 281, 514, 687)),
}, MEDIA, long_side=1000)
