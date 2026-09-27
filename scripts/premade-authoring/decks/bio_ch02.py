import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch02-biological-classification')
d = Deck('Chapter 2: Biological Classification', 'Class 11', ['class-11', 'biology', 'ch-2'])
M = 'media/'

# ---------------------------------------------------------------- Introduction
d.sec('history-of-classification')
d.basic('Who first tried to give classification a scientific basis?', T('Aristotle'))
d.basic('On what basis did Aristotle classify plants into trees, shrubs and herbs?', 'Simple ' + T('morphological characters'))
d.basic('Into which two groups did Aristotle divide animals?', 'Those with ' + T('red blood') + ' and those ' + X('without') + ' it')
d.basic("Which two kingdoms made up the classification of Linnaeus' time?", T('Plantae') + ' and ' + T('Animalia'))
d.cloze('The two kingdom system did not distinguish between {{c1::eukaryotes and prokaryotes}}, '
        '{{c2::unicellular and multicellular}} organisms, and {{c3::photosynthetic (green algae) and non-photosynthetic (fungi)}} organisms.')
d.basic('Who proposed the Five Kingdom Classification, and in which year?', T('R.H. Whittaker') + ', ' + N('1969'))
d.basic("Name Whittaker's five kingdoms.", 'Monera, Protista, Fungi, Plantae, Animalia')
d.basic("What were Whittaker's main criteria for classification?",
        '<ul><li>Cell structure</li><li>Body organisation</li><li>Mode of nutrition and reproduction</li><li>Phylogenetic relationships</li></ul>')
d.cloze('The three-domain system splits Kingdom {{c1::Monera}} into two domains, giving a {{c2::six}} kingdom classification.')
d.basic("In earlier systems, which single character united everything placed under 'Plants'?", 'Presence of a ' + T('cell wall'))
d.basic("Which prokaryotes did earlier systems wrongly group with eukaryotic 'Plants'?", 'Bacteria and ' + T('blue green algae') + ' (cyanobacteria)')
d.basic('Which unicellular and multicellular algae were placed together in the older system?', EI('Chlamydomonas') + ' (unicellular) and ' + EI('Spirogyra') + ' (multicellular)')
d.cloze('Fungi have {{c1::chitin}} in their cell walls, while green plants have a {{c2::cellulosic}} cell wall.')
d.cloze('Kingdom Protista brought together {{c1::<i>Chlamydomonas</i> and <i>Chlorella</i>}} (earlier in plants) with '
        '{{c2::<i>Paramoecium</i> and <i>Amoeba</i>}} (earlier in animals).')
d.basic('What does a phylogenetic classification rest on?', T('Evolutionary relationships'))

# ---------------------------------------------------------------- Table 2.1
d.sec('five-kingdoms-table')
d.basic('Which is the only kingdom with prokaryotic cells?', T('Monera') + '<br>All other kingdoms are eukaryotic.')
d.basic('Which kingdom lacks a nuclear membrane?', T('Monera'))
table_card(d, 'Table 2.1 · Five kingdoms', 'Cell wall in each kingdom?', [
    ('Monera', 'Non-cellulosic (polysaccharide + amino acid)', False),
    ('Protista', 'Present in some', False),
    ('Fungi', 'Present, with chitin', False),
    ('Plantae', 'Present (cellulose)', False),
    ('Animalia', 'Absent', True)], term='Five kingdoms: cell wall')
table_card(d, 'Table 2.1 · Five kingdoms', 'Body organisation in each kingdom?', [
    ('Monera', 'Cellular', False),
    ('Protista', 'Cellular', False),
    ('Fungi', 'Multicellular / loose tissue', False),
    ('Plantae', 'Tissue / organ', False),
    ('Animalia', 'Tissue / organ / organ system', False)], term='Five kingdoms: body organisation')
table_card(d, 'Table 2.1 · Five kingdoms', 'Mode of nutrition in each kingdom?', [
    ('Monera', 'Autotrophic (chemosynthetic, photosynthetic) and heterotrophic (saprophytic, parasitic)', False),
    ('Protista', 'Autotrophic (photosynthetic) and heterotrophic', False),
    ('Fungi', 'Heterotrophic (saprophytic, parasitic)', False),
    ('Plantae', 'Autotrophic (photosynthetic)', False),
    ('Animalia', 'Heterotrophic (holozoic, saprophytic etc.)', False)], term='Five kingdoms: mode of nutrition')

