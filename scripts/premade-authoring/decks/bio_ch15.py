import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch15-body-fluids-and-circulation')
d = Deck('Chapter 15: Body Fluids and Circulation', 'Class 11', ['class-11', 'biology', 'ch-15'])
d.description = 'Blood, blood groups, clotting, lymph, circulatory patterns, human heart, cardiac cycle, ECG, double circulation, disorders'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}
FE, HT = (1001, 235), (1001, 745)

# ---------------------------------------------------------------- Intro, 15.1 Blood
d.sec('15.0-intro')
d.basic('How do sponges and coelenterates move substances to cells?', 'They circulate ' + T('water') + ' from surroundings through body cavities')
d.basic('Two body fluids for transport in humans?', T('Blood') + ' and ' + T('lymph'))

d.sec('15.1-blood')
d.basic('Why is blood a connective tissue?', 'It is a ' + T('special connective tissue') + ':<br>cells (formed elements) in a fluid ' + T('matrix (plasma)') + '<br>Originates from mesoderm')
d.basic('What fraction of blood is plasma?', 'Nearly ' + N('55%'))
d.basic('Composition of plasma?', N('90–92%') + ' water; ' + N('6–8%') + ' proteins; minerals, glucose, amino acids, lipids, clotting factors')
d.basic('Colour and consistency of plasma?', T('Straw coloured') + ', viscous')
table_card(d, 'Plasma proteins', 'Function?', [
    ('Fibrinogen', 'Clotting of blood', False), ('Globulins', 'Defence (antibodies)', False), ('Albumins', 'Osmotic balance', False)],
    term='Plasma proteins and their roles')
d.basic('What is serum?', 'Plasma ' + X('without clotting factors'))
d.basic('Minerals in plasma?', 'Na⁺, Ca²⁺, Mg²⁺, HCO₃⁻, Cl⁻')

d.sec('15.1.2-formed-elements')
d.basic('What are the formed elements, and what fraction of blood?', T('Erythrocytes, leucocytes, platelets') + '; nearly ' + N('45%'))
d.basic('RBC count in a healthy adult man?', N('5–5.5 million') + ' per mm³')
d.basic('Where are RBCs formed in adults?', T('Red bone marrow'))
d.basic('Shape and nucleus of mammalian RBCs?', T('Biconcave') + ', ' + X('no nucleus') + ' in most mammals')
d.basic('Why are RBCs biconcave and without a nucleus? (intuition)', 'More ' + T('surface area') + ' for gas exchange and more room for haemoglobin.<br>The thin shape lets them squeeze through capillaries')
d.basic('Haemoglobin per 100 mL blood?', N('12–16 g'))
d.basic('Lifespan of RBCs, and where are they destroyed?', N('120 days') + '; destroyed in the ' + T('spleen') + ' ("graveyard of RBCs")')
d.basic('Why are WBCs colourless?', 'They ' + X('lack haemoglobin'))
d.basic('WBC count?', N('6000–8000') + ' per mm³')
d.cloze('Granulocytes: {{c1::neutrophils, eosinophils, basophils}}. Agranulocytes: {{c2::lymphocytes, monocytes}}.')
table_card(d, 'Leucocytes', '% of WBCs · role?', [
    ('Neutrophils', '60–65% · phagocytic (most abundant)', False), ('Lymphocytes', '20–25% · immunity (B and T)', False),
    ('Monocytes', '6–8% · phagocytic', False), ('Eosinophils', '2–3% · resist infection, allergy', False),
    ('Basophils', '0.5–1% · histamine, serotonin, heparin; inflammation (least)', False)], term='Types of WBCs')
