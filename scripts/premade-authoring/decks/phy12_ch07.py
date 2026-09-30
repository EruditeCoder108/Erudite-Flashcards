import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Physics', 'class12-physics-ch07-alternating-current')
d = Deck('Chapter 7: Alternating Current', 'Class 12', ['class-12', 'physics', 'ch-7'])
d.description = 'rms values, phasors, R, L, C in ac, series LCR, resonance, power factor, transformers and power transmission'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- 7.1 Introduction
d.sec('7.1-introduction')
d.basic('Main reason ac is preferred over dc for power supply?', 'Ac voltage can be ' + T('easily and efficiently stepped up or down with transformers') + '.<br>It can also be transmitted economically over long distances')
d.basic('Form of the mains ac voltage?', 'A ' + T('sinusoidal') + ' function of time: v = v_m sin ωt')
d.basic('Everyday use of a special property of ac circuits, named by NCERT?', 'Tuning a radio: ' + T('resonance') + ' in an LCR circuit')

# ---------------------------------------------------------------- 7.2 AC voltage applied to a resistor
d.sec('7.2-ac-voltage-applied-to-a-resistor')
d.basic('Ac voltage v = v_m sin ωt across a pure resistor. Current?', r'\( i = i_m\sin\omega t,\quad i_m = \dfrac{v_m}{R} \)' + ': Ohm’s law holds for ac too', **fig('fig_7_1_resistor'))
d.basic('Phase relation between v and i in a pure resistor?', T('In phase') + ' (phase difference 0): both peak and vanish together', **fig('fig_7_2_vi_resistor'))
d.basic('Average current over a full cycle? Is there still heating?', 'Average i = ' + N('0') + ', but heating goes as ' + T('i²R') + ' (always positive), so energy is dissipated')
d.basic('Instantaneous power in a resistor and its average?', 'p = i_m²R sin²ωt; average ' + r'\( \bar p = \tfrac12 i_m^2R \)' + ', because ⟨sin²ωt⟩ = ½')
d.basic('Define rms current and rms voltage.', r'\( I = \dfrac{i_m}{\sqrt2} = 0.707\,i_m,\quad V = \dfrac{v_m}{\sqrt2} = 0.707\,v_m \)', **fig('fig_7_3_rms'))
d.basic('What does the rms current mean physically?', 'The ' + T('dc that gives the same average heating') + ' in the same resistor')
d.basic('Average power of ac in a resistor using rms values?', r'\( P = I^2R = IV = \dfrac{V^2}{R} \)' + ': same form as dc')
d.basic('Household supply “220 V”: is that rms or peak? Peak value?', T('rms') + '. Peak v_m = √2 × 220 ≈ ' + N('311 V'))
d.basic('Note: NCERT’s “Points to ponder” quotes 240 V for the room outlet. What do exams use?', 'Use the value given; NCERT’s examples use ' + T('220 V') + ' (India’s nominal supply is now 230 V). Peak of 240 V rms ≈ 340 V')
d.basic('Teacher addition: what does an ac ammeter or voltmeter read? A dc moving-coil meter?', 'Ac meters (hot-wire type) read ' + T('rms') + '. A moving-coil dc meter reads the ' + X('average = 0') + ' and would not deflect on ac')
d.basic('Teacher addition: mean value of ac over a half cycle?', r'\( \dfrac{2i_m}{\pi} = 0.637\,i_m \)' + ' (over a full cycle it is 0)')
d.basic('Teacher addition: rms value of a general periodic current?', 'Square root of the ' + T('mean of i²') + ' over a period. The 1/√2 factor is only for a ' + T('sinusoid'))
steps_card(d, 'Example 7.1 · bulb', 'Find the missing step.', 'Bulb rated 100 W, 220 V. Find R, peak voltage and rms current.',
           ['R = V²/P = 220²/100 = <b>484 Ω</b>', 'Peak voltage v_m = √2 V = <b>311 V</b>', 'I = P/V = 100/220 = <b>0.454 A</b>'], 0,
           'A 100 W, 220 V bulb (Example 7.1)', 'R = 484 Ω, v_m = 311 V, I = 0.454 A')