# ---------------------------------------------------------------- 2.1 Monera
d.sec('2.1-monera')
d.basic('Who are the sole members of Kingdom Monera?', T('Bacteria'))
d.basic('Name four extreme habitats where bacteria live.', 'Hot springs, deserts, snow, deep oceans')
d.cloze('Bacterial shapes: spherical {{c1::Coccus}}, rod-shaped {{c2::Bacillus}}, comma-shaped {{c3::Vibrium}} and spiral {{c4::Spirillum}}.')
d.occlusion('Figure 2.1 · Bacteria of different shapes', M + 'fig_2_1_bacteria_shapes.webp', (1000, 252), [
    ('Spore', pad((398, 57, 53, 19))), ('Flagellum', pad((728, 53, 91, 19))), ('Cocci', pad((57, 199, 50, 19))),
    ('Bacilli', pad((276, 207, 58, 19))), ('Spirilla', pad((538, 195, 67, 19))), ('Vibrio', pad((882, 222, 55, 19)))])
d.basic('Which group of organisms shows the most extensive metabolic diversity?', T('Bacteria'))
d.basic('What are the two kinds of autotrophic bacteria?', T('Photosynthetic') + ' autotrophs and ' + T('chemosynthetic') + ' autotrophs')
d.basic('What is the mode of nutrition of the vast majority of bacteria?', T('Heterotrophic'))

d.sec('2.1.1-archaebacteria')
d.cloze('Archaebacteria: {{c1::halophiles}} live in extreme salty areas, {{c2::thermoacidophiles}} in hot springs, and {{c3::methanogens}} in marshy areas.')
d.basic('What lets archaebacteria survive extreme conditions?', 'A ' + T('different cell wall structure') + ' from other bacteria')
d.basic('Where in animals are methanogens found?', 'In the gut of ' + T('ruminants') + ', e.g. ' + E('cows and buffaloes'))
d.basic('What do methanogens produce from the dung of ruminants?', T('Methane') + ' (biogas)')

d.sec('2.1.2-eubacteria')
d.basic("What two features characterise eubacteria ('true bacteria')?", 'A ' + T('rigid cell wall') + ', and a ' + T('flagellum') + ' if motile')
d.basic('What is the common name for cyanobacteria?', T('Blue-green algae'))
d.basic('Which chlorophyll do cyanobacteria share with green plants?', T('Chlorophyll <i>a</i>'))
d.basic('What surrounds cyanobacterial colonies?', 'A ' + T('gelatinous sheath'))
d.basic('What do cyanobacteria often form in polluted water bodies?', T('Blooms'))
d.cloze('Some cyanobacteria fix atmospheric nitrogen in specialised cells called {{c1::heterocysts}}, e.g. {{c2::<i>Nostoc</i> and <i>Anabaena</i>}}.')
d.occlusion('Figure 2.2 · A filamentous blue-green alga, <i>Nostoc</i>', M + 'fig_2_2_nostoc.webp', (747, 901), [
    ('Heterocyst', [255, 172, 245, 60]), ('Mucilaginous sheath', [402, 312, 310, 108])])
d.basic('Which substances do chemosynthetic autotrophic bacteria oxidise for energy?', 'Nitrates, nitrites and ammonia')
d.basic('Chemosynthetic bacteria help recycle which nutrients?', 'Nitrogen, phosphorous, iron, sulphur')
d.basic('Which bacteria are the most abundant in nature?', T('Heterotrophic bacteria'))
d.basic('What ecological role do most heterotrophic bacteria play?', T('Decomposers'))
d.basic('Give three uses of heterotrophic bacteria.', '<ul><li>Making curd from milk</li><li>Producing antibiotics</li><li>Fixing nitrogen in legume roots</li></ul>')
d.basic('Name four diseases caused by bacteria.', E('Cholera, typhoid, tetanus, citrus canker'))
d.cloze('Bacteria reproduce mainly by {{c1::fission}}; under unfavourable conditions they produce {{c2::spores}}.')
d.basic('What sort of sexual reproduction do bacteria show?', 'A primitive ' + T('DNA transfer') + ' from one bacterium to another')
d.basic('Which organisms completely lack a cell wall?', T('Mycoplasma'))
d.basic('What are the smallest living cells known?', T('Mycoplasma'))

