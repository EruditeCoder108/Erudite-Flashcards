import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Biology', 'class12-biology-ch09-biotechnology-principles-and-processes')
d = Deck('Chapter 9: Biotechnology: Principles and Processes', 'Class 12', ['class-12', 'biology', 'ch-9'])
d.description = 'Genetic engineering principles, restriction enzymes, gel electrophoresis, vectors, competent hosts, PCR, bioreactors and downstream processing'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}
PB, PC = (1001, 801), (1001, 741)

# ---------------------------------------------------------------- intro
d.sec('9.0-intro')
d.basic('Define biotechnology.', 'Techniques using ' + T('live organisms or their enzymes') + ' to make products and processes useful to humans')
d.basic('Biotechnology in the restricted modern sense?', 'Processes using ' + T('genetically modified organisms') + ' on a large scale')
d.basic('Other processes included in biotechnology?', 'IVF (test-tube baby), synthesising and using a gene, DNA vaccines, correcting a defective gene')
d.basic('EFB definition of biotechnology?', '"The integration of ' + T('natural science and organisms, cells, parts thereof, and molecular analogues') + ' for products and services"')
d.basic('Who founded recombinant DNA technology (NCERT profile)?', T('Herbert Boyer') + ' (restriction enzymes, sticky ends) with ' + T('Stanley Cohen') + ' (plasmids)')

# ---------------------------------------------------------------- 9.1 Principles
d.sec('9.1-principles')
d.basic('Two core techniques of modern biotechnology?', T('Genetic engineering') + ' and ' + T('bioprocess engineering'))
d.basic('What is genetic engineering?', 'Altering the chemistry of genetic material (DNA/RNA), introducing it into hosts to ' + T('change the phenotype'))
d.basic('What is bioprocess engineering?', 'Maintaining a ' + T('sterile') + ' ambience so only the desired microbe/cell grows in large quantities (antibiotics, vaccines, enzymes)')
d.basic('Limitation of traditional hybridisation overcome by genetic engineering?', 'Hybridisation carries ' + X('undesirable genes') + ' along; genetic engineering introduces ' + T('only the desired gene(s)'))
d.basic('Why can’t an alien DNA piece multiply in a host on its own?', 'It needs an ' + T('origin of replication') + '; it must be part of a replicating chromosome or vector')
d.basic('What is cloning?', 'Making ' + T('multiple identical copies') + ' of a template DNA')
d.basic('First recombinant DNA: who, when, what?', T('Cohen and Boyer, 1972') + ': linked an antibiotic resistance gene to a native plasmid of ' + EI('Salmonella typhimurium'))
d.basic('What is a plasmid?', 'Autonomously replicating ' + T('circular extra-chromosomal DNA'))
d.basic('Why is a plasmid called a vector?', 'Like a mosquito carries malaria, it ' + T('delivers') + ' an alien piece of DNA into the host')
d.basic('Enzyme joining antibiotic-resistance gene with plasmid?', T('DNA ligase'))
d.basic('What is recombinant DNA?', 'A new combination of circular, autonomously replicating DNA ' + T('created in vitro'))
d.basic('Host used for cloning the first recombinant DNA?', EI('Escherichia coli') + ' (related to Salmonella); used its own DNA polymerase')
d.cloze('Three basic steps in genetically modifying an organism: {{c1::identification of DNA with desirable genes}}; {{c2::introduction of the DNA into the host}}; {{c3::maintenance of DNA in host and transfer to progeny}}.')