d.basic('Trap: resistance of a 100 W, 220 V bulb when operated on 110 V?', 'R stays ' + N('484 Ω') + '. Power drops to V²/R = 110²/484 = ' + N('25 W') + ' (quarter)')

# ---------------------------------------------------------------- 7.3 Phasors
d.sec('7.3-representation-by-rotating-vectors-phasors')
d.basic('What is a phasor?', 'A vector rotating about the origin with angular speed ' + T('ω') + '.<br>Its length is the ' + T('amplitude') + '.<br>Its vertical component is the instantaneous value')
d.basic('Phasor diagram of a resistor: angle between V and I phasors?', N('0') + ': they point along the same line at all times', **fig('fig_7_4_phasor_R'))
d.basic('Are voltage and current in ac really vectors?', X('No') + ': they are scalars; phasors are only a device so harmonic quantities add by the ' + T('vector addition rule'))
d.basic('Why use phasors?', 'To show ' + T('phase relations') + ' between v and i and to add voltages across R, L, C easily')
d.basic('Trap: how must voltages across R and C in series be added?', 'As ' + T('phasors') + ': ' + r'\( V = \sqrt{V_R^2 + V_C^2} \)' + ', not V_R + V_C, because they are 90° out of phase')

# ---------------------------------------------------------------- 7.4 Inductor
d.sec('7.4-ac-voltage-applied-to-an-inductor')
d.basic('Pure inductor, v = v_m sin ωt. Current?', r'\( i = i_m\sin(\omega t - \pi/2),\quad i_m = \dfrac{v_m}{\omega L} \)', **fig('fig_7_5_inductor'))
d.basic('Derive the current in a pure inductor.', 'v = L di/dt → di/dt = (v_m/L) sin ωt. Integrate: ' + T('i = −(v_m/ωL) cos ωt') + ' (integration constant 0 as no dc component) = i_m sin(ωt − π/2)')
d.basic('Inductive reactance: formula, unit, dependence?', r'\( X_L = \omega L = 2\pi\nu L \)' + '; ohm; ' + T('∝ frequency') + ' and ∝ L. Zero for dc')
d.basic('Phase relation in a pure inductor?', 'Current ' + T('lags') + ' the voltage by ' + N('π/2') + ' (one quarter cycle)', **fig('fig_7_6_phasor_L'))
d.basic('Average power absorbed by a pure inductor over a cycle?', N('Zero') + ': p = −½ i_m v_m sin 2ωt averages to 0; energy is stored and returned')
d.basic('Why does an inductor pass low frequencies more easily?', 'X_L = 2πνL is ' + T('small for small ν') + '; for dc X_L = 0')
steps_card(d, 'Example 7.2 · pure inductor', 'Find the missing step.', '25.0 mH inductor on a 220 V, 50 Hz source. Find X_L and rms current.',
           ['X_L = 2πνL = 2 × 3.14 × 50 × 25 × 10⁻³', 'X_L = <b>7.85 Ω</b>', 'I = V/X_L = 220/7.85 ≈ <b>28 A</b>'], 1,
           'Reactance and current in an inductor (Example 7.2)', 'X_L = 7.85 Ω, I ≈ 28 A')
d.basic('Example 7.5: iron rod pushed into a coil in series with a bulb on ac. Bulb glow?', T('Decreases') + ': L rises (μᵣ), so X_L rises and more of the supply voltage falls across the coil')
d.basic('Teacher addition: choke coil?', 'An inductor used to ' + T('reduce ac current without wasting power') + ', unlike a series resistor (which dissipates I²R).<br>Its power factor is nearly zero')

