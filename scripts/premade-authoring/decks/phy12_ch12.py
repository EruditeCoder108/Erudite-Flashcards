import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase_phy as sp

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Physics', 'class12-physics-ch12-atoms')
d = Deck('Chapter 12: Atoms', 'Class 12', ['class-12', 'physics', 'ch-12'])
d.description = 'Thomson and Rutherford models, α-scattering, Bohr’s postulates, hydrogen energy levels and spectral series'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- 12.1 Introduction
d.sec('12.1-introduction')
d.basic('Thomson’s atom model (1898)?', T('Plum-pudding model') + ': positive charge spread uniformly through the atom, with electrons embedded like seeds in a watermelon')
d.basic('Why is Thomson’s model unstable?', T('Electrostatically') + ' unstable: charges cannot sit in stable equilibrium (Earnshaw). It also cannot give large-angle α-scattering')
d.basic('Continuous vs line spectra: what emits which?', 'Hot solids, liquids and dense gases: ' + T('continuous') + ' spectrum (interacting atoms). Rarefied excited gases: ' + T('line') + ' spectrum from isolated atoms')
d.basic('Why is a line spectrum called an atom’s “fingerprint”?', 'Each element emits a ' + T('characteristic set of wavelengths') + ' with fixed relative positions, linked to its internal structure')
d.basic('Balmer’s contribution (1885)?', 'An ' + T('empirical formula') + ' for the wavelengths of a group of lines of atomic hydrogen')

# ---------------------------------------------------------------- 12.2 Rutherford
d.sec('12.2-alpha-particle-scattering-and-rutherfords-nuclear-model')
d.basic('Geiger–Marsden experiment (1911): source, target and detector?', T('5.5 MeV α-particles') + ' from Bi-214 collimated by lead bricks hit a ' + T('gold foil (2.1 × 10⁻⁷ m)') + '; scattered particles are seen as scintillations on a ' + T('ZnS screen') + ' with a rotatable microscope', **fig('fig_12_2_schematic'))
d.occlusion('Figure 12.2 · Geiger–Marsden set-up', M + 'fig_12_2_schematic.webp', (1001, 564), [
    ('Lead bricks', [140, 62, 145, 30], True), ('Thin gold foil', [470, 15, 170, 35], True), ('ZnS screen', [752, 358, 140, 30], True),
    ('Detector (Microscope)', [770, 495, 160, 60], True), ('Source of α-particles', [0, 240, 128, 62], True)], guess='hide-all')
