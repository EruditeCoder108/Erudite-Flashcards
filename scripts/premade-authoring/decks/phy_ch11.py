import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Physics', 'class11-physics-ch11-thermodynamics')
d = Deck('Chapter 11: Thermodynamics', 'Class 11', ['class-11', 'physics', 'ch-11'])
d.description = 'Zeroth law, internal energy, heat and work, first law, Cp − Cv, state variables, isothermal and adiabatic processes, second law, Carnot engine'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- 11.1 Introduction
d.sec('11.1-introduction')
d.basic('What was the caloric theory of heat?', 'Heat as an invisible ' + X('fluid') + ' ("caloric") filling the pores of matter, flowing until "caloric levels" equalised')
d.basic('How did Count Rumford (1798) disprove caloric theory?', 'Boring a cannon produced heat that depended on the ' + T('work done') + ' (by horses), not on the drill’s sharpness → heat is a form of ' + T('energy'))
d.basic('Thermodynamics vs mechanics?', 'Mechanics: motion of the body as a whole. Thermodynamics: the ' + T('internal macroscopic state') + ' (P, V, T, U) — a bullet is not hotter because it is fast')
d.basic('Is thermodynamics a microscopic or macroscopic science?', T('Macroscopic') + ': it uses bulk variables (P, V, T, mass, composition) and ignores molecules')

# ---------------------------------------------------------------- 11.2-11.3 Equilibrium, zeroth law
d.sec('11.2-thermal-equilibrium')
d.basic('Thermodynamic equilibrium vs mechanical equilibrium?', 'Thermodynamic: macroscopic variables ' + T('do not change with time') + '. Mechanical: net force and torque are zero')
d.basic('Adiabatic wall vs diathermic wall?', T('Adiabatic') + ': insulating, no heat flow. ' + T('Diathermic') + ': conducting, heat flows until thermal equilibrium', **fig('fig_11_1_walls'))
d.cloze('Zeroth law: two systems in thermal equilibrium with a {{c1::third system}} separately are in thermal equilibrium with {{c2::each other}}.')
d.basic('What concept does the zeroth law define?', T('Temperature') + ': the quantity that is equal for systems in thermal equilibrium', **fig('fig_11_2_zeroth_law'))
d.basic('Who formulated the zeroth law, and why is it called "zeroth"?', T('R. H. Fowler') + ' (1931), after the first and second laws were already numbered; it is logically more basic')

# ---------------------------------------------------------------- 11.4 Heat, internal energy, work
d.sec('11.4-heat-internal-energy-work')
d.basic('Define internal energy.', 'Sum of molecular ' + T('kinetic and potential energies') + ' in the frame where the centre of mass is at rest; excludes KE of the body as a whole', **fig('fig_11_3_internal_energy'))
d.basic('Is internal energy a state variable? Heat? Work?', 'U: ' + T('yes') + ' (depends only on the state). Heat and work: ' + X('no') + ' — they are energy in transit and depend on the path')
d.basic('Heat vs work as ways to change U?', T('Heat') + ': transfer due to a temperature difference. ' + T('Work') + ': transfer by other means (e.g. moving a piston)', **fig('fig_11_4_heat_work'))
d.basic('Why is "a gas has a certain amount of heat" meaningless?', 'Heat is energy ' + T('in transit') + ', not a property of a state; the state has internal energy')
d.basic('For an ideal gas, U depends on…?', T('Temperature only') + ' (no intermolecular forces)')

# ---------------------------------------------------------------- 11.5 First law
d.sec('11.5-first-law')
d.basic('State the first law of thermodynamics.', r'\( \Delta Q = \Delta U + \Delta W \)' + ': heat supplied = rise in internal energy + work done ' + T('by') + ' the system')
table_card(d, 'Sign convention (NCERT)', 'Sign?', [
    ('Heat absorbed by the system', 'ΔQ > 0', False), ('Heat released', 'ΔQ < 0', True),
    ('Work done by the system (expansion)', 'ΔW > 0', False), ('Work done on the system (compression)', 'ΔW < 0', True)],
    note='Chemistry books often write ΔU = q + w with w = work done ON the system — same physics, different sign.', term='First law sign conventions')
d.basic('The first law is really the law of…?', 'Conservation of ' + T('energy') + ', including heat and work exchanges')
d.basic('Which combination of Q and W is path independent?', r'\( \Delta Q - \Delta W = \Delta U \)' + ', because U is a state variable (Q and W separately depend on the path)')
d.basic('Work done by a gas against constant pressure?', r'\( \Delta W = P\,\Delta V \)' + '; in general, W = ∫P dV = area under the P–V curve')
steps_card(d, '11.5 · boiling 1 g of water', 'Find the missing step.', 'L = 2256 J/g; 1 g of water: 1 cm³ as liquid, 1671 cm³ as steam, at 1 atm. ΔU?',
           ['ΔQ = 2256 J', 'ΔW = P(V_g − V_l) = 1.013 × 10⁵ × 1670 × 10⁻⁶ ≈ 169 J', 'ΔU = ΔQ − ΔW', '= <b>≈ 2087 J</b>: most heat goes into internal energy'], 2,
           'Internal energy change on boiling water', 'ΔU = 2256 − 169 ≈ 2087 J')
