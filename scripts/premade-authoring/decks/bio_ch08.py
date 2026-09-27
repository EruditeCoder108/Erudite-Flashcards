import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch08-cell-the-unit-of-life')
d = Deck('Chapter 8: Cell: The Unit of Life', 'Class 11', ['class-11', 'biology', 'ch-8'])
d.description = 'Cell theory, prokaryotic cells, and every eukaryotic organelle with its NCERT diagram'
M = 'media/'
P = lambda b: pad(b, 6)
img = lambda name: {'termImage': M + name + '.webp'}
fig = lambda name: {'definitionImage': M + name + '.webp'}

d.sec('ramachandran')
d.basic('Which Indian scientist discovered the triple helical structure of collagen (1954)?', T('G.N. Ramachandran'))
d.basic('What is the Ramachandran plot used for?', 'Analysing the allowed ' + T('conformations of proteins'))

# ---------------------------------------------------------------- 8.1-8.2
d.sec('8.1-8.2-cell-theory')
d.basic('Why is the cell the fundamental unit of life?', 'Anything less than a complete cell ' + X('cannot') + ' live independently')
d.basic('Who first saw and described a live cell?', T('Antonie von Leeuwenhoek'))
d.basic('Who discovered the nucleus?', T('Robert Brown') + ' (1831)')
d.basic('Which is NOT correct: (a) Robert Brown discovered the cell; (b) Schleiden and Schwann formulated the cell theory; (c) Virchow: cells from pre-existing cells.', X('(a)') + ': Robert Brown discovered the ' + T('nucleus') + ', not the cell (Robert Hooke named cells)')
d.basic('What did Matthias Schleiden (1838) observe?', 'All ' + T('plants') + ' are composed of different kinds of cells forming tissues')
d.basic('What did Theodore Schwann (1839) conclude?', 'Animal cells have a thin outer layer (' + T('plasma membrane') + '); the ' + T('cell wall') + ' is unique to plant cells; bodies of animals and plants are cells and products of cells')
d.basic("What did Rudolf Virchow (1855) add to the cell theory?", 'Cells divide and new cells come from ' + T('pre-existing cells') + ': ' + I('Omnis cellula-e cellula'))
d.basic('State the modern cell theory.', '(i) All living organisms are composed of cells and products of cells. (ii) All cells arise from ' + T('pre-existing cells') + '.')
d.basic('Why was Schleiden and Schwann\'s cell theory incomplete?', 'It did not explain ' + X('how new cells form'))

# ---------------------------------------------------------------- 8.3 Overview
d.sec('8.3-overview')
d.basic('Eukaryotic vs prokaryotic cell?', T('Eukaryotic') + ': membrane-bound nucleus. ' + T('Prokaryotic') + ': ' + X('no') + ' membrane-bound nucleus.')
d.basic('What is the cytoplasm?', 'The semi-fluid matrix filling the cell: the main arena of cellular activities')
d.basic('Which organelle is found in all cells, prokaryotic and eukaryotic?', T('Ribosomes') + ' (non-membrane bound)')
d.basic('Besides the cytoplasm, where are ribosomes found in a cell?', 'Inside ' + T('chloroplasts') + ' and ' + T('mitochondria') + ', and on ' + T('rough ER'))
d.basic('Which non-membrane bound organelle in animal cells helps in cell division?', T('Centrosome'))
d.basic('Smallest cells, and their size (NCERT)?', T('Mycoplasmas') + ': NCERT prints "0.3 mm"')
d.basic('Is <i>Mycoplasma</i> really 0.3 mm long? (correction)', X('No') + ': about ' + N('0.3 µm') + ' (0.1–0.3 µm). "mm" in NCERT is a misprint; 0.3 mm would be visible to the naked eye.')
d.basic('Size of typical bacteria and of human RBCs?', 'Bacteria: ' + N('3–5 µm') + ' (Fig 8.2 says 1–2 µm). Human RBC: about ' + N('7.0 µm') + ' in diameter.')
d.basic('Largest isolated single cell?', 'The egg of an ' + T('ostrich'))
d.basic('Which are some of the longest cells?', T('Nerve cells'))
d.basic('Name the cell shapes shown in Figure 8.1.', 'RBC: round, biconcave. WBC: amoeboid. Columnar epithelial: long, narrow. Nerve cell: branched, long. Tracheid: elongated. Mesophyll: round, oval.', **img('fig_8_1_cell_shapes'))
d.basic('Rank by size (Figure 8.2): PPLO, virus, bacterium, eukaryotic cell.', 'Virus ' + N('0.02–0.2 µm') + ' < PPLO ' + N('~0.1 µm') + ' < bacterium ' + N('1–2 µm') + ' < eukaryotic cell ' + N('10–20 µm'), **fig('fig_8_2_cell_sizes'))

