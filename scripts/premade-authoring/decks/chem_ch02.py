import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Chemistry', 'class11-chemistry-ch02-structure-of-atom')
d = Deck('Chapter 2: Structure of Atom', 'Class 11', ['class-11', 'chemistry', 'ch-2'])
d.description = 'Subatomic particles, Thomson and Rutherford models, EM radiation, photoelectric effect, Bohr model, de Broglie, uncertainty, quantum numbers, orbitals and configurations'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}
HS = (1001, 447)

# ---------------------------------------------------------------- intro
d.sec('2.0-intro')
d.basic('Origin of the word "atom"?', 'Greek "' + T('a-tomio') + '": uncut-able, non-divisible')
d.basic('What did Dalton’s theory fail to explain (that led to sub-atomic particles)?', 'Why glass or ebonite ' + T('gets charged') + ' when rubbed with silk or fur')

# ---------------------------------------------------------------- 2.1 Sub-atomic particles
d.sec('2.1-discovery-of-subatomic-particles')
d.basic('What did Faraday’s electrolysis work (1830) suggest?', 'The ' + T('particulate nature of electricity'))
d.basic('Conditions for discharge in a cathode ray tube?', T('Very low pressure') + ' and ' + T('very high voltage'), **fig('fig_2_1a_cathode_tube'))
d.basic('Why a perforated anode and ZnS coating?', 'Rays pass through the hole and make a ' + T('bright spot') + ' on the phosphorescent ZnS.<br>This proves flow from cathode to anode', **fig('fig_2_1b_perforated_anode'))
d.cloze('Cathode rays travel from {{c1::cathode to anode}}, in {{c2::straight lines}} without fields, and behave as {{c3::negatively charged}} particles.')
d.basic('Do cathode ray properties depend on electrode material or gas?', X('No') + ': so electrons are a ' + T('basic constituent of all atoms'))
d.basic('Everyday device that is a cathode ray tube?', 'Old ' + E('television picture tubes') + ' (pictures from fluorescence on the screen)')
d.basic('Who measured e/mₑ, when, and how?', T('J.J. Thomson') + ', ' + N('1897') + ', balancing perpendicular ' + T('electric and magnetic fields'), **fig('fig_2_2_thomson_em'))
d.basic('Thomson’s apparatus: where does the beam hit with only E-field, only B-field, both balanced?', 'Only electric: ' + T('A') + '. Only magnetic: ' + T('C') + '. Balanced: ' + T('B') + ' (undeflected).')
d.cloze('Deflection of a charged particle increases with its {{c1::charge}} and the {{c2::field strength}}, and decreases with its {{c3::mass}}.')
d.basic('Value of e/mₑ?', N('1.758820 × 10¹¹ C kg⁻¹'))
d.basic('Who measured the electron’s charge, and by what experiment?', T('R.A. Millikan') + ', ' + T('oil drop experiment') + ' (1906–14)', **fig('fig_2_3_millikan'))
d.basic('Charge on the electron?', N('−1.602176 × 10⁻¹⁹ C') + ' (Millikan got −1.6 × 10⁻¹⁹ C)')
d.basic('How did the oil drops get charged in Millikan’s experiment?', 'Air was ionised by ' + T('X-rays') + '; drops picked up charge by colliding with ions')
d.basic('Millikan’s key conclusion?', 'Charge on any drop is an ' + T('integral multiple') + ' of e: \\( q = ne \\)')
d.basic('Three forces on a moving oil drop?', T('Gravity') + ', ' + T('electrostatic') + ' force and ' + T('viscous drag'))
d.basic('Mass of the electron and how obtained?', N('9.1094 × 10⁻³¹ kg') + ' = e ÷ (e/mₑ), combining Millikan and Thomson')
d.basic('Canal rays: how do they differ from cathode rays?', 'Positive ions; their ' + T('mass and e/m depend on the gas') + '; deflected opposite to cathode rays')
d.basic('Smallest positive ion from canal rays, and when characterised?', 'The ' + T('proton') + ' (from hydrogen), ' + N('1919'))
d.basic('Who discovered the neutron, when, how?', T('Chadwick') + ', ' + N('1932') + ', bombarding ' + T('beryllium') + ' with α-particles')
table_card(d, 'Table 2.1', 'Approx. mass (u) and relative charge?', [
    ('Electron', '≈ 0 (0.00054 u), −1', True), ('Proton', '≈ 1 (1.00727 u), +1', False),
    ('Neutron', '≈ 1 (1.00867 u), 0', False)], term='Properties of fundamental particles')
