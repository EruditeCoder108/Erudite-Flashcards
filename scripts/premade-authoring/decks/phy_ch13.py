import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase_phy as sp

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Physics', 'class11-physics-ch13-oscillations')
d = Deck('Chapter 13: Oscillations', 'Class 11', ['class-11', 'physics', 'ch-13'])
d.description = 'Periodic and oscillatory motion, SHM, phase, reference circle, velocity and acceleration, force law, energy, spring systems, simple pendulum'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- 13.2 Periodic and oscillatory
d.sec('13.2-periodic-and-oscillatory')
d.basic('Periodic vs oscillatory motion?', T('Periodic') + ': repeats at regular intervals<br>' + T('Oscillatory') + ': periodic to-and-fro motion about a mean (equilibrium) position', **fig('fig_13_1_periodic'))
d.basic('Is every periodic motion oscillatory?', X('No') + ': every oscillation is periodic, but ' + E('uniform circular motion') + ' is periodic without being oscillatory')
d.basic('Oscillation vs vibration?', 'No real difference.<br>Low frequency is usually called ' + T('oscillation') + ' (tree branch)<br>High frequency is called ' + T('vibration') + ' (guitar string)')
d.basic('Why do real oscillations die out? How can they be kept going?', T('Damping') + ' (friction, dissipation); an external periodic force can keep them going (forced oscillations)')
d.basic('How are waves related to oscillations?', 'A medium is a collection of coupled oscillators; their ' + T('collective oscillations') + ' are waves')
d.basic('Define period and frequency. Unit of frequency?', T('Period') + ' T: smallest interval after which motion repeats. ' + T('Frequency') + ' ν = 1/T, in ' + N('hertz') + ' (1 Hz = 1 s⁻¹)')
d.basic('Example 13.1: heart beats 75 times a minute. Frequency and period?', N('1.25 Hz') + ', ' + N('0.8 s'))
d.basic('What does "displacement" mean in oscillations?', 'Change with time of ' + T('any physical quantity') + ': position, angle of a pendulum, capacitor voltage, air pressure in sound…', **fig('fig_13_2b_pendulum'))
d.basic('Fourier’s theorem?', 'Any periodic function can be written as a ' + T('superposition of sines and cosines') + ' of different periods')
d.basic('Show that A sin ωt + B cos ωt is simple harmonic.', 'It equals ' + r'\( D\sin(\omega t + \phi) \)' + ' with ' + r'\( D = \sqrt{A^2 + B^2},\ \tan\phi = B/A \)')
table_card(d, 'Example 13.2 / Exercise 13.4', 'Type of motion?', [
    ('sin ωt + cos ωt', 'SHM, T = 2π/ω', False), ('sin ωt + cos 2ωt + sin 4ωt', 'periodic, not SHM; T = 2π/ω', False),
    ('3 cos(π/4 − 2ωt)', 'SHM, T = π/ω', False), ('cos ωt + cos 3ωt + cos 5ωt', 'periodic, not SHM; T = 2π/ω', False),
    ('e^(−ωt), log ωt, 1 + ωt + ω²t²', 'non-periodic', True)], term='Is it SHM, periodic, or neither?')
d.basic('Example 13.3: is sin²ωt simple harmonic?', 'sin²ωt = ½ − ½ cos 2ωt: harmonic with period ' + N('π/ω') + ', but about the mean value ½, not 0')
d.basic('Exercise 13.4(b): is sin³ωt simple harmonic?', X('No') + ': sin³ωt = (3 sin ωt − sin 3ωt)/4, periodic (T = 2π/ω) but not SHM')

# ---------------------------------------------------------------- 13.3 SHM
d.sec('13.3-simple-harmonic-motion')
d.basic('Define simple harmonic motion.', 'Motion in which displacement is a ' + T('sinusoidal function of time') + ': ' + r'\( x(t) = A\cos(\omega t + \phi) \)', **fig('fig_13_5_x_vs_t'))
table_card(d, 'Fig. 13.6 · symbols of SHM', 'Name?', [
    ('A', 'amplitude (maximum displacement)', False), ('ω', 'angular frequency (rad/s)', False),
    ('ωt + φ', 'phase (time-dependent)', False), ('φ', 'phase constant (phase at t = 0)', False)], term='Meaning of symbols in x = A cos(ωt + φ)')
