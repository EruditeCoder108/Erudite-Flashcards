"""Crops the figures for Chemistry 11 Ch 7 (Redox Reactions). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'chem11', 'kech201.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Chemistry', 'class11-chemistry-ch07-redox-reactions', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_7_1_zn_in_cu_nitrate': (3, (62, 612, 535, 705)),
    'fig_7_2_cu_in_silver_nitrate': (4, (62, 93, 535, 185)),
    'tab_highest_oxidation_numbers': (6, (58, 92, 531, 179)),
    'fig_7_3_daniell_cell': (15, (60, 434, 289, 621)),
    'tab_7_1_electrode_potentials': (16, (60, 195, 536, 710)),
}, MEDIA, long_side=1000)