# ---------------------------------------------------------------- 2.2 Protista
d.sec('2.2-protista')
d.basic('Which kingdom contains all single-celled eukaryotes?', T('Protista'))
d.basic('Which five groups does NCERT place under Protista?', 'Chrysophytes, dinoflagellates, euglenoids, slime moulds, protozoans')
d.basic('What is the main habitat of protists?', T('Aquatic'))
d.basic('How do protists reproduce sexually?', 'By ' + T('cell fusion') + ' and ' + T('zygote formation'))

d.sec('2.2.1-chrysophytes')
d.basic('Which organisms make up the chrysophytes?', T('Diatoms') + ' and ' + T('golden algae (desmids)'))
d.basic('What are organisms that float passively in water currents called?', T('Plankton'))
d.basic('How is a diatom cell wall built?', 'Two thin ' + T('overlapping shells') + ' that fit together like a ' + T('soap box'))
d.basic('Why are diatom cell walls indestructible?', 'They are embedded with ' + T('silica'))
d.basic("What is 'diatomaceous earth'?", 'Diatom cell wall deposits accumulated over billions of years')
d.basic('What is diatomaceous earth used for?', 'Polishing, and filtration of oils and syrups')
d.basic("Who are the chief 'producers' in the oceans?", T('Diatoms'))

d.sec('2.2.2-dinoflagellates')
d.basic('Where do dinoflagellates mostly live, and how do they get food?', 'Mostly ' + T('marine') + '; ' + T('photosynthetic'))
d.basic('What decides the colour of a dinoflagellate?', 'The main ' + T('pigments') + ' in its cells')
d.basic('What is on the outer surface of a dinoflagellate cell wall?', 'Stiff ' + T('cellulose plates'))
d.basic('How are the two flagella of a dinoflagellate arranged?', 'One ' + T('longitudinal') + ', one ' + T('transverse') + ' in a furrow between the wall plates')
d.basic('Which dinoflagellate causes red tides?', EI('Gonyaulax'))
d.basic('What harm do red tides do?', 'Their ' + T('toxins') + ' may kill marine animals such as fishes')

d.sec('2.2.3-euglenoids')
d.basic('Where are most euglenoids found?', T('Stagnant fresh water'))
d.basic('What do euglenoids have instead of a cell wall?', 'A protein-rich ' + T('pellicle') + ', which keeps the body flexible')
d.basic('What flagella do euglenoids have?', 'Two: one ' + T('short') + ', one ' + T('long'))
d.basic('How do euglenoids feed when kept out of sunlight?', 'As ' + T('heterotrophs') + ', preying on smaller organisms')
d.basic('Euglenoid pigments are identical to those of which organisms?', T('Higher plants'))
d.basic('Give an example of a euglenoid.', EI('Euglena'))

d.sec('2.2.4-slime-moulds')
d.basic('What is the mode of nutrition of slime moulds?', T('Saprophytic'))
d.basic('What aggregation do slime moulds form under suitable conditions?', 'A ' + T('plasmodium') + ', which can spread over several feet')
d.basic('What does the plasmodium form in unfavourable conditions?', T('Fruiting bodies') + ' bearing spores at their tips')
d.basic('Name two features of slime mould spores.', 'True walls; extremely resistant, surviving for many years')
d.basic('How are slime mould spores dispersed?', 'By ' + T('air currents'))

d.sec('2.2.5-protozoans')
d.basic('What is the mode of nutrition of protozoans?', 'All are ' + T('heterotrophs') + ', living as predators or parasites')
d.basic('Protozoans are believed to be primitive relatives of which group?', T('Animals'))
d.basic('Name the four major groups of protozoans.', 'Amoeboid, flagellated, ciliated, sporozoans')
d.basic('What do amoeboid protozoans use to move and catch prey?', T('Pseudopodia') + ' (false feet), as in ' + EI('Amoeba'))
d.basic('What do marine amoeboid protozoans have on their surface?', T('Silica shells'))
d.basic('Name a parasitic amoeboid protozoan.', EI('Entamoeba'))
d.basic('Which flagellated protozoan causes sleeping sickness?', EI('Trypanosoma'))
d.basic('How does food reach the gullet of a ciliated protozoan?', 'Coordinated movement of rows of ' + T('cilia') + ' steers food-laden water in')
d.basic('Give an example of a ciliated protozoan.', EI('Paramoecium'))
d.basic('What feature is shared by all sporozoans?', 'An infectious ' + T('spore-like stage') + ' in the life cycle')
d.basic('Which sporozoan causes malaria?', EI('Plasmodium'))
d.occlusion('Figure 2.4 · Name each protist', M + 'fig_2_4_protists.webp', (900, 972), [
    ('Dinoflagellate', [60, 432, 330, 50]), ('<i>Euglena</i>', [510, 432, 330, 50]),
    ('Slime mould', [60, 918, 330, 50]), ('<i>Paramoecium</i>', [510, 918, 330, 50])])

