import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Chemistry', 'class11-chemistry-ch01-some-basic-concepts-of-chemistry')
d = Deck('Chapter 1: Some Basic Concepts of Chemistry', 'Class 11', ['class-11', 'chemistry', 'ch-1'])
d.description = 'Matter, SI units, significant figures, laws of combination, mole concept, empirical formula, stoichiometry and concentration terms'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}
CL = (1001, 529)

# ---------------------------------------------------------------- intro
d.sec('1.0-development-of-chemistry')
d.basic('Define chemistry.', 'The branch of science that studies the ' + T('preparation, properties, structure and reactions') + ' of material substances')
d.cloze('Chemistry arose from the search for the {{c1::philosopher’s stone (Paras)}}, to turn base metals into gold, and the {{c2::elixir of life}}, to grant immortality.')
d.basic('In what forms did chemistry develop during 1300–1600 CE?', T('Alchemy') + ' and ' + T('Iatrochemistry'))
d.basic('Ancient Indian names for chemistry?', T('Rasayan Shastra') + ', Rastantra, Ras Kriya or Rasvidya')
d.basic('What did the Harappans use to harden copper?', T('Tin and arsenic'))
d.basic('What was faience?', 'A sort of ' + T('glass') + ' made by the Harappans, used in ornaments')
d.basic('Which ancient text mentions preparing sulphuric acid, nitric acid and metal oxides?', T('Charaka Samhita'))
d.basic('Which text describes the preparation of gunpowder?', T('Rasopanishada'))
d.basic('Nagarjuna’s work on mercury compounds?', T('Rasratnakar'))
d.basic('Who discovered mercury sulphide and is credited with inventing soap?', T('Chakrapani') + ' (used mustard oil and alkalies)')
d.basic('Who first proposed an atomic theory in India, and what did he call atoms?', T('Acharya Kanda') + ' (Kashyap, ~600 BCE), in the Vaiseshika Sutras; atoms = "' + T('Paramãnu') + '"')
d.basic('Properties of Kanda’s Paramãnu?', 'Eternal, indestructible, spherical, ' + T('suprasensible') + ' and in motion; could form pairs or triplets')
d.basic('Bhasmas of Charaka Samhita are now known to contain?', 'Metal ' + T('nanoparticles') + ' (extreme particle-size reduction = nanotechnology)')
d.basic('Correction: NCERT says paper was known in India "in the 17th century" per I-tsing. Actually?', 'I-tsing travelled in the ' + T('7th century CE') + '; "17th" is a typo')

d.sec('1.1-importance-of-chemistry')
d.basic('Two anticancer drugs named in NCERT?', E('Cisplatin') + ' and ' + E('taxol'))
d.basic('Drug used for AIDS patients?', E('AZT') + ' (azidothymidine)')
d.basic('Examples of new materials designed with chemistry?', E('Superconducting ceramics') + ', ' + E('conducting polymers') + ', ' + E('optical fibres'))
d.basic('Refrigerants replaced because of ozone depletion?', T('CFCs') + ' (chlorofluorocarbons)')

# ---------------------------------------------------------------- 1.2 Nature of matter
d.sec('1.2-nature-of-matter')
d.basic('Define matter.', 'Anything that has ' + T('mass') + ' and occupies ' + T('space'))
table_card(d, 'States of matter', 'Definite shape / volume?', [
    ('Solid', 'Definite volume and definite shape', False),
    ('Liquid', 'Definite volume, no definite shape', False),
    ('Gas', 'Neither definite volume nor shape', True)], term='States of matter: shape and volume')
d.basic('Particle arrangement in the three states?', 'Solid: close, orderly, little movement. Liquid: close but mobile. Gas: far apart, fast.', **fig('fig_1_1_states'))
d.basic('How are the states interconverted?', 'By changing ' + T('temperature and pressure'))
d.occlusion('Figure 1.2 · Classification of matter', M + 'fig_1_2_classification.webp', CL, [
    ('Mixtures', [117, 212, 197, 104], True), ('Pure substances', [679, 212, 209, 104], True),
    ('Homogeneous mixtures', [3, 422, 199, 106], True), ('Heterogeneous mixtures', [227, 422, 199, 106], True),
    ('Elements', [572, 422, 199, 106], True), ('Compounds', [796, 422, 199, 106], True)])