d.basic('Identify: where is the particle and how fast at t = 0, T/4, T/2, 3T/4?', 'At +A (rest), 0 (vₘₐₓ, moving to −A), −A (rest), 0 (vₘₐₓ, moving to +A)', **img('fig_13_4_positions'))
d.basic('Relation between ω, T and ν?', r'\( \omega = \dfrac{2\pi}{T} = 2\pi\nu \)', **fig('fig_13_8_two_periods'))
d.basic('What does the phase tell you?', 'The ' + T('state of motion') + ' (position and velocity) at time t')
d.basic('How many initial conditions fix a given SHM (known ω)?', N('Two') + ': e.g. initial position and velocity, or amplitude and phase')
d.basic('Does the period of SHM depend on amplitude?', X('No') + ': T is independent of amplitude, energy and phase (unlike planetary orbits)')
d.basic('Exercise 13.7: x(0) = 1 cm, v(0) = ω cm/s, ω = π s⁻¹. Amplitude and phase for x = A cos(ωt + φ)?', 'A = ' + N('√2 cm') + ', φ = ' + N('−π/4 (= 7π/4)') + '. With sine: B = √2 cm, α = π/4')

# ---------------------------------------------------------------- 13.4 Reference circle
d.sec('13.4-shm-and-circular-motion')
sp.shm_reference_circle(d)
d.basic('How is SHM related to uniform circular motion?', 'The ' + T('projection') + ' of uniform circular motion on any diameter is SHM (reference circle, reference particle)', **fig('fig_13_10_reference_circle'))
d.basic('A ball whirled in a horizontal circle, seen edge-on: what motion do you see?', 'To-and-fro ' + T('SHM') + ' along a line', **fig('fig_13_9_ball_circle'))
d.basic('Projections on the x- and y-axes: how do they differ?', 'Same amplitude and ω, but differ in phase by ' + N('π/2') + ' (cos vs sin)')
d.basic('Is the restoring force in SHM the same as the centripetal force of the reference circle?', X('No') + ': they are very different forces; only the projected motion matches')
d.basic('Example 13.4(a): radius A, T = 4 s, starts at 45°, anticlockwise. x(t)?', r'\( x = A\cos\left(\dfrac{\pi}{2}t + \dfrac{\pi}{4}\right) \)')
d.basic('Example 13.4(b): radius B, T = 30 s, starts at 90°, clockwise. x(t)?', r'\( x = B\sin\left(\dfrac{\pi}{15}t\right) = B\cos\left(\dfrac{\pi}{15}t - \dfrac{\pi}{2}\right) \)')
d.basic('Exercise 13.11 (Fig. 13.20): x-projections of the two motions shown?', '(a) ' + N('x = −3 sin πt cm') + '; (b) ' + N('x = −2 cos (πt/2) cm'), **fig('fig_13_20_ex_circles'))

# ---------------------------------------------------------------- 13.5 Velocity and acceleration
d.sec('13.5-velocity-and-acceleration')
d.basic('Velocity in SHM?', r'\( v = -\omega A\sin(\omega t + \phi) \)' + '; in terms of x: ' + r'\( v = \pm\omega\sqrt{A^2 - x^2} \)')
d.basic('Acceleration in SHM?', r'\( a = -\omega^2 A\cos(\omega t + \phi) = -\omega^2 x \)' + ': always towards the mean position', **fig('fig_13_12_acceleration_projection'))
d.basic('Maximum speed and maximum acceleration?', r'\( v_{max} = \omega A \)' + ' at x = 0; ' + r'\( a_{max} = \omega^2 A \)' + ' at x = ±A')
d.basic('Phase relations between x, v and a?', 'v leads x by ' + N('π/2') + '; a is ' + N('π') + ' out of phase with x', **fig('fig_13_13_x_v_a'))
d.basic('Mnemonic: where is each quantity zero or maximum?', '"' + T('Middle: fast, no force') + '; ' + T('ends: still, big force') + '": at x = 0, v max and a = 0; at x = ±A, v = 0 and |a| max')
d.basic('Example 13.5: x = 5 cos(2πt + π/4) m. Displacement, speed and acceleration at t = 1.5 s?', 'x = ' + N('−3.535 m') + '; speed ≈ ' + N('22 m/s') + '; a ≈ ' + N('+140 m/s²'))
table_card(d, 'Exercise 13.5 · signs', 'Signs of v, a (= F)? (A → B positive, 10 cm apart)', [
    ('At end A', 'v = 0, a +', False), ('At end B', 'v = 0, a −', False), ('Mid-point, going to A', 'v −, a = 0', False),
    ('2 cm from B, going to A', 'v −, a −', False), ('3 cm from A, going to B', 'v +, a +', False)], term='Signs of v and a in SHM (Exercise 13.5)')
