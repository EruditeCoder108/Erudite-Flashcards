import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Chemistry', 'class11-chemistry-ch06-equilibrium')
d = Deck('Chapter 6: Equilibrium', 'Class 11', ['class-11', 'chemistry', 'ch-6'])
d.description = 'Physical and chemical equilibria, Kc and Kp, Q, ΔG and K, Le Chatelier, acids and bases, pH, Ka and Kb, hydrolysis, buffers and Ksp'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- intro
d.sec('6.0-intro')
d.basic('What is equilibrium?', 'The state where the rates of the ' + T('forward and reverse') + ' processes are equal, so composition stays constant')
d.basic('Three classes of reactions by extent at equilibrium?', 'Nearly ' + T('complete') + '; only ' + T('small') + ' product formed; ' + T('comparable') + ' amounts of reactants and products')
d.basic('What is ionic equilibrium?', 'Equilibrium involving ' + T('ions in aqueous solution'))

# ---------------------------------------------------------------- 6.1 Physical
d.sec('6.1-physical-equilibria')
d.basic('Ice and water in a thermos at 273 K: why is it "dynamic"?', 'Molecules keep moving between ice and water at ' + T('equal rates') + '; masses stay constant')
d.basic('Define normal melting (freezing) point.', 'Temperature at which solid and liquid are in equilibrium at ' + T('1 atm'))
d.basic('What is equilibrium vapour pressure?', 'Constant pressure of vapour when ' + T('rate of evaporation = rate of condensation') + ' at a given T', **fig('fig_6_1_vapour_pressure'))
d.basic('Drying agents used in the vapour-pressure box?', 'Anhydrous ' + T('CaCl₂') + ' or ' + T('P₄O₁₀'))
d.basic('Higher vapour pressure means?', 'More ' + T('volatile') + ', ' + T('lower boiling point'))
d.basic('Why can’t an open watch glass of water reach equilibrium?', 'It is an ' + X('open system') + ': vapour disperses, so condensation stays below evaporation')
d.basic('Define normal boiling point. Water’s?', 'T at which liquid and vapour are in equilibrium at ' + N('1.013 bar') + '; water ' + N('100 °C'))
d.basic('Why does water boil below 100 °C in the hills?', 'Lower atmospheric pressure at ' + T('high altitude'))
d.basic('Examples of solid ⇌ vapour equilibrium?', E('Iodine') + ' (violet vapour), ' + E('camphor') + ', ' + E('NH₄Cl'))
d.basic('How was dynamic equilibrium in saturated sugar solution proved?', 'Adding ' + T('radioactive sugar') + ': radioactivity later appears in both solid and solution')
d.basic('Henry’s law?', 'Mass of gas dissolved in a given mass of solvent is ∝ the ' + T('pressure of the gas') + ' above it; decreases as T rises')
d.basic('Why does soda water fizz on opening and later go flat?', 'CO₂ was dissolved under ' + T('high pressure') + '; at lower pressure solubility falls until it matches atmospheric pCO₂')
table_card(d, 'Table 6.1', 'What stays constant?', [
    ('H₂O(l) ⇌ H₂O(g)', 'p(H₂O) at given T', False), ('H₂O(s) ⇌ H₂O(l)', 'Melting point at fixed p', False),
    ('Sugar(s) ⇌ Sugar(soln)', 'Solute concentration at given T', False), ('CO₂(g) ⇌ CO₂(aq)', '[CO₂(aq)]/[CO₂(g)] at given T', False)], term='Features of physical equilibria')
d.cloze('Physical equilibria: possible only in a {{c1::closed system}}; both processes occur at the {{c2::same rate}}; all measurable properties stay {{c3::constant}}.')

# ---------------------------------------------------------------- 6.2 Chemical
d.sec('6.2-chemical-equilibrium')
d.basic('Why does the forward rate fall and reverse rate rise as a reaction proceeds?', 'Reactants deplete and products accumulate until the rates are ' + T('equal'), **fig('fig_6_2_attainment'))
d.basic('Can equilibrium be approached from either side?', T('Yes'), **fig('fig_6_5_hi_either_side'))
d.basic('How did deuterium prove ammonia equilibrium is dynamic?', 'Mixing H₂/NH₃ and D₂/ND₃ equilibria gave ' + T('NH₂D, NHD₂, HD') + ': reactions never stop', **fig('fig_6_4_haber_equilibrium'))
d.basic('Classroom model of dynamic equilibrium (box)?', 'Transferring coloured water between two cylinders with glass tubes until levels stop changing')

