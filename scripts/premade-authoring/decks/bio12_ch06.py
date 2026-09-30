import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Biology', 'class12-biology-ch06-evolution')
d = Deck('Chapter 6: Evolution', 'Class 12', ['class-12', 'biology', 'ch-6'])
d.description = 'Origin of life, Darwinism, evidences, adaptive radiation, mechanism, Hardy-Weinberg, history of life and human evolution'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}
MI = (1001, 951)

# ---------------------------------------------------------------- 6.1 Origin of life
d.sec('6.1-origin-of-life')
d.basic('What is evolutionary biology?', 'Study of the ' + T('history of life forms') + ' on earth')
d.basic('Why is looking at stars "looking into the past"?', 'Their light started its journey ' + T('millions of years') + ' ago')
d.basic('Age of the universe?', 'About ' + N('13.8 billion years'))
d.basic('Theory explaining the origin of the universe?', T('Big Bang theory') + ': a singular huge explosion; universe expanded and cooled; H and He formed; gases condensed into galaxies')
d.basic('When did the earth form?', 'About ' + N('4.5 billion years') + ' ago')
d.basic('Gases on early earth’s surface?', T('Water vapour, methane, CO₂, ammonia') + ' released from molten mass; ' + X('no atmosphere') + ' initially')
d.basic('How did early O₂ and oceans form?', 'UV split water; light H₂ escaped; O combined with NH₃ and CH₄ to form water, CO₂; ozone formed; vapour fell as rain to fill depressions')
d.basic('When did life appear?', N('500 million years') + ' after earth formed: almost ' + N('4 billion years') + ' ago')
d.basic('What is panspermia?', 'Idea that units of life (' + T('spores') + ') were transferred to planets including earth from outer space')
d.basic('What is spontaneous generation?', 'Belief that life came from ' + T('decaying and rotting matter') + ' (straw, mud)')
d.basic('Who disproved spontaneous generation and how?', T('Louis Pasteur') + ':<br>in pre-sterilised flasks no life arose from killed yeast;<br>in flasks open to air, organisms arose<br>→ life comes only from pre-existing life')
d.basic('Oparin–Haldane hypothesis?', 'First life came from pre-existing ' + T('non-living organic molecules') + ' (RNA, protein), preceded by ' + T('chemical evolution'))
d.basic('Conditions on primitive earth (Oparin–Haldane)?', 'High temperature, volcanic storms, ' + T('reducing atmosphere') + ' with CH₄, NH₃ etc.')
d.basic('Miller’s experiment: year and setup?', N('1953') + ', S.L. Miller: electric discharge in a closed flask with ' + T('CH₄, H₂, NH₃ and water vapour'))
d.basic('Result of Miller’s experiment?', 'Formation of ' + T('amino acids'))
d.occlusion('Figure 6.1 · Miller’s experiment', M + 'fig_6_1_miller.webp', MI, [
    ('Electrodes', wbox(716, 136, 870, 166, MI), True), ('To vacuum pump', wbox(26, 230, 190, 294, MI), True),
    ('Spark discharge', wbox(716, 320, 832, 390, MI), True), ('Gases', wbox(520, 400, 614, 430, MI), True),
    ('CH₄, NH₃, H₂O, H₂', wbox(356, 340, 416, 494, MI)), ('Water out', wbox(722, 492, 866, 522, MI), True),
    ('Condenser', wbox(718, 560, 876, 590, MI), True), ('Water in', wbox(714, 632, 838, 662, MI), True),
    ('Water droplets', wbox(714, 702, 930, 734, MI), True), ('Water containing organic compounds', wbox(694, 798, 978, 864, MI), True),
    ('Boiling water', wbox(172, 826, 364, 858, MI), True), ('Liquid water in trap', wbox(498, 902, 792, 934, MI), True)])
d.basic('Correction: NCERT prints the gases were "at 8000C". Correct reading?', N('800 °C') + ' as printed in NCERT (the degree sign was lost); in Miller’s real setup water was boiled (~100 °C) and sparks supplied energy')
d.basic('Other products in similar experiments?', 'Sugars, nitrogen bases, pigments and fats')
d.basic('Evidence that chemical evolution occurs in space?', 'Similar compounds found in ' + T('meteorites'))
d.basic('When did the first non-cellular life arise?', 'About ' + N('3 billion years') + ' ago: giant molecules (RNA, protein, polysaccharides)')
d.basic('When did the first cellular life arise (NCERT)?', 'About ' + N('2000 million years') + ' ago; single cells in water')
d.basic('Update: earliest evidence of cellular life?', 'Fossil microbes/stromatolites about ' + N('3.5 billion years') + ' old (NCERT’s 2000 mya is outdated)')
d.basic('What is abiogenesis (as accepted)?', 'First life arose slowly through evolutionary forces from ' + T('non-living molecules'))

