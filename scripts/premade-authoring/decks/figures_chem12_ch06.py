"""Crops the figures for Chemistry 12 Ch 6 (Haloalkanes and Haloarenes). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'chem12', 'lech201.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Chemistry', 'class12-chemistry-ch06-haloalkanes-and-haloarenes', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_mono_di_tri': (1, (170, 125, 536, 268)),
    'fig_alkyl_1_2_3': (1, (215, 467, 480, 536)),
    'fig_allylic': (1, (215, 617, 502, 662)),
    'fig_benzylic': (2, (205, 50, 422, 143)),
    'fig_vinylic': (2, (240, 202, 380, 236)),
    'fig_aryl': (2, (245, 277, 395, 316)),
    'tab_6_1_names': (3, (160, 225, 537, 572)),
    'tab_6_2_cx_bond': (5, (55, 60, 535, 190)),
    'fig_alcohol_to_halide': (5, (190, 385, 520, 540)),
    'fig_arene_halogenation': (7, (205, 180, 502, 240)),
    'fig_sandmeyer': (7, (240, 408, 502, 572)),
    'fig_diazonium_ki': (7, (245, 630, 502, 675)),
    'fig_6_1_boiling_points': (9, (185, 295, 495, 468)),
    'tab_6_3_density': (10, (40, 222, 520, 320)),
    'tab_6_4_nucleophiles': (11, (46, 280, 545, 622)),
    'fig_6_2_sn2': (12, (45, 352, 520, 410)),
    'fig_6_2_balls': (12, (100, 522, 520, 578)),
    'fig_configuration_box': (13, (182, 388, 433, 492)),
    'fig_6_3_steric_sn2': (14, (48, 90, 517, 248)),
    'fig_sn1_overall': (14, (168, 392, 510, 432)),
    'fig_sn1_mechanism': (14, (180, 535, 510, 650)),
    'fig_sn_reactivity_order': (15, (140, 170, 440, 245)),
    'fig_allyl_benzyl_resonance': (15, (60, 292, 520, 390)),
    'fig_6_4_chiral_objects': (17, (55, 205, 295, 436)),
    'fig_6_5_propan2ol': (17, (240, 485, 515, 598)),
    'fig_6_6_butan2ol': (18, (200, 58, 500, 176)),
    'fig_6_7_chiral_molecule': (18, (45, 215, 183, 280)),
    'fig_retention_example': (19, (150, 258, 532, 345)),
    'fig_retention_inversion': (19, (160, 490, 522, 593)),
    'fig_sn2_inversion_octane': (20, (205, 214, 402, 260)),
    'fig_sn1_racemisation': (20, (125, 365, 513, 513)),
    'fig_beta_elimination': (20, (170, 615, 400, 694)),
    'fig_zaitsev': (21, (60, 217, 520, 262)),
    'fig_elim_vs_sub': (21, (110, 428, 470, 555)),
    'fig_haloarene_resonance': (22, (130, 570, 520, 642)),
    'fig_sp2_sp3_carbon': (23, (190, 120, 522, 185)),
    'fig_dow_process': (23, (200, 418, 510, 482)),
    'fig_nitro_activation': (23, (190, 517, 510, 700)),
    'fig_picric': (24, (160, 62, 502, 143)),
    'fig_nitro_mechanism': (24, (40, 196, 515, 545)),
    'fig_halobenzene_resonance': (25, (148, 171, 467, 250)),
    'fig_chlorobenzene_halogenation': (25, (160, 360, 525, 450)),
    'fig_chlorobenzene_nitration': (25, (160, 472, 525, 547)),
    'fig_chlorobenzene_sulphonation': (25, (160, 576, 530, 684)),
    'fig_chlorobenzene_friedel_crafts': (26, (148, 62, 532, 285)),
    'fig_ex69_directing': (26, (148, 386, 513, 587)),
    'fig_wurtz_fittig': (27, (171, 120, 513, 171)),
    'fig_fittig': (27, (171, 227, 513, 268)),
    'fig_ddt': (29, (260, 448, 420, 578)),
}, MEDIA, long_side=1000)
