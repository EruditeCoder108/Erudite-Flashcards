import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Chemistry', 'class12-chemistry-ch01-solutions')
d = Deck('Chapter 1: Solutions', 'Class 12', ['class-12', 'chemistry', 'ch-1'])
d.description = 'Concentration units, Henry’s and Raoult’s laws, ideal and non-ideal solutions, azeotropes, colligative properties, van’t Hoff factor'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- 1.1 Types
d.sec('1.1-types-of-solutions')
d.basic('What is a solution?', 'A ' + T('homogeneous mixture') + ' of two or more components: composition and properties uniform throughout')
d.basic('Solvent vs solute?', T('Solvent') + ': component in largest amount; decides the physical state. ' + T('Solute') + ': the other component(s).')
d.basic('What is a binary solution?', 'A solution of ' + N('two') + ' components')
d.cloze('Gaseous solutions: gas in gas = {{c1::O₂ + N₂ mixture}}; liquid in gas = {{c2::chloroform in N₂}}; solid in gas = {{c3::camphor in N₂}}.')
d.cloze('Liquid solutions: gas in liquid = {{c1::O₂ in water}}; liquid in liquid = {{c2::ethanol in water}}; solid in liquid = {{c3::glucose in water}}.')
d.cloze('Solid solutions: gas in solid = {{c1::H₂ in palladium}}; liquid in solid = {{c2::amalgam of Hg with Na}}; solid in solid = {{c3::Cu dissolved in gold}}.')
d.basic('Example of a solid solution with a gaseous solute?', E('Hydrogen in palladium'))
d.basic('Brass, bronze, German silver: compositions?', 'Brass ' + T('Cu + Zn') + '; bronze ' + T('Cu + Sn') + '; German silver ' + T('Cu + Zn + Ni'))
d.basic('Fluoride in drinking water: 1 ppm vs 1.5 ppm?', N('1 ppm') + ' prevents tooth decay; ' + N('1.5 ppm') + ' mottles teeth; high levels are poisonous (NaF in rat poison)')

# ---------------------------------------------------------------- 1.2 Concentration
d.sec('1.2-expressing-concentration')
d.basic('Mass percentage (w/w)?', 'Mass of component ÷ total mass of solution × 100')
d.basic('10% glucose (w/w) means?', N('10 g') + ' glucose in ' + N('90 g') + ' water (100 g solution)')
d.basic('Commercial bleach is how much NaOCl by mass?', N('3.62%'))
d.basic('10% ethanol (V/V) means?', N('10 mL') + ' ethanol made up to ' + N('100 mL') + ' of solution (not added to 100 mL water)')
d.basic('Antifreeze in cars: composition and freezing point?', N('35% (V/V)') + ' ethylene glycol; lowers f.p. of water to ' + N('255.4 K (−17.6 °C)'))
d.basic('Mass by volume percentage (w/V)?', 'Mass of solute (g) in ' + N('100 mL') + ' of solution; used in medicine and pharmacy')
d.basic('Parts per million?', r'\( \frac{n_{component}}{n_{total}} \times 10^{6} \)' + ' (as mass, volume or mass/volume); for trace amounts')
d.basic('Dissolved O₂ in sea water in ppm?', 'About ' + N('5.8 ppm') + ' (6 × 10⁻³ g in 1 L = 1030 g)')
d.basic('Mole fraction of A in a binary solution?', r'\( x_A = \frac{n_A}{n_A + n_B} \)' + '; all mole fractions add to ' + N('1'))
steps_card(d, 'Example 1.1', 'Mole fraction of ethylene glycol in 20% (w/w) solution?', 'Take 100 g solution: 20 g glycol (M = 62), 80 g water.',
           ['n(glycol) = 20/62 = 0.322 mol', 'n(water) = 80/18 = 4.444 mol', 'x(glycol) = 0.322 / 4.766 = <b>0.068</b>', 'x(water) = 1 − 0.068 = 0.932'], 2, 'Mole fraction of ethylene glycol', '0.068')
