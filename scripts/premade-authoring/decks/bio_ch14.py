import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch14-breathing-and-exchange-of-gases')
d = Deck('Chapter 14: Breathing and Exchange of Gases', 'Class 11', ['class-11', 'biology', 'ch-14'])
d.description = 'Respiratory organs, human respiratory system, breathing mechanism, lung volumes, gas exchange and transport, regulation, disorders'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}
RS, AL = (1001, 577), (1001, 585)

# ---------------------------------------------------------------- Intro, 14.1
d.sec('14.0-intro')
d.basic('What is breathing?', 'Exchange of ' + T('O₂') + ' from the atmosphere with ' + T('CO₂') + ' produced by cells; commonly called respiration')
d.basic('Why must CO₂ be removed?', 'It is ' + T('harmful') + ' (it forms acid and disturbs pH)')

d.sec('14.1-respiratory-organs')
table_card(d, 'Respiratory organs', 'How do they breathe?', [
    ('Sponges, coelenterates, flatworms', 'Diffusion over body surface', False), ('Earthworm', 'Moist cuticle', False),
    ('Insects', 'Tracheal tubes', False), ('Aquatic arthropods, molluscs, fishes', 'Gills (branchial)', False),
    ('Terrestrial forms: amphibians, reptiles, birds, mammals', 'Lungs (pulmonary)', False), ('Frog (extra)', 'Moist skin (cutaneous)', False)],
    term='Respiratory organs across animals')
d.basic('On what does the breathing mechanism of an animal depend?', 'Its ' + T('habitat') + ' and ' + T('level of organisation'))
d.basic('What is branchial respiration?', 'Respiration by ' + T('gills'))
d.basic('What is cutaneous respiration? Example?', 'Respiration through moist ' + T('skin') + ', e.g. ' + E('frog'))
d.basic('Site of gas exchange in an insect?', 'The fine ends of the ' + T('tracheal tubes') + ' (tracheoles), in direct contact with tissues')

d.sec('14.1.1-human-system')
d.basic('Path of air from nostrils to lungs?', 'External nostrils → nasal passage → nasal chamber → ' + T('pharynx') + ' → ' + T('larynx') + ' → ' + T('trachea') + ' → bronchi → bronchioles → ' + T('alveoli'))
d.basic('What is the common passage for food and air?', 'Part of the ' + T('pharynx'))
d.basic('Why is the larynx called the sound box?', 'It is a ' + T('cartilaginous box') + ' that helps in sound production')
d.basic('What is the epiglottis?', 'A thin elastic cartilaginous flap that covers the ' + T('glottis') + ' during swallowing, stopping food entering the larynx')
d.basic('At which level does the trachea divide into primary bronchi?', 'The ' + N('5th thoracic vertebra'))
d.basic('Which airways have incomplete cartilaginous rings?', 'Trachea, primary, secondary and tertiary bronchi, and initial bronchioles')
d.basic('Why are the cartilage rings incomplete (C-shaped)?', 'They keep the airway ' + T('open') + ' while the open back lets the oesophagus expand during swallowing (intuition)')
d.basic('What are alveoli?', 'Very thin, irregular-walled, ' + T('vascularised') + ' bag-like structures at the end of terminal bronchioles')
d.basic('What covers the lungs?', 'A double-layered ' + T('pleura') + ' with ' + T('pleural fluid') + ' between the layers')
d.basic('Function of pleural fluid?', 'Reduces ' + T('friction') + ' on the lung surface')
d.basic('Outer vs inner pleural membrane?', 'Outer: in contact with the ' + T('thoracic lining') + '. Inner: in contact with the ' + T('lung surface') + '.')
d.occlusion('Figure 14.1 · Human respiratory system', M + 'fig_14_1_respiratory_system.webp', RS, [
    ('Epiglottis', wbox(789, 19, 884, 40, RS), True), ('Larynx', wbox(790, 78, 860, 99, RS), True),
    ('Trachea', wbox(791, 129, 873, 150, RS), True), ('Bronchus', wbox(192, 239, 291, 260, RS), True),
    ('Cut end of rib', wbox(150, 342, 290, 363, RS), True), ('Heart', wbox(523, 357, 579, 379, RS), True),
    ('Pleural membranes', wbox(791, 339, 988, 360, RS), True), ('Alveoli', wbox(791, 392, 857, 413, RS), True),
    ('Pleural fluid', wbox(792, 425, 915, 446, RS), True), ('Bronchiole', wbox(791, 465, 900, 486, RS), True),
    ('Lung', wbox(251, 438, 302, 459, RS), True), ('Diaphragm', wbox(488, 485, 601, 506, RS), True)])
