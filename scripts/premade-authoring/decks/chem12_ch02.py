import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Chemistry', 'class12-chemistry-ch02-electrochemistry')
d = Deck('Chapter 2: Electrochemistry', 'Class 12', ['class-12', 'chemistry', 'ch-2'])
d.description = 'Galvanic cells, electrode potentials, Nernst equation, Gibbs energy, conductivity, Kohlrausch law, electrolysis, batteries, fuel cells, corrosion'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- intro
d.sec('2.0-introduction')
d.basic('What is electrochemistry?', 'Study of producing ' + T('electricity from spontaneous reactions') + ' and using electricity to drive ' + T('non-spontaneous') + ' ones')
d.basic('Galvanic cell vs electrolytic cell: energy conversion?', T('Galvanic') + ': chemical → electrical (spontaneous, ΔG < 0). ' + T('Electrolytic') + ': electrical → chemical (non-spontaneous).')

# ---------------------------------------------------------------- 2.1 Electrochemical cells
d.sec('2.1-electrochemical-cells')
d.basic('Cell reaction and emf of the Daniell cell?', r'\( Zn + Cu^{2+} \rightarrow Zn^{2+} + Cu \)' + '; ' + N('1.1 V') + ' at unit concentrations', **fig('fig_2_1_daniell_cell'))
d.occlusion('Figure 2.1 · Daniell cell', M + 'fig_2_1_daniell_cell.webp', (1001, 963), [
    ('Zinc (anode)', [62, 298, 115, 62], False), ('Copper (cathode)', [832, 298, 165, 62], False), ('Salt bridge', [372, 326, 225, 64], True)], guess='hide-all')
d.basic('External voltage opposing a Daniell cell: E_ext < 1.1 V, = 1.1 V, > 1.1 V?', '< 1.1 V: works as a ' + T('galvanic cell') + '<br>= 1.1 V: ' + X('no current, no reaction') + '<br>> 1.1 V: reaction ' + T('reverses') + ' (Zn deposits, Cu dissolves): electrolytic cell', **fig('fig_2_2_external_voltage'))
d.basic('Intuition: what does E_ext = 1.1 V tell you about the cell?', 'The opposing push exactly balances the reaction’s own "push"; so emf is the maximum voltage the reaction can supply')
d.basic('Correction/footnote: concentration or activity in the Nernst equation?', 'Strictly ' + T('activity') + '; it equals concentration only in dilute solutions')

# ---------------------------------------------------------------- 2.2 Galvanic cells
d.sec('2.2-galvanic-cells')
d.basic('Half-reactions in the Daniell cell and where they occur?', 'Reduction ' + r'\( Cu^{2+} + 2e^- \rightarrow Cu \)' + ' at copper; oxidation ' + r'\( Zn \rightarrow Zn^{2+} + 2e^- \)' + ' at zinc')
d.basic('What is a half-cell (redox couple)?', 'A metal electrode dipped in its electrolyte; the reduction half-cell and the oxidation half-cell')
d.basic('When is a salt bridge not needed?', 'When both electrodes dip in the ' + T('same electrolyte'))
d.basic('Why is a salt bridge needed? (teacher addition)', 'It completes the circuit and keeps both solutions ' + T('electrically neutral') + '.<br>Without it, charge builds up and current stops at once')
d.basic('What is electrode potential?', 'The potential difference between an electrode and its electrolyte, from the balance of metal → ion and ion → metal tendencies')
d.basic('What is standard electrode potential?', 'Electrode potential when all species are at ' + T('unit concentration') + ' (gases 1 bar), usually 298 K.<br>IUPAC: standard reduction potential')
d.cloze('In a galvanic cell, oxidation occurs at the {{c1::anode}}, which is {{c2::negative}}; reduction occurs at the {{c3::cathode}}, which is {{c4::positive}}.')
d.basic('Direction of electron flow and current in the external circuit?', 'Electrons: ' + T('anode → cathode') + ' (− to +). Current: the ' + X('opposite') + ' direction.')
d.basic('Mnemonic for anode and cathode?', T('An Ox, Red Cat') + ': ANode = OXidation, REDuction = CAThode. True in every cell.')
table_card(d, 'Sign trap', 'Sign of the electrode?', [
    ('Galvanic cell: anode', '− (negative)', False), ('Galvanic cell: cathode', '+ (positive)', False),
    ('Electrolytic cell: anode', '+ (connected to battery +)', True), ('Electrolytic cell: cathode', '− (connected to battery −)', True)],
    note='Oxidation is always at the anode; only the sign flips, because in electrolysis the battery forces electrons in.', term='Anode and cathode signs in the two cell types')
