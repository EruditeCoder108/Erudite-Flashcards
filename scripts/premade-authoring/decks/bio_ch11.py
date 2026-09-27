import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch11-photosynthesis-in-higher-plants')
d = Deck('Chapter 11: Photosynthesis in Higher Plants', 'Class 11', ['class-11', 'biology', 'ch-11'])
d.description = 'Early experiments, pigments, light reaction, Z scheme, chemiosmosis, Calvin cycle, C4 pathway, photorespiration, limiting factors'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}


def S(x0, y0, x1, y1, size, p=5):
    """Mask box from word-box corners (x0, y0, x1, y1) printed by figcrop, padded and kept inside the image."""
    return pad([x0, y0, x1 - x0, y1 - y0], p, size)


# ---------------------------------------------------------------- Intro, 11.1
d.sec('11.0-intro')
d.basic('What is photosynthesis?', 'A ' + T('physico-chemical') + ' process by which green plants use light energy to drive the synthesis of organic compounds')
d.basic('Why are green plants called autotrophs?', 'They ' + T('synthesise their own food') + ' by photosynthesis')
d.basic('Two reasons photosynthesis is important?', 'It is the ' + T('primary source of all food') + ' on earth, and it releases ' + T('oxygen') + ' into the atmosphere')

d.sec('11.1-what-we-know')
d.basic('What three things did school experiments show are needed for photosynthesis?', T('Chlorophyll, light') + ' and ' + T('CO₂'))
d.basic('Variegated leaf / half-covered leaf starch test shows what?', 'Photosynthesis occurs only in ' + T('green parts') + ' and only in ' + T('light'))
d.basic('Half-leaf experiment: what does KOH in the test tube do?', 'KOH ' + T('absorbs CO₂') + '; the enclosed part tests negative for starch, so CO₂ is required')

# ---------------------------------------------------------------- 11.2 Early experiments
d.sec('11.2-early-experiments')
d.basic('What did Priestley conclude from the bell-jar experiments (1770)?', 'Plants ' + T('restore to the air') + ' whatever breathing animals and burning candles remove', **fig('fig_11_1_priestley'))
d.basic('Describe Priestley\'s bell-jar observations (Figure 11.1).', 'A candle goes out and a mouse suffocates in a closed jar; with a ' + E('mint plant') + ' inside, the candle burns and the mouse lives', **img('fig_11_1_priestley'))
d.basic('Which gas did Priestley discover, and when?', T('Oxygen') + ', in ' + N('1774'))
d.basic('What did Jan Ingenhousz show?', T('Sunlight') + ' is essential; only the ' + T('green parts') + ' of plants release oxygen')
d.basic('How did Ingenhousz show that green parts release O₂?', 'An aquatic plant in bright sunlight formed ' + T('bubbles') + ' around green parts, not in the dark; the bubbles were oxygen')
d.basic('What did Julius von Sachs show (1854)?', 'Plants produce ' + T('glucose') + ' (stored as starch); chlorophyll is in special bodies (later called ' + T('chloroplasts') + ')')
d.basic('What did Engelmann\'s experiment show?', 'Aerobic bacteria gathered in ' + T('blue and red') + ' light around ' + EI('Cladophora') + ': the first ' + T('action spectrum') + ' of photosynthesis')
d.basic('Why did Engelmann use aerobic bacteria?', 'To detect the sites of ' + T('O₂ evolution'))
d.basic('What did Cornelius van Niel show?', 'Photosynthesis is a light-dependent reaction in which ' + T('hydrogen') + ' from an oxidisable compound reduces CO₂; the O₂ released by green plants comes from ' + T('water') + ', not CO₂')
d.basic('van Niel\'s general equation?', '2H₂A + CO₂ → 2A + CH₂O + H₂O (with light)')
d.basic('What is the hydrogen donor in purple and green sulphur bacteria? What is released?', T('H₂S') + '; they release ' + T('sulphur or sulphate') + ', ' + X('not O₂'))
d.basic('Balanced overall equation of photosynthesis?', '6CO₂ + 12H₂O → C₆H₁₂O₆ + 6H₂O + 6O₂ (with light)')
d.basic('Why 12 H₂O in the photosynthesis equation?', 'All O₂ comes from water: 6 O₂ need ' + N('12') + ' O atoms, so ' + N('12 H₂O') + ' are split; ' + N('6 H₂O') + ' are formed again')
d.basic('How was it proved that O₂ comes from water?', T('Radioisotope') + ' techniques (labelled ¹⁸O in water appears in the released O₂)')
d.basic('Is photosynthesis a single reaction?', X('No') + '. The equation summarises a multistep process.')
table_card(d, 'Early experiments', 'Who showed it?', [
    ('Plants restore air (mint, mouse, candle)', 'Priestley', False), ('Sunlight needed; green parts release O₂', 'Ingenhousz', False),
    ('Glucose made; chlorophyll in chloroplasts', 'Sachs', False), ('First action spectrum (Cladophora)', 'Engelmann', False),
    ('O₂ comes from H₂O', 'van Niel', False)], term='Early photosynthesis experiments')

