"""Crops the figures for Chemistry 11 Ch 3 (Classification of Elements and Periodicity). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'chem11', 'kech103.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Chemistry', 'class11-chemistry-ch03-classification-of-elements-and-periodicity', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'tab_3_1_triads': (1, (60, 363, 535, 458)),
    'tab_3_2_octaves': (1, (60, 602, 535, 717)),
    'tab_3_3_mendeleev_predictions': (2, (59, 554, 534, 717)),
    'fig_3_1_mendeleev_table': (3, (90, 93, 487, 718)),
    'fig_3_2_long_form': (5, (57, 92, 486, 726)),
    'tab_3_4_iupac_roots': (6, (305, 190, 535, 363)),
    'tab_3_5_elements_above_100': (6, (60, 395, 534, 717)),
    'fig_3_3_blocks': (9, (91, 95, 469, 718)),
    'tab_3_6a_radii_period': (12, (59, 513, 534, 579)),
    'tab_3_6b_radii_group': (12, (59, 608, 534, 717)),
    'fig_3_4a_radius_period': (13, (86, 93, 270, 287)),
    'fig_3_4b_radius_group': (13, (312, 94, 531, 289)),
    'fig_3_5_ie_vs_z': (14, (305, 93, 534, 252)),
    'fig_3_6_ie_period_group': (14, (60, 495, 536, 692)),
    'tab_3_7_electron_gain': (16, (59, 109, 534, 210)),
    'fig_3_7_trends': (17, (236, 228, 535, 442)),
    'tab_3_8a_en_period': (17, (61, 487, 535, 567)),
    'tab_3_8b_en_group': (17, (60, 591, 535, 717)),
    'tab_3_9_hydrides_oxides': (19, (60, 116, 535, 289)),
    'tab_valence_groups': (18, (59, 655, 534, 717)),
    'tab_anomalous_li_be': (19, (60, 548, 322, 717)),
}, MEDIA, long_side=1000)

# The three full-page tables are printed sideways: turn them upright.
from PIL import Image
for name in ('fig_3_1_mendeleev_table', 'fig_3_2_long_form', 'fig_3_3_blocks'):
    p = os.path.join(MEDIA, name + '.webp')
    im = Image.open(p).rotate(-90, expand=True)
    im.save(p, quality=88)
    print(name, 'rotated ->', im.size)
