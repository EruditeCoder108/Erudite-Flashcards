import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch05-morphology-of-flowering-plants')
d = Deck('Chapter 5: Morphology of Flowering Plants', 'Class 11', ['class-11', 'biology', 'ch-5'])
d.description = 'Root, stem, leaf, inflorescence, flower, fruit, seed, floral formula and Solanaceae'
M = 'media/'
P = lambda b: pad(b, 6)
img = lambda name: {'termImage': M + name + '.webp'}
ans_img = lambda name: {'definitionImage': M + name + '.webp'}

# ---------------------------------------------------------------- Katherine Esau, intro
d.sec('intro')
d.basic('Which botanist wrote <i>Plant Anatomy</i> (1954) and <i>Anatomy of Seed Plants</i> (1960)?', T('Katherine Esau'))
d.basic("What did Katherine Esau's early work show about the curly top virus?", 'It spreads through the plant via the ' + T('phloem') + ' (food-conducting tissue)')
d.basic('Which five parts characterise all angiosperms?', 'Roots, stems, leaves, flowers, fruits')
d.occlusion('Figure 5.1 · Parts of a flowering plant', M + 'fig_5_1_plant_parts.webp', (760, 1001), [
    ('Flower', P((485, 67, 103, 32))), ('Fruit', P((489, 227, 77, 32))), ('Stem', P((490, 305, 79, 32))), ('Leaf', P((514, 351, 64, 32))),
    ('Node', P((21, 517, 77, 32))), ('Internode', P((39, 569, 150, 32))), ('Bud', P((350, 614, 65, 32))),
    ('Primary root', P((466, 784, 122, 70))), ('Secondary root', P((467, 866, 162, 69))),
    ('Shoot system', P((624, 345, 108, 69))), ('Root system', P((644, 830, 108, 69)))], printed=True)

# ---------------------------------------------------------------- 5.1 Root
d.sec('5.1-root')
d.basic('From what does the primary root develop?', 'Direct elongation of the ' + T('radicle'))
d.basic('What is a tap root system? Example?', 'The primary root and its branches (secondary, tertiary roots), e.g. ' + E('mustard'))
d.basic('What is a fibrous root system? Example?', 'In monocots the short-lived primary root is replaced by many roots from the ' + T('base of the stem') + ', e.g. ' + E('wheat'))
d.basic('What are adventitious roots? Examples?', 'Roots arising from parts ' + X('other than the radicle') + ', e.g. ' + E('grass, <i>Monstera</i>, banyan'))
d.basic('Name the three root types in Figure 5.2.', '(a) ' + T('Tap') + ', (b) ' + T('fibrous') + ', (c) ' + T('adventitious'), **img('fig_5_2_roots'))
d.basic('Name four functions of the root system.', 'Absorbing water and minerals, anchorage, storing reserve food, synthesis of ' + T('plant growth regulators'))
d.basic('Tap or fibrous: which is typical of dicots and of monocots?', 'Dicots: ' + T('tap') + '. Monocots: ' + T('fibrous') + '.')

d.sec('5.1.1-regions-of-root')
d.basic('What is the root cap, and what does it do?', 'A ' + T('thimble-like') + ' structure at the root apex; protects the tender apex as it pushes through soil')
d.basic('Describe cells of the region of meristematic activity.', 'Very small, thin-walled, dense protoplasm; they ' + T('divide repeatedly'))
d.basic('Which region is responsible for growth of the root in length?', 'The ' + T('region of elongation'))
d.basic('Where do root hairs arise?', 'From epidermal cells of the ' + T('region of maturation'))
d.cloze('From the tip upwards: {{c1::root cap}} → {{c2::meristematic activity}} → {{c3::elongation}} → {{c4::maturation}} (root hairs).',
        extra='Mnemonic, tip up: <b>C</b>ap, <b>M</b>eristem, <b>E</b>longation, <b>M</b>aturation: "Can Men Eat Mangoes?"')
