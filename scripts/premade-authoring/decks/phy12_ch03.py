import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Physics', 'class12-physics-ch03-current-electricity')
d = Deck('Chapter 3: Current Electricity', 'Class 12', ['class-12', 'physics', 'ch-3'])
d.description = 'Current, Ohm’s law, drift velocity, mobility, resistivity and temperature, power, emf and internal resistance, cells, Kirchhoff’s rules, Wheatstone bridge'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- 3.1–3.3 Current
d.sec('3.2-electric-current')
d.basic('Define electric current (steady and instantaneous).', 'Net charge crossing an area per unit time: I = q/t; in general ' + r'\( I = \lim_{\Delta t\to0}\dfrac{\Delta Q}{\Delta t} \)')
d.basic('Net charge q crossing an area when both + and − charges move?', 'q = q₊ − q₋ (forward flow of + minus forward flow of −); a negative I means current in the backward direction')
d.basic('Orders of magnitude: lightning, domestic appliances, nerves?', 'Lightning: ' + N('tens of thousands of A') + '; appliances: ' + N('~1 A') + '; nerves: ' + N('μA'))
d.basic('Is current a scalar or a vector?', T('Scalar') + ' (the arrow only shows sense of flow; currents don’t add as vectors). ' + r'\( I = \vec j\cdot\Delta\vec S \)')
d.basic('Name natural free charges and the charge carriers in solids and electrolytes.', 'Free: ' + E('ionosphere') + '. Solid conductors: ' + T('electrons') + ' (ions fixed). Electrolytes: ' + T('positive and negative ions'))

d.sec('3.3-currents-in-conductors')
d.basic('With no field, why is there no current even though electrons move fast?', 'Thermal motion is ' + T('random') + ': as many electrons cross each way, so the net flow is zero')
d.basic('Charges ±Q stuck on the ends of a metal cylinder: what current flows?', 'Only a ' + T('brief') + ' current until the charges are neutralised; a cell must ' + T('replenish') + ' them to keep a steady field and current', **fig('fig_3_1_cylinder'))

# ---------------------------------------------------------------- 3.4 Ohm's law
d.sec('3.4-ohms-law')
d.basic('State Ohm’s law. Who, when?', r'\( V \propto I \)' + ', V = RI (at constant physical conditions); ' + T('G. S. Ohm') + ', ' + N('1828'))
d.basic('What analogy led Ohm to his law?', T('Heat conduction') + ': electric field ↔ temperature gradient, current ↔ heat flow')
d.basic('Resistance: unit and dimensions?', 'ohm, 1 Ω = 1 V A⁻¹; [ML²T⁻³A⁻²]')
d.basic('How does R depend on length and area? Show why.', r'\( R = \rho\dfrac{l}{A} \)' + ': two slabs end to end double V at the same I (R ∝ l); cut lengthwise, each half carries I/2 at the same V (R ∝ 1/A)', **fig('fig_3_2_slabs'))
d.basic('What is resistivity? Unit and dimensions?', 'Material constant ρ in R = ρl/A (depends on material and temperature, not size); Ω m, [ML³T⁻³A⁻²]')
d.basic('Define current density. Unit?', r'\( j = I/A \)' + ' (area normal to the current), a vector along E; A m⁻²')
d.basic('Ohm’s law in terms of E and j?', r'\( \vec E = \rho\,\vec j \)' + ' or ' + r'\( \vec j = \sigma\vec E \)' + ', with conductivity σ = 1/ρ')
d.basic('Correction: NCERT’s table gives the unit of conductivity σ as “S”. Right unit?', T('S m⁻¹') + ' (siemens per metre) — the dimensions it lists, [M⁻¹L⁻³T³A²], are those of S m⁻¹; S alone is the unit of conductance (1/R)')
d.basic('Points to ponder: is V = IR itself Ohm’s law?', X('No') + ': V = IR ' + T('defines') + ' R for any device. Ohm’s law is the claim that R is ' + T('independent of V') + ' (I–V plot linear)')
d.basic('Stretching trap: a wire is stretched to n times its length (volume constant). New R?', N('n²R') + ': l → nl and A → A/n')