d.basic('Why is the experiment performed in a vacuum with a very thin foil?', 'Vacuum: no scattering by air. Thin foil: each α-particle suffers ' + T('at most one scattering') + ', so one nucleus explains each path')
d.basic('Observations of the scattering experiment?', 'Most α-particles ' + T('pass straight through') + '; ~' + N('0.14%') + ' scatter by more than 1°; about ' + N('1 in 8000') + ' deflect by more than 90°', **fig('fig_12_3_scattering_data'))
d.basic('What did the results imply?', 'The atom is mostly ' + T('empty space') + '; all the positive charge and most of the mass sit in a tiny ' + T('nucleus') + ' (10⁻¹⁵–10⁻¹⁴ m vs atom 10⁻¹⁰ m)')
d.basic('Ratio of atomic size to nuclear size?', 'About ' + N('10⁴ to 10⁵') + ' (10⁻¹⁰ m / 10⁻¹⁴–10⁻¹⁵ m)')
d.basic('Why do atomic electrons hardly affect α-particles?', 'They are ' + T('7300 times lighter') + ' than an α-particle; scattering comes from the massive nucleus')
d.basic('Why is Rutherford credited with the discovery of the nucleus?', 'Backward deflection needs a large repulsive force: possible only if the positive charge and mass are ' + T('concentrated in a tiny centre'))
d.basic('Force on an α-particle at distance r from a nucleus of charge Ze?', r'\( F = \dfrac{1}{4\pi\varepsilon_0}\dfrac{(2e)(Ze)}{r^2} \)' + ' (Coulomb repulsion)')
d.basic('Why can the gold nucleus be assumed stationary?', 'It is about ' + T('50 times heavier') + ' than an α-particle')
d.basic('Define the impact parameter b.', 'The ' + T('perpendicular distance') + ' of the initial velocity vector of the α-particle from the centre of the nucleus', **fig('fig_12_4_trajectories'))
d.basic('Impact parameter and scattering angle?', 'Small b → ' + T('large θ') + '; head-on (b ≈ 0) → θ ≈ 180° (rebound); large b → θ ≈ 0')
sp.rutherford_scattering(d)
d.basic('Why do so few α-particles rebound?', 'Head-on collisions (very small b) are rare because the nucleus occupies a tiny area: it gives an ' + T('upper limit on nuclear size'))
d.basic('Distance of closest approach in a head-on collision?', 'K = electrostatic PE at the turning point: ' + r'\( \dfrac{1}{2}mv^2 = \dfrac{1}{4\pi\varepsilon_0}\dfrac{2Ze^2}{d} \)' + ', so ' + r'\( d = \dfrac{2Ze^2}{4\pi\varepsilon_0 K} \)')
steps_card(d, 'Example 12.2 · closest approach', 'Find the missing step.', 'A 7.7 MeV α-particle (K = 1.2 × 10⁻¹² J) is fired head-on at a gold nucleus (Z = 79). Find the distance of closest approach.',
           ['At the turning point K = U: K = (1/4πε₀)(2e)(Ze)/d', 'd = 2Ze²/(4πε₀K) = (2 × 9 × 10⁹ × (1.6 × 10⁻¹⁹)² Z)/(1.2 × 10⁻¹²)', 'd = 3.84 × 10⁻¹⁶ Z m', 'Z = 79: <b>d ≈ 3.0 × 10⁻¹⁴ m = 30 fm</b> (upper bound; actual radius ≈ 6 fm)'], 2,
           'Closest approach of a 7.7 MeV α-particle (Example 12.2)', 'd ≈ 3.0 × 10⁻¹⁴ m; the nucleus is smaller than this')
d.basic('Why does the closest-approach value exceed the actual gold nuclear radius (6 fm)?', 'The α-particle turns back ' + T('without touching') + ' the nucleus: d is much larger than the sum of the radii (Coulomb repulsion acts at a distance)')
d.basic('Teacher addition: how does the closest-approach distance depend on the energy K and charge Z?', T('d ∝ Z/K') + ': doubling K halves d; a heavier nucleus (larger Z) repels more, so d is larger')
d.basic('Teacher addition: Rutherford’s scattering formula?', 'The number of α-particles scattered at angle θ per unit area: ' + r'\( N \propto \dfrac{Z^2}{K^2\sin^4(\theta/2)} \)' + '. So N ∝ Z², N ∝ 1/K², and it falls steeply with θ (Fig 12.3)')
d.basic('Teacher addition: impact parameter and angle?', r'\( b = \dfrac{Ze^2\cot(\theta/2)}{4\pi\varepsilon_0 K} \)' + ': b → 0 as θ → 180°')
d.basic('Teacher addition: why can’t Thomson’s model explain 1 in 8000 backward scattering?', 'With charge spread over 10⁻¹⁰ m the field is weak, so the maximum deflection of a heavy, fast α-particle is tiny (< 0.01°); many small deflections never add up to 90°')
d.basic('Example 12.1: if the solar system had the atom’s proportions (orbit/nucleus = 10⁵), how far would Earth be from the Sun?', 'Sun’s radius 7 × 10⁸ m × 10⁵ = 7 × 10¹³ m, more than ' + T('100 times') + ' the real 1.5 × 10¹¹ m: the atom is far emptier than the solar system')