# ---------------------------------------------------------------- 8.4 Prokaryotes
d.sec('8.4-prokaryotic')
d.basic('Name the prokaryotes listed by NCERT.', 'Bacteria, blue-green algae, mycoplasma, ' + T('PPLO') + ' (Pleuro Pneumonia Like Organisms)')
d.cloze('Bacterial shapes: {{c1::bacillus}} (rod), {{c2::coccus}} (spherical), {{c3::vibrio}} (comma), {{c4::spirillum}} (spiral).')
d.basic('Which prokaryote lacks a cell wall?', T('Mycoplasma'))
d.basic('What are plasmids?', 'Small circular DNA ' + T('outside') + ' the genomic DNA in many bacteria')
d.basic('What do plasmids give bacteria, and how are they used?', 'Unique phenotypic characters, e.g. ' + T('antibiotic resistance') + '; used to monitor bacterial transformation with foreign DNA')
d.basic('Which is the only eukaryote-like organelle in prokaryotes?', T('Ribosomes'))
d.basic('What is a mesosome?', 'Infoldings of the ' + T('cell membrane') + ' (vesicles, tubules, lamellae): characteristic of prokaryotes')
d.basic('Functions of the mesosome?', 'Cell wall formation, DNA replication and distribution, respiration, secretion, more membrane surface area and enzymes')
d.basic('What are chromatophores? Where?', 'Pigment-containing membranous extensions into the cytoplasm, in ' + E('cyanobacteria'))

d.sec('8.4.1-cell-envelope')
d.basic('Three layers of the bacterial cell envelope, outside in?', T('Glycocalyx') + ' → ' + T('cell wall') + ' → ' + T('plasma membrane'))
d.basic('On what is the Gram positive / Gram negative division based?', 'Differences in the ' + T('cell envelope') + ' and whether it takes up the Gram stain')
d.basic('Slime layer vs capsule?', 'Both are glycocalyx: ' + T('slime layer') + ' is a loose sheath; ' + T('capsule') + ' is thick and tough')
d.basic('What does the bacterial cell wall do?', 'Determines ' + T('shape') + ' and stops the cell bursting or collapsing')
d.basic('Three parts of a bacterial flagellum?', T('Filament') + ', ' + T('hook') + ', ' + T('basal body') + ' (filament is the longest)')
d.basic('Pili vs fimbriae? Do they help movement?', X('Neither helps motility') + '. Pili: elongated tubular protein structures. Fimbriae: small bristle-like fibres that help attach to rocks and host tissues.')

d.sec('8.4.2-ribosomes-inclusions')
d.basic('Prokaryotic ribosomes: size, subunits and location?', N('70S') + ' (50S + 30S), about 15 × 20 nm, associated with the ' + T('plasma membrane'))
d.basic('What is a polysome?', 'Several ribosomes attached to a single ' + T('mRNA') + ', translating it into proteins')
d.basic('What are inclusion bodies? Examples?', 'Reserve material free in the cytoplasm, ' + X('not membrane-bound') + ': phosphate, cyanophycean and glycogen granules')
d.basic('Where are gas vacuoles found?', 'In blue green, and purple and green photosynthetic bacteria')

# ---------------------------------------------------------------- 8.5 Eukaryotes
d.sec('8.5-eukaryotic')
d.basic('Which organisms are eukaryotes?', 'All ' + T('protists, plants, animals and fungi'))
d.basic('What do plant cells have that animal cells lack?', T('Cell wall') + ', ' + T('plastids') + ', a large ' + T('central vacuole'))
d.basic('What do animal cells have that almost all plant cells lack?', T('Centrioles'))
d.occlusion('Figure 8.3 (a) · Plant cell', M + 'fig_8_3a_plant_cell.webp', (1001, 797), [
    ('Rough endoplasmic reticulum', P((435, 24, 209, 48))), ('Lysosome', P((356, 82, 105, 22))), ('Smooth endoplasmic reticulum', P((154, 99, 133, 73))),
    ('Plasmodesmata', P((39, 205, 167, 22))), ('Microtubule', P((29, 370, 129, 22))), ('Nucleus', P((717, 218, 86, 22))),
    ('Nucleolus', P((757, 269, 105, 22))), ('Golgi apparatus', P((769, 320, 109, 48))), ('Nuclear envelope', P((772, 393, 92, 48))),
    ('Plasma membrane', P((773, 471, 113, 45))), ('Vacuole', P((822, 555, 82, 22))), ('Middle lamella', P((780, 587, 155, 22))),
    ('Cell wall', P((699, 657, 90, 22))), ('Mitochondrion', P((621, 697, 155, 22))), ('Ribosomes', P((555, 753, 114, 22))),
    ('Chloroplast', P((360, 761, 123, 22))), ('Cytoplasm', P((249, 735, 113, 22))), ('Peroxisome', P((186, 697, 121, 22)))], printed=True)