# ---------------------------------------------------------------- 3.5 Drift
d.sec('3.5-drift-of-electrons')
d.basic('Acceleration of a free electron in a field E?', r'\( \vec a = -\dfrac{e\vec E}{m} \)')
d.basic('Define relaxation time τ.', 'Average time between ' + T('successive collisions') + ' of an electron')
d.basic('Drift velocity formula?', r'\( \vec v_d = -\dfrac{e\vec E}{m}\tau \)' + ' — opposite to E for electrons')
d.basic('Electrons accelerate, so why a constant drift velocity?', 'Each collision ' + T('randomises') + ' the velocity; between collisions the gain is eEt/m, averaging to eEτ/m — like a ball bouncing down a pin-board')
d.basic('Relation between current and drift speed?', r'\( I = neAv_d \)' + ' (charge in a cylinder of length v_d Δt crossing A per Δt)', **fig('fig_3_4_current_cylinder'))
d.basic('Identify: what does this path show?', 'Random zig-zag of an electron between collisions (A → B); with a field it ends at ' + T('B′') + ' — a slight ' + T('drift opposite to E'), **img('fig_3_3_drift_path'))
d.basic('Derive conductivity from the drift model.', r'\( j = \dfrac{ne^2\tau}{m}E \Rightarrow \sigma = \dfrac{ne^2\tau}{m},\ \rho = \dfrac{m}{ne^2\tau} \)' + ' — Ohm’s law, if n and τ don’t depend on E')
steps_card(d, 'Example 3.1 · drift speed in copper', 'Find the missing step.', 'Cu wire, A = 1.0 × 10⁻⁷ m², I = 1.5 A, ρ(density) = 9.0 × 10³ kg/m³, 63.5 u, one free electron per atom. v_d?',
           ['n = (9.0 × 10⁶ g/m³ ÷ 63.5 g) × 6.0 × 10²³ = <b>8.5 × 10²⁸ m⁻³</b>', 'v<sub>d</sub> = I/(neA)',
            'v<sub>d</sub> = 1.5/(8.5 × 10²⁸ × 1.6 × 10⁻¹⁹ × 10⁻⁷) = <b>1.1 mm/s</b>'], 1,
           'Drift speed of electrons in copper (Example 3.1)', 'n = 8.5 × 10²⁸ m⁻³; v_d = I/neA ≈ 1.1 × 10⁻³ m/s')
d.basic('Example 3.1(b): drift speed vs thermal speed of Cu atoms vs speed of the field signal?', 'v_d ~ 10⁻³ m/s; thermal speed of Cu atoms ~ ' + N('2 × 10² m/s') + ' (~10⁵ times more); field travels at ' + N('3 × 10⁸ m/s') + ' (~10¹¹ times more)')
d.basic('Update: how fast do the conduction electrons themselves move at random?', 'About ' + N('10⁶ m/s') + ' (the Fermi speed, a quantum effect) — so v_d is ~10⁻⁹ of their random speed; NCERT compares with atoms’ thermal speed instead')
d.basic('Example 3.2(a): drift is only mm/s. Why does a bulb light instantly?', 'The ' + T('electric field') + ' is set up in the whole circuit at nearly the speed of light; electrons everywhere start drifting at once')
d.basic('Example 3.2(c): tiny drift, tiny charge — how are currents large?', 'The ' + T('number density') + ' of free electrons is enormous, ~' + N('10²⁹ m⁻³'))
d.basic('Example 3.2(d): do all free electrons move in the same direction?', X('No') + ': the small drift is ' + T('superposed') + ' on large random velocities')
d.basic('Example 3.2(e): are electron paths straight between collisions?', 'Without a field: ' + T('straight') + '. With a field: ' + T('curved') + ' (parabolic), like projectiles')
d.basic('Exercise 3.9: n = 8.5 × 10²⁸ m⁻³, A = 2.0 × 10⁻⁶ m², I = 3.0 A. Time to drift along 3.0 m?', 'v_d ≈ 1.1 × 10⁻⁴ m/s → t ≈ ' + N('2.7 × 10⁴ s') + ' (~7.5 h)')

