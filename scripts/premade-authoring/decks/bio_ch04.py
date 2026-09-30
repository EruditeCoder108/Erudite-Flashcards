import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch04-animal-kingdom')
d = Deck('Chapter 4: Animal Kingdom', 'Class 11', ['class-11', 'biology', 'ch-4'])
d.description = 'Basis of classification, every non-chordate phylum, chordates and the vertebrate classes'
M = 'media/'
P = lambda b: pad(b, 6)
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- 4.1 Basis of classification
d.sec('4.1-basis')
d.basic('About how many animal species have been described?', 'Over a ' + N('million'))
d.basic('Name the fundamental features used as the basis of animal classification.', 'Arrangement of cells<br>Body symmetry<br>Nature of coelom<br>Patterns of digestive, circulatory or reproductive systems')

d.sec('4.1.1-levels-of-organisation')
d.cloze('Levels of organisation: sponges show {{c1::cellular}} level, coelenterates {{c2::tissue}} level, Platyhelminthes {{c3::organ}} level, and annelids to chordates {{c4::organ system}} level.')
d.basic('What is the cellular level of organisation?', 'Cells arranged as ' + T('loose cell aggregates') + ', with some division of labour, e.g. ' + E('sponges'))
d.basic('What is the tissue level of organisation?', 'Cells performing the same function are arranged into ' + T('tissues') + ', e.g. ' + E('coelenterates'))
d.basic('Why is the digestive system of Platyhelminthes called incomplete?', 'It has a ' + X('single opening') + ' that serves as both mouth and anus')
d.basic('What is a complete digestive system?', 'One with ' + N('two') + ' openings: ' + T('mouth') + ' and ' + T('anus'))
d.basic('What is an open circulatory system?', 'Blood is pumped out of the heart and cells and tissues are ' + T('directly bathed') + ' in it')
d.basic('What is a closed circulatory system?', 'Blood circulates through a series of ' + T('vessels') + ' (arteries, veins, capillaries)')

d.sec('4.1.2-symmetry')
d.basic('What is an asymmetrical animal? Example?', 'No plane through the centre divides it into equal halves, e.g. most ' + E('sponges'))
d.basic('What is radial symmetry? Which groups show it?', 'Any plane through the central axis gives two identical halves: ' + E('coelenterates, ctenophores, echinoderms'), **img('fig_4_1a_radial'))
d.basic('What is bilateral symmetry? Examples?', 'Identical left and right halves in ' + T('only one') + ' plane: ' + E('annelids, arthropods'), **img('fig_4_1b_bilateral'))
d.basic('Echinoderms: radial or bilateral?', 'Adults ' + T('radial') + ', larvae ' + T('bilateral'))

d.sec('4.1.3-germ-layers')
d.basic('What are diploblastic animals? Example?', 'Cells in ' + N('two') + ' embryonic layers, external ' + T('ectoderm') + ' and internal ' + T('endoderm') + ', e.g. ' + E('coelenterates'))
d.basic('What lies between ectoderm and endoderm in diploblastic animals?', 'An undifferentiated layer, the ' + T('mesoglea'))
d.basic('What are triploblastic animals? Which phyla?', 'The embryo has a third layer, ' + T('mesoderm') + ', between ectoderm and endoderm: ' + E('Platyhelminthes to chordates'))
d.occlusion('Figure 4.2 · Germinal layers: (a) diploblastic, (b) triploblastic', M + 'fig_4_2_germ_layers.webp', (1001, 654), [
    ('Ectoderm', P((394, 40, 184, 39)), True), ('Mesoglea', P((79, 64, 173, 39)), True), ('Endoderm', P((392, 124, 198, 39)), True),
    ('Mesoderm', P((447, 549, 197, 39)), True), ('Diploblastic', P((251, 581, 46, 39))), ('Triploblastic', P((745, 573, 47, 39)))])

