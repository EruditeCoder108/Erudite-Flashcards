import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase_phy as sp

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Physics', 'class11-physics-ch14-waves')
d = Deck('Chapter 14: Waves', 'Class 11', ['class-11', 'physics', 'ch-14'])
d.description = 'Transverse and longitudinal waves, wave equation, wave speed on strings and in gases, superposition, reflection, standing waves, pipes, beats'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- 14.1 Introduction
d.sec('14.1-introduction')
d.basic('What is a wave?', 'A pattern of disturbance that moves ' + X('without') + ' bulk flow of matter, carrying ' + T('energy and information'))
d.basic('Why do cork pieces on a rippled pond not move outward?', 'Water only moves ' + T('up and down') + ' locally; only the disturbance travels')
table_card(d, '14.1 · kinds of waves', 'Needs a medium? Example?', [
    ('Mechanical', 'yes — string, water, sound, seismic waves', False),
    ('Electromagnetic', 'no — light, radio, X-rays (speed c in vacuum)', False),
    ('Matter waves', 'associated with electrons, protons, atoms (electron microscope)', False)], term='Three kinds of waves')
d.basic('Speed of electromagnetic waves in vacuum?', N('c = 299 792 458 m/s') + ' (exact)')
d.basic('How does a disturbance travel along coupled springs or train bogies?', 'Each part pushes the next through ' + T('elastic coupling') + '; each only oscillates about its own equilibrium', **fig('fig_14_1_springs'))
d.basic('What plays the role of the spring’s extension in a sound wave?', 'The change in ' + T('density') + ' (and pressure): compressions and rarefactions')

# ---------------------------------------------------------------- 14.2 Transverse and longitudinal
d.sec('14.2-transverse-and-longitudinal')
d.basic('Transverse vs longitudinal wave?', T('Transverse') + ': particles oscillate ⟂ to the direction of travel (string). ' + T('Longitudinal') + ': particles oscillate along it (sound)', **fig('fig_14_3_harmonic_wave'))
d.basic('A single jerk on a string produces…?', 'A transverse ' + T('pulse'), **fig('fig_14_2_pulse'))
d.basic('How is a longitudinal wave produced in a pipe?', 'A piston pushed and pulled creates ' + T('compressions and rarefactions') + ' travelling along the air', **fig('fig_14_4_sound_pipe'))
d.basic('Why can’t transverse waves travel through fluids?', 'They need a medium that resists ' + T('shear') + '; fluids cannot sustain shearing stress. Longitudinal waves need only compressibility (all media)')
d.basic('Which waves can travel in steel? In air?', 'Steel: ' + T('both') + ' transverse and longitudinal. Air: ' + T('only longitudinal'))
d.basic('Capillary vs gravity water waves?', T('Capillary') + ': ripples of a few cm, restoring force surface tension. ' + T('Gravity') + ': metres to hundreds of metres, restoring force gravity')
d.basic('Ocean waves: transverse or longitudinal?', 'A ' + T('combination') + ': water particles move up–down and back–forth')
d.basic('Wind vs sound wave?', 'Wind is ' + T('motion of air as a whole') + '; a sound wave is a moving pattern of compressions with no net flow')
table_card(d, 'Example 14.1', 'Transverse, longitudinal or both?', [
    ('Kink in a spring from a sideways jerk', 'transverse and longitudinal', False), ('Piston moved back and forth in a liquid', 'longitudinal', False),
    ('Waves from a motorboat', 'transverse and longitudinal', False), ('Ultrasonic waves from a quartz crystal', 'longitudinal', False)], term='Wave type examples (Example 14.1)')

# ---------------------------------------------------------------- 14.3 Displacement relation
d.sec('14.3-displacement-relation')
d.basic('Equation of a harmonic wave travelling in +x?', r'\( y(x,t) = a\sin(kx - \omega t + \phi) \)' + '; for −x: ' + r'\( a\sin(kx + \omega t + \phi) \)')
table_card(d, 'Fig. 14.5 · wave symbols', 'Name?', [
    ('a', 'amplitude', False), ('k', 'angular wave number (rad/m)', False), ('ω', 'angular frequency (rad/s)', False),
    ('kx − ωt + φ', 'phase', False), ('φ', 'initial phase angle', False)], term='Symbols in y = a sin(kx − ωt + φ)')