d.basic('Pure substance vs mixture?', T('Pure substance') + ': all particles of the same chemical nature, fixed composition<br>' + T('Mixture') + ': two or more substances in ' + T('any ratio') + ' (variable composition)')
d.basic('Homogeneous vs heterogeneous mixture?', T('Homogeneous') + ': uniform composition throughout (' + E('sugar solution, air') + ')<br>' + T('Heterogeneous') + ': not uniform (' + E('salt + sugar, grains with dirt') + ')')
d.basic('How are components of a mixture separated?', 'By ' + T('physical methods') + ': hand-picking, filtration, crystallisation, distillation')
d.basic('Is air a compound or a mixture? (trap)', 'A ' + T('homogeneous mixture') + ': its composition varies and components keep their properties')
d.basic('Element vs compound?', T('Element') + ': only one type of atom (as atoms or molecules)<br>' + T('Compound') + ': atoms of different elements in a ' + T('fixed ratio') + '; separable only by chemical methods')
d.basic('Elements whose particles are atoms vs molecules?', 'Atoms: ' + E('Na, Cu') + '. Diatomic molecules: ' + E('H₂, N₂, O₂') + '.', **fig('fig_1_3_atoms_molecules'))
d.basic('Identify the molecules shown.', 'Water (' + T('H₂O') + ': 2 H + 1 O) and carbon dioxide (' + T('CO₂') + ': 1 C + 2 O)', **img('fig_1_4_h2o_co2'))
d.basic('How does water show that compound properties differ from its elements?', 'H₂ burns with a pop and O₂ supports combustion, but ' + T('water extinguishes fire'))

# ---------------------------------------------------------------- 1.3 Properties and measurement
d.sec('1.3-properties-and-measurement')
d.basic('Physical vs chemical property?', T('Physical') + ': measured without changing identity (colour, m.p., density)<br>' + T('Chemical') + ': needs a chemical change (combustibility, acidity)')
d.basic('When and by whom was the SI established?', 'In ' + N('1960') + ' by the ' + T('11th CGPM') + ' (General Conference on Weights and Measures)')
d.basic('Treaty that created the CGPM?', 'The ' + T('Metre Convention') + ', Paris, ' + N('1875'))
d.basic('Which Indian lab maintains the national standards of measurement?', T('National Physical Laboratory (NPL)') + ', New Delhi')
table_card(d, 'Table 1.1', 'SI unit?', [
    ('Length', 'metre (m)', False), ('Mass', 'kilogram (kg)', False), ('Time', 'second (s)', False),
    ('Electric current', 'ampere (A)', False), ('Thermodynamic temperature', 'kelvin (K)', False),
    ('Amount of substance', 'mole (mol)', False), ('Luminous intensity', 'candela (cd)', False)], term='The seven SI base units')
