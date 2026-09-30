import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch12-respiration-in-plants')
d = Deck('Chapter 12: Respiration in Plants', 'Class 11', ['class-11', 'biology', 'ch-12'])
d.description = 'Gas exchange in plants, glycolysis, fermentation, Krebs cycle, ETS, ATP balance sheet, amphibolic pathway, RQ'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}
G, K = (563, 1001), (1001, 938)

# ---------------------------------------------------------------- Intro
d.sec('12.0-intro')
d.basic('What is respiration?', 'Breaking of ' + T('C–C bonds') + ' of complex compounds by oxidation within cells, releasing considerable energy')
d.basic('What are respiratory substrates?', 'Compounds oxidised during respiration; usually ' + T('carbohydrates') + ', but also proteins, fats and organic acids')
d.basic('Most common respiratory substrate?', T('Glucose') + ' (carbohydrates)')
d.basic('Why is energy released step by step, not all at once?', 'So that small packets can be trapped as ' + T('ATP') + ' instead of being lost as heat; each step is enzyme-controlled')
d.basic('Why is ATP called the energy currency of the cell?', 'Energy from respiration is stored in ATP, which is broken down ' + T('whenever and wherever') + ' energy is needed')
d.basic('Besides ATP, what else does respiration provide?', T('Carbon skeletons') + ' used as precursors for biosynthesis')
d.basic('Where does respiration occur in eukaryotic cells?', 'In the ' + T('cytoplasm') + ' (glycolysis) and ' + T('mitochondria'))
d.basic('Why do non-green plant parts need food translocated to them?', 'Only chloroplast-containing (usually superficial) cells photosynthesise.<br>All other cells must oxidise food for energy')

# ---------------------------------------------------------------- 12.1 Do plants breathe
d.sec('12.1-do-plants-breathe')
d.basic('How do plants exchange gases without respiratory organs?', 'Through ' + T('stomata') + ' and ' + T('lenticels'))
d.basic('Three reasons plants manage without respiratory organs?', '(1) Each part handles its ' + T('own gas exchange') + '. (2) Plants have ' + T('low demands') + ' (respire slowly). (3) Gases diffuse only ' + T('short distances') + ': living cells are near the surface.')
d.basic('How do cells deep in woody stems get air?', 'Living cells are in thin layers beneath the bark with ' + T('lenticels') + '; interior cells are ' + T('dead') + ' (support only)')
d.basic('What helps air reach cells inside leaves, stems and roots?', 'Loosely packed ' + T('parenchyma') + ' forming an interconnected network of air spaces')
d.basic('Why don\'t photosynthesising cells lack O₂?', 'O₂ is ' + T('released within') + ' the cell itself')
d.basic('Complete combustion of glucose?', 'C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + energy (mostly heat)')
d.basic('Respiration vs combustion?', 'Combustion: one step, energy lost as ' + T('heat') + '. Respiration: many enzyme steps, energy trapped as ' + T('ATP') + '.')
d.basic('What did the first cells on earth likely use for energy?', 'Anaerobic pathways: the early atmosphere ' + X('lacked oxygen'))
d.basic('Facultative vs obligate anaerobes?', 'Facultative: can live with or without O₂. Obligate: ' + T('require') + ' anaerobic conditions.')
d.basic('What machinery do all living organisms retain?', 'Enzymes to partially oxidise glucose ' + T('without O₂') + ': glycolysis')

