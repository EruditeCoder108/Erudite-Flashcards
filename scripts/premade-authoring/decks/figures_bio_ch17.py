"""Crops the figures for Biology 11 Ch 17 (Locomotion and Movement). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'bio11', 'kebo117.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch17-locomotion-and-movement', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_17_1_muscle_cs': (2, (70, 250, 490, 505)),
    'fig_17_2_sarcomere': (3, (103, 326, 505, 678)),
    'fig_17_3_actin_myosin': (4, (27, 352, 462, 600)),
    'fig_17_4_cross_bridge': (5, (60, 300, 528, 548)),
    'fig_17_5_sliding_filament': (6, (61, 99, 500, 428)),
    'fig_17_6_skull': (7, (100, 300, 487, 572)),
    'fig_17_7_vertebral_column': (8, (273, 105, 520, 365)),
    'fig_17_8_rib_cage': (8, (263, 453, 518, 680)),
    'fig_17_9_pectoral_girdle': (9, (60, 98, 290, 382)),
    'fig_17_10_pelvic_girdle': (9, (60, 418, 290, 682)),
}, MEDIA, long_side=1000)