d.basic('Which is heavier, proton or neutron?', T('Neutron') + ' (1.674927 vs 1.6726216 × 10⁻²⁷ kg)')

# ---------------------------------------------------------------- 2.2 Atomic models
d.sec('2.2-atomic-models')
d.basic('Thomson model (1898)?', 'Sphere (r ≈ 10⁻¹⁰ m) of ' + T('uniform positive charge') + ' with electrons embedded; mass uniform', **fig('fig_2_4_thomson_model'))
d.basic('Other names of Thomson’s model?', T('Plum pudding') + ', raisin pudding or watermelon model')
d.basic('What did Thomson’s model explain, and what did it fail?', 'Explained overall ' + T('neutrality') + '; failed Rutherford’s scattering results')
d.basic('Who discovered X-rays, and properties?', T('Röntgen') + ', 1895: not deflected by fields, highly penetrating, λ ≈ ' + N('0.1 nm'))
d.basic('Who discovered radioactivity?', T('Henri Becquerel'))
d.basic('What are α-particles?', T('Helium nuclei') + ': 2 units of positive charge, 4 u mass')
d.cloze('Penetrating power: α {{c1::least}}; β ≈ {{c2::100}} times α; γ ≈ {{c3::1000}} times α.')
d.basic('Rutherford’s scattering set-up?', 'α-particles on a thin ' + T('gold foil') + ' (~100 nm) surrounded by a ' + T('ZnS screen') + '; with Geiger and Marsden', **fig('fig_2_5a_rutherford'))
table_card(d, 'Rutherford’s α-scattering', 'Conclusion?', [
    ('Most pass undeflected', 'Atom is mostly empty space', False),
    ('A few deflected by small angles', 'Positive charge concentrated in a tiny region', False),
    ('~1 in 20,000 bounce back (~180°)', 'Nucleus is tiny, dense and positive', False)], term='Rutherford: observations → conclusions')
d.basic('Radius of atom vs nucleus?', 'Atom ' + N('10⁻¹⁰ m') + '; nucleus ' + N('10⁻¹⁵ m') + ' (cricket ball nucleus → 5 km atom)', **fig('fig_2_5b_gold_foil'))
d.basic('Rutherford’s nuclear model in one line?', 'Tiny dense positive ' + T('nucleus') + ' with electrons revolving in circular ' + T('orbits') + ', like a solar system')
d.basic('Atomic number Z and mass number A?', T('Z') + ' = number of protons (= electrons in neutral atom). ' + T('A') + ' = protons + neutrons (nucleons).')
d.basic('Isotopes vs isobars?', T('Isotopes') + ': same Z, different A (¹²C, ¹³C, ¹⁴C). ' + T('Isobars') + ': same A, different Z (¹⁴C, ¹⁴N).')
d.basic('Isotopes of hydrogen?', T('Protium') + ' ¹H (99.985%), ' + T('deuterium') + ' ²H (0.015%), ' + T('tritium') + ' ³H (trace)')
d.basic('Why do isotopes have the same chemistry?', 'Chemistry depends on ' + T('electrons') + ' (set by Z); neutrons have very little effect')
d.basic('Isotones? (extra term)', 'Same number of ' + T('neutrons') + ', e.g. ¹⁴C and ¹⁶O (8 n each)')
d.basic('p, n, e in ⁸⁰₃₅Br? (Problem 2.1)', 'p = e = ' + N('35') + ', n = ' + N('45'))
d.basic('Species with 18 e, 16 p, 16 n? (Problem 2.2)', T('³²₁₆S²⁻') + ' (anion, 2 extra electrons)')
d.basic('Why does Rutherford’s model fail on stability?', 'An orbiting electron is ' + T('accelerating') + '; by Maxwell it should radiate and ' + X('spiral into the nucleus') + ' in ~' + N('10⁻⁸ s'))
d.basic('Rutherford model’s second drawback?', 'Says nothing about the ' + T('distribution and energies') + ' of electrons')

