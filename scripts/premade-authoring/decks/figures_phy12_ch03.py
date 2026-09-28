"""Crops the figures for Physics 12 Ch 3 (Current Electricity). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'phy12', 'leph103.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Physics', 'class12-physics-ch03-current-electricity', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_3_1_cylinder': (2, (300, 135, 538, 190)),
    'fig_3_2_slabs': (2, (428, 390, 538, 612)),
    'fig_3_3_drift_path': (4, (348, 424, 537, 595)),
    'fig_3_4_current_cylinder': (5, (72, 255, 280, 330)),
    'fig_3_5_ohmic': (8, (390, 99, 536, 221)),
    'fig_3_6_diode': (8, (58, 358, 232, 523)),
    'fig_3_7_gaas': (8, (342, 396, 531, 523)),
    'fig_3_8_copper': (9, (80, 460, 200, 580)),
    'fig_3_9_nichrome': (9, (236, 478, 368, 578)),
    'fig_3_10_semiconductor': (9, (418, 478, 558, 596)),
    'fig_3_11_cell_resistor': (12, (333, 188, 536, 293)),
    'fig_3_12_cell': (13, (75, 98, 215, 298)),
    'fig_3_15_kirchhoff': (17, (75, 99, 292, 239)),
    'fig_3_16_cube': (17, (195, 420, 455, 697)),
    'fig_3_17_network': (18, (140, 525, 342, 706)),
    'fig_3_18_wheatstone': (20, (396, 99, 537, 289)),
    'fig_3_19_example': (20, (155, 538, 330, 709)),
    'fig_3_20_exercise': (25, (298, 258, 434, 441)),
}, MEDIA, long_side=1000)