# ---------------------------------------------------------------- 6.3 Law
d.sec('6.3-law-of-chemical-equilibrium')
d.basic('Who proposed the law of mass action, and when?', T('Guldberg and Waage') + ' (Norway), ' + N('1864'))
d.basic('Why "mass action"?', 'Concentration was once called "' + T('active mass') + '"')
d.basic('Kc for aA + bB ⇌ cC + dD?', r'\( K_c = \frac{[C]^c [D]^d}{[A]^a [B]^b} \)')
d.basic('H₂ + I₂ ⇌ 2HI data (731 K): which ratio is constant?', r'\( \frac{[HI]^2}{[H_2][I_2]} \)' + ', not [HI]/[H₂][I₂]', **fig('tab_6_2_h2_i2_data'))
table_card(d, 'Table 6.4', 'New K?', [
    ('Reverse the reaction', '1/Kc', False), ('Multiply equation by n', 'Kcⁿ', False),
    ('Halve the equation', '√Kc', False), ('Add two reactions', 'K₁ × K₂', False)], term='Manipulating equilibrium constants')
d.basic('Kc for N₂ + 3H₂ ⇌ 2NH₃: [N₂] 1.5×10⁻², [H₂] 3.0×10⁻², [NH₃] 1.2×10⁻² M? (Problem 6.1)', N('3.55 × 10²'))
d.basic('Kc for N₂ + O₂ ⇌ 2NO: [N₂] 3.0×10⁻³, [O₂] 4.2×10⁻³, [NO] 2.8×10⁻³? (Problem 6.2)', N('0.622'))
d.basic('Homogeneous equilibrium: define and examples.', 'All species in ' + T('one phase') + ': N₂ + 3H₂ ⇌ 2NH₃; Fe³⁺ + SCN⁻ ⇌ Fe(SCN)²⁺')

d.sec('6.4-kp')
d.basic('Relation between Kp and Kc?', r'\( K_p = K_c (RT)^{\Delta n} \)' + ', Δn = gaseous moles of products − reactants')
d.basic('Value of R to use with Kp in bar?', N('0.0831 bar L mol⁻¹ K⁻¹'))
d.basic('When is Kp = Kc?', 'When ' + T('Δn = 0') + ', e.g. H₂ + I₂ ⇌ 2HI')
d.basic('Kc for PCl₃ + Cl₂ ⇌ PCl₅: [PCl₃] = [Cl₂] = 1.59, [PCl₅] = 1.41 M? (Problem 6.3)', '1.41 / 1.59² = ' + N('0.558'))
steps_card(d, 'Problem 6.4', 'CO + H₂O ⇌ CO₂ + H₂, Kc = 4.24 at 800 K; start 0.10 M each of CO and H₂O.', 'Let x = [CO₂] = [H₂].',
           ['x²/(0.1 − x)² = 4.24', 'Take root: x/(0.1 − x) = 2.06', 'x = 0.067 M', '[CO] = [H₂O] = <b>0.033 M</b>; [CO₂] = [H₂] = 0.067 M'], 2, 'Equilibrium concentrations from Kc', '0.067 M products, 0.033 M reactants')
d.basic('Shortcut for Problem 6.4? (trick)', 'Both sides are perfect squares: take ' + T('square roots') + ' instead of solving the quadratic')
d.basic('Kp for 2NOCl ⇌ 2NO + Cl₂, Kc = 3.75 × 10⁻⁶ at 1069 K? (Problem 6.5)', 'Δn = 1: Kp = 3.75 × 10⁻⁶ × 0.0831 × 1069 = ' + N('3.3 × 10⁻⁴'))
d.basic('Correction: NCERT’s Problem 6.5 prints Kp = 0.033. Recompute.', '3.75 × 10⁻⁶ × 88.8 = ' + T('3.33 × 10⁻⁴') + '; 0.033 is 100× too large')

d.sec('6.5-heterogeneous-equilibria')
d.basic('What is a heterogeneous equilibrium?', 'Species in ' + T('more than one phase') + ', e.g. H₂O(l) ⇌ H₂O(g); Ca(OH)₂(s) ⇌ Ca²⁺ + 2OH⁻')
d.basic('Why are pure solids and liquids left out of K?', 'Their molar concentration is ' + T('constant') + ', independent of amount')
d.basic('K for CaCO₃(s) ⇌ CaO(s) + CO₂(g)?', 'Kp = ' + T('p(CO₂)') + '; at 1100 K p(CO₂) = 2 × 10⁵ Pa → Kp = ' + N('2.00'))
d.basic('Kc for Ni(s) + 4CO(g) ⇌ Ni(CO)₄(g)?', r'\( K_c = \frac{[Ni(CO)_4]}{[CO]^4} \)' + ' (used to purify nickel)')
d.basic('Must the pure solid be present for heterogeneous equilibrium?', T('Yes') + ', however small, though it does not appear in K')
d.basic('Units of Kc and Kp for N₂O₄ ⇌ 2NO₂?', 'Kc: ' + T('mol/L') + '; Kp: ' + T('bar') + ' (H₂ + I₂ ⇌ 2HI: unitless)')
d.basic('How can K be made dimensionless?', 'Divide by standard states: ' + T('1 bar') + ' for gases, ' + T('1 M') + ' for solutes')
steps_card(d, 'Problem 6.6', 'CO₂ + C(s) ⇌ 2CO, Kp = 3.0; start p(CO₂) = 0.48 bar. Equilibrium pressures?', 'CO₂ falls by x, CO rises by 2x.',
           ['(2x)²/(0.48 − x) = 3', '4x² + 3x − 1.44 = 0 → x = 0.33', 'p(CO) = 2x = <b>0.66 bar</b>; p(CO₂) = 0.15 bar'], 2, 'Partial pressures from Kp', 'CO 0.66 bar, CO₂ 0.15 bar')