# ---------------------------------------------------------------- 11.3 Where
d.sec('11.3-where')
d.basic('Where does photosynthesis occur in a plant?', 'In green leaves, and also in ' + T('other green parts') + ' (e.g. green stems)')
d.basic('Which leaf cells have many chloroplasts?', T('Mesophyll') + ' cells')
d.basic('How do chloroplasts align in mesophyll cells?', 'Along the cell walls to get ' + T('optimum light') + ': flat surfaces face the light in low light and turn parallel (edge-on) to it in strong light')
d.basic('Division of labour in the chloroplast?', T('Membranes (grana)') + ': trap light, make ATP and NADPH. ' + T('Stroma') + ': enzymatic reactions make sugar, then starch.')
d.basic('Why are "dark reactions" not really dark reactions?', 'They don\'t need light directly but depend on ' + T('ATP and NADPH') + ' from the light reaction; they ' + X('do not') + ' occur in darkness. Better name: ' + T('carbon reactions') + ' or biosynthetic phase.')
d.occlusion('Figure 11.2 · Chloroplast (electron micrograph)', M + 'fig_11_2_chloroplast.webp', (1001, 424), [
    ('Outer membrane', S(771, 1, 950, 23, (1001, 424)), True), ('Inner membrane', S(774, 39, 949, 61, (1001, 424)), True),
    ('Stromal lamella', S(766, 88, 932, 110, (1001, 424)), True), ('Grana', S(771, 152, 837, 174, (1001, 424)), True),
    ('Stroma', S(770, 230, 847, 252, (1001, 424)), True), ('Ribosomes', S(769, 267, 882, 289, (1001, 424)), True),
    ('Starch granule', S(768, 340, 924, 362, (1001, 424)), True), ('Lipid droplet', S(770, 401, 903, 423, (1001, 424)), True)])

# ---------------------------------------------------------------- 11.4 Pigments
d.sec('11.4-pigments')
d.basic('Four leaf pigments separated by paper chromatography, with colours?', T('Chlorophyll a') + ': bright/blue green. ' + T('Chlorophyll b') + ': yellow green. ' + T('Xanthophylls') + ': yellow. ' + T('Carotenoids') + ': yellow to yellow-orange.')
d.cloze('Chlorophyll a appears {{c1::bright or blue green}}; chlorophyll b appears {{c2::yellow green}} on a chromatogram.')
d.basic('What are pigments?', 'Substances that absorb light at ' + T('specific wavelengths'))
d.basic('Most abundant plant pigment in the world?', T('Chlorophyll a'))
d.basic('In which colours does chlorophyll a absorb most?', T('Blue') + ' and ' + T('red'))
d.basic('Absorption spectrum vs action spectrum?', T('Absorption') + ': how much light a pigment absorbs at each wavelength. ' + T('Action') + ': rate of photosynthesis at each wavelength.', **fig('fig_11_3_spectra'))
d.basic('Why is chlorophyll a called the chief pigment?', 'Its absorption peaks (blue, red) match the peaks of the ' + T('action spectrum'))
d.basic('Do the absorption spectrum of chlorophyll a and the action spectrum overlap exactly?', X('No') + '. Some photosynthesis happens at other wavelengths, thanks to accessory pigments.')
d.basic('Name the accessory pigments.', 'Chlorophyll b, xanthophylls, carotenoids')
d.basic('Two roles of accessory pigments?', 'Absorb a ' + T('wider range') + ' of wavelengths and pass energy to chlorophyll a; ' + T('protect') + ' chlorophyll a from photo-oxidation')
d.basic('A plant with chlorophyll b but no chlorophyll a: would it photosynthesise?', X('No') + '. Chlorophyll a forms the reaction centre; accessory pigments only pass energy to it.')
d.basic('Why does a leaf kept in the dark turn yellow?', 'Chlorophyll breaks down and is not remade without light; the more stable ' + T('carotenoids') + ' remain')
d.basic('Shade leaves vs sun leaves: which are darker green, and why?', T('Shade leaves') + ': more chlorophyll to catch the limited light')