# ---------------------------------------------------------------- 6.2 Theory
d.sec('6.2-evolution-theory')
d.basic('Three connotations of special creation?', '1) All organisms created as such. 2) Diversity always the same. 3) Earth is about ' + N('4000 years') + ' old.')
d.basic('Darwin’s voyage ship?', T('H.M.S. Beagle'))
d.basic('Darwin’s conclusions from the voyage?', 'Living forms share similarities with each other and with extinct forms.<br>' + T('Gradual evolution') + ' with extinctions and new forms')
d.basic('Fitness according to Darwin?', 'Ultimately and only ' + T('reproductive fitness') + ': fitter individuals leave more progeny')
d.basic('Who reached similar conclusions independently?', T('Alfred Wallace') + ', working in the Malay Archipelago')
d.basic('Conclusion about earth’s age from Darwinism?', 'Earth is ' + T('billions of years') + ' old, not thousands')

# ---------------------------------------------------------------- 6.3 Evidences
d.sec('6.3-evidences')
d.basic('What are fossils?', 'Remains of ' + T('hard parts') + ' of life forms found in rocks')
d.basic('What is paleontological evidence?', 'Different-aged rock sediments contain different fossils: life forms varied over time and some are restricted to certain geological spans', **fig('fig_6_2_dinosaur_tree'))
d.basic('How is the age of fossils found?', T('Radioactive dating'))
d.basic('Living counterparts of dinosaurs in Figure 6.2?', E('Crocodiles') + ' and ' + E('birds'))
d.basic('Embryological evidence (Haeckel)?', 'All vertebrate embryos, incl. human, develop ' + T('vestigial gill slits') + ' behind the head; functional only in fish')
d.basic('Who disproved Haeckel’s proposal?', T('Karl Ernst von Baer') + ': embryos never pass through the adult stages of other animals')
d.basic('Correction: NCERT spells it "Ernst Heckel". Correct?', T('Ernst Haeckel'))
d.basic('What are homologous organs?', 'Same anatomical structure, ' + T('different functions') + '; result of ' + T('divergent evolution') + '; indicate common ancestry', **fig('fig_6_3_homologous'))
d.basic('Homologous forelimb bones in whale, bat, cheetah, human?', T('Humerus, radius, ulna, carpals, metacarpals, phalanges'))
d.basic('Other animal homologies?', 'Vertebrate ' + T('hearts') + ' and ' + T('brains'))
d.basic('Plant example of homology?', 'Thorn of ' + EI('Bougainvillea') + ' and tendril of ' + EI('Cucurbita'))
d.basic('What are analogous organs?', 'Different structures, ' + T('same function') + '; result of ' + T('convergent evolution'))
table_card(d, 'Analogy', 'Why analogous?', [
    ('Wings of butterfly and bird', 'Flight, different structure', False), ('Eye of octopus and mammal', 'Vision, different origin', False),
    ('Flippers of penguin and dolphin', 'Swimming', False), ('Sweet potato and potato', 'Root vs stem modification for storage', False)],
    term='Examples of analogous organs')
d.basic('Homology vs analogy mnemonic?', 'Hom' + T('O') + 'logy = same ' + T('Origin') + '. An' + T('A') + 'logy = same ' + T('Activity') + ' (function).')
d.basic('Biochemical evidence of evolution?', 'Similarities in ' + T('proteins and genes') + ' performing a function in diverse organisms point to common ancestry')
d.basic('Argument from artificial selection?', 'If man created new breeds (e.g. dogs) in hundreds of years, nature could do the same over ' + T('millions of years'))
d.basic('Peppered moth observation in England?', 'Before industrialisation (1850s): more ' + T('white-winged') + ' moths. After (1920): more ' + T('dark-winged (melanised)') + ' moths.', **fig('fig_6_4_peppered_moth'))
d.basic('Explanation of industrial melanism?', 'Predators spot moths against a ' + T('contrasting background') + '.<br>Soot darkened trunks and killed white lichens, so dark moths were camouflaged')
d.basic('Why are lichens pollution indicators?', 'They ' + X('do not grow') + ' in polluted areas')
d.basic('Evidence from rural areas?', 'Melanic moth count stayed ' + T('low') + ' where there was no industrialisation')
d.basic('Is any variant completely wiped out?', X('No') + '; only the ' + T('proportions') + ' change')
d.basic('Examples of evolution by anthropogenic action?', 'Resistance to ' + T('herbicides, pesticides, antibiotics') + ' and drugs appearing in months/years')
d.basic('Antibiotic resistance explained by Darwinian selection (Exercise 1)?', 'A few bacteria already carry resistance variations; antibiotic kills the rest; resistant ones ' + T('survive and multiply') + ' → resistant population')
d.basic('Is evolution directed?', X('No') + '; it is a ' + T('stochastic') + ' process based on chance events and chance mutation')