# ---------------------------------------------------------------- 7.5 Capacitor
d.sec('7.5-ac-voltage-applied-to-a-capacitor')
d.basic('Does a capacitor pass dc? Ac?', 'dc: current only during charging, then ' + X('zero') + '<br>Ac: it charges and discharges every half cycle, so current ' + T('flows') + ' (limited)', **fig('fig_7_7_capacitor'))
d.basic('Capacitor, v = v_m sin ωt. Current?', r'\( i = i_m\sin(\omega t + \pi/2),\quad i_m = \omega C v_m \)')
d.basic('Derive the current in a capacitor.', 'q = Cv = Cv_m sin ωt; i = dq/dt = ' + T('ωCv_m cos ωt') + ' = ωCv_m sin(ωt + π/2)')
d.basic('Capacitive reactance: formula, unit, dependence?', r'\( X_C = \dfrac{1}{\omega C} = \dfrac{1}{2\pi\nu C} \)' + '; ohm; ' + T('inversely') + ' proportional to ν and C. Infinite for dc')
d.basic('Phase relation in a pure capacitor?', 'Current ' + T('leads') + ' the voltage by ' + N('π/2'), **fig('fig_7_8_phasor_C'))
d.basic('Average power absorbed by a pure capacitor?', N('Zero') + ' over a cycle: p = ½ i_m v_m sin 2ωt averages to 0')
d.basic('Mnemonic for phase in L and C?', '“' + T('CIVIL') + '”: in a ' + T('C') + ' the ' + T('I') + ' leads ' + T('V') + '; in an ' + T('L') + ' the ' + T('V') + ' leads ' + T('I'))
d.basic('Example 7.3: lamp in series with a capacitor: dc source, then ac source; C reduced?', 'dc: lamp does ' + X('not') + ' glow (no steady current). Ac: lamp glows; smaller C → larger X_C → ' + T('dimmer'))
steps_card(d, 'Example 7.4 · capacitor', 'Find the missing step.', '15.0 μF capacitor on 220 V, 50 Hz. Find X_C, rms and peak current. What if ν doubles?',
           ['X_C = 1/(2π × 50 × 15 × 10⁻⁶) ≈ <b>212 Ω</b>', 'I = V/X_C = 220/212 = <b>1.04 A</b>', 'Peak i_m = √2 I = <b>1.47 A</b>, leading V by π/2', 'ν doubled: X_C halves → current <b>doubles</b>'], 1,
           'Reactance and current in a capacitor (Example 7.4)', 'X_C = 212 Ω, I = 1.04 A, i_m = 1.47 A; current doubles')
table_card(d, 'R, L, C in ac', 'Compare.', [
    ('Resistor', 'R; i in phase with v; power dissipated', False), ('Inductor', 'X_L = ωL; i lags v by π/2; P = 0', False),
    ('Capacitor', 'X_C = 1/ωC; i leads v by π/2; P = 0', False), ('Effect of raising ν', 'R same; X_L up; X_C down', False)],
    term='Pure R, L and C in ac')

# ---------------------------------------------------------------- 7.6 Series LCR
d.sec('7.6-ac-voltage-applied-to-a-series-lcr-circuit')
d.basic('Loop equation of a series LCR circuit?', r'\( L\dfrac{di}{dt} + iR + \dfrac{q}{C} = v \)', **fig('fig_7_10_lcr'))
d.basic('In a series LCR circuit, what is common to R, L and C?', 'The ' + T('current') + ' (same amplitude and phase). Voltages differ in phase')
d.basic('Phases of V_R, V_L, V_C relative to I?', 'V_R ' + T('in phase') + ' with I; V_L leads I by ' + N('π/2') + '; V_C lags I by ' + N('π/2'))
d.basic('Amplitudes of the three voltages?', 'v_Rm = i_m R, v_Lm = i_m X_L, v_Cm = i_m X_C')
d.basic('Why can V_L and V_C be combined into one phasor?', 'They lie along the same line in ' + T('opposite directions') + ': net magnitude |v_Cm − v_Lm|', **fig('fig_7_11_phasors'))
d.basic('Impedance of a series LCR circuit?', r'\( Z = \sqrt{R^2 + (X_L - X_C)^2},\quad i_m = \dfrac{v_m}{Z} \)', **fig('fig_7_12_impedance'))
d.basic('Phase angle φ of the current in a series LCR circuit (i = i_m sin(ωt + φ))?', r'\( \tan\phi = \dfrac{X_C - X_L}{R} \)')
d.basic('If X_C > X_L: nature of circuit, sign of φ, current?', 'Predominantly ' + T('capacitive') + '; φ positive; current ' + T('leads') + ' the source voltage', **fig('fig_7_13_lcr_phasor'))
d.basic('If X_L > X_C: nature of circuit, sign of φ, current?', 'Predominantly ' + T('inductive') + '; φ negative; current ' + T('lags') + ' the source voltage')
d.basic('Trap: with φ defined as “angle of current relative to voltage”, sign of φ?', 'NCERT uses ' + r'\( \tan\phi = \dfrac{X_C - X_L}{R} \)' + ' (angle of i). Many books define φ = angle of v, giving X_L − X_C. Check the definition in the question')
d.basic('Teacher addition: Z for an RL circuit and an RC circuit?', 'RL: ' + r'\( Z = \sqrt{R^2 + X_L^2} \)' + ', current lags. RC: ' + r'\( Z = \sqrt{R^2 + X_C^2} \)' + ', current leads')
d.basic('Limitation of the phasor method?', 'Gives only the ' + T('steady-state') + ' solution (no initial conditions); the ' + T('transient') + ' part dies out after some time')
steps_card(d, 'Example 7.6 · RC series', 'Find the missing step.', '200 Ω resistor and 15.0 μF capacitor in series on 220 V, 50 Hz. Find I and the voltage across each. Why do the two voltages add to more than 220 V?',
           ['X_C = 212.3 Ω; Z = √(200² + 212.3²) ≈ <b>291.7 Ω</b>', 'I = V/Z = 220/291.7 = <b>0.755 A</b>', 'V_R = IR = <b>151 V</b>, V_C = IX_C = <b>160.3 V</b> (sum 311 V > 220 V)', 'They are 90° out of phase: V = √(V_R² + V_C²) = <b>220 V</b> ✓'], 3,
           'Voltages in an RC circuit (Example 7.6)', 'I = 0.755 A, V_R = 151 V, V_C = 160.3 V, quadrature sum = 220 V')