d.basic('Fix t, then fix x in y = a sin(kx − ωt): what do you see?', 'Fixed t: the ' + T('shape') + ' of the wave (a sine in x). Fixed x: that particle does ' + T('SHM') + ' in time', **fig('fig_14_6_progressing'))
d.basic('Define wavelength and angular wave number.', T('λ') + ': least distance between points in the same phase (crest to crest). ' + r'\( k = \dfrac{2\pi}{\lambda} \)')
d.basic('Relations for period and frequency of a wave?', r'\( \omega = \dfrac{2\pi}{T} = 2\pi\nu \)', **fig('fig_14_7_element_time'))
d.basic('Longitudinal wave: what does the displacement mean?', r'\( s(x,t) = a\sin(kx - \omega t + \phi) \)' + ' — displacement ' + T('along') + ' the direction of travel')
steps_card(d, 'Example 14.2', 'Find the missing step.', 'y = 0.005 sin(80.0x − 3.0t) (SI). Amplitude, wavelength, period, frequency?',
           ['a = 0.005 m = 5 mm', 'λ = 2π/k = 2π/80 = 7.85 cm', 'T = 2π/ω = 2.09 s', 'ν = 1/T = <b>0.48 Hz</b>'], 1,
           'Reading a wave equation', 'a = 5 mm, λ = 7.85 cm, T = 2.09 s, ν = 0.48 Hz')
d.basic('Phase difference between two points Δx apart on a wave?', r'\( \Delta\phi = \dfrac{2\pi}{\lambda}\Delta x = k\,\Delta x \)')

