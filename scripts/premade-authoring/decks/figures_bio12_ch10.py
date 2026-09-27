"""Crops the figures for Biology 12 Ch 10 (Biotechnology and its Applications). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'bio12', 'lebo110.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Biology', 'class12-biology-ch10-biotechnology-and-its-applications', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_10_1_cotton_boll': (3, (170, 185, 532, 405)),
    'fig_10_2_rnai_roots': (4, (100, 78, 452, 256)),
    'fig_10_3_proinsulin': (5, (55, 78, 240, 232)),
}, MEDIA, long_side=1000)