d.occlusion('Figure 5.3 · Regions of the root tip', M + 'fig_5_3_root_tip.webp', (1001, 921), [
    ('Root hair', [15, 388, 205, 58]), ('Region of maturation', [722, 238, 268, 108]), ('Region of elongation', [592, 528, 235, 108]),
    ('Region of meristematic activity', [532, 708, 312, 178]), ('Root cap', [92, 832, 192, 60])], printed=True)

# ---------------------------------------------------------------- 5.2 Stem
d.sec('5.2-stem')
d.basic('What is the stem?', 'The ' + T('ascending') + ' part of the axis bearing branches, leaves, flowers and fruits')
d.basic('From what does the stem develop?', 'The ' + T('plumule') + ' of the embryo')
d.basic('What are nodes and internodes?', T('Nodes') + ': regions where leaves are borne. ' + T('Internodes') + ': portions between two nodes.')
d.basic('Name the main functions of the stem.', 'Spreading out branches with leaves, flowers, fruits; conducting water, minerals and photosynthates')
d.basic('What other functions may some stems perform?', 'Storage of food, support, protection, vegetative propagation')
d.basic('How can you tell a stem from a root?', 'Stems have ' + T('nodes and internodes') + ', buds, multicellular hairs, and are positively ' + T('phototropic'))

# ---------------------------------------------------------------- 5.3 Leaf
d.sec('5.3-leaf')
d.basic('What is a leaf?', 'A lateral, generally flattened structure borne on the stem at a ' + T('node') + ', with a bud in its axil')
d.basic('From where do leaves originate, and in what order are they arranged?', 'From ' + T('shoot apical meristems') + ', in ' + T('acropetal') + ' order (youngest at the top)')
d.basic('What does the axillary bud become?', 'A ' + T('branch'))
d.basic('Name the three main parts of a leaf.', T('Leaf base') + ', ' + T('petiole') + ', ' + T('lamina'))
d.occlusion('Figure 5.4 (a) · Parts of a leaf', M + 'fig_5_4a_leaf_parts.webp', (1001, 674), [
    ('Lamina', P((36, 49, 179, 46))), ('Stipule', P((660, 136, 169, 46))), ('Petiole', P((633, 429, 153, 46))),
    ('Leaf base', P((542, 553, 110, 95))), ('Axillary bud', P((786, 519, 179, 95)))], printed=True)
d.basic('What are stipules?', 'Two lateral small leaf-like structures at the leaf base')
d.basic('What does the leaf base form in monocots?', 'A ' + T('sheath') + ' covering the stem partially or wholly')
d.basic('What is a pulvinus? Where?', 'A ' + T('swollen leaf base') + ', in some leguminous plants')
d.basic('How do long, thin, flexible petioles help a leaf?', 'The blade flutters in wind, ' + T('cooling') + ' the leaf and bringing fresh air to its surface')
d.basic('What do veins do?', 'Give ' + T('rigidity') + ' to the blade and transport water, minerals and food')

d.sec('5.3.1-venation')
d.basic('What is venation?', 'The arrangement of veins and veinlets in the lamina')
d.basic('Reticulate vs parallel venation: which is typical of dicots and monocots?', 'Dicots: ' + T('reticulate') + ' (network). Monocots: ' + T('parallel') + '.', **img('fig_5_4bc_venation'))
d.basic('Exceptions worth knowing (beyond NCERT)?', 'Some monocots have reticulate venation (' + E('<i>Smilax</i>, <i>Dioscorea</i>') + '), and some dicots parallel (' + E('<i>Calophyllum</i>') + '). Venation is a tendency, not a rule.')