d.sec('4.1.4-coelom')
d.basic('What is a coelom?', 'A body cavity between body wall and gut wall, ' + T('lined by mesoderm'))
d.basic('Name the coelomate phyla.', 'Annelids, molluscs, arthropods, echinoderms, hemichordates, chordates')
d.basic('What is a pseudocoelom? Example?', 'A body cavity ' + X('not lined') + ' by mesoderm; mesoderm lies as scattered pouches between ectoderm and endoderm.<br>e.g. ' + E('Aschelminthes'))
d.basic('Which animals are acoelomates?', 'Those with no body cavity, e.g. ' + E('Platyhelminthes'))
d.occlusion('Figure 4.3 · Sectional view: name each body plan', M + 'fig_4_3_coelom.webp', (965, 1001), [
    ('Coelom', [80, 30, 155, 55], True), ('Pseudocoelom', [352, 36, 282, 55], True),
    ('Coelomate', [205, 512, 76, 52]), ('Pseudocoelomate', [705, 516, 76, 52]), ('Acoelomate', [448, 942, 76, 54])])

d.sec('4.1.5-segmentation-notochord')
d.basic('What is metameric segmentation? Example?', 'Body divided externally and internally into segments with serial repetition of some organs, e.g. ' + E('earthworm') + '<br>The phenomenon is ' + T('metamerism'))
d.basic('In which phylum is segmentation first seen?', T('Annelida'))
d.basic('What is the notochord?', 'A ' + T('mesodermally') + ' derived rod-like structure formed on the ' + T('dorsal') + ' side during embryonic development')
d.basic('Which phyla are non-chordates?', E('Porifera to Echinodermata') + ' (and Hemichordata)')
d.basic('Figure 4.4: broad classification of Kingdom Animalia. Trace the path to Annelida.', 'Organ system level → ' + T('bilateral') + ' → ' + T('true coelom') + ' (coelomate) → Annelida',
        definitionImage=M + 'fig_4_4_classification.webp')

# ---------------------------------------------------------------- Non-chordate phyla
d.sec('4.2.1-porifera')
d.basic('Which phylum is this? Name (a), (b), (c).', T('Porifera') + ': (a) ' + EI('Sycon') + ', (b) ' + EI('Euspongia') + ', (c) ' + EI('Spongilla'), **img('fig_4_5_porifera'))
d.basic('What is the common name of Porifera? Habitat and symmetry?', T('Sponges') + '; generally marine, mostly asymmetrical')
d.cloze('In sponges, water enters through minute pores, {{c1::ostia}}, into a central cavity, the {{c2::spongocoel}}, and goes out through the {{c3::osculum}}.')
d.basic('What does the canal system of sponges help with?', 'Food gathering, respiratory exchange, removal of waste')
d.basic('Which cells line the spongocoel and canals?', T('Choanocytes') + ' (collar cells)')
d.basic('Is digestion in sponges intracellular or extracellular?', T('Intracellular'))
d.basic('What is the skeleton of sponges made of?', T('Spicules') + ' or ' + T('spongin fibres'))
d.basic('Are sponges unisexual or hermaphrodite? Fertilisation and development?', T('Hermaphrodite') + '; fertilisation ' + T('internal') + '; development ' + T('indirect') + ' (larval stage)')
d.basic('Give the common names: <i>Sycon</i>, <i>Spongilla</i>, <i>Euspongia</i>.', EI('Sycon') + ' (Scypha), ' + EI('Spongilla') + ' (fresh water sponge), ' + EI('Euspongia') + ' (bath sponge)')

