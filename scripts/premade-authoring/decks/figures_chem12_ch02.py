"""Crops the figures for Chemistry 12 Ch 2 (Electrochemistry). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'chem12', 'lech102.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Chemistry', 'class12-chemistry-ch02-electrochemistry', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_2_1_daniell_cell': (1, (58, 98, 296, 327)),
    'fig_2_2_external_voltage': (1, (63, 366, 540, 667)),
    'fig_2_3_she': (3, (60, 480, 280, 682)),
    'tab_2_1_electrode_potentials': (6, (40, 60, 520, 660)),
    'fig_2_4_conductivity_cells': (12, (150, 434, 505, 578)),
    'fig_2_5_wheatstone': (13, (55, 365, 262, 540)),
    'tab_2_3_kcl_conductivity': (13, (170, 222, 537, 352)),
    'fig_2_6_molar_conductivity': (16, (40, 232, 290, 468)),
    'fig_2_7_kcl_plot': (17, (160, 428, 440, 652)),
    'tab_2_4_ion_conductivity': (18, (155, 390, 518, 522)),
    'fig_2_8_dry_cell': (23, (70, 398, 205, 637)),
    'fig_2_9_mercury_cell': (24, (135, 55, 312, 202)),
    'fig_2_10_lead_storage': (24, (180, 460, 500, 678)),
    'fig_2_11_nicd': (25, (170, 52, 352, 208)),
    'fig_2_12_fuel_cell': (25, (62, 382, 330, 568)),
    'fig_2_13_corrosion': (26, (38, 200, 325, 357)),
}, MEDIA, long_side=1000)

# White out neighbouring body text that shares the crop.
from PIL import Image, ImageDraw
for name, box in [('fig_2_1_daniell_cell', (480, 0, 1001, 80)), ('fig_2_13_corrosion', (660, 0, 1001, 345))]:
    p = os.path.join(MEDIA, name + '.webp')
    im = Image.open(p).convert('RGB'); ImageDraw.Draw(im).rectangle(box, fill='white'); im.save(p, quality=85)