# ---------------------------------------------------------------- 9.2 Tools
d.sec('9.2-tools')
d.basic('Key tools of recombinant DNA technology?', T('Restriction enzymes, polymerases, ligases, vectors') + ' and the ' + T('host organism'))
d.sec('9.2.1-restriction-enzymes')
d.basic('When were restriction enzymes found, and why the name?', N('1963') + ': they ' + T('restricted the growth of bacteriophage') + ' in E. coli')
d.basic('Two enzymes isolated in 1963?', 'One ' + T('added methyl groups') + ' to DNA; the other ' + T('cut DNA') + ' (restriction endonuclease)')
d.basic('First restriction endonuclease, and its recognition?', T('Hind II') + ': cuts at a specific ' + N('six base pair') + ' recognition sequence')
d.basic('How many restriction enzymes are known?', 'More than ' + N('900') + ', from over ' + N('230') + ' bacterial strains')
d.basic('Naming convention: EcoRI?', T('E') + ' = genus Escherichia, ' + T('co') + ' = species coli, ' + T('R') + ' = strain RY 13, ' + T('I') + ' = order of isolation')
d.basic('Exonuclease vs endonuclease?', T('Exonuclease') + ': removes nucleotides from the ' + T('ends') + '. ' + T('Endonuclease') + ': cuts at specific positions ' + T('within') + ' DNA.')
d.basic('How does a restriction endonuclease work?', '"Inspects" DNA, binds its specific ' + T('recognition sequence') + ', cuts both strands in the sugar-phosphate backbone')
d.basic('What is a DNA palindrome?', 'Sequence reading the ' + T('same on both strands') + ' when read in the same orientation (5′→3′)')
d.basic('EcoRI recognition sequence?', '5′-' + T('GAATTC') + '-3′ / 3′-CTTAAG-5′')
d.basic('What are sticky ends?', 'Single-stranded overhangs left because the enzyme cuts ' + T('a little away from the centre') + ' of the palindrome; they H-bond with complementary ends')
d.basic('What do sticky ends facilitate?', 'Action of ' + T('DNA ligase'), **fig('fig_9_1_ecori_action'))
d.basic('Why must vector and source DNA be cut by the same enzyme?', 'To get the ' + T('same kind of sticky ends') + ' that can be joined', **fig('fig_9_2_rdna_technology'))
d.basic('Create a palindrome from 5′-GGATCC-3′: is it one? (Exercise 7)', T('Yes') + ': complement read 5′→3′ is also GGATCC (BamHI site)')
d.basic('Do eukaryotic cells have restriction endonucleases? (Exercise 5)', X('No') + ' (typically); they are a bacterial defence against phages, bacterial DNA protected by methylation')
d.basic('Why doesn’t a bacterium cut its own DNA? (intuition)', 'Its own recognition sites are ' + T('methylated') + ' by the partner methylase enzyme')
d.basic('Separation technique for DNA fragments?', T('Gel electrophoresis'))
d.basic('Why does DNA move towards the anode?', 'DNA is ' + T('negatively charged'))
d.basic('Matrix used in electrophoresis?', T('Agarose') + ', a natural polymer from ' + T('sea weeds'))
d.basic('How are fragments separated in agarose?', 'By ' + T('size') + ' through a sieving effect; smaller fragments move ' + T('farther'))
d.basic('How is DNA visualised in the gel?', 'Stain with ' + T('ethidium bromide') + ', expose to ' + T('UV') + ' → bright orange bands', **fig('fig_9_3_gel_electrophoresis'))
d.basic('Read Figure 9.3: where was the sample loaded?', 'At the ' + T('wells') + ' (top); largest fragments near wells, smallest farthest', **img('fig_9_3_gel_electrophoresis'))
d.basic('What is elution?', 'Cutting out DNA bands from the gel and ' + T('extracting') + ' the DNA')
d.sec('9.2.2-cloning-vectors')
d.basic('Why are plasmids and phages useful vectors?', 'They replicate ' + T('independently') + ' of chromosomal DNA; phages have very high copy number; plasmids 1–2 to 15–100 copies')
d.cloze('Features required in a cloning vector: {{c1::origin of replication (ori)}}, {{c2::selectable marker}}, {{c3::cloning sites}}, and for plants/animals, suitable {{c4::vectors}}.')
d.basic('Role of ori?', 'Where replication starts; also controls ' + T('copy number') + ' of linked DNA')
d.basic('What is a selectable marker?', 'Helps identify and eliminate ' + T('non-transformants') + ' and permit transformants to grow')
d.basic('Common selectable markers for E. coli?', 'Resistance to ' + T('ampicillin, chloramphenicol, tetracycline, kanamycin'))
d.basic('What is transformation?', 'Introducing a piece of DNA into a host bacterium')
d.basic('Why should a vector have few (preferably one) recognition sites?', 'Multiple sites generate ' + X('several fragments') + ', complicating cloning')
d.occlusion('Figure 9.4 · pBR322', M + 'fig_9_4_pbr322.webp', PB, [
    ('EcoR I', wbox(172, 52, 306, 90, PB), True), ('Cla I', wbox(366, 44, 462, 80, PB), True),
    ('Hind III', wbox(514, 44, 670, 80, PB), True), ('Pvu I', wbox(144, 142, 250, 178, PB), True),
    ('Pst I', wbox(110, 216, 202, 252, PB), True), ('BamH I', wbox(780, 208, 936, 246, PB), True),
    ('Sal I', wbox(836, 396, 930, 432, PB), True), ('Pvu II', wbox(550, 728, 670, 764, PB), True),
    ('ampᴿ', wbox(330, 280, 442, 318, PB), True), ('tetᴿ', wbox(584, 292, 674, 330, PB), True),
    ('ori', wbox(354, 518, 410, 552, PB), True), ('rop', wbox(492, 552, 562, 592, PB), True)])
