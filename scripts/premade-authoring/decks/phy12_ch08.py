import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase_phy as sp

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Physics', 'class12-physics-ch08-electromagnetic-waves')
d = Deck('Chapter 8: Electromagnetic Waves', 'Class 12', ['class-12', 'physics', 'ch-8'])
d.description = 'Displacement current, Maxwell’s equations, nature of EM waves, E₀ = cB₀, intensity, and the EM spectrum'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- 8.1 Introduction
d.sec('8.1-introduction')
d.basic('Maxwell’s big idea (the converse of Faraday’s law)?', 'A ' + T('time-varying electric field') + ' also produces a magnetic field (not just a current)')
d.basic('What inconsistency did Maxwell find, and what did he add?', 'Ampere’s circuital law failed for a charging capacitor. He added the ' + T('displacement current') + ' i_d = ε₀ dΦ_E/dt')
d.basic('Most important prediction of Maxwell’s equations?', 'Existence of ' + T('electromagnetic waves') + ' travelling at ≈ ' + N('3 × 10⁸ m/s') + ' = speed of light, so light is an EM wave')
d.basic('Who first demonstrated EM waves experimentally, and who used them for communication?', T('Hertz') + ' demonstrated them; ' + T('Marconi') + ' used them for communication over many km')
d.basic('Correction: NCERT’s introduction gives Hertz’s experiment as 1885, but §8.3 says 1887. Which?', T('1887') + ' is accepted (and asked). Bose’s mm-wave work followed seven years later')
d.basic('What did Maxwell’s work unify?', T('Electricity, magnetism and light'))

# ---------------------------------------------------------------- 8.2 Displacement current
d.sec('8.2-displacement-current')
d.basic('Ampere’s circuital law (before Maxwell)?', r'\( \oint \vec B\cdot d\vec l = \mu_0 i_c \)' + ' (i_c = conduction current through the surface)')
d.basic('Charging capacitor: B at P outside the plates from a circle of radius r?', 'B(2πr) = μ₀i, so ' + r'\( B = \dfrac{\mu_0 i}{2\pi r} \)', **fig('fig_8_1a'))
d.basic('Same loop, but a pot-shaped surface passing between the plates. What does Ampere’s law give?', T('Zero') + ': no conduction current crosses that surface. Contradiction with the flat surface!', **fig('fig_8_1b'))
d.basic('What passes through the surface S between the plates instead?', 'A changing ' + T('electric flux') + ' (E = Q/ε₀A across area A)', **fig('fig_8_1c'))
d.basic('Derive the missing term.', 'Φ_E = Q/ε₀ so ' + r'\( \varepsilon_0\dfrac{d\Phi_E}{dt} = \dfrac{dQ}{dt} = i \)' + '. This equals the conduction current outside, closing the gap')
d.basic('Define displacement current.', r'\( i_d = \varepsilon_0\dfrac{d\Phi_E}{dt} \)' + ': the current “due to” a changing electric flux; same magnetic effect as i_c')
d.basic('Ampere–Maxwell law?', r'\( \oint \vec B\cdot d\vec l = \mu_0\left(i_c + \varepsilon_0\dfrac{d\Phi_E}{dt}\right) \)')
d.basic('Outside vs inside a charging capacitor: which currents exist?', 'Outside: only i_c (i_d = 0). Between plates: only ' + T('i_d') + ' (i_c = 0). In both, the total current is the same, i')
d.basic('Displacement current in a capacitor in terms of C and V?', r'\( i_d = \varepsilon_0 A\dfrac{dE}{dt} = C\dfrac{dV}{dt} \)' + ' (a fast way to answer numericals)')
d.basic('Is B between the capacitor plates zero? How is it checked?', X('No') + ': B measured at M between the plates equals that just outside at P; the field lines are circles about the axis (Fig. 8.2)', **fig('fig_8_2a'))
d.basic('Direction relation of E and B between the plates?', 'E ⊥ plates; B circles about the axis, ' + T('perpendicular to E') + ' — a hint that E ⟂ B in a wave', **fig('fig_8_2b'))
d.basic('Teacher addition: B at distance r from the axis between circular plates of radius R (r < R)?', r'\( B = \dfrac{\mu_0 r}{2\pi R^2}\,i_d \)' + ' (uniform i_d over the plate area). Outside (r > R): ' + r'\( \dfrac{\mu_0 i_d}{2\pi r} \)')
d.basic('Do steady currents have displacement current?', T('Zero') + ': E in a wire does not change with time, so i_d = 0')
d.basic('Symmetry made by displacement current?', 'Changing B → E (Faraday); changing E → B (Maxwell). They are still not fully symmetric: no ' + T('magnetic monopoles'))
d.basic('Exam trap: charging capacitor, conduction vs displacement current in the wire and gap?', 'Wire: i_c = i, i_d = 0. Gap: i_c = 0, i_d = i at every instant. Kirchhoff’s junction rule holds for the ' + T('total') + ' current')