d.sec('5.3.2-types-of-leaves')
d.basic('When is a leaf simple?', 'Lamina entire, or incisions ' + X('do not touch') + ' the midrib')
d.basic('When is a leaf compound?', 'Incisions reach the midrib, breaking it into ' + T('leaflets'))
d.basic('How do you tell a compound leaf from a branch with simple leaves?', 'A ' + T('bud') + ' is in the axil of the petiole, ' + X('never') + ' in the axil of leaflets')
d.basic('Pinnate vs palmate compound leaf? Examples?', T('Pinnate') + ': leaflets on a common axis, the ' + T('rachis') + ' (' + E('neem') + ')<br>' + T('Palmate') + ': leaflets at one point, tip of the petiole (' + E('silk cotton') + ')', **img('fig_5_5_compound_leaves'))
d.basic('What does the rachis represent?', 'The ' + T('midrib') + ' of the leaf')

d.sec('5.3.3-phyllotaxy')
d.basic('What is phyllotaxy?', 'The pattern of arrangement of ' + T('leaves') + ' on the stem or branch')
d.basic('Name the three types of phyllotaxy in Figure 5.6 with their plants.', T('Alternate') + ' (china rose), ' + T('opposite') + ' (guava), ' + T('whorled') + ' (' + I('Alstonia') + ')', **img('fig_5_6_phyllotaxy'))
d.cloze('Alternate phyllotaxy: {{c1::one}} leaf per node (china rose, mustard, sunflower). Opposite: {{c2::a pair}} per node (<i>Calotropis</i>, guava). Whorled: {{c3::more than two}} per node (<i>Alstonia</i>).')

# ---------------------------------------------------------------- 5.4 Inflorescence
d.sec('5.4-inflorescence')
d.basic('Why is a flower called a modified shoot?', 'The shoot apical meristem becomes a ' + T('floral meristem') + '.<br>Internodes do not elongate, and floral appendages form at successive nodes instead of leaves')
d.basic('What is an inflorescence?', 'The arrangement of ' + T('flowers') + ' on the floral axis')
d.basic('Racemose inflorescence: axis growth and flower order?', 'Main axis ' + T('continues to grow') + '; flowers lateral, in ' + T('acropetal') + ' succession (older below)', **img('fig_5_7_racemose'))
d.basic('Cymose inflorescence: axis growth and flower order?', 'Main axis ' + T('ends in a flower') + ' (limited growth); flowers in ' + T('basipetal') + ' order', **img('fig_5_8_cymose'))
d.basic('Trick to remember racemose vs cymose?', 'Racemose "races on": the tip keeps growing, so the ' + T('youngest') + ' flower is at the top. Cymose "caps" the tip with a flower, so the ' + T('oldest') + ' is at the top.')

# ---------------------------------------------------------------- 5.5 Flower
d.sec('5.5-flower')
d.basic('What is the thalamus?', 'The swollen end of the pedicel (stalk) bearing the floral whorls; also called ' + T('receptacle'))
d.basic('Name the four whorls of a flower, outside in.', T('Calyx') + ', ' + T('corolla') + ', ' + T('androecium') + ', ' + T('gynoecium'))
d.occlusion('Figure 5.10 · Parts of a flower', M + 'fig_5_10_flower_parts.webp', (1001, 269), [
    ('Androecium', P((219, 100, 114, 19))), ('Gynoecium', P((216, 140, 107, 19))), ('Corolla', P((254, 168, 69, 19))),
    ('Calyx', P((253, 201, 53, 19))), ('Pedicel', P((220, 231, 65, 19)))], printed=True)
d.basic('Which whorls are accessory and which reproductive?', 'Accessory: ' + T('calyx, corolla') + '. Reproductive: ' + T('androecium, gynoecium') + '.')
d.basic('What is a perianth? Example?', 'Calyx and corolla ' + X('not distinct') + ', e.g. ' + E('lily'))
d.basic('Bisexual vs unisexual flower?', T('Bisexual') + ': both androecium and gynoecium. ' + T('Unisexual') + ': only stamens or only carpels.')
d.basic('What is an actinomorphic flower? Examples?', 'Divisible into two equal halves in ' + T('any') + ' radial plane (radial symmetry): ' + E('mustard, datura, chilli'))
d.basic('What is a zygomorphic flower? Examples?', 'Divisible into two similar halves in ' + T('only one') + ' vertical plane: ' + E('pea, gulmohur, bean, <i>Cassia</i>'))
d.basic('Which flower does NCERT give as asymmetric (irregular)?', E('Canna'))
d.basic('What are trimerous, tetramerous and pentamerous flowers?', 'Floral appendages in multiples of ' + N('3') + ', ' + N('4') + ', ' + N('5'))
d.basic('What are bracteate and ebracteate flowers?', 'Bracteate: with ' + T('bracts') + ' (reduced leaves at the base of the pedicel). Ebracteate: without.')