d.basic('Conducting part vs respiratory (exchange) part?', T('Conducting') + ': external nostrils to terminal bronchioles. ' + T('Exchange') + ': alveoli and their ducts.')
d.basic('Functions of the conducting part?', 'Transports air to alveoli, ' + T('clears foreign particles') + ', ' + T('humidifies') + ', brings air to ' + T('body temperature'))
d.basic('Why does gas exchange happen only in alveoli?', 'Only alveoli have ' + T('very thin') + ' walls in close contact with a dense capillary network')
d.basic('What forms the thoracic chamber?', 'Dorsally: ' + T('vertebral column') + '. Ventrally: ' + T('sternum') + '. Laterally: ' + T('ribs') + '. Below: dome-shaped ' + T('diaphragm') + '.')
d.basic('Why must the thoracic chamber be air-tight?', 'Any change in thoracic volume is reflected in the lung volume; we ' + X('cannot') + ' change lung volume directly')
d.cloze('Steps of respiration: (i) {{c1::breathing (pulmonary ventilation)}} → (ii) diffusion across the {{c2::alveolar membrane}} → (iii) {{c3::transport by blood}} → (iv) diffusion between blood and {{c4::tissues}} → (v) {{c5::cellular respiration}}.')

# ---------------------------------------------------------------- 14.2 Mechanism
d.sec('14.2-mechanism')
d.basic('Two stages of breathing?', T('Inspiration') + ' (air drawn in) and ' + T('expiration') + ' (alveolar air released)')
d.basic('When does inspiration occur?', 'When intra-pulmonary pressure is ' + T('less than') + ' atmospheric pressure (negative pressure)')
d.basic('When does expiration occur?', 'When intra-pulmonary pressure is ' + T('higher than') + ' atmospheric pressure')
d.basic('Which muscles create the pressure gradients?', 'The ' + T('diaphragm') + ' and ' + T('external and internal intercostals'))
d.basic('What does contraction of the diaphragm do?', 'Increases thoracic volume in the ' + T('antero-posterior') + ' axis')
d.basic('What does contraction of external intercostals do?', 'Lifts ribs and sternum: increases thoracic volume in the ' + T('dorso-ventral') + ' axis')
d.basic('Explain inspiration in steps.', 'Diaphragm and external intercostals ' + T('contract') + ' → thoracic and pulmonary volume ↑ → intra-pulmonary pressure ↓ below atmospheric → air rushes in', **fig('fig_14_2_breathing'))
d.basic('Explain normal expiration.', 'Diaphragm and intercostals ' + T('relax') + ' → thoracic volume ↓ → pressure rises slightly above atmospheric → air is expelled')
d.basic('Is normal expiration active or passive?', T('Passive') + ' (muscle relaxation). Forceful breathing uses abdominal muscles.')
d.basic('Which muscles increase the strength of breathing?', 'Additional muscles in the ' + T('abdomen'))
d.basic('Normal breathing rate of a healthy human?', N('12–16') + ' times per minute')
d.basic('Instrument to measure breathing volumes?', T('Spirometer'))

