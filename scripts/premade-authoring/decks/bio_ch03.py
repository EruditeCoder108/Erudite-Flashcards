import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase as sc

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch03-plant-kingdom')
d = Deck('Chapter 3: Plant Kingdom', 'Class 11', ['class-11', 'biology', 'ch-3'])
d.description = 'Classification systems, algae, bryophytes, pteridophytes, gymnosperms and angiosperms'
M = 'media/'
P = lambda b: pad(b, 6)

# ---------------------------------------------------------------- Introduction
d.sec('intro-classification-systems')
d.basic('Which organisms, once placed in Plantae, have now been excluded from it?', 'Fungi, and members of ' + T('Monera') + ' and ' + T('Protista') + ' having cell walls')
d.basic("Why are cyanobacteria (blue green algae) no longer called 'algae'?", 'They are ' + T('prokaryotes') + ' (Monera), now excluded from Plantae')
d.basic('Which five groups does NCERT describe under Plantae?', 'Algae, bryophytes, pteridophytes, gymnosperms, angiosperms')
d.basic('What characters did the earliest (artificial) classification systems use?', 'Gross superficial ' + T('morphological') + ' characters: habit, colour, number and shape of leaves, etc.')
d.basic("On which structure was Linnaeus' artificial system mainly based?", 'The ' + T('androecium') + ' (and vegetative characters)')
d.basic('Give two drawbacks of artificial systems.', '<ul><li>They ' + X('separated closely related species') + ', being based on a few characters</li>'
        '<li>They gave ' + X('equal weightage') + ' to vegetative and sexual characters, though vegetative characters are more easily affected by environment</li></ul>')
d.basic('On what are natural classification systems based?', 'Natural ' + T('affinities') + ': external and internal features such as ultrastructure, anatomy, embryology and phytochemistry')
d.basic('Who gave a natural classification for flowering plants?', T('George Bentham') + ' and ' + T('Joseph Dalton Hooker'))
d.basic('On what are phylogenetic classification systems based?', T('Evolutionary relationships') + '; organisms of the same taxa are assumed to have a common ancestor')
d.basic('What is numerical taxonomy?', 'Classification using ' + T('all observable characters') + ', coded as numbers and processed by computer; each character gets equal importance')
d.basic('What is cytotaxonomy based on?', T('Cytological') + ' information: chromosome number, structure and behaviour')
d.basic('What does chemotaxonomy use?', 'The ' + T('chemical constituents') + ' of the plant')

# ---------------------------------------------------------------- 3.1 Algae
d.sec('3.1-algae')
d.basic('Describe algae in five words (NCERT).', 'Chlorophyll-bearing, simple, ' + T('thalloid') + ', autotrophic, largely ' + T('aquatic'))
d.basic('Name three non-aquatic habitats of algae.', 'Moist stones, soils and wood')
d.basic('Algae live in association with which organisms?', 'Fungi (' + T('lichen') + ') and animals (e.g. on ' + E('sloth bear') + ')')
d.cloze('Algae range from colonial forms like {{c1::<i>Volvox</i>}} to filamentous forms like {{c2::<i>Ulothrix</i> and <i>Spirogyra</i>}}; marine {{c3::kelps}} form massive plant bodies.')
d.basic('How do algae reproduce vegetatively?', 'By ' + T('fragmentation') + '; each fragment develops into a thallus')
d.basic('What are the most common asexual spores of algae?', T('Zoospores') + ': flagellated (motile), germinating into new plants')
sc.gamete_fusion(d)
d.basic('What is isogamy?', 'Fusion of two gametes ' + T('similar in size') + ', flagellated (' + EI('Ulothrix') + ') or non-flagellated (' + EI('Spirogyra') + ')')
d.basic('What is anisogamy? Example?', 'Fusion of two gametes ' + T('dissimilar in size') + ', e.g. ' + EI('Eudorina'))
d.basic('What is oogamy? Examples?', 'Fusion of a large, non-motile (static) female gamete with a smaller, motile male gamete, e.g. ' + EI('Volvox') + ', ' + EI('Fucus'))
d.occlusion('Figure 3.1 · Name each alga', M + 'fig_3_1_algae_grid.webp', (1020, 1428), [
    ('<i>Volvox</i> (green)', [60, 422, 220, 50]), ('<i>Ulothrix</i> (green)', [400, 422, 220, 50]),
    ('<i>Laminaria</i> (brown)', [740, 422, 220, 50]), ('<i>Fucus</i> (brown)', [60, 898, 220, 50]),
    ('<i>Dictyota</i> (brown)', [400, 898, 220, 50]), ('<i>Porphyra</i> (red)', [740, 898, 220, 50]),
    ('<i>Polysiphonia</i> (red)', [400, 1374, 220, 50])])