# ---------------------------------------------------------------- 12.2 Glycolysis
d.sec('12.2-glycolysis')
d.basic('Meaning of "glycolysis"?', 'Greek ' + I('glycos') + ' = sugar, ' + I('lysis') + ' = splitting')
d.basic('Who gave the scheme of glycolysis?', T('Embden, Meyerhof and Parnas') + ': the EMP pathway')
d.basic('Where does glycolysis occur?', 'In the ' + T('cytoplasm') + ', in all living organisms')
d.basic('In which organisms is glycolysis the only process of respiration?', T('Anaerobic') + ' organisms')
d.basic('End product of glycolysis?', T('Two') + ' molecules of ' + T('pyruvic acid') + ' (partial oxidation of glucose)')
d.basic('Source of glucose for glycolysis in plants?', T('Sucrose') + ' (end product of photosynthesis) or storage carbohydrates')
d.basic('Which enzyme converts sucrose to glucose and fructose?', T('Invertase'))
d.basic('Which enzyme phosphorylates glucose to glucose-6-phosphate?', T('Hexokinase'))
d.basic('Correction: NCERT says glucose and fructose are both phosphorylated "to glucose-6-phosphate". What is precise?', 'Hexokinase makes ' + T('glucose-6-phosphate') + ' from glucose<br>and ' + T('fructose-6-phosphate') + ' from fructose.<br>Both then follow the same path')
d.basic('How many reactions in glycolysis?', 'A chain of ' + N('ten') + ' enzyme-controlled reactions')
d.basic('At which two steps is ATP used in glycolysis?', 'Glucose → ' + T('glucose-6-phosphate') + '; fructose-6-phosphate → ' + T('fructose-1,6-bisphosphate'))
d.basic('Fructose-1,6-bisphosphate splits into?', T('Dihydroxyacetone phosphate (DHAP)') + ' and ' + T('3-phosphoglyceraldehyde (PGAL)'))
d.basic('At which step is NADH + H⁺ formed in glycolysis?', T('PGAL → 1,3-bisphosphoglycerate (BPGA)') + ': PGAL is oxidised and takes up Pi')
d.basic('At which steps is ATP made in glycolysis?', T('BPGA → 3-PGA') + ' and ' + T('PEP → pyruvic acid'))
d.basic('ATP count in glycolysis per glucose?', 'Used: ' + N('2') + '. Made: ' + N('4') + ' (2 steps × 2 trioses). Net: ' + N('2 ATP') + ', plus ' + N('2 NADH') + '.')
d.cloze('Glycolysis: glucose → {{c1::glucose-6-phosphate}} → {{c2::fructose-6-phosphate}} → {{c3::fructose-1,6-bisphosphate}} → PGAL + DHAP → {{c4::1,3-BPGA}} → {{c5::3-PGA}} → 2-PGA → {{c6::PEP}} → pyruvic acid.')
d.basic('Which step of glycolysis releases water?', T('2-phosphoglycerate → PEP'))
d.occlusion('Figure 12.1 · Steps of glycolysis', M + 'fig_12_1_glycolysis.webp', G, [
    ('Glucose-6-phosphate', wbox(45, 91, 244, 110, G, 4), True), ('Fructose-6-phosphate', wbox(48, 170, 254, 189, G, 4), True),
    ('Fructose-1,6-bisphosphate', wbox(32, 252, 286, 271, G, 4), True),
    ('PGAL (glyceraldehyde-3-phosphate)', wbox(18, 334, 277, 376, G, 4), True), ('DHAP (dihydroxyacetone phosphate)', wbox(349, 327, 529, 391, G, 4), True),
    ('1,3-bisphosphoglyceric acid', wbox(20, 456, 295, 497, G, 4), True), ('3-phosphoglyceric acid', wbox(37, 586, 264, 627, G, 4), True),
    ('2-phosphoglycerate', wbox(76, 723, 252, 742, G, 4), True), ('Phosphoenolpyruvate', wbox(76, 830, 270, 849, G, 4), True),
    ('Pyruvic acid', wbox(104, 928, 214, 947, G, 4), True)], guess='hide-one')
d.basic('Three fates of pyruvic acid?', T('Lactic acid fermentation') + ', ' + T('alcoholic fermentation') + ', ' + T('aerobic respiration'))

# ---------------------------------------------------------------- 12.3 Fermentation
d.sec('12.3-fermentation')
d.basic('What happens in alcoholic fermentation (yeast)?', 'Pyruvic acid → ' + T('CO₂ + ethanol') + ' under anaerobic conditions', **fig('fig_12_2_fermentation'))
d.basic('Two enzymes of alcoholic fermentation?', T('Pyruvic acid decarboxylase') + ' and ' + T('alcohol dehydrogenase'))
d.basic('Which enzyme reduces pyruvic acid to lactic acid?', T('Lactate dehydrogenase'))
d.basic('When do animal muscles make lactic acid?', 'During exercise, when ' + T('O₂ is inadequate'))
d.basic('What is the reducing agent in fermentation?', T('NADH + H⁺') + ', reoxidised to NAD⁺')
d.basic('Why is regenerating NAD⁺ the real purpose of fermentation?', 'Glycolysis needs NAD⁺ at the PGAL step.<br>Without O₂, turning pyruvate into lactate or ethanol is the only way to ' + T('recycle NADH') + ' so glycolysis keeps making ATP')
d.basic('How much of glucose\'s energy does fermentation release?', 'Less than ' + N('7%') + ', and not all of it is trapped as ATP')
d.basic('Net ATP from fermentation of one glucose?', N('2 ATP') + ' (from glycolysis)')
d.basic('Why is fermentation hazardous?', 'It produces ' + T('acid or alcohol'))
d.basic('At what alcohol concentration do yeasts poison themselves?', 'About ' + N('13%'))
d.basic('How are drinks stronger than 13% alcohol made?', T('Distillation') + ' of the fermented liquid')
d.basic('Where does fermentation occur?', 'In many ' + T('prokaryotes') + ', ' + T('unicellular eukaryotes') + ' and ' + T('germinating seeds'))
d.basic('Fermentation vs aerobic respiration?', 'Fermentation: ' + T('partial') + ' breakdown, net ' + N('2 ATP') + ', NADH oxidised slowly. Aerobic: ' + T('complete') + ' to CO₂ + H₂O, many ATP, NADH oxidised vigorously.')