d.sec('4.2.2-coelenterata')
d.basic('Which phylum is this? Name (a) and (b) and their body forms.', T('Coelenterata') + ': (a) ' + EI('Aurelia') + ' (medusa), (b) ' + EI('Adamsia') + ' (polyp)', **img('fig_4_6_coelenterata'))
d.basic("From what is the name 'Cnidaria' derived?", 'The ' + T('cnidoblasts') + ' (cnidocytes), which contain stinging capsules (' + T('nematocysts') + ')')
d.basic('What are cnidoblasts used for?', 'Anchorage, defence, capture of prey', **img('fig_4_7_cnidoblast'))
d.basic('Level of organisation and germ layers of cnidarians?', T('Tissue') + ' level; ' + T('diploblastic'))
d.basic('Where is the mouth of a cnidarian?', 'On the ' + T('hypostome') + ', opening into a central gastro-vascular cavity')
d.basic('Is digestion in cnidarians intracellular or extracellular?', T('Both'))
d.basic('What is the skeleton of corals made of?', T('Calcium carbonate'))
d.basic('Compare the polyp and medusa forms.', T('Polyp') + ': sessile, cylindrical (' + EI('Hydra') + ', ' + EI('Adamsia') + '). ' + T('Medusa') + ': umbrella-shaped, free-swimming (' + EI('Aurelia') + ').')
d.basic('What is metagenesis? Example?', 'Alternation of generations: polyps produce medusae ' + T('asexually') + ', medusae form polyps ' + T('sexually') + ', e.g. ' + EI('Obelia'))
d.cloze('Cnidarians: {{c1::<i>Physalia</i>}} is the Portuguese man-of-war, {{c2::<i>Adamsia</i>}} the sea anemone, {{c3::<i>Pennatula</i>}} the sea-pen, {{c4::<i>Gorgonia</i>}} the sea-fan and {{c5::<i>Meandrina</i>}} the brain coral.')

d.sec('4.2.3-ctenophora')
d.basic('Which phylum is this animal from? Name it.', T('Ctenophora') + ': ' + EI('Pleurobrachia'), **img('fig_4_8_ctenophora'))
d.basic('Common names of ctenophores?', T('Sea walnuts') + ' or ' + T('comb jellies'))
d.basic('What helps ctenophores move?', N('Eight') + ' external rows of ciliated ' + T('comb plates'))
d.basic('Which property is well marked in ctenophores?', T('Bioluminescence') + ': emitting light')
d.basic('Ctenophores: sexes, reproduction, fertilisation?', 'Sexes not separate; ' + T('only sexual') + ' reproduction; fertilisation ' + T('external') + ', indirect development')
d.basic('Name two ctenophores.', EI('Pleurobrachia') + ', ' + EI('Ctenoplana'))

d.sec('4.2.4-platyhelminthes')
d.basic('Which phylum is this? Name (a) and (b).', T('Platyhelminthes') + ': (a) tapeworm (' + EI('Taenia') + '), (b) liver fluke (' + EI('Fasciola') + ')', **img('fig_4_9_platyhelminthes'))
d.basic('Why are Platyhelminthes called flatworms?', 'Their body is ' + T('dorso-ventrally flattened'))
d.basic('Symmetry, germ layers, coelom and level of Platyhelminthes?', 'Bilateral, triploblastic, ' + T('acoelomate') + ', organ level')
d.basic('Which features of parasitic flatworms suit parasitism?', T('Hooks and suckers') + '; some absorb nutrients directly through the body surface')
d.basic('Which cells help flatworms in osmoregulation and excretion?', T('Flame cells'))
d.basic('Which flatworm has high regeneration capacity?', EI('Planaria'))

d.sec('4.2.5-aschelminthes')
d.basic('Which phylum is this? Which is male and female?', T('Aschelminthes') + ' (roundworm). Females are often ' + T('longer') + ' than males.', **img('fig_4_10_roundworm'))
d.basic('Why are aschelminthes called roundworms?', 'Body is ' + T('circular in cross-section'))
d.basic('Coelom of roundworms?', T('Pseudocoelomate'))
d.basic('Describe the alimentary canal of roundworms.', T('Complete') + ', with a well-developed muscular ' + T('pharynx'))
d.basic('How are body wastes removed in roundworms?', 'An ' + T('excretory tube') + ' removes them through the excretory pore')
d.basic('Are roundworms monoecious or dioecious?', T('Dioecious') + ': sexes separate')
d.cloze('Aschelminthes: {{c1::<i>Ascaris</i>}} (roundworm), {{c2::<i>Wuchereria</i>}} (filaria worm), {{c3::<i>Ancylostoma</i>}} (hookworm).')