d.sec('8.2-maxwells-equations')
d.basic('Gauss’s law for electricity (Maxwell equation 1)?', r'\( \oint \vec E\cdot d\vec A = \dfrac{Q}{\varepsilon_0} \)' + ': charges are sources of E')
d.basic('Gauss’s law for magnetism (equation 2)?', r'\( \oint \vec B\cdot d\vec A = 0 \)' + ': no magnetic monopoles')
d.basic('Faraday’s law (equation 3)?', r'\( \oint \vec E\cdot d\vec l = -\dfrac{d\Phi_B}{dt} \)' + ': changing B produces E')
d.basic('Ampere–Maxwell law (equation 4)?', r'\( \oint \vec B\cdot d\vec l = \mu_0 i_c + \mu_0\varepsilon_0\dfrac{d\Phi_E}{dt} \)')
d.basic('Mnemonic: sort Maxwell’s four equations by what they say.', T('1 & 2') + ': sources (charge yes, monopole no). ' + T('3 & 4') + ': changing B makes E, changing E (or current) makes B. Together with the Lorentz force they give all of electromagnetism')
d.basic('Which of Maxwell’s equations did Maxwell himself add?', 'The ' + T('displacement-current term') + ' in equation 4 (the other three were known)')

# ---------------------------------------------------------------- 8.3 EM waves
d.sec('8.3-electromagnetic-waves')
d.basic('Which charges radiate electromagnetic waves?', T('Accelerated') + ' charges. Stationary charges give only E; steady currents give only steady B')
d.basic('How does an oscillating charge produce a wave?', 'Oscillating E → oscillating B → oscillating E … each regenerates the other as the wave moves out; energy comes from the ' + T('source charge'))
d.basic('Frequency of the wave from a charge oscillating at ν?', 'The same ' + T('ν'))
d.basic('Basic source of EM waves?', 'An oscillating ' + T('electric dipole') + ' (accelerating charge)')
d.basic('Why did Hertz’s test have to be in the radio range, not visible light?', 'Yellow light is ≈ ' + N('6 × 10¹⁴ Hz') + ' but circuits reach only ≈ ' + N('10¹¹ Hz'))
d.basic('Contribution of J. C. Bose?', 'In Calcutta he produced and observed EM waves of ' + T('25 mm to 5 mm') + ' wavelength (seven years after Hertz)')
d.basic('Contribution of Marconi?', 'Transmitted EM waves over ' + T('many kilometres') + ': beginning of wireless communication')
d.basic('Nature of the E and B fields in an EM wave?', T('Perpendicular to each other and to the direction of propagation') + ' (transverse wave); E × B is along the direction of travel', **fig('fig_8_3_wave'))
sp.em_wave_travelling(d)
d.basic('Equations of a plane EM wave travelling along +z (E along x)?', r'\( E_x = E_0\sin(kz-\omega t),\quad B_y = B_0\sin(kz-\omega t) \)')
d.basic('Wave number and speed?', r'\( k = \dfrac{2\pi}{\lambda},\quad v = \dfrac{\omega}{k} = \nu\lambda \)')
d.basic('Speed of EM waves in vacuum in terms of ε₀ and μ₀?', r'\( c = \dfrac{1}{\sqrt{\mu_0\varepsilon_0}} \)' + ' = 3 × 10⁸ m/s')
d.basic('Relation between E₀ and B₀?', r'\( B_0 = \dfrac{E_0}{c} \)' + ' (E and B are in phase)')
d.basic('Why is E ≫ B numerically in an EM wave (in SI)?', 'E₀ = cB₀ with c = 3 × 10⁸: e.g. E₀ = 60 V/m goes with B₀ = 2 × 10⁻⁷ T')
d.basic('Speed of light in a medium (ε, μ)?', r'\( v = \dfrac{1}{\sqrt{\mu\varepsilon}} \)' + ', so refractive index ' + r'\( n = \dfrac{c}{v} = \sqrt{\mu_r\varepsilon_r} \)')
d.basic('Do EM waves need a medium?', X('No') + ': self-sustaining oscillating fields in vacuum, unlike sound or water waves')
d.basic('Does the speed of EM waves in vacuum depend on wavelength?', X('No') + ': radio waves, light and X-rays all travel at c; this constancy is used to define the standard of length (the metre)')
d.basic('What do EM waves carry?', T('Energy') + ' (sunlight, radio, TV signals) and momentum')
d.basic('Teacher addition: energy density of an EM wave, and how E and B contribute?', r'\( u = \tfrac12\varepsilon_0E^2 + \dfrac{B^2}{2\mu_0} \)' + '; the two halves are ' + T('equal') + ' (B = E/c and c² = 1/μ₀ε₀), so u = ε₀E²')
d.basic('Teacher addition: intensity of an EM wave (average energy per unit area per second)?', r'\( I = \tfrac12\varepsilon_0cE_0^2 = \dfrac{cB_0^2}{2\mu_0} = u_{av}\,c \)')
d.basic('Teacher addition: radiation pressure on a perfectly absorbing and a perfectly reflecting surface?', 'Absorbing: ' + r'\( p = \dfrac{I}{c} \)' + '. Reflecting: ' + r'\( \dfrac{2I}{c} \)' + '. Momentum carried by energy U is U/c')
d.basic('Teacher addition: how does the intensity of a point source fall with distance?', T('I ∝ 1/r²') + ', so E₀ and B₀ ∝ 1/r')
d.basic('Example 8.1: 25 MHz wave along x, E = 6.3 ĵ V/m. B?', 'B = E/c = ' + N('2.1 × 10⁻⁸ T') + '; E × B along x with E along y means B along ' + T('+z') + ': B = 2.1 × 10⁻⁸ k̂ T')
d.basic('Trick for the direction of B?', 'Direction of travel = ' + T('E × B') + '. Use right-hand rule: x̂ × ŷ = ẑ, ŷ × ẑ = x̂, ẑ × x̂ = ŷ')
steps_card(d, 'Example 8.2 · read off a wave equation', 'Find the missing step.', 'B_y = (2 × 10⁻⁷ T) sin(0.5 × 10³ x + 1.5 × 10¹¹ t). Find λ, ν and the E-field expression.',
           ['k = 0.5 × 10³ m⁻¹ → λ = 2π/k = <b>1.26 cm</b>', 'ω = 1.5 × 10¹¹ → ν = ω/2π = <b>23.9 GHz</b>', 'E₀ = cB₀ = 3 × 10⁸ × 2 × 10⁻⁷ = <b>60 V/m</b>', '+x in the argument means travel along −x; E ⟂ B and E × B along −x gives <b>E along z</b>: E_z = 60 sin(0.5 × 10³x + 1.5 × 10¹¹t)'], 2,
           'Compare with B = B₀ sin(kx + ωt) (Example 8.2)', 'λ = 1.26 cm, ν = 23.9 GHz, E_z = 60 sin(0.5 × 10³x + 1.5 × 10¹¹t) V/m')