d.basic('Mnemonic for the 7 SI base quantities?', '"' + T('LMT CTAL') + '": Length, Mass, Time, Current, Temperature, Amount, Luminous intensity')
d.basic('How is the kilogram defined now (Table 1.2)?', 'By fixing the ' + T('Planck constant') + ' h = ' + N('6.62607015 × 10⁻³⁴') + ' J s')
d.basic('Which constant fixes the kelvin? The ampere?', 'Kelvin: ' + T('Boltzmann constant') + ' k = 1.380649 × 10⁻²³ J K⁻¹. Ampere: ' + T('elementary charge') + ' e = 1.602176634 × 10⁻¹⁹ C.')
d.basic('What defines the second?', 'The caesium-133 hyperfine frequency fixed at ' + N('9192631770') + ' Hz')
d.basic('Update: NCERT’s box says the kilogram standard is still a Pt-Ir cylinder. Current status?', 'Since ' + N('20 May 2019') + ' the kg is defined through the ' + T('Planck constant') + '.<br>The Pt-Ir prototype is retired (Table 1.2 already uses the new definition)')
d.basic('Why was Pt-Ir chosen for the old kilogram prototype?', 'Highly ' + T('resistant to chemical attack') + ', so its mass stays constant')
d.basic('1983 definition of the metre?', 'Path travelled by light in vacuum in ' + N('1/299 792 458') + ' of a second')
d.cloze('SI prefixes: pico = {{c1::10⁻¹²}}, nano = {{c2::10⁻⁹}}, micro = {{c3::10⁻⁶}}, milli = 10⁻³.')
d.cloze('SI prefixes: kilo = 10³, mega = {{c1::10⁶}}, giga = {{c2::10⁹}}, tera = {{c3::10¹²}}.')
d.cloze('femto = {{c1::10⁻¹⁵}}; atto = {{c2::10⁻¹⁸}}; deca = {{c3::10}}; hecto = {{c4::10²}}.')
d.basic('Full list of SI prefixes (Table 1.3)?', 'yocto 10⁻²⁴ … yotta 10²⁴', **fig('tab_1_3_prefixes'))
d.basic('Mass vs weight?', T('Mass') + ': amount of matter, constant. ' + T('Weight') + ': force of gravity on it, varies with place.')
d.basic('Instrument for accurate mass in the lab?', T('Analytical balance'), **fig('fig_1_5_balance'))
d.cloze('1 L = {{c1::1000 mL}} = {{c2::1000 cm³}} = {{c3::1 dm³}}.', extra='The litre is ' + X('not') + ' an SI unit; SI volume is m³.')
d.basic('How many litres in 1 m³?', N('1000 L') + ' (1 m³ = 10⁶ cm³)', **fig('fig_1_6_volume_units'))
d.basic('Name the volume measuring devices.', 'Burette, pipette, graduated cylinder, ' + T('volumetric flask') + ' (to prepare a known volume of solution)', **img('fig_1_7_volume_devices'))
d.basic('SI unit of density, and the unit chemists use?', T('kg m⁻³') + '; chemists use ' + T('g cm⁻³'))
d.basic('What does a higher density tell you?', 'Particles are more ' + T('closely packed'))
d.basic('Relation between °F and °C?', r'\( ^{\circ}F = \frac{9}{5}(^{\circ}C) + 32 \)')
d.basic('Relation between K and °C?', r'\( K = {}^{\circ}C + 273.15 \)', **fig('fig_1_8_thermometers'))
d.cloze('Water freezes at {{c1::273.15 K}} = 0 °C = {{c2::32 °F}} and boils at 373 K = 100 °C = {{c3::212 °F}}.')
d.basic('At what temperature are °C and °F equal? (trap)', N('−40°') + ': solve \\( x = \\frac{9}{5}x + 32 \\)')
d.basic('Can temperature be negative on the Kelvin scale?', X('No') + '; negative values are possible only on the Celsius (and Fahrenheit) scale')
d.basic('Human body temperature on the three scales?', N('37 °C') + ' = ' + N('310 K') + ' = ' + N('98.6 °F'))

# ---------------------------------------------------------------- 1.4 Uncertainty
d.sec('1.4-uncertainty-in-measurement')
d.basic('Form of scientific notation?', r'\( N \times 10^{n} \)' + ', where N (digit term) is from ' + N('1.000…') + ' to ' + N('9.999…'))
d.basic('Write 232.508 and 0.00016 in scientific notation.', r'\( 2.32508 \times 10^{2} \)' + ' and ' + r'\( 1.6 \times 10^{-4} \)')
d.basic('Rule for adding numbers in scientific notation?', 'First bring them to the ' + T('same exponent') + ', then add the digit terms')
d.basic('What are significant figures?', 'Meaningful digits known with certainty ' + T('plus one uncertain') + ' (estimated) digit')
d.cloze('Sig-fig rules: all {{c1::non-zero}} digits count; zeros {{c2::before}} the first non-zero digit do not; zeros {{c3::between}} non-zero digits do.')
d.basic('Are trailing zeros significant?', 'Only if there is a ' + T('decimal point') + ': 0.200 has ' + N('3') + '; 100 has ' + N('1') + '; 100.0 has ' + N('4'))
d.basic('How many sig figs in an exact count like "20 eggs"?', T('Infinite') + ' (exact numbers)')
d.basic('Sig figs in 4.01 × 10² and 8.256 × 10⁻³?', N('3') + ' and ' + N('4') + ' (all digits in scientific notation are significant)')
d.basic('Sig figs in 0.0025, 208, 5005, 126,000, 500.0, 2.0034? (Ex 1.19)', N('2, 3, 4, 3, 4, 5'))
d.basic('How do you write 100 with exactly 2 sig figs?', r'\( 1.0 \times 10^{2} \)')
d.basic('Precision vs accuracy?', T('Precision') + ': closeness of repeated measurements to each other. ' + T('Accuracy') + ': closeness to the ' + T('true value') + '.')
table_card(d, 'Table 1.4 · true value 2.00 g', 'Precise? Accurate?', [
    ('A: 1.95, 1.93', 'Precise, not accurate', True), ('B: 1.94, 2.05', 'Neither', True),
    ('C: 2.01, 1.99', 'Precise and accurate', False)], term='Precision vs accuracy data')
