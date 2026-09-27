"""Crops the figures for Biology 11 Ch 18 (Neural Control and Coordination). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'bio11', 'kebo118.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch18-neural-control-and-coordination', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_18_1_neuron': (2, (50, 100, 270, 455)),
    'fig_18_2_impulse': (3, (80, 122, 413, 312)),
    'fig_18_3_synapse': (4, (151, 443, 482, 694)),
    'fig_18_4_brain': (5, (68, 440, 445, 688)),
}, MEDIA, long_side=1000)