d.basic('Intuition: why is the galvanic anode negative?', 'Oxidation there ' + T('releases electrons') + ' into the metal, so electrons pile up: it is the electron source (−)')
d.basic('Cell potential vs emf?', 'Both = E(cathode) − E(anode); called ' + T('emf') + ' when ' + X('no current') + ' is drawn')
d.basic('Cell notation convention?', T('Anode on the left') + ', cathode on the right; | = phase boundary; || = salt bridge; e.g. Cu|Cu²⁺||Ag⁺|Ag')
d.basic('Formula for E_cell from electrode potentials?', r'\( E_{cell} = E_{right} - E_{left} = E_{cathode} - E_{anode} \)' + ' (both as reduction potentials)')
d.basic('Trap: in E_cell = E_cathode − E_anode, do you reverse the anode’s sign as well?', X('No') + ': use both ' + T('reduction potentials as listed') + '; the minus sign already accounts for the anode being an oxidation')

d.sec('2.2.1-measurement-of-electrode-potential')
d.basic('Why can’t a single electrode potential be measured?', 'A voltmeter needs ' + T('two electrodes') + '; only differences can be measured, so a reference is chosen')
d.basic('Standard hydrogen electrode (SHE): notation and potential?', 'Pt(s)|H₂(g, 1 bar)|H⁺(aq, 1 M); assigned ' + N('0 V at all temperatures'))
d.occlusion('Figure 2.3 · Standard hydrogen electrode', M + 'fig_2_3_she.webp', (1001, 919), [
    ('H₂(g) at 1 bar', [590, 180, 175, 108], True), ('Finely divided platinum coated on platinum foil', [612, 730, 330, 160], True), ('1.00 M H⁺', [250, 758, 230, 64], True)])
d.basic('Construction of SHE?', 'Pt electrode coated with ' + T('platinum black') + ', dipped in 1 M acid, pure H₂ bubbled at 1 bar')
d.basic('How is E° of Cu²⁺/Cu measured?', 'SHE as anode (left), Cu half-cell as cathode: measured emf ' + N('0.34 V') + ' = E°')
d.basic('E° of Zn²⁺/Zn and its meaning?', N('−0.76 V') + ': H⁺ can oxidise Zn (Zn dissolves in acids)')
d.basic('Why doesn’t Cu dissolve in HCl, but does in HNO₃?', 'E°(Cu²⁺/Cu) > 0, so ' + X('H⁺ cannot oxidise Cu') + '; in HNO₃ the ' + T('nitrate ion') + ' is the oxidant')
d.basic('E° of Daniell cell from E° values?', '0.34 − (−0.76) = ' + N('1.10 V'))
d.basic('Role of Pt or Au as inert electrodes?', 'Provide a ' + T('surface') + ' for the redox reaction and conduct electrons, without reacting (H₂ electrode, Br₂ electrode)')
d.basic('Positive E° means the reduced form is…?', 'More stable than H₂; the couple is a ' + T('weaker reducing agent') + ' than H⁺/H₂')
d.basic('Strongest oxidising agent and strongest reducing agent in Table 2.1?', T('F₂') + ' (E° = +2.87 V); ' + T('Li') + ' (E° = −3.05 V)', **fig('tab_2_1_electrode_potentials'))
d.basic('Going down Table 2.1 (E° decreasing): trend?', 'Oxidising power of the left-side species ' + X('falls') + '; reducing power of the right-side species ' + T('rises'))
d.basic('Intuition: how to read E° as a "tug of war" for electrons?', 'Higher E° = grabs electrons harder (gets reduced). In any pair, the ' + T('higher-E° couple is reduced') + ', the lower one is oxidised')
d.basic('Can CuSO₄ be stored in a zinc pot? (Intext 2.2)', X('No') + ': E°(Zn) < E°(Cu), so Zn reduces Cu²⁺ and the pot dissolves')
d.basic('Three substances that can oxidise Fe²⁺? (Intext 2.3)', 'Any with E° > 0.77 V: ' + E('F₂, Cl₂, Br₂, MnO₄⁻/H⁺, Cr₂O₇²⁻/H⁺, H₂O₂'))
d.basic('Uses of electrochemical cells (NCERT list)?', 'Finding ' + T('pH') + ', solubility product, equilibrium constants, thermodynamic data; potentiometric titrations')

# ---------------------------------------------------------------- 2.3 Nernst
d.sec('2.3-nernst-equation')
d.basic('Nernst equation for Mⁿ⁺ + ne⁻ → M?', r'\( E = E^{\circ} - \frac{RT}{nF} \ln \frac{1}{[M^{n+}]} \)')
d.basic('Nernst equation for a cell at 298 K?', r'\( E_{cell} = E^{\circ}_{cell} - \frac{0.059}{n} \log Q \)')
d.basic('Where does 0.059 V come from?', r'\( \frac{2.303 \, RT}{F} \)' + ' at 298 K = 2.303 × 8.314 × 298 / 96487')
d.basic('Nernst equation for the Daniell cell?', r'\( E_{cell} = 1.1 - \frac{0.059}{2} \log \frac{[Zn^{2+}]}{[Cu^{2+}]} \)')
d.basic('How does E_cell of Daniell cell change with [Cu²⁺] and [Zn²⁺]?', 'Rises with more ' + T('Cu²⁺') + ' (reactant), falls with more ' + X('Zn²⁺') + ' (product)')
d.basic('Intuition: Nernst equation = Le Chatelier?', 'More reactant pushes the reaction forward, so the cell "pushes" electrons harder (higher E).<br>More product pushes back')
d.basic('What goes into Q in the Nernst equation?', T('Products over reactants') + ' with powers; solids and pure liquids = 1; gases as partial pressures')
d.basic('Trap: n for Ni + 2Ag⁺ → Ni²⁺ + 2Ag?', N('n = 2') + ' (electrons transferred), and Q = [Ni²⁺]/[Ag⁺]²')
d.basic('Potential of hydrogen electrode at pH 10? (Intext 2.4)', 'E = −0.059 × pH = ' + N('−0.59 V'))
steps_card(d, 'Example 2.1', 'Mg + 2Ag⁺(0.0001 M) → Mg²⁺(0.130 M) + 2Ag; E° = 3.17 V. E_cell?', 'Cell: Mg|Mg²⁺(0.130 M)||Ag⁺(0.0001 M)|Ag; n = 2.',
           ['Q = 0.130 / (0.0001)² = 1.3 × 10⁷', 'log Q = 7.11', 'E = 3.17 − 0.0295 × 7.11 = 3.17 − 0.21', '= <b>2.96 V</b>'], 2, 'Nernst: Mg–Ag cell', '2.96 V')