d.basic('Rule for sig figs in addition/subtraction?', 'Result has no more ' + T('decimal places') + ' than the number with the fewest (12.11 + 18.0 + 1.012 = ' + N('31.1') + ')')
d.basic('Rule for sig figs in multiplication/division?', 'Result has no more ' + T('significant figures') + ' than the least precise number (2.5 × 1.25 = ' + N('3.1') + ')')
d.cloze('Rounding when the dropped digit is exactly 5: if the preceding digit is {{c1::even}}, leave it; if {{c2::odd}}, add one. So 6.35 → {{c3::6.4}}, 6.25 → {{c4::6.2}}.')
d.basic('Round to 3 sig figs: 34.216, 10.4107, 0.04597, 2808. (Ex 1.20)', N('34.2, 10.4, 0.0460, 2810'))
d.basic('Other names of dimensional analysis?', T('Factor label method') + ' or ' + T('unit factor method'))
d.basic('What is a unit factor?', 'A ratio equal to 1, e.g. 2.54 cm / 1 in; multiply so unwanted units ' + T('cancel'))
steps_card(d, 'Dimensional analysis', 'A jug holds 2 L of milk. Volume in m³?', '1 L = 1000 cm³; 1 m = 100 cm.',
           ['2 L = 2 × 1000 cm³ = 2000 cm³', '(1 m / 100 cm)³ = 1 m³ / 10⁶ cm³', '2000 cm³ × 1 m³/10⁶ cm³ = <b>2 × 10⁻³ m³</b>'], 1, 'Convert 2 L to m³', '2 × 10⁻³ m³')
d.basic('Seconds in 2 days?', '2 × 24 × 60 × 60 = ' + N('172800 s'))
d.basic('Distance covered by light in 2.00 ns (c = 3.0 × 10⁸ m/s)? (Ex 1.22)', r'\( 3.0 \times 10^{8} \times 2.00 \times 10^{-9} = 0.600 \)' + ' m')

# ---------------------------------------------------------------- 1.5 Laws of chemical combination
d.sec('1.5-laws-of-chemical-combination')
d.basic('Law of conservation of mass: who and when?', T('Antoine Lavoisier') + ', ' + N('1789') + ': matter can neither be created nor destroyed')
d.basic('Law of definite proportions: who, and statement?', T('Joseph Proust') + ': a given compound always contains exactly the same proportion of elements ' + T('by weight'))
d.basic('Compound Proust used to prove definite proportions?', T('Cupric carbonate') + ', natural vs synthetic: Cu ' + N('51.35%') + ', C ' + N('9.74%') + ', O ' + N('38.91%') + ' in both')
d.basic('Another name for the law of definite proportions?', T('Law of definite composition'))
d.basic('Law of multiple proportions: who, when, statement?', T('Dalton') + ', ' + N('1803') + ':<br>when two elements form more than one compound, the masses of one that combine with a fixed mass of the other are in a ' + T('small whole-number ratio'))
d.basic('NCERT example of multiple proportions?', E('H₂O and H₂O₂') + ': 16 g and 32 g O per 2 g H → ' + N('1 : 2'))
d.basic('N₂ + O₂ data: 14:16, 14:32, 28:32, 28:80. Which law? (Ex 1.21)', T('Multiple proportions') + ': O per 14 g N = 16, 32, 16, 40 → ' + N('2 : 4 : 2 : 5'))
d.basic('Gay Lussac’s law (1808)?', 'Gases combine or are produced in a ' + T('simple ratio by volume') + ' at the same T and P')
d.basic('H₂ + O₂ → water vapour: volumes?', N('100 mL + 50 mL → 100 mL') + ' (2 : 1 : 2)')
d.basic('Gay Lussac’s law is really which law, by volume?', 'The law of ' + T('definite proportions by volume'))
d.basic('Avogadro’s law (1811)?', T('Equal volumes') + ' of all gases at the same T and P contain ' + T('equal numbers of molecules'), **fig('fig_1_9_avogadro_volumes'))
d.basic('What key idea let Avogadro explain Gay Lussac’s data?', 'Distinguishing ' + T('atoms from molecules') + ': H₂ and O₂ are ' + T('diatomic'))
d.basic('Why was Avogadro ignored at first?', 'Dalton and others believed atoms of the same kind ' + X('could not combine') + ', so O₂/H₂ molecules couldn’t exist')
d.basic('Who revived Avogadro’s work, where and when?', T('Stanislao Cannizzaro') + ', first international chemistry conference, ' + T('Karlsruhe') + ', ' + N('1860'))

