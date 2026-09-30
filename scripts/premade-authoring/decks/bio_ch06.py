import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch06-anatomy-of-flowering-plants')
d = Deck('Chapter 6: Anatomy of Flowering Plants', 'Class 11', ['class-11', 'biology', 'ch-6'])
d.description = 'Tissue systems, stomata, vascular bundles, and T.S. of dicot and monocot root, stem and leaf'
M = 'media/'
P = lambda b: pad(b, 6)
fig = lambda name: {'definitionImage': M + name + '.webp'}

d.sec('intro')
d.basic('What is anatomy?', 'The study of the ' + T('internal structure') + ' of plants')
d.basic('How is a plant organised, from unit to organ?', 'Cells → ' + T('tissues') + ' → organs')
d.basic('Name the three tissue systems of a plant.', T('Epidermal') + ', ' + T('ground (fundamental)') + ', ' + T('vascular (conducting)'))

# ---------------------------------------------------------------- 6.1.1 Epidermal
d.sec('6.1.1-epidermal')
d.basic('What makes up the epidermal tissue system?', 'Epidermal cells, ' + T('stomata') + ', and epidermal appendages (' + T('trichomes and hairs') + ')')
d.basic('Describe the epidermis.', 'Outermost layer of the primary plant body.<br>Elongated, compactly arranged, usually ' + N('single') + '-layered, parenchymatous cells with a large vacuole')
d.basic('What is the cuticle, and where is it absent?', 'A waxy thick layer on the epidermis that prevents water loss; ' + X('absent in roots'))
d.basic('What do stomata regulate?', T('Transpiration') + ' and ' + T('gaseous exchange'))
d.basic('Shape of guard cells in most plants and in grasses?', 'Most: ' + T('bean-shaped') + '. Grasses: ' + T('dumb-bell shaped') + '.')
d.basic('Which wall of a guard cell is thickened?', 'The ' + T('inner') + ' wall (towards the pore); the outer wall is thin')
d.basic('Why does thick inner / thin outer wall matter for opening?', 'When guard cells swell, the thin outer walls stretch more, so the cells bow ' + T('outwards') + ' and the pore opens.<br>(Intuition beyond NCERT)')
d.basic('What are subsidiary cells?', 'Epidermal cells near the guard cells, specialised in shape and size')
d.basic('What is the stomatal apparatus?', 'Stomatal aperture + ' + T('guard cells') + ' + surrounding ' + T('subsidiary cells'))
d.occlusion('Figure 6.1 · Stomata: (a) bean-shaped, (b) dumb-bell shaped guard cells', M + 'fig_6_1_stomata.webp', (1001, 233), [
    ('Epidermal cells', P((428, 25, 154, 20))), ('Subsidiary cells', P((427, 65, 161, 20))), ('Chloroplast', P((428, 102, 117, 20))),
    ('Guard cells', P((437, 136, 115, 20))), ('Stomatal pore', P((435, 174, 91, 44)))], printed=True)
d.basic('Root hairs vs trichomes?', 'Root hairs: ' + T('unicellular') + ' outgrowths of root epidermis that absorb water. Trichomes: hairs on the stem, usually ' + T('multicellular') + '.')
d.basic('Describe trichomes and their role.', 'Branched or unbranched, soft or stiff, may be secretory; they ' + T('prevent water loss') + ' by transpiration')

# ---------------------------------------------------------------- 6.1.2 Ground
d.sec('6.1.2-ground')
d.basic('What makes up the ground tissue?', 'All tissues ' + X('except') + ' epidermis and vascular bundles: parenchyma, collenchyma, sclerenchyma')
d.basic('Where is parenchyma found in primary stems and roots?', 'Cortex, pericycle, pith, medullary rays')
d.basic('What is mesophyll?', 'The ground tissue of leaves: thin-walled cells with ' + T('chloroplasts'))

# ---------------------------------------------------------------- 6.1.3 Vascular
d.sec('6.1.3-vascular')
d.basic('What makes a vascular bundle?', T('Xylem') + ' and ' + T('phloem') + ' together')
d.basic('Open vs closed vascular bundles?', T('Open') + ': cambium between xylem and phloem, can form secondary tissues (dicot stems)<br>' + T('Closed') + ': no cambium (monocots)')
d.basic('What is a radial vascular bundle? Where?', 'Xylem and phloem on ' + T('alternate radii') + ': in ' + T('roots'))
d.basic('What is a conjoint vascular bundle? Where?', 'Xylem and phloem on the ' + T('same radius') + ', phloem usually on the outer side: in ' + T('stems and leaves'))
d.basic('Name the three types in Figure 6.2.', '(a) ' + T('radial') + ', (b) ' + T('conjoint closed') + ', (c) ' + T('conjoint open') + ' (cambium between phloem and xylem)', **fig('fig_6_2_vascular_bundles'))