# ---------------------------------------------------------------- 6.4 Adaptive radiation
d.sec('6.4-adaptive-radiation')
d.basic('Where did Darwin see his finches?', T('Galapagos Islands'))
d.basic('Darwin’s finches: original and derived forms?', 'From ' + T('seed-eating') + ' ancestors arose insectivorous and vegetarian finches with altered beaks', **fig('fig_6_5_finches'))
d.basic('Define adaptive radiation.', 'Evolution of different species in a geographical area starting from a point and ' + T('radiating') + ' to other habitats')
d.basic('Two examples of adaptive radiation (Exercise 8)?', T('Darwin’s finches') + ' and ' + T('Australian marsupials'))
d.basic('Name marsupials of the Australian radiation (Figure 6.6).', 'Tasmanian wolf, tiger cat, banded anteater, marsupial rat, kangaroo,<br>wombat, bandicoot, koala, marsupial mole, sugar glider', **img('fig_6_6_marsupial_radiation'))
d.basic('When is adaptive radiation called convergent evolution?', 'When ' + T('more than one') + ' adaptive radiation occurs in an isolated area, giving similar forms')
d.basic('Example of convergence: placental vs marsupial?', 'Placental wolf and ' + T('Tasmanian wolf') + ' (marsupial)', **fig('fig_6_7_convergent'))
d.basic('Pairs of placental and Australian marsupial mammals (Figure 6.7)?', 'Mole–marsupial mole; anteater–numbat; mouse–marsupial mouse; lemur–spotted cuscus; flying squirrel–flying phalanger; bobcat–Tasmanian tiger cat; wolf–Tasmanian wolf', **img('fig_6_7_convergent'))
d.basic('Can human evolution be called adaptive radiation? (Exercise 9)', X('No') + '. It is a single lineage, not many species radiating into different habitats from one ancestor in one area')

# ---------------------------------------------------------------- 6.5 Biological evolution
d.sec('6.5-biological-evolution')
d.basic('When would natural selection truly have started?', 'When cellular life with differences in ' + T('metabolic capability') + ' arose')
d.basic('Why do microbes evolve faster than fish or fowl?', 'Rate of new forms is linked to ' + T('life span') + '; microbes divide in minutes, animals live years')
d.basic('Why must fitness have a genetic basis?', 'Only ' + T('inherited') + ' characteristics can be selected and evolve')
d.basic('Two key concepts of Darwinian theory?', T('Branching descent') + ' and ' + T('natural selection'))
d.basic('Lamarck’s theory?', 'Evolution driven by ' + T('use and disuse') + ' of organs; acquired characters inherited (giraffe’s neck)')
d.basic('Why is Lamarckism rejected?', T('Acquired characters') + ' are not inherited; nobody believes the giraffe conjecture any more')
d.basic('Who may have influenced Darwin on populations?', T('Thomas Malthus'))
d.basic('Factual observations behind natural selection?', 'Resources limited; populations stable; members vary; most variations ' + T('inherited') + '; theoretical exponential growth → ' + T('competition'))
d.basic('Darwin’s key insight?', T('Heritable') + ' variations that improve resource use let a few reproduce more.<br>Over generations the population changes')

# ---------------------------------------------------------------- 6.6 Mechanism
d.sec('6.6-mechanism-of-evolution')
d.basic('Who proposed mutation theory, and on what plant?', T('Hugo de Vries') + ', ' + E('evening primrose'))
d.basic('De Vries’ mutations vs Darwin’s variations?', T('Mutations') + ': large, sudden, random, directionless. ' + T('Darwinian variations') + ': small, directional, gradual.')
d.basic('What is saltation?', T('Single-step large mutation') + ' causing speciation (de Vries)')
d.basic('What brought clarity between Darwin and de Vries?', T('Population genetics'))