d.basic('emf of Ni|Ni²⁺(0.160 M)||Ag⁺(0.002 M)|Ag, E° = 1.05 V? (Intext 2.5)', 'Q = 0.160/(0.002)² = 4 × 10⁴; E = 1.05 − 0.0295 × 4.60 = ' + N('0.91 V'))
d.basic('What happens to a Daniell cell’s voltage as it runs?', '[Zn²⁺] rises, [Cu²⁺] falls, so E ' + X('drops') + ' until ' + T('E = 0 at equilibrium'))

d.sec('2.3.1-equilibrium-constant')
d.basic('Relation between E°_cell and K?', r'\( E^{\circ}_{cell} = \frac{2.303 \, RT}{nF} \log K_C = \frac{0.059}{n} \log K_C \)' + ' (298 K)')
d.basic('K_C for the Daniell cell reaction?', 'log K = 2 × 1.1/0.059 = 37.3, so K_C ≈ ' + N('2 × 10³⁷') + ': goes to completion')
d.basic('K for Cu + 2Ag⁺ → Cu²⁺ + 2Ag, E° = 0.46 V? (Example 2.2)', 'log K = 0.46 × 2/0.059 = 15.6 → K = ' + N('3.92 × 10¹⁵'))
d.basic('Intuition: why do small E° values give enormous K?', 'K depends on E° ' + T('exponentially') + ': every 0.059/n V multiplies K by 10')

d.sec('2.3.2-gibbs-energy')
d.basic('Relation between ΔrG and E_cell?', r'\( \Delta_r G = -nFE_{cell} \)' + '; standard: ' + r'\( \Delta_r G^{\circ} = -nFE^{\circ}_{cell} \)')
d.basic('Why is ΔrG = −nFE the maximum useful work?', 'Reversible work (charge nF moved through potential E) equals the ' + T('decrease in Gibbs energy'))
d.basic('Spontaneous cell: signs of E and ΔG?', T('E > 0, ΔG < 0') + ' (and K > 1)')
d.basic('E_cell is intensive; ΔrG is extensive. Consequence?', 'Doubling the equation ' + T('doubles ΔG') + ' (n doubles) but ' + X('E stays the same'))
d.basic('Trap: to balance 2Ag⁺ + 2e⁻ → 2Ag, do you double E°(Ag⁺/Ag)?', X('Never') + ': E° is intensive (volts = energy per charge). Keep 0.80 V.')
steps_card(d, 'Combining half-cells', 'E°(Fe³⁺/Fe²⁺) = 0.77 V, E°(Fe²⁺/Fe) = −0.44 V. E°(Fe³⁺/Fe)?', 'Potentials don’t add for a half-cell; ΔG does.',
           ['ΔG₁ = −1·F·0.77 = −0.77F', 'ΔG₂ = −2·F·(−0.44) = +0.88F', 'ΔG₃ = ΔG₁ + ΔG₂ = +0.11F = −3F·E°', 'E°(Fe³⁺/Fe) = <b>−0.037 V</b>'], 3, 'Combining electrode potentials via ΔG', '−0.037 V')
steps_card(d, 'Example 2.3', 'Daniell cell, E° = 1.1 V. ΔrG°?', 'n = 2, F = 96487 C mol⁻¹.',
           ['ΔrG° = −nFE°', '= −2 × 96487 × 1.1', '= −212,271 J mol⁻¹ = <b>−212.27 kJ mol⁻¹</b>'], 2, 'ΔG° of the Daniell cell', '−212.27 kJ/mol')