d.sec('4.2.6-annelida')
d.basic('Which phylum is this? Name (a) and (b).', T('Annelida') + ': (a) ' + EI('Nereis') + ', (b) ' + EI('Hirudinaria'), **img('fig_4_11_annelida'))
d.basic("What does 'Annelida' mean?", 'Latin ' + T('annulus') + ': little ring (body marked into segments, metameres)')
d.basic('Annelids: coelom and segmentation?', T('Coelomate') + ', ' + T('metamerically segmented'))
d.basic('What are parapodia? In which annelid?', 'Lateral appendages for ' + T('swimming') + ', in aquatic ' + EI('Nereis'))
d.basic('Circulatory system of annelids?', T('Closed'))
d.basic('Which organs help annelids in osmoregulation and excretion?', T('Nephridia'))
d.basic('Describe the neural system of annelids.', 'Paired ' + T('ganglia') + ' connected by lateral nerves to a ' + T('double ventral nerve cord'))
d.basic('Which annelid is dioecious, and which are monoecious?', EI('Nereis') + ' is dioecious; ' + E('earthworms and leeches') + ' are monoecious')
d.cloze('Annelida: {{c1::<i>Pheretima</i>}} is the earthworm and {{c2::<i>Hirudinaria</i>}} the blood sucking leech.')

d.sec('4.2.7-arthropoda')
d.basic('Which phylum is this? Name (a)–(d).', T('Arthropoda') + ': (a) locust, (b) butterfly, (c) scorpion, (d) prawn', **img('fig_4_12_arthropoda'))
d.basic('Which is the largest phylum of Animalia?', T('Arthropoda') + ': over ' + N('two-thirds') + ' of all named species')
d.basic('What covers the body of arthropods?', 'A ' + T('chitinous exoskeleton'))
d.basic("What does 'Arthropoda' mean?", T('Jointed appendages') + ' (arthros: joint, poda: appendages)')
d.basic('Name the respiratory organs of arthropods.', 'Gills, book gills, book lungs, tracheal system')
d.basic('Circulatory system of arthropods?', T('Open'))
d.basic('What are the excretory organs of arthropods?', T('Malpighian tubules'))
d.basic('What are statocysts?', T('Balancing') + ' organs (sensory organs of arthropods)')
d.cloze('Useful insects: {{c1::<i>Apis</i>}} (honey bee), {{c2::<i>Bombyx</i>}} (silkworm), {{c3::<i>Laccifer</i>}} (lac insect).')
d.basic('Name three mosquito vectors.', EI('Anopheles') + ', ' + EI('Culex') + ', ' + EI('Aedes'))
d.basic('Which arthropod is a gregarious pest?', EI('Locusta') + ' (locust)')
d.basic('Which arthropod is a living fossil?', EI('Limulus') + ' (king crab)')

d.sec('4.2.8-mollusca')
d.basic('Which phylum is this? Name (a) and (b).', T('Mollusca') + ': (a) ' + EI('Pila') + ', (b) ' + EI('Octopus'), **img('fig_4_13_mollusca'))
d.basic('Which is the second largest animal phylum?', T('Mollusca'))
d.basic('Body plan of a mollusc?', 'Covered by a ' + T('calcareous shell') + '; unsegmented, with a distinct head, muscular foot and visceral hump')
d.basic('What is the mantle, and the mantle cavity?', T('Mantle') + ': soft spongy skin over the visceral hump. The space between hump and mantle is the ' + T('mantle cavity') + ', with feather-like gills.')
d.basic('What do the gills of molluscs do?', T('Respiratory') + ' and ' + T('excretory') + ' functions')
d.basic('What is the radula?', 'A ' + T('file-like rasping organ') + ' in the mouth, for feeding')
d.cloze('Molluscs: {{c1::<i>Pinctada</i>}} pearl oyster, {{c2::<i>Sepia</i>}} cuttlefish, {{c3::<i>Loligo</i>}} squid, {{c4::<i>Octopus</i>}} devil fish, {{c5::<i>Aplysia</i>}} sea-hare, {{c6::<i>Dentalium</i>}} tusk shell, {{c7::<i>Chaetopleura</i>}} chiton.')
d.basic('What is <i>Pila</i>?', E('Apple snail'))