d.sec('12.2.2-electron-orbits')
d.basic('Condition for a stable circular orbit of the electron in hydrogen (Rutherford model)?', 'Coulomb force = centripetal force: ' + r'\( \dfrac{1}{4\pi\varepsilon_0}\dfrac{e^2}{r^2} = \dfrac{mv^2}{r} \)' + ', so ' + r'\( r = \dfrac{e^2}{4\pi\varepsilon_0 mv^2} \)')
d.basic('Kinetic, potential and total energy of the electron in a hydrogen orbit of radius r?', r'\( K = \dfrac{e^2}{8\pi\varepsilon_0 r},\ U = -\dfrac{e^2}{4\pi\varepsilon_0 r},\ E = -\dfrac{e^2}{8\pi\varepsilon_0 r} \)')
d.basic('Ratio K : U : E for a hydrogen orbit? Why is E negative?', T('K : U : E = 1 : −2 : −1') + ', so E = −K = U/2. Negative E means the electron is ' + T('bound') + '; E > 0 would give an open (unbound) path')
d.basic('Teacher addition: what happens to K, U and E when an electron moves to a larger orbit?', 'K falls, U rises (less negative), E rises (less negative): the atom absorbs energy')
steps_card(d, 'Example 12.3 · radius and speed', 'Find the missing step.', '13.6 eV separates a hydrogen atom into a proton and an electron. Find the orbital radius and the electron’s speed.',
           ['E = −13.6 eV = −2.2 × 10⁻¹⁸ J = −e²/(8πε₀r)', 'r = e²/(8πε₀|E|) = (9 × 10⁹)(1.6 × 10⁻¹⁹)²/(2 × 2.2 × 10⁻¹⁸) = <b>5.3 × 10⁻¹¹ m</b>', 'v = e/√(4πε₀ m r)', '<b>v ≈ 2.2 × 10⁶ m/s</b>'], 1,
           'Bohr radius from the ionisation energy (Example 12.3)', 'r = 5.3 × 10⁻¹¹ m; v = 2.2 × 10⁶ m/s')

# ---------------------------------------------------------------- 12.3 Atomic spectra
d.sec('12.3-atomic-spectra')
d.basic('Emission line spectrum: definition?', 'Bright lines on a dark background from an excited rarefied gas at low pressure, each line at a specific wavelength (the “fingerprint” of the element)')
d.basic('Absorption spectrum?', 'Dark lines in a continuous spectrum seen when white light passes through a gas: the dark lines fall at exactly the ' + T('same wavelengths') + ' as the emission lines of that gas')
d.basic('Kirchhoff/Fraunhofer application?', 'Dark lines in sunlight (Fraunhofer lines) reveal the elements in the Sun’s atmosphere (helium was found this way)')