d.basic('Define molarity (M).', 'Moles of solute per ' + T('litre of solution') + r': \( M = \frac{n_{solute}}{V_{L}} \)')
d.basic('Molarity of 5 g NaOH in 450 mL solution? (Example 1.2)', '0.125 mol / 0.450 L = ' + N('0.278 M'))
d.basic('Define molality (m).', 'Moles of solute per ' + T('kg of solvent') + r': \( m = \frac{n_{solute}}{w_{solvent}\,(kg)} \)')
d.basic('Molality of 2.5 g acetic acid in 75 g benzene? (Example 1.3)', '0.0417 mol / 0.075 kg = ' + N('0.556 mol kg⁻¹'))
d.basic('Which concentration units depend on temperature, and why?', T('Molarity') + ' (and other volume-based units): volume changes with T, mass does not')
d.basic('Temperature-independent concentration units (NCERT)?', 'Mass %, ppm, ' + T('mole fraction') + ', ' + T('molality'))
d.basic('Correction: are ppm and percentages always temperature-independent?', X('Only mass/mass forms are') + '. V/V %, w/V % and ppm by volume use volume, so they change with T just like molarity.')
d.basic('Trap: 1 m aqueous solution vs 1 M: which has more solute per litre?', T('1 M') + ' (1 mol per litre of solution); 1 m has 1 mol per 1 kg water, i.e. per > 1 L of solution')
d.basic('Molarity ↔ molality conversion (density d in g/mL, M₂ = molar mass of solute)?', r'\( m = \frac{1000\,M}{1000\,d - M\,M_2} \)')
d.basic('Molarity from mass % and density?', r'\( M = \frac{10 \times \% \times d}{M_2} \)' + ' (d in g/mL)')
steps_card(d, 'Intext 1.5', '20% (w/w) aqueous KI, density 1.202 g/mL. Molality, molarity, x(KI)?', 'Take 100 g solution: 20 g KI (M = 166), 80 g water.',
           ['n(KI) = 20/166 = 0.120 mol', 'm = 0.120/0.080 = <b>1.51 mol/kg</b>', 'V = 100/1.202 = 83.2 mL, so M = 0.120/0.0832 = <b>1.45 M</b>', 'x(KI) = 0.120/(0.120 + 4.44) = <b>0.0263</b>'], 2, 'KI solution: m, M and x', 'm 1.51, M 1.45, x 0.0263')

# ---------------------------------------------------------------- 1.3 Solubility
d.sec('1.3-solubility')
d.basic('Define solubility.', 'Maximum amount of a substance that dissolves in a specified amount of solvent at a specified ' + T('temperature') + ' (and pressure)')
d.basic('"Like dissolves like" means?', T('Polar') + ' solutes dissolve in polar solvents, ' + T('non-polar') + ' in non-polar (NaCl in water; naphthalene in benzene)')
d.basic('Dissolution vs crystallisation?', T('Dissolution') + ': solute enters solution. ' + T('Crystallisation') + ': solute particles leave solution. Equal rates = dynamic equilibrium.')
d.basic('Saturated solution?', 'One in ' + T('dynamic equilibrium') + ' with undissolved solute; no more solute dissolves at that T and p')
d.basic('Effect of temperature on solubility of a solid?', 'If Δ_solH > 0 (endothermic): solubility ' + T('rises') + ' with T; if exothermic: ' + X('falls') + ' (Le Chatelier)')
d.basic('Effect of pressure on solubility of a solid in a liquid?', X('No significant effect') + ': solids and liquids are nearly incompressible')
d.basic('Why does raising pressure increase gas solubility?', 'More gas particles per volume strike the surface, so more enter the solution until a new equilibrium', **fig('fig_1_1_henry_pressure'))
d.basic('Henry’s law (NCERT statement)?', 'At constant T, the ' + T('solubility of a gas') + ' in a liquid is directly proportional to the ' + T('partial pressure') + ' of the gas above it')
d.basic('Most common form of Henry’s law?', r'\( p = K_H \, x \)' + ': partial pressure ∝ mole fraction of gas in solution')
d.basic('What is the slope of p vs x for a gas?', T('K_H') + ' (Henry’s law constant)', **fig('fig_1_2_hcl_cyclohexane'))
d.basic('Higher K_H means higher or lower solubility?', X('Lower') + ' solubility (x = p/K_H)')
d.basic('K_H depends on?', 'Nature of the gas (and solvent) and ' + T('temperature'))
d.basic('Why do aquatic animals prefer cold water?', 'K_H rises with T, so gases (O₂) are ' + T('more soluble in cold water'), **fig('tab_1_2_henry_constants'))
d.basic('From Table 1.2, which is more soluble: O₂ or N₂ at 293 K?', T('O₂') + ' (K_H 34.86 kbar < 76.48 kbar)')
d.basic('Why is soda water sealed under high pressure?', 'To raise the ' + T('solubility of CO₂') + ' (Henry’s law)')
d.basic('What are "bends" in scuba divers?', 'On surfacing, pressure falls and dissolved ' + T('N₂ forms bubbles') + ' in blood, blocking capillaries')
d.basic('How do divers avoid bends?', 'Tanks with air diluted by ' + T('helium') + ' (11.7% He, 56.2% N₂, 32.1% O₂)')
d.basic('What is anoxia?', 'Low blood O₂ at ' + T('high altitude') + ' (low partial pressure of O₂): climbers become weak and confused')
d.basic('Why does gas solubility fall with temperature?', 'Dissolving a gas is like condensation: ' + T('exothermic') + ', so heating shifts equilibrium back')
steps_card(d, 'Example 1.4', 'N₂ at 0.987 bar, K_H = 76.48 kbar, 293 K. Millimoles N₂ in 1 L water?', 'x = p/K_H; 1 L water = 55.5 mol.',
           ['x = 0.987 / 76480 = 1.29 × 10⁻⁵', 'n ≈ x × 55.5 = 7.16 × 10⁻⁴ mol', '= <b>0.716 mmol</b>'], 1, 'Henry’s law: N₂ in water', '0.716 mmol')
