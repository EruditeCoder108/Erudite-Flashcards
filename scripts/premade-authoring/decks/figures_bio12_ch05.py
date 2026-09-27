"""Crops the figures for Biology 12 Ch 5 (Molecular Basis of Inheritance). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'bio12', 'lebo105.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Biology', 'class12-biology-ch05-molecular-basis-of-inheritance', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_5_1_polynucleotide': (1, (100, 570, 530, 690)),
    'fig_5_2_double_strand': (3, (60, 70, 515, 288)),
    'fig_5_3_double_helix': (3, (40, 304, 310, 592)),
    'fig_5_x_central_dogma': (3, (240, 630, 532, 705)),
    'fig_5_4a_nucleosome': (4, (307, 110, 515, 316)),
    'fig_5_4b_beads_on_string': (4, (300, 338, 515, 490)),
    'fig_5_5_hershey_chase': (7, (120, 240, 535, 595)),
    'fig_5_6_semiconservative': (9, (45, 255, 258, 572)),
    'fig_5_7_meselson_stahl': (10, (40, 380, 510, 612)),
    'fig_5_8_replication_fork': (12, (300, 75, 515, 318)),
    'fig_5_9_transcription_unit': (13, (60, 300, 510, 436)),
    'fig_5_10_transcription_bacteria': (14, (55, 450, 400, 690)),
    'fig_5_11_transcription_eukaryotes': (15, (195, 405, 535, 690)),
    'table_5_1_codons': (17, (225, 201, 480, 432)),
    'fig_5_12_trna': (19, (60, 295, 432, 447)),
    'fig_5_13_translation': (20, (240, 75, 520, 277)),
    'fig_5_14_lac_operon': (22, (70, 75, 470, 365)),
    'fig_5_15_hgp': (24, (250, 456, 520, 680)),
    'fig_5_16_dna_fingerprinting': (28, (50, 85, 500, 522)),
}, MEDIA, long_side=1000)

# White out page-number tabs and corner ornaments caught in some crops.
from PIL import Image, ImageDraw
for name, box in [('fig_5_15_hgp', (835, 560, 1001, 730)), ('fig_5_2_double_strand', (0, 0, 45, 22)),
                  ('fig_5_7_meselson_stahl', (925, 440, 1001, 495))]:
    p = os.path.join(MEDIA, name + '.webp')
    im = Image.open(p).convert('RGB'); ImageDraw.Draw(im).rectangle(box, fill='white'); im.save(p, quality=85)
