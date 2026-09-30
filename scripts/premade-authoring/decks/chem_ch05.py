import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Chemistry', 'class11-chemistry-ch05-thermodynamics')
d = Deck('Chapter 5: Thermodynamics', 'Class 11', ['class-11', 'chemistry', 'ch-5'])
d.description = 'Systems, first law, work and heat, enthalpy, calorimetry, Hess’s law, bond and lattice enthalpy, entropy, Gibbs energy and equilibrium'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}
BC = (776, 1001)

# ---------------------------------------------------------------- 5.1 Terms
d.sec('5.1-thermodynamic-terms')
d.basic('System vs surroundings vs universe?', T('System') + ': the part being studied. ' + T('Surroundings') + ': the rest that can interact. ' + T('Universe') + ' = system + surroundings.', **fig('fig_5_1_system_surroundings'))
d.basic('What is the boundary?', 'The real or imaginary wall separating system from surroundings; tracks matter and energy flow')
table_card(d, 'Types of system', 'Exchanges?', [
    ('Open (open beaker)', 'Matter and energy', False), ('Closed (sealed copper vessel)', 'Energy only', False),
    ('Isolated (thermos flask)', 'Neither', True)], term='Open, closed and isolated systems')
d.basic('Identify the three systems.', '(a) ' + T('Open') + ', (b) ' + T('closed') + ', (c) ' + T('isolated'), **img('fig_5_2_open_closed_isolated'))
d.basic('What are state functions? Examples?', 'Depend only on the state, ' + X('not the path') + ': p, V, T, U, H, S, G')
d.basic('Is heat (q) or work (w) a state function?', X('No') + ': both are path functions; but q + w = ΔU is')
d.basic('Everyday example of a state function? (NCERT)', 'Volume of water in a pond: same whether filled by rain or tubewell')
d.basic('What is internal energy U?', 'Total energy of the system (chemical, electrical, mechanical…); only ' + T('ΔU') + ' can be measured')
d.basic('Three ways U can change?', 'Heat flows in/out, work is done on/by the system, matter enters/leaves')
d.basic('What is an adiabatic process?', 'No ' + T('heat transfer') + ' between system and surroundings (adiabatic wall)', **fig('fig_5_3_adiabatic'))
d.basic('What did Joule’s paddle/immersion-rod experiments show?', 'The same adiabatic work, done any way, gives the same change of state: ' + T('ΔU = w_ad') + ', so U is a state function')
d.cloze('IUPAC sign convention: w is {{c1::positive}} when work is done on the system; q is {{c2::positive}} when heat flows into the system.', extra='Trap: many physics books use the old convention (work done BY the system positive).')
d.basic('When heat flows through conducting walls with no work, ΔU = ?', T('q'), **fig('fig_5_4_conducting_walls'))

# ---------------------------------------------------------------- 5.2 First law, work
d.sec('5.2-first-law-and-work')
d.basic('First law of thermodynamics?', r'\( \Delta U = q + w \)' + ': energy of an isolated system is constant')
d.basic('Problem 5.1: ΔU for (i) adiabatic, work done on; (ii) heat lost, no work; (iii) work by system, heat supplied?', '(i) ΔU = w_ad (adiabatic wall). (ii) ΔU = −q (conducting wall). (iii) ΔU = q − w (closed system).')
d.basic('Work against constant external pressure?', r'\( w = -p_{ex} \Delta V = -p_{ex}(V_f - V_i) \)', **fig('fig_5_5a_compression'))
d.basic('On a p-V plot, what does work on the gas equal?', 'The ' + T('shaded area') + ' under the curve', **fig('fig_5_5b_finite_steps'))
d.basic('What is a reversible process?', 'One that can be reversed at any moment by an ' + T('infinitesimal change') + '.<br>It proceeds infinitely slowly through equilibrium states', **fig('fig_5_5c_reversible'))
d.basic('Reversible isothermal work for an ideal gas?', r'\( w_{rev} = -2.303 \, nRT \log \frac{V_f}{V_i} \)')
d.basic('What is free expansion, and the work done?', 'Expansion into ' + T('vacuum') + ' (p_ex = 0): ' + T('w = 0') + ', reversible or not')
d.basic('For isothermal expansion of an ideal gas, ΔU = ?', N('0') + ' (U depends only on T), so q = −w')
d.basic('Why does reversible expansion give the most work? (intuition)', 'The gas always pushes against the ' + T('largest possible') + ' opposing pressure; area under the curve is maximum')
d.basic('2 L gas at 10 atm expands isothermally into vacuum to 10 L. q and w? (Problem 5.2)', T('q = w = 0'))
d.basic('Same expansion against 1 atm? (Problem 5.3)', 'q = −w = 1 × 8 = ' + N('8 L atm'))
steps_card(d, 'Problem 5.4', '1 mol gas, 2 L → 10 L reversibly at 298 K. q?', 'q = −w = 2.303 nRT log(V_f/V_i)',
           ['V_f/V_i = 10/2 = 5', 'q = 2.303 × 1 × 0.08206 × 298 × log 5', '= 2.303 × 0.08206 × 298 × 0.699', '= <b>39.37 L atm</b>'], 3, 'Reversible isothermal expansion', '39.37 L atm')
