import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Biology', 'class12-biology-ch01-sexual-reproduction-in-flowering-plants')
d = Deck('Chapter 1: Sexual Reproduction in Flowering Plants', 'Class 12', ['class-12', 'biology', 'ch-1'])
d.description = 'Anther, pollen, ovule, embryo sac, pollination, double fertilisation, endosperm, embryo, seed, fruit and apomixis'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}
FL, AT, OV, ES, EM = (1001, 850), (1001, 408), (1001, 633), (1001, 891), (368, 1001)

# ---------------------------------------------------------------- 1.1 Flower
d.sec('1.1-flower')
d.basic('Why are flowers important to a biologist?', 'They are morphological and embryological marvels and the ' + T('sites of sexual reproduction'))
d.basic('What is floriculture?', 'Cultivation of flowering plants for ' + T('ornamental/commercial') + ' use (cut flowers, gardens)')
d.basic('Two parts of a flower in which the two units of sexual reproduction develop?', T('Anther') + ' (pollen, male) and ' + T('ovary/ovule') + ' (embryo sac, female)')
d.occlusion('Figure 1.1 · L.S. of a flower', M + 'fig_1_1_flower_ls.webp', FL, [
    ('Stigma', wbox(340, 38, 412, 62, FL), True), ('Anther', wbox(640, 48, 714, 72, FL), True),
    ('Petal', wbox(745, 82, 798, 104, FL), True), ('Style', wbox(98, 244, 152, 266, FL), True),
    ('Filament', wbox(895, 322, 990, 344, FL), True), ('Sepal', wbox(732, 657, 790, 680, FL), True),
    ('Ovary', wbox(530, 778, 594, 800, FL), True)])

# ---------------------------------------------------------------- 1.2 Pre-fertilisation
d.sec('1.2-pre-fertilisation')
d.basic('What happens in a plant long before a flower is seen?', 'The decision to flower is taken; ' + T('hormonal and structural changes') + ' lead to differentiation of the ' + T('floral primordium'))
d.cloze('The {{c1::androecium}} (whorl of stamens) is the male reproductive organ; the {{c2::gynoecium}} is the female reproductive organ.')

d.sec('1.2.1-stamen-anther')
d.cloze('A stamen has a long slender stalk, the {{c1::filament}}, and a terminal, generally bilobed {{c2::anther}}.', )
d.basic('Where is the proximal end of the filament attached?', 'To the ' + T('thalamus') + ' or the ' + T('petal'))
d.basic('What does "dithecous" mean?', 'Each anther lobe has ' + T('two theca') + ' (a typical anther is bilobed and dithecous)', **fig('fig_1_2_stamen_anther'))
d.basic('What separates the two theca of a lobe?', 'A ' + T('longitudinal groove') + ' running lengthwise')
d.basic('Why is an anther called tetrasporangiate?', 'It is four-sided (tetragonal) with ' + N('four microsporangia') + ' at the corners, ' + N('two') + ' in each lobe')
d.basic('What do microsporangia become?', T('Pollen sacs') + ': they run the length of the anther and are packed with pollen grains')
d.cloze('A microsporangium is surrounded by four wall layers: {{c1::epidermis}}, {{c1::endothecium}}, {{c1::middle layers}} and {{c1::tapetum}} (outer to inner).')
d.basic('Function of the outer three wall layers of the microsporangium?', T('Protection') + ' and help in ' + T('dehiscence') + ' of the anther to release pollen')
d.basic('Innermost wall layer of the microsporangium, and its function?', T('Tapetum') + ': ' + T('nourishes') + ' the developing pollen grains')
d.basic('Features of tapetal cells?', T('Dense cytoplasm') + ' and generally ' + T('more than one nucleus'))
d.basic('How can tapetal cells become binucleate? (think)', 'Nuclear division (mitosis) ' + X('without') + ' cytokinesis (or endomitosis/nuclear fusion)')
d.basic('Role of the tapetum in forming the pollen wall? (Exercise 17)', 'It secretes ' + T('sporopollenin') + ' precursors (and enzymes, Ubisch bodies) that build the ' + T('exine') + '; also nourishes microspores')
d.basic('What occupies the centre of a young microsporangium?', T('Sporogenous tissue') + ': compactly arranged homogenous cells')
d.occlusion('Figure 1.3 · T.S. of young anther and one microsporangium', M + 'fig_1_3ab_anther_ts.webp', AT, [
    ('Connective', wbox(460, 176, 540, 198, AT), True), ('Epidermis', wbox(460, 213, 532, 236, AT), True),
    ('Endothecium', wbox(458, 254, 560, 276, AT), True), ('Sporogenous tissue', wbox(460, 282, 590, 326, AT), True),
    ('Middle layers', wbox(12, 314, 142, 338, AT), True), ('Tapetum', wbox(458, 366, 545, 390, AT), True),
    ('Epidermis', wbox(866, 36, 942, 58, AT), True), ('Endothecium', wbox(864, 99, 968, 122, AT), True),
    ('Middle layers', wbox(864, 150, 998, 173, AT), True), ('Microspore mother cells', wbox(874, 200, 996, 246, AT), True),
    ('Tapetum', wbox(866, 310, 954, 332, AT), True)])