# ---------------------------------------------------------------- 1.6 Dalton
d.sec('1.6-daltons-atomic-theory')
d.basic('Dalton’s book (1808)?', '"' + T('A New System of Chemical Philosophy') + '"')
d.cloze('Dalton: matter consists of {{c1::indivisible atoms}}; atoms of an element have identical {{c2::mass}}; compounds form in a {{c3::fixed ratio}}; reactions only {{c4::reorganise}} atoms.')
d.basic('What could Dalton’s theory NOT explain?', 'The ' + X('law of gaseous volumes') + ', and ' + X('why atoms combine'))
d.basic('Greek philosopher behind "a-tomio" (indivisible)?', T('Democritus') + ' (460–370 BC)')
d.basic('Correction: NCERT prints Dalton’s dates as 1776–1884. Actual?', T('1766–1844') + ' (NCERT itself says 1766–1844 on page 3)')
d.basic('Update: which of Dalton’s postulates are known to be wrong today?', 'Atoms ' + X('are divisible') + ' (e, p, n); atoms of an element can differ in mass (' + T('isotopes') + ')')

# ---------------------------------------------------------------- 1.7 Atomic and molecular masses
d.sec('1.7-atomic-and-molecular-masses')
d.basic('Present standard for atomic masses, adopted when?', T('Carbon-12') + ', assigned exactly ' + N('12 amu') + ', in ' + N('1961'))
d.basic('Define 1 amu.', 'Exactly ' + T('1/12 of the mass of one ¹²C atom') + ' = ' + N('1.66056 × 10⁻²⁴ g'))
d.basic('What replaced "amu"?', T('u') + ' (unified mass)')
d.basic('Mass of an H atom in u?', '1.6736 × 10⁻²⁴ / 1.66056 × 10⁻²⁴ = ' + N('1.0078 u'))
d.basic('Why is the atomic mass in the periodic table not a whole number?', 'It is the ' + T('average atomic mass') + ', weighted by the natural abundance of isotopes')
steps_card(d, 'Average atomic mass', 'Average atomic mass of chlorine? (Ex 1.9)', '³⁵Cl: 75.77%, 34.9689 u. ³⁷Cl: 24.23%, 36.9659 u.',
           ['0.7577 × 34.9689 = 26.496', '0.2423 × 36.9659 = 8.957', 'Sum = <b>35.45 u</b>'], 2, 'Average atomic mass of Cl', '35.45 u')