d.sec('4.2.9-echinodermata')
d.basic('Which phylum is this? Name (a) and (b).', T('Echinodermata') + ': (a) ' + EI('Asterias') + ', (b) ' + EI('Ophiura'), **img('fig_4_14_echinodermata'))
d.basic("Why the name 'Echinodermata'?", 'Spiny bodied: an endoskeleton of ' + T('calcareous ossicles'))
d.basic('Habitat of echinoderms?', 'All ' + T('marine'))
d.basic('Where are the mouth and anus of echinoderms?', 'Mouth on the lower ' + T('(ventral)') + ' side, anus on the upper ' + T('(dorsal)') + ' side')
d.basic('What is the most distinctive feature of echinoderms?', 'The ' + T('water vascular system') + ': locomotion, capture and transport of food, respiration')
d.basic('Which system is absent in echinoderms?', T('Excretory') + ' system')
d.cloze('Echinoderms: {{c1::<i>Asterias</i>}} star fish, {{c2::<i>Echinus</i>}} sea urchin, {{c3::<i>Antedon</i>}} sea lily, {{c4::<i>Cucumaria</i>}} sea cucumber, {{c5::<i>Ophiura</i>}} brittle star.')

d.sec('4.2.10-hemichordata')
d.basic('Where is Hemichordata placed now?', 'A separate phylum under ' + T('non-chordata') + ' (earlier a sub-phylum of Chordata)')
d.basic('What is the stomochord?', 'A rudimentary structure in the ' + T('collar') + ' region, similar to the notochord')
d.occlusion('Figure 4.15 · <i>Balanoglossus</i>', M + 'fig_4_15_balanoglossus.webp', (418, 1000), [
    ('Proboscis', P((171, 135, 191, 40))), ('Collar', P((188, 535, 122, 40))), ('Trunk', P((179, 815, 125, 40)))], printed=True)
d.basic('Circulatory system and excretory organ of hemichordates?', 'Circulation ' + T('open') + '; excretory organ: ' + T('proboscis gland'))
d.basic('Name two hemichordates.', EI('Balanoglossus') + ', ' + EI('Saccoglossus'))

d.sec('table-4.2')
table_card(d, 'Table 4.2 · Coelom', 'Coelom in each?', [
    ('Porifera to Platyhelminthes', 'Absent', True), ('Aschelminthes', 'Pseudocoelomate', False), ('Annelida onwards', 'Coelomate', False)], term='Table 4.2: coelom')
table_card(d, 'Table 4.2 · Circulatory system', 'Present or absent?', [
    ('Porifera to Aschelminthes', 'Absent', True), ('Annelida to Chordata', 'Present', False)], term='Table 4.2: circulatory system')
table_card(d, 'Table 4.2 · Respiratory system', 'Present or absent?', [
    ('Porifera to Annelida', 'Absent', True), ('Arthropoda to Chordata', 'Present', False)], term='Table 4.2: respiratory system')
table_card(d, 'Table 4.2 · Segmentation', 'Which phyla are segmented?', [
    ('Annelida', 'Present', False), ('Arthropoda', 'Present', False), ('Chordata', 'Present', False), ('All others', 'Absent', True)], term='Table 4.2: segmentation')
d.basic('Match: operculum, parapodia, comb plates, radula, choanocytes.', 'Operculum: ' + T('Osteichthyes') + '<br>Parapodia: ' + T('Annelida') + '<br>Comb plates: ' + T('Ctenophora') + '<br>Radula: ' + T('Mollusca') + '<br>Choanocytes: ' + T('Porifera'))

# ---------------------------------------------------------------- 4.2.11 Chordata
d.sec('4.2.11-chordata')
d.occlusion('Figure 4.16 · Chordate characteristics', M + 'fig_4_16_chordata.webp', (1001, 474), [
    ('Nerve cord', P((132, 33, 208, 40))), ('Notochord', P((401, 33, 202, 40))),
    ('Post-anal part', P((690, 344, 278, 40))), ('Gill slits', P((364, 408, 162, 40)))], printed=True)
d.basic('Three fundamental characters of chordates?', 'A ' + T('notochord') + ', a ' + T('dorsal hollow nerve cord') + ', paired ' + T('pharyngeal gill slits'))
d.basic('Besides the three basic features, what else do chordates possess?', 'A ' + T('post anal tail') + ' and a ' + T('closed') + ' circulatory system')
table_card(d, 'Table 4.1 · Chordates vs non-chordates', 'Chordate feature (non-chordates: the opposite)?', [
    ('Notochord', 'Present (absent in non-chordates)', False), ('Central nervous system', 'Dorsal, hollow, single (ventral, solid, double)', False),
    ('Pharynx', 'Perforated by gill slits (absent)', False), ('Heart', 'Ventral (dorsal, if present)', False), ('Post-anal tail', 'Present (absent)', False)],
    term='Table 4.1: chordates vs non-chordates')