d.sec('3.5.1-mobility')
d.basic('Define mobility. Unit?', r'\( \mu = \dfrac{|v_d|}{E} = \dfrac{e\tau}{m} \)' + '; m² V⁻¹ s⁻¹ (1 m²/Vs = 10⁴ cm²/Vs); always positive')
d.basic('Dimensions of mobility?', '[M⁻¹ T² A]')
d.basic('Mobile charge carriers in metals, ionised gases, electrolytes?', 'Metals: ' + T('electrons') + '; ionised gas: ' + T('electrons and positive ions') + '; electrolytes: ' + T('positive and negative ions'))
d.basic('Teacher addition: conductivity in terms of mobility?', r'\( \sigma = ne\mu \)')

# ---------------------------------------------------------------- 3.6 Limitations
d.sec('3.6-limitations-of-ohms-law')
d.basic('Three kinds of deviation from Ohm’s law?', '(a) V not ∝ I (' + E('good conductor at large I') + '); (b) depends on the ' + T('sign of V') + ' (' + E('diode') + '); (c) ' + T('non-unique') + ' V for the same I (' + E('GaAs') + ')')
d.basic('Identify: what does this V–I graph show?', 'A ' + T('good conductor') + ' deviating from the straight Ohm’s-law line (dashed) at large current', **img('fig_3_5_ohmic'))
d.basic('Identify: which device has this I–V curve? Note the axes.', 'A ' + T('diode') + ': current depends on the sign of V; note different scales (mA/V forward, μA/V reverse)', **img('fig_3_6_diode'))
d.basic('Identify: which material shows this I–V curve?', T('GaAs') + ': a negative-resistance region, so one I can occur at more than one V', **img('fig_3_7_gaas'))
d.basic('Points to ponder: do silver or germanium obey Ohm’s law always?', 'Only within some range of field; ' + X('all materials deviate') + ' in very strong fields')

# ---------------------------------------------------------------- 3.7–3.8 Resistivity
d.sec('3.7-resistivity-of-materials')
d.basic('Resistivity range of metals? Insulators?', 'Metals: ' + N('10⁻⁸ to 10⁻⁶ Ω m') + '. Insulators (ceramic, rubber, plastic): ' + N('≥10¹⁸ times') + ' larger')
d.basic('Note: NCERT’s summary says insulators are 10²² to 10²⁴ times more resistive; the text says 10¹⁸ or more. Which is right?', 'Both are rough: real insulators span ~' + N('10¹⁸–10²⁴') + ' times metals (glass lower, hard rubber higher). Remember “metals 10⁻⁸, insulators ~10¹⁰ and up”')
d.basic('Two special features of semiconductors’ resistivity?', 'It ' + T('decreases with temperature') + ', and falls sharply on adding small amounts of suitable ' + T('impurities') + ' (doping)')