d.basic('Correction: Problem 6.6 labels both answers "pCO₂". Which is which?', T('p(CO) = 0.66 bar') + ' (= 2x) and ' + T('p(CO₂) = 0.15 bar'))

# ---------------------------------------------------------------- 6.6 Applications
d.sec('6.6-applications-of-k')
d.cloze('Features of K: independent of {{c1::initial concentrations}}; depends on {{c2::temperature}}; reverse reaction has {{c3::1/K}}; says nothing about {{c4::rate}}.')
table_card(d, 'Extent of reaction', 'What does K tell?', [
    ('Kc > 10³', 'Products predominate; nearly complete', False), ('Kc < 10⁻³', 'Reactants predominate; hardly proceeds', True),
    ('10⁻³ to 10³', 'Appreciable reactants and products', False)], term='Magnitude of K and extent', note='e.g. H₂ + Cl₂: 4 × 10³¹; N₂ + O₂ → 2NO: 4.8 × 10⁻³¹; H₂ + I₂: 57 at 700 K')
d.basic('Figure 6.6 in a line?', 'Negligible ← Kc 10⁻³ … 10³ → extremely large', **fig('fig_6_6_extent_vs_k'))
d.basic('What is the reaction quotient Q?', 'Same expression as K but with concentrations at ' + T('any time') + ', not necessarily equilibrium')
quadrant_card(d, 'Q vs K', 'Which way does the reaction go?', [
    ('Q < K', 'Forward →'), ('Q > K', '← Reverse'), ('Q = K', 'At equilibrium'), ('Q ≪ K', 'Strongly forward')],
    'Compare Q with K at the same temperature.', 'Predicting direction from Q and K', 'Q < K forward; Q > K reverse; Q = K equilibrium')
d.basic('Direction with Q and K bars (Fig 6.7)?', 'Qc < Kc → products; Qc > Kc → reactants', **fig('fig_6_7_q_vs_k'))
d.basic('H₂ + I₂ ⇌ 2HI (Kc 57): [H₂] 0.10, [I₂] 0.20, [HI] 0.40 M. Direction?', 'Qc = 0.16/0.02 = ' + N('8.0') + ' < 57 → ' + T('forward'))
d.basic('2A ⇌ B + C, Kc = 2 × 10⁻³; all at 3 × 10⁻⁴ M. Direction? (Problem 6.7)', 'Qc = ' + N('1') + ' > Kc → ' + T('reverse'))
d.basic('Steps to find equilibrium concentrations (ICE)?', 'Balanced equation → table of ' + T('Initial, Change (x), Equilibrium') + ' → substitute in K → solve for x → check')
steps_card(d, 'Problem 6.8', '13.8 g N₂O₄ in 1 L at 400 K; total p at equilibrium 9.15 bar. Kp, Kc?', 'Initial p from pV = nRT.',
           ['n = 0.15 mol → p(N₂O₄)₀ = 0.15 × 0.083 × 400 = 4.98 bar', 'Total: 4.98 + x = 9.15 → x = 4.17', 'p(N₂O₄) = 0.81, p(NO₂) = 8.34 bar', 'Kp = 8.34²/0.81 = <b>85.9</b>; Kc = 85.9/(0.083 × 400) = 2.6'], 3, 'N₂O₄ dissociation Kp and Kc', 'Kp ≈ 85.9, Kc ≈ 2.6')
d.basic('3.0 mol PCl₅ in 1 L at 380 K, Kc = 1.80. Composition? (Problem 6.9)', 'x²/(3 − x) = 1.8 → x = 1.59: [PCl₃] = [Cl₂] = ' + N('1.59 M') + ', [PCl₅] = ' + N('1.41 M'))