d.basic('Name the three subphyla of Chordata.', T('Urochordata') + ' (Tunicata), ' + T('Cephalochordata') + ', ' + T('Vertebrata'))
d.basic('What are protochordates?', T('Urochordata') + ' and ' + T('Cephalochordata') + ': exclusively marine')
d.basic('Where is the notochord in Urochordata and in Cephalochordata?', 'Urochordata: only in the ' + T('larval tail') + '. Cephalochordata: head to tail, ' + T('throughout life') + '.')
d.basic('Name three urochordates and one cephalochordate.', 'Urochordata: ' + EI('Ascidia, Salpa, Doliolum') + '. Cephalochordata: ' + EI('Branchiostoma') + ' (Amphioxus / lancelet).')
d.basic('Which protochordate is this?', EI('Ascidia') + ' (Urochordata)', **img('fig_4_17_ascidia'))
d.basic('What replaces the notochord in adult vertebrates?', 'A ' + T('cartilaginous or bony vertebral column'))
d.basic('Justify: all vertebrates are chordates but all chordates are not vertebrates.', 'Vertebrates have a notochord only in the ' + T('embryo') + ', replaced by a vertebral column.<br>Protochordates keep the notochord and have ' + X('no vertebral column'))
d.basic('Features of vertebrates besides the basic chordate ones?', 'Ventral muscular heart (2, 3 or 4 chambers), ' + T('kidneys') + ', paired appendages (fins or limbs)')
d.occlusion('Classification of subphylum Vertebrata', M + 'vertebrata_chart.webp', (1001, 614), [
    ('Agnatha (lacks jaw)', P((114, 178, 139, 59))), ('Gnathostomata (bears jaw)', P((558, 173, 205, 59))),
    ('Pisces (bear fins)', P((395, 326, 132, 59))), ('Tetrapoda (bear limbs)', P((782, 322, 155, 59))),
    ('Cyclostomata', P((110, 440, 178, 27))), ('Chondrichthyes', P((414, 445, 210, 27))), ('Osteichthyes', P((414, 476, 171, 27)))],
    printed=True)

d.sec('4.2.11.1-cyclostomata')
d.basic('Which vertebrate is this, and what is special about its mouth?', EI('Petromyzon') + ' (lamprey): sucking, circular mouth ' + X('without jaws'), **img('fig_4_18_petromyzon'))
d.basic('How do living cyclostomes live?', 'As ' + T('ectoparasites') + ' on some fishes')
d.basic('How many gill slits do cyclostomes have?', N('6–15 pairs'))
d.basic('Do cyclostomes have scales and paired fins?', X('No') + '. Cranium and vertebral column are ' + T('cartilaginous') + '.')
d.basic('Describe the spawning of cyclostomes.', 'Marine, but migrate to ' + T('fresh water') + ' to spawn; they die within a few days; larvae return to the ocean after metamorphosis')
d.basic('Name two cyclostomes.', EI('Petromyzon') + ' (lamprey), ' + EI('Myxine') + ' (hagfish)')

d.sec('4.2.11.2-chondrichthyes')
d.basic('Which class are these fishes? Name (a) and (b).', T('Chondrichthyes') + ': (a) ' + EI('Scoliodon') + ', (b) ' + EI('Pristis'), **img('fig_4_19_cartilaginous'))
d.basic('Endoskeleton and mouth position of Chondrichthyes?', T('Cartilaginous') + ' endoskeleton; mouth ' + T('ventral'))
d.basic('Gill slits of cartilaginous fishes?', 'Separate, ' + X('without operculum') + ' (gill cover)')
d.basic('What are placoid scales, and what are the teeth of sharks?', 'Minute scales in the tough skin. Teeth are ' + T('modified placoid scales') + ', backwardly directed.')
d.basic('Why must cartilaginous fishes swim constantly?', 'No ' + X('air bladder') + ', so they would sink')
d.basic('Heart of fishes?', N('Two') + '-chambered: one auricle, one ventricle')
d.basic('What does poikilothermous mean?', T('Cold-blooded') + ': unable to regulate body temperature')
d.basic('What do the pelvic fins of male Chondrichthyes bear?', T('Claspers'))
d.cloze('Chondrichthyes: {{c1::<i>Torpedo</i>}} has electric organs and {{c2::<i>Trygon</i>}} (sting ray) a poison sting.')
d.cloze('{{c1::<i>Scoliodon</i>}} is the dog fish, {{c2::<i>Pristis</i>}} the saw fish, and {{c3::<i>Carcharodon</i>}} the great white shark.')