d.basic('Average atomic mass of carbon from its isotopes?', N('12.011 u') + ' (¹²C 98.892%, ¹³C 1.108%, ¹⁴C trace)')
d.basic('Why does NCERT’s carbon table show ¹⁴C as 2 × 10⁻¹⁰ but use 2 × 10⁻¹² in the sum?', 'The table is in ' + T('per cent') + '; the sum uses a ' + T('fraction') + ' (÷ 100). Same quantity; ¹⁴C adds nothing measurable.')
d.basic('Define molecular mass.', 'Sum of the atomic masses of all atoms in a molecule')
d.basic('Molecular mass of CH₄ and H₂O?', 'CH₄ = ' + N('16.043 u') + '; H₂O = ' + N('18.02 u'))
d.basic('Molecular mass of glucose C₆H₁₂O₆? (Problem 1.1)', '6(12.011) + 12(1.008) + 6(16.00) = ' + N('180.162 u'))
d.basic('Why "formula mass" for NaCl, not molecular mass?', 'NaCl has ' + X('no discrete molecules') + ': it is a 3D network of Na⁺ and Cl⁻ ions', **fig('fig_1_10_nacl'))
d.basic('Coordination in NaCl crystal?', 'Each Na⁺ is surrounded by ' + N('six') + ' Cl⁻ and vice versa')
d.basic('Formula mass of NaCl?', '23.0 + 35.5 = ' + N('58.5 u'))

# ---------------------------------------------------------------- 1.8 Mole
d.sec('1.8-mole-concept')
d.basic('Define one mole (current SI).', 'Exactly ' + N('6.02214076 × 10²³') + ' elementary entities (atoms, molecules, ions, electrons…)')
d.basic('What is the Avogadro constant?', r'\( N_A = 6.022 \times 10^{23} \)' + ' mol⁻¹, the number of entities in one mole')
d.basic('How was the number of atoms in 12 g of ¹²C found?', '12 g ÷ mass of one ¹²C atom (' + N('1.992648 × 10⁻²³ g') + ', by mass spectrometer) = ' + N('6.022 × 10²³'))
d.basic('Everyday analogy for the mole? (intuition)', 'Like a ' + T('dozen') + ' (12) or a gross (144): a counting unit, just a very large one')
d.basic('Define molar mass.', 'Mass of one mole of a substance in ' + T('grams') + '; numerically equal to atomic/molecular/formula mass in u', **fig('fig_1_11_one_mole'))
d.basic('Key mole relations (exam formula sheet)?', r'\( n = \frac{m}{M} = \frac{N}{N_A} = \frac{V}{22.7} \)' + ' (V of gas in L at STP)')
d.basic('Moles of C atoms, H atoms and molecules in 3 mol C₂H₆? (Ex 1.10)', N('6 mol C') + ', ' + N('18 mol H') + ', ' + N('1.807 × 10²⁴') + ' molecules')
d.basic('Number of atoms in 52 mol Ar, 52 u He, 52 g He? (classic)', r'\( 52 N_A \)' + '; ' + N('13') + ' atoms (52/4); ' + r'\( 13 N_A \)')
d.basic('Trap: "1 mole of O" vs "1 mole of O₂"?', '1 mol O atoms = ' + N('16 g') + '; 1 mol O₂ molecules = ' + N('32 g') + '. Always name the entity.')

# ---------------------------------------------------------------- 1.9 Percentage composition
d.sec('1.9-percentage-composition')
d.basic('Formula for mass % of an element?', 'Mass % = (mass of element in 1 mol of compound ÷ molar mass) × 100')
d.basic('Mass % of H and O in water?', 'H = 2.016/18.02 = ' + N('11.18%') + '; O = ' + N('88.79%'))
d.basic('Mass % of C, H, O in ethanol (C₂H₅OH)?', 'C ' + N('52.14%') + ', H ' + N('13.13%') + ', O ' + N('34.73%'))
d.basic('Use of percentage composition for a known compound?', 'To check the ' + T('purity') + ' of a sample')
d.basic('Empirical vs molecular formula?', T('Empirical') + ': simplest whole-number ratio of atoms. ' + T('Molecular') + ': exact number of each atom.')
d.cloze('Empirical formula steps: mass % → grams (take {{c1::100 g}}) → {{c2::moles}} (÷ atomic mass) → divide by the {{c3::smallest}} → whole numbers.')
d.basic('How do you get the molecular formula from the empirical one?', 'n = molar mass ÷ empirical formula mass; multiply the empirical formula by ' + T('n'))
steps_card(d, 'Problem 1.2', 'H 4.07%, C 24.27%, Cl 71.65%; M = 98.96 g. Formulas?', 'Take 100 g.',
           ['mol H = 4.04, C = 2.021, Cl = 2.021', 'Ratio H:C:Cl = 2:1:1 → CH₂Cl', 'EF mass 49.48; n = 98.96/49.48 = 2', 'Molecular formula <b>C₂H₄Cl₂</b>'], 3, 'Empirical to molecular formula', 'CH₂Cl → C₂H₄Cl₂')