# ---------------------------------------------------------------- 14.4 Speed
d.sec('14.4-speed-of-waves')
d.basic('Wave speed in terms of ω, k, λ, ν?', r'\( v = \dfrac{\omega}{k} = \lambda\nu = \dfrac{\lambda}{T} \)' + ': in one period the pattern moves one wavelength', **fig('fig_14_8_shift'))
d.basic('What sets the speed and what sets the frequency of a mechanical wave?', 'Speed: the ' + T('medium') + ' (elasticity and inertia). Frequency: the ' + T('source') + '. Then λ = v/ν')
d.basic('Speed of transverse waves on a stretched string?', r'\( v = \sqrt{\dfrac{T}{\mu}} \)' + ' (T = tension, μ = mass per unit length)')
d.basic('How is v = √(T/μ) found in NCERT?', 'By ' + T('dimensional analysis') + ' (the constant C = 1 comes from the exact theory)')
d.basic('Example 14.3: steel wire 0.72 m, 5.0 g, tension 60 N. Wave speed?', 'μ = 6.9 × 10⁻³ kg/m → v = ' + N('≈ 93 m/s'))
d.basic('Speed of longitudinal (sound) waves in a fluid and in a solid bar?', r'\( v = \sqrt{\dfrac{B}{\rho}} \)' + ' (fluid); ' + r'\( v = \sqrt{\dfrac{Y}{\rho}} \)' + ' (thin bar)')
d.basic('Why is sound faster in solids and liquids than in gases?', 'They are denser, but their ' + T('elastic moduli are far larger'), **fig('tab_14_1_sound_speeds'))
d.basic('Speed of sound in air (0 °C), water, steel (Table 14.1)?', 'Air ' + N('331 m/s') + ', water ' + N('≈ 1402–1482 m/s') + ', steel ' + N('5941 m/s'))
d.basic('Newton’s formula for sound in a gas, and its value for air?', r'\( v = \sqrt{\dfrac{P}{\rho}} \)' + ' (isothermal, B = P) → ' + N('280 m/s') + ': about 15 % too low')
d.basic('What was the Laplace correction?', 'Sound compressions are too fast for heat flow → ' + T('adiabatic') + ', B = γP: ' + r'\( v = \sqrt{\dfrac{\gamma P}{\rho}} \)' + ' ≈ ' + N('331 m/s'))
d.basic('Exercise 14.4: speed of sound in air vs pressure, temperature, humidity?', r'\( v = \sqrt{\gamma RT/M} \)' + ': ' + T('independent of pressure') + '; ∝ √T; ' + T('increases with humidity') + ' (water vapour lowers M)')
d.basic('Does the speed of a mechanical wave depend on the source’s velocity?', X('No') + ': relative to the medium it depends only on the medium')
d.basic('Exercise 14.1: 2.50 kg, 20.0 m string under 200 N. Time for a jerk to travel its length?', 'v = √(200/0.125) = 40 m/s → ' + N('0.5 s'))
d.basic('Exercise 14.2: stone dropped from a 300 m tower. When is the splash heard at the top (sound 340 m/s)?', '7.82 s fall + 0.88 s sound ≈ ' + N('8.7 s'))
d.basic('Exercise 14.3: 12.0 m, 2.10 kg steel wire. Tension for wave speed 343 m/s?', 'T = μv² ≈ ' + N('2.06 × 10⁴ N'))
d.basic('Exercise 14.6: 1000 kHz bat sound hits water. Wavelength reflected (air 340 m/s) and transmitted (water 1486 m/s)?', N('3.4 × 10⁻⁴ m') + ' and ' + N('1.49 × 10⁻³ m') + ' (frequency is unchanged)')
d.basic('Exercise 14.7: ultrasonic scanner 4.2 MHz in tissue (1.7 km/s). Wavelength?', N('4.1 × 10⁻⁴ m'))
d.basic('Exercise 14.8: y = 3.0 sin(36t + 0.018x + π/4) (cm, s). Direction, speed, frequency, λ?', 'Travels ' + T('right to left') + ' at ' + N('20 m/s') + '; a = 3.0 cm, ν ≈ ' + N('5.7 Hz') + ', φ = π/4, λ ≈ ' + N('3.5 m'))
d.basic('Exercise 14.10: y = 2.0 cos 2π(10t − 0.0080x + 0.35) (cm). Phase difference for points 4 m and 0.5 m apart?', N('6.4π rad') + ' and ' + N('0.8π rad') + '; for λ/2: π; for 3λ/4: 3π/2 (the key writes π/2, the same phase counted the other way round)')
d.basic('Exercise 14.5: must every function of (x ± vt) represent a travelling wave?', X('No') + ': it must also be ' + T('finite everywhere, always') + '; of (x − vt)², log[(x + vt)/x₀], 1/(x + vt), none qualifies')

# ---------------------------------------------------------------- 14.5 Superposition
d.sec('14.5-superposition')
d.cloze('Principle of superposition: when waves overlap, the resultant displacement is the {{c1::algebraic sum}} of the individual displacements; each wave moves {{c2::as if the others were absent}}.')
d.basic('Two equal and opposite pulses cross. What happens at the moment of full overlap? After?', 'Displacement is ' + T('zero everywhere') + ' for an instant; afterwards both pulses continue unchanged', **fig('fig_14_9_pulses'))
d.basic('Two identical waves with phase difference φ: resultant amplitude?', r'\( A = 2a\cos\dfrac{\phi}{2} \)', **fig('fig_14_10_interference'))
d.basic('Constructive vs destructive interference?', T('Constructive') + ': φ = 0, 2π… → amplitude 2a. ' + T('Destructive') + ': φ = π → amplitude 0')

# ---------------------------------------------------------------- 14.6 Reflection, standing waves
d.sec('14.6-reflection')
d.basic('Reflection at a rigid boundary vs an open (free) boundary?', T('Rigid') + ': phase change of ' + N('π') + ' (pulse inverted). ' + T('Free') + ': no phase change', **fig('fig_14_11_reflection'))
d.basic('Why is a pulse inverted at a rigid wall?', 'The end cannot move, so incident + reflected must cancel there; also the wall pulls back on the string (third law)')
d.basic('Correction: NCERT Eqs. (14.35)–(14.36) write the reflected wave as a sin(kx − ωt ± …). What is right?', 'A reflected wave travels the ' + T('other way') + ': ' + r'\( y_r = -a\sin(kx + \omega t) \)' + ' (rigid) or ' + r'\( +a\sin(kx + \omega t) \)' + ' (open), as NCERT’s own summary states')
d.basic('Examples of rigid and open reflection?', 'Rigid: echo, string tied to a wall. Open: string on a freely sliding ring, open end of an organ pipe')