d.sec('4.2.11.3-osteichthyes')
d.basic('Which class are these? Name (a) and (b).', T('Osteichthyes') + ': (a) ' + EI('Hippocampus') + ' (sea horse), (b) ' + EI('Catla'), **img('fig_4_20_bony_fishes'))
d.basic('How many gills do bony fishes have, and what covers them?', N('Four') + ' pairs, covered by an ' + T('operculum') + ' on each side')
d.basic('Scales of bony fishes?', T('Cycloid') + ' or ' + T('ctenoid'))
d.basic('What does the air bladder of bony fishes do?', 'Regulates ' + T('buoyancy'))
d.basic('Fertilisation and development in bony fishes?', 'Fertilisation usually ' + T('external') + '; mostly oviparous; development ' + T('direct'))
table_card(d, 'Osteichthyes', 'Give the NCERT examples.', [
    ('Marine', '<i>Exocoetus</i> (flying fish), <i>Hippocampus</i> (sea horse)', False),
    ('Freshwater', '<i>Labeo</i> (rohu), <i>Catla</i> (katla), <i>Clarias</i> (magur)', False),
    ('Aquarium', '<i>Betta</i> (fighting fish), <i>Pterophyllum</i> (angel fish)', False)], term='Bony fishes: examples')

d.sec('4.2.11.4-amphibia')
d.basic('Which class are these? Name (a) and (b).', T('Amphibia') + ': (a) ' + EI('Salamandra') + ', (b) ' + EI('Rana'), **img('fig_4_21_amphibia'))
d.basic("What does 'Amphibia' mean?", 'Gr. amphi: dual, bios: life. They live in ' + T('water and on land') + '.')
d.basic('Skin, eyes and ear of amphibians?', 'Moist skin ' + X('without scales') + '; eyes with ' + T('eyelids') + '; a ' + T('tympanum') + ' represents the ear')
d.basic('What is the cloaca?', 'A common chamber into which the alimentary canal, urinary and reproductive tracts open')
d.basic('Respiration in amphibians?', 'By gills, lungs and through ' + T('skin'))
d.basic('Heart of amphibians?', N('Three') + '-chambered: two auricles, one ventricle')
d.basic('Fertilisation and development of amphibians?', 'Fertilisation ' + T('external') + '; oviparous; development ' + T('indirect'))
d.cloze('Amphibia: {{c1::<i>Bufo</i>}} toad, {{c2::<i>Rana</i>}} frog, {{c3::<i>Hyla</i>}} tree frog, {{c4::<i>Salamandra</i>}} salamander, {{c5::<i>Ichthyophis</i>}} limbless amphibian.')

d.sec('4.2.11.5-reptilia')
d.basic('Which class are these? Name (a)–(d).', T('Reptilia') + ': (a) ' + EI('Chameleon') + ', (b) ' + EI('Crocodilus') + ', (c) ' + EI('Chelone') + ', (d) ' + EI('Naja'), **img('fig_4_22_reptiles'))
d.basic("What does 'Reptilia' refer to?", 'Their ' + T('creeping or crawling') + ' locomotion (Latin repere / reptum)')
d.basic('Skin of reptiles?', 'Dry, ' + T('cornified') + ' skin with epidermal scales or scutes')
d.basic('Do reptiles have external ear openings?', X('No') + '. A tympanum represents the ear.')
d.basic('Heart of reptiles?', 'Usually ' + N('three') + '-chambered, but ' + N('four') + '-chambered in ' + X('crocodiles'))
d.basic('Which reptiles shed their scales as skin cast?', E('Snakes and lizards'))
d.cloze('Reptiles: {{c1::<i>Chelone</i>}} turtle, {{c2::<i>Testudo</i>}} tortoise, {{c3::<i>Calotes</i>}} garden lizard, {{c4::<i>Hemidactylus</i>}} wall lizard, {{c5::<i>Chameleon</i>}} tree lizard.')
d.cloze('Poisonous snakes: {{c1::<i>Naja</i>}} cobra, {{c2::<i>Bangarus</i>}} krait, {{c3::<i>Vipera</i>}} viper.')