d.occlusion('Figure 3.1 · <i>Volvox</i>', M + 'fig_3_1_volvox.webp', (1001, 757), [
    ('Daughter colony', [730, 290, 250, 120]), ('Parent colony', [760, 545, 190, 125])], printed=True)
d.occlusion('Figure 3.1 · <i>Laminaria</i>', M + 'fig_3_1_laminaria.webp', (549, 1001), [
    ('Frond', [340, 552, 160, 60]), ('Stipe', [262, 846, 130, 62]), ('Holdfast', [296, 948, 210, 53])], printed=True)
d.occlusion('Figure 3.1 · <i>Fucus</i>', M + 'fig_3_1_fucus.webp', (909, 1001), [
    ('Air bladder', [590, 182, 295, 62]), ('Frond', [615, 322, 165, 64]), ('Midrib', [586, 412, 178, 64]),
    ('Holdfast', [586, 886, 220, 64])], printed=True)

d.sec('3.1-algae-uses')
d.basic('How much of the total CO<sub>2</sub> fixation on earth do algae carry out?', 'At least ' + N('half'))
d.basic('Why are algae of paramount importance in water?', 'As ' + T('primary producers') + ' of energy-rich compounds, the basis of aquatic food cycles; they also raise dissolved oxygen')
d.basic('How many species of marine algae are used as food? Name three genera.', 'About ' + N('70') + ': ' + EI('Porphyra') + ', ' + EI('Laminaria') + ', ' + EI('Sargassum'))
d.cloze('Hydrocolloids: {{c1::algin}} comes from brown algae and {{c2::carrageen}} from red algae.')
d.basic('What are hydrocolloids?', T('Water holding') + ' substances, used commercially')
d.basic('Agar is obtained from which algae?', EI('Gelidium') + ' and ' + EI('Gracilaria'))
d.basic('What is agar used for?', 'Growing ' + T('microbes') + ', and in ice-creams and jellies')
d.basic('Which unicellular alga is used as a protein-rich food supplement, even by space travellers?', EI('Chlorella'))
d.basic('Name the three main classes of algae.', T('Chlorophyceae') + ', ' + T('Phaeophyceae') + ', ' + T('Rhodophyceae'))
d.basic('What is the basis of classifying algae into classes?', 'The type of ' + T('pigment') + ' and the type of ' + T('stored food'))

d.sec('3.1.1-chlorophyceae')
d.basic('What is the common name of Chlorophyceae?', T('Green algae'))
d.basic('Why are green algae grass green?', 'Dominance of ' + T('chlorophyll <i>a</i> and <i>b</i>'))
d.basic('Name six shapes of chloroplasts in green algae.', 'Discoid, plate-like, reticulate, cup-shaped, spiral, ribbon-shaped')
d.basic('What are pyrenoids, and what do they contain?', 'Storage bodies in the ' + T('chloroplasts') + '; they contain ' + T('protein') + ' besides starch')
d.basic('Besides starch, in what form may some green algae store food?', T('Oil droplets'))
d.basic('What is the cell wall of green algae made of?', 'Inner layer of ' + T('cellulose') + ', outer layer of ' + T('pectose'))
d.basic('Where are zoospores produced in green algae?', 'In ' + T('zoosporangia'))
d.basic('Name five common green algae.', EI('Chlamydomonas, Volvox, Ulothrix, Spirogyra, Chara'))