d.basic('What does rop code for in pBR322?', 'Proteins involved in ' + T('replication of the plasmid'))
d.basic('Antibiotic resistance genes in pBR322?', T('ampᴿ') + ' and ' + T('tetᴿ'))
d.basic('Insertion at BamH I in pBR322: selection?', 'Recombinants lose ' + X('tetracycline') + ' resistance but keep ampicillin: grow on ampicillin, ' + X('not') + ' on tetracycline; non-recombinants grow on both')
d.basic('What is insertional inactivation?', 'Inserting DNA within a gene (e.g. β-galactosidase) ' + T('inactivates') + ' it')
d.basic('Blue-white selection?', 'With a chromogenic substrate: ' + T('blue') + ' = no insert (β-gal active). ' + T('Colourless (white)') + ' = recombinant.')
d.basic('Why is blue-white better than antibiotic inactivation?', 'Antibiotic method needs ' + X('simultaneous plating') + ' on two plates; blue-white needs one')
d.basic('How can a reporter enzyme monitor transformation? (Exercise 9)', 'Its visible activity (e.g. colour from β-galactosidase) shows which cells took up and express the foreign DNA')
d.basic('Plant vector derived from a pathogen?', T('Ti plasmid') + ' of ' + EI('Agrobacterium tumefaciens') + ', disarmed to deliver genes without causing tumours')
d.basic('What does wild Agrobacterium do?', 'Delivers ' + T('T-DNA') + ' that transforms dicot plant cells into a ' + T('tumour') + ' making chemicals for the pathogen')
d.basic('Animal vectors derived from pathogens?', 'Disarmed ' + T('retroviruses') + ' (which normally make cells cancerous)')
d.basic('Correction: NCERT spells "Agrobacterium tumifaciens". Correct?', EI('Agrobacterium tumefaciens'))
d.sec('9.2.3-competent-host')
d.basic('Why can’t DNA pass through cell membranes?', 'DNA is ' + T('hydrophilic'))
d.basic('How are bacteria made competent?', 'Treat with a specific concentration of a ' + T('divalent cation') + ' such as ' + T('calcium'))
d.basic('Heat-shock method?', 'Incubate cells with rDNA ' + T('on ice') + ' → briefly at ' + N('42 °C') + ' → back on ice')
d.basic('Correction: NCERT prints "420C" for heat shock. Correct?', N('42 °C'))
table_card(d, 'Gene transfer', 'Method?', [
    ('Micro-injection', 'rDNA injected directly into nucleus of animal cell', False),
    ('Biolistics (gene gun)', 'Plant cells bombarded with gold/tungsten particles coated with DNA', False),
    ('Disarmed pathogen vectors', 'Infect the cell and transfer rDNA', False),
    ('Heat shock (Ca²⁺)', 'Competent bacteria take up plasmid', False)], term='Methods of introducing DNA into hosts')

# ---------------------------------------------------------------- 9.3 Processes
d.sec('9.3-processes')
d.cloze('Steps of rDNA technology: isolation of DNA → {{c1::fragmentation by restriction endonucleases}} → isolation of desired fragment → {{c2::ligation into a vector}} → {{c3::transfer into host}} → culturing at large scale → {{c4::extraction of product}}.')
d.sec('9.3.1-isolation')
d.basic('Why must DNA be pure before cutting?', 'Restriction enzymes need DNA ' + T('free from other macromolecules'))
table_card(d, 'Breaking cells', 'Enzyme?', [
    ('Bacteria', 'Lysozyme', False), ('Plant cells', 'Cellulase', False), ('Fungus', 'Chitinase', False)], term='Enzymes to release DNA')