d.basic('Correction: NCERT Example 2.3 prints ΔrG° = −21227 J mol⁻¹. Right value?', T('−212,271 J mol⁻¹') + ' (a digit is missing); the kJ value, −212.27, is correct')
d.basic('ΔG° and K for 2Fe³⁺ + 2I⁻ → 2Fe²⁺ + I₂, E° = 0.236 V? (Intext 2.6)', 'ΔG° = −2 × 96487 × 0.236 = ' + N('−45.5 kJ/mol') + '; log K = 8.0 → K ≈ ' + N('1 × 10⁸'))
table_card(d, 'Link', 'Spontaneity from each?', [
    ('E°cell > 0', 'ΔG° < 0, K > 1: forward favoured', False), ('E°cell = 0', 'ΔG° = 0, K = 1', False), ('E°cell < 0', 'ΔG° > 0, K < 1: reverse favoured', True)],
    note='ΔG° = −nFE° = −RT ln K ties all three together.', term='E°, ΔG° and K')

# ---------------------------------------------------------------- 2.4 Conductance
d.sec('2.4-conductance')
d.basic('Resistance in terms of resistivity?', r'\( R = \rho \frac{l}{A} \)' + '; ρ in ' + N('Ω m') + ' (1 Ω m = 100 Ω cm)')
d.basic('Conductance G and conductivity κ?', r'\( G = \frac{1}{R} = \kappa \frac{A}{l} \)' + '; G in siemens (S = Ω⁻¹ = mho); κ = 1/ρ in S m⁻¹')
d.basic('Unit conversion: 1 S cm⁻¹ = ? S m⁻¹', N('100 S m⁻¹'))
d.basic('Metallic (electronic) conductance depends on?', 'Nature and structure of metal, number of ' + T('valence electrons') + ', temperature (' + X('decreases') + ' as T rises)')
d.basic('Conductivity of pure water and why?', N('3.5 × 10⁻⁵ S m⁻¹') + ': only ~10⁻⁷ M H⁺ and OH⁻ from self-ionisation')
d.basic('Correction: NCERT Table 2.2 lists metals at ~10³ S m⁻¹ (Cu 5.9 × 10³). Real values?', 'About ' + T('10⁷ S m⁻¹') + ' (Cu ≈ 5.9 × 10⁷, Ag ≈ 6.2 × 10⁷); the table’s exponents are off by 10⁴')
d.cloze('Classes by conductivity: {{c1::conductors}} (metals, graphite), {{c2::insulators}} (glass, Teflon), {{c3::semiconductors}} (Si, doped Si, GaAs), {{c4::superconductors}} (zero resistivity).')
d.basic('Superconductors: temperature range?', 'Metals/alloys at ' + N('0–15 K') + '; some ceramics and mixed oxides up to ~' + N('150 K'))
d.basic('Conducting polymers: discovery and examples (box)?', T('Polyacetylene') + ' doped with I₂ (MacDiarmid, Heeger, Shirakawa, Nobel 2000)<br>Also polyaniline, polypyrrole, polythiophene')
d.basic('Ionic (electrolytic) conductivity depends on?', 'Nature of electrolyte<br>' + T('Ion size and solvation') + '<br>Solvent and its viscosity<br>Concentration<br>Temperature (' + T('increases') + ' with T)')
d.basic('Intuition: why does heating raise ionic but lower metallic conductivity?', 'Hot solvent is ' + T('less viscous') + ', so ions move faster; in metals, hotter vibrating atoms ' + X('scatter electrons') + ' more')
d.basic('Metallic vs electrolytic conduction: effect on the conductor?', 'Metal: composition ' + T('unchanged') + '. Electrolyte: prolonged DC ' + X('changes composition') + ' (electrolysis)')

d.sec('2.4.1-measuring-conductivity')
d.basic('Two problems in measuring resistance of a solution, and the fixes?', 'DC changes the solution → use ' + T('AC') + '. Solution can’t be clamped like a wire → use a ' + T('conductivity cell') + '.', **fig('fig_2_4_conductivity_cells'))
d.basic('Why are the electrodes platinised (Pt black)?', 'Finely divided Pt gives a large surface; reduces polarisation errors (teacher note)')
d.basic('What is the cell constant G*?', r'\( G^* = \frac{l}{A} = R \kappa \)' + '; unit length⁻¹; found using ' + T('KCl solutions of known κ'), **fig('tab_2_3_kcl_conductivity'))
d.basic('Wheatstone bridge for solutions: source and detector?', 'Oscillator O: AC at ' + N('550–5000 Hz') + '; detector P: headphone; at balance ' + r'\( R_2 = \frac{R_1 R_4}{R_3} \)', **fig('fig_2_5_wheatstone'))
d.basic('Conductivity from cell constant?', r'\( \kappa = \frac{G^*}{R} \)')
d.basic('Define molar conductivity.', r'\( \Lambda_m = \frac{\kappa}{c} \)' + ': conductivity per unit molar concentration')
d.basic('Λm in S cm² mol⁻¹ from κ in S cm⁻¹ and molarity M?', r'\( \Lambda_m = \frac{1000 \, \kappa}{M} \)')
d.basic('1 S m² mol⁻¹ = ? S cm² mol⁻¹', N('10⁴'))
steps_card(d, 'Example 2.4', 'Cell: 100 Ω with 0.1 M KCl (κ 1.29 S/m); 520 Ω with 0.02 M KCl. κ and Λm of 0.02 M KCl?', 'Find G* first.',
           ['G* = κR = 1.29 × 100 = 129 m⁻¹', 'κ = G*/R = 129/520 = <b>0.248 S m⁻¹</b>', 'c = 0.02 M = 20 mol m⁻³', 'Λm = 0.248/20 = <b>124 × 10⁻⁴ S m² mol⁻¹</b> (124 S cm² mol⁻¹)'], 1, 'Conductivity from cell constant', 'κ 0.248 S/m; Λm 124 S cm²/mol')