d.sec('6.7-k-q-and-g')
d.basic('Relation of ΔG with ΔG° and Q?', r'\( \Delta G = \Delta G^{\circ} + RT \ln Q \)')
d.basic('At equilibrium, ΔG° = ?', r'\( -RT \ln K \)' + ' (since ΔG = 0 and Q = K)')
d.basic('K from ΔG°?', r'\( K = e^{-\Delta G^{\circ}/RT} \)' + ': ΔG° < 0 → K > 1')
d.basic('Kc for glucose phosphorylation, ΔG° = 13.8 kJ/mol at 298 K? (Problem 6.10)', 'ln K = −5.569 → K = ' + N('3.81 × 10⁻³'))
d.basic('ΔG° for sucrose hydrolysis, Kc = 2 × 10¹³ at 300 K? (Problem 6.11)', N('−7.64 × 10⁴ J mol⁻¹'))

# ---------------------------------------------------------------- 6.8 Le Chatelier
d.sec('6.8-le-chatelier')
d.basic('Le Chatelier’s principle?', 'A change in any factor that determines equilibrium makes the system shift so as to ' + T('counteract the change'))
d.basic('Effect of adding H₂ to H₂ + I₂ ⇌ 2HI?', 'Qc < Kc → shifts ' + T('forward') + '; new [H₂] is lower than just after addition but higher than originally', **fig('fig_6_8_add_h2'))
d.basic('Industrial use of removing a product?', 'NH₃ is ' + T('liquefied and removed') + '; CO₂ removed from the lime kiln so CaCO₃ decomposes completely')
d.basic('Fe³⁺ + SCN⁻ ⇌ [Fe(SCN)]²⁺: colours?', 'Yellow + colourless ⇌ ' + T('deep red'))
d.basic('Adding oxalic acid or HgCl₂ to the Fe(SCN)²⁺ equilibrium?', 'Removes Fe³⁺ (as [Fe(C₂O₄)₃]³⁻) or SCN⁻ (as [Hg(SCN)₄]²⁻) → shifts ' + T('back') + ', red fades')
d.basic('When does pressure (volume) change shift an equilibrium?', 'Only if gaseous moles differ (' + T('Δn ≠ 0') + '); solids/liquids ignored')
d.basic('CO + 3H₂ ⇌ CH₄ + H₂O compressed to half volume: shift?', T('Forward') + ' (4 mol gas → 2 mol); Qc becomes less than Kc')
d.basic('C(s) + CO₂ ⇌ 2CO: effect of higher pressure?', T('Reverse') + ' (forward increases gas moles)')
d.basic('Inert gas added at constant volume?', X('No effect') + ': partial pressures and concentrations unchanged')
d.basic('Inert gas added at constant pressure? (JEE extension)', 'Volume increases → shifts towards ' + T('more gaseous moles'))
d.basic('How does temperature affect K?', 'Exothermic: K ' + T('decreases') + ' with T. Endothermic: K ' + T('increases') + ' with T. (Only T changes K.)')
d.basic('2NO₂ ⇌ N₂O₄ (ΔH = −57.2 kJ): colour in ice vs hot water?', 'Cold: ' + T('paler') + ' (more N₂O₄). Hot: ' + T('darker brown') + ' (more NO₂).', **fig('fig_6_9_no2_temperature'))
d.basic('[Co(H₂O)₆]²⁺ + 4Cl⁻ ⇌ [CoCl₄]²⁻ (endothermic): colour change on cooling?', 'Blue (room T) → ' + T('pink') + ' when cooled')
d.basic('Correction: NCERT writes [Co(H₂O)₆]³⁺ and calls [CoCl₄]²⁻ "colourless". Accurate?', 'It is ' + T('[Co(H₂O)₆]²⁺') + ' (Co²⁺, pink) and [CoCl₄]²⁻ is ' + T('blue') + ' (NCERT’s own text says the mixture is blue)')
d.basic('Effect of a catalyst on equilibrium?', 'Speeds forward and reverse equally (same lowering of Eₐ); ' + X('no change') + ' in K or composition')
d.basic('Optimum Haber conditions?', T('Iron catalyst') + ', ~' + N('500 °C') + ', ~' + N('200 atm'))
d.basic('Why not run Haber at low temperature despite higher yield?', 'Rate becomes ' + X('too slow'))
d.basic('Contact process catalyst and why needed despite Kc = 1.7 × 10²⁶?', T('Pt or V₂O₅') + ': SO₂ → SO₃ is very slow')
d.basic('Can a catalyst help a reaction with tiny K?', X('Little help') + ': it cannot shift equilibrium')
d.basic('Mnemonic for Le Chatelier? (intuition)', '"' + T('The system is a contrarian') + '": add something, it uses it up; heat it, it absorbs heat; squeeze it, it makes fewer gas molecules')

# ---------------------------------------------------------------- 6.9 Ionic
d.sec('6.9-ionic-equilibrium')
d.basic('Faraday’s classification of substances?', T('Electrolytes') + ' (conduct in solution) and ' + T('non-electrolytes'))
d.basic('Strong vs weak electrolyte, with ionisation %?', T('Strong') + ': ~100% (NaCl). ' + T('Weak') + ': partial, e.g. acetic acid < 5%.')
d.basic('Why does NaCl dissolve and ionise in water?', 'Water’s high ' + T('dielectric constant (80)') + ' cuts ionic attraction 80-fold; ions get hydrated', **fig('fig_6_10_nacl_hydration'))
d.basic('Dissociation vs ionisation (NCERT)?', T('Dissociation') + ': separating ions already present (NaCl). ' + T('Ionisation') + ': neutral molecule splits into ions (HCl).')