d.sec('5.5-position-of-ovary')
d.basic('Hypogynous flower: ovary position? Examples?', 'Gynoecium ' + T('highest') + ', others below: ovary ' + T('superior') + '. ' + E('Mustard, china rose, brinjal'))
d.basic('Perigynous flower: ovary position? Examples?', 'Other parts on the rim of the thalamus at about the same level: ovary ' + T('half inferior') + '. ' + E('Plum, rose, peach'))
d.basic('Epigynous flower: ovary position? Examples?', 'Thalamus encloses and fuses with the ovary; other parts arise above it: ovary ' + T('inferior') + '<br>' + E('Guava, cucumber, ray florets of sunflower'))
d.occlusion('Figure 5.9 · Position of floral parts on the thalamus', M + 'fig_5_9_thalamus.webp', (1001, 399), [
    ('Hypogynous', P((146, 378, 26, 20))), ('Perigynous', P((383, 378, 26, 20))), ('Perigynous', P((618, 378, 24, 20))), ('Epigynous', P((817, 382, 26, 20)))])
d.basic('Mnemonic: hypo-, peri-, epi-gynous?', '<i>hypo</i> = below (other parts ' + T('below') + ' the ovary), <i>peri</i> = around, <i>epi</i> = upon (other parts ' + T('on top') + ' of the ovary)')

d.sec('5.5.1-calyx-corolla')
d.basic('What are sepals, and what do they usually do?', 'Members of the calyx; green, leaf-like, ' + T('protect the flower in bud'))
d.cloze('United sepals: {{c1::gamosepalous}}; free sepals: {{c2::polysepalous}}. United petals: {{c3::gamopetalous}}; free petals: {{c4::polypetalous}}.')
d.basic('Why are petals usually brightly coloured?', 'To attract ' + T('insects') + ' for pollination')
d.basic('Name four shapes of corolla.', 'Tubular, bell-shaped, funnel-shaped, wheel-shaped')
d.basic('What is aestivation?', 'Arrangement of sepals or petals in the ' + T('floral bud') + ' relative to other members of the same whorl')
d.occlusion('Figure 5.11 · Types of aestivation', M + 'fig_5_11_aestivation.webp', (1001, 584), [
    ('Valvate', P((131, 538, 33, 26))), ('Twisted', P((381, 538, 33, 26))), ('Imbricate', P((631, 538, 31, 26))), ('Vexillary', P((880, 538, 33, 26)))])
d.basic('Valvate aestivation: arrangement and example?', 'Margins just ' + T('touch') + ' without overlapping: ' + E('<i>Calotropis</i>'))
d.basic('Twisted aestivation: arrangement and examples?', 'Each margin overlaps the next ' + T('in one direction') + ': ' + E("china rose, lady's finger, cotton"))
d.basic('Imbricate aestivation: arrangement and examples?', 'Margins overlap but ' + X('in no particular direction') + ': ' + E('<i>Cassia</i>, gulmohur'))
d.cloze('Vexillary (papilionaceous) aestivation in pea and bean: the largest petal, the {{c1::standard}}, overlaps two lateral {{c2::wings}}, which overlap the two smallest anterior petals, the {{c3::keel}}.')