d.basic('Exam trap: sign in sin(kx − ωt) vs sin(kx + ωt)?', T('kx − ωt') + ' → wave travels along ' + T('+x') + '. ' + T('kx + ωt') + ' → along ' + T('−x'))
d.basic('Exam question: which of E, B, direction of travel is fixed if two are known?', 'The third: E × B = direction of propagation, so any two determine the third (sign included)')

# ---------------------------------------------------------------- 8.4 Spectrum
d.sec('8.4-electromagnetic-spectrum')
d.basic('What is the electromagnetic spectrum? Sharp boundaries?', 'Classification of EM waves by frequency or wavelength; ' + X('no sharp boundaries') + ', regions overlap and depend on production/detection')
d.basic('Order of EM waves from longest to shortest wavelength?', T('Radio') + ' > ' + T('microwave') + ' > ' + T('infrared') + ' > ' + T('visible') + ' > ' + T('ultraviolet') + ' > ' + T('X-ray') + ' > ' + T('γ-ray'))
d.basic('Mnemonic for the order (increasing frequency)?', '“' + T('R') + 'abbits ' + T('M') + 'ate ' + T('I') + 'n ' + T('V') + 'ery ' + T('U') + 'seful ' + T('X') + '-tra ' + T('G') + 'ardens”: Radio, Microwave, IR, Visible, UV, X-ray, Gamma')
d.occlusion('Figure 8.4 · The EM spectrum', M + 'fig_8_4_spectrum.webp', (1001, 918), [
    ('Gamma rays', [205, 132, 152, 30], True), ('X-rays', [245, 224, 85, 30], True), ('Ultraviolet', [230, 316, 125, 30], True),
    ('Visible', [250, 381, 82, 26], True), ('Infrared', [238, 428, 97, 30], True), ('Microwaves', [218, 516, 136, 30], True),
    ('Short radio waves', [188, 565, 204, 30], True), ('Television and FM radio', [156, 620, 270, 30], True),
    ('AM radio', [236, 678, 108, 30], True), ('Long radio waves', [190, 768, 196, 30], True)], guess='hide-all')