# ---------------------------------------------------------------- 12.4 Bohr model
d.sec('12.4-bohr-model-of-the-hydrogen-atom')
d.basic('Two failures of Rutherford’s planetary model (classical physics)?', '(1) An orbiting (accelerating) electron radiates and would ' + T('spiral into the nucleus') + ': atoms unstable. (2) Frequency of emitted light would change continuously: ' + T('continuous spectrum') + ', not lines', **fig('fig_12_6_spiral'))
d.basic('Example 12.4: classical frequency of light from the H electron at r = 5.3 × 10⁻¹¹ m, v = 2.2 × 10⁶ m/s?', 'ν = v/2πr = ' + N('6.6 × 10¹⁵ Hz'))
d.basic('Print note: Example 12.4 writes the electron speed as 2.2 × 10⁻⁶ m/s in words. Right?', X('Typo') + ' (printed in the sentence): it is ' + T('2.2 × 10⁶ m/s') + ', as the formula next to it uses')
d.basic('Bohr’s first postulate?', 'The electron can revolve in certain ' + T('stable (stationary) orbits without radiating') + ', each with a definite energy')
d.basic('Bohr’s second postulate (quantum condition)?', 'Angular momentum is quantised: ' + r'\( L = mvr = \dfrac{nh}{2\pi},\ n = 1, 2, 3, \dots \)')
d.basic('Bohr’s third postulate?', 'The electron may jump to a lower-energy orbit and emit a photon: ' + r'\( h\nu = E_i - E_f \)' + '. Absorbing a photon of the same energy lifts it back')
d.basic('Radius of the nth Bohr orbit?', r'\( r_n = \dfrac{n^2h^2\varepsilon_0}{\pi m e^2} = n^2 a_0 \)' + ', a₀ = ' + N('0.529 Å') + ' (Bohr radius); r ∝ n²')
d.basic('Energy of the nth level of hydrogen?', r'\( E_n = -\dfrac{me^4}{8\varepsilon_0^2h^2n^2} = -\dfrac{13.6\ \mathrm{eV}}{n^2} \)'.replace(r'\ \mathrm{eV}', '') + ' with E₁ = −13.6 eV. In joules: −2.18 × 10⁻¹⁸/n² J')
d.basic('Teacher addition: speed of the electron in the nth orbit?', r'\( v_n = \dfrac{e^2}{2\varepsilon_0 nh} = \dfrac{2.19\times10^6}{n}\ \text{m/s} \)'.replace(r'\text{m/s}', 'm/s') + ' (v ∝ 1/n)')
d.basic('Teacher addition: scaling with n: r, v, E, T, K, L?', 'r ∝ n²; v ∝ 1/n; ' + T('E, K, |U| ∝ 1/n²') + '; time period T ∝ n³; frequency of revolution ∝ 1/n³; angular momentum ∝ n')
d.basic('Teacher addition: hydrogen-like ions (He⁺, Li²⁺) with atomic number Z?', 'r_n = n²a₀/Z; v_n = Zv₁/n; ' + r'\( E_n = -\dfrac{13.6Z^2}{n^2} \)' + ' eV (Bohr model works for any one-electron ion)')
d.basic('Ionisation energy of hydrogen? Excitation energies?', 'Ionisation: ' + N('13.6 eV') + ' from n = 1. To n = 2: ' + N('10.2 eV') + '; to n = 3: ' + N('12.09 eV'))

d.sec('12.4.1-energy-levels')
d.basic('Ground state and excited states?', 'Ground state: n = 1, E = −13.6 eV, orbit of radius a₀. Excited states: n > 1. Higher n means ' + T('higher (less negative) energy'), **fig('fig_12_7_levels'))
d.occlusion('Figure 12.7 · Hydrogen energy levels', M + 'fig_12_7_levels.webp', (644, 1001), [
    ('n = 1', [405, 955, 85, 32], True), ('n = 2', [405, 430, 85, 32], True), ('n = 3', [405, 320, 85, 32], True),
    ('Ground state', [355, 915, 205, 35], True), ('Excited states', [520, 308, 110, 72], True), ('Unbound (ionised) atom', [365, 113, 280, 70], True)], guess='hide-all')
d.occlusion('Figure 12.7 · Energy values (eV)', M + 'fig_12_7_levels.webp', (644, 1001), [
    ('−13.6 eV', [55, 953, 95, 32], True), ('−3.40 eV', [55, 432, 95, 32], True), ('−1.51 eV', [55, 322, 95, 32], True), ('−0.85 eV', [55, 275, 95, 32], True)], guess='hide-all')
d.cloze('Energy levels of hydrogen: E₁ = {{c1::−13.6}} eV, E₂ = {{c2::−3.40}} eV, E₃ = {{c3::−1.51}} eV, E₄ = {{c4::−0.85}} eV, E₅ = {{c5::−0.54}} eV, E∞ = {{c6::0}}.')
d.basic('What does E = 0 at n = ∞ mean? What about E > 0?', 'The electron is completely removed and at rest. Above 0 the electron is free with a ' + T('continuum') + ' of energies')
d.basic('How do the level spacings vary with n?', 'Energies come ' + T('closer together as n increases') + ' (E ∝ 1/n²)')
d.basic('As n increases, what happens to the energy needed to free the electron?', 'It ' + T('decreases') + ' (binding energy = 13.6/n² eV)')
d.basic('At room temperature where are most hydrogen atoms?', 'In the ' + T('ground state') + ' (n = 1); excitation needs collisions or photon absorption')
d.basic('Intuition: why do the levels crowd together near E = 0?', 'E = −13.6/n²: successive gaps 13.6(1/n² − 1/(n+1)²) shrink as ~ 27/n³, so high levels merge into the ' + T('ionisation continuum'))