d.occlusion('Figure 8.3 (b) · Animal cell', M + 'fig_8_3b_animal_cell.webp', (1001, 651), [
    ('Golgi apparatus', P((188, 18, 109, 48))), ('Smooth endoplasmic reticulum', P((62, 257, 133, 74))), ('Nuclear envelope', P((93, 357, 92, 48))),
    ('Nucleolus', P((93, 442, 105, 22))), ('Nucleus', P((159, 573, 86, 22))), ('Microvilli', P((699, 22, 97, 22))),
    ('Plasma membrane', P((722, 73, 113, 47))), ('Centriole', P((736, 180, 96, 22))), ('Peroxisome', P((750, 246, 109, 22))),
    ('Lysosome', P((761, 316, 105, 22))), ('Ribosomes', P((767, 393, 114, 22))), ('Mitochondrion', P((766, 460, 155, 22))),
    ('Rough endoplasmic reticulum', P((747, 518, 133, 74))), ('Cytoplasm', P((697, 604, 113, 22)))], printed=True)

d.sec('8.5.1-cell-membrane')
d.basic('Which cells were used in the chemical studies of the cell membrane?', 'Human ' + T('red blood cells'))
d.basic('What are cell membranes mainly made of?', T('Lipids') + ' (mainly phospholipids in a bilayer) and ' + T('proteins') + '; also cholesterol and carbohydrate')
d.basic('How are phospholipids arranged in the membrane?', 'Polar heads ' + T('outwards') + ', hydrophobic tails ' + T('inwards') + ', away from water')
d.basic('Protein and lipid in the human RBC membrane?', 'About ' + N('52%') + ' protein and ' + N('40%') + ' lipid')
d.basic('Integral vs peripheral proteins?', T('Peripheral') + ': on the surface. ' + T('Integral') + ': partially or totally buried in the membrane.')
d.basic('Who proposed the fluid mosaic model, and when?', T('Singer and Nicolson') + ', ' + N('1972'))
d.basic('What does "fluid" in the fluid mosaic model mean?', 'The quasi-fluid lipid lets proteins move ' + T('laterally') + ' within the bilayer (measured as fluidity)')
d.basic('Which functions depend on membrane fluidity?', 'Cell growth, intercellular junctions, secretion, endocytosis, cell division')
d.occlusion('Figure 8.4 · Fluid mosaic model', M + 'fig_8_4_fluid_mosaic.webp', (1001, 605), [
    ('Sugar', P((104, 30, 68, 22))), ('Peripheral protein', P((232, 24, 117, 49))), ('Phospholipid bilayer', P((839, 95, 137, 49))),
    ('Cholesterol', P((58, 565, 127, 22)))], printed=True)
d.basic('What is passive transport?', 'Movement across the membrane ' + X('without energy') + ', e.g. simple diffusion along the concentration gradient')
d.basic('What is osmosis?', 'Movement of ' + T('water') + ' by diffusion')
d.basic('How do polar molecules cross the membrane?', 'Via a ' + T('carrier protein') + ' (they cannot pass through the nonpolar bilayer)')
d.basic('What is active transport? Example?', 'Movement ' + T('against') + ' the concentration gradient using ' + T('ATP') + ', e.g. ' + E('Na⁺/K⁺ pump'))