d.basic('What is microsporogenesis?', 'Formation of ' + T('microspores') + ' from a ' + T('pollen mother cell (PMC)') + ' by ' + T('meiosis'))
d.basic('Why is each sporogenous cell a potential pollen mother cell?', 'Each can undergo meiosis to give a ' + T('microspore tetrad'))
d.basic('Ploidy of the cells of a microspore tetrad?', T('Haploid (n)') + ' (products of meiosis)')
d.basic('What makes microspores separate from the tetrad?', 'As anthers ' + T('mature and dehydrate') + ', microspores dissociate and develop into pollen grains')
d.basic('How are pollen grains released?', 'By ' + T('dehiscence') + ' of the anther (along the line of dehiscence)', **fig('fig_1_3c_dehisced_anther'))
d.basic('Identify this figure.', 'Mature ' + T('dehisced anther') + ' (T.S.) releasing pollen grains', **img('fig_1_3c_dehisced_anther'))
d.basic('Arrange in order: pollen grain, sporogenous tissue, microspore tetrad, pollen mother cell, male gametes (Exercise 3)', 'Sporogenous tissue → PMC → microspore tetrad → pollen grain → male gametes')

d.basic('What do pollen grains represent?', 'The ' + T('male gametophytes'))
d.basic('Shape and size of pollen grains?', 'Generally ' + T('spherical') + ', about ' + N('25–50 µm') + ' in diameter', **fig('fig_1_4_pollen_sem'))
d.basic('Identify: scanning electron micrographs of these structures.', T('Pollen grains') + ' of different species (Figure 1.4); note the varied exine patterns', **img('fig_1_4_pollen_sem'))
d.basic('Outer wall layer of pollen, and what it is made of?', T('Exine') + ', made of ' + T('sporopollenin'))
d.basic('Why is sporopollenin remarkable?', 'One of the most resistant organic materials: withstands ' + T('high temperature, strong acids and alkali') + '; ' + X('no enzyme') + ' is known to degrade it')
d.basic('What are germ pores?', 'Prominent apertures in the exine where ' + X('sporopollenin is absent') + '; the pollen tube emerges through one')
d.basic('Why are pollen grains well-preserved as fossils?', 'Because of ' + T('sporopollenin') + ' in the exine')
d.basic('Why should the exine be hard? (think)', 'To protect the male gametophyte from ' + T('drying, UV and damage') + ' during transfer')
d.basic('Inner wall of pollen, and its composition?', T('Intine') + ': thin, continuous, made of ' + T('cellulose and pectin'))
d.basic('Two cells of a mature pollen grain?', T('Vegetative cell') + ' and ' + T('generative cell'), **fig('fig_1_5_pollen_maturation'))
d.basic('Vegetative cell vs generative cell?', T('Vegetative') + ': bigger, abundant food reserve, large irregular nucleus. ' + T('Generative') + ': small, spindle-shaped, dense cytoplasm, floats in the vegetative cell.')
d.basic('In what % of angiosperms is pollen shed at the 2-celled stage?', 'Over ' + N('60%'))
d.basic('What is the 3-celled pollen stage?', 'Generative cell has divided ' + T('mitotically') + ' into ' + N('two male gametes') + ' before shedding')
d.basic('Health problem caused by pollen of many species?', T('Allergies') + ' and bronchial afflictions: asthma, bronchitis')
d.basic('Which weed causes pollen allergy in India, and how did it arrive?', EI('Parthenium') + ' (carrot grass), as a contaminant with ' + T('imported wheat'))
d.basic('Why are pollen tablets used? (Figure 1.6)', 'Pollen is ' + T('rich in nutrients') + '; claimed to boost performance of athletes and race horses')
d.basic('On what does pollen viability depend?', 'Highly variable; partly on ' + T('temperature and humidity'))
d.basic('How long does pollen of rice and wheat stay viable?', 'About ' + N('30 minutes') + ' after release')
d.basic('Which families have pollen viable for months?', 'Some members of ' + E('Rosaceae, Leguminosae and Solanaceae'))
d.basic('How is pollen stored for years? What is it used for?', 'In ' + T('liquid nitrogen') + ' at ' + N('−196°C') + '; as ' + T('pollen banks') + ' in crop breeding')
d.basic('Correction: NCERT prints "-1960C" for liquid nitrogen. Correct value?', N('−196 °C') + ' (the degree sign was lost in printing)')