d.basic('Trap: 1 L atm in joules?', N('101.3 J'))
d.basic('For an adiabatic change, ΔU = ?', T('w_ad') + ' (q = 0)')
d.basic('At constant volume, ΔU = ?', T('q_V'))

d.sec('5.2.2-enthalpy')
d.basic('Define enthalpy.', r'\( H = U + pV \)' + '; a state function (Greek "enthalpien", to warm)')
d.basic('What is ΔH physically?', 'Heat absorbed at ' + T('constant pressure') + ': ΔH = q_p')
d.basic('Relation between ΔH and ΔU for gaseous reactions?', r'\( \Delta H = \Delta U + \Delta n_g RT \)')
d.basic('What is Δn_g?', 'Moles of ' + T('gaseous products − gaseous reactants'))
d.basic('When is ΔH ≈ ΔU?', 'For solids/liquids only, or when ' + T('Δn_g = 0') + ' (e.g. H₂ + Cl₂ → 2HCl)')
d.basic('ΔU for vaporising 1 mol water at 100 °C if ΔvapH = 41 kJ/mol? (Problem 5.5)', '41.00 − (1 × 8.3 × 373 × 10⁻³) = ' + N('37.9 kJ mol⁻¹'))
d.basic('Trap: sign of ΔH − ΔU for N₂ + 3H₂ → 2NH₃?', 'Δn_g = ' + N('−2') + ', so ΔH < ΔU')
d.basic('Extensive vs intensive property?', T('Extensive') + ': depends on amount (mass, V, U, H, C). ' + T('Intensive') + ': does not (T, p, density).', **fig('fig_5_6_extensive_intensive'))
d.basic('Is a molar property extensive or intensive?', T('Intensive') + ' (e.g. molar volume, molar heat capacity)')
d.basic('Heat capacity, molar heat capacity and specific heat?', T('C') + ': q = CΔT. ' + T('Cₘ') + ': per mole. ' + T('Specific heat c') + ': per unit mass, q = c·m·ΔT.')
d.basic('Relation between Cp and Cv for an ideal gas?', r'\( C_p - C_V = R \)')
d.basic('Why is Cp > Cv? (intuition)', 'At constant p, part of the heat does ' + T('expansion work') + ', so more heat is needed per degree')

d.sec('5.3-calorimetry')
d.basic('Which calorimeter measures ΔU, and why?', 'The ' + T('bomb calorimeter') + ': sealed steel bomb, constant volume, so q_V = ΔU')
d.occlusion('Figure 5.7 · Bomb calorimeter', M + 'fig_5_7_bomb_calorimeter.webp', BC, [
    ('Thermometer', [440, 5, 250, 44], True), ('Firing leads', [280, 48, 190, 46], True), ('Stirrer', [30, 165, 112, 48], True),
    ('Oxygen inlet', [272, 172, 136, 92], True), ('Sample', [2, 462, 130, 48], True), ('Bomb', [2, 598, 104, 50], True),
    ('Oxygen under pressure', [410, 672, 152, 128], True), ('Water', [414, 876, 116, 48], True)])
d.basic('What measures ΔH directly?', 'A ' + T('constant-pressure calorimeter') + ' (e.g. coffee-cup / foamed polystyrene cup)', **fig('fig_5_8_constant_p_calorimeter'))
steps_card(d, 'Problem 5.6', '1 g graphite burnt in bomb calorimeter, C = 20.7 kJ/K, T 298 → 299 K. ΔH?', 'q = −C·ΔT; scale to 1 mol; Δn_g = 0.',
           ['q(1 g) = −20.7 × 1 = −20.7 kJ', 'Per mol: −20.7 × 12 = −248 kJ', 'Δn_g = 0, so ΔH = ΔU = <b>−2.48 × 10² kJ mol⁻¹</b>'], 1, 'Bomb calorimeter: graphite', '−248 kJ/mol')