d.sec('3.1.2-phaeophyceae')
d.basic('Where are brown algae found?', 'Primarily in ' + T('marine') + ' habitats')
d.basic('Give a simple and a profusely branched brown alga.', 'Simple branched filamentous: ' + EI('Ectocarpus') + '. Profusely branched: ' + E('kelps'))
d.basic('How tall may kelps grow?', N('100 metres'))
d.basic('Which pigments do brown algae possess?', 'Chlorophyll ' + T('<i>a</i>, <i>c</i>') + ', carotenoids and xanthophylls')
d.basic('Which pigment decides the colour (olive green to brown) of brown algae?', 'The xanthophyll ' + T('fucoxanthin'))
d.basic('In what form do brown algae store food?', 'Complex carbohydrates: ' + T('laminarin') + ' or ' + T('mannitol'))
d.basic('What covers the cellulosic wall of brown algae?', 'A gelatinous coating of ' + T('algin'))
d.cloze('A brown alga is attached to the substratum by a {{c1::holdfast}}, has a stalk, the {{c2::stipe}}, and a leaf-like photosynthetic organ, the {{c3::frond}}.')
d.basic('Describe the zoospores of brown algae.', T('Biflagellate') + ', pear-shaped, with two ' + T('unequal laterally') + ' attached flagella')
d.basic('Where may union of gametes take place in brown algae?', 'In water, or within the ' + T('oogonium') + ' (oogamous species)')
d.basic('Name five common brown algae.', EI('Ectocarpus, Dictyota, Laminaria, Sargassum, Fucus'))

d.sec('3.1.3-rhodophyceae')
d.basic('Why are red algae red?', 'Predominance of the red pigment ' + T('r-phycoerythrin'))
d.basic('Where are most red algae found?', T('Marine') + ', with greater concentrations in ' + T('warmer') + ' areas')
d.basic('At what depths do red algae occur?', 'Both near the surface and at ' + T('great depths') + ' where little light penetrates')
d.basic('In what form do red algae store food?', T('Floridean starch') + ', very similar to amylopectin and glycogen')
d.basic('How do red algae reproduce asexually and sexually?', 'Asexually by ' + X('non-motile') + ' spores; sexually by non-motile gametes (' + T('oogamous') + ')')
d.basic('What follows fertilisation in red algae?', T('Complex post fertilisation') + ' developments')
d.basic('Name four common red algae.', EI('Polysiphonia, Porphyra, Gracilaria, Gelidium'))

d.sec('table-3.1')
sc.algae_tiles(d, 'Major pigments?', ('Chlorophyll <i>a</i>, <i>b</i>', 'Chlorophyll <i>a</i>, <i>c</i>, fucoxanthin', 'Chlorophyll <i>a</i>, <i>d</i>, phycoerythrin'), 'Algae classes: pigments')
sc.algae_tiles(d, 'Stored food?', ('Starch', 'Mannitol, laminarin', 'Floridean starch'), 'Algae classes: stored food')
sc.algae_tiles(d, 'Cell wall?', ('Cellulose', 'Cellulose and algin', 'Cellulose, pectin and poly sulphate esters'), 'Algae classes: cell wall')
sc.algae_tiles(d, 'Flagella: number and insertion?', ('2–8, equal, apical', '2, unequal, lateral', 'Absent'), 'Algae classes: flagella')
sc.algae_tiles(d, 'Habitat?', ('Fresh water, brackish water, salt water', 'Fresh water (rare), brackish, salt water', 'Fresh water (some), brackish, salt water (most)'), 'Algae classes: habitat')
d.basic('Which class of algae has no flagellated cells?', T('Rhodophyceae') + ' (red algae)')
d.basic('Which chlorophyll is found only in red algae (among the three classes)?', T('Chlorophyll <i>d</i>'))