d.sec('5.5.1.3-androecium')
d.basic('What does a stamen consist of?', 'A ' + T('filament') + ' and an ' + T('anther'))
d.basic('How many pollen sacs does a typical anther have?', 'Bilobed, each lobe with two chambers: ' + N('four') + ' pollen sacs')
d.basic('What is a staminode?', 'A ' + T('sterile') + ' stamen')
d.basic('Epipetalous vs epiphyllous stamens? Examples?', T('Epipetalous') + ': attached to petals (' + E('brinjal') + '). ' + T('Epiphyllous') + ': attached to the perianth (' + E('lily') + ').')
d.basic('What is a polyandrous condition?', 'Stamens remain ' + T('free'))
d.cloze('Stamens united in one bundle: {{c1::monoadelphous}} (china rose); two bundles: {{c2::diadelphous}} (pea); more than two: {{c3::polyadelphous}} (citrus).',
        extra='Greek <i>adelphos</i> = brother: mono-, di-, poly- "brotherhoods" of stamens.')
d.basic('In which flowers do filament lengths vary?', E('<i>Salvia</i> and mustard'))

d.sec('5.5.1.4-gynoecium')
d.basic('What are the three parts of a carpel?', T('Stigma') + ', ' + T('style') + ', ' + T('ovary'))
d.basic('What is the stigma?', 'The ' + T('receptive surface') + ' for pollen, usually at the tip of the style')
d.basic('To what are ovules attached inside the ovary?', 'A flattened, cushion-like ' + T('placenta'))
d.basic('Apocarpous vs syncarpous? Examples?', T('Apocarpous') + ': carpels free (' + E('lotus, rose') + '). ' + T('Syncarpous') + ': carpels fused (' + E('mustard, tomato') + ').')
d.basic('After fertilisation, what do ovules and ovary become?', 'Ovules → ' + T('seeds') + '; ovary → ' + T('fruit'))
d.basic('What is placentation?', 'The arrangement of ' + T('ovules') + ' within the ovary')
d.occlusion('Figure 5.12 · Types of placentation', M + 'fig_5_12_placentation.webp', (219, 1001), [
    ('Marginal', P((89, 162, 21, 17))), ('Axile', P((94, 377, 21, 17))), ('Parietal', P((95, 588, 20, 17))),
    ('Free central', P((95, 801, 21, 17))), ('Basal', P((92, 972, 20, 17)))])
d.basic('Marginal placentation: description and example?', 'Placenta a ridge along the ' + T('ventral suture') + ', ovules in two rows: ' + E('pea'))
d.basic('Axile placentation: description and examples?', 'Placenta ' + T('axial') + ' in a ' + T('multilocular') + ' ovary: ' + E('china rose, tomato, lemon'))
d.basic('Parietal placentation: description and examples?', 'Ovules on the ' + T('inner wall') + '; one-chambered ovary becomes two-chambered by a ' + T('false septum') + ': ' + E('mustard, <i>Argemone</i>'))
d.basic('Free central placentation: description and examples?', 'Ovules on a central axis, ' + X('septa absent') + ': ' + E('<i>Dianthus</i>, primrose'))
d.basic('Basal placentation: description and examples?', 'Placenta at the ' + T('base') + ', a ' + N('single') + ' ovule: ' + E('sunflower, marigold'))
d.basic('Mnemonic for placentation examples?', '<b>M</b>arginal: <b>P</b>ea<br><b>A</b>xile: <b>T</b>omato, china rose, lemon<br><b>P</b>arietal: <b>M</b>ustard, <i>Argemone</i><br><b>F</b>ree central: <b>D</b>ianthus, primrose<br><b>B</b>asal: <b>S</b>unflower, marigold')