d.sec('14.2.1-volumes')
d.basic('Tidal volume (TV)?', 'Air inspired or expired in a ' + T('normal') + ' breath: about ' + N('500 mL'))
d.basic('Air breathed per minute by a healthy man?', N('6000–8000 mL') + ' (TV × 12–16)')
d.basic('Tidal volume of a healthy human in an hour (approx.)?', N('≈ 360–480 L') + ' (6–8 L/min × 60)')
d.basic('Inspiratory reserve volume (IRV)?', 'Extra air inspired by ' + T('forcible inspiration') + ': ' + N('2500–3000 mL'))
d.basic('Expiratory reserve volume (ERV)?', 'Extra air expired by ' + T('forcible expiration') + ': ' + N('1000–1100 mL'))
d.basic('Residual volume (RV)?', 'Air remaining in lungs ' + T('even after forcible expiration') + ': ' + N('1100–1200 mL'))
d.cloze('Inspiratory capacity (IC) = {{c1::TV + IRV}}. Expiratory capacity (EC) = {{c2::TV + ERV}}.')
d.cloze('Functional residual capacity (FRC) = {{c1::ERV + RV}}: air left after a normal expiration.')
d.cloze('Vital capacity (VC) = {{c1::ERV + TV + IRV}}. Total lung capacity (TLC) = {{c2::VC + RV}}.')
d.basic('Define vital capacity.', 'Maximum air a person can breathe ' + T('in after a forced expiration') + ' (or out after a forced inspiration)')
d.basic('Significance of vital capacity?', 'It indicates lung fitness: higher in ' + E('athletes, mountain dwellers, swimmers') + ', lower in smokers and lung disease')
d.basic('Volume of air in the lungs after a normal expiration?', T('FRC') + ' = ERV + RV ≈ ' + N('2100–2300 mL'))
d.basic('Which volume cannot be measured by a spirometer?', T('Residual volume') + ' (and so FRC and TLC). It never leaves the lungs.')
d.basic('Mnemonic: volumes vs capacities?', 'Volumes are single blocks (TV, IRV, ERV, RV). ' + T('Capacities = sum of 2+ volumes') + '. Any capacity with "residual" or "total" includes RV.')
table_card(d, 'Lung volumes (NCERT)', 'Approximate value?', [
    ('TV', '500 mL', False), ('IRV', '2500–3000 mL', False), ('ERV', '1000–1100 mL', False), ('RV', '1100–1200 mL', False),
    ('VC', '≈ 4000–4600 mL', False), ('TLC', '≈ 5100–5800 mL', False)], term='Lung volumes and capacities')

# ---------------------------------------------------------------- 14.3 Exchange
d.sec('14.3-exchange')
d.basic('Primary sites of gas exchange?', T('Alveoli') + '; exchange also occurs between blood and tissues')
d.basic('How are O₂ and CO₂ exchanged?', 'By ' + T('simple diffusion') + ', based on pressure/concentration gradient')
d.basic('Factors affecting rate of diffusion?', 'Partial pressure gradient, ' + T('solubility') + ' of the gas, ' + T('thickness') + ' of membranes')
d.basic('What is partial pressure?', 'Pressure contributed by ' + T('one gas') + ' in a mixture: pO₂, pCO₂')
table_card(d, 'Table 14.1 · mm Hg', 'pO₂ / pCO₂?', [
    ('Atmospheric air', '159 / 0.3', False), ('Alveoli', '104 / 40', False), ('Deoxygenated blood', '40 / 45', False),
    ('Oxygenated blood', '95 / 40', False), ('Tissues', '40 / 45', False)], term='Table 14.1: partial pressures')