# ---------------------------------------------------------------- 3.2 Bryophytes
d.sec('3.2-bryophytes')
d.basic('Which plants make up the bryophytes, and where do they grow?', T('Mosses') + ' and ' + T('liverworts') + ', in moist shaded areas in the hills')
d.basic("Why are bryophytes called the 'amphibians of the plant kingdom'?", 'They live in soil but ' + T('depend on water') + ' for sexual reproduction')
d.basic('What role do bryophytes play on bare rocks and soil?', 'An important role in ' + T('plant succession'))
d.basic('What attaches a bryophyte to the substratum?', 'Unicellular or multicellular ' + T('rhizoids'))
d.basic('Do bryophytes have true roots, stems or leaves?', X('No') + '. They may have root-like, leaf-like or stem-like structures')
d.basic('Is the main plant body of a bryophyte haploid or diploid? What is it called?', T('Haploid') + '; it produces gametes, so it is the ' + T('gametophyte'))
d.cloze('The male sex organ of bryophytes, the {{c1::antheridium}}, produces {{c2::biflagellate antherozoids}}; the flask-shaped female sex organ, the {{c3::archegonium}}, produces a {{c4::single egg}}.')
d.basic('Are the sex organs of bryophytes unicellular or multicellular?', T('Multicellular'))
d.basic('Does the bryophyte zygote undergo meiosis at once?', X('No') + '. It forms a multicellular ' + T('sporophyte') + ' first')
d.basic('Is the bryophyte sporophyte free-living?', X('No') + '. It is attached to the photosynthetic gametophyte and ' + T('derives nourishment') + ' from it')
d.basic('In bryophytes, which cells undergo meiosis and what do they form?', 'Some cells of the ' + T('sporophyte') + ', forming haploid ' + T('spores') + ', which germinate into gametophytes')
sc.dominant_generation(d)
d.basic('Which moss provides peat?', EI('Sphagnum'))
d.basic('What is peat (from <i>Sphagnum</i>) used for?', T('Fuel') + ', and as packing material for trans-shipment of living material (it holds water)')
d.basic('Which organisms are the first to colonise rocks?', T('Mosses') + ' along with ' + T('lichens'))
d.basic('How do mosses help higher plants on rocks?', 'They ' + T('decompose rocks') + ', making the substrate suitable for higher plants')
d.basic('How do mosses prevent soil erosion?', 'Their dense mats reduce the impact of ' + T('falling rain'))
d.basic('Into which two groups are bryophytes divided?', T('Liverworts') + ' and ' + T('mosses'))

d.sec('3.2.1-liverworts')
d.basic('Name five habitats of liverworts.', 'Banks of streams, marshy ground, damp soil, bark of trees, deep in the woods')
d.basic('Give an example of a thalloid liverwort.', EI('Marchantia'))
d.basic('Describe the thallus of a liverwort.', T('Dorsiventral') + ' and closely appressed to the substrate')
d.basic('How are the leaf-like appendages of leafy liverworts arranged?', 'Tiny, in ' + N('two rows') + ' on the stem-like structures')
d.basic('What are gemmae?', 'Green, multicellular, ' + T('asexual buds') + ' that develop in gemma cups on the thalli')
d.basic('Where do gemmae develop?', 'In small receptacles called ' + T('gemma cups'))
d.basic('Into what is the liverwort sporophyte differentiated?', T('Foot, seta and capsule'))
d.occlusion('Figure 3.2 · <i>Marchantia</i>: (a) female thallus, (b) male thallus', M + 'fig_3_2_marchantia.webp', (1001, 487), [
    ('Archegoniophore', P((160, 65, 201, 24))), ('Antheridiophore', P((798, 32, 193, 24))),
    ('Gemma cup', P((199, 209, 144, 24))), ('Gemma cup', P((818, 206, 143, 24))),
    ('Rhizoids', P((241, 417, 101, 24))), ('Rhizoids', P((859, 414, 101, 24)))], printed=True)
d.basic('In <i>Marchantia</i>, which thallus bears the archegoniophore?', 'The ' + T('female') + ' thallus (the male bears the antheridiophore)')