# ---------------------------------------------------------------- 2.3 EM radiation
d.sec('2.3-electromagnetic-radiation')
d.basic('Two developments that led to Bohr’s model?', T('Dual nature of EM radiation') + ' and ' + T('atomic spectra'))
d.basic('Who explained EM waves (1870) and who confirmed them?', T('Maxwell') + '; confirmed by ' + T('Heinrich Hertz'))
d.basic('Orientation of E and B fields in an EM wave?', 'Perpendicular to each other and to the ' + T('direction of propagation'), **fig('fig_2_6_em_wave'))
d.basic('Do EM waves need a medium?', X('No') + '; they travel in vacuum')
d.basic('Uses of EM regions: 10⁶ Hz, 10¹⁰ Hz, 10¹³ Hz, 10¹⁶ Hz?', T('Radio') + ' (broadcast), ' + T('microwave') + ' (radar), ' + T('IR') + ' (heating), ' + T('UV') + ' (sun)')
d.basic('Order of EM regions by increasing wavelength.', 'γ < X < UV < visible < IR < microwave < radio', **fig('fig_2_7_em_spectrum'))
d.basic('Mnemonic for EM spectrum from long λ to short?', '"' + T('Raging Martians Invaded Venus Using X-ray Guns') + '": Radio, Micro, IR, Visible, UV, X, Gamma')
d.basic('Key wave relations?', r'\( c = \nu \lambda \)' + ' and wavenumber ' + r'\( \bar{\nu} = \frac{1}{\lambda} \)')
d.basic('Units of frequency and wavenumber?', 'ν: ' + T('Hz (s⁻¹)') + '. Wavenumber: ' + T('m⁻¹') + ' (SI), cm⁻¹ commonly.')
d.basic('Wavelength of Vividh Bharati at 1368 kHz? (Problem 2.3)', 'λ = c/ν = ' + N('219.3 m') + ': radio wave')
d.basic('Frequency range of visible light (400–750 nm)?', N('7.5 × 10¹⁴') + ' Hz (violet) to ' + N('4.0 × 10¹⁴') + ' Hz (red)')
d.basic('Wavenumber and frequency of 5800 Å light? (Problem 2.5)', r'\( \bar{\nu} = 1.724 \times 10^{6} \)' + ' m⁻¹; ν = ' + N('5.172 × 10¹⁴ Hz'))
d.cloze('Phenomena classical wave theory could not explain: {{c1::black-body radiation}}, the {{c2::photoelectric effect}}, heat capacity of solids vs T, and {{c3::line spectra}} of atoms.')
d.basic('What is a black body?', 'An ideal body that ' + T('absorbs and emits all frequencies') + '.<br>Approximated by a cavity with a tiny hole (or carbon black)')
d.basic('Black-body curve: what happens as T rises?', 'Intensity rises and the peak shifts to ' + T('shorter wavelength') + ' (red → white → blue)', **fig('fig_2_8_blackbody_curve'))
d.basic('Planck’s quantum theory (1900)?', 'Energy is emitted/absorbed in discrete packets (' + T('quanta') + '): \\( E = h\\nu \\)')
d.basic('Planck’s constant?', r'\( h = 6.626 \times 10^{-34} \)' + ' J s')
d.basic('Staircase analogy for quantisation? (intuition)', 'You can stand on any step but ' + X('never between') + ' steps: E = 0, hν, 2hν, … nhν')
d.basic('Photoelectric effect: who observed it first, and metals used?', T('H. Hertz') + ', ' + N('1887') + '; K, Rb, Cs', **fig('fig_2_9_photoelectric'))
d.cloze('Photoelectric effect: emission is {{c1::instantaneous}}; number of electrons ∝ {{c2::intensity}}; KE of electrons ∝ {{c3::frequency}}; no emission below the {{c4::threshold frequency}}.')
d.basic('Einstein’s photoelectric equation?', r'\( h\nu = h\nu_0 + \frac{1}{2} m_e v^2 \)' + ' (W₀ = hν₀ is the work function)')
d.basic('Why can bright red light not eject electrons from K, but dim yellow can?', 'Red ν < ν₀ (' + N('5.0 × 10¹⁴ Hz') + ' for K); each photon too weak. Intensity only adds ' + T('more photons') + ', not more energy per photon.')
d.basic('Lowest work function among Li, Na, K, Mg, Cu, Ag (Table 2.2)?', T('K') + ' (2.25 eV); highest Cu (4.8 eV)')
d.basic('Energy of 1 mol photons at 5 × 10¹⁴ Hz? (Problem 2.6)', N('199.5 kJ mol⁻¹'))
steps_card(d, 'Problem 2.7', '100 W bulb, λ = 400 nm. Photons per second?', 'E = hc/λ; number = power ÷ E.',
           ['E = (6.626×10⁻³⁴)(3×10⁸)/(400×10⁻⁹)', '= 4.969 × 10⁻¹⁹ J', 'n = 100 / 4.969×10⁻¹⁹ = <b>2.012 × 10²⁰ s⁻¹</b>'], 2, 'Photons emitted per second', '2.012 × 10²⁰ s⁻¹')