# ---------------------------------------------------------------- 5.6 Fruit, 5.7 Seed
d.sec('5.6-fruit')
d.basic('What is a fruit?', 'A mature or ripened ' + T('ovary') + ', developed after fertilisation')
d.basic('What is a parthenocarpic fruit?', 'A fruit formed ' + X('without fertilisation') + ' of the ovary (e.g. seedless banana, grapes)')
d.basic('What is the pericarp, and its three layers when fleshy?', 'The fruit wall: outer ' + T('epicarp') + ', middle ' + T('mesocarp') + ', inner ' + T('endocarp'))
d.basic('What is a drupe? Examples?', 'Fruit from a ' + T('monocarpellary superior') + ' ovary, ' + N('one') + '-seeded: ' + E('mango, coconut'))
d.basic('Describe the pericarp of mango (a drupe).', 'Thin epicarp, fleshy ' + T('edible mesocarp') + ', stony hard endocarp', **ans_img('fig_5_13_fruits'))
d.basic('What is special about the mesocarp of coconut?', 'It is ' + T('fibrous'))

d.sec('5.7-seed')
d.basic('What is a seed made of?', 'A ' + T('seed coat') + ' and an ' + T('embryo') + ' (radicle, embryonal axis, one or two cotyledons)')
d.basic('Give NCERT examples of one-cotyledon and two-cotyledon seeds.', 'One: ' + E('wheat, maize') + '. Two: ' + E('gram, pea') + '.')
d.basic('Name the two layers of the seed coat.', 'Outer ' + T('testa') + ', inner ' + T('tegmen'))
d.basic('What is the hilum?', 'A ' + T('scar') + ' on the seed coat where the seed was attached to the fruit')
d.basic('What is the micropyle of a seed?', 'A small pore ' + T('above the hilum'))
d.occlusion('Figure 5.14 · Structure of a dicot seed', M + 'fig_5_14_dicot_seed.webp', (1001, 514), [
    ('Seed coat', P((49, 24, 191, 41))), ('Cotyledon', P((435, 48, 198, 41))), ('Plumule', P((774, 92, 164, 41))),
    ('Hilum', P((306, 376, 123, 41))), ('Radicle', P((710, 418, 145, 41))), ('Micropyle', P((196, 465, 192, 41)))], printed=True)
d.basic('Endospermic vs non-endospermous seeds? Examples?', T('Endospermic') + ': endosperm stores food in the mature seed (' + E('castor') + ')<br>' + T('Non-endospermous') + ': endosperm used up (' + E('bean, gram, pea') + ')')
d.basic('Are monocot seeds endospermic?', 'Generally ' + T('yes') + '; some, as in ' + X('orchids') + ', are non-endospermic')
d.basic('In maize, how are the seed coat and fruit wall related?', 'Seed coat is membranous and ' + T('fused') + ' with the fruit wall')
d.basic('What is the aleurone layer?', 'A ' + T('proteinous') + ' layer, the outer covering of the endosperm, separating it from the embryo')
d.basic('What is the scutellum?', 'The single, large, ' + T('shield-shaped cotyledon') + ' of a cereal embryo')
d.cloze('In maize the plumule is enclosed in the {{c1::coleoptile}} and the radicle in the {{c2::coleorhiza}}.',
        extra='coleo = sheath; <i>ptile</i> ↔ plumule (shoot), <i>rhiza</i> = root.')
d.occlusion('Figure 5.15 · Structure of a monocot seed (maize)', M + 'fig_5_15_monocot_seed.webp', (1001, 506), [
    ('Seed coat & fruit-wall', P((203, 101, 265, 25))), ('Aleurone layer', P((299, 183, 177, 25))), ('Endosperm', P((838, 101, 141, 25))),
    ('Scutellum', P((838, 218, 125, 25))), ('Coleoptile', P((837, 278, 120, 25))), ('Plumule', P((839, 338, 101, 25))),
    ('Radicle', P((836, 428, 89, 25))), ('Coleorhiza', P((838, 469, 128, 25))), ('Embryo', P((279, 412, 96, 25)))], printed=True)