d.sec('8.5.2-cell-wall')
d.basic('Functions of the cell wall?', 'Shape, protection from mechanical damage and infection, cell-to-cell interaction, barrier to undesirable macromolecules')
d.basic('Cell wall of algae vs other plants?', 'Algae: cellulose, galactans, mannans, minerals like CaCO₃. Other plants: cellulose, ' + T('hemicellulose') + ', pectins, proteins.')
d.basic('Primary vs secondary wall?', 'Primary: of a young cell, capable of growth. Secondary: formed on the ' + T('inner') + ' side (towards the membrane) as the cell matures.')
d.basic('What is the middle lamella made of, and what does it do?', 'Mainly ' + T('calcium pectate') + '; glues neighbouring cells together')
d.basic('What are plasmodesmata?', 'Connections through the cell wall and middle lamella linking the ' + T('cytoplasm') + ' of neighbouring cells')

d.sec('8.5.3-endomembrane')
d.basic('Which organelles make up the endomembrane system?', T('ER, Golgi complex, lysosomes, vacuoles'))
d.basic('Why are mitochondria, chloroplasts and peroxisomes excluded from the endomembrane system?', 'Their functions are ' + X('not coordinated') + ' with it')
d.basic('Into which compartments does the ER divide the cell?', T('Luminal') + ' (inside ER) and ' + T('extra luminal') + ' (cytoplasm)')
d.basic('RER vs SER: structure and function?', T('RER') + ': ribosomes on the surface; protein synthesis and secretion; continuous with the outer nuclear membrane. ' + T('SER') + ': no ribosomes; lipid synthesis (steroid hormones in animals).')
d.occlusion('Figure 8.5 · Endoplasmic reticulum', M + 'fig_8_5_er.webp', (669, 1001), [
    ('Nucleus', P((252, 43, 105, 26))), ('Nuclear pore', P((281, 87, 165, 26))), ('Rough endoplasmic reticulum', P((473, 79, 162, 82))),
    ('Ribosome', P((435, 680, 125, 26))), ('Smooth endoplasmic reticulum', P((27, 893, 168, 81)))], printed=True)
d.basic('Who first observed Golgi bodies, and when?', T('Camillo Golgi') + ', ' + N('1898'))
d.basic('What are cisternae, and their size?', 'Flat, disc-shaped sacs of the Golgi, ' + N('0.5–1.0 µm') + ' across, stacked in parallel', **fig('fig_8_6_golgi'))
d.cloze('The Golgi has a convex {{c1::cis (forming)}} face and a concave {{c2::trans (maturing)}} face; ER vesicles fuse with the {{c3::cis}} face.')
d.basic('Main function of the Golgi apparatus?', T('Packaging') + ' materials for delivery inside the cell or secretion; modifies proteins from the ER')
d.basic('What does the Golgi form besides packaged proteins?', T('Glycoproteins') + ' and ' + T('glycolipids'))
d.basic('How are lysosomes formed?', 'By packaging in the ' + T('Golgi apparatus'))
d.basic('What do lysosomes contain, and at what pH are these active?', 'Hydrolytic enzymes (lipases, proteases, carbohydrases), optimally active at ' + T('acidic') + ' pH')
d.basic('What is the tonoplast?', 'The single membrane around the ' + T('vacuole'))
d.basic('How much of a plant cell can the vacuole occupy?', 'Up to ' + N('90%'))
d.basic('Why is ion concentration higher in the vacuole than in the cytoplasm?', 'The tonoplast transports ions ' + T('against') + ' concentration gradients into the vacuole')
d.basic('Contractile vacuole vs food vacuole?', T('Contractile') + ' (Amoeba): osmoregulation and excretion. ' + T('Food vacuole') + ' (protists): formed by engulfing food.')
d.basic('Lysosomes and vacuoles are both endomembrane structures. How do their functions differ?', 'Lysosomes ' + T('digest') + ' macromolecules with enzymes; vacuoles ' + T('store') + ' water, sap and wastes, and regulate osmosis')

d.sec('8.5.4-mitochondria')
d.basic('Shape and size of a typical mitochondrion?', 'Sausage-shaped or cylindrical; diameter ' + N('0.2–1.0 µm') + ' (avg 0.5), length ' + N('1.0–4.1 µm'))
d.basic('What are cristae, and why are they there?', 'Infoldings of the ' + T('inner membrane') + ' towards the matrix; they ' + T('increase surface area'))
d.occlusion('Figure 8.7 · Mitochondrion (L.S.)', M + 'fig_8_7_mitochondrion.webp', (1001, 585), [
    ('Outer membrane', P((320, 36, 152, 58))), ('Inner membrane', P((498, 81, 151, 56))), ('Inter-membrane space', P((631, 60, 232, 57))),
    ('Matrix', P((558, 178, 92, 28))), ('Crista', P((737, 173, 88, 28)))], printed=True)