# ---------------------------------------------------------------- 6.2.1 Dicot root
d.sec('6.2.1-dicot-root')
d.basic('Which dicot root does NCERT section?', E('Sunflower'))
d.basic('What is the outermost layer of a root called?', T('Epiblema') + ' (many cells form unicellular root hairs)')
d.basic('Describe the root cortex.', 'Several layers of thin-walled ' + T('parenchyma') + ' with intercellular spaces')
d.basic('Describe the root endodermis.', 'Single layer of ' + T('barrel-shaped') + ' cells ' + X('without') + ' intercellular spaces')
d.basic('What are casparian strips?', 'Deposits of water-impermeable, waxy ' + T('suberin') + ' on the tangential and radial walls of endodermal cells')
d.basic('Why do casparian strips matter (intuition)?', 'They block water from sneaking between cells, forcing it ' + T('through the cell membranes') + '.<br>So the root controls what enters the xylem')
d.basic('What is the pericycle, and what arises from it?', 'A few layers of thick-walled parenchyma next to the endodermis.<br>' + T('Lateral roots') + ' and ' + T('vascular cambium') + ' (secondary growth) start here')
d.basic('What is conjunctive tissue?', 'Parenchyma between the ' + T('xylem and phloem') + ' in roots')
d.basic('How many xylem patches in a dicot root?', 'Usually ' + N('two to four') + ' (diarch to tetrarch)')
d.basic('What is the stele?', 'All tissues ' + T('inside the endodermis') + ': pericycle, vascular bundles and pith')
d.basic('Is the protoxylem of roots endarch or exarch? (beyond NCERT)', T('Exarch') + ': protoxylem towards the ' + T('outside') + ', metaxylem towards the centre. Stems are endarch.')
d.occlusion('Figure 6.3 (a) · T.S. of dicot root (primary)', M + 'fig_6_3a_dicot_root.webp', (1001, 939), [
    ('Root hair', P((741, 96, 163, 35))), ('Epidermis', P((747, 147, 172, 35))), ('Cortex', P((748, 283, 114, 35))),
    ('Endodermis', P((736, 481, 205, 35))), ('Pericycle', P((739, 524, 146, 35))), ('Protoxylem', P((743, 574, 190, 35))),
    ('Metaxylem', P((741, 641, 184, 35))), ('Pith', P((745, 719, 70, 35))), ('Phloem', P((744, 777, 125, 35)))], printed=True)

d.sec('6.2.2-monocot-root')
d.basic('How many xylem bundles in a monocot root?', 'Usually ' + T('more than six') + ' (' + T('polyarch') + ')')
d.basic('Pith: dicot root vs monocot root?', 'Dicot: small or inconspicuous. Monocot: ' + T('large and well developed') + '.')
d.basic('Do monocot roots show secondary growth?', X('No'))
d.basic('T.S. of monocot root: point out what differs from the dicot root.', 'Polyarch xylem, ' + T('large pith') + ', no cambium', **fig('fig_6_3b_monocot_root'))

# ---------------------------------------------------------------- 6.2.3 Dicot stem
d.sec('6.2.3-dicot-stem')
d.basic('Name the three sub-zones of the cortex in a dicot stem.', T('Hypodermis') + ', cortical layers, ' + T('endodermis'))
d.basic('What is the hypodermis of a dicot stem made of, and what does it do?', 'A few layers of ' + T('collenchyma') + ' below the epidermis; mechanical strength to the young stem')
d.basic('Why is the stem endodermis called the starch sheath?', 'Its cells are rich in ' + T('starch grains'))
d.basic('What is the pericycle like in a dicot stem?', T('Semi-lunar patches of sclerenchyma') + ' inside the endodermis, above the phloem')
d.basic('What are medullary rays?', 'Radially placed ' + T('parenchyma') + ' between the vascular bundles')
d.basic('What is characteristic about vascular bundles in a dicot stem?', 'Arranged in a ' + T('ring') + '; each ' + T('conjoint, open') + ', with ' + T('endarch') + ' protoxylem')
d.basic('T.S. of dicot stem: read the labelled figure from outside in.', 'Epidermis<br>→ hypodermis (collenchyma)<br>→ cortex (parenchyma)<br>→ endodermis<br>→ pericycle<br>→ vascular bundles in a ring (phloem, cambium, xylem)<br>→ pith', **fig('fig_6_4a_dicot_stem'))