d.sec('7.6.2-resonance')
d.basic('Resonance in a series LCR circuit: condition and frequency?', T('X_L = X_C') + ' → ' + r'\( \omega_0 = \dfrac{1}{\sqrt{LC}},\ \nu_0 = \dfrac{1}{2\pi\sqrt{LC}} \)')
d.basic('What happens at resonance?', 'Z is minimum (' + N('Z = R') + '); current is maximum, ' + r'\( i_m = v_m/R \)' + '; φ = 0 (current in phase with v); V_L and V_C cancel', **fig('fig_7_14_resonance'))
d.basic('Effect of increasing R on the resonance curve?', 'Peak height ' + T('falls') + ' (i_m = v_m/R) and the curve gets ' + T('broader') + ' (less sharp). R = 100 Ω gives twice the peak of R = 200 Ω')
d.basic('Can resonance occur in an RL or RC circuit? Why?', X('No') + ': needs both L and C so that V_L and V_C can cancel')
d.basic('Mechanical analogy for resonance?', 'A child on a swing pushed at its ' + T('natural frequency') + ': amplitude grows large')
d.basic('How does a radio tune to a station?', 'Vary ' + T('C') + ' so that ω₀ = 1/√LC matches the station’s frequency: current at that frequency is maximum')
d.basic('Example 7.10: how does an airport metal detector work?', 'Walk-through coil + capacitor tuned to ' + T('resonance') + '.<br>Metal changes L, so impedance and current change, triggering the alarm')
d.basic('Teacher addition: quality factor Q of a series LCR circuit?', r'\( Q = \dfrac{\omega_0 L}{R} = \dfrac{1}{\omega_0 CR} = \dfrac{1}{R}\sqrt{\dfrac{L}{C}} \)' + ': measures the ' + T('sharpness') + ' of resonance (dimensionless)')
d.basic('Teacher addition: bandwidth and its link to Q?', 'Half-power bandwidth ' + r'\( \Delta\omega = \dfrac{R}{L} = \dfrac{\omega_0}{Q} \)' + ': ' + T('higher Q → narrower, sharper') + ' resonance')
d.basic('Teacher addition: voltage across L or C at resonance compared with the source?', 'V_L = V_C = ' + T('Q × V') + ', which can be far larger than the source voltage (while V_L and V_C cancel each other)')