d.basic('Sign of ΔrH for exothermic and endothermic reactions?', 'Exothermic: ' + T('negative') + '; endothermic: ' + T('positive'))

# ---------------------------------------------------------------- 5.4 Enthalpy change of reaction
d.sec('5.4-reaction-enthalpy')
d.basic('ΔrH from molar enthalpies?', r'\( \Delta_r H = \sum a_i H_{products} - \sum b_i H_{reactants} \)')
d.basic('What is the standard state?', 'Pure form at ' + N('1 bar') + ' and the specified temperature (usually 298 K)')
d.cloze('Phase-change enthalpies: melting = {{c1::ΔfusH}}, boiling = {{c2::ΔvapH}}, solid → vapour = {{c3::ΔsubH}}; all are {{c4::positive}}.')
d.basic('ΔfusH and ΔvapH of water?', N('6.01') + ' and ' + N('40.79 kJ mol⁻¹'), **fig('tab_5_1_fusion_vaporisation'))
d.basic('Sublimation examples in NCERT?', 'Dry ice CO₂ at 195 K (' + N('25.2 kJ/mol') + '); naphthalene (' + N('73.0 kJ/mol') + ')')
d.basic('Why does acetone need less heat to vaporise than water?', 'Water has strong ' + T('H-bonds') + '; acetone only weaker dipole-dipole forces')
d.basic('Heat to evaporate 18 g water at 298 K, and ΔvapU? (Problem 5.7)', 'q = ' + N('44.01 kJ') + '; ΔU = 44.01 − 2.48 = ' + N('41.53 kJ'))
steps_card(d, 'Problem 5.8', '1 mol water at 100 °C → ice at 0 °C. ΔU? (ΔfusH = 6.00 kJ/mol, c = 4.2 J/g°C)', 'Cool the liquid, then freeze.',
           ['ΔH₁ = −18 × 4.2 × 100 = −7.56 kJ', 'ΔH₂ = −6.00 kJ', 'ΔH = −13.56 kJ; no gas, so <b>ΔU = −13.56 kJ mol⁻¹</b>'], 2, 'Water at 100 °C to ice', '−13.56 kJ/mol')
d.basic('Define standard enthalpy of formation ΔfH°.', 'Enthalpy change to form ' + T('one mole') + ' of a compound from its elements in their ' + T('most stable states'))
d.basic('Reference states of H, O, C, S?', 'H₂(g), O₂(g), ' + T('C (graphite)') + ', ' + T('S (rhombic)'))
d.basic('ΔfH° of an element in its reference state?', T('Zero') + ' by convention')
d.basic('Why is CaO + CO₂ → CaCO₃ not ΔfH of CaCO₃?', 'CaCO₃ is formed from ' + X('compounds') + ', not from elements')
d.basic('Why is H₂ + Br₂ → 2HBr not ΔfH of HBr?', 'It forms ' + X('2 mol') + ': ΔfH(HBr) = ½ of it = ' + N('−36.4 kJ/mol'))
d.basic('ΔfH° of H₂O(l), CH₄(g), CO₂(g)?', N('−285.8') + ', ' + N('−74.81') + ', ' + N('−393.5 kJ mol⁻¹'), **fig('tab_5_2_formation_enthalpies'))
d.basic('ΔrH from enthalpies of formation?', r'\( \Delta_r H^{\circ} = \sum a \, \Delta_f H^{\circ}_{prod} - \sum b \, \Delta_f H^{\circ}_{react} \)')
d.basic('ΔrH for CaCO₃ → CaO + CO₂?', '(−635.1) + (−393.5) − (−1206.9) = ' + N('+178.3 kJ mol⁻¹') + ': endothermic')
d.basic('What is a thermochemical equation?', 'A balanced equation with ' + T('physical states') + ' and its ' + T('ΔrH'))
d.cloze('Thermochemical rules: coefficients mean {{c1::moles}} (never molecules); halving the equation {{c2::halves}} ΔrH; reversing it {{c3::reverses the sign}}.')
d.basic('ΔrH for Fe₂O₃ + 3H₂ → 2Fe + 3H₂O(l)?', '3(−285.83) − (−824.2) = ' + N('−33.3 kJ mol⁻¹'))
d.basic('Hess’s law of constant heat summation?', 'ΔrH is the ' + T('same') + ' whether a reaction occurs in one step or many (H is a state function)')
steps_card(d, 'Hess’s law', 'ΔrH for C(graphite) + ½O₂ → CO?', 'C + O₂ → CO₂: −393.5. CO + ½O₂ → CO₂: −283.0.',
           ['Reverse the second: CO₂ → CO + ½O₂, +283.0', 'Add to the first', 'ΔrH = −393.5 + 283.0 = <b>−110.5 kJ mol⁻¹</b>'], 2, 'Hess: enthalpy of formation of CO', '−110.5 kJ/mol')
