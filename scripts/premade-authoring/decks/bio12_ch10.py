import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Biology', 'class12-biology-ch10-biotechnology-and-its-applications')
d = Deck('Chapter 10: Biotechnology and its Applications', 'Class 12', ['class-12', 'biology', 'ch-10'])
d.description = 'Tissue culture, GM crops, Bt cotton, RNAi, recombinant insulin, gene therapy, molecular diagnosis, transgenic animals and biopiracy'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}
PI = (1001, 834)

# ---------------------------------------------------------------- intro
d.sec('10.0-intro')
d.basic('Applications of biotechnology?', 'Therapeutics, diagnostics, GM crops, processed food, bioremediation, waste treatment, energy production')
d.cloze('Three critical research areas of biotechnology: best {{c1::catalyst}} (improved organism or pure enzyme); optimal {{c2::conditions}} through engineering; {{c3::downstream processing}} to purify the product.')

# ---------------------------------------------------------------- 10.1 Agriculture
d.sec('10.1-agriculture')
d.basic('Three options to increase food production?', T('Agro-chemical') + ' based, ' + T('organic') + ', and ' + T('genetically engineered crop') + '-based agriculture')
d.basic('Achievement and limit of the Green Revolution?', 'Tripled food supply, but ' + X('not enough') + ' for the growing population; agrochemicals too costly for poor farmers')
d.basic('What is an explant?', 'Any part of a plant taken out and grown in a test tube under ' + T('sterile') + ' conditions')
d.basic('What is totipotency?', 'Capacity to generate a ' + T('whole plant') + ' from any cell/explant')
d.basic('Components of a plant tissue culture medium (Exercise 3)?', 'Carbon source (' + T('sucrose') + '), inorganic salts, vitamins, amino acids, growth regulators (' + T('auxins, cytokinins') + ')')
d.basic('What is micropropagation?', 'Producing ' + T('thousands of plants') + ' in a short time through tissue culture')
d.basic('What are somaclones?', 'Plants from tissue culture, ' + T('genetically identical') + ' to the original plant')
d.basic('Advantage of micropropagation (Exercise 2)?', 'Many ' + T('genetically identical') + ' plants quickly, all year round; e.g. ' + E('tomato, banana, apple'))
d.basic('Which part is used for virus-free plants and why? (Exercise 1)', T('Meristem') + ' (apical and axillary): it is ' + T('free of virus') + ' even in an infected plant')
d.basic('Crops recovered virus-free by meristem culture?', E('Banana, sugarcane, potato'))
d.basic('What are protoplasts?', 'Naked plant cells after ' + T('digesting the cell wall') + ', surrounded by plasma membrane')
d.basic('What is somatic hybridisation?', 'Fusing protoplasts of two varieties with desirable characters to grow a ' + T('somatic hybrid'))
d.basic('Example of somatic hybrid and its drawback?', T('Pomato') + ' (tomato + potato); ' + X('lacked') + ' the desired combination for commercial use')
d.basic('What are GMOs?', 'Plants, bacteria, fungi and animals whose ' + T('genes have been altered') + ' by manipulation')
d.cloze('Benefits of GM plants: tolerance to {{c1::abiotic stresses}}; less reliance on {{c2::chemical pesticides}}; reduced {{c3::post-harvest losses}}; better {{c4::mineral usage}}; enhanced {{c5::nutritional value}}.')
d.basic('What is golden rice?', T('Vitamin A') + ' (β-carotene) enriched rice')
d.basic('Update: status of golden rice?', 'Approved for commercial cultivation in the ' + T('Philippines') + ' (2021), the first country to do so')
d.basic('Industrial use of tailor-made GM plants?', 'Alternative resources: ' + T('starches, fuels, pharmaceuticals'))
d.basic('Source of Bt toxin?', 'Bacterium ' + EI('Bacillus thuringiensis'))
d.basic('Examples of Bt crops?', E('Bt cotton, Bt corn, rice, tomato, potato, soyabean'))
d.basic('Insects killed by Bt proteins?', T('Lepidopterans') + ' (tobacco budworm, armyworm), ' + T('coleopterans') + ' (beetles), ' + T('dipterans') + ' (flies, mosquitoes)')
d.basic('Form of Bt toxin in the bacterium?', 'Protein ' + T('crystals') + ' of inactive ' + T('protoxin'))
d.basic('Why doesn’t Bt toxin kill the bacterium? (Exercise 4)', 'It is an ' + T('inactive protoxin') + ' in the bacterium (option c)')
d.basic('How is the Bt protoxin activated?', T('Alkaline pH') + ' of the insect gut solubilises crystals → active toxin')
d.basic('How does active Bt toxin kill insects?', 'Binds midgut epithelial cells, ' + T('creates pores') + ' → cell swelling and lysis → death')
d.basic('Mnemonic for Bt action?', '"' + T('Eat, Alkali, Activate, Pore, Pop') + '": eaten protoxin → alkaline gut → active toxin → pores → lysis')
d.basic('Name of Bt toxin genes?', T('cry') + ' genes; proteins are Cry proteins')
table_card(d, 'cry genes', 'Controls?', [
    ('cryIAc and cryIIAb', 'Cotton bollworms', False), ('cryIAb', 'Corn borer', False)], term='cry genes and target pests')
