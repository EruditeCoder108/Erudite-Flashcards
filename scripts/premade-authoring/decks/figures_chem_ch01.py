"""Crops the figures for Chemistry 11 Ch 1 (Some Basic Concepts of Chemistry). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'chem11', 'kech101.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Chemistry', 'class11-chemistry-ch01-some-basic-concepts-of-chemistry', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_1_1_states': (4, (59, 92, 291, 214)),
    'fig_1_2_classification': (4, (306, 93, 535, 214)),
    'fig_1_3_atoms_molecules': (5, (60, 295, 290, 488)),
    'fig_1_4_h2o_co2': (5, (306, 90, 537, 181)),
    'tab_1_3_prefixes': (8, (61, 108, 289, 450)),
    'fig_1_5_balance': (8, (306, 93, 533, 333)),
    'fig_1_6_volume_units': (8, (325, 512, 515, 689)),
    'fig_1_7_volume_devices': (9, (68, 186, 279, 359)),
    'fig_1_8_thermometers': (9, (315, 392, 524, 611)),
    'fig_1_9_avogadro_volumes': (15, (60, 93, 534, 215)),
    'fig_1_10_nacl': (16, (354, 449, 470, 566)),
    'fig_1_11_one_mole': (17, (305, 549, 534, 704)),
}, MEDIA, long_side=1000)