d.basic('How are RNA and proteins removed?', 'RNA by ' + T('ribonuclease') + '; proteins by ' + T('protease'))
d.basic('How is purified DNA finally precipitated?', 'By adding ' + T('chilled ethanol') + '; seen as fine threads removed by ' + T('spooling'), **fig('fig_9_5_dna_spooling'))
d.basic('What is chitinase? (Exercise 11c)', 'Enzyme that breaks ' + T('chitin') + ' of fungal cell walls to release DNA')
d.sec('9.3.2-cutting')
d.basic('How is progress of restriction digestion checked?', T('Agarose gel electrophoresis'))
d.basic('How is recombinant DNA prepared after cutting?', 'Mix cut gene of interest with cut vector and add ' + T('ligase'))
d.sec('9.3.3-pcr')
d.basic('What does PCR stand for?', T('Polymerase Chain Reaction'))
d.basic('What are primers?', 'Small chemically synthesised ' + T('oligonucleotides') + ' complementary to regions of DNA')
d.cloze('Each PCR cycle: {{c1::denaturation}} (heat) → {{c2::annealing}} of primers → {{c3::extension}} by DNA polymerase.')
d.occlusion('Figure 9.6 · PCR', M + 'fig_9_6_pcr.webp', PC, [
    ('Denaturation', wbox(742, 120, 878, 144, PC), True), ('Annealing', wbox(742, 222, 846, 246, PC), True),
    ('Extension', wbox(742, 452, 846, 476, PC), True), ('Primers', wbox(636, 224, 716, 246, PC), True),
    ('DNA polymerase (Taq) + deoxynucleotides', wbox(408, 326, 594, 388, PC)), ('30 cycles', wbox(406, 548, 502, 570, PC), True),
    ('Amplified ~1 billion times', wbox(576, 646, 746, 688, PC), True)])
d.basic('Thermostable polymerase in PCR and source?', T('Taq polymerase') + ' from ' + EI('Thermus aquaticus'))
d.basic('Why is a thermostable polymerase essential?', 'It stays ' + T('active') + ' during the high-temperature denaturation step, so it needn’t be re-added each cycle')
d.basic('Amplification by PCR?', 'About ' + N('1 billion') + ' copies (≈ 30 cycles, since \\( 2^{30} \\approx 10^9 \\))')
d.basic('Why does 30 cycles give ~a billion copies? (intuition)', 'Copies ' + T('double') + ' every cycle: \\( 2^{10} \\approx 1000 \\), so \\( 2^{30} \\approx 1000^3 = 10^9 \\)')
d.sec('9.3.4-insertion')
d.basic('How are transformants selected with an ampicillin marker?', 'Spread on ampicillin plates: only ' + T('transformants') + ' grow; untransformed cells die')
d.sec('9.3.5-product')
d.basic('What is a recombinant protein?', 'Protein from a gene expressed in a ' + T('heterologous host'))
d.basic('What is a continuous culture system?', 'Used medium drained from one side, fresh added from the other: cells kept in ' + T('log/exponential phase') + ' → more biomass and yield')
d.basic('What are bioreactors?', 'Vessels where raw materials are biologically converted into products using microbial, plant, animal or human cells; ' + N('100–1000 L'))
d.basic('Optimum conditions provided by a bioreactor?', 'Temperature, pH, substrate, salts, vitamins, oxygen')
d.basic('Most common bioreactors?', T('Stirred-tank') + ' type: cylindrical or curved base for mixing', **fig('fig_9_7_bioreactors'))
d.basic('Components of a stirred-tank bioreactor?', 'Agitator, oxygen delivery, foam control, temperature control, pH control, sampling ports')
d.basic('Simple vs sparged stirred-tank bioreactor?', T('Sparged') + ': sterile air bubbles increase the ' + T('oxygen transfer area'), **img('fig_9_7_bioreactors'))
d.basic('Advantages of stirred tank over shake flask (Exercise 6)?', 'Large volumes, controlled ' + T('temperature, pH, foam') + ', sampling, continuous culture and sterile operation')
d.sec('9.3.6-downstream')
d.basic('What is downstream processing?', T('Separation and purification') + ' of the product after biosynthesis')
d.basic('Steps after purification before marketing?', 'Formulation with ' + T('preservatives') + ', ' + T('clinical trials') + ' (for drugs) and strict ' + T('quality control'))

# ---------------------------------------------------------------- summary
d.sec('summary')
table_card(d, 'Tools', 'Role?', [
    ('Restriction endonuclease', 'Molecular scissors', False), ('DNA ligase', 'Molecular glue', False),
    ('Plasmid / phage', 'Vector (vehicle)', False), ('Taq polymerase', 'Amplifies DNA in PCR', False),
    ('Agarose gel', 'Separates DNA by size', False), ('Ethidium bromide + UV', 'Visualises DNA', False)], term='Tools of genetic engineering')
table_card(d, 'Exercise 12', 'Difference?', [
    ('Plasmid vs chromosomal DNA', 'Small, circular, extra-chromosomal, self-replicating vs main genome', False),
    ('Exonuclease vs endonuclease', 'Cuts from ends vs cuts within', False),
    ('RNA vs DNA', 'Ribose, uracil, usually single-stranded vs deoxyribose, thymine, double', False)], term='Distinguish (Exercise 12)')

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