d.sec('1.2.2-pistil-ovule-embryo-sac')
d.cloze('A gynoecium with a single pistil is {{c1::monocarpellary}}; with more than one it is {{c2::multicarpellary}}.')
d.cloze('Fused pistils are {{c1::syncarpous}} (e.g. {{c2::<i>Papaver</i>}}); free pistils are {{c3::apocarpous}} (e.g. <i>Michelia</i>).')
d.cloze('Three parts of a pistil: {{c1::stigma}} (landing platform for pollen), {{c2::style}} (slender part), {{c3::ovary}} (basal bulged part).')
d.basic('What is the locule?', 'The ' + T('ovarian cavity') + '; the placenta lies inside it')
d.basic('Another name for ovules?', T('Megasporangia'))
d.cloze('Ovules per ovary: one in {{c1::wheat, paddy, mango}}; many in {{c2::papaya, watermelon, orchids}}.')
d.occlusion('Figure 1.7 · Pistils of Hibiscus, Papaver, Michelia', M + 'fig_1_7_pistil_ovule.webp', OV, [
    ('Stigma', wbox(98, 85, 168, 106, OV), True), ('Style', wbox(100, 171, 150, 192, OV), True),
    ('Ovary', wbox(105, 484, 163, 505, OV), True), ('Thalamus', wbox(107, 515, 206, 537, OV), True),
    ('Stigma', wbox(172, 207, 242, 229, OV), True), ('Syncarpous ovary', wbox(78, 352, 194, 396, OV), True),
    ('Carpels', wbox(533, 40, 609, 62, OV), True)])
d.basic('Identify pistils (a), (b), (c) of Figure 1.7.', '(a) ' + EI('Hibiscus') + ' (single pistil); (b) multicarpellary syncarpous ' + EI('Papaver') + '; (c) multicarpellary apocarpous ' + EI('Michelia'), **img('fig_1_7_pistil_ovule'))
d.basic('What is the funicle?', 'The ' + T('stalk') + ' attaching the ovule to the placenta')
d.basic('What is the hilum?', 'Region where the body of the ovule ' + T('fuses with the funicle') + ' (junction of ovule and funicle)')
d.basic('What are integuments?', 'One or two ' + T('protective envelopes') + ' of the ovule, encircling the nucellus')
d.basic('What is the micropyle?', 'Small opening at the tip where integuments ' + X('do not cover') + ' the nucellus')
d.basic('What is the chalaza?', 'The ' + T('basal part') + ' of the ovule, opposite the micropylar end')
d.basic('What is the nucellus?', 'Mass of cells inside the integuments with abundant ' + T('reserve food') + '; contains the embryo sac')
d.basic('How many embryo sacs does an ovule generally have, and from what?', T('One') + ', formed from a ' + T('megaspore'))
d.occlusion('Figure 1.7d · Anatropous ovule', M + 'fig_1_7_pistil_ovule.webp', OV, [
    ('Hilum', wbox(822, 146, 884, 168, OV), True), ('Funicle', wbox(822, 197, 896, 219, OV), True),
    ('Micropyle', wbox(820, 222, 918, 244, OV), True), ('Micropylar pole', wbox(818, 247, 970, 270, OV), True),
    ('Outer integument', wbox(822, 277, 998, 300, OV), True), ('Inner integument', wbox(820, 322, 994, 345, OV), True),
    ('Nucellus', wbox(822, 361, 910, 383, OV), True), ('Embryo sac', wbox(822, 390, 940, 412, OV), True),
    ('Chalazal pole', wbox(818, 512, 952, 535, OV), True)])
d.basic('What is megasporogenesis?', 'Formation of ' + T('megaspores') + ' from the ' + T('megaspore mother cell (MMC)'))
d.basic('Where does the MMC differentiate, and what is it like?', 'In the ' + T('micropylar region') + ' of the nucellus; a large cell with dense cytoplasm and a prominent nucleus')
d.basic('What does meiosis of the MMC produce?', N('Four') + ' megaspores (via a dyad, then a tetrad)')
d.occlusion('Figure 1.8a · Megasporogenesis', M + 'fig_1_8_embryo_sac.webp', ES, [
    ('Nucellus', wbox(183, 90, 270, 112, ES), True), ('Megaspore mother cell', wbox(180, 203, 290, 250, ES), True),
    ('Nucellus', wbox(540, 105, 627, 127, ES), True), ('Megaspore dyad', wbox(533, 197, 612, 245, ES), True),
    ('Megaspore tetrad', wbox(882, 172, 962, 217, ES), True)])