d.basic('Most and least abundant WBCs?', 'Most: ' + T('neutrophils') + '. Least: ' + T('basophils') + '.')
d.basic('Which WBCs are phagocytic?', T('Neutrophils') + ' and ' + T('monocytes'))
d.basic('What do basophils secrete?', T('Histamine, serotonin, heparin'))
d.basic('Which WBCs are associated with allergic reactions?', T('Eosinophils'))
d.basic('Mnemonic for WBC abundance?', '"' + T('Never Let Monkeys Eat Bananas') + '": Neutrophils > Lymphocytes > Monocytes > Eosinophils > Basophils')
d.basic('What are platelets?', 'Cell fragments (' + T('thrombocytes') + ') produced from ' + T('megakaryocytes') + ' in bone marrow')
d.basic('Platelet count?', N('1,50,000–3,50,000') + ' per mm³')
d.basic('Correction: NCERT prints the platelet count as "1,500,00–3,500,00". Correct figure?', N('1,50,000–3,50,000') + ' per mm³ (150,000–350,000); the commas are misplaced in the book')
d.basic('Effect of low platelet count?', T('Clotting disorders') + ', excessive blood loss')
d.occlusion('Figure 15.1 · Formed elements of blood', M + 'fig_15_1_formed_elements.webp', FE, [
    ('RBC', wbox(61, 59, 116, 78, FE, 4), True), ('Platelets', wbox(190, 146, 269, 165, FE, 4), True),
    ('Eosinophil', wbox(296, 42, 396, 61, FE, 4), True), ('Basophil', wbox(426, 153, 509, 172, FE, 4), True),
    ('Neutrophil', wbox(518, 36, 618, 55, FE, 4), True), ('Monocyte', wbox(647, 151, 737, 170, FE, 4), True),
    ('T lymphocyte', wbox(740, 44, 866, 63, FE, 4), True), ('B lymphocyte', wbox(833, 151, 961, 170, FE, 4), True)])

d.sec('15.1.3-blood-groups')
d.basic('Two widely used blood groupings?', T('ABO') + ' and ' + T('Rh'))
d.basic('ABO grouping is based on?', 'Presence or absence of surface ' + T('antigens A and B') + ' on RBCs')
d.basic('What are antigens and antibodies?', T('Antigens') + ': chemicals that induce an immune response. ' + T('Antibodies') + ': proteins made in response to antigens.')
table_card(d, 'Table 15.1', 'Antigen · antibody · can receive from?', [
    ('A', 'A · anti-B · A, O', False), ('B', 'B · anti-A · B, O', False), ('AB', 'A, B · nil · AB, A, B, O', False),
    ('O', 'nil · anti-A, anti-B · O', False)], term='Table 15.1: ABO blood groups')
d.basic('Universal donor and why?', T('Group O') + ': RBCs carry no A or B antigen')
d.basic('Universal recipient and why?', T('Group AB') + ': plasma has no anti-A or anti-B antibodies')
d.basic('What happens with mismatched transfusion?', T('Clumping') + ' (agglutination) and destruction of RBCs')
d.basic('Why is it called the Rh antigen?', 'It is similar to an antigen of ' + T('Rhesus monkeys'))
d.basic('What percentage of humans are Rh+?', 'Nearly ' + N('80%'))
d.basic('What happens if an Rh− person receives Rh+ blood?', 'They form specific ' + T('antibodies against Rh antigen'))
d.basic('What is erythroblastosis foetalis?', 'Rh− mother\'s anti-Rh antibodies destroy RBCs of an Rh+ foetus in a ' + T('later pregnancy') + '.<br>Result: severe anaemia, jaundice, even death')
d.basic('Why is the first Rh+ baby usually safe?', 'The bloods are separated by the ' + T('placenta') + '; the mother is exposed to foetal blood only at ' + T('delivery'))
d.basic('How is erythroblastosis foetalis prevented?', 'Give ' + T('anti-Rh antibodies') + ' to the mother immediately after the first delivery')

d.sec('15.1.4-coagulation')
d.basic('Why does blood clot?', 'To prevent excessive ' + T('blood loss') + ' after injury')
d.basic('What is a clot made of?', 'A network of ' + T('fibrin') + ' threads trapping dead and damaged formed elements')
d.basic('Clotting cascade in brief?', 'Injury → platelets/tissues release factors → ' + T('thrombokinase') + ' → prothrombin → ' + T('thrombin') + ' → fibrinogen → ' + T('fibrin'))
d.cloze('Thrombokinase converts {{c1::prothrombin}} to {{c2::thrombin}}, which converts {{c3::fibrinogen}} to {{c4::fibrin}}.')
d.basic('Which ion is important in clotting?', T('Calcium (Ca²⁺)'))
d.basic('Why is heparin (from basophils) useful?', 'It is an ' + T('anticoagulant') + ': prevents clotting inside vessels')