d.basic('Empirical formula of iron oxide with 69.9% Fe, 30.1% O? (Ex 1.3)', 'Fe 1.25 : O 1.88 = 1 : 1.5 = 2 : 3 → ' + T('Fe₂O₃'))
d.basic('Trap: mole ratio comes out 1 : 1.5 or 1 : 1.33. What next?', 'Multiply all by ' + N('2') + ' or ' + N('3') + ' to reach whole numbers; don’t round 1.5 to 2')

# ---------------------------------------------------------------- 1.10 Stoichiometry
d.sec('1.10-stoichiometry')
d.basic('Meaning of "stoichiometry"?', 'Greek ' + T('stoicheion') + ' (element) + ' + T('metron') + ' (measure): calculating masses/volumes of reactants and products')
d.basic('What are stoichiometric coefficients?', 'The numbers before formulas in a balanced equation: they give ' + T('molecule and mole ratios'))
d.basic('CH₄ + 2O₂ → CO₂ + 2H₂O: read it in mass and in volume.', '16 g CH₄ + 64 g O₂ → 44 g CO₂ + 36 g H₂O; ' + N('22.7 L') + ' + 45.4 L → 22.7 L + 45.4 L')
d.basic('Molar volume of an ideal gas at STP in NCERT?', N('22.7 L') + ' (STP = 273.15 K, ' + T('1 bar') + ')')
d.basic('Update: 22.4 L or 22.7 L?', N('22.4 L') + ' is at 0 °C and ' + T('1 atm') + ' (old STP); ' + N('22.7 L') + ' at 1 bar (IUPAC). Check which STP the question uses.')
d.basic('Rule you must never break while balancing?', X('Never change subscripts') + ' in formulas; only change coefficients')
d.basic('Balance P₄ + O₂ → P₄O₁₀.', 'P₄ + ' + N('5') + 'O₂ → P₄O₁₀')
d.basic('Balance the combustion of propane.', 'C₃H₈ + ' + N('5') + 'O₂ → ' + N('3') + 'CO₂ + ' + N('4') + 'H₂O')
d.basic('Water from combustion of 16 g CH₄? (Problem 1.3)', '1 mol CH₄ → 2 mol H₂O = ' + N('36 g'))
d.basic('Moles of CH₄ needed for 22 g CO₂? (Problem 1.4)', '22/44 = 0.5 mol CO₂ ← ' + N('0.5 mol CH₄'))
d.basic('Define limiting reagent.', 'The reactant ' + T('consumed first') + '; it limits the amount of product formed')
steps_card(d, 'Problem 1.5', '50.0 kg N₂ + 10.0 kg H₂ → NH₃. Limiting reagent and NH₃?', 'N₂ + 3H₂ → 2NH₃',
           ['mol N₂ = 50000/28 = 1786; mol H₂ = 10000/2.016 = 4960', 'H₂ needed = 3 × 1786 = 5360 > 4960, so <b>H₂ is limiting</b>', 'NH₃ = 4960 × 2/3 = 3307 mol', '× 17 g = <b>56.1 kg NH₃</b>'], 1, 'Limiting reagent in NH₃ synthesis', 'H₂ limiting; 56.1 kg NH₃')
d.basic('Quick test for limiting reagent? (trick)', 'Divide each reactant’s moles by its ' + T('coefficient') + '; the ' + T('smallest') + ' quotient is limiting')
d.basic('A + B₂ → AB₂: 2 mol A + 3 mol B₂. Limiting? (Ex 1.23)', T('A') + ' is limiting (needs only 2 mol B₂; 1 mol B₂ left over)')
d.basic('CO₂ from 2 mol C burnt in 16 g O₂? (Ex 1.4 iii)', '16 g O₂ = 0.5 mol, so O₂ limits: ' + N('0.5 mol = 22 g CO₂'))
d.basic('Copper obtainable from 100 g CuSO₄? (Ex 1.7)', '63.5/159.5 × 100 = ' + N('39.8 g'))