d.sec('6.10-acids-bases-salts')
d.basic('Acids in gastric juice, vinegar, lemon, tamarind?', 'HCl (1.2–1.5 L/day); ' + E('acetic') + '; ' + E('citric and ascorbic') + '; ' + E('tartaric'))
d.basic('Origin of the word "acid"?', 'Latin "' + T('acidus') + '": sour')
d.basic('Arrhenius acids and bases?', 'Acids give ' + T('H⁺(aq)') + '; bases give ' + T('OH⁻(aq)') + ' in water')
d.basic('Limitations of the Arrhenius concept?', 'Only for ' + X('aqueous') + ' solutions; can’t explain basicity of ' + X('NH₃') + ' (no OH group)')
d.basic('Why does H⁺ exist as H₃O⁺?', 'A bare proton (~10⁻¹⁵ m) has an intense field and bonds to a lone pair of water; H₃O⁺ is ' + T('trigonal pyramidal'))
d.basic('Further hydrated forms of H₃O⁺ and OH⁻?', 'H₅O₂⁺, H₇O₃⁺, H₉O₄⁺; H₃O₂⁻, H₅O₃⁻, H₇O₄⁻')
d.basic('Brönsted–Lowry acids and bases?', 'Acid = ' + T('proton donor') + '; base = ' + T('proton acceptor'))
d.basic('What is a conjugate acid–base pair?', 'Two species differing by ' + T('one proton') + ' (NH₄⁺/NH₃, H₂O/OH⁻)')
d.basic('Strength relation in a conjugate pair?', 'Strong acid → ' + T('weak') + ' conjugate base, and vice versa')
d.basic('Conjugate bases of HF, H₂SO₄, HCO₃⁻? (Problem 6.12)', T('F⁻, HSO₄⁻, CO₃²⁻'))
d.basic('Conjugate acids of NH₂⁻, NH₃, HCOO⁻? (Problem 6.13)', T('NH₃, NH₄⁺, HCOOH'))
table_card(d, 'Problem 6.14', 'Conjugate acid / conjugate base?', [
    ('H₂O', 'H₃O⁺ / OH⁻', False), ('HCO₃⁻', 'H₂CO₃ / CO₃²⁻', False),
    ('HSO₄⁻', 'H₂SO₄ / SO₄²⁻', False), ('NH₃', 'NH₄⁺ / NH₂⁻', False)], term='Amphiprotic species')
d.basic('Lewis acids and bases (1923)?', 'Acid = ' + T('electron-pair acceptor') + '; base = ' + T('electron-pair donor'))
d.basic('Examples of Lewis acids and bases?', 'Acids: ' + E('BF₃, AlCl₃, Co³⁺, Mg²⁺, H⁺') + '. Bases: ' + E('H₂O, NH₃, OH⁻, F⁻') + '.')
d.basic('BF₃ + NH₃ → ?', T('F₃B←NH₃') + ': BF₃ accepts N’s lone pair')
d.basic('Classify OH⁻, F⁻, H⁺, BCl₃. (Problem 6.15)', 'Lewis bases: ' + T('OH⁻, F⁻') + '. Lewis acids: ' + T('H⁺, BCl₃') + '.')