d.sec('3.2.2-mosses')
d.basic('Which stage is predominant in the life cycle of a moss?', 'The ' + T('gametophyte'))
d.basic('Name the two stages of the moss gametophyte.', 'The ' + T('protonema') + ' stage and the ' + T('leafy') + ' stage')
d.basic('Describe the protonema.', 'Develops directly from a ' + T('spore') + '; creeping, green, branched, frequently filamentous')
d.basic('From what does the leafy stage of a moss develop?', 'From the ' + T('secondary protonema') + ', as a lateral bud')
d.basic('Which stage of the moss bears the sex organs?', 'The ' + T('leafy stage'))
d.basic('How are leaves arranged in the leafy stage of a moss?', T('Spirally') + ', on upright slender axes')
d.basic('What kind of rhizoids do mosses have?', T('Multicellular') + ' and branched')
d.basic('How do mosses reproduce vegetatively?', 'By ' + T('fragmentation') + ' and ' + T('budding') + ' in the secondary protonema')
d.basic('Where are the sex organs of a moss produced?', 'At the ' + T('apex') + ' of the leafy shoots')
d.basic('Compare the sporophyte of mosses with that of liverworts.', 'Moss sporophyte (foot, seta, capsule) is ' + T('more elaborate') + '; mosses have an elaborate spore dispersal mechanism')
d.basic('Name three common mosses.', EI('Funaria, Polytrichum, Sphagnum'))
d.occlusion('Figure 3.2 (c) · <i>Funaria</i>: gametophyte and sporophyte', M + 'fig_3_2_funaria.webp', (992, 1001), [
    ('Capsule', P((729, 67, 169, 43))), ('Seta', P((576, 294, 92, 43))), ('Sporophyte', P((49, 232, 238, 43))),
    ('Gametophyte', P((16, 697, 278, 43))), ('Leaves', P((520, 430, 140, 43))), ('Main axis', P((646, 782, 203, 43))),
    ('Rhizoids', P((712, 849, 178, 43)))], printed=True)
d.occlusion('Figure 3.2 (d) · <i>Sphagnum</i> gametophyte', M + 'fig_3_2_sphagnum.webp', (1001, 1001), [
    ('Antheridial branch', P((68, 35, 231, 92))), ('Branches', P((765, 106, 197, 42))), ('Archegonial branch', P((697, 558, 245, 92)))],
    printed=True)
table_card(d, '3.2 · Bryophytes', 'Liverworts vs mosses?', [
    ('Plant body', 'Liverwort: thalloid, dorsiventral. Moss: upright axes with spiral leaves', False),
    ('Asexual', 'Liverwort: gemmae. Moss: fragmentation, budding in protonema', False),
    ('Sporophyte', 'Moss: more elaborate (both have foot, seta, capsule)', False)], term='Liverworts vs mosses')

# ---------------------------------------------------------------- 3.3 Pteridophytes
d.sec('3.3-pteridophytes')
d.basic('Which plants make up the pteridophytes?', T('Horsetails') + ' and ' + T('ferns'))
d.basic('Name three uses of pteridophytes.', 'Medicinal purposes, soil-binders, ornamentals')
d.basic('Which were evolutionarily the first terrestrial plants with vascular tissues?', T('Pteridophytes') + ' (xylem and phloem)')
d.basic('Where are pteridophytes found?', 'Cool, damp, shady places (some in ' + T('sandy soil') + ')')
d.basic('Is the main plant body of a pteridophyte a gametophyte or a sporophyte?', T('Sporophyte') + ', differentiated into true root, stem and leaves')
d.cloze('Pteridophyte leaves are small ({{c1::microphylls}}) as in <i>Selaginella</i>, or large ({{c2::macrophylls}}) as in ferns.')
d.basic('What are sporophylls?', 'Leaf-like appendages that subtend the ' + T('sporangia'))
d.basic('What are strobili (cones)? Examples?', 'Compact structures formed by ' + T('sporophylls') + ', e.g. ' + EI('Selaginella') + ', ' + EI('Equisetum'))
d.basic('How are spores produced in pteridophytes?', 'By ' + T('meiosis') + ' in spore mother cells in the sporangia')
d.basic('What is the prothallus?', 'The small, multicellular, free-living, mostly photosynthetic thalloid ' + T('gametophyte') + ' of pteridophytes')
d.basic('Why is the spread of living pteridophytes restricted?', 'The gametophyte needs cool, damp, shady places, and ' + T('water') + ' is needed for fertilisation')
d.basic('What is water needed for in pteridophyte fertilisation?', 'To transfer ' + T('antherozoids') + ' from the antheridia to the mouth of the archegonium')
d.basic('What are homosporous pteridophytes?', 'Those producing ' + T('similar kinds') + ' of spores (the majority)')
d.basic('What are heterosporous pteridophytes? Examples?', 'Those producing ' + T('macro (large) and micro (small)') + ' spores: ' + EI('Selaginella') + ', ' + EI('Salvinia'))
d.basic('What do megaspores and microspores give rise to?', 'Megaspores: ' + T('female') + ' gametophytes. Microspores: ' + T('male') + ' gametophytes.')
d.basic('Why is heterospory in <i>Selaginella</i> and <i>Salvinia</i> an important step in evolution?', 'The female gametophyte is retained on the sporophyte and the embryo develops within it: a ' + T('precursor to the seed habit'))
table_card(d, '3.3 · Pteridophytes', 'Give the NCERT example(s) of each class.', [
    ('Psilopsida', '<i>Psilotum</i>', False), ('Lycopsida', '<i>Selaginella</i>, <i>Lycopodium</i>', False),
    ('Sphenopsida', '<i>Equisetum</i>', False), ('Pteropsida', '<i>Dryopteris</i>, <i>Pteris</i>, <i>Adiantum</i>', False)],
    term='Pteridophyte classes: examples')
