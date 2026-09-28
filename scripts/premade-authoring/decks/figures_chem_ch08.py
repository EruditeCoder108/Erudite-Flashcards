"""Crops the figures for Chemistry 11 Ch 8 (Organic Chemistry: Some Basic Principles and Techniques). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'chem11', 'kech202.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Chemistry', 'class11-chemistry-ch08-organic-chemistry-basic-principles', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_8_1_wedge_dash': (4, (80, 583, 268, 704)),
    'fig_8_2_models': (4, (306, 445, 533, 696)),
    'tab_8_1_common_names': (6, (306, 320, 532, 558)),
    'tab_8_2_alkanes': (7, (61, 452, 291, 575)),
    'tab_8_3_alkyl_groups': (7, (306, 222, 535, 356)),
    'fig_8_3a_carbocation': (16, (100, 165, 205, 268)),
    'fig_8_3b_carbanion': (16, (140, 456, 206, 545)),
    'fig_8_4a_hyperconj_cation': (21, (315, 300, 528, 420)),
    'fig_8_4b_hyperconj_propene': (22, (70, 222, 272, 330)),
    'fig_8_5_simple_distillation': (23, (297, 188, 537, 438)),
    'fig_8_6_fractional_distillation': (24, (58, 95, 336, 398)),
    'fig_8_7_fractionating_columns': (24, (355, 437, 504, 699)),
    'fig_8_8_reduced_pressure': (25, (110, 92, 485, 364)),
    'fig_8_9_steam_distillation': (26, (133, 94, 500, 376)),
    'fig_8_10_differential_extraction': (26, (305, 405, 535, 595)),
    'fig_8_11_column_chromatography': (27, (70, 306, 238, 519)),
    'fig_8_12_tlc': (27, (330, 245, 528, 530)),
    'fig_8_13_paper_chromatography': (28, (72, 393, 280, 677)),
    'fig_8_14_c_h_estimation': (30, (115, 94, 477, 207)),
    'fig_8_15_dumas': (31, (89, 93, 489, 335)),
    'fig_8_16_kjeldahl': (32, (81, 92, 520, 337)),
    'fig_8_17_carius': (33, (92, 254, 205, 495)),
}, MEDIA, long_side=1000)

# The functional-group table is dense: export it larger.
export(PDF, {'tab_8_4_functional_groups': (11, (89, 108, 505, 718))}, MEDIA, long_side=1500)

# White out a caption between the TLC panels and body text beside the fractional-distillation figure.
from PIL import Image, ImageDraw
for name, box in [('fig_8_12_tlc', (0, 432, 696, 505)), ('fig_8_6_fractional_distillation', (805, 0, 918, 130))]:
    p = os.path.join(MEDIA, name + '.webp')
    im = Image.open(p).convert('RGB'); ImageDraw.Draw(im).rectangle(box, fill='white'); im.save(p, quality=85)