d.sec('6.11-ionization-of-acids-and-bases')
d.basic('Strong acids named in NCERT?', E('HClO₄, HCl, HBr, HI, HNO₃, H₂SO₄'))
d.basic('Strong bases named in NCERT?', E('LiOH, NaOH, KOH, CsOH, Ba(OH)₂'))
d.basic('In an acid–base equilibrium, which side is favoured?', 'Towards the ' + T('weaker acid and weaker base'))
d.basic('Very strong bases (conjugates of very weak acids)?', E('NH₂⁻, O²⁻, H⁻'))
d.basic('How does an indicator like phenolphthalein work?', 'It is a weak acid whose ' + T('HIn and In⁻') + ' forms have different colours')
d.basic('Ionic product of water at 298 K?', r'\( K_w = [H^+][OH^-] = 1.0 \times 10^{-14} \)')
d.basic('Molarity of pure water, and fraction dissociated?', N('55.55 M') + '; about ' + N('2 in 10⁹') + ' molecules')
d.basic('Is Kw constant with temperature?', X('No') + ': it increases with T (ionisation is endothermic), so neutral pH < 7 at higher T')
d.basic('Definition of pH (strict)?', r'\( pH = -\log a_{H^+} \)' + '; for dilute solutions ≈ −log[H⁺]')
d.cloze('At 298 K: pH + pOH = {{c1::14}}; acidic pH {{c2::< 7}}; basic pH {{c3::> 7}}.')
d.basic('A tenfold change in [H⁺] changes pH by?', N('1 unit') + ' (100-fold → 2 units)')
d.basic('pH of 10⁻² M HCl and of NaOH with [OH⁻] = 10⁻⁴ M?', N('2') + ' and ' + N('10'))
d.basic('Accuracy of pH paper vs pH meter?', 'Paper ~' + N('0.5') + ' (four-strip paper, Fig 6.11); meter ~' + N('0.001'), **fig('fig_6_11_ph_paper'))
d.basic('pH of human blood, gastric juice, lemon juice, milk of magnesia?', N('7.4') + ', ~' + N('1.2') + ', ~' + N('2.2') + ', ' + N('10'), **fig('tab_6_5_ph_common'))
d.basic('pH of soft drink with [H⁺] = 3.8 × 10⁻³ M? (Problem 6.16)', N('2.42'))
steps_card(d, 'Problem 6.17', 'pH of 1.0 × 10⁻⁸ M HCl?', 'Trap: water’s own H⁺ cannot be ignored.',
           ['[H⁺] = 10⁻⁸ + x; [OH⁻] = x', '(10⁻⁸ + x)x = 10⁻¹⁴ → x = 9.5 × 10⁻⁸', 'pOH = 7.02 → <b>pH = 6.98</b>'], 2, 'pH of very dilute acid', '6.98')
d.basic('Why isn’t pH of 10⁻⁸ M HCl equal to 8? (trap)', 'An acid can’t be basic: water supplies ' + T('10⁻⁷ M H⁺') + ', far more than the acid')
d.basic('Ka for weak acid HX in terms of c and α?', r'\( K_a = \frac{c\alpha^2}{1 - \alpha} \approx c\alpha^2 \)')
d.basic('Ostwald dilution law shortcut for weak acids?', r'\( \alpha \approx \sqrt{K_a / c} \)' + ', ' + r'\( [H^+] \approx \sqrt{K_a c} \)')
d.basic('Strongest and weakest acid in Table 6.6?', 'Strongest: ' + T('HNO₂') + ' (4.5 × 10⁻⁴); weakest: ' + T('phenol') + ' (1.3 × 10⁻¹⁰)', **fig('tab_6_6_ka_weak_acids'))
d.basic('Define pKa. Larger pKa means?', 'pKa = −log Ka; larger pKa → ' + T('weaker') + ' acid')
steps_card(d, 'Problem 6.18', '0.02 M HF, Ka = 3.2 × 10⁻⁴. α, species and pH?', 'Ka ≫ Kw, so HF ionisation is the main reaction.',
           ['0.02α²/(1 − α) = 3.2 × 10⁻⁴', 'α = 0.12', '[H₃O⁺] = [F⁻] = 2.4 × 10⁻³ M; [HF] = 17.6 × 10⁻³ M', 'pH = <b>2.62</b>'], 1, 'Degree of ionisation of HF', 'α = 0.12, pH 2.62')