d.sec('6.2.4-monocot-stem')
d.basic('Hypodermis of a monocot stem?', T('Sclerenchymatous'))
d.basic('Vascular bundles of a monocot stem?', T('Scattered') + ', each with a sclerenchymatous ' + T('bundle sheath') + '; conjoint and ' + T('closed'))
d.basic('Peripheral vs central bundles in a monocot stem?', 'Peripheral bundles are ' + T('smaller') + ' than central ones')
d.basic('Which tissue is absent in monocot stem bundles, and what is present instead?', X('Phloem parenchyma') + ' is absent; ' + T('water-containing cavities') + ' are present')
d.basic('A T.S. shows conjoint, scattered bundles with sclerenchymatous sheaths and no phloem parenchyma. What is it?', 'A ' + T('monocot stem'), **fig('fig_6_4b_monocot_stem'))
table_card(d, 'Dicot vs monocot stem', 'Dicot stem feature (monocot in brackets)?', [
    ('Hypodermis', 'Collenchyma (sclerenchyma)', False), ('Vascular bundles', 'Ring (scattered)', False),
    ('Bundle type', 'Conjoint, open (conjoint, closed)', False), ('Ground tissue', 'Cortex, pith, medullary rays (large undifferentiated)', False)],
    term='Dicot vs monocot stem')

# ---------------------------------------------------------------- 6.2.5-6 Leaves
d.sec('6.2.5-dicot-leaf')
d.basic('What are the three main parts in a section of a dorsiventral leaf?', T('Epidermis') + ', ' + T('mesophyll') + ', ' + T('vascular system'))
d.basic('Adaxial vs abaxial epidermis?', T('Adaxial') + ': upper surface. ' + T('Abaxial') + ': lower surface.')
d.basic('Which leaf surface has more stomata in a dicot leaf?', 'The ' + T('abaxial') + ' (lower); the adaxial may even lack them')
d.basic('Palisade vs spongy parenchyma?', T('Palisade') + ': adaxial, elongated cells, vertical and parallel<br>' + T('Spongy') + ': below it, oval or round, loosely arranged with large air spaces')
d.basic('What surrounds the vascular bundles of a leaf?', 'A layer of thick-walled ' + T('bundle sheath') + ' cells')
d.basic('In a leaf vascular bundle, which side is xylem on?', T('Adaxial') + ' (upper) side, phloem towards the abaxial side', **fig('fig_6_5a_dicot_leaf'))

d.sec('6.2.6-monocot-leaf')
d.basic('How does an isobilateral leaf differ from a dorsiventral one?', 'Stomata on ' + T('both') + ' surfaces; mesophyll ' + X('not differentiated') + ' into palisade and spongy')
d.basic('What are bulliform cells? Where?', 'Large, empty, colourless ' + T('adaxial') + ' epidermal cells along the veins, in ' + E('grasses'))
d.basic('What do bulliform cells do?', 'Turgid: leaf surface exposed. Flaccid in water stress: leaves ' + T('curl inwards') + ' to reduce water loss.')
d.basic('Why are the vascular bundles of a monocot leaf nearly the same size?', 'Its ' + T('parallel venation') + ' (except main veins)', **fig('fig_6_5b_monocot_leaf'))
table_card(d, 'Dicot vs monocot leaf', 'Dicot (dorsiventral) feature (monocot in brackets)?', [
    ('Stomata', 'Mostly lower surface (both surfaces)', False), ('Mesophyll', 'Palisade + spongy (undifferentiated)', False),
    ('Bulliform cells', 'Absent (present in grasses)', False), ('Bundles', 'Vary in size (near similar)', False)], term='Dicot vs monocot leaf')

d.sec('summary')
table_card(d, 'Dicot vs monocot root', 'Dicot root feature (monocot in brackets)?', [
    ('Xylem bundles', '2–4 (more than 6, polyarch)', False), ('Pith', 'Small (large)', False), ('Secondary growth', 'Occurs (absent)', False)],
    term='Dicot vs monocot root')
d.basic('Name the three kinds of meristem.', T('Apical') + ', ' + T('lateral') + ', ' + T('intercalary'))

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