d.basic('Fate of the four megaspores in most flowering plants?', N('One') + ' is functional; the other ' + N('three degenerate'))
d.basic('What is monosporic development?', 'Embryo sac formed from a ' + T('single megaspore'))
table_card(d, 'Ploidy', 'n or 2n?', [
    ('Nucellus', '2n', False), ('MMC', '2n', False), ('Functional megaspore', 'n', False),
    ('Female gametophyte (embryo sac)', 'n', False), ('Endosperm (PEN)', '3n', False)], term='Ploidy of ovule structures')
d.cloze('The functional megaspore nucleus divides mitotically to give {{c1::2}}, then {{c2::4}}, then {{c3::8}}-nucleate stages of the embryo sac.')
d.basic('Why are the embryo-sac divisions called free nuclear?', 'Nuclear divisions are ' + X('not followed immediately') + ' by cell wall formation')
d.basic('When are cell walls laid down in the embryo sac?', 'After the ' + N('8-nucleate') + ' stage')
d.basic('What are polar nuclei?', 'The ' + N('two') + ' nuclei not walled into cells; they lie below the egg apparatus in the large ' + T('central cell'))
d.cloze('The egg apparatus, at the {{c1::micropylar}} end, has two {{c2::synergids}} and one {{c2::egg cell}}.')
d.basic('What is the filiform apparatus and its role?', 'Special cellular thickenings at the micropylar tip of the ' + T('synergids') + '; ' + T('guide the pollen tube') + ' into a synergid')
d.basic('Cells at the chalazal end of the embryo sac?', N('Three') + ' ' + T('antipodals'))
d.basic('Why is the mature embryo sac "8-nucleate but 7-celled"?', '3 antipodals + 2 synergids + 1 egg = 6 cells, plus ' + T('one central cell with two polar nuclei') + ' = 7 cells, 8 nuclei')
d.occlusion('Figure 1.8c · Mature embryo sac', M + 'fig_1_8_embryo_sac.webp', ES, [
    ('Chalazal end', wbox(688, 378, 818, 401, ES), True), ('Antipodals', wbox(870, 410, 978, 432, ES), True),
    ('Polar nuclei', wbox(870, 597, 992, 620, ES), True), ('Central cell', wbox(872, 626, 990, 650, ES), True),
    ('Egg', wbox(872, 654, 912, 676, ES), True), ('Synergids', wbox(872, 720, 974, 742, ES), True),
    ('Filiform apparatus', wbox(864, 776, 970, 822, ES), True), ('Micropylar end', wbox(666, 814, 816, 836, ES), True)])
d.basic('Mnemonic for the embryo sac (micropylar → chalazal)?', '"' + T('2-1-2-3') + '": 2 synergids + 1 egg at the micropyle, 2 polar nuclei in the middle, 3 antipodals at the chalaza = 8 nuclei')