# ---------------------------------------------------------------- 15.2 Lymph
d.sec('15.2-lymph')
d.basic('What is interstitial (tissue) fluid?', 'Water and small solutes that leave capillaries into spaces between cells,<br>' + X('leaving large proteins') + ' and most formed elements behind')
d.basic('Mineral composition of tissue fluid?', 'Same as ' + T('plasma'))
d.basic('What is lymph?', 'Tissue fluid collected by the ' + T('lymphatic system') + ' and drained back into major veins')
d.basic('Blood vs lymph?', 'Lymph: ' + T('colourless') + ', ' + X('no RBCs') + ', fewer proteins, has lymphocytes. Blood: red, RBCs, more proteins.')
d.basic('Functions of lymph?', 'Carries specialised ' + T('lymphocytes') + ' (immunity), nutrients and hormones; absorbs ' + T('fats') + ' through lacteals')
d.basic('Where are fats absorbed into lymph?', 'In the ' + T('lacteals') + ' of intestinal villi')

# ---------------------------------------------------------------- 15.3 Circulatory pathways
d.sec('15.3-pathways')
d.basic('Open circulation: what and where?', 'Blood flows from vessels into open spaces (' + T('sinuses') + '); in ' + E('arthropods, molluscs'))
d.basic('Closed circulation: what and where?', 'Blood always flows in a closed network of vessels; in ' + E('annelids, chordates'))
d.basic('Why is closed circulation more advantageous?', 'Flow can be regulated more ' + T('precisely'))
table_card(d, 'Vertebrate hearts', 'Chambers · circulation?', [
    ('Fishes', '2 (1 atrium, 1 ventricle) · single', False), ('Amphibians, reptiles', '3 (2 atria, 1 ventricle) · incomplete double', False),
    ('Crocodiles, birds, mammals', '4 (2 atria, 2 ventricles) · double', False)], term='Evolution of the vertebrate heart')
d.basic('Which reptile has a 4-chambered heart?', X('Crocodile') + ' (exception)')
d.basic('Why is fish circulation called single?', 'Blood passes through the heart ' + T('once') + ' per circuit; the heart pumps only deoxygenated blood to the gills')
d.basic('Why is amphibian circulation incomplete double?', 'Oxygenated and deoxygenated blood ' + T('mix') + ' in the single ventricle')

d.sec('15.3.1-human-heart')
d.basic('Three parts of the human circulatory system?', 'A muscular chambered ' + T('heart') + ', closed branching ' + T('blood vessels') + ', and ' + T('blood'))
d.basic('Germ layer origin of the heart?', T('Mesoderm'))
d.basic('Position and size of the heart?', 'In the thoracic cavity between the lungs, ' + T('slightly tilted left') + '; size of a clenched fist')
d.basic('What protects the heart?', 'Double-walled ' + T('pericardium') + ' enclosing pericardial fluid')
d.basic('Septa of the heart?', T('Inter-atrial') + ' (thin, muscular), ' + T('inter-ventricular') + ' (thick), ' + T('atrio-ventricular') + ' (thick fibrous)')
d.basic('Tricuspid vs bicuspid valve?', T('Tricuspid') + ': right atrium → right ventricle (3 cusps). ' + T('Bicuspid (mitral)') + ': left atrium → left ventricle.')
d.basic('Mnemonic for valve sides?', '"' + T('Try before you Buy') + '": Tricuspid is on the right (comes first in the blood path), Bicuspid on the left')
d.basic('Where are the semilunar valves?', 'At the openings of the ventricles into the ' + T('pulmonary artery') + ' and ' + T('aorta'))
d.basic('Why are ventricle walls thicker than atrial walls?', 'Ventricles pump blood to the lungs and whole body; atria only push blood next door. The left ventricle is thickest.')
d.occlusion('Figure 15.2 · Section of a human heart', M + 'fig_15_2_heart.webp', HT, [
    ('Aorta', pad([781, 134, 64, 26], 5, HT), True), ('Vena cava', pad([90, 189, 116, 27], 5, HT), True),
    ('Pulmonary artery', pad([792, 224, 201, 26], 5, HT), True), ('Pulmonary veins', pad([784, 257, 193, 27], 5, HT), True),
    ('Left atrium', pad([779, 296, 129, 27], 5, HT), True), ('Sino-atrial node', pad([23, 292, 182, 26], 5, HT), True),
    ('Right atrium', pad([60, 334, 145, 27], 5, HT), True), ('Atrio-ventricular node', pad([42, 371, 189, 53], 5, HT), True),
    ('Bundle of His', pad([781, 421, 156, 27], 5, HT), True), ('Chordae tendinae', pad([13, 476, 200, 27], 5, HT), True),
    ('Right ventricle', pad([36, 532, 164, 26], 5, HT), True), ('Left ventricle', pad([781, 550, 146, 26], 5, HT), True),
    ('Interventricular septum', pad([779, 622, 179, 56], 5, HT), True), ('Apex', pad([768, 703, 59, 27], 5, HT), True)])

