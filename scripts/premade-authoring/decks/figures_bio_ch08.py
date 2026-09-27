"""Crops the figures for Biology 11 Ch 8 (Cell: The Unit of Life). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'bio11', 'kebo108.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch08-cell-the-unit-of-life', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_8_1_cell_shapes': (4, (35, 95, 522, 450)),
    'fig_8_2_cell_sizes': (5, (60, 100, 292, 302)),
    'fig_8_3a_plant_cell': (7, (95, 95, 510, 425)),
    'fig_8_3b_animal_cell': (7, (95, 425, 510, 695)),
    'fig_8_4_fluid_mosaic': (8, (60, 440, 490, 700)),
    'fig_8_5_er': (10, (290, 100, 525, 452)),
    'fig_8_6_golgi': (10, (290, 462, 525, 690)),
    'fig_8_7_mitochondrion': (12, (50, 92, 392, 292)),
    'fig_8_8_chloroplast': (13, (55, 92, 312, 235)),
    'fig_8_9_ribosome': (13, (50, 498, 250, 612)),
    'fig_8_10_cilium': (14, (50, 92, 490, 296)),
    'fig_8_11_nucleus': (15, (52, 290, 320, 462)),
    'fig_8_12_kinetochore': (16, (375, 98, 522, 370)),
    'fig_8_13_chromosome_types': (16, (40, 455, 490, 688)),
}, MEDIA, long_side=1000)