steps_card(d, 'Problem 2.8', '300 nm on Na; KE = 1.68 × 10⁵ J/mol. Work function, λ₀?', 'hν = W₀ + KE',
           ['E(1 mol photons) = 3.99 × 10⁵ J/mol', 'W₀ = 3.99 − 1.68 = 2.31 × 10⁵ J/mol = 3.84 × 10⁻¹⁹ J per e⁻', 'λ₀ = hc/W₀ = <b>517 nm</b> (green)'], 2, 'Threshold wavelength of sodium', '517 nm')
d.basic('Handy shortcut: photon energy in eV from λ in nm? (trick)', r'\( E(eV) \approx \frac{1240}{\lambda(nm)} \)')
d.basic('When does light show wave vs particle behaviour?', T('Wave') + ' while propagating (interference, diffraction); ' + T('particle') + ' when interacting with matter')

d.sec('2.3.3-atomic-spectra')
d.basic('Continuous vs line spectrum?', T('Continuous') + ': all wavelengths merge (white light, rainbow). ' + T('Line') + ': only specific wavelengths, from gaseous atoms.')
d.basic('Which colour deviates least through a prism?', T('Red') + ' (longest λ); violet deviates most')
d.basic('Emission vs absorption spectrum?', T('Emission') + ': bright lines from an excited sample<br>' + T('Absorption') + ': dark lines in a continuous spectrum (the photographic negative)', **fig('fig_2_10_emission_absorption'))
d.basic('Why are line spectra called atomic "fingerprints"?', 'Each element has a ' + T('unique') + ' line spectrum')
d.basic('Elements discovered by spectroscopy?', E('Rb, Cs, Tl, In, Ga, Sc') + '; ' + E('He') + ' was found in the sun')
d.basic('Early user of line spectra to identify elements?', T('Robert Bunsen'))
d.basic('Rydberg formula for hydrogen?', r'\( \bar{\nu} = 109677 \left( \frac{1}{n_1^2} - \frac{1}{n_2^2} \right) \)' + ' cm⁻¹')
d.occlusion('Table 2.3 · Hydrogen spectral series', M + 'tab_2_3_hydrogen_series.webp', HS, [
    ('1', pad([297, 116, 25, 53], 6), True), ('2', pad([297, 181, 25, 53], 6), True), ('3', pad([297, 246, 25, 53], 6), True),
    ('4', pad([297, 311, 25, 53], 6), True), ('5', pad([297, 377, 25, 53], 6), True),
    ('Ultraviolet', pad([594, 116, 206, 53], 6), True), ('Visible', pad([594, 181, 206, 53], 6), True),
    ('Infrared', pad([594, 246, 206, 53], 6), True), ('Infrared', pad([594, 311, 206, 53], 6), True), ('Infrared', pad([594, 377, 206, 53], 6), True)])