d.sec('1.2.3-pollination')
d.basic('Why do flowering plants need pollination?', 'Both male and female gametes are ' + X('non-motile') + ', so they must be brought together')
d.basic('Define pollination.', 'Transfer of pollen grains from the ' + T('anther') + ' to the ' + T('stigma') + ' of a pistil')
d.basic('What is autogamy?', 'Pollination within the ' + T('same flower'), **fig('fig_1_9a_self'))
d.basic('Why is complete autogamy rare in open flowers?', 'It needs ' + T('synchrony') + ' of pollen release and stigma receptivity and anthers close to the stigma')
d.cloze('<i>Viola</i>, <i>Oxalis</i> and <i>Commelina</i> produce open {{c1::chasmogamous}} flowers and closed {{c2::cleistogamous}} flowers.')
d.basic('What are cleistogamous flowers?', 'Flowers that ' + X('do not open at all') + '; anthers dehisce in the bud and pollinate the stigma', **fig('fig_1_9c_cleistogamous'))
d.basic('Why are cleistogamous flowers invariably autogamous?', X('No chance') + ' of cross pollen landing on the stigma')
d.basic('Advantage and disadvantage of cleistogamy?', 'Advantage: ' + T('assured seed-set') + ' even without pollinators. Disadvantage: no variation, risk of inbreeding depression.')
d.basic('What is geitonogamy?', 'Pollen from anther to stigma of ' + T('another flower of the same plant'))
d.basic('Geitonogamy is functionally cross-pollination but genetically like…?', T('Autogamy') + ', because the pollen comes from the same plant')
d.basic('What is xenogamy?', 'Pollen from anther to stigma of a ' + T('different plant'), **fig('fig_1_9b_cross'))
d.basic('Only type of pollination bringing genetically different pollen?', T('Xenogamy'))
d.basic('Agents of pollination?', T('Abiotic') + ': wind, water. ' + T('Biotic') + ': animals. Most plants use biotic agents.')
d.basic('Why do wind/water-pollinated flowers make huge amounts of pollen?', 'Landing on the stigma is a ' + T('chance') + ' event; extra pollen compensates for loss')
d.basic('Features of wind-pollinated flowers?', T('Light, non-sticky pollen') + '; ' + T('well-exposed stamens') + '; large, often ' + T('feathery stigma') + '; single ovule per ovary; many flowers in an inflorescence', **fig('fig_1_10_wind'))
d.basic('What are the "silk" threads of a corn cob?', 'The ' + T('stigma and style') + ', waving in the wind to trap pollen')
d.basic('Common group showing wind pollination?', E('Grasses'))
d.basic('How common is water pollination?', 'Rare: about ' + N('30 genera') + ', mostly ' + T('monocotyledons'))
d.basic('Examples of water-pollinated plants?', EI('Vallisneria') + ', ' + EI('Hydrilla') + ' (fresh water); sea-grass ' + EI('Zostera') + ' (marine)')
d.basic('Why is distribution of some bryophytes and pteridophytes limited?', 'They need ' + T('water') + ' for transport of male gametes and fertilisation')
d.basic('Do water hyacinth and water lily use water for pollination?', X('No') + '. Flowers emerge above water and are pollinated by ' + T('insects or wind'))
d.basic('How is Vallisneria pollinated?', 'Female flower reaches the surface on a ' + T('long stalk') + '; male flowers/pollen released on the surface are carried passively by currents', **fig('fig_1_11a_vallisneria'))
d.basic('How are sea-grasses pollinated?', 'Female flowers stay ' + T('submerged') + '; long, ' + T('ribbon-like') + ' pollen is carried inside the water')
d.basic('How is pollen of water-pollinated species protected from wetting?', 'A ' + T('mucilaginous covering'))
d.basic('Why are wind/water-pollinated flowers not colourful and lack nectar?', 'They ' + X('need not attract animals') + '; making colour and nectar would waste energy')
d.basic('Common animal pollinators?', 'Bees, butterflies, flies, beetles, wasps, ants, moths, birds (' + E('sunbirds, hummingbirds') + '), bats')
d.basic('Dominant biotic pollinators?', T('Insects') + ', particularly ' + T('bees'))
d.basic('Unusual larger animal pollinators?', E('Lemurs') + ' (primates), arboreal rodents, reptiles (' + E('gecko, garden lizard') + ')')
d.basic('Features of insect-pollinated flowers?', T('Large, colourful, fragrant, nectar-rich') + '; small flowers clustered into an inflorescence', **fig('fig_1_11b_insect'))
d.basic('Why do flowers pollinated by flies and beetles smell foul?', 'To ' + T('attract') + ' these animals')
d.basic('Usual floral rewards?', T('Nectar') + ' and ' + T('pollen grains'))
d.basic('How does an animal bring about pollination?', 'While harvesting rewards it touches anthers, gets coated in (sticky) pollen, then touches a ' + T('stigma'))
d.basic('Tallest flower, and its reward?', EI('Amorphophallus') + ' (~' + N('6 ft') + '); reward is a safe place to ' + T('lay eggs'))
d.basic('Describe the Yucca–moth relationship.', 'Moth lays eggs in the ovary locule and pollinates the flower; larvae feed on developing seeds. ' + T('Neither can complete its life cycle without the other.'))
d.basic('What are pollen/nectar robbers?', 'Floral visitors that consume pollen/nectar ' + X('without pollinating') + ' the flower')

d.basic('Why do plants avoid continued self-pollination?', 'It leads to ' + T('inbreeding depression'))
table_card(d, 'Outbreeding devices', 'Prevents?', [
    ('Pollen release and stigma receptivity not synchronised', 'Autogamy', False),
    ('Anther and stigma at different positions', 'Autogamy', False),
    ('Self-incompatibility', 'Self-fertilisation (autogamy + geitonogamy)', False),
    ('Monoecy (castor, maize)', 'Autogamy only, not geitonogamy', True),
    ('Dioecy (papaya)', 'Both autogamy and geitonogamy', False)], term='Outbreeding devices')
d.basic('What is self-incompatibility?', 'A ' + T('genetic mechanism') + ' preventing self-pollen from fertilising ovules by inhibiting ' + T('pollen germination or pollen-tube growth') + ' in the pistil')
d.basic('Monoecious vs dioecious, with examples?', T('Monoecious') + ': male and female flowers on the same plant (' + E('castor, maize') + '). ' + T('Dioecious') + ': on different plants (' + E('papaya') + ').')