d.basic('<i>Equisetum</i> belongs to which class of pteridophytes?', T('Sphenopsida') + ' (horsetails)')
d.basic('<i>Adiantum</i> belongs to which class of pteridophytes?', T('Pteropsida'))
d.occlusion('Figure 3.3 · Name each pteridophyte', M + 'fig_3_3_pteridophytes_grid.webp', (900, 972), [
    ('<i>Selaginella</i>', [60, 432, 330, 50]), ('<i>Equisetum</i>', [510, 432, 330, 50]),
    ('Fern', [60, 918, 330, 50]), ('<i>Salvinia</i>', [510, 918, 330, 50])])
d.occlusion('Figure 3.3 (a) · <i>Selaginella</i>', M + 'fig_3_3_selaginella.webp', (1001, 803), [
    ('Leaves', [400, 182, 152, 50]), ('Stem', [286, 382, 118, 50]), ('Roots', [836, 472, 132, 50])], printed=True)
d.occlusion('Figure 3.3 (b) · <i>Equisetum</i>', M + 'fig_3_3_equisetum.webp', (618, 1001), [
    ('Strobilus', P((445, 89, 133, 30))), ('Node', P((471, 278, 73, 30))), ('Internode', P((439, 349, 141, 30))),
    ('Branch', P((473, 621, 107, 30))), ('Rhizome', P((38, 846, 125, 30)))], printed=True)

# ---------------------------------------------------------------- 3.4 Gymnosperms
d.sec('3.4-gymnosperms')
d.basic("What does 'gymnosperm' mean?", T('Naked seeds') + ' (gymnos: naked, sperma: seeds)')
d.basic('Why are gymnosperms called naked-seeded?', 'Ovules are ' + X('not enclosed') + ' by an ovary wall before or after fertilisation, so seeds are uncovered')
d.basic('Which gymnosperm is one of the tallest tree species?', 'The giant redwood, ' + EI('Sequoia'))
d.basic('What kind of roots do gymnosperms generally have?', T('Tap roots'))
d.cloze('Roots of <i>Pinus</i> have a fungal association called {{c1::mycorrhiza}}; <i>Cycas</i> has small specialised {{c2::coralloid}} roots associated with {{c3::N<sub>2</sub>-fixing cyanobacteria}}.')
d.basic('Give a gymnosperm with an unbranched stem and two with branched stems.', 'Unbranched: ' + EI('Cycas') + '. Branched: ' + EI('Pinus') + ', ' + EI('Cedrus'))
d.basic('In which gymnosperm do the pinnate leaves persist for a few years?', EI('Cycas'))
d.basic('How are conifer leaves adapted to reduce water loss?', '<ul><li>Needle-like: less surface area</li><li>Thick cuticle</li><li>Sunken stomata</li></ul>')
d.basic('Are gymnosperms homosporous or heterosporous?', T('Heterosporous') + ': haploid microspores and megaspores')
d.basic('What are male strobili (microsporangiate strobili)?', 'Strobili bearing ' + T('microsporophylls') + ' and microsporangia')
d.basic('What is the pollen grain of a gymnosperm?', 'The highly reduced ' + T('male gametophyte') + ', confined to a limited number of cells')
d.basic('Where do pollen grains develop?', 'Within the ' + T('microsporangia'))
d.basic('What are female (macrosporangiate) strobili?', 'Cones bearing ' + T('megasporophylls') + ' with ovules (megasporangia)')
d.basic('Are male and female cones on the same tree?', 'In ' + EI('Pinus') + ', ' + T('yes') + '. In ' + EI('Cycas') + ', male cones and megasporophylls are on ' + X('different trees') + '.')
d.basic('From what is the megaspore mother cell differentiated?', 'One of the cells of the ' + T('nucellus'))
d.basic('What is an ovule?', 'The ' + T('nucellus') + ' protected by envelopes: a composite structure')
d.basic('How many megaspores does the megaspore mother cell form, and how many develop further?', N('Four') + ' by meiosis; ' + N('one') + ' develops into the female gametophyte')
d.basic('What does the female gametophyte of a gymnosperm bear?', N('Two or more') + ' ' + T('archegonia'))
d.basic('Do gymnosperm gametophytes live independently?', X('No') + '. Unlike bryophytes and pteridophytes, they remain within the sporangia on the sporophyte')
d.basic('How does the pollen grain reach the ovule in gymnosperms?', 'Carried by ' + T('air currents') + ' to the opening of the ovules')
d.basic('What does the pollen tube do in gymnosperms?', 'Carries the male gametes towards the archegonia and discharges them near the ' + T('mouth of the archegonia'))
d.basic('After fertilisation in gymnosperms, what do the zygote and the ovule become?', 'Zygote: ' + T('embryo') + '. Ovule: ' + T('seed') + ' (uncovered).')
d.occlusion('Figure 3.4 · Name each gymnosperm', M + 'fig_3_4_gymnosperms_grid.webp', (900, 972), [
    ('<i>Cycas</i>', [60, 432, 330, 50]), ('<i>Pinus</i>', [510, 432, 330, 50]), ('<i>Ginkgo</i>', [285, 918, 330, 50])])