steps_card(d, 'Intext 1.7', 'K_H(CO₂) = 1.67 × 10⁸ Pa, 298 K. CO₂ in 500 mL soda water at 2.5 atm?', 'p = 2.5 × 101325 = 2.53 × 10⁵ Pa.',
           ['x = 2.53 × 10⁵ / 1.67 × 10⁸ = 1.52 × 10⁻³', 'n(water) = 500/18 = 27.8 mol', 'n(CO₂) = 1.52 × 10⁻³ × 27.8 = 0.042 mol', '= <b>1.85 g CO₂</b>'], 2, 'CO₂ in soda water', '1.85 g')
d.basic('Trap: units of K_H?', 'Pressure units (bar, kbar, Pa), because x is dimensionless in p = K_H x')

# ---------------------------------------------------------------- 1.4 Vapour pressure
d.sec('1.4-raoults-law')
d.basic('Raoult’s law for volatile liquids?', 'Partial vapour pressure of each component ∝ its ' + T('mole fraction') + r': \( p_1 = p_1^{\circ} x_1 \)')
d.basic('Total vapour pressure of an ideal binary solution?', r'\( p_{total} = p_1^{\circ} + (p_2^{\circ} - p_1^{\circ})\,x_2 \)')
d.basic('Shape of p_total vs x₂ for an ideal solution?', T('Straight line') + ' from p₁° to p₂°', **fig('fig_1_3_ideal_raoult'))
d.basic('Composition of the vapour phase?', r'\( y_i = \frac{p_i}{p_{total}} \)' + ' (Dalton’s law)')
d.basic('Which component is the vapour richer in?', 'The ' + T('more volatile') + ' component (higher p°)')
d.basic('Shortcut for p_total from vapour composition?', r'\( \frac{1}{p_{total}} = \frac{y_1}{p_1^{\circ}} + \frac{y_2}{p_2^{\circ}} \)')
steps_card(d, 'Example 1.5', '25.5 g CHCl₃ (p° 200) + 40 g CH₂Cl₂ (p° 415 mm Hg). p_total and y?', 'n(CH₂Cl₂) = 40/85 = 0.47; n(CHCl₃) = 25.5/119.5 = 0.213.',
           ['x(CH₂Cl₂) = 0.47/0.683 = 0.688', 'p_total = 200 + 215 × 0.688 = <b>347.9 mm Hg</b>', 'p(CH₂Cl₂) = 285.5; p(CHCl₃) = 62.4', 'y(CH₂Cl₂) = <b>0.82</b>, y(CHCl₃) = 0.18'], 1, 'Vapour pressure of CHCl₃ + CH₂Cl₂', '347.9 mm Hg; y 0.82/0.18')