# ---------------------------------------------------------------- 7.7 Power
d.sec('7.7-power-in-ac-circuit-the-power-factor')
d.basic('Average power in a series LCR circuit?', r'\( P = VI\cos\phi = I^2Z\cos\phi \)' + '; cos φ = ' + T('power factor') + ' = R/Z')
d.basic('Derive P = VI cos φ.', 'p = vi = ½ v_m i_m [cos φ − cos(2ωt + φ)]; the second term averages to 0, so P = ½ v_m i_m cos φ = ' + T('V I cos φ'))
d.basic('Power factor of a purely resistive circuit? Power?', 'cos φ = ' + N('1') + ': maximum power dissipation')
d.basic('Power factor and average power of a pure L or pure C?', 'φ = π/2 → cos φ = ' + N('0') + ', no power, though current flows: ' + T('wattless current'))
d.basic('In an LCR circuit, in which element is power dissipated?', 'Only in the ' + T('resistor') + ': P = I²R')
d.basic('Power and power factor at resonance?', 'cos φ = 1 and P = I²R = ' + T('V²/R') + ', the maximum')
d.basic('Example 7.7: why does a low power factor cause large transmission loss?', 'P = IV cos φ: for fixed P and V, small cos φ needs ' + T('larger I') + ', so the ' + T('I²R') + ' loss in the lines rises')
d.basic('How is the power factor improved?', 'Connect a suitable ' + T('capacitor in parallel') + ': its leading wattless current cancels the lagging wattless component I_q', **fig('fig_7_15_power_comp'))
d.basic('Power component and wattless component of current?', 'I_p = I cos φ (along V, gives power). I_q = I sin φ (⊥ V, ' + T('wattless') + ')')
steps_card(d, 'Example 7.8 · LCR numbers', 'Find the missing step.', 'v_m = 283 V, ν = 50 Hz, R = 3 Ω, L = 25.48 mH, C = 796 μF in series. Find Z, φ, P and power factor.',
           ['X_L = 2πνL = <b>8 Ω</b>, X_C = 1/2πνC = <b>4 Ω</b>', 'Z = √(3² + (8 − 4)²) = <b>5 Ω</b>', 'tan φ = (X_C − X_L)/R = −4/3 → φ = <b>−53.1°</b> (current lags)', 'I = 283/(√2 × 5) = 40 A; P = I²R = <b>4800 W</b>; cos φ = <b>0.6</b>'], 2,
           'Series LCR calculation (Example 7.8)', 'Z = 5 Ω, φ = −53.1°, P = 4800 W, power factor 0.6')
steps_card(d, 'Example 7.9 · resonance', 'Find the missing step.', 'Same circuit, frequency now variable. Find ν₀, and Z, I, P at resonance.',
           ['ω₀ = 1/√(LC) = 1/√(25.48 × 10⁻³ × 796 × 10⁻⁶) = <b>222.1 rad/s</b>', 'ν₀ = ω₀/2π = <b>35.4 Hz</b>', 'Z = R = <b>3 Ω</b>; I = (283/√2)/3 = <b>66.7 A</b>', 'P = I²R = <b>13.35 kW</b> (more than at 50 Hz)'], 0,
           'Resonance of the LCR circuit (Example 7.9)', 'ν₀ = 35.4 Hz, Z = 3 Ω, I = 66.7 A, P = 13.35 kW')
d.basic('Teacher addition: a series LCR at 50 Hz has X_L = X_C. What is I?', 'V/R (resonance at 50 Hz), and V_R = V (whole source across R)')