# ---------------------------------------------------------------- 12.5 Line spectra of hydrogen
d.sec('12.5-the-line-spectra-of-the-hydrogen-atom')
d.basic('Frequency of the photon emitted in a jump from n_i to n_f?', r'\( h\nu = E_{n_i} - E_{n_f} = 13.6\left(\dfrac{1}{n_f^2} - \dfrac{1}{n_i^2}\right)\ \) eV'.replace(r'\ \)', r' \)'))
d.basic('Rydberg formula for the wavelength?', r'\( \dfrac{1}{\lambda} = R\left(\dfrac{1}{n_f^2} - \dfrac{1}{n_i^2}\right) \)' + ', R = ' + N('1.097 × 10⁷ m⁻¹') + ' (Rydberg constant)')
d.basic('Why is the spectrum discrete?', 'Only certain n exist, so ΔE takes discrete values, giving ' + T('discrete frequencies'))
d.basic('Absorption in Bohr’s model?', 'A photon whose energy exactly equals E_f − E_i lifts the electron up: dark ' + T('absorption lines') + ' appear at the same frequencies as emission lines', **fig('fig_12_5_h_lines'))
d.occlusion('Figure 12.5 · Hydrogen spectral series', M + 'fig_12_5_h_lines.webp', (1001, 264), [
    ('Lyman series', [0, 205, 98, 59], True), ('Balmer series', [150, 207, 195, 38], True), ('Paschen series', [600, 207, 210, 38], True)], guess='hide-all')
table_card(d, 'Hydrogen series', 'Region and lower level n_f?', [
    ('Lyman', 'n_f = 1; ultraviolet; limit 91.2 nm (122 nm to 91 nm)', False), ('Balmer', 'n_f = 2; visible (and near UV); 656.3 nm (Hα) to limit 364.6 nm', False),
    ('Paschen', 'n_f = 3; infrared; 1875 nm to limit 820 nm', False), ('Brackett', 'n_f = 4; infrared (far)', False), ('Pfund', 'n_f = 5; infrared (far)', False)],
    term='Hydrogen spectral series (teacher addition table)')
d.basic('Mnemonic: order of the hydrogen series (n_f = 1 → 5)?', '“' + T('L') + 'ittle ' + T('B') + 'oys ' + T('P') + 'lay ' + T('B') + 'all ' + T('P') + 'ractice”: Lyman, Balmer, Paschen, Brackett, Pfund (UV, visible, then infrared ×3)')
d.basic('Teacher addition: wavelengths of the first Balmer lines (n = 3, 4, 5, 6 → 2)?', T('656 nm (red, Hα)') + ', ' + T('486 nm (blue-green)') + ', ' + T('434 nm (violet)') + ', ' + T('410 nm (violet)'))
d.basic('Teacher addition: longest and shortest wavelengths of a series?', 'Longest: jump from n_f + 1 to n_f (first line). Shortest: from ∞ (series ' + T('limit') + '), 1/λ = R/n_f². Lyman limit 91.2 nm; Balmer limit 364.6 nm')
d.basic('Teacher addition: maximum number of spectral lines from an electron that starts in level n?', r'\( \dfrac{n(n-1)}{2} \)' + ' (all possible drops between levels): n = 4 gives 6 lines')
d.basic('Teacher addition: for the same Δn, which transitions give the largest photon energy?', 'Transitions ending at ' + T('n = 1') + ' (Lyman): energy gaps are biggest near the nucleus')
d.basic('Teacher addition: what is “the third line of the Balmer series”?', 'n = 5 → 2 (434 nm): the first line is 3 → 2, second 4 → 2, third 5 → 2')
steps_card(d, 'Exercise 12.5 · absorbing to n = 4', 'Find the missing step.', 'A hydrogen atom in the ground state absorbs a photon and jumps to n = 4. Find the photon’s wavelength and frequency.',
           ['ΔE = 13.6 (1/1² − 1/4²) = <b>12.75 eV</b>', 'ΔE = 12.75 × 1.6 × 10⁻¹⁹ = 2.04 × 10⁻¹⁸ J', 'ν = ΔE/h = <b>3.1 × 10¹⁵ Hz</b>', 'λ = c/ν = <b>9.7 × 10⁻⁸ m</b> (97 nm, UV)'], 0,
           'Photon absorbed for 1 → 4 (Exercise 12.5)', '12.75 eV; ν = 3.1 × 10¹⁵ Hz; λ = 97 nm')