steps_card(d, 'Intext 1.8', 'p°A = 450, p°B = 700 mm Hg, p_total = 600. Liquid and vapour composition?', 'p_total = p°A + (p°B − p°A) x_B',
           ['600 = 450 + 250 x_B', 'x_B = <b>0.6</b>, x_A = 0.4', 'y_A = 0.4 × 450/600 = 0.30', 'y_B = <b>0.70</b>'], 1, 'Liquid and vapour composition', 'x_B 0.6; y_B 0.70')
d.basic('How is Raoult’s law a special case of Henry’s law?', 'Both say p ∝ x; in Raoult’s law ' + T('K_H = p₁°'))
d.basic('Why does a non-volatile solute lower vapour pressure?', 'Solute particles occupy part of the ' + T('surface') + ', so fewer solvent molecules escape', **fig('fig_1_4_vp_lowering'))
d.basic('Does vapour-pressure lowering depend on the solute’s nature?', X('No') + ': only on the amount (1 mol sucrose ≈ 1 mol urea per kg water)')
d.basic('Raoult’s law for a solution with a non-volatile solute?', r'\( p_1 = x_1 p_1^{\circ} \)' + '; p vs x₁ is linear from 0 to p₁°', **fig('fig_1_5_raoult_solvent'))
d.basic('Raoult’s law in general form?', 'For any solution, the partial vapour pressure of each ' + T('volatile') + ' component is proportional to its mole fraction')

# ---------------------------------------------------------------- 1.5 Ideal / non-ideal
d.sec('1.5-ideal-and-non-ideal-solutions')
d.basic('Define an ideal solution.', 'Obeys Raoult’s law over the ' + T('entire concentration range') + r', with \( \Delta_{mix}H = 0 \) and \( \Delta_{mix}V = 0 \)')
d.basic('Molecular condition for ideality?', 'A–B attractions ≈ A–A and B–B attractions')
d.cloze('Nearly ideal solutions: {{c1::n-hexane + n-heptane}}, {{c2::bromoethane + chloroethane}}, {{c3::benzene + toluene}}.')
d.basic('For an ideal solution, signs of ΔmixS and ΔmixG?', r'\( \Delta_{mix}S > 0 \)' + ', ' + r'\( \Delta_{mix}G < 0 \)' + ': mixing is still spontaneous, driven by entropy')
d.basic('Positive deviation: cause?', 'A–B interactions ' + X('weaker') + ' than A–A / B–B; molecules escape more easily, so p > Raoult value')
d.basic('Negative deviation: cause?', 'A–B interactions ' + T('stronger') + ' than A–A / B–B; escaping tendency and p fall')
d.basic('Identify: (a) and (b).', '(a) ' + T('positive deviation') + ' (curve bulges above the line); (b) ' + T('negative deviation') + ' (sags below)', **img('fig_1_6_deviations'))
d.basic('Why does ethanol + acetone show positive deviation?', 'Acetone molecules get between ethanol molecules and ' + X('break H-bonds'))
d.basic('Carbon disulphide + acetone: deviation?', T('Positive') + ': solute–solvent dipolar attractions are weaker')
d.basic('Why does phenol + aniline show negative deviation?', 'Strong ' + T('H-bond') + ' between phenolic H and the N lone pair of aniline')
d.basic('Why does chloroform + acetone show negative deviation?', 'CHCl₃ ' + T('H-bonds') + ' to the C=O oxygen of acetone', **fig('fig_chcl3_acetone_hbond'))
table_card(d, 'Deviations', 'Sign?', [
    ('Positive deviation: ΔmixH', '> 0 (endothermic)', False), ('Positive deviation: ΔmixV', '> 0 (expands)', False),
    ('Negative deviation: ΔmixH', '< 0 (exothermic)', True), ('Negative deviation: ΔmixV', '< 0 (contracts)', True)],
    note='Teacher addition, standard in JEE/NEET: weaker A–B forces absorb heat and loosen packing.', term='ΔH and ΔV of mixing for non-ideal solutions')
d.basic('What is an azeotrope?', 'A binary mixture with the ' + T('same composition in liquid and vapour') + ', boiling at constant T.<br>It cannot be separated by fractional distillation')
d.basic('Which deviation gives a minimum boiling azeotrope? Example?', T('Large positive') + ' deviation; ' + E('ethanol–water') + ' (~95% ethanol by volume)')
d.basic('Which deviation gives a maximum boiling azeotrope? Example?', T('Large negative') + ' deviation; ' + E('HNO₃–water') + ' (68% HNO₃, 32% water, b.p. ' + N('393.5 K') + ')')
d.basic('Why can’t fermentation + distillation give 100% ethanol? (intuition)', 'At ~95% the vapour has the same composition as the liquid, so distillation stops enriching it')
d.basic('Mnemonic: positive deviation → which azeotrope?', 'Positive = higher p = boils easier = ' + T('minimum boiling') + '. Negative = lower p = ' + T('maximum boiling') + '.')