d.basic('Why can’t ΔfH of CO be measured directly?', 'Burning carbon always gives ' + X('some CO₂') + ' along with CO')

d.sec('5.5-types-of-reaction-enthalpies')
d.basic('Define standard enthalpy of combustion.', 'Enthalpy change per mole when a substance ' + T('burns completely') + ', all in standard states')
d.basic('ΔcH° of butane (LPG) and glucose?', 'Butane ' + N('−2658 kJ/mol') + '; glucose ' + N('−2802 kJ/mol'))
steps_card(d, 'Problem 5.9', 'ΔcH(benzene) = −3267 kJ/mol. ΔfH(benzene)? (ΔfH CO₂ −393.5, H₂O −285.83)', 'C₆H₆ + 15/2 O₂ → 6CO₂ + 3H₂O',
           ['6(−393.5) + 3(−285.83) = −3218.5', 'ΔfH = −3218.5 − (−3267.0)', '= <b>+48.5 kJ mol⁻¹</b>'], 2, 'Enthalpy of formation of benzene', '+48.5 kJ/mol')
d.basic('Correction: NCERT’s Problem 5.9 working prints the final ΔfH(benzene) with a minus sign. Right sign?', T('+48.5 kJ/mol') + ': −3218.5 − (−3267.0) is positive; reversing the combustion equation gives +3267, not −3267')
d.basic('Define enthalpy of atomization.', 'Enthalpy change to break ' + T('one mole of bonds completely') + ' into gaseous atoms.<br>e.g. H₂ → 2H, 435 kJ/mol<br>e.g. CH₄ → C + 4H, 1665 kJ/mol')
d.basic('For Na(s) → Na(g), atomization enthalpy equals?', 'Enthalpy of ' + T('sublimation') + ' (108.4 kJ/mol)')
d.basic('Bond dissociation enthalpy vs mean bond enthalpy?', T('Dissociation') + ': for a specific bond. ' + T('Mean') + ': average over identical bonds, e.g. C–H in CH₄ = 1665/4 = ' + N('416 kJ/mol') + '.')
d.basic('Why do the 4 C–H bonds of CH₄ need different energies (427, 439, 452, 347)?', 'Each step breaks a bond in a ' + T('different fragment') + ' (CH₄, CH₃, CH₂, CH)')
d.basic('Bond enthalpies of H–H, Cl–Cl, O=O?', N('435') + ', ' + N('242') + ', ' + N('498') + ' kJ/mol (Table 5.3; the text says 428 for O=O)', **fig('tab_5_3a_single_bonds'))
d.basic('ΔrH from bond enthalpies (gas phase)?', r'\( \Delta_r H = \sum BE_{reactants} - \sum BE_{products} \)' + ' (bonds broken − bonds formed)', **fig('tab_5_3b_multiple_bonds'))
d.basic('Trap: order of terms in the bond-enthalpy formula vs the ΔfH formula?', 'Bond enthalpies: ' + T('reactants − products') + '. Formation enthalpies: ' + T('products − reactants') + '.')
d.basic('Define lattice enthalpy.', 'Enthalpy change when 1 mol of an ionic solid ' + T('dissociates into gaseous ions') + ' (NaCl: ' + N('+788 kJ/mol') + ')')
d.basic('How is lattice enthalpy found?', 'Indirectly, by a ' + T('Born-Haber cycle') + ' (Hess’s law; sum round a cycle = 0)', **fig('fig_5_9_born_haber'))
d.cloze('Born-Haber for NaCl: ΔlatticeH = {{c1::411.2}} (−ΔfH) + {{c2::108.4}} (ΔsubH Na) + {{c3::121}} (½ Cl–Cl) + {{c4::496}} (ΔiH Na) − {{c5::348.6}} (ΔegH Cl) = 788 kJ/mol.')
d.basic('Ionization energy vs ionization enthalpy (box)?', 'Energies are defined at 0 K; ΔiH = E₀ + ' + T('5/2 RT') + '; ΔegH = −A − 5/2 RT')
d.basic('Enthalpy of solution from lattice and hydration enthalpy?', r'\( \Delta_{sol} H = \Delta_{lattice} H + \Delta_{hyd} H \)' + '; NaCl: 788 − 784 = ' + N('+4 kJ/mol'))
d.basic('Why does solubility of most salts rise with temperature?', 'ΔsolH is usually ' + T('positive') + ' (endothermic dissolution)')
d.basic('Why are many fluorides less soluble than chlorides?', 'Small F⁻ gives a very high ' + T('lattice enthalpy'))
d.basic('What is enthalpy of dilution?', 'Heat change on adding more solvent to a solution, e.g. HCl·25aq + 15aq → HCl·40aq: ' + N('−0.76 kJ/mol'))
d.basic('Enthalpy of solution at infinite dilution for HCl?', N('−74.85 kJ/mol') + ' (limiting value as solvent increases)')