d.basic('What are Cry proteins, who makes them and use? (Exercise 7)', 'Insecticidal proteins of ' + EI('Bacillus thuringiensis') + '; genes put into crops (Bt cotton) as biopesticide')
d.basic('Why are different cry genes used for different crops?', 'Most Bt toxins are ' + T('insect-group specific') + '; choice depends on crop and target pest')
d.basic('Cotton boll (Figure 10.1): (a) vs (b)?', '(a) ' + X('destroyed by bollworms') + '; (b) fully mature boll', **img('fig_10_1_cotton_boll'))
d.basic('Nematode infecting tobacco roots?', EI('Meloidogyne incognita'))
d.basic('Correction: NCERT spells it "Meloidegyne incognitia". Correct?', EI('Meloidogyne incognita') + ' (root-knot nematode)')
d.basic('What is RNA interference (RNAi)?', 'Silencing of a specific ' + T('mRNA') + ' by a complementary ' + T('dsRNA') + ' that prevents its translation.<br>A cellular defence in all eukaryotes')
d.basic('Natural sources of dsRNA for RNAi?', 'Viruses with RNA genomes, or ' + T('transposons') + ' replicating via RNA')
d.basic('How was tobacco made nematode-resistant?', 'Nematode-specific genes introduced via ' + T('Agrobacterium') + '<br>make ' + T('sense and antisense RNA') + '<br>→ dsRNA<br>→ RNAi silences the nematode’s mRNA', **fig('fig_10_2_rnai_roots'))
d.basic('Figure 10.2: (a) vs (b) roots?', '(a) Control plant roots infested; (b) ' + T('transgenic') + ' roots protected 5 days after infection', **img('fig_10_2_rnai_roots'))
d.basic('Why does sense + antisense RNA silence a gene? (intuition)', 'They pair into dsRNA, which the cell treats as an ' + T('invader') + ' and uses as a guide to destroy matching mRNA')
d.basic('Advantages vs disadvantages of GM crops (Exercise 6)?', T('Pros') + ': higher yield, pest resistance, less pesticide, nutrition<br>' + T('Cons') + ': possible ecological harm, resistant pests, gene flow to weeds, allergy concerns, biopiracy/patents')