d.sec('4.2.11.6-aves')
d.basic('Which class are these? Name (a)–(d).', T('Aves') + ': (a) ' + EI('Neophron') + ', (b) ' + EI('Struthio') + ', (c) ' + EI('Psittacula') + ', (d) ' + EI('Pavo'), **img('fig_4_23_birds'))
d.basic('Characteristic features of birds?', T('Feathers') + ', a beak, forelimbs modified into ' + T('wings'))
d.basic('Which gland is present in the skin of birds?', 'Only the ' + T('oil gland') + ' at the base of the tail')
d.basic('What are pneumatic bones?', 'Hollow long bones with ' + T('air cavities') + ' (birds)')
d.basic('What extra chambers does the digestive tract of birds have?', T('Crop') + ' and ' + T('gizzard'))
d.basic('What supplements respiration in birds?', T('Air sacs') + ' connected to the lungs')
d.basic('What does homoiothermous mean?', T('Warm-blooded') + ': able to maintain a constant body temperature')
d.basic('Which modifications help birds fly?', 'Feathers, wings, ' + T('pneumatic bones') + ', air sacs, four-chambered heart, warm blood')
d.cloze('Birds: {{c1::<i>Corvus</i>}} crow, {{c2::<i>Columba</i>}} pigeon, {{c3::<i>Psittacula</i>}} parrot, {{c4::<i>Struthio</i>}} ostrich, {{c5::<i>Pavo</i>}} peacock, {{c6::<i>Aptenodytes</i>}} penguin, {{c7::<i>Neophron</i>}} vulture.')

d.sec('4.2.11.7-mammalia')
d.basic('Which class are these? Name (a)–(d).', T('Mammalia') + ': (a) ' + EI('Ornithorhynchus') + ', (b) ' + EI('Macropus') + ', (c) ' + EI('Pteropus') + ', (d) ' + EI('Balaenoptera'), **img('fig_4_24_mammals'))
d.basic('What is the most unique mammalian characteristic?', T('Mammary glands') + ' (milk-producing)')
d.basic('Which features of the skin and ear are unique to mammals?', 'Skin with ' + T('hair') + '; external ears (' + T('pinnae') + ')')
d.basic('Which mammal is oviparous?', EI('Ornithorhynchus') + ' (platypus)')
d.cloze('Mammals: {{c1::<i>Macropus</i>}} kangaroo, {{c2::<i>Pteropus</i>}} flying fox, {{c3::<i>Balaenoptera</i>}} blue whale, {{c4::<i>Delphinus</i>}} common dolphin, {{c5::<i>Macaca</i>}} monkey.')

d.sec('vertebrate-classes')
table_card(d, 'Vertebrates', 'Chambers of the heart?', [
    ('Fishes', '2', False), ('Amphibians', '3', False), ('Reptiles', '3 (4 in crocodiles)', False), ('Birds, mammals', '4', False)], term='Heart chambers in vertebrates')
table_card(d, 'Vertebrates', 'Cold- or warm-blooded?', [
    ('Fishes, amphibians, reptiles', 'Poikilothermous (cold)', False), ('Birds, mammals', 'Homoiothermous (warm)', False)], term='Body temperature in vertebrates')
table_card(d, 'Vertebrates', 'Fertilisation?', [
    ('Cartilaginous fishes', 'Internal', False), ('Bony fishes', 'Usually external', False), ('Amphibians', 'External', False),
    ('Reptiles, birds, mammals', 'Internal', False)], term='Fertilisation in vertebrates')

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
