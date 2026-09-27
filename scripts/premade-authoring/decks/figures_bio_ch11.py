"""Crops the figures for Biology 11 Ch 11 (Photosynthesis in Higher Plants). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'bio11', 'kebo111.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch11-photosynthesis-in-higher-plants', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_11_1_priestley': (3, (62, 102, 270, 447)),
    'fig_11_2_chloroplast': (5, (88, 495, 530, 682)),
    'fig_11_3_spectra': (6, (297, 146, 519, 586)),
    'fig_11_4_lhc': (7, (58, 290, 290, 488)),
    'fig_11_5_z_scheme': (8, (276, 108, 520, 318)),
    'fig_11_6_cyclic': (9, (56, 131, 271, 303)),
    'fig_11_7_chemiosmosis': (10, (73, 101, 460, 400)),
    'fig_11_8_calvin': (13, (118, 117, 465, 512)),
    'fig_11_9_hatch_slack': (15, (189, 326, 491, 697)),
    'fig_11_10_light_curve': (18, (298, 470, 522, 662)),
}, MEDIA, long_side=1000)