# ---------------------------------------------------------------- 11.5 Light reaction
d.sec('11.5-light-reaction')
d.basic('What does the light reaction (photochemical phase) include?', 'Light absorption, ' + T('water splitting') + ', oxygen release, and formation of ' + T('ATP and NADPH'))
d.basic('Into what are the pigments organised?', 'Two light harvesting complexes (' + T('LHC') + ') within ' + T('PS I') + ' and ' + T('PS II'))
d.basic('Why is PS I called "I" even though PS II acts first?', 'Photosystems are named by the order of ' + T('discovery') + ', not the order they function')
d.basic('What is the antenna?', 'All the pigments of a photosystem (hundreds, bound to proteins) except the ' + T('reaction centre') + ' chlorophyll a; they harvest light')
d.basic('What forms the reaction centre?', 'A single ' + T('chlorophyll a') + ' molecule')
d.cloze('Reaction centre of PS I = {{c1::P700}}; of PS II = {{c2::P680}}.')
d.basic('Mnemonic: which reaction centre is PS II?', '"' + T('Two eight') + '" is the first to act: PS II = P680 (shorter wavelength, acts first); PS I = P700.')
d.occlusion('Figure 11.4 · Light harvesting complex', M + 'fig_11_4_lhc.webp', (1000, 854), [
    ('Photon', S(40, 404, 181, 445, (1000, 854)), True), ('Reaction centre', S(599, 389, 773, 478, (1000, 854)), True),
    ('Pigment molecules', S(776, 595, 975, 684, (1000, 854)), True), ('Primary acceptor', S(296, 72, 636, 113, (1000, 854)), True)])

# ---------------------------------------------------------------- 11.6 Electron transport
d.sec('11.6-electron-transport')
d.basic('What happens when P680 absorbs red light?', 'Electrons are ' + T('excited') + ' and picked up by an electron acceptor, then passed to an ETS of ' + T('cytochromes'))
d.basic('Are electrons used up in the ETS between PS II and PS I?', X('No') + '. They pass downhill (redox scale) to the pigments of PS I.')
d.basic('Where do electrons from PS I finally go?', 'To ' + T('NADP⁺') + ', reducing it to ' + T('NADPH + H⁺'))
d.basic('What is the Z scheme?', 'The electron path PS II → acceptor → ETS → PS I → acceptor → NADP⁺; it looks like a ' + T('Z') + ' when carriers are placed on a redox potential scale')
d.occlusion('Figure 11.5 · Z scheme of light reaction', M + 'fig_11_5_z_scheme.webp', (1001, 862), [
    ('Photosystem II', S(148, 40, 418, 78, (1001, 862)), True), ('Photosystem I', S(491, 45, 748, 83, (1001, 862)), True),
    ('Electron transport system', S(388, 348, 559, 474, (1001, 862)), True), ('NADP⁺ → NADPH', S(826, 157, 1001, 267, (1001, 862)), True),
    ('2e⁻ + 2H⁺ + [O]', S(619, 784, 873, 837, (1001, 862)), True), ('ADP + Pi → ATP', S(390, 244, 612, 280, (1001, 862)), True)])