steps_card(d, 'Example 2.5', '0.05 M NaOH column: d = 1 cm, l = 50 cm, R = 5.55 × 10³ Ω. ρ, κ, Λm?', 'A = πr² = 0.785 cm².',
           ['ρ = RA/l = 5550 × 0.785/50 = <b>87.1 Ω cm</b>', 'κ = 1/ρ = <b>0.01148 S cm⁻¹</b>', 'Λm = 1000 × 0.01148/0.05 = <b>229.6 S cm² mol⁻¹</b>'], 2, 'Resistivity, conductivity and Λm of NaOH', '87.1 Ω cm; 0.01148 S/cm; 229.6')

d.sec('2.4.2-variation-with-concentration')
d.basic('Effect of dilution on κ, and why?', 'κ ' + X('decreases') + ' (strong and weak): fewer ions per unit volume')
d.basic('Effect of dilution on Λm, and why?', 'Λm ' + T('increases') + ': Λm = κV, and the rise in V (volume holding 1 mol) outweighs the fall in κ')
d.basic('Intuition: κ vs Λm on dilution?', 'κ = current carriers in a fixed 1 cm³ box (fewer as you dilute).<br>Λm = all ions from ' + T('1 mole') + ', wherever they are.<br>They are never lost, and on dilution they move more freely (and weak ones ionise more)')
d.basic('What is limiting molar conductivity Λ°m?', 'Λm as concentration → ' + T('zero') + ' (infinite dilution)')
d.basic('Debye–Hückel–Onsager form for strong electrolytes?', r'\( \Lambda_m = \Lambda^{\circ}_m - A\sqrt{c} \)' + '; Λm vs √c is a straight line, intercept Λ°m, slope −A')
d.basic('A depends on?', 'Solvent, temperature and electrolyte ' + T('type') + ' (1-1 NaCl, 2-1 CaCl₂, 2-2 MgSO₄); same for all of one type')
d.basic('Strong vs weak electrolyte: shape of Λm vs √c?', 'Strong (KCl): ' + T('gentle straight line') + '. Weak (CH₃COOH): ' + T('steep rise') + ' near zero concentration.', **fig('fig_2_6_molar_conductivity'))
d.basic('Why does Λm of a weak electrolyte rise so steeply on dilution?', 'Degree of ' + T('dissociation α increases') + ', creating many more ions per mole')
d.basic('Why can’t Λ°m of a weak electrolyte be found by extrapolation?', 'The curve is steep and non-linear near c = 0, and at such dilution κ is ' + X('too small to measure accurately'))
d.basic('Λ°m and A for KCl from Example 2.6?', 'Λ°m = ' + N('150.0 S cm² mol⁻¹') + '; A = ' + N('87.46 S cm² mol⁻¹ (mol/L)⁻¹ᐟ²'), **fig('fig_2_7_kcl_plot'))

d.sec('2.4.3-kohlrausch-law')
d.basic('Kohlrausch’s observation?', 'Λ°(KX) − Λ°(NaX) ≈ ' + N('23.4') + ' for any X; Λ°(NaBr) − Λ°(NaCl) ≈ ' + N('1.8') + ' S cm² mol⁻¹: each ion contributes a fixed amount')
d.basic('Kohlrausch law of independent migration of ions?', 'Λ°m of an electrolyte = sum of the limiting molar conductivities of its ' + T('cation and anion') + r': \( \Lambda^{\circ}_m = \nu_+ \lambda^{\circ}_+ + \nu_- \lambda^{\circ}_- \)')
d.basic('Why are λ° of H⁺ (349.6) and OH⁻ (199.1) so high?', 'They hop along H-bonded water chains (' + T('Grotthuss mechanism') + ') instead of moving bodily (teacher addition)', **fig('tab_2_4_ion_conductivity'))
d.basic('Λ°m of CaCl₂ and MgSO₄? (Example 2.7)', 'CaCl₂: 119.0 + 2(76.3) = ' + N('271.6') + '; MgSO₄: 106.0 + 160.0 = ' + N('266 S cm² mol⁻¹'))
steps_card(d, 'Example 2.8', 'Λ° of NaCl, HCl, NaAc = 126.4, 425.9, 91.0. Λ°(HAc)?', 'Add and subtract so only H⁺ and Ac⁻ remain.',
           ['Λ°(HAc) = Λ°(HCl) + Λ°(NaAc) − Λ°(NaCl)', '= 425.9 + 91.0 − 126.4', '= <b>390.5 S cm² mol⁻¹</b>'], 0, 'Kohlrausch: Λ° of acetic acid', '390.5 S cm²/mol')