d.sec('14.6.1-standing-waves')
d.basic('Equation of a stationary wave?', r'\( y = 2a\sin kx\,\cos\omega t \)' + ': kx and ωt appear ' + T('separately'), **fig('fig_14_12_stationary'))
sp.standing_wave_string(d)
d.basic('Positions of nodes and antinodes?', 'Nodes: ' + r'\( x = \dfrac{n\lambda}{2} \)' + '; antinodes: ' + r'\( x = \left(n + \tfrac12\right)\dfrac{\lambda}{2} \)' + '; each set is λ/2 apart')
table_card(d, 'Points to ponder', 'Same or different for all particles?', [
    ('Progressive wave: amplitude', 'same', False), ('Progressive wave: phase', 'different', True),
    ('Stationary wave: amplitude', 'different (0 at nodes)', True), ('Stationary wave: phase (within a loop)', 'same', False)], term='Progressive vs stationary waves')
d.basic('String of length L fixed at both ends: allowed wavelengths and frequencies?', r'\( \lambda_n = \dfrac{2L}{n},\quad \nu_n = \dfrac{nv}{2L} \)' + ', n = 1, 2, 3… (all harmonics)', **fig('fig_14_13_string_harmonics'))
d.basic('Fundamental of a string fixed at both ends?', r'\( \nu_1 = \dfrac{v}{2L} = \dfrac{1}{2L}\sqrt{\dfrac T\mu} \)')
d.basic('Why do a violin and a sitar playing the same note sound different?', 'They excite different mixtures of ' + T('harmonics') + ' (timbre / quality)')
d.basic('Pipe closed at one end: allowed frequencies?', r'\( \nu = \left(n + \tfrac12\right)\dfrac{v}{2L} \)' + ': fundamental ' + r'\( \dfrac{v}{4L} \)' + ', then ' + T('only odd harmonics') + ' (3, 5, 7…)', **fig('fig_14_14a_closed_pipe'))
d.basic('Identify the higher modes of a closed pipe.', 'Seventh, ninth, eleventh harmonics: still only odd multiples, closed end a node, open end an antinode', **img('fig_14_14b_closed_pipe'))
d.basic('Pipe open at both ends: allowed frequencies?', r'\( \nu_n = \dfrac{nv}{2L} \)' + ': ' + T('all harmonics') + '; both ends antinodes', **fig('fig_14_15_open_pipe'))
d.basic('Mnemonic for pipes?', '"' + T('Closed is Odd') + '": closed pipe → v/4L and odd harmonics; open pipe and string → v/2L and all harmonics')
d.basic('In a sound wave, why is a displacement node a pressure antinode?', 'Where air cannot move, neighbouring layers push in and pull away → ' + T('largest pressure change') + ' (Exercise 14.19a)')
d.basic('Example 14.5: 30.0 cm pipe open at both ends, source 1.1 kHz (v = 330 m/s). Which mode? And with one end closed?', 'Open: νₙ = 550n → ' + T('2nd harmonic') + '. Closed: 275 Hz × odd only; 1.1 kHz = 4th → ' + X('no resonance'))
d.basic('What is resonance for strings and pipes?', 'Large response when a driving frequency matches a ' + T('natural (normal-mode) frequency'))
d.basic('Exercise 14.11: y = 0.06 sin(2πx/3) cos(120πt), 1.5 m, 30 g string. λ, ν, v of the component waves and the tension?', 'λ = ' + N('3 m') + ', ν = ' + N('60 Hz') + ', v = ' + N('180 m/s') + '; T = μv² = ' + N('648 N'))
d.basic('Exercise 14.12: on that string, do all points have the same frequency, phase, amplitude? Amplitude at 0.375 m?', 'Same frequency and phase (except nodes), different amplitudes; at 0.375 m: 0.06 sin(π/4) ≈ ' + N('0.042 m'))
d.basic('Correction: NCERT Exercise 14.12 refers to "Exercise 15.11". Which one?', T('Exercise 14.11'))
d.basic('Exercise 14.14: wire in its fundamental at 45 Hz, mass 3.5 × 10⁻² kg, μ = 4.0 × 10⁻² kg/m. Speed and tension?', 'L = 0.875 m → v = 2Lν ≈ ' + N('79 m/s') + '; T = μv² ≈ ' + N('248 N'))
d.basic('Exercise 14.15: resonance tube with a 340 Hz fork resonates at 25.5 cm. Speed of sound?', 'L = λ/4 → λ = 1.02 m → v ≈ ' + N('347 m/s'))
d.basic('Exercise 14.16: 100 cm steel rod clamped at the middle; fundamental 2.53 kHz. Speed of sound in steel?', 'Ends are antinodes, middle a node: L = λ/2 → v = 2 × 2530 = ' + N('5.06 km/s'))
d.basic('Exercise 14.17: 20 cm pipe closed at one end, 430 Hz source (v = 340 m/s). Which mode? Open at both ends?', 'Fundamental (340/0.8 ≈ 425 Hz); with both ends open (850 Hz) ' + X('no resonance'))

