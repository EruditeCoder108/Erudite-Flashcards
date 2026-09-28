"""Crops the figures for Chemistry 11 Ch 5 (Thermodynamics). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'chem11', 'kech105.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Chemistry', 'class11-chemistry-ch05-thermodynamics', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_5_1_system_surroundings': (1, (85, 473, 234, 575)),
    'fig_5_2_open_closed_isolated': (1, (315, 435, 526, 683)),
    'fig_5_3_adiabatic': (2, (372, 464, 480, 594)),
    'fig_5_4_conducting_walls': (3, (316, 313, 484, 453)),
    'fig_5_5a_compression': (4, (306, 430, 534, 659)),
    'fig_5_5b_finite_steps': (5, (60, 445, 292, 659)),
    'fig_5_5c_reversible': (5, (305, 445, 535, 648)),
    'fig_5_6_extensive_intensive': (8, (330, 93, 480, 273)),
    'fig_5_7_bomb_calorimeter': (9, (326, 241, 509, 477)),
    'fig_5_8_constant_p_calorimeter': (10, (85, 284, 280, 544)),
    'tab_5_1_fusion_vaporisation': (11, (128, 511, 463, 701)),
    'tab_5_2_formation_enthalpies': (13, (107, 118, 477, 512)),
    'tab_5_3a_single_bonds': (18, (58, 390, 536, 562)),
    'tab_5_3b_multiple_bonds': (18, (94, 587, 499, 656)),
    'fig_5_9_born_haber': (19, (59, 376, 290, 690)),
    'fig_5_10a_exothermic': (22, (60, 93, 290, 246)),
    'fig_5_10b_endothermic': (22, (59, 333, 289, 481)),
    'fig_5_11_diffusion': (22, (317, 80, 525, 350)),
    'tab_5_4_spontaneity': (26, (59, 551, 534, 688)),
}, MEDIA, long_side=1000)

# White out the Fig. 5.6(a) caption that sits between the two panels.
from PIL import Image, ImageDraw
p = os.path.join(MEDIA, 'fig_5_6_extensive_intensive.webp')
im = Image.open(p).convert('RGB'); ImageDraw.Draw(im).rectangle((0, 445, 834, 530), fill='white'); im.save(p, quality=85)