d.basic("Why are mitochondria called the cell's power houses?", 'They are sites of ' + T('aerobic respiration') + ' and produce ' + T('ATP'))
d.basic('What does the mitochondrial matrix contain for protein synthesis?', 'Single circular ' + T('DNA') + ', a few RNAs, ' + N('70S') + ' ribosomes')
d.basic('How do mitochondria divide?', 'By ' + T('fission'))
d.basic('Match: cristae, cisternae, thylakoids.', 'Cristae: infoldings in ' + T('mitochondria') + '. Cisternae: disc-shaped sacs in ' + T('Golgi') + '. Thylakoids: flat sacs in ' + T('chloroplast stroma') + '.')

d.sec('8.5.5-plastids')
d.basic('Where are plastids found?', 'All ' + T('plant cells') + ' and ' + T('euglenoids'))
d.basic('Name the three types of plastids and their pigments.', T('Chloroplasts') + ': chlorophyll, carotenoids. ' + T('Chromoplasts') + ': fat-soluble carotenoids (yellow, orange, red). ' + T('Leucoplasts') + ': colourless.')
d.cloze('Leucoplasts: {{c1::amyloplasts}} store starch (e.g. potato), {{c2::elaioplasts}} store oils and fats, and {{c3::aleuroplasts}} store proteins.',
        extra='Memory aid: <b>A</b>myl<b>o</b> = starch (amylose), <b>Ela</b>io = oil (Greek <i>elaion</i>, olive oil), <b>Aleur</b>o = protein (aleurone layer).')
d.basic('Size and number of chloroplasts?', N('5–10 µm') + ' long, ' + N('2–4 µm') + ' wide; from ' + N('1') + ' per cell (' + I('Chlamydomonas') + ') to ' + N('20–40') + ' per mesophyll cell')
d.basic('Which chloroplast membrane is less permeable?', 'The ' + T('inner') + ' membrane')
d.basic('What are grana and stroma lamellae?', T('Grana') + ': stacks of thylakoids like piles of coins. ' + T('Stroma lamellae') + ': flat tubules connecting thylakoids of different grana.', **fig('fig_8_8_chloroplast'))
d.basic('Where are chlorophyll pigments located?', 'In the ' + T('thylakoids'))
d.basic('What does the chloroplast stroma contain?', 'Enzymes for carbohydrate and protein synthesis, small double-stranded circular DNA, ribosomes')
d.basic('Which reactions occur in grana and stroma?', 'Grana: ' + T('light reactions') + '. Stroma: ' + T('dark reactions') + '.')
d.basic('Why is it thought mitochondria and chloroplasts were once bacteria? (beyond NCERT)', 'Both have their own ' + T('circular DNA') + ', ' + T('70S ribosomes') + ', double membranes, and divide by fission: the endosymbiotic theory')

d.sec('8.5.6-ribosomes')
d.basic('Who first observed ribosomes, and when?', T('George Palade') + ', ' + N('1953'))
d.basic('What are ribosomes made of?', T('RNA and proteins') + ', with no membrane')
d.basic('Subunits of 80S and 70S ribosomes?', '80S: ' + N('60S + 40S') + '. 70S: ' + N('50S + 30S') + '.', **fig('fig_8_9_ribosome'))
d.basic("What does 'S' mean in 70S and 80S?", T('Svedberg unit') + ': sedimentation coefficient, indirectly a measure of density and size')
d.basic('Why is 60S + 40S = 80S and not 100S?', 'Svedberg units measure how fast particles ' + T('sediment') + ', which depends on shape and size, so they do ' + X('not add up'))

d.sec('8.5.7-cytoskeleton-cilia')
d.basic('What makes up the cytoskeleton?', T('Microtubules, microfilaments, intermediate filaments'))
d.basic('Functions of the cytoskeleton?', 'Mechanical support, motility, maintaining cell shape')
d.basic('Cilia vs flagella?', 'Cilia: small, work like ' + T('oars') + ' to move the cell or fluid. Flagella: longer, move the cell.')
d.basic('What is the axoneme?', 'The core of a cilium or flagellum: microtubules parallel to its long axis')
d.basic('What is the 9+2 array?', N('Nine') + ' peripheral microtubule ' + T('doublets') + ' + a ' + N('pair') + ' of central microtubules')
d.occlusion('Figure 8.10 (b) · Section of a cilium / flagellum', M + 'fig_8_10_cilium.webp', (1001, 464), [
    ('Plasma membrane', P((719, 30, 113, 42))), ('Peripheral microtubules (doublets)', P((798, 101, 140, 63))),
    ('Interdoublet bridge', P((846, 229, 130, 42))), ('Central microtubule', P((742, 386, 114, 43))),
    ('Radial spoke', P((482, 414, 67, 47))), ('Central sheath', P((349, 184, 78, 42)))], printed=True)