d.basic('Degree of dissociation from conductivity?', r'\( \alpha = \frac{\Lambda_m}{\Lambda^{\circ}_m} \)' + ' and ' + r'\( K_a = \frac{c\alpha^2}{1 - \alpha} \)')
steps_card(d, 'Example 2.9', 'κ of 0.001028 M acetic acid = 4.95 × 10⁻⁵ S cm⁻¹; Λ° = 390.5. Ka?', 'Λm = 1000κ/c.',
           ['Λm = 4.95 × 10⁻⁵ × 1000/0.001028 = 48.15 S cm² mol⁻¹', 'α = 48.15/390.5 = 0.1233', 'Ka = cα²/(1 − α)', '= <b>1.78 × 10⁻⁵ mol L⁻¹</b>'], 1, 'Ka of acetic acid from conductivity', '1.78 × 10⁻⁵')
d.basic('α and Ka of 0.025 M HCOOH, Λm = 46.1 (λ° H⁺ 349.6, HCOO⁻ 54.6)? (Intext 2.9)', 'Λ° = 404.2; α = ' + N('0.114') + '; Ka = 0.025 × 0.114²/0.886 ≈ ' + N('3.67 × 10⁻⁴'))
d.basic('How to get Λ°m of water? (Intext 2.8)', 'λ°(H⁺) + λ°(OH⁻) = ' + N('548.7 S cm² mol⁻¹') + ' (or Λ°HCl + Λ°NaOH − Λ°NaCl)')

# ---------------------------------------------------------------- 2.5 Electrolysis
d.sec('2.5-electrolysis')
d.basic('Electrolysis of CuSO₄ with copper electrodes?', 'Cathode: Cu²⁺ + 2e⁻ → Cu (deposits). Anode: Cu → Cu²⁺ + 2e⁻ (dissolves).')
d.basic('Electrolytic refining of copper?', T('Impure Cu = anode') + ' (dissolves); ' + T('pure Cu deposits on the cathode'))
d.basic('Why are Na, Mg, Al made electrolytically? How?', 'No suitable chemical reducing agent. Na, Mg: ' + T('fused chlorides') + '; Al: ' + T('Al₂O₃ with cryolite'))
d.basic('Faraday’s first law?', 'Amount of reaction at an electrode ∝ ' + T('quantity of electricity') + ' passed (w = ZQ)')
d.basic('Faraday’s second law?', 'For the same charge, amounts liberated ∝ ' + T('equivalent weights') + ' (atomic mass ÷ electrons needed)')
d.basic('Charge passed by a current?', r'\( Q = I t \)' + ' (C = A × s)')
d.basic('What is 1 Faraday?', 'Charge on 1 mol electrons = ' + N('96487 ≈ 96500 C mol⁻¹'))
d.basic('Faradays to deposit 1 mol Ag, Mg, Al?', N('1F, 2F, 3F') + ' (electrons in the half-reaction)')
d.basic('Faradays per second at 50,000 A?', '≈ ' + N('0.518 F s⁻¹'))
steps_card(d, 'Example 2.10', 'CuSO₄ electrolysed 10 min at 1.5 A. Mass of Cu?', 'Cu²⁺ + 2e⁻ → Cu (63 g needs 2F).',
           ['Q = 1.5 × 600 = 900 C', 'mol e⁻ = 900/96487 = 0.00933', 'mol Cu = 0.00466', 'mass = 0.00466 × 63 = <b>0.2938 g</b>'], 1, 'Mass of Cu deposited', '0.294 g')
d.basic('Electrons through a wire at 0.5 A for 2 h? (Intext 2.10)', 'Q = 3600 C; n = 3600/1.602 × 10⁻¹⁹ = ' + N('2.25 × 10²²'))
d.basic('Charge to reduce 1 mol Cr₂O₇²⁻ to Cr³⁺? (Intext 2.12)', '6 mol e⁻ = 6F = ' + N('5.79 × 10⁵ C'))
d.basic('Trap: 1 mol electrons at the cathode deposits how many moles of H₂, Cu, Al?', N('½, ½, ⅓') + ' mol respectively')

d.sec('2.5.1-products-of-electrolysis')
d.basic('Products of electrolysis depend on?', 'Material electrolysed, ' + T('electrode type') + ' (inert vs reactive), competing E° values, and overpotential')
d.basic('What is overpotential?', 'Extra voltage needed because some feasible electrode reactions are ' + T('kinetically slow'))
d.basic('Products of electrolysis of molten NaCl?', T('Na') + ' at cathode, ' + T('Cl₂') + ' at anode')
d.basic('Products of electrolysis of aqueous NaCl?', T('H₂') + ' at cathode, ' + T('Cl₂') + ' at anode, ' + T('NaOH') + ' in solution')
d.basic('Why H₂ and not Na at the cathode (aq NaCl)?', 'Higher E° is reduced first: H⁺/H₂ ' + N('0.00 V') + ' ≫ Na⁺/Na ' + N('−2.71 V') + '; net H₂O + e⁻ → ½H₂ + OH⁻')
d.basic('Why Cl₂ and not O₂ at the anode (aq NaCl), though O₂ has lower E° (1.23 vs 1.36 V)?', 'Oxygen evolution has a high ' + T('overpotential') + ', so Cl⁻ is oxidised in practice')
d.basic('Rule of thumb for electrolysis products (intuition)?', 'Cathode: the species ' + T('easiest to reduce') + ' (highest E°). Anode: the species ' + T('easiest to oxidise') + ' (lowest E°), unless overpotential interferes.')
d.basic('Anode product for dilute vs concentrated H₂SO₄?', 'Dilute: ' + T('O₂') + ' (2H₂O → O₂ + 4H⁺ + 4e⁻, 1.23 V). Concentrated: ' + T('S₂O₈²⁻') + ' (peroxodisulphate, 1.96 V).')
d.basic('Trap: aqueous CuSO₄ with inert Pt electrodes gives?', T('Cu') + ' at cathode, ' + T('O₂') + ' at anode (solution turns acidic); with Cu electrodes the anode dissolves instead')