# ---------------------------------------------------------------- 10.2 Medicine
d.sec('10.2-medicine')
d.basic('Advantage of recombinant therapeutics?', 'Safe, effective, mass-produced; ' + X('no unwanted immune responses') + ' unlike products from non-human sources')
d.basic('Recombinant therapeutics approved (NCERT)?', 'About ' + N('30') + ' worldwide; ' + N('12') + ' marketed in India')
d.basic('Update: are there still only ~30 recombinant therapeutics?', X('No') + '; hundreds of biopharmaceuticals (insulin analogues, antibodies, vaccines) are now approved; NCERT’s figure is dated')
d.sec('10.2.1-insulin')
d.basic('Earlier source of insulin and its problem?', 'Pancreas of slaughtered ' + T('cattle and pigs') + '; caused ' + X('allergy') + ' in some patients')
d.basic('Structure of insulin?', 'Two short chains, ' + T('A and B') + ', linked by ' + T('disulphide bridges'))
d.basic('What is proinsulin?', 'Pro-hormone with an extra ' + T('C peptide') + ', removed during maturation', **fig('fig_10_3_proinsulin'))
d.occlusion('Figure 10.3 · Maturation of proinsulin', M + 'fig_10_3_proinsulin.webp', PI, [
    ('Proinsulin', wbox(325, 110, 595, 170, PI), True), ('A peptide', wbox(545, 390, 800, 445, PI), True),
    ('Insulin', wbox(520, 512, 715, 570, PI), True), ('B peptide', wbox(520, 598, 780, 655, PI), True),
    ('Free C peptide', wbox(278, 742, 650, 797, PI), True)])
d.basic('Main challenge of rDNA insulin?', 'Getting insulin ' + T('assembled into mature form'))
d.basic('How did Eli Lilly make human insulin (1983)?', 'Two DNA sequences for chains ' + T('A and B') + ' put into ' + T('E. coli plasmids') + '.<br>Chains made separately, extracted and joined by disulphide bonds')
d.basic('Why can’t insulin be taken orally?', 'It is a protein; ' + X('digested') + ' by proteases in the gut')
d.basic('Transgenic bacteria example (Exercise 5)?', EI('E. coli') + ' carrying human insulin A/B chain genes, producing human insulin')
d.sec('10.2.2-gene-therapy')
d.basic('What is gene therapy?', 'Methods to correct a diagnosed gene defect by inserting ' + T('normal genes') + ' into a person’s cells/tissues')
d.basic('First clinical gene therapy?', N('1990') + ', a ' + N('4-year-old') + ' girl with ' + T('ADA deficiency'))
d.basic('What is ADA and cause of its deficiency?', T('Adenosine deaminase') + ', crucial for the immune system; deficiency due to ' + T('deletion') + ' of the ADA gene')
d.basic('Non-gene treatments for ADA deficiency?', T('Bone marrow transplantation') + ' and ' + T('enzyme replacement therapy') + '; ' + X('not completely curative'))
d.basic('Steps of ADA gene therapy?', 'Patient’s ' + T('lymphocytes') + ' cultured → functional ADA ' + T('cDNA') + ' introduced via ' + T('retroviral vector') + ' → returned to patient')
d.basic('Why periodic infusions in ADA gene therapy?', 'Engineered lymphocytes are ' + X('not immortal'))
d.basic('Permanent cure for ADA deficiency?', 'Introduce the ADA gene into cells at ' + T('early embryonic stages'))
d.basic('Update: gene-based therapies today?', 'CRISPR therapy ' + T('Casgevy') + ' approved (2023) for sickle-cell disease and β-thalassaemia')
d.sec('10.2.3-molecular-diagnosis')
d.basic('Why is conventional diagnosis not early?', 'Pathogen suspected only after symptoms, when its concentration is already high')
d.basic('Techniques for early diagnosis?', T('rDNA technology, PCR, ELISA'))
d.basic('How does PCR detect low amounts of pathogen?', 'Amplifies the pathogen’s ' + T('nucleic acid') + ' to detectable levels before symptoms')
d.basic('Uses of PCR in diagnosis?', 'Detect ' + T('HIV') + ' in suspected AIDS patients; mutations in suspected ' + T('cancer') + ' patients; genetic disorders')
d.basic('How does a radioactive probe detect a mutated gene?', 'Probe hybridises to its complementary DNA; clone with the mutated gene ' + X('does not appear') + ' on autoradiography')
d.basic('Principle of ELISA?', T('Antigen–antibody interaction') + ': detects pathogen antigens or antibodies made against it')