d.sec('11.6.1-water-splitting')
d.basic('How does PS II get its electrons replaced?', 'By ' + T('splitting of water'))
d.basic('Water splitting equation?', '2H₂O → 4H⁺ + O₂ + 4e⁻')
d.basic('Water splitting is associated with which photosystem?', T('PS II'))
d.basic('On which side of the thylakoid membrane is the water-splitting complex?', 'The ' + T('inner side') + ' (lumen side); so H⁺ and O₂ are released into the ' + T('lumen'))
d.basic('Where do the electrons that replace those lost by PS I come from?', 'From ' + T('PS II'))

d.sec('11.6.2-photophosphorylation')
d.basic('What is photophosphorylation?', 'Synthesis of ATP from ADP and Pi in the presence of ' + T('light'))
d.basic('What is non-cyclic photophosphorylation?', 'PS II and PS I work ' + T('in series') + ' (Z scheme); makes both ' + T('ATP and NADPH'))
d.basic('What is cyclic photophosphorylation?', 'Only ' + T('PS I') + ' works; the electron cycles back to PS I through the ETS; only ' + T('ATP') + ' is made, ' + X('no NADPH'))
d.basic('Where may cyclic photophosphorylation occur, and why there?', 'In the ' + T('stroma lamellae') + ': they lack PS II and NADP reductase', **fig('fig_11_6_cyclic'))
d.basic('When else does cyclic photophosphorylation occur?', 'When only light of wavelength ' + T('beyond 680 nm') + ' is available')
d.basic('Grana lamellae vs stroma lamellae: photosystems?', 'Grana: ' + T('PS I and PS II') + '. Stroma lamellae: ' + T('PS I only') + '.')
table_card(d, 'Photophosphorylation', 'Cyclic vs non-cyclic?', [
    ('Photosystems', 'Cyclic: PS I · Non-cyclic: PS I + PS II', False), ('Products', 'Cyclic: ATP only · Non-cyclic: ATP + NADPH', False),
    ('Water split, O₂ released?', 'Cyclic: no · Non-cyclic: yes', False), ('Location', 'Cyclic: stroma lamellae · Non-cyclic: grana', False)],
    term='Cyclic vs non-cyclic photophosphorylation')

d.sec('11.6.3-chemiosmosis')
d.basic('What does the chemiosmotic hypothesis explain?', 'How ATP is made: ATP synthesis is linked to a ' + T('proton gradient') + ' across a membrane (here the thylakoid)')
d.basic('Where do protons accumulate in photosynthesis vs respiration?', 'Photosynthesis: thylakoid ' + T('lumen') + '. Respiration: mitochondrial ' + T('intermembrane space') + '.')
d.basic('Three causes of the proton gradient across the thylakoid?', '(a) ' + T('Water splitting') + ' inside releases H⁺ into the lumen. (b) The primary acceptor passes electrons to an ' + T('H carrier') + ', which moves H⁺ from stroma to lumen. (c) ' + T('NADP reductase') + ' on the stroma side uses up H⁺ from the stroma.')
d.basic('What happens to lumen pH during the light reaction?', 'It ' + T('decreases') + ' (more acidic) as H⁺ accumulates')
d.basic('How does the gradient make ATP?', 'H⁺ flow back to the stroma through the ' + T('CF₀') + ' channel of ATP synthase; the energy changes the conformation of ' + T('CF₁') + ', which makes ATP')
d.cloze('ATP synthase: {{c1::CF₀}} is embedded in the membrane and forms the proton channel; {{c2::CF₁}} protrudes on the stroma side and makes ATP.')
d.basic('Four requirements of chemiosmosis?', 'A membrane, a ' + T('proton pump') + ', a ' + T('proton gradient') + ' and ' + T('ATP synthase'))
d.basic('Figure 11.7: trace the protons.', 'H⁺ from water splitting and the PQ shuttle collect in the lumen (high H⁺); they return to the stroma (low H⁺) through ATP synthase, making ATP', **img('fig_11_7_chemiosmosis'))
d.basic('Intuition: chemiosmosis is like a…?', 'A ' + T('dam') + ': the light reaction pumps water (H⁺) uphill into the reservoir (lumen); ATP synthase is the turbine it flows back through')