d.basic('Mnemonic for the hydrogen series (n₁ = 1 to 5)?', '"' + T('Lazy Boys Prefer Bed Pillows') + '": Lyman, Balmer, Paschen, Brackett, Pfund')
d.basic('Only hydrogen series in the visible region?', T('Balmer') + ' (n₁ = 2)', **fig('fig_2_11_h_transitions'))
d.basic('Max number of spectral lines when an electron falls from level n to 1? (JEE)', r'\( \frac{n(n-1)}{2} \)' + ' (e.g. n = 4 → 6 lines)')

# ---------------------------------------------------------------- 2.4 Bohr
d.sec('2.4-bohr-model')
d.cloze('Bohr: electrons move in fixed circular {{c1::stationary orbits}}; energy changes only by {{c2::jumps}} between them with \\( \\nu = \\Delta E / h \\); angular momentum is {{c3::quantised}}.')
d.basic('Bohr’s quantisation condition?', r'\( m_e v r = n \frac{h}{2\pi} \)')
d.basic('Radius of nth Bohr orbit (hydrogen-like)?', r'\( r_n = 52.9 \frac{n^2}{Z} \)' + ' pm')
d.basic('Energy of nth orbit (hydrogen-like)?', r'\( E_n = -2.18 \times 10^{-18} \frac{Z^2}{n^2} \)' + ' J = ' + r'\( -13.6 \frac{Z^2}{n^2} \)' + ' eV')
d.basic('What does the negative sign in Eₙ mean?', 'The bound electron has ' + T('lower energy') + ' than a free electron at rest (E = 0 at n = ∞)')
d.basic('Energy of H electron at n = 2?', N('−0.545 × 10⁻¹⁸ J') + ' (= −3.4 eV)')
d.basic('How do velocity and radius change with Z and n?', 'Velocity ∝ ' + T('Z/n') + '; radius ∝ ' + T('n²/Z'))
d.basic('Bohr’s ΔE for a transition?', r'\( \Delta E = 2.18 \times 10^{-18} \left( \frac{1}{n_i^2} - \frac{1}{n_f^2} \right) \)' + ' J')
d.basic('Absorption vs emission in Bohr’s model?', T('Absorption') + ': n_f > n_i, ΔE positive. ' + T('Emission') + ': n_i > n_f, energy released.')
d.basic('Frequency and wavelength for H transition n = 5 → 2? (Problem 2.10)', 'ν = ' + N('6.91 × 10¹⁴ Hz') + ', λ = ' + N('434 nm') + ' (Balmer, visible)')
d.basic('Energy and radius of first orbit of He⁺? (Problem 2.11)', 'E = ' + N('−8.72 × 10⁻¹⁸ J') + '; r = ' + N('26.45 pm'))
d.basic('Correction: NCERT calls 2.18 × 10⁻¹⁸ J the "Rydberg constant". Precise term?', 'That is the ' + T('Rydberg energy') + ' (hcR); the Rydberg constant itself is ' + N('109677 cm⁻¹') + ' for H')
d.cloze('Bohr’s model fails to explain: the {{c1::fine (doublet) structure}} of H lines, spectra of {{c2::multi-electron atoms}}, the {{c3::Zeeman}} (magnetic) and {{c4::Stark}} (electric) effects, and {{c5::chemical bonding}}.')