d.occlusion('Figure 3.4 (c) · <i>Ginkgo</i>', M + 'fig_3_4_ginkgo.webp', (1001, 752), [
    ('Dwarf shoot', P((50, 132, 282, 46))), ('Long shoot', P((63, 367, 255, 46))), ('Seeds', P((196, 610, 126, 46)))], printed=True)
d.basic('Both gymnosperms and angiosperms bear seeds. Why are they classified separately?', 'Gymnosperm ovules and seeds are ' + X('naked') + '; angiosperm ovules are in flowers and seeds are ' + T('enclosed in fruits'))

# ---------------------------------------------------------------- 3.5 Angiosperms
d.sec('3.5-angiosperms')
d.basic('In angiosperms, where are the pollen grains and ovules developed?', 'In specialised structures called ' + T('flowers'))
d.basic('What encloses the seeds of angiosperms?', T('Fruits'))
d.basic('Name the smallest angiosperm and a tall angiosperm tree (with height).', 'Smallest: ' + EI('Wolffia') + '. Tall: ' + EI('Eucalyptus') + ' (over ' + N('100 metres') + ')')
d.basic('Into which two classes are angiosperms divided?', T('Dicotyledons') + ' and ' + T('monocotyledons'))
d.basic('Name four uses of angiosperms.', 'Food, fodder, fuel, medicines (and other commercial products)')

# ---------------------------------------------------------------- Across groups
d.sec('across-groups')
d.basic('Name three groups of plants that bear archegonia.', 'Bryophytes, pteridophytes, gymnosperms')
d.basic('Match: <i>Chlamydomonas</i>, <i>Cycas</i>, <i>Selaginella</i>, <i>Sphagnum</i>.',
        EI('Chlamydomonas') + ': alga. ' + EI('Cycas') + ': gymnosperm. ' + EI('Selaginella') + ': pteridophyte. ' + EI('Sphagnum') + ': moss.')
table_card(d, 'Ploidy', 'Haploid (n) or diploid (2n)?', [
    ('Protonema cell of a moss', 'n', False), ('Leaf cell of a moss', 'n', False), ('Prothallus cell of a fern', 'n', False),
    ('Gemma cell of <i>Marchantia</i>', 'n', False), ('Zygote of a fern', '2n', False)], term='Ploidy of plant cells')

os.makedirs(OUT, exist_ok=True)
n = d.write(os.path.join(OUT, 'deck.json'))
print('notes', n)