# ---------------------------------------------------------------- 2.3 Fungi
d.sec('2.3-fungi')
d.basic('Which unicellular fungus is used to make bread and beer?', E('Yeast'))
d.basic('Which fungus causes wheat rust?', EI('Puccinia'))
d.basic('Which fungus is a source of antibiotics?', EI('Penicillium'))
d.basic('Which fungi are unicellular rather than filamentous?', X('Yeasts'))
d.cloze('A fungal body is made of long thread-like {{c1::hyphae}}; their network is called the {{c2::mycelium}}.')
d.basic('What are coenocytic hyphae?', 'Continuous tubes filled with ' + T('multinucleated cytoplasm'))
d.basic('What divides the hyphae of some fungi into cells?', T('Septae') + ' (cross walls)')
d.basic('What are fungal cell walls made of?', T('Chitin') + ' and ' + T('polysaccharides'))
d.basic('What are fungi that absorb soluble organic matter from dead substrates called?', T('Saprophytes'))
d.cloze('Fungi live as symbionts with algae as {{c1::lichens}} and with roots of higher plants as {{c2::mycorrhiza}}.')
d.basic('Name three means of vegetative reproduction in fungi.', 'Fragmentation, fission, budding')
d.basic('Name three kinds of asexual spores in fungi.', 'Conidia, sporangiospores, zoospores')
d.basic('Name three kinds of sexual spores in fungi.', 'Oospores, ascospores, basidiospores')
d.basic('Where are fungal spores produced?', 'In distinct structures called ' + T('fruiting bodies'))
d.cloze('Sexual cycle of fungi: {{c1::plasmogamy}} (fusion of protoplasms) → {{c2::karyogamy}} (fusion of nuclei) → {{c3::meiosis}} in the zygote, giving haploid spores.')
d.basic('What is a dikaryon?', 'A cell with ' + T('two nuclei') + ' (' + N('n + n') + '). The phase is called the ' + T('dikaryophase') + '.')
d.basic('In which fungal classes does a dikaryotic stage occur?', T('Ascomycetes') + ' and ' + T('basidiomycetes'))
d.basic('What is the basis for dividing Kingdom Fungi into classes?', '<ul><li>Morphology of the mycelium</li><li>Mode of spore formation</li><li>Fruiting bodies</li></ul>')
d.occlusion('Figure 2.5 · Name each fungus', M + 'fig_2_5_fungi.webp', (900, 972), [
    ('<i>Mucor</i>', [60, 432, 330, 50]), ('<i>Aspergillus</i>', [510, 432, 330, 50]), ('<i>Agaricus</i>', [285, 918, 330, 50])])

d.sec('2.3.1-phycomycetes')
d.basic('Where are phycomycetes found?', 'Aquatic habitats, decaying wood in moist places, or as ' + T('obligate parasites') + ' on plants')
d.basic('What kind of mycelium do phycomycetes have?', T('Aseptate') + ' and ' + T('coenocytic'))
d.cloze('Phycomycetes reproduce asexually by motile {{c1::zoospores}} or non-motile {{c2::aplanospores}}, produced endogenously in a {{c3::sporangium}}.')
d.basic('How is a zygospore formed?', 'By ' + T('fusion of two gametes'))
d.basic('What are gametes called when they are similar in morphology?', T('Isogamous'))
d.basic('Which phycomycete is the bread mould?', EI('Rhizopus'))
d.basic('Which phycomycete is parasitic on mustard?', EI('Albugo'))

d.sec('2.3.2-ascomycetes')
d.basic('What is the common name of ascomycetes?', T('Sac fungi'))
d.basic('Name a unicellular ascomycete.', E('Yeast') + ' (' + EI('Saccharomyces') + ')')
d.basic("What does 'coprophilous' mean?", 'Growing on ' + T('dung'))
d.basic('Where are the asexual spores (conidia) of ascomycetes produced?', T('Exogenously') + ' on special mycelium called ' + T('conidiophores'))
d.basic('Where are ascospores produced?', T('Endogenously') + ' in sac-like ' + T('asci'))
d.basic('What are the fruiting bodies of ascomycetes called?', T('Ascocarps'))
d.basic('Which ascomycete is used extensively in biochemical and genetic work?', EI('Neurospora'))
d.basic('Which edible ascomycetes are considered delicacies?', E('Morels') + ' and ' + E('truffles'))