d.occlusion('Figure 8.4 · Colours of visible light', M + 'fig_8_4_spectrum.webp', (1001, 918), [
    ('Violet', [916, 141, 75, 30], True), ('Blue', [916, 258, 60, 30], True), ('Green', [916, 378, 75, 30], True),
    ('Yellow', [916, 520, 80, 30], True), ('Orange', [916, 610, 90, 30], True), ('Red', [916, 726, 55, 30], True)], guess='hide-all')
d.basic('Visible light: wavelength and frequency range?', T('400–700 nm') + ' (violet → red); ≈ ' + N('4 × 10¹⁴ to 7 × 10¹⁴ Hz'))
d.basic('Mnemonic for colours of light, short λ to long λ?', '“' + T('VIBGYOR') + '”: Violet, Indigo, Blue, Green, Yellow, Orange, Red (violet has the highest frequency and energy)')
d.basic('Quick photon-energy rule of thumb, from E = hc/λ?', 'E (eV) ≈ 1240 / λ (nm): 500 nm light ≈ 2.5 eV; higher frequency → higher photon energy')

d.sec('8.4.1-radio-waves')
d.basic('How are radio waves produced?', T('Accelerated motion of charges in conducting wires') + ' (aerials)')
d.basic('Frequency range of radio waves; AM and FM bands?', '≈ 500 kHz to 1000 MHz. AM: ' + N('530–1710 kHz') + '; FM: ' + N('88–108 MHz') + '; TV: 54–890 MHz')
d.basic('Radio waves used in cellular phones?', T('UHF') + ' (ultrahigh frequency) band')

d.sec('8.4.2-microwaves')
d.basic('How are microwaves produced?', 'Special vacuum tubes: ' + T('klystron, magnetron') + ' or ' + T('Gunn diode'))
d.basic('Uses of microwaves?', T('Radar') + ' (aircraft navigation, speed guns for cricket balls and cars), ' + T('microwave ovens'))
d.basic('Why can radar use microwaves rather than long radio waves?', 'Short wavelengths give ' + T('narrow, well-defined beams') + ' and reflect well from small objects')
d.basic('How does a microwave oven heat food? NCERT’s explanation and the correction.', 'NCERT: frequency matches the resonant frequency of water molecules. ' + X('Correction:') + ' ovens use ≈ ' + N('2.45 GHz') + ', well below water’s molecular resonance; the rapidly reversing E-field ' + T('rotates polar water molecules') + ' and the friction heats the food. Exams still write NCERT’s line')