d.sec('3.8-temperature-dependence-of-resistivity')
d.basic('Resistivity of a metal vs temperature (limited range)?', r'\( \rho_T = \rho_0[1 + \alpha(T - T_0)] \)' + '; α > 0 for metals, unit K⁻¹ (or °C⁻¹)')
d.basic('Define the temperature coefficient of resistivity α.', 'The ' + T('fractional increase in resistivity per unit rise') + ' in temperature')
d.basic('Identify: whose resistivity–temperature graph is this?', T('Copper') + ': roughly linear near room temperature, curving away at low T', **img('fig_3_8_copper'))
d.basic('Identify: whose resistivity–temperature graph is this? Why useful?', T('Nichrome') + ': very weak dependence (also manganin, constantan) → used in ' + T('standard resistors'), **img('fig_3_9_nichrome'))
d.basic('Identify: what kind of material has this ρ–T graph?', 'A ' + T('semiconductor') + ': ρ falls steeply as T rises', **img('fig_3_10_semiconductor'))
d.basic('Why does a metal’s resistivity rise with temperature?', 'n is almost constant, but faster random motion means more frequent collisions: ' + T('τ decreases') + ' → ρ = m/ne²τ rises')
d.basic('Why does a semiconductor’s resistivity fall with temperature?', T('n increases') + ' sharply with T, more than offsetting the fall in τ')
d.basic('Nichrome is an alloy of which metals?', T('Nickel and chromium') + ' (NCERT adds iron, present in some grades)')
steps_card(d, 'Example 3.3 · toaster', 'Find the missing step.', 'Nichrome element: 75.3 Ω at 27.0 °C; on 230 V the current settles at 2.68 A. α = 1.70 × 10⁻⁴ °C⁻¹. Steady temperature?',
           ['Hot resistance R₂ = 230/2.68 = <b>85.8 Ω</b>', 'R₂ = R₁[1 + α(T₂ − T₁)]',
            'T₂ − T₁ = (85.8 − 75.3)/(75.3 × 1.70 × 10⁻⁴) = 820 °C', 'T₂ = <b>847 °C</b>'], 2,
           'Heating element temperature from resistance (Example 3.3)', 'R₂ = 85.8 Ω; ΔT = 820 °C; T₂ = 847 °C')
d.basic('Example 3.4: Pt thermometer reads 5 Ω at 0 °C, 5.23 Ω at 100 °C, 5.795 Ω in a bath. Bath temperature?', 't = (5.795 − 5)/(5.23 − 5) × 100 = ' + N('345.65 °C'))
d.basic('Exercise 3.3: 100 Ω at 27 °C becomes 117 Ω; α = 1.70 × 10⁻⁴ °C⁻¹. Temperature?', 'ΔT = 0.17/1.7 × 10⁻⁴ = 1000 °C → ' + N('1027 °C'))
d.basic('Exercise 3.5: silver wire 2.1 Ω at 27.5 °C, 2.7 Ω at 100 °C. α?', '0.6/(2.1 × 72.5) ≈ ' + N('0.0039 °C⁻¹'))
d.basic('Exercise 3.6: nichrome on 230 V draws 3.2 A initially, 2.8 A steady; room 27 °C. Steady temperature?', 'R = 71.9 Ω → 82.1 Ω; ΔT ≈ 840 °C → ' + N('≈ 867 °C'))
d.basic('Exercise 3.4: 15 m wire, A = 6.0 × 10⁻⁷ m², R = 5.0 Ω. Resistivity?', 'ρ = RA/l = ' + N('2.0 × 10⁻⁷ Ω m'))

# ---------------------------------------------------------------- 3.9 Power
d.sec('3.9-electrical-energy-power')
d.basic('Charge ΔQ falls through V: where does the lost potential energy go in a real conductor?', 'Not into KE (drift is steady) but into ' + T('heat') + ': collisions pass it to the ions, which vibrate more')
d.basic('Power dissipated in a resistor?', r'\( P = IV = I^2R = \dfrac{V^2}{R} \)' + ' (ohmic loss)')
d.basic('Who supplies the power in a simple cell–resistor circuit?', 'The ' + T('chemical energy') + ' of the cell', **fig('fig_3_11_cell_resistor'))
d.basic('Why is power transmitted at very high voltage?', 'Line loss ' + r'\( P_c = \dfrac{P^2R_c}{V^2} \)' + ' ∝ 1/V²: high V means small I and small loss; a ' + T('transformer') + ' steps it down for use')
d.basic('Series or parallel: which bulb glows brighter, 100 W or 60 W (both 220 V)?', 'Parallel: ' + T('100 W') + ' (P = V²/R, smaller R). Series: ' + T('60 W') + ' (same I, P = I²R, larger R)')

