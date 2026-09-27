"""Crops the figures for Biology 11 Ch 4 (Animal Kingdom). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'bio11', 'kebo104.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch04-animal-kingdom', 'media')
os.makedirs(MEDIA, exist_ok=True)

# Diagrams with examinable labels (masked in the deck).
export(PDF, {
    'fig_4_2_germ_layers': (1, (55, 520, 300, 680)),
    'fig_4_3_coelom': (2, (280, 155, 520, 404)),
    'fig_4_4_classification': (3, (66, 102, 526, 342)),
    'fig_4_7_cnidoblast': (4, (425, 478, 495, 612)),
    'fig_4_15_balanoglossus': (8, (405, 432, 505, 672)),
    'fig_4_16_chordata': (9, (55, 100, 292, 212)),
    'vertebrata_chart': (10, (108, 118, 460, 334)),
}, MEDIA, long_side=1000)

# Examples shown on ordinary cards.
export(PDF, {
    'fig_4_1a_radial': (1, (110, 110, 275, 268)), 'fig_4_1b_bilateral': (1, (44, 290, 280, 488)),
    'fig_4_5_porifera': (3, (50, 435, 290, 684)), 'fig_4_6_coelenterata': (4, (90, 205, 495, 440)),
    'fig_4_8_ctenophora': (5, (40, 100, 222, 348)), 'fig_4_9_platyhelminthes': (5, (170, 490, 462, 700)),
    'fig_4_10_roundworm': (6, (330, 92, 455, 315)), 'fig_4_11_annelida': (6, (325, 364, 512, 684)),
    'fig_4_12_arthropoda': (7, (65, 110, 300, 358)), 'fig_4_13_mollusca': (7, (75, 440, 300, 684)),
    'fig_4_14_echinodermata': (8, (345, 98, 490, 336)), 'fig_4_17_ascidia': (9, (148, 410, 236, 630)),
    'fig_4_18_petromyzon': (10, (276, 394, 518, 462)), 'fig_4_19_cartilaginous': (10, (280, 520, 520, 686)),
    'fig_4_20_bony_fishes': (11, (55, 100, 256, 345)), 'fig_4_21_amphibia': (11, (80, 448, 220, 636)),
    'fig_4_22_reptiles': (12, (38, 105, 525, 270)), 'fig_4_23_birds': (13, (40, 92, 536, 294)),
    'fig_4_24_mammals': (13, (55, 512, 536, 694)),
}, MEDIA, long_side=800)