d.sec('1.10.2-reactions-in-solutions')
d.cloze('Four ways to express concentration in NCERT: {{c1::mass per cent}}, {{c2::mole fraction}}, {{c3::molarity}} and {{c4::molality}}.')
d.basic('Mass per cent of solute?', '(mass of solute ÷ mass of ' + T('solution') + ') × 100')
d.basic('2 g of A in 18 g water: mass %? (Problem 1.6)', '2/20 × 100 = ' + N('10%'))
d.basic('Mole fraction of A in a mixture of A and B?', r'\( x_A = \frac{n_A}{n_A + n_B} \)' + '; the sum of all mole fractions = ' + N('1'))
d.basic('Define molarity (M).', 'Moles of solute per ' + T('litre of solution'))
d.basic('Define molality (m).', 'Moles of solute per ' + T('kg of solvent'))
d.basic('Which of molarity or molality changes with temperature, and why?', T('Molarity') + ' changes (volume expands); ' + T('molality') + ' does ' + X('not') + ' (mass is unaffected)')
d.basic('Molarity of 4 g NaOH in 250 mL solution? (Problem 1.7)', '0.1 mol / 0.250 L = ' + N('0.4 M'))
d.basic('Dilution formula?', r'\( M_1 V_1 = M_2 V_2 \)' + ' (moles of solute unchanged)')
d.basic('Volume of 1 M NaOH needed to make 1 L of 0.2 M?', N('200 mL') + ', diluted to 1 L')
d.basic('What is a stock solution?', 'A solution of known ' + T('higher concentration') + ' that is diluted to the desired one')
steps_card(d, 'Problem 1.8', '3 M NaCl, density 1.25 g/mL. Molality?', 'Take 1 L of solution.',
           ['Mass NaCl = 3 × 58.5 = 175.5 g', 'Mass solution = 1000 × 1.25 = 1250 g', 'Mass water = 1250 − 175.5 = 1074.5 g', 'm = 3 / 1.0745 = <b>2.79 m</b>'], 2, 'Molarity to molality', '2.79 m')
d.basic('Correction: Problem 1.8 in NCERT prints "1250 − 75.5". Right?', T('1250 − 175.5') + ' = 1074.5 g (the answer 2.79 m uses this)')
d.basic('Molarity of 69% HNO₃, density 1.41 g/mL? (Ex 1.6)', '1 L = 1410 g, HNO₃ = 972.9 g ÷ 63 = ' + N('15.44 M'))
d.basic('Molarity of 20 g sucrose in 2 L? (Ex 1.11)', '20/342 = 0.0585 mol ÷ 2 = ' + N('0.0293 M'))
d.basic('Mass of sodium acetate for 500 mL of 0.375 M? (Ex 1.5)', '0.1875 mol × 82.02 = ' + N('15.38 g'))
d.basic('15 ppm CHCl₃ in water as mass %? (Ex 1.17)', '15/10⁶ × 100 = ' + N('1.5 × 10⁻³ %'))
d.basic('Molarity vs molality for dilute aqueous solutions? (intuition)', 'Nearly ' + T('equal') + ': 1 L of dilute solution ≈ 1 kg of water')

# ---------------------------------------------------------------- summary
d.sec('summary')
table_card(d, 'Summary', 'Given by?', [
    ('Conservation of mass', 'Lavoisier, 1789', False), ('Definite proportions', 'Proust', False),
    ('Multiple proportions', 'Dalton, 1803', False), ('Gaseous volumes', 'Gay Lussac, 1808', False),
    ('Equal volumes, equal molecules', 'Avogadro, 1811', False)], term='Laws of chemical combination')
table_card(d, 'Summary', 'Definition?', [
    ('Mass %', 'g solute per 100 g solution', False), ('Mole fraction', 'n(A) / total n', False),
    ('Molarity (M)', 'mol per L solution; changes with T', True), ('Molality (m)', 'mol per kg solvent; T-independent', False)], term='Concentration terms')

n = d.write(os.path.join(OUT, 'deck.json'))
print(n, 'cards')