# ---------------------------------------------------------------- 2.6 Batteries
d.sec('2.6-batteries')
d.basic('What makes a battery practical?', 'Light, compact, and ' + T('voltage steady') + ' during use')
d.basic('Primary vs secondary battery?', T('Primary') + ': reaction occurs once, not rechargeable (dry cell). ' + T('Secondary') + ': rechargeable (lead storage, Ni–Cd).')
d.basic('Dry (Leclanché) cell: anode, cathode, electrolyte?', 'Anode: ' + T('Zn container') + '. Cathode: ' + T('graphite rod') + ' in MnO₂ + carbon. Electrolyte: moist paste of ' + T('NH₄Cl + ZnCl₂') + '.', **fig('fig_2_8_dry_cell'))
d.occlusion('Figure 2.8 · Dry cell', M + 'fig_2_8_dry_cell.webp', (566, 1001), [
    ('Carbon rod (cathode)', [70, 25, 250, 110], True), ('Zinc cup (anode)', [60, 840, 195, 110], True), ('MnO₂ + carbon black + NH₄Cl paste', [262, 845, 304, 156], True)])
d.basic('Dry cell electrode reactions and voltage?', 'Anode: Zn → Zn²⁺ + 2e⁻. Cathode: MnO₂ + NH₄⁺ + e⁻ → MnO(OH) + NH₃. About ' + N('1.5 V') + '.')
d.basic('Change in Mn oxidation state in a dry cell? Fate of NH₃?', T('+4 → +3') + '; NH₃ complexes Zn²⁺ as [Zn(NH₃)₄]²⁺')
d.basic('Mercury cell: electrodes, electrolyte, use?', 'Anode ' + T('Zn–Hg amalgam') + '; cathode ' + T('HgO + carbon paste') + '; electrolyte KOH + ZnO paste; hearing aids, watches', **fig('fig_2_9_mercury_cell'))
d.basic('Mercury cell overall reaction and voltage?', 'Zn(Hg) + HgO → ZnO + Hg; ' + N('1.35 V'))
d.basic('Why is the mercury cell voltage constant over its life?', 'No ' + T('ion in solution') + ' appears in the overall reaction, so no concentration term changes')
d.basic('Lead storage battery: anode, cathode, electrolyte?', 'Anode ' + T('Pb') + '; cathode ' + T('grid of Pb packed with PbO₂') + '; ' + N('38%') + ' H₂SO₄')
d.occlusion('Figure 2.10 · Lead storage battery', M + 'fig_2_10_lead_storage.webp', (1001, 682), [
    ('Anode', [65, 30, 120, 55], True), ('Cathode', [450, 35, 150, 55], True), ('Negative plates: lead grids filled with spongy lead', [720, 325, 281, 170], True),
    ('38% sulphuric acid solution', [65, 550, 240, 90], True), ('Positive plates: lead grids filled with PbO₂', [585, 535, 300, 130], True)])
d.cloze('Lead storage discharge: anode {{c1::Pb + SO₄²⁻ → PbSO₄ + 2e⁻}}; cathode {{c2::PbO₂ + SO₄²⁻ + 4H⁺ + 2e⁻ → PbSO₄ + 2H₂O}}.')
d.basic('Overall lead storage reaction (discharge)?', 'Pb + PbO₂ + 2H₂SO₄ → ' + T('2PbSO₄') + ' + 2H₂O')
d.basic('What happens on recharging a lead storage battery? (Intext 2.13)', 'Reaction reverses: PbSO₄ → ' + T('Pb at anode, PbO₂ at cathode') + '; H₂SO₄ regenerated')
d.basic('Why does acid density drop as a car battery discharges? (intuition)', 'H₂SO₄ is ' + X('used up') + ' and water formed; mechanics check charge with a hydrometer')
d.basic('Ni–Cd cell: vs lead storage, and overall reaction (NCERT)?', T('Longer life') + ', costlier; Cd + 2Ni(OH)₃ → CdO + 2Ni(OH)₂ + H₂O', **fig('fig_2_11_nicd'))
d.basic('Update: how is the Ni–Cd discharge usually written now?', 'Cd + 2NiO(OH) + 2H₂O → ' + T('Cd(OH)₂ + 2Ni(OH)₂') + ' (alkaline, KOH)')