d.sec('2.3.3-basidiomycetes')
d.basic('Name three common forms of basidiomycetes.', 'Mushrooms, bracket fungi, puffballs')
d.basic('Which basidiomycetes are parasites on living plants?', E('Rusts') + ' and ' + E('smuts'))
d.basic('How do basidiomycetes usually reproduce vegetatively?', 'By ' + T('fragmentation') + ' (asexual spores are ' + X('generally not found') + ')')
d.basic('How does plasmogamy occur in basidiomycetes, which lack sex organs?', 'Fusion of two ' + T('vegetative (somatic) cells') + ' of different strains')
d.basic('Where do karyogamy and meiosis occur in basidiomycetes?', 'In the ' + T('basidium'))
d.basic('How many basidiospores does a basidium produce?', N('Four'))
d.basic('Are basidiospores produced endogenously or exogenously?', T('Exogenously') + ', on the basidium')
d.basic('What are the fruiting bodies of basidiomycetes called?', T('Basidiocarps'))

d.sec('2.3.4-deuteromycetes')
d.basic('Why are deuteromycetes called imperfect fungi?', 'Only their ' + T('asexual or vegetative') + ' phases are known')
d.basic('Where are deuteromycetes usually moved once their sexual stage is found?', T('Ascomycetes') + ' or ' + T('basidiomycetes'))
d.basic('By which spores alone do deuteromycetes reproduce?', T('Conidia') + ' (asexual)')
d.basic('What useful role do many deuteromycetes play?', 'Decomposing litter and helping ' + T('mineral cycling'))

d.sec('fungi-comparison')
table_card(d, 'Kingdom Fungi · four classes', 'Type of mycelium?', [
    ('Phycomycetes', 'Aseptate, coenocytic', False), ('Ascomycetes', 'Branched, septate', False),
    ('Basidiomycetes', 'Branched, septate', False), ('Deuteromycetes', 'Septate, branched', False)],
    term='Fungi classes: mycelium')
table_card(d, 'Kingdom Fungi · four classes', 'Sexual spores?', [
    ('Phycomycetes', 'Zygospore', False), ('Ascomycetes', 'Ascospores (in asci)', False),
    ('Basidiomycetes', 'Basidiospores (on basidium)', False), ('Deuteromycetes', 'None known', True)],
    term='Fungi classes: sexual spores')
table_card(d, 'Kingdom Fungi · four classes', 'Give the examples NCERT lists.', [
    ('Phycomycetes', '<i>Mucor, Rhizopus, Albugo</i>', False),
    ('Ascomycetes', '<i>Aspergillus, Claviceps, Neurospora</i>', False),
    ('Basidiomycetes', '<i>Agaricus, Ustilago, Puccinia</i>', False),
    ('Deuteromycetes', '<i>Alternaria, Colletotrichum, Trichoderma</i>', False)],
    term='Fungi classes: examples')
d.basic('<i>Ustilago</i> is which kind of fungus?', E('Smut') + ' (basidiomycete)')

# ---------------------------------------------------------------- 2.4 Plantae, 2.5 Animalia
d.sec('2.4-plantae')
d.basic('Which organisms does Kingdom Plantae include?', 'All ' + T('eukaryotic chlorophyll-containing') + ' organisms')
d.basic('Name two insectivorous plants.', E('Bladderwort') + ' and ' + E('Venus fly trap'))
d.basic('Name a parasitic plant.', EI('Cuscuta'))
d.basic('Which five groups make up Kingdom Plantae?', 'Algae, bryophytes, pteridophytes, gymnosperms, angiosperms')
d.basic('What is alternation of generations?', 'The diploid ' + T('sporophytic') + ' and haploid ' + T('gametophytic') + ' phases alternate in the life cycle')

d.sec('2.5-animalia')
d.basic('Which kingdom has multicellular, heterotrophic eukaryotes whose cells have no cell wall?', T('Animalia'))
d.basic('In what form do animals store food reserves?', T('Glycogen') + ' or ' + T('fat'))
d.basic('What is the mode of nutrition of animals?', T('Holozoic') + ' (by ingestion of food)')
d.basic('How do animals reproduce sexually?', T('Copulation') + ' of male and female, then embryological development')