d.basic('Can a pistil tell right pollen from wrong pollen?', 'Yes. It recognises ' + T('compatible') + ' pollen and accepts it; rejects ' + T('incompatible') + ' pollen')
d.basic('How does the pistil reject wrong pollen?', 'Prevents ' + T('pollen germination') + ' on the stigma or ' + T('pollen-tube growth') + ' in the style')
d.basic('What mediates the pollen–pistil "dialogue"?', 'Chemical components of the ' + T('pollen') + ' interacting with those of the ' + T('pistil'))
d.basic('Through what does a pollen tube emerge?', 'One of the ' + T('germ pores'), **fig('fig_1_12abc_pollen_tube'))
d.basic('In 2-celled pollen, when are the male gametes formed?', 'Generative cell divides during growth of the pollen tube in the ' + T('stigma'))
d.basic('Path of the pollen tube?', 'Stigma → style → ovary → ovule via ' + T('micropyle') + ' → a ' + T('synergid') + ' via filiform apparatus', **fig('fig_1_12de_egg_apparatus'))
d.basic('Define pollen-pistil interaction.', 'All events from ' + T('pollen deposition on the stigma') + ' until ' + T('pollen tubes enter the ovule'))
d.basic('Why does pollen-pistil interaction matter to breeders?', 'Manipulating it, even in incompatible pollinations, can yield ' + T('desired hybrids'))
d.basic('How to see pollen germination in the lab?', 'Dust pollen (pea, chickpea, ' + EI('Crotalaria') + ', balsam, ' + EI('Vinca') + ') on ' + N('~10%') + ' sugar solution; observe after ' + N('15–30 min'))
d.basic('What is artificial hybridisation?', 'Crossing chosen parents so only ' + T('desired pollen') + ' reaches the stigma; a major crop-improvement approach')
d.basic('What is emasculation?', 'Removal of ' + T('anthers') + ' from a bisexual flower bud ' + T('before dehiscence') + ', using forceps')
d.basic('What is bagging?', 'Covering the emasculated flower with a bag (usually ' + T('butter paper') + ') to prevent contamination by unwanted pollen')
d.cloze('Artificial hybridisation: {{c1::emasculation}} → {{c2::bagging}} → dust desired pollen when stigma is receptive → {{c3::rebagging}}.')
d.basic('Is emasculation needed if the female parent has unisexual flowers?', X('No') + '. Female buds are simply bagged before opening, pollinated, then rebagged.')

# ---------------------------------------------------------------- 1.3 Double fertilisation
d.sec('1.3-double-fertilisation')
d.basic('What happens after the pollen tube enters a synergid?', 'It releases the ' + N('two male gametes') + ' into the synergid cytoplasm')
d.basic('What is syngamy?', 'Fusion of one male gamete with the ' + T('egg') + ' → diploid ' + T('zygote'))
d.basic('What is triple fusion?', 'Fusion of the second male gamete with the ' + N('two polar nuclei') + ' → triploid ' + T('primary endosperm nucleus (PEN)'))
d.basic('Where does triple fusion occur?', 'In the ' + T('central cell') + ' of the embryo sac')
d.basic('What is double fertilisation?', 'Occurrence of ' + T('syngamy + triple fusion') + ' in one embryo sac; unique to ' + T('flowering plants'))
d.cloze('After triple fusion the central cell becomes the {{c1::primary endosperm cell (PEC)}}, which develops into the {{c2::endosperm}}; the zygote develops into the {{c3::embryo}}.')
d.basic('Why is it called "fertilisation" if triple fusion forms no embryo? (intuition)', 'Both fusions involve a ' + T('male gamete') + '; one builds the baby (embryo), the other builds its lunch box (endosperm)')

# ---------------------------------------------------------------- 1.4 Post-fertilisation
d.sec('1.4-post-fertilisation')
d.basic('What are post-fertilisation events?', 'Endosperm and embryo development, maturation of ' + T('ovules → seeds') + ' and ' + T('ovary → fruit'))
d.sec('1.4.1-endosperm')
d.basic('Why does endosperm develop before the embryo?', 'To give ' + T('assured nutrition') + ' to the developing embryo')
d.basic('Ploidy and function of endosperm?', T('Triploid (3n)') + '; stores reserve food for the developing embryo')
d.basic('What is free-nuclear endosperm?', 'PEN divides repeatedly into ' + T('free nuclei') + ' without walls; later walls form and it becomes ' + T('cellular'))
d.cloze('Tender coconut water is {{c1::free-nuclear}} endosperm; the white kernel is {{c2::cellular}} endosperm.')
d.basic('Seeds where endosperm is fully consumed before maturity?', E('Pea, groundnut, beans'))
d.basic('Seeds where endosperm persists?', E('Castor and coconut') + ' (also cereals: wheat, rice, maize)')