# ---------------------------------------------------------------- 12.6 de Broglie explanation
d.sec('12.6-de-broglies-explanation-of-bohrs-second-postulate')
d.basic('De Broglie’s explanation of Bohr’s quantisation (1923)?', 'The electron orbit must hold a ' + T('whole number of de Broglie wavelengths') + ': 2πr_n = nλ (a circular standing wave)', **fig('fig_12_8_standing_wave'))
d.basic('Derive L = nh/2π from the standing wave.', '2πr = nλ with λ = h/mv gives 2πr = nh/mv, so ' + T('mvr = nh/2π'))
d.basic('Who verified the wave nature of electrons and when?', T('Davisson and Germer') + ' (1927)')
d.basic('What happens to wavelengths that do not fit the orbit?', 'They ' + T('interfere destructively with themselves') + ' after each turn and their amplitude dies out; only resonant standing waves survive')
d.basic('Teacher addition: de Broglie wavelength of the electron in the nth orbit?', r'\( \lambda_n = \dfrac{h}{mv_n} = \dfrac{2\pi r_n}{n} \)' + ', so ' + T('n wavelengths fit the nth orbit'))

d.sec('12.6.1-limitations-of-the-bohr-model')
d.basic('Limitations of Bohr’s model?', '(i) Works only for ' + T('hydrogenic (one-electron) atoms') + ', not even helium (electron–electron forces ignored). (ii) Cannot explain the ' + T('relative intensities') + ' of spectral lines')
d.basic('Hydrogenic atoms: definition and examples?', 'A nucleus of charge +Ze with a single electron: ' + T('H, He⁺, Li²⁺') + '…')
d.basic('Why can’t Bohr’s planet-like model be applied to many-electron atoms?', 'Electron–electron repulsion is ' + T('comparable') + ' to nucleus–electron attraction (unlike planet–planet forces compared to the Sun’s pull)')
d.basic('Other limitations exams mention?', 'Inconsistent with the ' + T('uncertainty principle') + ' (fixed orbits with definite r and p); does not explain fine structure, Zeeman effect, or chemical bonding')
d.basic('Why study Bohr’s model still?', 'Three simple postulates explain the main features of the hydrogen spectrum, use classical concepts, and show how physicists ' + T('build models and test them'))
d.basic('Modern picture of Bohr orbits?', 'In quantum mechanics they become regions of ' + T('high probability') + ' of finding the electron; a state needs four quantum numbers (n, l, m, s) but for hydrogen E depends only on n')
d.basic('Why did Bohr quantise angular momentum specifically?', 'h has the ' + T('dimensions of angular momentum') + ', and angular momentum is the natural quantity for circular orbits')
d.basic('Frequency of revolution vs frequency of the spectral line?', 'Not equal in Bohr’s model (line frequency = ΔE/h); they ' + T('coincide only for large n') + ' (n → n − 1), the correspondence principle')