# ---------------------------------------------------------------- 3.10 EMF
d.sec('3.10-cells-emf-internal-resistance')
d.basic('Define emf of a cell (in terms of electrode potentials).', 'ε = V₊ + V₋: potential difference between the terminals on ' + T('open circuit') + ' (no current)', **fig('fig_3_12_cell'))
d.basic('Summary definition of emf (work).', 'Work done per unit charge by the source in taking charge from ' + T('lower to higher potential energy') + ' inside it')
d.basic('Is emf a force?', X('No') + ': it is a potential difference; the name is historical')
d.basic('Terminal voltage when the cell delivers current I?', r'\( V = \varepsilon - Ir \)' + ' (r = internal resistance)')
d.basic('Current from a cell into an external resistor R?', r'\( I = \dfrac{\varepsilon}{R + r} \)')
d.basic('Maximum current a cell can give? Is it safe?', r'\( I_{max} = \varepsilon/r \)' + ' (short circuit); ' + X('usually far above the safe limit') + ' — damages the cell')
d.basic('Terminal voltage while a cell is being charged?', r'\( V = \varepsilon + Ir \)' + ' (current enters at the + terminal)')
d.basic('Which has higher internal resistance: dry cells or common electrolytic cells?', T('Dry cells') + ' (much higher)')
d.basic('Exercise 3.1: car battery ε = 12 V, r = 0.4 Ω. Maximum current?', N('30 A'))
d.basic('Exercise 3.2: ε = 10 V, r = 3 Ω, I = 0.5 A. External R and terminal voltage?', 'R = 20 − 3 = ' + N('17 Ω') + '; V = 10 − 1.5 = ' + N('8.5 V'))
steps_card(d, 'Exercise 3.8 · charging a battery', 'Find the missing step.', '8.0 V battery (r = 0.5 Ω) charged from 120 V dc through a 15.5 Ω series resistor. Terminal voltage?',
           ['Net driving emf = 120 − 8 = 112 V', 'I = 112/(15.5 + 0.5) = <b>7 A</b>', 'Charging: V = ε + Ir = 8 + 7 × 0.5 = <b>11.5 V</b>',
            'The series resistor limits the current, which would otherwise be dangerously large'], 2,
           'Terminal voltage during charging (Exercise 3.8)', 'I = 7 A; V = ε + Ir = 11.5 V; the series resistor limits the current')
d.basic('Teacher addition: power delivered to R by a cell (ε, r) is maximum when?', r'\( R = r \)' + ' (maximum power transfer); P_max = ε²/4r')

# ---------------------------------------------------------------- 3.11 Combination of cells
d.sec('3.11-cells-in-series-and-parallel')
d.basic('Two cells in series (+ to −): equivalent emf and internal resistance?', r'\( \varepsilon_{eq} = \varepsilon_1 + \varepsilon_2,\ r_{eq} = r_1 + r_2 \)')
d.basic('Two cells in series with like terminals joined (opposing)?', r'\( \varepsilon_{eq} = \varepsilon_1 - \varepsilon_2 \)' + ' (ε₁ > ε₂); r still adds')
d.basic('Two cells in parallel: equivalent emf and internal resistance?', r'\( \dfrac{1}{r_{eq}} = \dfrac1{r_1} + \dfrac1{r_2},\quad \dfrac{\varepsilon_{eq}}{r_{eq}} = \dfrac{\varepsilon_1}{r_1} + \dfrac{\varepsilon_2}{r_2} \)')
d.basic('Parallel cells with one reversed?', 'Use the same formulas with ' + r'\( \varepsilon_2 \to -\varepsilon_2 \)')
d.basic('Teacher addition: n identical cells (ε, r) in parallel?', 'ε_eq = ' + N('ε') + ', r_eq = ' + N('r/n') + ': same emf, more current capacity')
d.basic('Teacher addition: when is series better, when parallel (n identical cells, external R)?', T('Series') + ' if R ≫ r (I = nε/(R + nr)); ' + T('parallel') + ' if R ≪ r (I = ε/(R + r/n))')