# ---------------------------------------------------------------- 5.6 Spontaneity
d.sec('5.6-spontaneity')
d.basic('Meaning of "spontaneous"?', 'Has the potential to proceed ' + T('without external help') + '; says ' + X('nothing about rate') + ' (H₂ + O₂ at room T)')
d.basic('Is a spontaneous process reversible?', X('No') + ': it is irreversible and can be reversed only by an external agency')
d.basic('Is decrease in enthalpy enough for spontaneity?', X('No') + ': some endothermic reactions are spontaneous (e.g. ½N₂ + O₂ → NO₂; C + 2S → CS₂)', **fig('fig_5_10b_endothermic'))
d.basic('Enthalpy diagram of an exothermic reaction?', 'Products lie ' + T('below') + ' reactants; ΔrH negative', **fig('fig_5_10a_exothermic'))
d.basic('What drives diffusion of two gases when ΔH = 0?', 'Increase in ' + T('entropy') + ' (disorder)', **fig('fig_5_11_diffusion'))
d.basic('Entropy change for a reversible process?', r'\( \Delta S = \frac{q_{rev}}{T} \)')
d.basic('Why does heat added at low T raise entropy more? (intuition)', 'A cold system is ordered, so the same heat causes a ' + T('bigger relative increase') + ' in randomness.<br>(Like a sneeze in a quiet library vs a busy street)')
d.basic('Entropy order of solid, liquid, gas?', T('Solid < liquid < gas'))
d.basic('Criterion for spontaneity in terms of entropy?', r'\( \Delta S_{total} = \Delta S_{sys} + \Delta S_{surr} > 0 \)' + '; at equilibrium ΔS_total = 0')
d.basic('Does ΔU distinguish reversible from irreversible expansion?', X('No') + ' (ΔU = 0 for both isothermally); ' + T('ΔS_total') + ' does')
d.basic('Entropy increases or decreases? (i) liquid → solid, (ii) solid 0 → 115 K, (iii) NaHCO₃ decomposes, (iv) H₂ → 2H. (Problem 5.10)', '(i) ' + X('decreases') + '; (ii), (iii), (iv) ' + T('increase'))
steps_card(d, 'Problem 5.11', '4Fe + 3O₂ → 2Fe₂O₃: ΔS = −549.4 J/K/mol, ΔH = −1648 kJ/mol. Why spontaneous?', 'ΔS_surr = −ΔH/T',
           ['ΔS_surr = 1648 × 10³ / 298 = 5530 J/K/mol', 'ΔS_total = 5530 − 549.4', '= <b>+4980.6 J/K/mol > 0</b>, spontaneous'], 1, 'Rusting is spontaneous', 'ΔS_total = +4980.6 J/K/mol')