# ---------------------------------------------------------------- 1.6 Colligative
d.sec('1.6-colligative-properties')
d.basic('What are colligative properties?', 'Properties that depend on the ' + T('number of solute particles') + ', not their identity')
d.cloze('The four colligative properties: {{c1::relative lowering of vapour pressure}}, {{c2::elevation of boiling point}}, {{c3::depression of freezing point}}, {{c4::osmotic pressure}}.')
d.basic('Origin of the word "colligative"?', 'Latin ' + I('co') + ' (together) + ' + I('ligare') + ' (to bind)')

d.sec('1.6.1-relative-lowering-of-vapour-pressure')
d.basic('Relative lowering of vapour pressure equals?', r'\( \frac{p_1^{\circ} - p_1}{p_1^{\circ}} = x_2 \)' + ' (mole fraction of solute)')
d.basic('Dilute-solution form used to find molar mass?', r'\( \frac{p_1^{\circ} - p_1}{p_1^{\circ}} = \frac{w_2 M_1}{M_2 w_1} \)')
d.basic('Trap: is ΔP itself colligative?', X('Not strictly') + ': Δp = x₂p₁° depends on the solvent’s p₁°; the ' + T('relative') + ' lowering is the colligative one')
steps_card(d, 'Example 1.6', 'p°(benzene) 0.850 bar; 0.5 g solute in 39 g benzene gives 0.845 bar. M₂?', 'Δp/p° = w₂M₁/(M₂w₁)',
           ['Δp/p° = 0.005/0.850 = 0.00588', '0.00588 = (0.5 × 78)/(M₂ × 39)', 'M₂ = <b>170 g mol⁻¹</b>'], 2, 'Molar mass from vapour-pressure lowering', '170 g/mol')
steps_card(d, 'Intext 1.9', '50 g urea in 850 g water; p° = 23.8 mm Hg. p and relative lowering?', 'Non-volatile solute: p = x₁p°.',
           ['n(urea) = 50/60 = 0.833; n(water) = 47.2', 'x₂ = 0.833/48.1 = <b>0.0173</b> (relative lowering)', 'p = 23.8 × (1 − 0.0173) = <b>23.4 mm Hg</b>'], 1, 'Vapour pressure of urea solution', '23.4 mm Hg; 0.0173')

d.sec('1.6.2-elevation-of-boiling-point')
d.basic('When does a liquid boil?', 'When its vapour pressure equals ' + T('atmospheric pressure') + ' (water: 1.013 bar at 373.15 K)')
d.basic('Why does a solution boil at a higher temperature?', 'Its vapour pressure is lower, so it must be heated more to reach 1.013 bar', **fig('fig_1_7_bp_elevation'))
d.basic('Boiling point of 1 mol sucrose in 1000 g water?', N('373.52 K'))
d.basic('Elevation of boiling point formula?', r'\( \Delta T_b = K_b \, m \)')
d.basic('Names and unit of K_b?', T('Molal elevation constant') + ' / ' + T('ebullioscopic constant') + '; unit ' + N('K kg mol⁻¹'))
d.basic('Molar mass from ΔT_b?', r'\( M_2 = \frac{1000 \, K_b \, w_2}{\Delta T_b \, w_1} \)')
d.basic('b.p. of 18 g glucose in 1 kg water (K_b 0.52)? (Example 1.7)', 'm = 0.1; ΔT_b = ' + N('0.052 K') + '; b.p. = ' + N('373.202 K'))
d.basic('1.80 g solute in 90 g benzene raises b.p. 353.23 → 354.11 K (K_b 2.53). M₂? (Example 1.8)', '2.53 × 1.8 × 1000 / (0.88 × 90) = ' + N('58 g mol⁻¹'))
steps_card(d, 'Intext 1.10', 'Water boils at 99.63 °C at 750 mm Hg. Sucrose in 500 g water to boil at 100 °C?', 'K_b = 0.52 K kg/mol, M(sucrose) = 342.',
           ['ΔT_b = 0.37 K', 'm = 0.37/0.52 = 0.711 mol/kg', 'n = 0.711 × 0.5 = 0.356 mol', 'mass = 0.356 × 342 = <b>121.7 g</b>'], 1, 'Sucrose needed to boil at 100 °C', '121.7 g')