# ---------------------------------------------------------------- 2.5 Towards QM
d.sec('2.5-dual-behaviour-and-uncertainty')
d.basic('de Broglie relation (1924)?', r'\( \lambda = \frac{h}{mv} = \frac{h}{p} \)')
d.basic('Experimental proof of electron waves, and its use?', T('Electron diffraction') + '; used in the ' + T('electron microscope') + ' (~15 million ×)')
d.basic('Why don’t we notice the wave nature of a cricket ball?', 'Large mass → λ ' + T('far too small') + ' to detect')
d.basic('λ of a 0.1 kg ball at 10 m/s? (Problem 2.12)', N('6.626 × 10⁻³⁴ m'))
d.basic('λ of electron with KE = 3.0 × 10⁻²⁵ J? (Problem 2.13)', 'v = 812 m/s; λ = ' + N('896.7 nm'))
d.basic('de Broglie λ from kinetic energy (shortcut)?', r'\( \lambda = \frac{h}{\sqrt{2mK}} \)' + '; for an electron through V volts, λ ≈ ' + r'\( \frac{1.227}{\sqrt{V}} \)' + ' nm')
d.basic('"Mass" of a 3.6 Å photon? (Problem 2.14)', 'm = h/λc = ' + N('6.135 × 10⁻²⁹ kg'))
d.basic('Heisenberg uncertainty principle (1927)?', r'\( \Delta x \cdot \Delta p_x \geq \frac{h}{4\pi} \)' + ': exact position and momentum cannot both be known')
d.basic('Why can’t we "see" an electron without disturbing it? (intuition)', 'Light of λ smaller than the electron has ' + T('huge momentum') + ' and knocks the electron away')
d.basic('Main implication of the uncertainty principle?', 'Rules out ' + X('definite paths or trajectories') + ' for electrons; we speak of ' + T('probability'))
d.basic('Δv for an electron if Δx = 10⁻⁸ m?', '≈ ' + N('5.79 × 10³ m/s') + ': too large for fixed Bohr orbits')
d.basic('Δv of an electron located within 0.1 Å? (Problem 2.15)', 'Δv = h/(4π m Δx) = ' + N('5.79 × 10⁶ m/s'))
d.basic('Δx for a 40 g golf ball at 45 m/s, 2% error? (Problem 2.16)', N('1.46 × 10⁻³³ m') + ': meaningless for large objects')
d.basic('Two reasons for failure of the Bohr model?', 'Ignores ' + T('dual behaviour') + ' of electrons; contradicts the ' + T('uncertainty principle') + ' (defined orbits)')

# ---------------------------------------------------------------- 2.6 QM model
d.sec('2.6-quantum-mechanical-model')
d.basic('Who developed quantum mechanics (1926)?', T('Heisenberg') + ' and ' + T('Schrödinger') + ' independently')
d.basic('Schrödinger equation form?', r'\( \hat{H} \psi = E \psi \)' + ' (Ĥ = Hamiltonian operator)')
d.basic('What is an atomic orbital?', 'The ' + T('wave function ψ') + ' of an electron in an atom')
d.basic('Physical meaning of ψ and of |ψ|²?', 'ψ has ' + X('no physical meaning') + '; ' + T('|ψ|²') + ' = probability density (always positive)')
d.basic('Why do multi-electron orbital energies depend on n and l, not n alone?', 'Electron–electron ' + T('repulsion') + ' and shielding')
d.basic('Orbit vs orbital?', T('Orbit') + ': definite circular path (Bohr), 2n² e⁻. ' + T('Orbital') + ': 3D region of probability, max 2 e⁻.')

d.sec('2.6.1-quantum-numbers')
table_card(d, 'Quantum numbers', 'What does it tell?', [
    ('n (principal)', 'Shell; size and (mainly) energy', False), ('l (azimuthal)', 'Subshell; shape', False),
    ('mₗ (magnetic)', 'Orientation in space', False), ('mₛ (spin)', 'Spin orientation, +½ or −½', False)], term='The four quantum numbers')