d.basic('Exercise 13.6: which is SHM: a = 0.7x, a = −200x², a = −10x, a = 100x³?', T('a = −10x') + ' only (a ∝ −x)')

# ---------------------------------------------------------------- 13.6 Force law
d.sec('13.6-force-law')
d.basic('Force law for SHM?', r'\( F = -kx \)' + ' with ' + r'\( k = m\omega^2 \)' + ': restoring force ∝ displacement, towards the mean position')
d.basic('Period of a mass on a spring?', r'\( T = 2\pi\sqrt{\dfrac mk} \)' + ', ' + r'\( \omega = \sqrt{\dfrac km} \)')
d.basic('Linear vs non-linear oscillator?', T('Linear') + ': F ∝ −x exactly. ' + T('Non-linear') + ': extra x², x³ terms (real systems at large amplitude)')
d.basic('Example 13.6: mass between two identical springs k. Period?', 'Net force −2kx → ' + r'\( T = 2\pi\sqrt{\dfrac{m}{2k}} \)', **fig('fig_13_14_two_springs'))
table_card(d, 'Teacher addition · spring combinations', 'Effective k?', [
    ('Two springs in parallel (or on both sides of a mass)', 'k₁ + k₂', False), ('Two springs in series', 'k₁k₂/(k₁ + k₂)', False),
    ('Spring cut into two equal halves', 'each half 2k', False)], term='Effective spring constant')
d.basic('Exercise 13.13: spring k with mass m at one end (a) vs masses m at both ends (b), each pulled by F. Extension and period?', 'Extension ' + N('F/k') + ' in both. T = ' + r'\( 2\pi\sqrt{m/k} \)' + ' for (a), ' + r'\( 2\pi\sqrt{m/2k} \)' + ' for (b) (each half acts as a 2k spring)', **img('fig_13_21_ex_springs'))
d.basic('Exercise 13.8: spring balance, 0–50 kg over 20 cm; a hanging body oscillates with T = 0.6 s. Its weight?', 'k = 50 × 9.8/0.2 = 2450 N/m → m ≈ 22.3 kg → weight ≈ ' + N('219 N'))
d.basic('Exercise 13.9: 3 kg on a spring k = 1200 N/m pulled 2.0 cm. Frequency, max acceleration, max speed?', 'ω = 20 rad/s → ν ≈ ' + N('3.2 Hz') + '; aₘₐₓ = ' + N('8.0 m/s²') + '; vₘₐₓ = ' + N('0.4 m/s'), **fig('fig_13_19_ex_spring'))
d.basic('Exercise 13.10: same spring; x(t) if timing starts at the mean position, at maximum stretch, at maximum compression?', N('x = 2 sin 20t') + ', ' + N('2 cos 20t') + ', ' + N('−2 cos 20t') + ' (cm): only the initial phase differs')
d.basic('Exercise 13.17: why does a floating cork pushed down execute SHM?', 'The extra buoyancy is ∝ depth pushed (Aρₗgx): a restoring force ∝ −x; ' + r'\( T = 2\pi\sqrt{\dfrac{h\rho}{\rho_l g}} \)')
d.basic('Teacher addition: period of a liquid column (total length L) oscillating in a U-tube (Exercise 13.18)?', r'\( T = 2\pi\sqrt{\dfrac{L}{2g}} \)' + ': restoring force from the level difference 2x')
d.basic('Exercise 13.14: locomotive piston, stroke 1.0 m, ω = 200 rad/min. Maximum speed?', 'vₘₐₓ = ωA = 200 × 0.5 = ' + N('100 m/min'))

# ---------------------------------------------------------------- 13.7 Energy
d.sec('13.7-energy-in-shm')
d.basic('Kinetic and potential energy in SHM?', r'\( K = \tfrac12 kA^2\sin^2(\omega t + \phi),\quad U = \tfrac12 kx^2 = \tfrac12 kA^2\cos^2(\omega t + \phi) \)')
d.basic('Total energy in SHM?', r'\( E = \tfrac12 kA^2 = \tfrac12 m\omega^2A^2 \)' + ': constant, ∝ amplitude²', **fig('fig_13_16_energy'))
d.basic('Period of K and U compared with the period of motion?', N('T/2') + ': each peaks twice per oscillation')
d.basic('Where is energy all kinetic, all potential?', 'All ' + T('kinetic') + ' at x = 0; all ' + T('potential') + ' at x = ±A')
d.basic('At what displacement are K and U equal?', r'\( x = \pm\dfrac{A}{\sqrt2} \)')
d.basic('Example 13.7: 1 kg on a 50 N/m spring pulled 10 cm. K, U and E at x = 5 cm?', 'K ≈ ' + N('0.19 J') + ', U = ' + N('0.0625 J') + ', E = ' + N('0.25 J') + ' (= ½ × 50 × 0.1²)')