d.sec('1.6.3-depression-of-freezing-point')
d.basic('Define freezing point in terms of vapour pressure.', 'Temperature at which vapour pressure of the ' + T('liquid = that of the solid') + ' phase')
d.basic('Why does a solution freeze at a lower temperature?', 'Its lowered vapour pressure meets the solid-solvent curve at a ' + T('lower T'), **fig('fig_1_8_fp_depression'))
d.occlusion('Figure 1.8 · Depression of freezing point', M + 'fig_1_8_fp_depression.webp', (1001, 977), [
    ('Frozen solvent', rot([212, 392, 300, 64], -43), True), ('Liquid solvent', rot([530, 170, 270, 60], -27), True),
    ('Solution', rot([640, 240, 175, 58], -26), True), ('T_f (solution)', [295, 815, 70, 65], False), ('T_f° (pure solvent)', [535, 805, 80, 65], False)])
d.basic('Depression of freezing point formula?', r'\( \Delta T_f = K_f \, m \)')
d.basic('Names and unit of K_f?', T('Molal depression constant') + ' / ' + T('cryoscopic constant') + '; ' + N('K kg mol⁻¹'))
d.basic('Molar mass from ΔT_f?', r'\( M_2 = \frac{1000 \, K_f \, w_2}{\Delta T_f \, w_1} \)')
d.basic('K_f and K_b from solvent properties?', r'\( K_f = \frac{R M_1 T_f^2}{1000 \, \Delta_{fus}H} \)' + ', ' + r'\( K_b = \frac{R M_1 T_b^2}{1000 \, \Delta_{vap}H} \)')
d.basic('K_b and K_f of water?', N('0.52') + ' and ' + N('1.86 K kg mol⁻¹'), **fig('tab_1_3_kb_kf'))
d.basic('K_f of benzene and camphor-like solvents: why prefer a large K_f?', 'Benzene ' + N('5.12') + '; CCl₄ ' + N('31.8') + ', cyclohexane ' + N('20.0') + ': a larger K_f gives a bigger, easier-to-measure ΔT_f')
d.basic('Trap: Table 1.3 gives water’s f.p. as 273.0 K. Correct value?', T('273.15 K') + ' (0 °C); NCERT itself uses 273.15 K in Example 1.9')
d.basic('Trap: Example 1.12 uses K_f(benzene) = 4.9, Table 1.3 says 5.12. Which to use?', 'Always the value ' + T('given in the question') + '; tables differ by source')
steps_card(d, 'Example 1.9', '45 g ethylene glycol in 600 g water. ΔT_f and f.p.?', 'K_f = 1.86 K kg/mol; M = 62.',
           ['n = 45/62 = 0.73 mol', 'm = 0.73/0.60 = 1.2 mol/kg', 'ΔT_f = 1.86 × 1.2 = <b>2.2 K</b>', 'f.p. = 273.15 − 2.2 = <b>270.95 K</b>'], 2, 'Freezing point of glycol solution', 'ΔT_f 2.2 K; f.p. 270.95 K')
d.basic('1.00 g non-electrolyte in 50 g benzene lowers f.p. by 0.40 K (K_f 5.12). M₂? (Example 1.10)', '5.12 × 1 × 1000 / (0.40 × 50) = ' + N('256 g mol⁻¹'))
d.basic('Vitamin C to dissolve in 75 g acetic acid to lower f.p. by 1.5 °C (K_f 3.9)? (Intext 1.11)', 'm = 0.385; n = 0.0288 mol × 176 = ' + N('5.08 g'))
d.basic('Why is salt spread on icy roads? (intuition)', 'Brine freezes below 0 °C (ΔT_f), so ice melts at road temperature')