# ---------------------------------------------------------------- 2.6 Viruses, viroids, prions, lichens
d.sec('2.6-viruses')
d.basic("Which organisms find no place in Whittaker's five kingdoms?", 'Lichens, viruses, viroids, prions')
d.basic('Why were viruses left out of classification?', 'They are not truly living: they have ' + X('no cell structure'))
d.basic('What are viruses like outside a living cell?', 'An ' + T('inert crystalline') + ' structure')
d.basic("What does the word 'virus' mean?", T('Venom') + ' or poisonous fluid')
d.basic('What did Dmitri Ivanowsky (1892) find about the cause of tobacco mosaic disease?', 'Microbes ' + T('smaller than bacteria') + '; they passed through bacteria-proof filters')
d.basic("Who named the new pathogen 'virus' and called it <i>Contagium vivum fluidum</i>?", T('M.W. Beijerinck') + ' (' + N('1898') + ')')
d.basic('What does <i>Contagium vivum fluidum</i> mean?', T('Infectious living fluid'))
d.basic('What did W.M. Stanley (1935) show about viruses?', 'They can be ' + T('crystallised') + '; the crystals are largely proteins')
d.basic('Can a virus reproduce outside a host cell?', X('No') + '. Viruses are ' + T('obligate parasites'))
d.basic('Can a virus contain both RNA and DNA?', X('No') + '. It has ' + T('either') + ' RNA or DNA')
d.basic('Which part of a virus is infectious?', 'The ' + T('genetic material'))
table_card(d, '2.6 · Viruses', 'Usual genetic material?', [
    ('Plant viruses', 'Single stranded RNA', False),
    ('Animal viruses', 'Single or double stranded RNA, or double stranded DNA', False),
    ('Bacteriophages', 'Double stranded DNA', False)], term='Genetic material of viruses')
d.cloze('The protein coat of a virus, the {{c1::capsid}}, is made of small subunits called {{c2::capsomeres}}.')
d.basic('In what geometric forms are capsomeres arranged?', T('Helical') + ' or ' + T('polyhedral'))
d.basic('Name five viral diseases of humans.', E('Mumps, small pox, herpes, influenza, AIDS'))
d.basic('Name four symptoms of viral infection in plants.', '<ul><li>Mosaic formation</li><li>Leaf rolling and curling</li><li>Yellowing and vein clearing</li><li>Dwarfing, stunted growth</li></ul>')
d.occlusion('Figure 2.6 (a) · Tobacco Mosaic Virus (TMV)', M + 'fig_2_6a_tmv.webp', (901, 619), [
    ('RNA', pad((196, 544, 70, 33))), ('Capsid', pad((382, 544, 110, 33)))], guess='hide-one')
d.occlusion('Figure 2.6 (b) · Bacteriophage', M + 'fig_2_6b_bacteriophage.webp', (1001, 976), [
    ('Head', pad((813, 216, 103, 41))), ('Collar', pad((812, 393, 119, 41))), ('Sheath', pad((45, 458, 141, 41))),
    ('Tail fibres', pad((347, 910, 199, 41)))])

d.sec('2.6-viroids-prions')
d.basic('Who discovered viroids, and when?', T('T.O. Diener') + ', ' + N('1971'))
d.basic('Which disease do viroids cause?', E('Potato spindle tuber disease'))
d.basic('How does a viroid differ from a virus?', 'A viroid is free RNA that ' + X('lacks a protein coat'))
d.basic('What is a prion made of?', 'Abnormally ' + T('folded protein') + ', about the size of a virus')
d.cloze('Prions cause {{c1::bovine spongiform encephalopathy (BSE)}}, or mad cow disease, in cattle and {{c2::Creutzfeldt–Jacob disease (CJD)}} in humans.')

d.sec('2.6-lichens')
d.basic('What are lichens?', 'Symbiotic associations between ' + T('algae') + ' and ' + T('fungi'))
d.basic('What is the algal partner of a lichen called?', T('Phycobiont') + ' (autotrophic)')
d.basic('What is the fungal partner of a lichen called?', T('Mycobiont') + ' (heterotrophic)')
d.basic('What does each partner give the other in a lichen?', 'Alga: ' + T('food') + '. Fungus: ' + T('shelter') + ', plus mineral nutrients and water.')
d.basic('Why are lichens good pollution indicators?', 'They ' + X('do not grow') + ' in polluted areas')

os.makedirs(OUT, exist_ok=True)
n = d.write(os.path.join(OUT, 'deck.json'))
print('notes', n)