d.cloze('For a given n, l = {{c1::0 to n − 1}}; for a given l, mₗ = {{c2::−l … 0 … +l}}, i.e. {{c3::2l + 1}} values.')
d.basic('Shell letters for n = 1, 2, 3, 4?', T('K, L, M, N'))
d.basic('Subshell letters for l = 0, 1, 2, 3?', T('s, p, d, f'))
d.basic('Number of orbitals in shell n; max electrons?', T('n²') + ' orbitals; ' + T('2n²') + ' electrons')
d.basic('Orbitals in n = 3? (Problem 2.17)', '1 + 3 + 5 = ' + N('9'))
d.basic('Name orbitals: (n=2,l=1), (4,0), (5,3), (3,2). (Problem 2.18)', T('2p, 4s, 5f, 3d'))
d.basic('Which of these is impossible: 1p, 2s, 2d, 3f, 3p? (classic)', X('1p, 2d, 3f') + ' (l must be < n)')
d.basic('Who proposed electron spin, and when?', T('Uhlenbeck and Goudsmit') + ', ' + N('1925'))
d.basic('What led to the fourth quantum number?', 'Lines appearing as ' + T('doublets and triplets') + ' in multi-electron spectra')
d.basic('Correction: NCERT says the electron "spins around its own axis like the earth". Accurate?', X('Not literally') + ': spin is an ' + T('intrinsic') + ' quantum angular momentum; the spinning-top picture is only an analogy')

d.sec('2.6.2-shapes-of-orbitals')
d.basic('ψ and ψ² vs r for 1s and 2s?', '1s: max at nucleus, falls off. 2s: falls to ' + T('zero (a node)') + ' then rises again', **fig('fig_2_12_psi_plots'))
d.basic('Number of radial nodes formula?', T('n − l − 1') + ' (ns has n − 1)')
d.basic('Number of angular nodes; total nodes?', 'Angular = ' + T('l') + '; total = ' + T('n − 1'))
d.basic('Radial and angular nodes in 3p and 4d? (JEE)', '3p: 1 radial, 1 angular. 4d: 1 radial, 2 angular.')
d.basic('What is a boundary surface diagram?', 'Surface of constant |ψ|² enclosing ~' + N('90%') + ' probability of finding the electron', **fig('fig_2_13_1s_2s'))
d.basic('Why not draw a 100% boundary surface?', '|ψ|² is ' + T('never zero') + ' at any finite distance')
d.basic('Shape and size order of s orbitals?', T('Spherical') + '; 4s > 3s > 2s > 1s')
d.basic('Shape of p orbitals, and nodal plane of pz?', 'Two ' + T('lobes') + ' (dumbbell) along x, y, z; pz has the ' + T('xy-plane') + ' as nodal plane', **fig('fig_2_14_p_orbitals'))
d.basic('Is there a simple link between mₗ = −1, 0, +1 and px, py, pz?', X('No'))
d.basic('Lowest n with d orbitals, and their names?', T('n = 3') + '; ' + T('dxy, dyz, dxz, dx²−y², dz²'), **fig('fig_2_15_d_orbitals'))
d.basic('Which d orbital has a different shape?', T('dz²') + ' (dumbbell with a ring/doughnut); all five 3d are degenerate')
d.basic('Which d orbitals have lobes along the axes?', T('dx²−y²') + ' and ' + T('dz²') + '; the other three lie between axes')

d.sec('2.6.3-energies-of-orbitals')
d.basic('Energy order in the hydrogen atom?', 'Depends on n only: 1s < 2s = 2p < 3s = 3p = 3d < …', **fig('fig_2_16_energy_levels'))
d.basic('What are degenerate orbitals?', 'Orbitals of the ' + T('same energy'))
d.basic('Define effective nuclear charge.', 'Net positive charge felt by an outer electron after ' + T('shielding') + ' by inner electrons (Zeff·e)')
d.basic('Shielding order within a shell?', T('s > p > d > f') + ' (s electrons penetrate closest to the nucleus)')
d.basic('The (n + l) rule?', 'Lower (n + l) → lower energy; if equal, ' + T('lower n') + ' is lower')
d.basic('Which is lower: 4s or 3d? 4f or 6p?', T('4s') + ' (4+0 < 3+2). ' + T('4f') + ' (7, lower n than 6p also 7).')
d.basic('Order E₂s(H), E₂s(Li), E₂s(Na), E₂s(K)?', 'E₂s(H) > E₂s(Li) > E₂s(Na) > E₂s(K): energy falls as Z rises')