d.basic('0.1 M monobasic acid has pH 4.50. Ka and pKa? (Problem 6.19)', '[H⁺] = 3.16 × 10⁻⁵; Ka = ' + N('1.0 × 10⁻⁸') + ', pKa = ' + N('8'))
d.basic('pH and % dissociation of 0.08 M HOCl, Ka = 2.5 × 10⁻⁵? (Problem 6.20)', '[H⁺] = 1.41 × 10⁻³; ' + N('1.76%') + '; pH ' + N('2.85'))
d.basic('Kb for weak base in terms of c and α?', r'\( K_b = \frac{c\alpha^2}{1 - \alpha} \)')
d.basic('Weakest and strongest base in Table 6.7?', 'Strongest: ' + T('dimethylamine') + ' (5.4 × 10⁻⁴); weakest: ' + T('urea') + ' (1.3 × 10⁻¹⁴)', **fig('tab_6_7_kb_weak_bases'))
d.basic('Kb of 0.004 M hydrazine with pH 9.7? (Problem 6.21)', '[OH⁻] = 5.98 × 10⁻⁵; Kb = ' + N('8.96 × 10⁻⁷') + ', pKb = ' + N('6.04'))
d.basic('pH of 0.2 M NH₄Cl + 0.1 M NH₃, pKb = 4.75? (Problem 6.22)', '[OH⁻] = 0.88 × 10⁻⁵ → pH ' + N('8.95'))
d.basic('Relation between Ka and Kb of a conjugate pair?', r'\( K_a \times K_b = K_w \)' + '; pKa + pKb = 14')
d.basic('Ka of NH₄⁺ from Kb(NH₃) = 1.77 × 10⁻⁵?', N('5.64 × 10⁻¹⁰'))
d.basic('α and pH of 0.05 M NH₃? (Problem 6.23)', 'α = ' + N('0.018') + ', [OH⁻] = 9.4 × 10⁻⁴, pH = ' + N('10.97'))
d.basic('K for a net reaction made by adding reactions?', r'\( K_{net} = K_1 \times K_2 \times \dots \)')
d.basic('What are polybasic (polyprotic) acids?', 'Acids with more than one ionisable proton: ' + E('oxalic, H₂SO₄, H₃PO₄'), **fig('tab_6_8_polyprotic'))
d.basic('Why is Ka₂ < Ka₁?', 'Harder to remove H⁺ from a ' + T('negatively charged') + ' ion')
d.basic('Acid strength down a group (HF → HI)? Deciding factor?', 'Increases: ' + T('HF ≪ HCl ≪ HBr ≪ HI') + '; weaker H–A bond (size) decides')
d.basic('Acid strength across a period (CH₄ → HF)? Deciding factor?', 'Increases: ' + T('CH₄ < NH₃ < H₂O < HF') + '; bond polarity (electronegativity) decides')
d.basic('Which is the stronger acid, H₂S or H₂O?', T('H₂S') + ' (weaker, longer H–S bond)')
d.basic('What is the common ion effect?', 'Suppression of ionisation by adding a substance that supplies an ' + T('ion already present') + '; a Le Chatelier effect')
d.basic('pH of 0.05 M acetic acid + 0.05 M acetate, Ka = 1.8 × 10⁻⁵?', '[H⁺] = Ka → pH = ' + N('4.74'))
steps_card(d, 'Problem 6.24', '50 mL 0.10 M NH₃ + 25 mL 0.10 M HCl. pH before and after? (Kb 1.77 × 10⁻⁵)', 'Half the NH₃ is neutralised.',
           ['Before: [OH⁻] = √(1.77×10⁻⁶) = 1.33 × 10⁻³ → pH 11.12', '5 mmol NH₃ − 2.5 mmol HCl → 2.5 mmol NH₃ + 2.5 mmol NH₄⁺', 'Equal amounts: [OH⁻] = Kb = 1.77 × 10⁻⁵', 'pH = <b>9.24</b>'], 3, 'Half-neutralised ammonia', 'pH 11.12 → 9.24')

d.sec('6.11.9-hydrolysis-of-salts')
d.basic('What is salt hydrolysis?', 'Reaction of a salt’s cation/anion with ' + T('water') + ' to re-form the weak acid/base, changing pH')
table_card(d, 'Salt hydrolysis', 'Nature of solution?', [
    ('Strong acid + strong base (NaCl)', 'Neutral, pH 7 (no hydrolysis)', False), ('Weak acid + strong base (CH₃COONa)', 'Basic, pH > 7', False),
    ('Strong acid + weak base (NH₄Cl)', 'Acidic, pH < 7', False), ('Weak acid + weak base (CH₃COONH₄)', 'pH = 7 + ½(pKa − pKb)', False)], term='pH of salt solutions')
d.basic('Why is CH₃COONa solution basic?', 'CH₃COO⁻ + H₂O ⇌ CH₃COOH + ' + T('OH⁻'))
d.basic('Why is NH₄Cl solution acidic?', 'NH₄⁺ + H₂O ⇌ NH₄OH + ' + T('H⁺'))
d.basic('Special feature of weak acid–weak base salt hydrolysis?', 'Degree of hydrolysis and pH are ' + T('independent of concentration'))
d.basic('pH of ammonium acetate, pKa 4.76, pKb 4.75? (Problem 6.25)', '7 + ½(0.01) = ' + N('7.005'))

d.sec('6.12-buffers')
d.basic('Define a buffer solution.', 'Resists change in pH on ' + T('dilution') + ' or adding ' + T('small amounts') + ' of acid/base')
d.basic('Two classic buffers and their pH?', 'Acetic acid + sodium acetate ~' + N('4.75') + '; NH₄Cl + NH₄OH ~' + N('9.25'))
d.basic('Henderson–Hasselbalch equation (acidic buffer)?', r'\( pH = pK_a + \log \frac{[salt]}{[acid]} \)')
d.basic('Basic buffer equation?', r'\( pOH = pK_b + \log \frac{[salt]}{[base]} \)')
d.basic('When is buffer pH = pKa?', 'When [salt] = [acid] (log 1 = 0)')
d.basic('How do you choose an acid to make a buffer of a given pH?', 'Pick one whose ' + T('pKa is close') + ' to the target pH')
d.basic('Why doesn’t dilution change buffer pH?', 'The ' + T('ratio') + ' [salt]/[acid] is unchanged')
d.basic('Why does blood need buffering? (intuition)', 'Enzymes work in a narrow pH window (~7.4); the H₂CO₃/HCO₃⁻ buffer mops up added H⁺ or OH⁻')