d.sec('1.6.4-osmosis-and-osmotic-pressure')
d.basic('What is a semipermeable membrane (SPM)? Examples?', 'Lets ' + T('solvent') + ' pass but not solute; natural: pig’s bladder, parchment; synthetic: cellophane')
d.basic('What is osmosis?', 'Flow of ' + T('solvent') + ' through an SPM from pure solvent (or dilute solution) into the solution (more concentrated)', **fig('fig_1_9_thistle_funnel'))
d.occlusion('Figure 1.9 · Osmosis in a thistle funnel', M + 'fig_1_9_thistle_funnel.webp', (1001, 811), [
    ('Solvent', [628, 330, 160, 50], True), ('Solution', [640, 510, 175, 50], True), ('Semipermeable membrane', [650, 670, 350, 120], True)])
d.basic('Define osmotic pressure (Π).', 'The ' + T('excess pressure') + ' that must be applied to the solution to just stop osmosis', **fig('fig_1_10_osmotic_pressure'))
d.basic('Osmotic pressure formula?', r'\( \Pi = C R T = \frac{n_2}{V} R T \)' + ' (C = molarity)')
d.basic('Molar mass from osmotic pressure?', r'\( M_2 = \frac{w_2 R T}{\Pi V} \)')
d.basic('Why is osmotic pressure preferred for proteins and polymers?', 'Measured at ' + T('room temperature') + '<br>Uses molarity<br>Π is ' + T('large even for dilute solutions') + '<br>Biomolecules are heat-sensitive')
steps_card(d, 'Example 1.11', '1.26 g protein in 200 cm³; Π = 2.57 × 10⁻³ bar at 300 K. M₂?', 'R = 0.083 L bar/(mol K).',
           ['M₂ = w₂RT/(ΠV)', '= 1.26 × 0.083 × 300 / (2.57 × 10⁻³ × 0.200)', '= <b>61,022 g mol⁻¹</b>'], 2, 'Molar mass of a protein', '61,022 g/mol')
d.basic('Osmotic pressure of 1.0 g polymer (M 185,000) in 450 mL water at 37 °C? (Intext 1.12)', 'C = 1.20 × 10⁻² mol m⁻³; Π = CRT = ' + N('30.9 Pa'))
d.basic('Isotonic solutions?', 'Same ' + T('osmotic pressure') + ' at the same T; no osmosis between them')
d.basic('Normal saline?', N('0.9% (w/V) NaCl') + ': isotonic with fluid in blood cells; safe to inject intravenously')
d.basic('Hypertonic vs hypotonic for red cells?', T('Hypertonic') + ' (> 0.9%): water leaves, cells ' + X('shrink') + '. ' + T('Hypotonic') + ' (< 0.9%): water enters, cells ' + T('swell') + '.')
d.basic('Why do raw mangoes shrivel in brine?', 'They lose water to the concentrated salt solution by ' + T('osmosis'))
d.basic('What is edema?', 'Puffiness from water retention in tissues after a lot of ' + T('salt') + ' (osmosis)')
d.basic('Why does salting meat or sugaring fruit preserve it?', 'Bacteria lose water by osmosis, ' + T('shrivel and die'))
d.basic('Intuition: why does solvent flow into the solution?', 'Pure solvent has higher ' + T('escaping tendency') + ' (chemical potential).<br>Like water vapour moving to a drier room, it moves to where it is "diluted"')

d.sec('1.6.5-reverse-osmosis')
d.basic('What is reverse osmosis?', 'Applying pressure ' + T('greater than Π') + ' on the solution side, so pure solvent flows out of the solution', **fig('fig_1_11_reverse_osmosis'))
d.basic('Main use of reverse osmosis?', T('Desalination') + ' of sea water')
d.basic('Membrane used in reverse osmosis?', T('Cellulose acetate') + ' film on a support: permeable to water, not to ions/impurities')