d.basic('Define Gibbs energy.', r'\( G = H - TS \)' + '; extensive state function')
d.basic('Gibbs equation?', r'\( \Delta G = \Delta H - T \Delta S \)')
d.cloze('At constant T and p: ΔG {{c1::< 0}} → spontaneous; ΔG {{c2::> 0}} → non-spontaneous; ΔG {{c3::= 0}} → equilibrium.')
d.basic('Why is G called "free energy"?', 'ΔG is the net energy ' + T('available for useful work') + ' (TΔS is unavailable)')
quadrant_card(d, 'Table 5.4', 'When is the reaction spontaneous?', [
    ('ΔH −, ΔS +', 'Always'), ('ΔH +, ΔS +', 'High T'), ('ΔH −, ΔS −', 'Low T'), ('ΔH +, ΔS −', 'Never')],
    'Low/high T are relative; the crossover is at T = ΔH/ΔS.', 'Effect of temperature on spontaneity', 'ΔH−ΔS+: always; ΔH+ΔS+: high T; ΔH−ΔS−: low T; ΔH+ΔS−: never')
d.basic('Table 5.4 in full?', 'Signs of ΔH, ΔS and ΔG with the temperature condition', **fig('tab_5_4_spontaneity'))
d.basic('Temperature at which ΔG changes sign?', r'\( T = \frac{\Delta H}{\Delta S} \)')
d.basic('Second law of thermodynamics (NCERT form)?', 'The entropy of an ' + T('isolated system') + ' increases in a spontaneous change')
d.basic('Why are spontaneous exothermic reactions so common?', 'Released heat increases the ' + T('entropy of the surroundings'))
d.basic('Third law of thermodynamics?', 'Entropy of a ' + T('pure perfect crystal') + ' → 0 as T → 0 K')
d.basic('Why is the third law limited to pure crystals?', 'Solutions and supercooled liquids have ' + X('non-zero') + ' entropy at 0 K')
d.basic('Use of the third law?', 'Lets us find ' + T('absolute entropies') + ' from thermal data')

d.sec('5.7-gibbs-energy-and-equilibrium')
d.basic('Relation between ΔG° and K?', r'\( \Delta_r G^{\circ} = -RT \ln K = -2.303 \, RT \log K \)')
d.basic('If ΔG° is large and negative, K is?', 'Much ' + T('greater than 1') + ': reaction goes nearly to completion')
d.basic('ΔrG° for 3/2 O₂ → O₃ at 298 K, Kp = 2.47 × 10⁻²⁹? (Problem 5.12)', N('+163 kJ mol⁻¹'))
d.basic('K at 298 K if ΔrG° = −13.6 kJ/mol? (Problem 5.13)', 'log K = 2.38 → K = ' + N('2.4 × 10²'))
steps_card(d, 'Problem 5.14', 'N₂O₄ ⇌ 2NO₂ is 50% dissociated at 60 °C, 1 atm. ΔG°?', 'Start with 1 mol N₂O₄.',
           ['Mol: N₂O₄ 0.5, NO₂ 1.0; total 1.5', 'Kp = (1/1.5)² / (0.5/1.5) = 1.33 atm', 'ΔG° = −2.303 × 8.314 × 333 × log 1.33', '= <b>≈ −790 J mol⁻¹ (−0.79 kJ mol⁻¹)</b>'], 3, 'ΔG° of N₂O₄ dissociation', '≈ −0.79 kJ/mol')
d.basic('Correction: NCERT prints ΔG° = −763.8 kJ/mol in Problem 5.14. Right answer?', '2.303 × 8.314 × 333 × 0.1239 ≈ ' + T('790 J') + ', so ΔG° ≈ ' + N('−0.79 kJ/mol') + '<br>Sanity check: K ≈ 1 always means ΔG° ≈ 0, never hundreds of kJ')

# ---------------------------------------------------------------- summary
d.sec('summary')
table_card(d, 'Summary', 'Key relation?', [
    ('First law', 'ΔU = q + w', False), ('Enthalpy', 'ΔH = ΔU + Δn_g RT', False), ('Heat capacities', 'Cp − Cv = R', False),
    ('Reversible isothermal work', 'w = −2.303 nRT log(V_f/V_i)', False), ('Gibbs', 'ΔG = ΔH − TΔS', False),
    ('Equilibrium', 'ΔG° = −2.303 RT log K', False)], term='Thermodynamics formula sheet')
table_card(d, 'Summary', 'Measured by / equals?', [
    ('q at constant V', 'ΔU (bomb calorimeter)', False), ('q at constant p', 'ΔH (coffee-cup calorimeter)', False),
    ('q in adiabatic process', 'zero', True), ('w in free expansion', 'zero', True)], term='Heat and work special cases')

n = d.write(os.path.join(OUT, 'deck.json'))
print(n, 'cards')