d.sec('6.13-solubility-equilibria')
table_card(d, 'Solubility classes', 'Range?', [
    ('Soluble', '> 0.1 M', False), ('Slightly soluble', '0.01–0.1 M', False), ('Sparingly soluble', '< 0.01 M', True)], term='Solubility categories')
d.basic('Condition for a salt to dissolve?', 'Solvation enthalpy must ' + T('exceed') + ' lattice enthalpy; hence ionic salts don’t dissolve in non-polar solvents')
d.basic('Define solubility product.', r'\( K_{sp} = [Ba^{2+}][SO_4^{2-}] \)' + ' for BaSO₄ ⇌ Ba²⁺ + SO₄²⁻ (saturated solution)')
d.basic('Molar solubility of BaSO₄, Ksp = 1.1 × 10⁻¹⁰?', 'S = √Ksp = ' + N('1.05 × 10⁻⁵ M'))
d.basic('General Ksp for MₓXᵧ with solubility S?', r'\( K_{sp} = x^x y^y S^{x+y} \)')
d.basic('Ksp of Zr₃(PO₄)₄ in terms of S?', r'\( (3S)^3 (4S)^4 = 6912 \, S^7 \)')
d.basic('Solubility of A₂X₃, Ksp = 1.1 × 10⁻²³? (Problem 6.26)', '108 S⁵ = 1.1 × 10⁻²³ → S = ' + N('1.0 × 10⁻⁵ M'))
d.basic('Qsp vs Ksp: precipitation or dissolution?', 'Qsp > Ksp → ' + T('precipitates') + '; Qsp < Ksp → more dissolves')
d.basic('Ksp values of common salts (Table 6.9)?', 'e.g. AgCl 1.8 × 10⁻¹⁰, BaSO₄ 1.1 × 10⁻¹⁰, CaCO₃ 2.8 × 10⁻⁹', **fig('tab_6_9a_ksp'))
d.basic('Table 6.9 continued?', 'Lead to zinc salts', **fig('tab_6_9b_ksp'))
d.basic('More soluble: Ni(OH)₂ (Ksp 2 × 10⁻¹⁵) or AgCN (6 × 10⁻¹⁷)? (Problem 6.27)', 'AgCN: S = 7.8 × 10⁻⁹. Ni(OH)₂: 4S³ = 2 × 10⁻¹⁵ → S = 7.9 × 10⁻⁶. ' + T('Ni(OH)₂') + ' is more soluble.')
d.basic('Correction: NCERT gives S of Ni(OH)₂ as 0.58 × 10⁻⁴ M. Recompute.', '(2 × 10⁻¹⁵ / 4)^(1/3) = ' + T('7.9 × 10⁻⁶ M') + '; the conclusion (Ni(OH)₂ more soluble) still holds')
d.basic('Trap: compare solubility by Ksp directly?', X('Only for the same formula type') + ': convert to S first when stoichiometry differs')
d.basic('Molar solubility of Ni(OH)₂ in 0.10 M NaOH? (Problem 6.28)', 'S × (0.10)² = 2 × 10⁻¹⁵ → S = ' + N('2 × 10⁻¹³ M'))
d.basic('How is very pure NaCl obtained by the common ion effect?', 'Pass ' + T('HCl gas') + ' through saturated brine: extra Cl⁻ precipitates NaCl')
d.basic('Use of common ion effect in gravimetric analysis?', 'Near-complete precipitation: Ag⁺ as AgCl, Fe³⁺ as hydroxide, Ba²⁺ as BaSO₄')
d.basic('Why are phosphates more soluble at low pH?', 'H⁺ protonates the anion, lowering its concentration, so more salt dissolves')

# ---------------------------------------------------------------- summary
d.sec('summary')
table_card(d, 'Summary', 'Effect on equilibrium?', [
    ('Add reactant', 'Shifts forward (K unchanged)', False), ('Raise T (exothermic)', 'Shifts back; K falls', True),
    ('Raise p (fewer gas moles on right)', 'Shifts forward', False), ('Inert gas, constant V', 'No effect', True),
    ('Catalyst', 'No effect; faster equilibrium', True)], term='Le Chatelier summary')
table_card(d, 'Summary', 'Formula?', [
    ('Kp and Kc', 'Kp = Kc(RT)^Δn', False), ('ΔG° and K', 'ΔG° = −RT ln K', False), ('Weak acid', '[H⁺] = √(Ka·c)', False),
    ('Conjugate pair', 'Ka·Kb = Kw', False), ('Buffer', 'pH = pKa + log[salt]/[acid]', False), ('Ksp of MₓXᵧ', 'xˣyʸS^(x+y)', False)], term='Equilibrium formula sheet')

n = d.write(os.path.join(OUT, 'deck.json'))
print(n, 'cards')
