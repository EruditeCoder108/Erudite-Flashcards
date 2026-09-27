"""Crops the figures for Biology 11 Ch 14 (Breathing and Exchange of Gases). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'bio11', 'kebo114.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch14-breathing-and-exchange-of-gases', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_14_1_respiratory_system': (3, (70, 418, 530, 683)),
    'fig_14_2_breathing': (5, (57, 106, 300, 560)),
    'fig_14_3_gas_exchange': (7, (109, 105, 481, 408)),
    'fig_14_4_alveolus': (7, (56, 512, 316, 664)),
    'fig_14_5_odc': (8, (284, 358, 507, 582)),
}, MEDIA, long_side=1000)