d.sec('2.6.4-filling-of-orbitals')
d.basic('Aufbau principle?', 'In the ground state, orbitals are filled in order of ' + T('increasing energy') + ' ("aufbau" = building up)')
d.basic('Standard filling order?', '1s, 2s, 2p, 3s, 3p, ' + T('4s, 3d') + ', 4p, 5s, 4d, 5p, ' + T('6s, 4f, 5d') + ', 6p, 7s', **fig('fig_2_17_filling_order'))
d.basic('Pauli exclusion principle (1926)?', 'No two electrons in an atom can have the ' + T('same four quantum numbers') + '; an orbital holds 2 e⁻ of opposite spin')
d.basic('Hund’s rule of maximum multiplicity?', 'Electrons pair in a subshell only after ' + T('each orbital is singly occupied') + ' (same spin)')
d.basic('Pairing starts with which electron in p, d, f?', N('4th') + ', ' + N('6th') + ' and ' + N('8th'))
d.basic('Mnemonic for Hund’s rule? (intuition)', '"' + T('Bus seat rule') + '": passengers take an empty double seat before sitting next to someone')

d.sec('2.6.5-electronic-configuration')
d.basic('Advantage of orbital (box) diagrams over spdf notation?', 'Shows ' + T('all four quantum numbers') + ' (including spin)')
d.basic('Core vs valence electrons?', T('Core') + ': in completely filled inner shells. ' + T('Valence') + ': in the outermost shell.')
d.basic('Configuration of N and O?', 'N: 1s² 2s² 2p³. O: 1s² 2s² 2p⁴.')
d.basic('Configuration of K and why?', '[Ar] ' + T('4s¹') + ': 4s is lower than 3d')
d.basic('Configurations of Cr and Cu?', 'Cr: [Ar] ' + X('3d⁵ 4s¹') + '. Cu: [Ar] ' + X('3d¹⁰ 4s¹') + '.')
d.basic('Why do Cr and Cu break the aufbau pattern?', 'Half-filled (d⁵) and fully filled (d¹⁰) subshells have ' + T('extra stability'))
d.basic('Where do 4f and 5d get filled?', 'From ' + T('lanthanum to mercury'))
d.basic('Elements after which one are all artificial and short-lived?', T('Uranium'))
d.basic('Unpaired electrons in Fe, Fe²⁺, Fe³⁺? (JEE)', N('4, 4, 5') + ' (ions lose 4s electrons first)')
d.basic('Trap: which electrons leave first when a transition metal ionises?', T('4s') + ' (outermost n), even though they filled first')

d.sec('2.6.7-stability-of-half-and-fully-filled')
d.cloze('Half-filled and fully filled subshells are extra stable because of {{c1::symmetrical distribution}} of electrons and maximum {{c2::exchange energy}}.')
d.basic('What is exchange energy?', 'Energy released when electrons of the ' + T('same spin') + ' in degenerate orbitals exchange positions')
d.basic('Number of exchanges in d⁵?', N('10') + ' (4 + 3 + 2 + 1): maximum', **fig('fig_2_18_exchange'))
d.basic('Link between exchange energy and Hund’s rule?', 'Parallel spins maximise exchanges → the basis of ' + T('Hund’s rule'))

# ---------------------------------------------------------------- summary
d.sec('summary')
table_card(d, 'Summary', 'Discovered / proposed by?', [
    ('Electron e/m', 'J.J. Thomson, 1897', False), ('Electron charge', 'Millikan (oil drop)', False),
    ('Neutron', 'Chadwick, 1932', False), ('Nucleus', 'Rutherford (α-scattering)', False),
    ('Quantum theory', 'Planck, 1900', False), ('Matter waves', 'de Broglie, 1924', False)], term='Who discovered what')
table_card(d, 'Summary', 'Formula?', [
    ('Photon energy', 'E = hν = hc/λ', False), ('Photoelectric', 'hν = hν₀ + ½mv²', False),
    ('Bohr energy', 'Eₙ = −13.6 Z²/n² eV', False), ('Bohr radius', 'rₙ = 52.9 n²/Z pm', False),
    ('de Broglie', 'λ = h/mv', False), ('Heisenberg', 'Δx·Δp ≥ h/4π', False)], term='Structure of atom formula sheet')

n = d.write(os.path.join(OUT, 'deck.json'))
print(n, 'cards')