# ---------------------------------------------------------------- 14.7 Beats
d.sec('14.7-beats')
d.basic('What are beats?', 'Periodic ' + T('waxing and waning of loudness') + ' when two sounds of slightly different frequencies are heard together', **fig('fig_14_16_beats'))
d.basic('Beat frequency?', r'\( \nu_{beat} = |\nu_1 - \nu_2| \)')
d.basic('Resultant of two nearly equal frequencies?', r'\( s = [2a\cos\omega_b t]\cos\omega_a t \)' + ': oscillates at the average frequency with a slowly varying amplitude')
d.basic('How do musicians use beats?', 'To ' + T('tune') + ' instruments: adjust until the beats disappear')
d.basic('Example 14.6: A (427 Hz) and B give 5 beats/s; tightening B reduces beats to 3/s. Original frequency of B?', 'Tightening raises ν_B and beats fall, so ν_B < ν_A: '.replace('ν_B', 'νB').replace('ν_A', 'νA') + N('422 Hz'))
d.basic('Exercise 14.18: A (324 Hz) and B give 6 beats/s; loosening A reduces beats to 3/s. Frequency of B?', 'Loosening lowers A and beats fall, so A > B: ' + N('318 Hz'))
d.basic('What are the musical pillars of the Nellaiappar temple?', 'Stone pillars (7th century, Tamil Nadu) that give the ' + T('notes of Indian music') + ' when tapped; their vibrations depend on elasticity, density and shape', **fig('fig_14_pillars'))

# ---------------------------------------------------------------- Exercises / summary
d.sec('exercises')
table_card(d, 'Exercise 14.13', 'Travelling, stationary or none?', [
    ('y = 2 cos(3x) sin(10t)', 'stationary', False), ('(b) the function that blows up at x + vt = 0', 'none: not an acceptable wave', True),
    ('y = 3 sin(5x − 0.5t) + 4 cos(5x − 0.5t)', 'travelling harmonic wave', False), ('y = cos x sin t + cos 2x sin 2t', 'sum of two stationary waves', False)], term='Classify the wave functions (Exercise 14.13)')
d.basic('Exercise 14.19(b): how do bats locate obstacles without eyes?', T('Echolocation') + ': they emit ultrasound and use the delay and change of the reflected waves')
d.basic('Exercise 14.19(e): why does a pulse change shape in a dispersive medium?', 'Its component frequencies travel at ' + T('different speeds'))

d.sec('summary')
table_card(d, 'Summary', 'Formula?', [
    ('Wave speed', 'v = νλ = ω/k', False), ('String', 'v = √(T/μ)', False), ('Sound in a gas', 'v = √(γP/ρ)', False),
    ('String / open pipe', 'νₙ = nv/2L', False), ('Closed pipe', 'ν = (2n + 1)v/4L', False), ('Beats', 'ν₁ − ν₂', False)], term='Chapter 14 formula sheet')

print(d.write(os.path.join(OUT, 'deck.json')), 'cards')