# ---------------------------------------------------------------- 12.4 Aerobic respiration
d.sec('12.4-aerobic')
d.basic('What is aerobic respiration?', 'Complete oxidation of organic substances in the presence of ' + T('O₂') + ', releasing CO₂, water and much energy')
d.basic('Two crucial events of aerobic respiration, and where?', '(1) Complete oxidation of pyruvate by removing H atoms, leaving 3 CO₂: ' + T('matrix') + '<br>(2) Passing electrons to O₂ with ATP synthesis: ' + T('inner membrane'))
d.basic('What happens to pyruvate in the mitochondrial matrix?', T('Oxidative decarboxylation') + ' to acetyl CoA, by ' + T('pyruvic dehydrogenase'))
d.basic('Link reaction equation?', 'Pyruvic acid + CoA + NAD⁺ → acetyl CoA + CO₂ + NADH + H⁺ (Mg²⁺, pyruvate dehydrogenase)')
d.basic('Coenzymes needed by pyruvate dehydrogenase?', T('NAD⁺') + ' and ' + T('coenzyme A') + ' (and Mg²⁺)')
d.basic('NADH from the link reaction per glucose?', N('2'))

d.sec('12.4.1-krebs')
d.basic('Other names of the Krebs cycle?', T('Tricarboxylic acid (TCA) cycle') + ', citric acid cycle')
d.basic('First step of the Krebs cycle?', 'Acetyl group + ' + T('OAA') + ' + water → ' + T('citric acid') + ', by ' + T('citrate synthase') + '; CoA released')
d.basic('After citrate, what happens?', 'Isomerised to ' + T('isocitrate') + ', then two decarboxylations → ' + T('α-ketoglutaric acid') + ' → ' + T('succinyl-CoA'))
d.basic('Where is GTP made in the Krebs cycle?', T('Succinyl-CoA → succinic acid') + ': substrate-level phosphorylation')
d.basic('What is substrate-level phosphorylation?', 'ATP (or GTP) made directly from a ' + T('substrate') + ' in a reaction, not through the ETS')
d.basic('What happens to the GTP?', 'GTP → GDP, coupled with ' + T('ADP → ATP'))
d.basic('How many NADH and FADH₂ points in one turn of the Krebs cycle?', N('3') + ' NAD⁺ → NADH; ' + N('1') + ' FAD → FADH₂')
d.basic('What must be replenished for the Krebs cycle to continue?', T('Oxaloacetic acid') + ', plus NAD⁺ and FAD regenerated from NADH and FADH₂')
d.basic('Krebs cycle summary equation (per pyruvate)?', 'Pyruvic acid + 4NAD⁺ + FAD + 2H₂O + ADP + Pi → 3CO₂ + 4NADH + 4H⁺ + FADH₂ + ATP')
d.basic('Totals up to the end of the Krebs cycle (per glucose)?', N('8 NADH') + ' (from link + Krebs), ' + N('2 FADH₂') + ', ' + N('2 ATP') + ' in TCA; plus glycolysis\'s 2 NADH and 2 ATP')
d.basic('Carbon count through the cycle?', 'Acetyl CoA (' + N('2C') + ') + OAA (' + N('4C') + ') → citric acid (' + N('6C') + ') → α-ketoglutaric (' + N('5C') + ') → succinic, malic, OAA (' + N('4C') + ')')
d.basic('Note on "FAD⁺" in NCERT?', 'FAD carries no charge. It is written ' + T('FAD') + ' → FADH₂ (NAD⁺ does carry a charge).')
d.occlusion('Figure 12.3 · Citric acid cycle', M + 'fig_12_3_krebs.webp', K, [
    ('Acetyl coenzyme A (2C)', wbox(331, 210, 641, 284, K), True), ('Citric acid (6C)', wbox(553, 415, 726, 482, K), True),
    ('Oxaloacetic acid (4C)', wbox(179, 382, 453, 449, K), True), ('α-ketoglutaric acid (5C)', wbox(620, 570, 934, 652, K), True),
    ('Succinic acid (4C)', wbox(373, 833, 596, 907, K), True), ('Malic acid (4C)', wbox(123, 624, 293, 698, K), True),
    ('GTP', wbox(720, 890, 788, 924, K), True), ('FADH₂', wbox(69, 768, 182, 806, K), True)], guess='hide-one')