# ---------------------------------------------------------------- 10.3 Transgenic animals
d.sec('10.3-transgenic-animals')
d.basic('What are transgenic animals?', 'Animals with DNA manipulated to possess and express an ' + T('extra (foreign) gene'))
d.basic('Most common transgenic animals?', T('Mice') + ' (over ' + N('95%') + '); also rats, rabbits, pigs, sheep, cows, fish')
table_card(d, 'Transgenic animals', 'Use / example?', [
    ('Normal physiology', 'Insulin-like growth factor studies', False),
    ('Study of disease', 'Models for cancer, cystic fibrosis, rheumatoid arthritis, Alzheimer’s', False),
    ('Biological products', 'α-1-antitrypsin for emphysema; Rosie’s milk', False),
    ('Vaccine safety', 'Polio vaccine testing in mice', False),
    ('Chemical safety', 'Toxicity testing, faster results', False)], term='Why transgenic animals are made')
d.basic('Human protein from transgenic animals to treat emphysema?', T('α-1-antitrypsin'))
d.basic('First transgenic cow and its product?', T('Rosie') + ' (' + N('1997') + '): milk with human ' + T('alpha-lactalbumin') + ' (' + N('2.4 g/L') + '), more balanced for babies')
d.basic('How could transgenic mice help polio vaccine testing?', 'Test vaccine safety and could ' + T('replace monkeys'))
d.basic('Why are transgenic animals used in toxicity testing?', 'Carry genes making them ' + T('more sensitive') + ' to toxins → quicker results')

# ---------------------------------------------------------------- 10.4 Ethics
d.sec('10.4-ethical-issues')
d.basic('Why are ethical standards needed for GM?', 'GM organisms can have ' + X('unpredictable results') + ' in ecosystems; manipulation needs regulation')
d.basic('Indian body regulating GM research and release?', T('GEAC') + ' (Genetic Engineering Approval Committee)')
d.basic('Update: current name of GEAC?', T('Genetic Engineering Appraisal Committee') + ' (renamed in 2010), under the Ministry of Environment')
d.basic('Varieties of rice in India?', 'About ' + N('2,00,000') + '; ' + N('27') + ' documented Basmati varieties')
d.basic('Basmati patent controversy?', 'In ' + N('1997') + ' an American company got a US patent on Basmati derived from Indian farmers’ varieties crossed with semi-dwarf varieties')
d.basic('Other Indian resources targeted for patents?', 'Traditional herbal medicines: ' + E('turmeric, neem'))
d.basic('Define biopiracy.', 'Use of bio-resources by multinational companies/organisations ' + X('without authorisation') + ' and ' + X('without compensatory payment'))
d.basic('Why is biopiracy one-sided?', 'Industrialised nations are rich financially but ' + T('poor in biodiversity') + '.<br>Developing nations are rich in biodiversity and traditional knowledge')
d.basic('India’s legal response to biopiracy?', 'Second amendment of the ' + T('Indian Patents Bill'))

# ---------------------------------------------------------------- summary
d.sec('summary')
table_card(d, 'Techniques', 'Used for?', [
    ('Micropropagation', 'Many identical plants fast', False), ('Meristem culture', 'Virus-free plants', False),
    ('Somatic hybridisation', 'Pomato', False), ('Bt genes', 'Insect-resistant crops', False),
    ('RNAi', 'Nematode-resistant tobacco', False), ('rDNA insulin', 'Human insulin in E. coli', False)], term='Applications of biotechnology')
d.basic('Can oil be removed from seeds using rDNA? (Exercise 10)', 'Silence/knock out genes for ' + T('oil (fatty acid) synthesis') + ' e.g. by RNAi, so seeds store little oil')
d.basic('Does our blood have proteases and nucleases? (Exercise 12)', T('Yes') + '; that is why naked DNA/protein drugs are degraded and need protection')

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