d.cloze('pO₂: atmosphere {{c1::159}}, alveoli {{c2::104}}, oxygenated blood {{c3::95}}, tissues {{c4::40}} mm Hg.')
d.cloze('pCO₂: atmosphere {{c1::0.3}}, alveoli {{c2::40}}, deoxygenated blood {{c3::45}}, tissues {{c4::45}} mm Hg.')
d.basic('Atmospheric air vs alveolar air: pO₂ and pCO₂?', 'Atmospheric air has ' + T('higher pO₂') + ' and ' + T('lower pCO₂'))
d.basic('Why is alveolar pO₂ (104) lower than atmospheric (159)?', 'Fresh air mixes with the ' + T('residual air') + ' in the lungs, which is poorer in O₂ (and water vapour adds pressure)')
d.basic('How much more soluble is CO₂ than O₂?', N('20–25 times'))
d.basic('Why does CO₂ diffuse well despite a small gradient (45 → 40)?', 'Its ' + T('solubility') + ' is 20–25 times that of O₂')
d.basic('Three layers of the diffusion membrane?', 'Thin ' + T('squamous epithelium') + ' of alveoli, ' + T('endothelium') + ' of alveolar capillaries, and the ' + T('basement substance') + ' between them')
d.basic('Total thickness of the diffusion membrane?', 'Much ' + T('less than a millimetre'))
d.occlusion('Figure 14.4 · Alveolus with pulmonary capillary', M + 'fig_14_4_alveolus.webp', AL, [
    ('Squamous epithelium of alveolar wall', [17, 122, 322, 122]), ('Basement substance', [702, 122, 176, 90]),
    ('Endothelium of blood capillary', [756, 235, 237, 90]), ('Alveolar cavity', [375, 249, 250, 56]),
    ('Blood capillary', [229, 419, 124, 96]), ('Red blood cell', [629, 455, 164, 90])], printed=True)
d.basic('Figure 14.3: summarise exchange at alveolus and tissues.', 'At alveoli O₂ enters blood (pO₂ 104 → 95) and CO₂ leaves (45 → 40); at tissues O₂ leaves blood and CO₂ enters', **img('fig_14_3_gas_exchange'))

# ---------------------------------------------------------------- 14.4 Transport
d.sec('14.4-transport')
d.basic('How is O₂ transported?', N('97%') + ' by RBCs; ' + N('3%') + ' dissolved in plasma')
d.basic('How is CO₂ transported?', N('20–25%') + ' by RBCs (carbamino-haemoglobin); ' + N('70%') + ' as bicarbonate; ' + N('7%') + ' dissolved in plasma')
d.basic('What is haemoglobin?', 'A red, ' + T('iron-containing') + ' pigment in RBCs')
d.basic('Maximum O₂ molecules per haemoglobin?', N('Four'))
d.basic('Main factor in O₂ binding to haemoglobin?', T('Partial pressure of O₂') + '; pCO₂, H⁺ and temperature also interfere')
d.basic('What is the oxygen dissociation curve?', 'Percentage saturation of haemoglobin with O₂ plotted against ' + T('pO₂') + '; it is ' + T('sigmoid'), **fig('fig_14_5_odc'))
d.basic('Why is the oxygen dissociation curve sigmoid?', 'Binding of one O₂ makes the next bind more easily (' + T('cooperative binding') + '), so saturation rises steeply in the middle range')
d.basic('Conditions in alveoli favouring oxyhaemoglobin formation?', T('High pO₂') + ', low pCO₂, fewer H⁺, lower temperature')
d.basic('Conditions in tissues favouring O₂ release?', T('Low pO₂') + ', high pCO₂, high H⁺, higher temperature')
d.basic('Effect of pCO₂ on oxygen transport?', 'High pCO₂ (and H⁺) ' + T('lowers') + ' haemoglobin\'s O₂ affinity: curve shifts right, O₂ released to tissues (Bohr effect)')
d.basic('Mnemonic for a right shift of the O₂ curve?', '"' + T('CADET, face Right') + '": CO₂, Acid (H⁺), 2,3-DPG, Exercise, Temperature ↑ → curve shifts right, O₂ unloaded')
d.basic('O₂ delivered to tissues per 100 mL oxygenated blood?', 'About ' + N('5 mL'))
d.basic('What is carbamino-haemoglobin?', 'CO₂ carried bound to ' + T('haemoglobin') + ' (20–25% of CO₂)')
d.basic('When does CO₂ bind to Hb and when is it released?', 'Binds at ' + T('tissues') + ' (high pCO₂, low pO₂); released at ' + T('alveoli') + ' (low pCO₂, high pO₂)')
d.basic('Which enzyme helps carry CO₂ as bicarbonate, and where is it?', T('Carbonic anhydrase') + ': very high in RBCs, minute amounts in plasma')
d.basic('Carbonic anhydrase reaction?', 'CO₂ + H₂O ⇌ H₂CO₃ ⇌ HCO₃⁻ + H⁺')
d.basic('Direction of the carbonic anhydrase reaction at tissues vs alveoli?', 'Tissues (high pCO₂): → ' + T('HCO₃⁻ + H⁺') + '. Alveoli (low pCO₂): ← ' + T('CO₂ + H₂O') + '.')
d.basic('CO₂ delivered to alveoli per 100 mL deoxygenated blood?', 'About ' + N('4 mL'))
d.basic('Why is CO poisonous (beyond NCERT)?', 'Carbon monoxide binds haemoglobin about ' + N('200×') + ' more strongly than O₂ (carboxyhaemoglobin), so O₂ transport stops')