d.basic('Why are O₂ and big ATP yields still missing after the Krebs cycle?', 'The energy is held in ' + T('NADH and FADH₂') + '.<br>It is released only when they are oxidised through the ETS, with O₂ as the final acceptor')

d.sec('12.4.2-ets')
d.basic('Where is the ETS located?', 'In the ' + T('inner mitochondrial membrane'))
d.cloze('ETS complexes: I = {{c1::NADH dehydrogenase}}; II = {{c2::succinate dehydrogenase (FADH₂)}}; III = {{c3::cytochrome bc₁}}; IV = {{c4::cytochrome c oxidase}}; V = {{c5::ATP synthase}}.')
d.basic('Where do electrons from NADH go first?', 'Complex I (' + T('NADH dehydrogenase') + ') → ' + T('ubiquinone'))
d.basic('How does FADH₂ enter the ETS?', 'Via ' + T('complex II') + ' to ubiquinone (it bypasses complex I)')
d.basic('Reduced ubiquinone is called?', T('Ubiquinol'))
d.basic('What is cytochrome c?', 'A small protein on the outer surface of the inner membrane; a ' + T('mobile carrier') + ' between complex III and IV')
d.basic('What does complex IV contain?', 'Cytochromes ' + T('a and a₃') + ' and ' + T('two copper centres'))
d.basic('Mobile carriers of the ETS?', T('Ubiquinone') + ' (in the membrane) and ' + T('cytochrome c'), **fig('fig_12_4_ets'))
d.basic('ATP per NADH and per FADH₂ (NCERT)?', 'NADH: ' + N('3 ATP') + '. FADH₂: ' + N('2 ATP') + '.')
d.basic('Why does FADH₂ give fewer ATP than NADH?', 'It enters at complex II, ' + T('skipping complex I') + ', so fewer protons are pumped')
d.basic('Role of O₂ in aerobic respiration?', T('Final hydrogen (electron) acceptor') + ', forming water; it drives the whole process by removing hydrogen')
d.basic('Why is it called oxidative phosphorylation?', 'The proton gradient is made with energy from ' + T('oxidation-reduction') + ' (vs light energy in photophosphorylation)')
d.basic('ATP synthase in mitochondria: F₁ vs F₀?', T('F₁') + ': peripheral headpiece with the ATP-making site. ' + T('F₀') + ': integral membrane channel for protons.', **fig('fig_12_5_atp_synthase'))
d.basic('How many H⁺ pass through F₀ per ATP?', N('4 H⁺') + ', from intermembrane space to matrix')
d.basic('Direction of proton flow through mitochondrial ATP synthase?', 'Intermembrane space → ' + T('matrix'))
d.basic('Chloroplast vs mitochondrion: where do protons pile up?', 'Chloroplast: thylakoid ' + T('lumen') + ' (CF₀–CF₁). Mitochondrion: ' + T('intermembrane space') + ' (F₀–F₁).')
d.basic('Why does cyanide kill?', 'It blocks ' + T('cytochrome c oxidase') + ' (complex IV), so electrons cannot reach O₂ and ATP production stops')