# ---------------------------------------------------------------- Exam patterns
d.sec('exam-patterns')
d.basic('NEET pattern: ratio of the shortest wavelength of Balmer to Lyman series?', 'Balmer limit: 1/λ_B = R/4; Lyman limit: 1/λ_L = R. So λ_B/λ_L = ' + N('4 : 1'))
d.basic('NEET pattern: ratio of the longest wavelengths of the Lyman and Balmer series?', 'Lyman: 1/λ = R(1 − 1/4) = 3R/4. Balmer: R(1/4 − 1/9) = 5R/36. Ratio λ_L : λ_B = (4/3R) : (36/5R) = ' + N('5 : 27'))
d.basic('JEE pattern: an electron in the n = 3 state of H⁻like He⁺ (Z = 2). Its energy and radius vs hydrogen n = 3?', 'E = −13.6 × 4/9 = ' + N('−6.04 eV') + ' (4× more negative); radius = 9a₀/2 = ' + N('4.5 a₀') + ' (half)')
d.basic('JEE pattern: hydrogen atom in the ground state absorbs a 12.75 eV photon. Which lines appear on de-excitation?', 'Goes to n = 4; possible lines = 4 × 3/2 = ' + N('6') + ': 3 Lyman, 2 Balmer, 1 Paschen')
d.basic('JEE pattern: minimum energy photon that can ionise a hydrogen atom in the n = 2 state?', N('3.4 eV') + ' (binding energy 13.6/4)')
d.basic('Pattern: a 12.5 eV electron beam bombards hydrogen. Which series can be excited?', 'Highest reachable n satisfies 13.6(1 − 1/n²) ≤ 12.5 → n = 3 (12.09 eV): Lyman (122, 103 nm) and Balmer (656 nm). No Paschen lines (Exercise 12.8)')
d.basic('Pattern: kinetic energy of the electron in the second Bohr orbit of hydrogen?', 'K = −E = 13.6/4 = ' + N('3.4 eV') + ', PE = −6.8 eV')
d.basic('Pattern: angular momentum of the electron in the third orbit?', 'L = 3h/2π = ' + N('3.16 × 10⁻³⁴ J s'))
d.basic('Board pattern: state Bohr’s postulates and derive the radius of the nth orbit (outline)?', 'Coulomb = centripetal: mv²/r = e²/(4πε₀r²). With mvr = nh/2π eliminate v: ' + r'\( r_n = \dfrac{\varepsilon_0 n^2 h^2}{\pi m e^2} \)')
d.basic('Board pattern: two limitations of Rutherford’s model?', 'Atoms would be unstable (radiating electron spirals in) and would emit a continuous rather than a line spectrum')

# ---------------------------------------------------------------- Points to ponder
d.sec('points-to-ponder')
d.basic('Why are both Thomson’s and Rutherford’s models unstable?', 'Thomson’s: ' + T('electrostatically') + ' unstable. Rutherford’s: unstable due to ' + T('radiation by the orbiting electron'))
d.basic('What did the uncertainty principle do to Bohr’s orbits?', 'The exact orbit picture is inconsistent with it; orbits become ' + T('probability regions') + ' in quantum mechanics')