d.sec('8.4.3-infrared-waves')
d.basic('How are infrared waves produced? Detected?', 'Produced by ' + T('hot bodies and vibrating molecules') + '. Detected by thermopiles, bolometers, IR film')
d.basic('Why are infrared waves called “heat waves”?', 'Water and CO₂, NH₃ etc. ' + T('absorb IR readily') + ', raising molecular thermal motion and temperature')
d.basic('Role of infrared in the greenhouse effect?', 'Earth absorbs visible light and re-radiates ' + T('longer-wavelength IR') + ', which is trapped by CO₂ and water vapour, keeping Earth warm')
d.basic('Uses of infrared?', 'Physical therapy lamps, satellite crop monitoring, ' + T('remote controls') + ' (IR LEDs), night vision')
d.basic('Which animals see IR or UV?', 'Snakes detect ' + T('infrared') + '; many insects see into the ' + T('ultraviolet'))

d.sec('8.4.5-ultraviolet-rays')
d.basic('Wavelength range and sources of UV?', '≈ 400 nm down to 0.6 nm (NCERT text). Sources: special lamps, very hot bodies, the ' + T('Sun'))
d.basic('What absorbs the Sun’s harmful UV, and where?', 'The ' + T('ozone layer') + ' at ≈ 40–50 km altitude; depleted by ' + T('CFCs') + ' (freon)')
d.basic('Why can’t you tan through a glass window?', T('Ordinary glass absorbs UV'))
d.basic('Uses of UV?', 'Water purifiers (kill germs), ' + T('LASIK') + ' eye surgery (short λ focuses to fine beams), welders’ goggles guard against it')
d.basic('Effect of UV on skin?', 'Induces more ' + T('melanin') + ' (tanning); large doses are harmful')

d.sec('8.4.6-x-rays-and-gamma-rays')
d.basic('How are X-rays generated? Uses?', 'By bombarding a ' + T('metal target with high-energy electrons') + '. Medical diagnosis and cancer treatment; overexposure damages tissue')
d.basic('X-ray wavelength range?', '≈ 10 nm to 10⁻⁴ nm (NCERT text); Table 8.1 says 1 nm to 10⁻³ nm')
d.basic('Source and use of gamma rays?', 'Nuclear reactions and ' + T('radioactive nuclei') + '; used to destroy cancer cells')
d.basic('Note: NCERT’s wavelength ranges differ between text and Table 8.1. Which do exams use?', 'Ranges overlap (UV/X-ray, X-ray/γ). Learn the ' + T('table') + ': radio > 0.1 m; microwave 0.1 m–1 mm; IR 1 mm–700 nm; light 700–400 nm; UV 400–1 nm; X-ray 1 nm–10⁻³ nm; γ < 10⁻³ nm')
table_card(d, 'Table 8.1', 'How produced?', [
    ('Radio', 'Rapid acceleration/deceleration of electrons in aerials', False), ('Microwave', 'Klystron or magnetron valve', False),
    ('Infrared', 'Vibration of atoms and molecules', False), ('Visible light', 'Electrons in atoms dropping to lower energy levels', False),
    ('Ultraviolet', 'Inner-shell electrons moving to lower levels', False), ('X-rays', 'X-ray tubes or inner-shell electrons', False),
    ('Gamma rays', 'Radioactive decay of the nucleus', False)],
    term='Table 8.1 · Production of EM waves')
table_card(d, 'Table 8.1', 'How detected?', [
    ('Radio', 'Receiver’s aerials', False), ('Microwave', 'Point-contact diodes', False), ('Infrared', 'Thermopiles, bolometer, IR film', False),
    ('Visible light', 'The eye, photocells, photographic film', False), ('Ultraviolet', 'Photocells, photographic film', False),
    ('X-rays', 'Photographic film, Geiger tube, ionisation chamber', False), ('Gamma rays', 'Same as X-rays', False)],
    term='Table 8.1 · Detection of EM waves')
d.basic('Exam trick: which EM wave has the maximum penetrating power? The highest photon energy?', T('Gamma rays') + ' for both (highest frequency, smallest λ)')
d.basic('Exam trick: which of these are not EM waves: γ-rays, X-rays, cathode rays, β-rays, sound?', X('Cathode rays, β-rays') + ' (electrons) and ' + X('sound') + ' (mechanical). γ- and X-rays are EM')
d.basic('Exam trick: Do EM waves get deflected in electric or magnetic fields?', X('No') + ': they carry no charge (fields of the wave itself are oscillating, not static)')