d.basic('Exercise 11.7: heater supplies 100 W; system does work at 75 J/s. Rate of rise of U?', N('25 W'))
d.basic('Exercise 11.5: A → B adiabatically needs 22.3 J of work on the gas. Via another path the gas absorbs 9.35 cal. Work done by the gas then?', 'ΔU = +22.3 J (same for any path); W = Q − ΔU = 39.2 − 22.3 = ' + N('16.9 J'))

# ---------------------------------------------------------------- 11.6 Specific heat
d.sec('11.6-specific-heat-capacity')
d.basic('Molar specific heat of solids (Dulong–Petit)?', r'\( C \approx 3R \approx 25\ \text{J mol}^{-1}\text{K}^{-1} \)'.replace(r'\ \text{J mol}^{-1}\text{K}^{-1}', '') + ' J mol⁻¹ K⁻¹: each atom is a 3D oscillator with energy 3kT', **fig('tab_11_1_solids_heat'))
d.basic('Which solid in Table 11.1 breaks the 3R rule?', E('Carbon') + ' (6.1 J mol⁻¹ K⁻¹); the rule also fails at low temperatures')
d.basic('Define the calorie precisely. 1 cal in joules?', 'Heat to raise 1 g of water from ' + T('14.5 °C to 15.5 °C') + '; 1 cal = ' + N('4.186 J'), **fig('fig_11_5_water_specific_heat'))
d.basic('Why is "mechanical equivalent of heat" now superfluous?', 'Heat and work are both energy measured in ' + T('joules') + '; 4.186 J/cal is only a unit conversion')
d.basic('Mayer’s relation for an ideal gas?', r'\( C_p - C_v = R \)')
steps_card(d, '11.6 · proof of Cp − Cv = R', 'Find the missing step.', 'Prove Cp − Cv = R for one mole of an ideal gas.',
           ['ΔQ = ΔU + PΔV', 'Constant V: Cv = ΔU/ΔT', 'Constant P: Cp = ΔU/ΔT + P(ΔV/ΔT); PV = RT gives P ΔV/ΔT = R', 'So <b>Cp − Cv = R</b>'], 2,
           'Proof of Mayer’s relation', 'At constant P the extra heat does work PΔV = RΔT per mole, so Cp − Cv = R')
d.basic('Why is Cp > Cv?', 'At constant pressure part of the heat does ' + T('work') + ' (expansion); at constant volume all of it raises U')
d.basic('Exercise 11.2: heat to raise 20 g of nitrogen by 45 °C at constant pressure?', 'μ = 20/28 mol, Cp = 7R/2 → Q ≈ ' + N('933 J'))
d.basic('Exercise 11.3(a): why don’t two bodies in contact settle at (T₁ + T₂)/2?', 'Only if their ' + T('heat capacities') + ' are equal; in general the final temperature is weighted by ms')
d.basic('Exercise 11.3(b): why should a coolant have high specific heat?', 'It absorbs a lot of heat with only a small ' + T('rise in its temperature'))
d.basic('Exercise 11.3(d): why is a harbour town’s climate milder than a desert town’s?', 'The sea’s high heat capacity (and humid air) smooths temperature changes')

# ---------------------------------------------------------------- 11.7 State variables
d.sec('11.7-state-variables')
d.basic('What is an equation of state? Example?', 'A relation among state variables; for an ideal gas ' + r'\( PV = \mu RT \)' + ' (only two of P, V, T independent)')
d.basic('Can a gas in free expansion or an explosion be described by state variables?', X('No') + ': it is not in equilibrium; P and T are not uniform', **fig('fig_11_6_non_equilibrium'))
d.basic('Extensive vs intensive variables? Test?', 'Divide the system in two: variables that ' + T('halve') + ' are extensive (U, V, mass); those ' + T('unchanged') + ' are intensive (P, T, ρ)')
d.basic('Is ΔQ = ΔU + PΔV consistent in extensive/intensive terms?', T('Yes') + ': every term is extensive (P × ΔV is intensive × extensive)')
d.basic('What is an isotherm?', 'The P–V curve at fixed temperature')