d.sec('15.3.1-nodal-tissue')
d.basic('What is nodal tissue?', 'Specialised cardiac musculature that is ' + T('autoexcitable') + ' (generates action potentials without external stimuli)')
d.basic('Where is the SAN?', 'Right ' + T('upper corner') + ' of the right atrium')
d.basic('Where is the AVN?', 'Lower left corner of the ' + T('right atrium') + ', near the atrio-ventricular septum')
d.basic('Conduction pathway of the heart?', T('SAN') + ' → atria → ' + T('AVN') + ' → ' + T('AV bundle (bundle of His)') + ' → right and left bundle branches → ' + T('Purkinje fibres'))
d.basic('Why is the SAN called the pacemaker?', 'It generates the ' + T('maximum') + ' number of action potentials (' + N('70–75/min') + '), so it initiates and sets the rhythm')
d.basic('Significance of the AVN and AV bundle?', 'They relay the impulse from atria to ' + T('ventricles') + ' with a slight delay, so atria finish contracting first')
d.basic('Normal heart rate?', N('70–75') + ' beats per minute (average ' + N('72') + ')')

d.sec('15.3.2-cardiac-cycle')
d.basic('What is joint diastole?', 'All four chambers ' + T('relaxed') + '; AV valves open, semilunar valves closed, blood fills ventricles')
d.basic('How much does atrial systole add to ventricular filling?', 'About ' + N('30%'))
d.basic('Order of events in the cardiac cycle?', '1) Joint diastole<br>2) ' + T('Atrial systole') + '<br>3) ' + T('Ventricular systole') + ' (AV valves close, semilunar open)<br>4) ' + T('Ventricular diastole') + ' (semilunar close, AV open)<br>5) Joint diastole')
d.basic('Why do the AV valves close during ventricular systole?', 'Rising ventricular pressure pushes blood back towards the atria, ' + T('snapping them shut'))
d.basic('What is the cardiac cycle?', 'The cyclically repeated sequence of ' + T('systole and diastole') + ' of atria and ventricles')
d.basic('Duration of one cardiac cycle?', N('0.8 s') + ' (60 ÷ 72)')
d.basic('What is stroke volume?', 'Blood pumped by each ventricle per cycle: about ' + N('70 mL'))
d.basic('What is cardiac output?', 'Stroke volume × heart rate: blood pumped by each ventricle per minute, about ' + N('5 L'))
d.basic('Why is an athlete\'s cardiac output higher?', 'The body can raise both ' + T('stroke volume') + ' and heart rate')
d.basic('What causes the first heart sound (lub)?', 'Closure of the ' + T('tricuspid and bicuspid') + ' valves')
d.basic('What causes the second heart sound (dub)?', 'Closure of the ' + T('semilunar') + ' valves')
d.basic('Systole vs diastole?', T('Systole') + ': contraction. ' + T('Diastole') + ': relaxation.')

d.sec('15.3.3-ecg')
d.basic('What is an ECG?', 'A graphical record of the ' + T('electrical activity') + ' of the heart during a cardiac cycle', **img('fig_15_3_ecg'))
d.basic('Standard ECG leads?', N('Three') + ': one to each wrist and one to the left ankle')
d.basic('What does the P-wave represent?', T('Depolarisation of the atria') + ' → atrial contraction')
d.basic('What does the QRS complex represent?', T('Depolarisation of the ventricles') + ' → ventricular contraction (starts shortly after Q)')
d.basic('What does the T-wave represent?', T('Repolarisation') + ' of the ventricles; its end marks the end of systole')
d.basic('How can heart rate be counted from an ECG?', 'Count the number of ' + T('QRS complexes') + ' in a given time')
d.basic('P-wave vs T-wave?', 'P: ' + T('atrial depolarisation') + '. T: ' + T('ventricular repolarisation') + '.')
d.basic('Why is atrial repolarisation not seen on an ECG?', 'It is hidden by the much larger ' + T('QRS complex'))