# ---------------------------------------------------------------- 7.8 Transformers
d.sec('7.8-transformers')
d.basic('Principle and parts of a transformer?', T('Mutual induction') + '. Primary (N_p turns) and secondary (N_s turns) on a ' + T('soft-iron core'), **fig('fig_7_16_transformer'))
d.basic('Voltage ratio of an ideal transformer?', r'\( \dfrac{V_s}{V_p} = \dfrac{N_s}{N_p} \)')
d.basic('Current ratio of an ideal transformer?', r'\( \dfrac{I_s}{I_p} = \dfrac{N_p}{N_s} = \dfrac{V_p}{V_s} \)' + ' (from V_pI_p = V_sI_s)')
d.basic('Step-up vs step-down transformer?', 'Step-up: ' + T('N_s > N_p') + ', V rises, I falls. Step-down: ' + T('N_s < N_p') + ', V falls, I rises')
d.basic('Does a step-up transformer violate energy conservation?', X('No') + ': voltage rises but current falls in the same ratio; power in = power out (ideal)')
d.basic('Assumptions behind V_s/V_p = N_s/N_p?', 'Negligible primary resistance and current; ' + T('all flux links both coils') + '; small secondary current')
d.basic('Why is e_p = v_p in an ideal transformer?', 'Else the primary current would be ' + X('infinite') + ' (zero resistance); the back emf equals the applied voltage')
d.basic('Example: primary 100 turns, secondary 200 turns, 220 V at 10 A input. Output?', T('440 V at 5.0 A'))
d.basic('Efficiency of a transformer?', r'\( \eta = \dfrac{P_{out}}{P_{in}} = \dfrac{V_sI_s}{V_pI_p} \)' + '; well-designed ones exceed ' + N('95%'))
d.basic('List the four energy losses in a real transformer and remedy for each.', '(i) ' + T('Flux leakage') + ': wind coils over one another. (ii) ' + T('Resistance of windings') + ' (I²R): thick wire. (iii) ' + T('Eddy currents') + ': laminated core. (iv) ' + T('Hysteresis') + ': low-loss soft magnetic material')
d.basic('Why is the core laminated?', 'Insulated thin sheets break up ' + T('eddy current') + ' loops in the iron, reducing heating')
d.basic('Why is transmission done at high voltage?', 'For fixed power P = VI, high V means ' + T('small I') + ', so the ' + T('I²R') + ' loss in the lines is small')
d.basic('Steps in power transmission, per NCERT?', '1) Generator voltage stepped ' + T('up') + '<br>2) Long-distance lines<br>3) Area sub-station steps ' + T('down') + '<br>4) Distribution sub-stations and poles<br>5) About 240 V at homes')
d.basic('Teacher addition: power loss in a line of resistance R carrying P at voltage V?', r'\( P_{loss} = I^2R = \dfrac{P^2R}{V^2} \)' + ': raising V tenfold cuts loss ' + N('100×'))
d.basic('Teacher addition: can a transformer work on dc? Why?', X('No') + ': needs changing flux; a steady primary current gives no induced secondary emf')
d.basic('Teacher addition: does a transformer change the frequency?', X('No') + ': output has the same frequency as the input')

# ---------------------------------------------------------------- Points to ponder
d.sec('points-to-ponder')
d.basic('Rating of an ac appliance (e.g. 60 W)?', 'Refers to ' + T('average power') + ' (rms based)')
d.basic('Can power consumed in an ac circuit be negative on average?', X('No') + ': the average power P = VI cos φ is never negative (instantaneous power in L and C can be)')
d.basic('How is the ac ampere defined?', '1 A rms = the alternating current producing the ' + T('same average heating') + ' as 1 A dc.<br>(The force between wires averages to zero for ac)')
d.basic('Generator vs motor?', 'Generator: mechanical → electrical. Motor: ' + T('electrical → mechanical') + '. Both just transform energy')
d.basic('Where are the losses in an ac circuit?', 'Only in ' + T('resistive') + ' elements; pure L and C have none')
d.basic('Why does the power factor matter?', 'It measures how close the circuit is to using the ' + T('maximum power') + ' for the given V and I')
table_card(d, 'NCERT quantity table', 'Symbol, dimensions?', [
    ('rms voltage V', 'V; [ML²T⁻³A⁻¹]', False), ('rms current I', 'A; [A]', False), ('Reactance X_L, X_C', 'Ω; [ML²T⁻³A⁻²]', False),
    ('Impedance Z', 'Ω; [ML²T⁻³A⁻²]', False), ('Resonant frequency ω₀', '1/√LC; [T⁻¹]', False), ('Quality factor Q', 'ω₀L/R = 1/ω₀CR; dimensionless', False),
    ('Power factor', 'cos φ; dimensionless', False)],
    term='Chapter 7 quantities')

