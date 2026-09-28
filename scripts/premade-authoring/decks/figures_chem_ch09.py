"""Crops the figures for Chemistry 11 Ch 9 (Hydrocarbons). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'chem11', 'kech203.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Chemistry', 'class11-chemistry-ch09-hydrocarbons', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_9_1_methane': (1, (340, 245, 490, 352)),
    'tab_9_1_nomenclature': (4, (60, 108, 536, 508)),
    'tab_9_2_alkane_mp_bp': (7, (58, 505, 534, 720)),
    'fig_9_2_sawhorse': (10, (325, 290, 515, 386)),
    'fig_9_3_newman': (10, (318, 573, 521, 710)),
    'fig_9_4_ethene_sigma': (11, (306, 505, 534, 627)),
    'fig_9_5_ethene_pi': (12, (60, 93, 537, 182)),
    'tab_alkynes_names': (19, (58, 644, 534, 722)),
    'fig_9_6_ethyne_orbitals': (20, (305, 162, 537, 358)),
    'fig_9_7_aromatic_rings': (26, (60, 212, 535, 336)),
    'fig_aromatic_polycyclic': (26, (305, 305, 536, 470)),
}, MEDIA, long_side=1000)