d.basic('How many radial spokes in a cilium?', N('Nine'))
d.basic('From what do cilia and flagella emerge?', 'Centriole-like ' + T('basal bodies'))
d.basic('Is the bacterial flagellum like the eukaryotic one?', X('No') + '; structurally different (no 9+2 axoneme)')

d.sec('8.5.9-centrosome')
d.basic('What does a centrosome contain?', 'Usually two ' + T('centrioles') + ', perpendicular to each other, in amorphous pericentriolar material')
d.basic('Structure of a centriole?', 'Cartwheel of ' + N('nine') + ' peripheral ' + T('triplet') + ' fibrils of tubulin; central ' + T('hub') + ' joined to them by radial spokes')
d.basic('Doublets or triplets: cilium vs centriole?', 'Cilium axoneme: ' + T('9 doublets') + ' + 2 central (9+2). Centriole: ' + T('9 triplets') + ', no central pair (9+0).')
d.basic('What do centrioles form?', 'The ' + T('basal body') + ' of cilia or flagella, and ' + T('spindle fibres') + ' in animal cell division')

d.sec('8.5.10-nucleus')
d.basic('Who named chromatin?', T('Flemming') + ' (material stained by basic dyes)')
d.basic('What is the perinuclear space?', 'The ' + N('10–50 nm') + ' space between the two membranes of the nuclear envelope')
d.basic('What is the outer nuclear membrane continuous with?', 'The ' + T('endoplasmic reticulum') + ' (it bears ribosomes)')
d.basic('What passes through nuclear pores?', T('RNA and protein') + ' molecules, in both directions')
d.occlusion('Figure 8.11 · Structure of nucleus', M + 'fig_8_11_nucleus.webp', (1001, 642), [
    ('Nucleoplasm', P((734, 188, 231, 35))), ('Nucleolus', P((749, 300, 179, 35))), ('Nuclear pore', P((745, 353, 232, 35))),
    ('Nuclear membrane', P((749, 471, 193, 69)))], printed=True)
d.basic('Name two kinds of cells without a nucleus.', 'Erythrocytes of many ' + E('mammals') + ' and ' + E('sieve tube cells'))
d.basic('What happens in the nucleolus?', 'Active ' + T('ribosomal RNA') + ' synthesis; it is ' + X('not membrane-bound'))
d.basic('Which cells have larger, more numerous nucleoli?', 'Cells actively carrying out ' + T('protein synthesis'))
d.basic('What does chromatin contain?', 'DNA, basic proteins (' + T('histones') + '), non-histone proteins, RNA')
d.basic('Length of DNA in a single human cell, and in how many chromosomes?', 'About ' + N('2 metres') + ', in ' + N('46') + ' (23 pairs)')
d.basic('What are kinetochores?', 'Disc-shaped structures on the sides of the ' + T('centromere') + ' (primary constriction)', **fig('fig_8_12_kinetochore'))
d.cloze('Centromere position: {{c1::metacentric}} = middle (equal arms); {{c2::sub-metacentric}} = slightly off-centre; {{c3::acrocentric}} = close to one end; {{c4::telocentric}} = terminal.')
d.basic('Identify the four chromosome types in Figure 8.13 (left to right).', 'Metacentric, sub-metacentric, acrocentric, telocentric', **img('fig_8_13_chromosome_types'))
d.basic('What is a satellite chromosome?', 'A chromosome with a non-staining ' + T('secondary constriction') + ' that makes a small fragment appear')
d.basic('What are microbodies?', 'Minute membrane-bound vesicles with enzymes, in both plant and animal cells')

d.sec('summary')
table_card(d, 'Membranes', 'Single or double membrane?', [
    ('Mitochondria, chloroplasts, nucleus', 'Double', False), ('ER, Golgi, lysosome, vacuole', 'Single', False),
    ('Ribosome, centrosome', 'None', True)], term='Organelle membranes')

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