d.sec('1.4.2-embryo')
d.basic('Where does the embryo develop?', 'At the ' + T('micropylar end') + ' of the embryo sac, where the zygote lies')
d.basic('Why does the zygote remain dormant for a while? (Exercise 12)', 'It divides only after some ' + T('endosperm') + ' forms, ensuring nutrition for the embryo')
d.cloze('Embryogeny: zygote → {{c1::proembryo}} → {{c2::globular}} → {{c3::heart-shaped}} → mature embryo.')
d.basic('Identify these structures (Figure 1.13).', '(a) Fertilised embryo sac with zygote and PEN; (b) stages of ' + T('dicot embryo') + ' development', **img('fig_1_13_embryo_stages'))
d.basic('Are early embryo stages different in monocots and dicots?', X('No') + '; early embryogeny is ' + T('similar') + ' in both')
d.basic('Parts of a typical dicot embryo?', 'An ' + T('embryonal axis') + ' and ' + N('two') + ' ' + T('cotyledons'))
table_card(d, 'Exercise 13a', 'What is it?', [
    ('Epicotyl', 'Axis above the cotyledons; ends in the plumule (stem tip)', False),
    ('Hypocotyl', 'Axis below the cotyledons; ends in the radicle (root tip)', False)], term='Epicotyl vs hypocotyl')
d.basic('What covers the root tip of the embryo?', 'A ' + T('root cap'))
d.occlusion('Figure 1.14 · Dicot embryo and grass embryo', M + 'fig_1_14_embryos.webp', EM, [
    ('Plumule', wbox(218, 57, 300, 79, EM), True), ('Cotyledons', wbox(216, 133, 324, 155, EM), True),
    ('Hypocotyl', wbox(214, 198, 312, 220, EM), True), ('Radicle', wbox(214, 314, 286, 335, EM), True),
    ('Root cap', wbox(214, 348, 299, 370, EM), True), ('Scutellum', wbox(210, 480, 312, 501, EM), True),
    ('Coleoptile', wbox(210, 581, 307, 603, EM), True), ('Shoot apex', wbox(210, 642, 320, 664, EM), True),
    ('Epiblast', wbox(208, 716, 292, 738, EM), True), ('Radicle', wbox(208, 864, 280, 885, EM), True),
    ('Root cap', wbox(208, 885, 294, 906, EM), True), ('Coleorhiza', wbox(208, 915, 312, 937, EM), True)])
d.basic('Cotyledon of the grass family called?', T('Scutellum') + ', lateral to the embryonal axis')
table_card(d, 'Exercise 13b', 'What does it sheath?', [
    ('Coleorhiza', 'Radicle and root cap', False), ('Coleoptile', 'Shoot apex and a few leaf primordia', False)], term='Coleoptile vs coleorhiza')
d.basic('In a grass embryo, the epicotyl is the axis above…?', 'The level of attachment of the ' + T('scutellum'))
d.basic('Correction: NCERT prints "radical" on p. 20. Correct word?', T('Radicle') + ' (the embryonic root); "radical" means something else')

d.sec('1.4.3-seed')
d.basic('What is a seed?', 'The final product of sexual reproduction; often described as a ' + T('fertilised ovule'))
d.basic('Parts of a typical seed?', T('Seed coat(s), cotyledon(s), embryo axis'), **fig('fig_1_15a_seeds'))
d.basic('Why are legume cotyledons thick?', 'They store ' + T('food reserves'))
d.basic('Non-albuminous (ex-albuminous) seeds, with examples?', 'No residual endosperm (consumed during embryo development): ' + E('pea, groundnut'))
d.basic('Albuminous seeds, with examples?', 'Retain part of the endosperm: ' + E('wheat, maize, barley, castor'))
d.basic('What is perisperm, with examples?', 'Residual, persistent ' + T('nucellus') + ' in the seed: ' + E('black pepper, beet'))
table_card(d, 'Exercise 13c, d', 'Develops from?', [
    ('Testa (seed coat)', 'Integuments of the ovule', False), ('Perisperm', 'Nucellus (persisting)', False),
    ('Pericarp (fruit wall)', 'Ovary wall', False)], term='Integument, testa, perisperm, pericarp')