# ---------------------------------------------------------------- 15.4 Double circulation
d.sec('15.4-double-circulation')
d.cloze('Artery/vein wall: inner {{c1::tunica intima}} (squamous endothelium); middle {{c2::tunica media}} (smooth muscle, elastic fibres); outer {{c3::tunica externa}} (fibrous connective tissue, collagen).')
d.basic('Which layer is thinner in veins?', T('Tunica media'))
d.basic('Pulmonary circulation?', T('Right ventricle') + ' → pulmonary artery → lungs → pulmonary veins → ' + T('left atrium'))
d.basic('Systemic circulation?', T('Left ventricle') + '<br>→ aorta<br>→ arteries, arterioles, capillaries<br>→ tissues<br>→ venules, veins, vena cava<br>→ ' + T('right atrium'), **fig('fig_15_4_circulation'))
d.basic('Which artery carries deoxygenated blood, and which vein oxygenated?', T('Pulmonary artery') + ' (deoxygenated); ' + T('pulmonary vein') + ' (oxygenated)')
d.basic('Significance of double circulation?', 'Oxygenated and deoxygenated blood ' + X('never mix') + ', so tissues get fully oxygenated blood at high pressure')
d.basic('What is the hepatic portal system?', 'The ' + T('hepatic portal vein') + ' carries blood from the ' + T('intestine to the liver') + ' before it reaches systemic circulation')
d.basic('What is the coronary system?', 'Vessels exclusively for circulation to and from the ' + T('cardiac muscle'))

# ---------------------------------------------------------------- 15.5 Regulation
d.sec('15.5-regulation')
d.basic('Why is the human heart called myogenic?', 'Its beat is initiated by specialised ' + T('muscle (nodal tissue)') + ', not by nerves')
d.basic('Where is the neural centre that moderates heart function?', T('Medulla oblongata') + ', acting through the ANS')
d.basic('Effect of sympathetic nerves on the heart?', T('Increase') + ' heart rate, strength of ventricular contraction and cardiac output')
d.basic('Effect of parasympathetic nerves on the heart?', T('Decrease') + ' heart rate, conduction speed and cardiac output')
d.basic('Which hormones increase cardiac output?', T('Adrenal medullary') + ' hormones (adrenaline, noradrenaline)')

# ---------------------------------------------------------------- 15.6 Disorders
d.sec('15.6-disorders')
d.basic('Normal blood pressure?', N('120/80') + ' mm Hg: systolic (pumping) / diastolic (resting)')
d.basic('What reading indicates hypertension?', 'Repeatedly ' + N('140/90') + ' or higher')
d.basic('Effects of hypertension?', 'Heart diseases; affects vital organs like ' + T('brain and kidney'))
d.basic('What is coronary artery disease (CAD)?', T('Atherosclerosis') + ':<br>deposits of calcium, fat, cholesterol and fibrous tissue narrow arteries supplying the heart muscle')
d.basic('What is angina (angina pectoris)?', 'Acute ' + T('chest pain') + ' when not enough O₂ reaches the heart muscle')
d.basic('What is heart failure? Other name?', 'Heart not pumping effectively enough; ' + T('congestive heart failure') + ' (lung congestion is a main symptom)')
table_card(d, 'Heart problems', 'What is it?', [
    ('Heart failure', 'Pumps too weakly for body needs', False), ('Cardiac arrest', 'Heart stops beating', False),
    ('Heart attack', 'Heart muscle suddenly damaged by poor blood supply', False)], term='Heart failure vs cardiac arrest vs heart attack')
table_card(d, 'Exercise 3', 'Match', [
    ('Eosinophils', 'Resist infections', False), ('RBC', 'Gas transport', False), ('AB group', 'Universal recipient', False),
    ('Platelets', 'Coagulation', False), ('Systole', 'Contraction of heart', False)], term='Match the column (Exercise 3)')

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