# ---------------------------------------------------------------- Points to ponder
d.sec('points-to-ponder')
d.basic('What is different between various EM waves, and what is the same?', 'Same: speed c in vacuum. Different: ' + T('wavelength/frequency') + ', hence how they interact with matter')
d.basic('What sets the wavelength of radiation from a system?', 'Roughly the ' + T('size of the source') + ': γ from nuclei (10⁻¹⁴ m), X-rays from heavy atoms, radio from circuits. An antenna radiates best when its size ≈ λ')
d.basic('Why do our eyes peak in the visible region?', 'Human vision evolved to be most sensitive to the ' + T('strongest wavelengths of sunlight'))

# ---------------------------------------------------------------- Exercises
d.sec('exercises')
steps_card(d, 'Exercise 8.1 · charging capacitor', 'Find the missing step.', 'Circular plates of radius 12 cm, gap 5.0 cm, charging current 0.15 A. (a) C and dV/dt (b) i_d (c) Kirchhoff’s rule?',
           ['C = ε₀A/d = 8.85 × 10⁻¹² × π(0.12)²/0.05 ≈ <b>80 pF</b>', 'i = C dV/dt → dV/dt = 0.15/(80 × 10⁻¹²) ≈ <b>1.9 × 10⁹ V/s</b>', 'i_d = i_c = <b>0.15 A</b> (between plates)', 'Kirchhoff’s junction rule holds at each plate <b>if displacement current is counted</b> as part of the total current'], 1,
           'Constant charging current (Exercise 8.1)', 'C ≈ 80 pF, dV/dt ≈ 1.9 × 10⁹ V/s, i_d = 0.15 A, rule valid with i_d included')
d.basic('Check: dV/dt in Exercise 8.1, with C = 80.1 pF?', '0.15/(80.1 × 10⁻¹²) = ' + N('1.87 × 10⁹ V/s') + '', **img('fig_8_5_capacitor'))
steps_card(d, 'Exercise 8.2 · capacitor on ac', 'Find the missing step.', 'Circular plates R = 6.0 cm, C = 100 pF, 230 V ac, ω = 300 rad/s. (a) rms conduction current (b) i_c = i_d? (c) amplitude of B at 3.0 cm from the axis.',
           ['I_rms = V/X_C = VωC = 230 × 300 × 100 × 10⁻¹² = <b>6.9 μA</b>', 'Yes: <b>i_c = i_d</b> at every instant in the wire and between the plates', 'Peak current I₀ = √2 × 6.9 μA = 9.76 μA', 'B = μ₀rI₀/(2πR²) = 2 × 10⁻⁷ × 0.03 × 9.76 × 10⁻⁶/(0.06)² ≈ <b>1.63 × 10⁻¹¹ T</b>'], 3,
           'Displacement current on ac (Exercise 8.2)', 'I_rms = 6.9 μA, i_c = i_d, B₀ ≈ 1.63 × 10⁻¹¹ T')
d.basic('Exercise 8.3: what physical quantity is the same for X-rays (10⁻¹⁰ m), red light (6800 Å) and radio waves (500 m)?', T('Speed') + ' in vacuum (3 × 10⁸ m/s), and they are all transverse EM waves')
d.basic('Exercise 8.4: EM wave along z in vacuum. Directions of E and B? λ at 30 MHz?', 'E and B lie in the ' + T('xy-plane') + ', perpendicular to each other. λ = c/ν = 3 × 10⁸/30 × 10⁶ = ' + N('10 m'))
d.basic('Exercise 8.5: radio tunes 7.5 MHz to 12 MHz. Wavelength band?', 'λ = c/ν: ' + N('40 m') + ' (7.5 MHz) to ' + N('25 m') + ' (12 MHz); band 25–40 m')
d.basic('Exercise 8.6: charge oscillating at 10⁹ Hz. Frequency of the EM wave?', N('10⁹ Hz') + ': same as the oscillation')
d.basic('Exercise 8.7: B₀ = 510 nT. E₀?', 'E₀ = cB₀ = 3 × 10⁸ × 510 × 10⁻⁹ = ' + N('153 N/C'))
steps_card(d, 'Exercise 8.8 · full wave description', 'Find the missing step.', 'E₀ = 120 N/C, ν = 50.0 MHz. Find B₀, ω, k, λ and write E and B.',
           ['B₀ = E₀/c = 120/(3 × 10⁸) = <b>4 × 10⁻⁷ T</b>', 'ω = 2πν = <b>3.14 × 10⁸ rad/s</b>', 'k = ω/c = <b>1.05 rad/m</b>; λ = c/ν = <b>6.0 m</b>', 'E = 120 sin(1.05z − 3.14 × 10⁸t) N/C (x-direction); B = 4 × 10⁻⁷ sin(1.05z − 3.14 × 10⁸t) T (y-direction)'], 2,
           'Complete EM wave from E₀ and ν (Exercise 8.8)', 'B₀ = 400 nT, ω = 3.14 × 10⁸, k = 1.05, λ = 6 m')