# ---------------------------------------------------------------- 3.12 Kirchhoff
d.sec('3.12-kirchhoffs-rules')
d.basic('State Kirchhoff’s junction rule. Basis?', 'Sum of currents entering = sum leaving; based on ' + T('conservation of charge') + ' (no charge piles up in steady state)')
d.basic('State Kirchhoff’s loop rule. Basis?', 'Algebraic sum of potential changes around any closed loop = 0; based on ' + T('potential being single-valued') + ' (energy conservation)')
d.basic('Identify: write the junction rule at a and the loop rules shown.', 'I₃ = I₁ + I₂; loop ahdcba: −30I₁ − 41I₃ + 45 = 0; loop ahdefga: −30I₁ + 21I₂ − 80 = 0', **img('fig_3_15_kirchhoff'))
d.basic('Sign convention: crossing a resistor and a cell in a loop?', 'Resistor ' + T('along the current') + ': −IR (drop); against: +IR. Cell from − to +: +ε; from + to −: −ε')
d.basic('A current comes out negative after solving. What does it mean?', 'The actual current flows ' + T('opposite') + ' to the arrow you assumed — no need to redo')
d.basic('Points to ponder: does bending or reorienting wires affect the junction rule?', X('No') + ': it is charge conservation, independent of geometry')
steps_card(d, 'Example 3.5 · cube of resistors', 'Find the missing step.', 'Twelve 1 Ω resistors on the edges of a cube; 10 V across diagonally opposite corners A and C′. R_eq and currents?',
           ['By symmetry each of the 3 edges from A carries I, total 3I', 'Each splits into two edges carrying I/2, which recombine into 3 edges carrying I',
            'Loop A → B → C → C′ → battery: ε = IR + ½IR + IR = (5/2) IR', 'R<sub>eq</sub> = ε/3I = <b>5R/6 = 5/6 Ω</b>; 3I = 12 A, I = 4 A'], 2,
           'Cube of equal resistors, body diagonal (Example 3.5)', 'R_eq = 5R/6; with 10 V and R = 1 Ω: 12 A total, 4 A in each edge next to A or C′, 2 A in the middle edges')
d.basic('Identify: equivalent resistance between opposite corners of this cube (each edge R)?', r'\( R_{eq} = \dfrac56 R \)' + ' (symmetry: I, I/2, I pattern)', **img('fig_3_16_cube'))
d.basic('Teacher addition: cube of resistors R between the ends of one edge? Across a face diagonal?', 'Edge: ' + N('7R/12') + '; face diagonal: ' + N('3R/4') + '; body diagonal: ' + N('5R/6'))
d.basic('Example 3.6 (Fig 3.17): branch currents?', 'I₁ = ' + N('2.5 A') + ', I₂ = ' + N('5/8 A') + ', I₃ = ' + N('15/8 A') + '; AB 5/8 A, CA and BC 2.5 A, AD and DEB 15/8 A, CD ' + N('0'), **img('fig_3_17_network'))
d.basic('Correction/reading note: NCERT prints I₃ in Example 3.6 as a mixed fraction. Value?', 'I₃ = 1⁷⁄₈ A = ' + N('15/8 A = 1.875 A') + ' (check: I₂ + I₃ = 2.5 A)')