# ---------------------------------------------------------------- 1.7 Abnormal molar mass
d.sec('1.7-abnormal-molar-masses')
d.basic('Why does 1 m KCl raise water’s b.p. by ~1.04 K, not 0.52 K?', 'KCl gives ' + T('2 particles') + ' (K⁺, Cl⁻), doubling the colligative effect')
d.basic('Dissociation makes the observed molar mass higher or lower?', X('Lower') + ' than the true value (more particles)')
d.basic('Why does acetic acid show double molar mass in benzene?', 'It ' + T('dimerises by H-bonding') + ' in low-dielectric solvents, halving particle count', **fig('fig_acetic_dimer'))
d.basic('What is an abnormal molar mass?', 'An experimental molar mass ' + T('lower or higher') + ' than the true value, due to dissociation or association')
d.cloze('van’t Hoff factor i = {{c1::normal molar mass / abnormal molar mass}} = {{c2::observed / calculated colligative property}} = {{c3::moles of particles after / before association or dissociation}}.')
d.basic('i for association vs dissociation?', 'Association: ' + T('i < 1') + '. Dissociation: ' + T('i > 1') + '.')
d.basic('Approximate i for aqueous KCl and for acetic acid in benzene?', 'KCl ≈ ' + N('2') + '; CH₃COOH in benzene ≈ ' + N('0.5'))
d.basic('Colligative formulas with i?', r'\( \Delta T_b = i K_b m \)' + ', ' + r'\( \Delta T_f = i K_f m \)' + ', ' + r'\( \Pi = i C R T \)' + ', relative lowering = ' + r'\( i \, n_2 / n_1 \)')
d.basic('i from degree of dissociation α (solute gives n ions)?', r'\( i = 1 + (n - 1)\alpha \)')
d.basic('i from degree of association α (n molecules → 1)?', r'\( i = 1 - \alpha \left(1 - \frac{1}{n}\right) \)')
d.basic('Why is i for 0.1 m NaCl 1.87, not 2? ', 'Inter-ionic ' + T('attractions') + ' (ion pairing); i → 2 only at infinite dilution', **fig('tab_1_4_vant_hoff'))
d.basic('Why is i(MgSO₄) at 0.1 m only 1.21?', 'Doubly charged Mg²⁺ and SO₄²⁻ attract strongly and ' + T('pair') + ' much more than Na⁺/Cl⁻')
d.basic('i for complete dissociation of K₂SO₄? Al₂(SO₄)₃? K₄[Fe(CN)₆]?', N('3') + ', ' + N('5') + ', ' + N('5'))
d.basic('Trap: order of f.p. for 0.1 m glucose, NaCl, CaCl₂?', 'Particles 1 : 2 : 3, so f.p. ' + T('glucose > NaCl > CaCl₂') + ' (CaCl₂ lowest)')
steps_card(d, 'Example 1.12', '2 g benzoic acid in 25 g benzene: ΔT_f = 1.62 K (K_f 4.9). % association (dimer)?', 'Find the observed M₂, then i.',
           ['M₂ = 4.9 × 2 × 1000/(25 × 1.62) = 241.98', 'i = 122/241.98 = 0.504', 'i = 1 − x/2 ⇒ x/2 = 0.496', 'x = <b>0.992 → 99.2% associated</b>'], 3, 'Association of benzoic acid', '99.2%')
steps_card(d, 'Example 1.13', '0.6 mL acetic acid (d 1.06) in 1 L water: ΔT_f = 0.0205 °C. i and Ka?', 'n = 0.6 × 1.06/60 = 0.0106 mol, m = 0.0106.',
           ['Calculated ΔT_f = 1.86 × 0.0106 = 0.0197 K', 'i = 0.0205/0.0197 = 1.041', 'α = i − 1 = 0.041', 'Ka = cα²/(1 − α) = <b>1.86 × 10⁻⁵</b>'], 2, 'Ka of acetic acid from ΔT_f', 'i 1.041; Ka 1.86 × 10⁻⁵')

# ---------------------------------------------------------------- summary
d.sec('summary')
table_card(d, 'Summary', 'Formula?', [
    ('Henry’s law', 'p = K_H x', False), ('Raoult (volatile)', 'p_total = p₁°x₁ + p₂°x₂', False),
    ('Relative lowering', 'Δp/p° = i·x₂', False), ('Boiling point', 'ΔT_b = i K_b m', False),
    ('Freezing point', 'ΔT_f = i K_f m', False), ('Osmotic pressure', 'Π = i C R T', False)], term='Solutions formula sheet')
table_card(d, 'Summary', 'Ideal or which deviation?', [
    ('Benzene + toluene', 'Ideal', False), ('Ethanol + acetone', 'Positive', False), ('Ethanol + water', 'Positive (min-boiling azeotrope)', False),
    ('Chloroform + acetone', 'Negative', True), ('Phenol + aniline', 'Negative', True), ('HNO₃ + water', 'Negative (max-boiling azeotrope)', True)],
    term='Classify binary liquid mixtures')

n = d.write(os.path.join(OUT, 'deck.json'))
print(n, 'cards')