# ---------------------------------------------------------------- 14.5 Regulation
d.sec('14.5-regulation')
d.basic('Which system regulates respiratory rhythm?', 'The ' + T('neural system'))
d.basic('Where is the respiratory rhythm centre?', 'In the ' + T('medulla') + ' of the brain')
d.basic('Where is the pneumotaxic centre, and what does it do?', 'In the ' + T('pons') + '; it moderates the rhythm centre and can ' + T('reduce the duration of inspiration') + ', altering the rate')
d.basic('What is the chemosensitive area sensitive to?', T('CO₂ and H⁺') + '; located next to the rhythm centre')
d.basic('Which peripheral receptors detect CO₂ and H⁺?', 'Receptors on the ' + T('aortic arch') + ' and ' + T('carotid artery'))
d.basic('Role of O₂ in regulating respiratory rhythm?', X('Quite insignificant') + '. CO₂ and H⁺ are the main drivers.')
d.basic('What happens to breathing on going up a hill?', 'Low pO₂ at altitude → breathing rate and depth ' + T('increase') + '; over days the body makes more RBCs (acclimatisation)')
d.basic('What is hypoxia?', 'Shortage of ' + T('O₂') + ' reaching tissues, e.g. at high altitude')

# ---------------------------------------------------------------- 14.6 Disorders
d.sec('14.6-disorders')
d.basic('What is asthma?', 'Difficulty in breathing with ' + T('wheezing') + ', due to inflammation of ' + T('bronchi and bronchioles'))
d.basic('What is emphysema?', 'A chronic disorder in which ' + T('alveolar walls are damaged') + ', reducing respiratory surface')
d.basic('Major cause of emphysema?', T('Cigarette smoking'))
d.basic('What are occupational respiratory disorders?', 'Long exposure to ' + T('dust') + ' (grinding, stone-breaking) causes inflammation and ' + T('fibrosis') + ' of the lungs')
d.basic('What is fibrosis?', 'Proliferation of ' + T('fibrous tissue') + ', causing serious lung damage')
d.basic('Prevention of occupational lung disorders?', 'Workers should wear ' + T('protective masks'))
table_card(d, 'Disorders', 'What goes wrong?', [
    ('Asthma', 'Inflamed bronchi/bronchioles, wheezing', False), ('Emphysema', 'Alveolar walls damaged', False),
    ('Occupational disorders', 'Dust → inflammation → fibrosis', False)], term='Respiratory disorders')

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