# ---------------------------------------------------------------- 3.13 Wheatstone bridge
d.sec('3.13-wheatstone-bridge')
d.basic('Wheatstone bridge: name the arms.', 'Battery across A–C (' + T('battery arm') + '); galvanometer across B–D (' + T('galvanometer arm') + '); four resistors R₁…R₄', **fig('fig_3_18_wheatstone'))
d.basic('Balance condition of a Wheatstone bridge?', r'\( \dfrac{R_2}{R_1} = \dfrac{R_4}{R_3} \)' + ' → I_g = 0 (null deflection)')
d.basic('How is an unknown resistance found with a Wheatstone bridge?', 'Put it in arm 4, fix R₁ and R₂, vary R₃ until null: ' + r'\( R_4 = R_3\dfrac{R_2}{R_1} \)')
d.basic('At balance, does it matter if the battery and galvanometer are swapped?', X('No') + ': the balance condition is unchanged; the galvanometer resistance also doesn’t matter at balance')
d.basic('Name a practical device based on the Wheatstone bridge.', 'The ' + T('meter bridge'))
d.basic('Mnemonic: balance condition?', '“' + T('Products of opposite arms are equal') + '”: R₁R₄ = R₂R₃')
steps_card(d, 'Example 3.7 · unbalanced bridge', 'Find the missing step.', 'AB = 100 Ω, BC = 10 Ω, CD = 5 Ω, DA = 60 Ω; galvanometer 15 Ω across BD; 10 V across AC. I_g?',
           ['Loop BADB: 100I₁ + 15I<sub>g</sub> − 60I₂ = 0', 'Loop BCDB: 10(I₁ − I<sub>g</sub>) − 15I<sub>g</sub> − 5(I₂ + I<sub>g</sub>) = 0',
            'Loop ADCEA: 60I₂ + 5(I₂ + I<sub>g</sub>) = 10', 'Eliminate I₁: I₂ = 31.5 I<sub>g</sub> → I<sub>g</sub> = 2/410.5 = <b>4.87 mA</b>'], 1,
           'Current through the galvanometer in an unbalanced bridge (Example 3.7)', 'Three loop equations; I₂ = 31.5 I_g; I_g ≈ 4.87 mA')
d.basic('Identify: the unbalanced bridge of Example 3.7. Why is it unbalanced?', '100/10 ≠ 60/5 (10 ≠ 12), so ' + T('I_g ≠ 0') + ' (4.87 mA)', **img('fig_3_19_example'))
d.basic('Exercise 3.7 (Fig 3.20): currents in the network with 10 V and a 10 Ω series resistor?', 'R_AC = 7 Ω → total ' + N('10/17 A') + '; AB and DC ' + N('4/17 A') + ', AD and BC ' + N('6/17 A') + ', BD ' + N('2/17 A') + ' (from D to B)', **img('fig_3_20_exercise'))

# ---------------------------------------------------------------- Points to ponder / summary
d.sec('points-to-ponder')
d.basic('Points to ponder: why can j = ρv (charge density × velocity) not be applied to the total charge of a wire?', 'A current-carrying wire is ' + T('neutral') + ' (ρ₊ = −ρ₋, total ρ = 0), yet j ≠ 0; apply j = ρv to each carrier type separately (j = ρ₋v₋, as v₊ ≈ 0)')
d.basic('Kirchhoff’s rules: which conservation law does each express?', 'Junction: ' + T('charge') + '. Loop: ' + T('energy') + ' (potential is single-valued)')

d.sec('summary')
table_card(d, 'Summary', 'Formula?', [
    ('Resistance', 'R = ρl/A', False), ('Drift velocity', 'v_d = eEτ/m', False), ('Current', 'I = neAv_d', False),
    ('Resistivity', 'ρ = m/ne²τ', False), ('Mobility', 'μ = v_d/E = eτ/m', False), ('Temperature', 'ρ_T = ρ₀[1 + α(T − T₀)]', False),
    ('Cell', 'V = ε − Ir, I = ε/(R + r)', False), ('Power', 'P = VI = I²R = V²/R', False), ('Bridge balance', 'R₁R₄ = R₂R₃', False)],
    term='Chapter 3 formula sheet')
table_card(d, 'Concept checks', 'True or false?', [
    ('Current is a vector', 'False (scalar)', True), ('Metals’ resistance rises with temperature', 'True', False),
    ('Drift speed is of the order of the speed of light', 'False (~mm/s)', True), ('Terminal voltage < emf while discharging', 'True', False),
    ('Ohm’s law holds for a diode', 'False', True)], term='Chapter 3 concept checks')

print(d.write(os.path.join(OUT, 'deck.json')), 'cards')