d.basic('Role of the micropyle in a seed?', 'Remains as a small pore that lets ' + T('oxygen and water') + ' in during germination')
d.basic('Moisture content of a mature seed?', N('10–15%') + ' by mass')
d.basic('What is dormancy?', 'State of ' + T('inactivity') + ' of the embryo as the seed dries; it germinates when conditions become favourable')
d.basic('Conditions needed for seed germination?', 'Adequate ' + T('moisture, oxygen') + ' and suitable ' + T('temperature'))
d.basic('Fleshy vs dry fruits, examples?', T('Fleshy') + ': ' + E('guava, orange, mango') + '. ' + T('Dry') + ': ' + E('groundnut, mustard') + '.')
d.basic('What are false fruits?', 'Fruits where the ' + T('thalamus') + ' also contributes: ' + E('apple, strawberry, cashew'), **fig('fig_1_15b_false_fruits'))
d.basic('Why is apple a false fruit? (Exercise 14)', 'The fleshy edible part develops from the ' + T('thalamus') + ', not only the ovary')
d.basic('What are true fruits?', 'Fruits that develop ' + T('only from the ovary'))
d.basic('What are parthenocarpic fruits?', 'Fruits developed ' + X('without fertilisation') + ': seedless, e.g. ' + E('banana') + '; inducible with growth hormones')
d.basic('Which fruits would you choose for induced parthenocarpy? (Exercise 16)', 'Fruits eaten for their flesh with many/hard seeds: ' + E('orange, lemon, watermelon, grapes, guava') + ' (seedless is preferred)')
d.basic('Advantages of seeds to angiosperms?', T('Pollination and fertilisation independent of water') + '; better dispersal; food reserve for seedlings; hard coat protects embryo; new genetic combinations')
d.basic('Why are dehydration and dormancy crucial for agriculture?', 'They allow ' + T('storage') + ' of seeds as food all year and for the next crop')
d.basic('Oldest recorded viable seed?', EI('Lupinus arcticus') + ' from Arctic tundra: germinated after ~' + N('10,000 years'))
d.basic('2000-year-old viable seed?', 'Date palm, ' + EI('Phoenix dactylifera') + ', from King Herod’s palace near the Dead Sea')
d.basic('Plants whose fruits contain thousands of tiny seeds?', E('Orchids') + ', parasitic ' + EI('Orobanche') + ' and ' + EI('Striga'))

# ---------------------------------------------------------------- 1.5 Apomixis
d.sec('1.5-apomixis-polyembryony')
d.basic('What is apomixis?', 'Production of ' + T('seeds without fertilisation') + ': asexual reproduction that mimics sexual reproduction')
d.basic('Where is apomixis found?', 'Some species of ' + E('Asteraceae and grasses'))
d.basic('Apomixis vs parthenocarpy?', T('Apomixis') + ': seed without fertilisation. ' + T('Parthenocarpy') + ': fruit without fertilisation (seedless).')
d.basic('One way apomictic seeds form?', 'A ' + T('diploid egg') + ' forms without reduction division and develops into an embryo without fertilisation')
d.basic('Another way (e.g. Citrus, mango)?', T('Nucellar cells') + ' around the embryo sac divide, protrude into it and develop into embryos')
d.basic('What is polyembryony?', 'More than one embryo in a seed, e.g. ' + E('orange (Citrus)') + ', ' + E('mango'))
d.basic('Genetic nature of apomictic (nucellar) embryos?', 'Genetically ' + T('identical to the mother') + ': they are ' + T('clones'))
d.basic('Problem with hybrid seeds?', 'Must be produced ' + T('every year') + '; seeds from hybrids ' + X('segregate') + ' and lose hybrid characters; costly for farmers')
d.basic('Why is apomixis important to the hybrid seed industry?', 'Apomictic hybrids show ' + X('no segregation') + ', so farmers can reuse hybrid seed year after year')
d.basic('Why does an apomictic hybrid not segregate? (intuition)', 'No meiosis and no fertilisation: every seed is a ' + T('photocopy') + ' of the hybrid mother')

# ---------------------------------------------------------------- Summary
d.sec('summary')
table_card(d, 'Exercise 2', 'Micro vs mega?', [
    ('Mother cell', 'PMC vs MMC', False), ('Division', 'Meiosis in both', False),
    ('Product', 'Microspore tetrad → pollen vs 4 megaspores (1 functional)', False),
    ('Gametophyte', 'Pollen grain vs embryo sac', False)], term='Microsporogenesis vs megasporogenesis')
table_card(d, 'Fate after fertilisation', 'Becomes?', [
    ('Ovary', 'Fruit', False), ('Ovary wall', 'Pericarp', False), ('Ovule', 'Seed', False),
    ('Integuments', 'Seed coat (testa, tegmen)', False), ('Zygote', 'Embryo', False), ('PEC', 'Endosperm', False)],
    term='Post-fertilisation fates')

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