# ---------------------------------------------------------------- 5.8 Floral formula
d.sec('5.8-floral-formula')
d.basic('In what order is a flowering plant described?', '1) Habit<br>2) Vegetative characters (root, stem, leaves)<br>3) Floral characters (inflorescence, flower parts)<br>4) Floral diagram and floral formula')
d.basic('Floral formula symbols: Br, K, C, P, A, G?', 'Br: bracteate. K: calyx. C: corolla. P: perianth. A: androecium. G: gynoecium.')
d.basic('How are superior and inferior ovaries written in a floral formula?', 'Superior: line ' + T('below') + ' G (G̲). Inferior: line ' + T('above') + ' G (Ḡ).')
d.basic('Which symbols show actinomorphic and zygomorphic flowers?', '⊕ actinomorphic; % (or ↑) zygomorphic')
d.basic('How are fusion and adhesion shown in a floral formula?', T('Fusion') + ' (cohesion): number in brackets, e.g. C<sub>(5)</sub><br>' + T('Adhesion') + ': a line drawn above the symbols of the joined whorls')
d.basic('What does the dot at the top of a floral diagram show?', 'The position of the ' + T('mother axis'))
d.basic('Which family does this floral diagram (⊕ ⚥ K<sub>2+2</sub> C<sub>4</sub> A<sub>2+4</sub> G<sub>(2)</sub>) represent?', T('Brassicaceae') + ' (mustard)', **img('fig_5_16_floral_diagram'))
d.basic('Read the mustard formula: ⊕ ⚥ K<sub>2+2</sub> C<sub>4</sub> A<sub>2+4</sub> G<sub>(2)</sub>.', 'Actinomorphic, bisexual; 4 sepals in 2 whorls; 4 free petals; 6 stamens (2 + 4, tetradynamous); ovary of 2 fused carpels, superior')

# ---------------------------------------------------------------- 5.9 Solanaceae
d.sec('5.9-solanaceae')
d.basic('What is the common name of Solanaceae?', 'The ' + T("'potato family'"))
d.basic('Which plant is shown in Figure 5.17?', EI('Solanum nigrum') + ' (makoi): flowering twig, flower, L.S., stamens, carpel, floral diagram', **img('fig_5_17_solanum'))
d.basic('Solanaceae: habit and stem?', 'Mostly herbs, shrubs, rarely small trees; stem herbaceous, rarely woody; underground stem in potato (' + I('Solanum tuberosum') + ')')
d.basic('Solanaceae: leaves?', 'Alternate, simple (rarely pinnately compound), ' + T('exstipulate') + ', reticulate venation')
d.basic('Solanaceae: calyx and corolla?', 'Calyx: ' + N('5') + ' united, ' + T('persistent') + ', valvate. Corolla: ' + N('5') + ' united, valvate.')
d.basic('Solanaceae: androecium?', N('Five') + ' stamens, ' + T('epipetalous'))
d.basic('Solanaceae: gynoecium?', T('Bicarpellary') + ', obliquely placed, syncarpous<br>Ovary ' + T('superior') + ', bilocular<br>Placenta swollen with many ovules, ' + T('axile'))
d.basic('NCERT prints "obligately placed" carpels in Solanaceae. What is meant?', X('Obliquely') + ' placed: the two carpels sit at an angle to the median plane. "Obligately" is a misprint.')
d.basic('Solanaceae: fruit and seeds?', 'Fruit: ' + T('berry or capsule') + '. Seeds: many, ' + T('endospermous') + '.')
d.basic('Floral formula of Solanaceae?', '⊕ ⚥ K<sub>(5)</sub> C<sub>(5)</sub> A<sub>5</sub> G<sub>(2)</sub>, with a line joining C and A (epipetalous) and the ovary superior')
table_card(d, '5.9 · Solanaceae', 'Name the example(s) for each use.', [
    ('Food', 'Tomato, brinjal, potato', False), ('Spice', 'Chilli', False), ('Medicine', 'Belladonna, ashwagandha', False),
    ('Fumigatory', 'Tobacco', False), ('Ornamental', 'Petunia', False)], term='Solanaceae: economic importance')

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