# ---------------------------------------------------------------- 2.7 Fuel cells
d.sec('2.7-fuel-cells')
d.basic('What is a fuel cell?', 'Galvanic cell converting combustion energy of fuels (H₂, CH₄, CH₃OH) directly to electricity.<br>' + T('Reactants are fed continuously'))
d.basic('H₂–O₂ fuel cell: electrodes, electrolyte, catalyst?', 'Porous ' + T('carbon') + ' electrodes; concentrated ' + T('NaOH') + '; finely divided ' + T('Pt or Pd'), **fig('fig_2_12_fuel_cell'))
d.cloze('H₂–O₂ fuel cell: cathode {{c1::O₂ + 2H₂O + 4e⁻ → 4OH⁻}}; anode {{c2::2H₂ + 4OH⁻ → 4H₂O + 4e⁻}}; overall {{c3::2H₂ + O₂ → 2H₂O}}.')
d.basic('Where was the H₂–O₂ fuel cell used? Bonus?', 'Apollo space programme; the water was ' + T('drunk by astronauts'))
d.basic('Efficiency: fuel cell vs thermal plant?', 'Fuel cell ~' + N('70%') + '; thermal plant ~' + N('40%'))
d.basic('Intuition: why is a fuel cell more efficient than burning fuel?', 'It skips heat → steam → turbine; each conversion step wastes energy (heat engines are Carnot-limited)')
d.basic('Fuels other than H₂ in fuel cells? (Intext 2.14)', E('Methane, methanol'))
d.basic('Hydrogen economy (box)?', 'H₂ from ' + T('solar splitting of water') + ', burnt in fuel cells: product only water; both steps are electrochemical')

# ---------------------------------------------------------------- 2.8 Corrosion
d.sec('2.8-corrosion')
d.basic('Examples of corrosion?', 'Rusting of iron, ' + T('tarnishing of silver') + ', green coating on copper and bronze')
d.basic('Rusting as an electrochemical cell: anode and cathode reactions?', 'Anode spot: 2Fe → 2Fe²⁺ + 4e⁻ (' + N('−0.44 V') + '). Cathode spot: O₂ + 4H⁺ + 4e⁻ → 2H₂O (' + N('1.23 V') + ').', **fig('fig_2_13_corrosion'))
d.basic('E°cell for rusting?', '1.23 − (−0.44) = ' + N('1.67 V'))
d.basic('Source of H⁺ for rusting?', T('H₂CO₃') + ' from dissolved CO₂ (and other acidic oxides)')
d.basic('Composition of rust?', 'Hydrated ferric oxide, ' + T('Fe₂O₃·xH₂O') + ' (Fe²⁺ oxidised further by air)')
d.basic('Intuition: why does rust form away from where the metal is eaten?', 'One drop is a ' + T('mini galvanic cell') + '.<br>Electrons travel through the iron from the anodic pit to a cathodic spot where O₂ is abundant')
d.basic('Why does salt water (sea air) speed up rusting?', 'Dissolved ions make the water a better ' + T('electrolyte') + ', completing the mini cell')
d.basic('Ways to prevent corrosion?', 'Barrier: ' + T('paint') + ', chemicals (bisphenol), coating with Sn/Zn. Electrochemical: ' + T('sacrificial electrode') + ' of Mg or Zn.')
d.basic('How does a sacrificial anode work?', 'A more reactive metal (' + E('Mg, Zn') + ', lower E°) is oxidised instead of iron, pushing electrons into the iron')
d.basic('Galvanised (Zn) vs tin-plated iron when scratched? (teacher trap)', 'Zinc still protects (Zn is more reactive). ' + X('Tin makes it worse') + ': Fe becomes the anode next to Sn.')

# ---------------------------------------------------------------- summary
d.sec('summary')
table_card(d, 'Summary', 'Formula?', [
    ('Cell emf', 'E°cell = E°cathode − E°anode', False), ('Nernst (298 K)', 'E = E° − (0.059/n) log Q', False),
    ('Gibbs energy', 'ΔG° = −nFE°', False), ('Equilibrium', 'log K = nE°/0.059', False),
    ('Conductivity', 'κ = G*/R', False), ('Molar conductivity', 'Λm = 1000κ/M', False), ('Faraday', 'm = (M/nF)·It', False)], term='Electrochemistry formula sheet')
table_card(d, 'Summary', 'Anode / cathode / electrolyte?', [
    ('Dry cell', 'Zn / graphite + MnO₂ / NH₄Cl + ZnCl₂', False), ('Mercury cell', 'Zn–Hg / HgO + C / KOH + ZnO', False),
    ('Lead storage', 'Pb / PbO₂ / 38% H₂SO₄', False), ('H₂–O₂ fuel cell', 'H₂ on C / O₂ on C / conc. NaOH', False)], term='Cells and batteries at a glance')

n = d.write(os.path.join(OUT, 'deck.json'))
print(n, 'cards')