# ---------------------------------------------------------------- 13.8 Simple pendulum
d.sec('13.8-simple-pendulum')
d.basic('Who noticed the periodic swing of a chandelier, timing it with his pulse?', T('Galileo'))
d.basic('Which force gives the restoring torque on a pendulum bob?', 'The tangential component ' + T('mg sin θ') + '; T − mg cos θ provides the centripetal force', **fig('fig_13_17_pendulum_forces'))
d.basic('Why is a pendulum SHM only for small angles?', 'Restoring torque ∝ sin θ, and ' + T('sin θ ≈ θ') + ' (radians) only for small θ — within ~1 % up to about 20°', **fig('tab_13_1_sin_theta'))
d.basic('Period of a simple pendulum?', r'\( T = 2\pi\sqrt{\dfrac Lg} \)' + ' — independent of mass and (small) amplitude')
d.basic('Example 13.8: length of a seconds pendulum (T = 2 s)?', 'L = gT²/4π² ≈ ' + N('1 m'))
d.basic('Exercise 13.15: a pendulum has T = 3.5 s on Earth. On the Moon (g = 1.7 m/s²)?', '3.5 × √(9.8/1.7) ≈ ' + N('8.4 s'))
d.basic('Exercise 13.16: pendulum in a car going round a circle (radius R, speed v). Period?', r'\( T = 2\pi\sqrt{\dfrac{l}{\sqrt{g^2 + v^4/R^2}}} \)' + ' (effective g includes v²/R)')
d.basic('Teacher addition: pendulum in a lift accelerating up at a?', r'\( T = 2\pi\sqrt{\dfrac{L}{g + a}} \)' + ' (down: g − a; free fall: no oscillation)')

# ---------------------------------------------------------------- Exercises and corrections
d.sec('exercises')
d.basic('Exercise 13.1: which are periodic — swimmer’s return trip, displaced bar magnet, rotating H₂ molecule, arrow from a bow?', T('Bar magnet') + ' and ' + T('rotating H₂ molecule') + '; the swimmer and arrow do not repeat')
d.basic('Exercise 13.2: which are (nearly) SHM — Earth’s rotation, mercury in a U-tube, ball in a bowl, polyatomic molecule vibrations?', 'SHM: ' + T('U-tube mercury') + ', ' + T('ball in a bowl') + '. Periodic but not SHM: Earth’s rotation, polyatomic vibrations')
d.basic('Exercise 13.3 (Fig. 13.18): which x–t plots are periodic?', '(b) and (d), each with period ' + N('2 s') + '; (a), (c) are not (repeating one position is not enough)', **img('fig_13_18_ex_xt'))
d.basic('Correction: NCERT labels the Exercise 13.3 figure "Fig. 18.18", cites "Eq. (14.4)" and potential energy "in Chapter 6". Right references?', T('Fig. 13.18') + ', ' + T('Eq. (13.4)') + ', and ' + T('Chapter 5') + ' (Work, Energy and Power) — leftovers of the old numbering')

d.sec('summary')
table_card(d, 'Summary', 'Formula?', [
    ('Displacement', 'x = A cos(ωt + φ)', False), ('Velocity', 'v = ±ω√(A² − x²)', False), ('Acceleration', 'a = −ω²x', False),
    ('Spring', 'T = 2π√(m/k)', False), ('Pendulum', 'T = 2π√(L/g)', False), ('Energy', 'E = ½kA²', False)], term='Chapter 13 formula sheet')
table_card(d, 'Points to ponder', 'True or false?', [
    ('Every periodic motion is SHM', 'False (only F = −kx)', True),
    ('A sum of two SHMs is always periodic', 'False (frequencies must be commensurate)', True),
    ('Damped oscillation is strictly SHM', 'False', True), ('Period of SHM is independent of amplitude', 'True', False)], term='Chapter 13 concept checks')

print(d.write(os.path.join(OUT, 'deck.json')), 'cards')