# ---------------------------------------------------------------- 11.7 Calvin cycle
d.sec('11.7-biosynthetic')
d.basic('Products of the light reaction and their fate?', T('O₂') + ' diffuses out; ' + T('ATP and NADPH') + ' drive sugar synthesis in the stroma')
d.basic('How can you show the biosynthetic phase depends on light products?', 'After light is switched off it ' + T('continues briefly then stops') + '; it restarts when light returns')
d.basic('Which isotope did Calvin use, and in what organism?', T('¹⁴C') + ', in ' + T('algal') + ' photosynthesis')
d.basic('First stable product of CO₂ fixation found by Calvin?', T('3-phosphoglyceric acid (PGA)') + ': a ' + N('3-carbon') + ' acid')
d.basic('First product in C4 plants?', T('Oxaloacetic acid (OAA)') + ': a ' + N('4-carbon') + ' acid')
d.basic('Primary CO₂ acceptor in the Calvin cycle?', T('Ribulose bisphosphate (RuBP)') + ': a ' + N('5-carbon') + ' ketose sugar')
d.basic('Why did scientists first look for a 2-carbon CO₂ acceptor?', 'The first product (PGA) had 3 carbons, so they assumed 2 + 1. It was actually 5 + 1 → 2 × 3.')
d.basic('Does the Calvin cycle occur in C4 plants too?', T('Yes') + '. It occurs in ' + T('all') + ' photosynthetic plants.')
d.cloze('Calvin cycle stages: {{c1::carboxylation}} → {{c2::reduction}} → {{c3::regeneration}}.')
d.basic('What is carboxylation?', 'Fixation of CO₂ into a stable organic intermediate: ' + T('RuBP + CO₂ → 2 × 3-PGA') + ', by RuBisCO')
d.basic('Most crucial step of the Calvin cycle?', T('Carboxylation'))
d.basic('Why is RuBP carboxylase better called RuBisCO?', 'It also has ' + T('oxygenase') + ' activity: RuBP carboxylase-oxygenase')
d.basic('Reduction step uses what per CO₂ fixed?', N('2 ATP') + ' (phosphorylation) and ' + N('2 NADPH') + ' (reduction)')
d.basic('Regeneration step uses what per CO₂?', N('1 ATP') + ' to regenerate RuBP')
d.basic('ATP and NADPH per CO₂ fixed?', N('3 ATP') + ' and ' + N('2 NADPH'))
d.basic('How many turns of the Calvin cycle make one glucose?', N('6') + ' (6 CO₂ fixed)')
table_card(d, 'Calvin cycle', 'In → out, for one glucose?', [
    ('6 CO₂', '1 glucose', False), ('18 ATP', '18 ADP', False), ('12 NADPH', '12 NADP⁺', False)], term='Calvin cycle: inputs and outputs per glucose')
d.basic('Why is cyclic photophosphorylation needed?', 'Calvin cycle needs ATP : NADPH = ' + N('3 : 2') + '; non-cyclic flow gives them roughly equally, so cyclic flow makes the ' + T('extra ATP'))
d.occlusion('Figure 11.8 · Calvin cycle', M + 'fig_11_8_calvin.webp', (880, 1001), [
    ('Ribulose-1,5-bisphosphate (RuBP)', S(331, 84, 496, 137, (880, 1001))), ('Carboxylation', S(574, 189, 745, 213, (880, 1001)), True),
    ('3-phosphoglycerate', S(597, 432, 836, 456, (880, 1001)), True), ('Reduction', S(583, 660, 706, 684, (880, 1001)), True),
    ('ATP + NADPH', S(763, 632, 852, 713, (880, 1001)), True), ('Triose phosphate', S(356, 744, 485, 797, (880, 1001)), True),
    ('Regeneration', S(36, 409, 198, 433, (880, 1001)), True)])