# ---------------------------------------------------------------- Exercises
d.sec('exercises')
d.basic('Exercise 12.1: complete: (a) The size of the atom in Thomson’s model is ___ the atomic size in Rutherford’s. (b) Ground-state stable equilibrium in ___, net force always in ___. (c) A classical atom based on ___ collapses. (d) Nearly continuous mass in ___, highly non-uniform in ___. (e) Positive part has most of the mass in ___.', '(a) ' + T('no different from') + '. (b) ' + T('Thomson’s model') + '; ' + T('Rutherford’s model') + '. (c) ' + T('Rutherford’s model') + '. (d) ' + T('Thomson’s') + '; ' + T('Rutherford’s') + '. (e) ' + T('both models'))
d.basic('Exercise 12.2: repeat the α-scattering with solid hydrogen foil instead of gold. What results?', 'A proton is ' + T('lighter than the α-particle') + ' (1.67 × 10⁻²⁷ vs 6.64 × 10⁻²⁷ kg), so the α-particle cannot bounce back (like a football hitting a tennis ball): ' + T('no large-angle scattering') + '; the protons are knocked forward')
d.basic('Exercise 12.3: two levels 2.3 eV apart. Frequency of the emitted radiation?', 'ν = ΔE/h = 2.3 × 1.6 × 10⁻¹⁹/6.63 × 10⁻³⁴ = ' + N('5.6 × 10¹⁴ Hz'))
d.basic('Exercise 12.4: ground state of hydrogen is −13.6 eV. KE and PE of the electron?', 'K = −E = ' + N('+13.6 eV') + '; U = 2E = ' + N('−27.2 eV'))
steps_card(d, 'Exercise 12.6 · speeds and periods', 'Find the missing step.', 'Bohr model: speed of the electron in hydrogen for n = 1, 2, 3 and the orbital period in each.',
           ['v_n = v₁/n with v₁ = 2.18 × 10⁶ m/s', '<b>v = 2.18 × 10⁶, 1.09 × 10⁶, 7.27 × 10⁵ m/s</b>', 'r_n = n² × 5.3 × 10⁻¹¹ m; T = 2πr/v', '<b>T = 1.52 × 10⁻¹⁶ s, 1.22 × 10⁻¹⁵ s, 4.11 × 10⁻¹⁵ s</b> (T ∝ n³)'], 3,
           'Bohr speeds and periods (Exercise 12.6)', 'v = 2.18, 1.09, 0.727 × 10⁶ m/s; T = 1.52 × 10⁻¹⁶, 1.22 × 10⁻¹⁵, 4.11 × 10⁻¹⁵ s')
d.basic('Exercise 12.7: radius of the n = 1 orbit is 5.3 × 10⁻¹¹ m. Radii for n = 2 and 3?', 'r ∝ n²: ' + N('2.12 × 10⁻¹⁰ m') + ' and ' + N('4.77 × 10⁻¹⁰ m'))
d.basic('Exercise 12.8: 12.5 eV electrons bombard hydrogen at room temperature. Series of wavelengths emitted?', 'Highest level reached is n = 3 (12.09 eV). Lyman: ' + N('103 nm') + ' and ' + N('122 nm') + '; Balmer: ' + N('656 nm'))
d.basic('Exercise 12.9: quantum number of Earth’s orbit (r = 1.5 × 10¹¹ m, v = 3 × 10⁴ m/s, M = 6.0 × 10²⁴ kg)?', 'n = mvr/(h/2π) = (6 × 10²⁴ × 3 × 10⁴ × 1.5 × 10¹¹)/(1.055 × 10⁻³⁴) = ' + N('2.6 × 10⁷⁴') + ' (so quantisation is invisible for macroscopic bodies)')

# ---------------------------------------------------------------- Summary
d.sec('summary')
table_card(d, 'Summary', 'Formula?', [
    ('Distance of closest approach', 'd = 2Ze²/(4πε₀K)', False), ('Orbit energy (classical)', 'K = −E, U = 2E', False), ('Bohr quantisation', 'mvr = nh/2π', False),
    ('Bohr radius', 'r_n = n² × 0.529 Å', False), ('Energy levels', 'E_n = −13.6 Z²/n² eV', False), ('Photon emitted', 'hν = E_i − E_f', False),
    ('Rydberg formula', '1/λ = R(1/n_f² − 1/n_i²)', False), ('de Broglie orbits', '2πr_n = nλ', False)],
    term='Chapter 12 formula sheet')
table_card(d, 'Concept checks', 'True or false?', [
    ('Most α-particles are scattered by more than 90°', 'False (about 1 in 8000)', True), ('Bohr’s model works for helium atom (two electrons)', 'False', True),
    ('Energy of the hydrogen electron is negative in every bound state', 'True', False), ('Balmer series lies entirely in the infrared', 'False (visible/near UV)', True),
    ('Lyman series transitions end at n = 1', 'True', False), ('Bohr’s model explains the relative intensities of lines', 'False', True)],
    term='Chapter 12 concept checks')

print(d.write(os.path.join(OUT, 'deck.json')), 'cards')