# ---------------------------------------------------------------- 12.5 Balance sheet
d.sec('12.5-balance-sheet')
d.basic('Four assumptions for the ATP balance sheet?', '(1) Sequential orderly pathway. (2) Glycolytic NADH enters mitochondria for oxidative phosphorylation. (3) No intermediates used for other compounds. (4) Only glucose is respired.')
d.basic('Why are these assumptions unrealistic?', 'Pathways run ' + T('simultaneously') + '; substrates enter and leave as needed; ATP is used as needed; enzyme rates are controlled')
d.basic('Net ATP per glucose in aerobic respiration (NCERT)?', N('38 ATP'))
table_card(d, 'Balance sheet (NCERT)', 'ATP per glucose?', [
    ('Glycolysis', '2 ATP + 2 NADH (6) = 8', False), ('Link reaction', '2 NADH = 6', False),
    ('Krebs cycle', '2 ATP + 6 NADH (18) + 2 FADH₂ (4) = 24', False), ('Total', '38', False)], term='38 ATP balance sheet')
d.basic('Update: is 38 ATP what cells really get?', 'Modern values are about ' + N('30–32 ATP') + ' (≈2.5 per NADH, 1.5 per FADH₂; shuttling glycolytic NADH costs energy). For exams, use NCERT\'s ' + N('38') + '.')
d.basic('Significance of step-wise energy release?', 'Energy is released in small packets that can be ' + T('trapped as ATP') + ', and intermediates can be used for biosynthesis')

# ---------------------------------------------------------------- 12.6 Amphibolic
d.sec('12.6-amphibolic')
d.basic('Favoured respiratory substrate?', T('Glucose') + ': other carbohydrates are usually converted to glucose first')
d.basic('Where do fatty acids enter respiration?', 'As ' + T('acetyl CoA'), **fig('fig_12_6_amphibolic'))
d.basic('Where does glycerol enter respiration?', 'As ' + T('PGAL') + ' (3-phosphoglyceraldehyde)')
d.basic('How do proteins enter respiration?', 'Proteases → amino acids → ' + T('deamination') + ' → enter as pyruvate, acetyl CoA or Krebs intermediates')
d.basic('Why is the respiratory pathway called amphibolic?', 'It serves both ' + T('catabolism') + ' (breakdown) and ' + T('anabolism') + ' (e.g. acetyl CoA withdrawn to make fatty acids)')
d.basic('Catabolism vs anabolism?', T('Catabolism') + ': breaking down. ' + T('Anabolism') + ': synthesis.')

# ---------------------------------------------------------------- 12.7 RQ
d.sec('12.7-rq')
d.basic('Define respiratory quotient (RQ).', 'Volume of ' + T('CO₂ evolved') + ' ÷ volume of ' + T('O₂ consumed') + '. Also called respiratory ratio.')
d.basic('RQ depends on what?', 'The type of ' + T('respiratory substrate'))
d.basic('RQ of carbohydrates?', N('1') + ' (6 CO₂ / 6 O₂)')
d.basic('RQ of fats? Example?', 'Less than 1: tripalmitin ' + N('102 CO₂ / 145 O₂ ≈ 0.7'))
d.basic('Tripalmitin oxidation equation?', '2(C₅₁H₉₈O₆) + 145O₂ → 102CO₂ + 98H₂O + energy')
d.basic('RQ of proteins?', 'About ' + N('0.9'))
d.basic('Why is fat RQ below 1? (intuition)', 'Fats contain little oxygen, so extra O₂ is needed to oxidise their many H atoms to water.<br>More O₂ is used than CO₂ given out')
d.basic('Beyond NCERT: RQ of organic acids and anaerobic respiration?', 'Organic acids (e.g. malic acid): ' + N('> 1') + '. Anaerobic respiration: ' + N('∞') + ' (CO₂ released, no O₂ used).')
d.basic('Are pure fats or proteins used as respiratory substrates?', X('Never') + '. Usually more than one substrate is used.')

d.sec('summary')
table_card(d, 'Respiration map', 'Where does it happen?', [
    ('Glycolysis', 'Cytoplasm', False), ('Fermentation', 'Cytoplasm', False), ('Pyruvate → acetyl CoA', 'Mitochondrial matrix', False),
    ('Krebs cycle', 'Mitochondrial matrix', False), ('ETS, oxidative phosphorylation', 'Inner mitochondrial membrane', False)], term='Location of respiratory steps')
d.basic('Glycolysis vs Krebs cycle?', 'Glycolysis: ' + T('cytoplasm') + ', glucose → 2 pyruvate, anaerobic, net 2 ATP<br>Krebs: ' + T('matrix') + ', acetyl CoA → CO₂, needs aerobic conditions, makes NADH/FADH₂')

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