# ---------------------------------------------------------------- 11.8 Processes
d.sec('11.8-thermodynamic-processes')
d.basic('What is a quasi-static process?', 'An ' + T('infinitely slow') + ' process: the system stays in equilibrium, differing from the surroundings only infinitesimally in P and T', **fig('fig_11_7_quasi_static'))
table_card(d, 'Table 11.2', 'What is kept fixed?', [
    ('Isothermal', 'temperature', False), ('Isobaric', 'pressure', False), ('Isochoric', 'volume', False), ('Adiabatic', 'no heat flow (ΔQ = 0)', False)],
    term='Special thermodynamic processes (Table 11.2)')
d.basic('Identify the four processes starting from A on this P–V diagram.', 'Horizontal: isobaric; vertical: isochoric; PV = const: isothermal; steeper PVᵞ = const: adiabatic', **img('drawn_pv_processes'))
d.basic('Isothermal process of an ideal gas: relation, ΔU, work?', 'PV = constant (Boyle); ΔU = 0; ' + r'\( Q = W = \mu RT\ln\dfrac{V_2}{V_1} \)')
d.basic('Isothermal expansion vs compression: heat?', 'Expansion: gas ' + T('absorbs') + ' heat and does work. Compression: work is done on it and it ' + T('releases') + ' heat')
d.basic('Adiabatic process of an ideal gas: relation?', r'\( PV^\gamma = \text{const} \)'.replace(r'\text{const}', 'constant') + ', γ = Cp/Cv; also ' + r'\( TV^{\gamma-1} = \text{const} \)'.replace(r'\text{const}', 'constant'))
d.basic('Work done by an ideal gas in an adiabatic change?', r'\( W = \dfrac{P_1V_1 - P_2V_2}{\gamma - 1} = \dfrac{\mu R(T_1 - T_2)}{\gamma - 1} \)')
d.basic('Adiabatic expansion: what happens to temperature? Compression?', 'Expansion: work comes from U → gas ' + T('cools') + '. Compression: gas ' + T('heats up') + ' (e.g. a bicycle pump)')
d.basic('Why is an adiabat steeper than an isotherm on a P–V graph?', 'Slope: isotherm −P/V, adiabat ' + T('−γP/V') + ' (γ > 1)', **fig('fig_11_8_isotherm_adiabat'))
d.basic('Isochoric process?', 'W = 0; all heat changes U: ' + r'\( Q = \mu C_v\Delta T \)')
d.basic('Isobaric process?', r'\( W = P(V_2 - V_1) = \mu R(T_2 - T_1) \)' + '; Q = μCₚΔT')
d.basic('Cyclic process?', 'ΔU = 0, so ' + T('net heat absorbed = net work done') + ' = area enclosed by the loop')
d.basic('Exercise 11.4: 3 mol of H₂ compressed adiabatically to half its volume. Pressure factor?', r'\( 2^{1.4} \approx \)' + ' ' + N('2.64'))
d.basic('Exercise 11.6: gas in A expands freely into evacuated B (equal volumes, insulated). Final P, ΔU, ΔT?', 'P halves (' + N('0.5 atm') + '); ΔU = ' + N('0') + ', ΔT = ' + N('0') + ' (ideal gas: Q = 0, W = 0)')
d.basic('Exercise 11.6(d): do the intermediate states of free expansion lie on the P–V–T surface?', X('No') + ': free expansion is rapid; intermediate states are not equilibrium states')
d.basic('Exercise 11.3(c): why does tyre pressure rise while driving?', 'Friction heats the tyre air at nearly ' + T('constant volume') + ', so P rises')
d.basic('Exercise 11.8: gas goes D → E linearly (600 → 300 N/m², 2 → 5 m³), then isobarically back E → F. Total work?', 'Area of triangle DEF = ½ × 3 × 300 = ' + N('450 J'), **fig('fig_11_11_ex_pv'))
d.basic('Correction: NCERT Exercise 11.8 refers to "Fig. (11.13)". Which figure?', T('Fig. 11.11'))

# ---------------------------------------------------------------- 11.9-11.10 Second law, reversibility
d.sec('11.9-second-law')
d.basic('Why is the first law not enough?', 'Many energy-conserving events never happen (a book jumping up by cooling the table); the ' + T('second law') + ' forbids them')
d.cloze('Kelvin–Planck statement: no process is possible whose sole result is the absorption of heat from a reservoir and its {{c1::complete conversion into work}}.')
d.cloze('Clausius statement: no process is possible whose sole result is the transfer of heat from a {{c1::colder}} object to a {{c2::hotter}} object.')
d.basic('What do the two statements rule out?', 'A heat engine with efficiency ' + X('1') + ' and a refrigerator with infinite coefficient of performance; the statements are equivalent')
d.basic('Teacher addition: efficiency of a heat engine?', r'\( \eta = \dfrac{W}{Q_1} = 1 - \dfrac{Q_2}{Q_1} \)', **fig('drawn_engine_fridge'))
d.basic('Teacher addition: coefficient of performance of a refrigerator?', r'\( \beta = \dfrac{Q_2}{W} = \dfrac{Q_2}{Q_1 - Q_2} \)' + '; for a Carnot fridge ' + r'\( \dfrac{T_2}{T_1 - T_2} \)', **fig('drawn_engine_fridge'))