table_card(d, 'Exercise 8.9', 'Photon energy E = hν = 1240/λ(nm) eV?', [
    ('γ-rays (λ ~ 10⁻¹² m)', '~ 10⁶ eV (MeV): nuclear energy scale', False), ('X-rays (~ 1 nm)', '~ 10³ eV (keV): inner-shell electrons', False),
    ('Ultraviolet (~ 100 nm)', '~ 10 eV: outer-electron transitions', False), ('Visible (~ 500 nm)', '~ 2.5 eV: outer-electron transitions', False),
    ('Infrared (~ 10 μm)', '~ 0.1 eV: molecular vibrations', False), ('Microwave (~ 1 cm)', '~ 10⁻⁴ eV: molecular rotations, klystron', False),
    ('Radio (~ 100 m)', '~ 10⁻⁸ eV: oscillating circuits', False)],
    term='Exercise 8.9 · Photon energy scale of the spectrum')
d.basic('Exercise 8.9: what do the photon-energy scales tell you about the sources?', 'They match the energy scales of the processes: ' + T('nuclear (MeV) → inner shell (keV) → outer electrons (eV) → molecules (< eV) → circuits (tiny)') + ', in line with Table 8.1')
steps_card(d, 'Exercise 8.10 · wave of 20 GHz', 'Find the missing step.', 'ν = 2.0 × 10¹⁰ Hz, E₀ = 48 V/m. (a) λ (b) B₀ (c) show u_E = u_B on average.',
           ['λ = c/ν = 3 × 10⁸/2 × 10¹⁰ = <b>1.5 cm</b>', 'B₀ = E₀/c = 48/3 × 10⁸ = <b>1.6 × 10⁻⁷ T</b>', 'u_E = ¼ε₀E₀²; u_B = B₀²/4μ₀ = E₀²/(4μ₀c²)', 'c² = 1/μ₀ε₀ → u_B = ¼ε₀E₀² = <b>u_E</b> ✓'], 3,
           'Equal E and B energy densities (Exercise 8.10)', 'λ = 1.5 cm, B₀ = 1.6 × 10⁻⁷ T, u_E = u_B')

# ---------------------------------------------------------------- Summary
d.sec('summary')
table_card(d, 'Summary', 'Formula?', [
    ('Displacement current', 'i_d = ε₀ dΦ_E/dt', False), ('Ampere–Maxwell law', '∮B·dl = μ₀(i_c + i_d)', False), ('Speed of EM waves', 'c = 1/√(μ₀ε₀)', False),
    ('Relation of fields', 'E₀/B₀ = c', False), ('Wave relation', 'c = νλ', False), ('Speed in a medium', 'v = 1/√(με)', False),
    ('Refractive index', 'n = c/v = √(μᵣεᵣ)', False), ('Intensity (teacher addition)', 'I = ½ε₀cE₀²', False)],
    term='Chapter 8 formula sheet')
table_card(d, 'Concept checks', 'True or false?', [
    ('A steady current radiates EM waves', 'False (accelerated charges do)', True), ('E and B in an EM wave are in phase', 'True', False),
    ('EM waves need a material medium', 'False', True), ('Gamma rays have the longest wavelength in the spectrum', 'False (shortest)', True),
    ('Displacement current exists between capacitor plates', 'True', False), ('E and B of an EM wave are parallel', 'False (perpendicular)', True)],
    term='Chapter 8 concept checks')

print(d.write(os.path.join(OUT, 'deck.json')), 'cards')