# ---------------------------------------------------------------- 6.7 Hardy-Weinberg
d.sec('6.7-hardy-weinberg')
d.basic('State the Hardy–Weinberg principle.', 'Allele frequencies in a population are ' + T('stable and constant') + ' from generation to generation (genetic equilibrium)')
d.basic('What is a gene pool?', 'Total genes and their alleles in a population')
d.cloze('Hardy–Weinberg: \\( p^2 + 2pq + q^2 = 1 \\), where \\( p^2 \\) = frequency of {{c1::AA}}, \\( 2pq \\) = {{c2::Aa}}, \\( q^2 \\) = {{c3::aa}}.')
d.basic('What is \\( p + q \\)?', N('1') + ' (sum of all allele frequencies)')
d.basic('What indicates evolution in H–W terms?', 'Measured frequencies ' + T('differ from expected') + ': disturbance of genetic equilibrium')
d.cloze('Five factors affecting H–W equilibrium: {{c1::gene migration (gene flow)}}, {{c2::genetic drift}}, {{c3::mutation}}, {{c4::genetic recombination}}, {{c5::natural selection}}.')
d.basic('Gene migration vs gene flow?', T('Migration') + ' of a section of population changes allele frequencies in both populations.<br>Repeated migration = ' + T('gene flow'))
d.basic('What is genetic drift?', 'Change in allele frequency by ' + T('chance'))
d.basic('What is the founder effect?', 'A drifted population so different it becomes a new species; the original drifted group are ' + T('founders'))
steps_card(d, 'Hardy–Weinberg', '16% of a population is aa. Carrier (Aa) frequency?', 'Assume equilibrium.',
           ['q² = 0.16 → q = 0.4', 'p = 1 − 0.4 = 0.6', '2pq = 2 × 0.6 × 0.4 = <b>0.48</b>'], 2, 'H–W: aa = 16%, find Aa', '2pq = 0.48')
d.basic('Why is H–W equilibrium rare in nature? (intuition)', 'It needs no mutation, no migration, no selection, random mating and a huge population.<br>Real populations always break at least one')
d.basic('Three types of natural selection?', T('Stabilising') + ': more individuals at mean. ' + T('Directional') + ': shift away from mean. ' + T('Disruptive') + ': both extremes favoured.', **fig('fig_6_8_natural_selection'))
d.basic('Identify selection types in Figure 6.8.', '(a) ' + T('Stabilising') + ' (peak higher, narrower). (b) ' + T('Directional') + ' (peak shifts). (c) ' + T('Disruptive') + ' (two peaks).', **img('fig_6_8_natural_selection'))

# ---------------------------------------------------------------- 6.8 Brief account
d.sec('6.8-brief-account')
d.basic('What did some early cells gain the ability to do?', 'Release ' + T('O₂') + ', probably by splitting water like the light reaction')
table_card(d, 'Timeline (NCERT)', 'When?', [
    ('First cellular life', '2000 mya', False), ('Invertebrates active', '500 mya', False), ('Jawless fish', '350 mya', False),
    ('Sea weeds and few plants', '320 mya', False), ('Lobefins move to land', '350 mya', False), ('Dinosaurs disappear', '65 mya', False)],
    term='Brief history of life (NCERT dates)')
d.basic('Correction: NCERT dates jawless fish at ~350 mya. Modern estimate?', 'About ' + N('500 mya') + ' (Cambrian–Ordovician); NCERT’s dates are simplified')
d.basic('Who first invaded land?', T('Plants'))
d.basic('Living fossil caught in 1938?', T('Coelacanth') + ' (lobefin) off South Africa')
d.basic('What did lobefins evolve into?', 'The first ' + T('amphibians') + '; ancestors of frogs and salamanders')
d.basic('Key reptile innovation?', T('Thick-shelled eggs') + ' that do not dry up in the sun')
d.basic('Modern descendants of early reptiles?', E('Turtles, tortoises, crocodiles'))
d.basic('Fate of giant ferns?', 'Fell to form ' + T('coal deposits'))
d.basic('Fish-like reptiles that returned to water?', E('Ichthyosaurs') + ' (~200 mya)')
d.basic('Tyrannosaurus rex size?', 'About ' + N('20 feet') + ' tall with dagger-like teeth')
d.basic('Update: did dinosaurs "evolve into birds"?', 'Birds are ' + T('living theropod dinosaurs') + '; the non-avian dinosaurs died out ~66 mya, most likely after an ' + T('asteroid impact'))
d.basic('What were the first mammals like?', 'Small, ' + T('shrew-like'))
d.basic('Advantages of mammals?', T('Viviparous') + ' (young protected inside mother) and more intelligent in sensing and avoiding danger')
d.basic('Why did South American mammals disappear?', T('Continental drift') + ' joined South and North America; North American fauna overrode them')
d.basic('Why did Australian pouched mammals survive?', 'Continental drift isolated them; ' + X('no competition') + ' from other mammals')
d.basic('Aquatic mammals?', E('Whales, dolphins, seals, sea cows'))
d.basic('Read Figure 6.9: plant groups through geological periods.', 'Chlorophyte ancestors<br>→ tracheophytes, psilophyton<br>→ bryophytes, lycopods, horsetails, ferns, seed ferns<br>→ gymnosperms (cycads, conifers)<br>→ angiosperms (monocots, dicots)', **img('fig_6_9_plant_evolution'))
d.basic('Read Figure 6.10: which reptile group gave rise to mammals?', T('Therapsids') + ' (via pelycosaurs/synapsids)', **img('fig_6_10_vertebrate_evolution'))