# ---------------------------------------------------------------- 11.8 C4
d.sec('11.8-c4')
d.basic('Where are C4 plants adapted?', T('Dry tropical') + ' regions')
d.basic('Main biosynthetic pathway in C4 plants?', 'Still the ' + T('Calvin cycle') + ' (C3 pathway)')
d.basic('Special features of C4 plants?', T('Kranz anatomy') + ', tolerate ' + T('higher temperatures') + ', respond to high light, ' + X('lack photorespiration') + ', greater biomass productivity')
d.basic('What is Kranz anatomy?', 'Large ' + T('bundle sheath cells') + ' around vascular bundles, arranged like a wreath')
d.basic('What does "Kranz" mean?', T('Wreath'))
d.basic('Features of bundle sheath cells in C4 plants?', 'Many ' + T('chloroplasts') + ', thick walls ' + T('impervious to gas exchange') + ', ' + X('no intercellular spaces') + '; may form several layers')
d.basic('Examples of C4 plants?', E('Maize, sorghum') + ' (also sugarcane)')
d.basic('Can you tell C3 from C4 by looking at a plant from outside?', X('Not reliably') + '. You need a leaf section to see Kranz anatomy.')
d.basic('Other name of the C4 pathway?', T('Hatch and Slack pathway'))
d.basic('Primary CO₂ acceptor in C4 plants?', T('Phosphoenol pyruvate (PEP)') + ': ' + N('3-carbon') + ', in mesophyll cells')
d.basic('Enzyme that fixes CO₂ in C4 mesophyll?', T('PEP carboxylase (PEPcase)'))
d.basic('Do C4 mesophyll cells have RuBisCO?', X('No'))
d.basic('C4 pathway steps?', 'Mesophyll: PEP + CO₂ → ' + T('OAA') + ' → malic or aspartic acid → bundle sheath: C4 acid breaks down to ' + T('CO₂ + 3C molecule') + ' → CO₂ enters the Calvin cycle; the 3C molecule returns to mesophyll → PEP', **fig('fig_11_9_hatch_slack'))
d.basic('Bundle sheath cells of C4 plants: RuBisCO and PEPcase?', 'Rich in ' + T('RuBisCO') + ', ' + X('lack PEPcase'))
d.basic('Where does the Calvin cycle run in C3 vs C4 plants?', 'C3: all ' + T('mesophyll') + ' cells. C4: only ' + T('bundle sheath') + ' cells.')
d.basic('C4 plants run the Calvin cycle in few cells yet are more productive. Why?', 'CO₂ is ' + T('concentrated') + ' at RuBisCO in bundle sheath cells, so there is no photorespiration')

# ---------------------------------------------------------------- 11.9 Photorespiration
d.sec('11.9-photorespiration')
d.basic('Most abundant enzyme in the world?', T('RuBisCO'))
d.basic('Why can RuBisCO bind O₂?', 'Its active site binds both ' + T('CO₂ and O₂') + '; binding is ' + T('competitive') + ' and depends on their relative concentrations')
d.basic('When does RuBisCO favour CO₂?', 'When CO₂ : O₂ is ' + T('nearly equal') + ' (it has much greater affinity for CO₂)')
d.basic('What happens in photorespiration?', 'RuBP + O₂ → one ' + T('phosphoglycerate') + ' + one ' + T('phosphoglycolate') + ' (2C)')
d.basic('Photorespiration produces sugar, ATP or NADPH?', X('None') + '. It releases CO₂ and uses ATP.')
d.basic('Biological function of photorespiration?', X('Not known') + ' (per NCERT)')
d.basic('Beyond NCERT: which organelles take part in photorespiration?', T('Chloroplast, peroxisome, mitochondrion') + '. Many scientists now think it protects against photo-damage and recycles carbon lost as glycolate.')
d.basic('Why don\'t C4 plants show photorespiration?', 'C4 acids release CO₂ in bundle sheath cells, ' + T('raising CO₂') + ' at RuBisCO, so it acts as a carboxylase')
table_card(d, 'Table 11.1', 'C3 vs C4?', [
    ('Calvin cycle in', 'C3: mesophyll · C4: bundle sheath', False), ('Initial carboxylation in', 'C3: mesophyll · C4: mesophyll', False),
    ('Primary CO₂ acceptor', 'C3: RuBP (5C) · C4: PEP (3C)', False), ('First product', 'C3: PGA (3C) · C4: OAA (4C)', False),
    ('PEPcase?', 'C3: no · C4: yes', False), ('Photorespiration at high light', 'C3: high · C4: negligible', False),
    ('Temperature optimum', 'C3: 20–25 °C · C4: 30–40 °C', False)], term='Table 11.1: C3 vs C4 plants')