d.sec('11.10-reversible-irreversible')
d.basic('Define a reversible process.', 'One that can be turned back so that ' + T('both system and surroundings') + ' return to their original states, with no change elsewhere')
d.basic('Conditions for reversibility?', T('Quasi-static') + ' and ' + T('no dissipative effects') + ' (friction, viscosity)')
d.basic('Two main causes of irreversibility?', 'Passing through ' + X('non-equilibrium states') + ' (free expansion, explosions) and ' + X('dissipation') + ' (friction, viscosity)')
d.basic('Examples of irreversible processes?', 'Heat flowing from a hot base to the rest of a vessel, free expansion, combustion, diffusion of leaking gas, stirring a liquid')
d.basic('Example of a (nearly) reversible process?', 'Quasi-static isothermal expansion of an ideal gas with a ' + T('frictionless piston'))

# ---------------------------------------------------------------- 11.11 Carnot
d.sec('11.11-carnot-engine')
d.basic('Why must a reversible engine between two temperatures use isothermal and adiabatic steps?', 'Heat must be exchanged with no finite temperature difference (' + T('isothermal') + '), and temperature changed without other reservoirs (' + T('adiabatic') + ')')
d.cloze('Carnot cycle: {{c1::isothermal expansion}} at T₁ → {{c2::adiabatic expansion}} to T₂ → {{c3::isothermal compression}} at T₂ → {{c4::adiabatic compression}} back to T₁.')
d.basic('Identify: which parts of the Carnot cycle absorb and reject heat?', '1 → 2 (isothermal at T₁) absorbs Q₁; 3 → 4 (isothermal at T₂) rejects Q₂; the two adiabats exchange no heat', **img('fig_11_9_carnot'))
d.basic('Efficiency of a Carnot engine?', r'\( \eta = 1 - \dfrac{T_2}{T_1} \)' + ' (kelvin temperatures)')
d.basic('Key relation in a Carnot cycle (used to define temperature)?', r'\( \dfrac{Q_1}{Q_2} = \dfrac{T_1}{T_2} \)' + ' — independent of the working substance')
d.basic('State Carnot’s theorem.', '(a) No engine between T₁ and T₂ is more efficient than a ' + T('Carnot') + ' engine. (b) Carnot efficiency is ' + T('independent of the working substance'))
d.basic('How is Carnot’s theorem proved?', 'If an engine I beat a reversible engine R run as a refrigerator, the pair would turn heat from one reservoir fully into work, violating ' + T('Kelvin–Planck'), **fig('fig_11_10_engine_refrigerator'))
d.basic('Who first analysed the ideal heat engine?', T('Sadi Carnot') + ', French engineer, 1824')
d.basic('Teacher addition: Carnot engine between 500 K and 300 K. Efficiency?', '1 − 300/500 = ' + N('40 %'))
d.basic('Can a Carnot engine have 100 % efficiency?', 'Only if T₂ = ' + X('0 K') + ', which is unattainable')

# ---------------------------------------------------------------- Summary
d.sec('summary')
table_card(d, 'Summary · ideal gas processes', 'W done by the gas?', [
    ('Isochoric', '0', False), ('Isobaric', 'P(V₂ − V₁)', False), ('Isothermal', 'μRT ln(V₂/V₁)', False),
    ('Adiabatic', '(P₁V₁ − P₂V₂)/(γ − 1)', False), ('Cyclic', 'area of the loop', False)], term='Work in thermodynamic processes')
table_card(d, 'Points to ponder', 'True or false?', [
    ('A fast bullet is hotter because of its speed', 'False', True),
    ('In thermodynamic equilibrium, molecules are at rest', 'False', True),
    ('Heat capacity depends on the process', 'True', False),
    ('An isothermal process exchanges heat though T never changes', 'True (tiny ΔT with the reservoir)', False)], term='Chapter 11 concept checks')
d.basic('Correction: NCERT’s summary table gives thermal conductivity in J s⁻¹ K⁻¹. What is right?', T('J s⁻¹ m⁻¹ K⁻¹') + ' (W m⁻¹ K⁻¹): H = KA ΔT/L needs a per-metre unit')

print(d.write(os.path.join(OUT, 'deck.json')), 'cards')