# ---------------------------------------------------------------- Exercises
d.sec('exercises')
d.basic('Exercise 7.1: 100 Ω resistor on 220 V, 50 Hz. (a) rms current (b) net power over a cycle?', '(a) I = V/R = ' + N('2.20 A') + '. (b) P = V²/R = ' + N('484 W'))
d.basic('Exercise 7.2: (a) peak 300 V, rms? (b) rms 10 A, peak?', '(a) 300/√2 = ' + N('212.1 V') + '. (b) 10√2 = ' + N('14.1 A'))
d.basic('Exercise 7.3: 44 mH inductor on 220 V, 50 Hz. rms current?', 'X_L = 2π × 50 × 0.044 = 13.8 Ω; I = 220/13.8 = ' + N('15.9 A'))
d.basic('Exercise 7.4: 60 μF capacitor on 110 V, 60 Hz. rms current?', 'X_C = 1/(2π × 60 × 60 × 10⁻⁶) = 44.2 Ω; I = 110/44.2 = ' + N('2.49 A'))
d.basic('Exercise 7.5: net power absorbed in Exercises 7.3 and 7.4 over a cycle?', N('Zero') + ' in each: pure L and C have φ = 90°, so cos φ = 0 (energy stored and returned)')
d.basic('Exercise 7.6: charged 30 μF capacitor joined to a 27 mH inductor. Angular frequency of free oscillations?', 'ω = 1/√(LC) = 1/√(27 × 10⁻³ × 30 × 10⁻⁶) = ' + N('1.1 × 10³ s⁻¹'))
d.basic('Exercise 7.7: R = 20 Ω, L = 1.5 H, C = 35 μF, 200 V supply at the natural frequency. Average power?', 'At resonance Z = R, so P = V²/R = 200²/20 = ' + N('2000 W'))
steps_card(d, 'Exercise 7.8 · resonating LCR', 'Find the missing step.', 'L = 5.0 H, C = 80 μF, R = 40 Ω, 230 V source. (a) ω₀ (b) Z and current amplitude (c) rms voltage across each element.',
           ['ω₀ = 1/√(LC) = 1/√(5 × 80 × 10⁻⁶) = <b>50 rad/s</b>', 'Z = R = <b>40 Ω</b>; i_m = √2 × 230/40 = <b>8.1 A</b>', 'I_rms = 230/40 = 5.75 A; X_L = X_C = 250 Ω', 'V_L = V_C = 5.75 × 250 = <b>1437.5 V</b>, V_R = <b>230 V</b>; V_L − V_C = 0'], 3,
           'Resonating series LCR circuit (Exercise 7.8)', 'ω₀ = 50 rad/s, Z = 40 Ω, i_m = 8.1 A, V_L = V_C = 1437.5 V, V_R = 230 V')
d.basic('Exercise 7.8: how can V_L = 1437.5 V exist with a 230 V source?', 'V_L and V_C are ' + T('180° out of phase') + ' and cancel exactly; each is Q times the source (Q = 6.25)')

# ---------------------------------------------------------------- Summary
d.sec('summary')
table_card(d, 'Summary', 'Formula?', [
    ('rms current, voltage', 'I = i_m/√2, V = v_m/√2', False), ('Average power (resistor)', 'P = I²R = IV', False), ('Inductive reactance', 'X_L = ωL', False),
    ('Capacitive reactance', 'X_C = 1/ωC', False), ('Impedance (LCR)', 'Z = √(R² + (X_L − X_C)²)', False), ('Phase angle', 'tan φ = (X_C − X_L)/R', False),
    ('Resonant frequency', 'ω₀ = 1/√LC', False), ('Average power', 'P = VI cos φ', False), ('Quality factor', 'Q = ω₀L/R = 1/ω₀CR', False), ('Transformer', 'V_s/V_p = N_s/N_p = I_p/I_s', False)],
    term='Chapter 7 formula sheet')
table_card(d, 'Concept checks', 'True or false?', [
    ('Average ac current over a full cycle is 0.707 i_m', 'False (it is 0; rms is 0.707 i_m)', True), ('In a pure inductor, current leads voltage', 'False (lags by π/2)', True),
    ('A pure capacitor dissipates no average power', 'True', False), ('Resonance can occur in an RL circuit', 'False (needs L and C)', True),
    ('Power factor is 1 at resonance', 'True', False), ('A transformer works on dc', 'False', True)],
    term='Chapter 7 concept checks')

print(d.write(os.path.join(OUT, 'deck.json')), 'cards')