d.basic('C3 vs C4: CO₂ fixation rate under high light?', 'C3: ' + T('low') + '. C4: ' + T('high') + '.')
d.basic('Photorespiration at low vs high CO₂ (C3 plants)?', 'Low CO₂: ' + T('high') + '. High CO₂: ' + T('negligible') + '.')

# ---------------------------------------------------------------- 11.10 Factors
d.sec('11.10-factors')
d.basic('Internal (plant) factors affecting photosynthesis?', 'Number, size, age and orientation of leaves; mesophyll cells and chloroplasts; internal CO₂; amount of chlorophyll')
d.basic('External factors affecting photosynthesis?', 'Sunlight, temperature, ' + T('CO₂') + ' concentration, water')
d.basic('State Blackman\'s law of limiting factors (1905).', 'If a process is affected by more than one factor, its rate is determined by the factor ' + T('nearest to its minimal value'))
d.basic('Example of Blackman\'s law?', 'A green leaf with optimal light and CO₂ will ' + X('not') + ' photosynthesise if the ' + T('temperature') + ' is very low')
d.basic('Three aspects of light as a factor?', T('Quality, intensity') + ' and ' + T('duration'))
d.basic('Light intensity vs CO₂ fixation rate?', T('Linear') + ' at low intensity; levels off at high intensity as other factors limit')
d.basic('At what fraction of full sunlight does light saturation occur?', N('10%'))
d.basic('Is light usually limiting in nature?', X('Rarely') + ', except for plants in shade or dense forests')
d.basic('What happens with very high light?', T('Chlorophyll breaks down') + ' and photosynthesis decreases')
d.basic('Figure 11.10: where is light limiting, and what are C and D?', 'Region ' + T('A') + ' (rising line): light limiting. Plateau ' + T('C') + ': other factors limiting (maximum rate). ' + T('D') + ': light saturation point.', **img('fig_11_10_light_curve'))
d.basic('Major limiting factor for photosynthesis?', T('CO₂'))
d.basic('CO₂ concentration in the atmosphere?', N('0.03–0.04%') + '. Up to ' + N('0.05%') + ' increases fixation; beyond that it can damage over long periods.')
d.basic('Update: atmospheric CO₂ today?', 'About ' + N('0.042%') + ' (≈420 ppm) and rising; NCERT\'s 0.03–0.04% is from older data')
d.basic('CO₂ saturation points of C4 vs C3?', 'C4: about ' + N('360 µL/L') + '. C3: only beyond ' + N('450 µL/L') + ' (so current CO₂ limits C3 plants).')
d.basic('At low light, do C3 or C4 plants respond to high CO₂?', X('Neither'))
d.basic('Which greenhouse crops are grown in CO₂-enriched air?', E('Tomatoes, bell pepper') + ' (C3 plants: higher yield)')
d.basic('Light vs dark reactions: temperature sensitivity?', 'Dark reactions (enzymatic) are ' + T('temperature controlled') + '; light reactions are affected much less')
d.basic('C3 vs C4 temperature optimum?', 'C4: ' + T('higher') + '. C3: much lower. Tropical plants have higher optima than temperate plants.')
d.basic('How does water stress reduce photosynthesis?', 'Stomata ' + T('close') + ' (less CO₂); leaves wilt (less surface area and metabolic activity). The effect is on the ' + T('plant') + ', not directly on the reaction.')

d.sec('summary')
d.basic('Correction: NCERT\'s summary says electrons go "finally to NAD forming NADH". What is right?', 'In photosynthesis the final acceptor is ' + T('NADP⁺') + ', forming ' + T('NADPH') + '. NAD⁺/NADH is used in respiration.')
d.basic('Light reaction vs dark reaction: location and products?', 'Light: ' + T('thylakoid membranes') + '; makes ATP, NADPH, O₂. Dark (carbon): ' + T('stroma') + '; makes sugars using ATP and NADPH.')

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