# ---------------------------------------------------------------- 6.9 Man
d.sec('6.9-origin-of-man')
d.basic('Primates of ~15 mya?', EI('Dryopithecus') + ' and ' + EI('Ramapithecus') + ': hairy, walked like gorillas and chimpanzees')
d.basic('Dryopithecus vs Ramapithecus?', EI('Ramapithecus') + ': more ' + T('man-like') + '. ' + EI('Dryopithecus') + ': more ' + T('ape-like') + '.')
d.basic('Where were man-like fossil bones found?', T('Ethiopia and Tanzania'))
d.basic('Hominids of 3–4 mya?', 'Man-like primates in eastern Africa: ≤ ' + N('4 feet') + ' tall, walked ' + T('upright'))
d.basic('Australopithecines?', '~' + N('2 mya') + ' in East African grasslands; hunted with stone weapons but ate mainly ' + T('fruit'))
table_card(d, 'Human evolution', 'Brain size / feature?', [
    ('Homo habilis', '650–800 cc; first human-like hominid; probably no meat', False),
    ('Homo erectus', '~900 cc; ~1.5 mya; fossils in Java (1891); ate meat', False),
    ('Neanderthal man', '1400 cc; 1,00,000–40,000 yrs ago; hides, buried dead', False),
    ('Homo sapiens', 'Arose in Africa; modern form during ice age 75,000–10,000 yrs ago', False)], term='Stages of human evolution')
d.basic('Mnemonic for human brain sizes?', '"' + T('Habilis 7, Erectus 9, Neanderthal 14') + '" (hundreds of cc): 650–800, 900, 1400')
d.basic('Where did Neanderthals live?', 'Near east and central Asia')
d.basic('Where did Homo sapiens arise?', T('Africa') + '; moved across continents and developed into distinct races')
d.basic('Update: when did Homo sapiens arise?', 'Fossils from Jebel Irhoud (Morocco) show ~' + N('300,000 years') + '; NCERT’s 75,000–10,000 refers to modern humans spreading during the ice age')
d.basic('When did pre-historic cave art develop?', 'About ' + N('18,000 years') + ' ago')
d.basic('Indian site of pre-historic cave paintings?', T('Bhimbetka') + ' rock shelter, Raisen district, Madhya Pradesh')
d.basic('When did agriculture and settlements begin?', 'About ' + N('10,000 years') + ' ago')
d.basic('What does Figure 6.11 show about skulls?', 'The ' + T('baby chimpanzee') + ' skull is more like the adult human skull than the adult chimpanzee skull', **fig('fig_6_11_skulls'))
d.basic('Trends in human evolution (Exercise 4)?', 'Increasing ' + T('brain size') + ', upright posture, shift to omnivory/meat, tool use, language and self-consciousness')

# ---------------------------------------------------------------- summary
d.sec('summary')
table_card(d, 'Who said what', 'Idea?', [
    ('Oparin & Haldane', 'Chemical evolution before life', False), ('Miller', 'Amino acids from simple gases (1953)', False),
    ('Lamarck', 'Use and disuse; inheritance of acquired characters', False), ('Darwin & Wallace', 'Natural selection', False),
    ('de Vries', 'Mutation theory, saltation', False), ('Hardy & Weinberg', 'Genetic equilibrium', False)], term='Evolution: scientists and ideas')
table_card(d, 'Divergent vs convergent', 'Which?', [
    ('Forelimbs of whale, bat, human', 'Divergent (homologous)', False), ('Wings of bird and butterfly', 'Convergent (analogous)', False),
    ('Marsupials of Australia', 'Adaptive radiation', False), ('Tasmanian wolf and placental wolf', 'Convergent', False)],
    term='Divergent vs convergent evolution')

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
