import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase_phy as sp

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Physics', 'class12-physics-ch13-nuclei')
d = Deck('Chapter 13: Nuclei', 'Class 12', ['class-12', 'physics', 'ch-13'])
d.description = 'Composition and size of the nucleus, mass defect and binding energy, nuclear force, radioactivity, fission and fusion'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- 13.1 Introduction
d.sec('13.1-introduction')
d.basic('How much smaller is the nucleus than the atom? Volume ratio?', 'Radius smaller by about ' + N('10⁴') + '; volume about ' + N('10⁻¹²') + ' of the atom, yet it holds > ' + N('99.9%') + ' of the mass')
d.basic('Analogy for atom vs nucleus size?', 'If the atom were a classroom, the nucleus would be a ' + T('pinhead'))

# ---------------------------------------------------------------- 13.2 Atomic masses and composition
d.sec('13.2-atomic-masses-and-composition-of-nucleus')
d.basic('Define the atomic mass unit (u).', T('1/12') + ' of the mass of one ' + T('¹²C') + ' atom: 1 u = ' + N('1.66 × 10⁻²⁷ kg') + ' = 931.5 MeV/c²')
d.basic('Isotopes: definition and why they behave chemically alike?', 'Atoms of the same element (same ' + T('Z') + ') with different mass (' + T('different N') + ').<br>Identical electronic structure gives the same chemistry and the same place in the periodic table')
d.basic('Why is chlorine’s atomic mass 35.46 u, not an integer?', 'Weighted average of isotopes: 75.4% × 34.98 + 24.6% × 36.98 = ' + N('35.47 u'))
d.basic('Isotopes of hydrogen?', T('Protium ¹H') + ' (99.985%), ' + T('deuterium ²H') + ', ' + T('tritium ³H') + ' (unstable, artificial)')
d.basic('Masses of proton, neutron and electron in u?', 'm_p = ' + N('1.00727 u') + '; m_n = ' + N('1.00866 u') + '; m_e = ' + N('0.00055 u') + ' (m_H = 1.00783 u = m_p + m_e)')
d.basic('Mass of proton and neutron in kg?', 'm_p = ' + N('1.6726 × 10⁻²⁷ kg') + '; m_n = ' + N('1.6749 × 10⁻²⁷ kg'))
d.basic('Why can’t electrons be inside the nucleus?', 'Ruled out by ' + T('quantum theory') + ' arguments; all Z electrons are outside, and the nucleus has exactly Z protons')
d.basic('Discovery of the neutron: who, when and how?', T('Chadwick, 1932') + ': beryllium bombarded by α-particles emitted neutral radiation that knocked protons out of light nuclei; photons would need too much energy, so it was a new neutral particle. Nobel Prize 1935')
d.basic('Free neutron vs bound neutron?', 'Free neutron is ' + X('unstable') + ' (n → p + e⁻ + ν̄, mean life ≈ 1000 s); inside the nucleus it is stable')
d.basic('Define Z, N and A.', 'Z = atomic number (protons); N = neutron number; ' + T('A = Z + N') + ' = mass number = number of nucleons')
d.basic('Nuclide notation and example?', r'\( {}^{A}_{Z}\mathrm{X} \)'.replace(r'\mathrm{X}', 'X') + ': gold ' + T('¹⁹⁷₇₉Au') + ' has 79 protons and 118 neutrons')
d.basic('Isotopes, isobars, isotones?', T('Isotopes') + ': same Z (e.g. ¹H, ²H). ' + T('Isobars') + ': same A (³H and ³He). ' + T('Isotones') + ': same N (¹⁹⁸Hg and ¹⁹⁷Au)')
d.basic('Mnemonic for isotopes / isobars / isotones?', T('Iso-TOPE') + ' = same TOP number (Z at the top of the periodic-table position); ' + T('Iso-BAR') + ' = same “bulk” (A); ' + T('Iso-TONE') + ' = same “n”umber of neutrons')
d.basic('Teacher addition: ratio N/Z for stable nuclei?', T('≈ 1') + ' for light nuclei rising to about ' + T('1.5') + ' for heavy nuclei (extra neutrons offset proton repulsion). Only ~10% of known isotopes are stable')
d.basic('Teacher addition: electrons in a neutral atom vs nucleus for ²³⁸₉₂U?', 'Protons 92, neutrons 146, electrons 92 (neutral atom), nucleons 238')

# ---------------------------------------------------------------- 13.3 Size
d.sec('13.3-size-of-the-nucleus')
d.basic('How did α-scattering bound the nuclear size?', 'A 5.5 MeV α-particle reaches a closest distance of about ' + N('4 × 10⁻¹⁴ m') + ' from gold.<br>Rutherford’s Coulomb scattering held, so the nucleus is smaller than this')
d.basic('Why use faster α-particles or electron beams?', 'At higher energy the α gets closer and deviations from ' + T('pure Coulomb') + ' scattering (short-range nuclear force) show up, revealing the size.<br>Fast electrons measure the charge distribution accurately')
d.basic('Nuclear radius formula?', r'\( R = R_0A^{1/3},\quad R_0 = 1.2\ \mathrm{fm} \)'.replace(r'\ \mathrm{fm}', '') + ' fm (1 fm = 10⁻¹⁵ m)')
d.basic('Why is the nuclear density independent of A?', 'Volume ∝ R³ ∝ A, and mass ∝ A, so ' + T('density = constant') + ' (nuclei behave like drops of liquid of constant density)')
d.basic('Nuclear density value and comparison?', 'About ' + N('2.3 × 10¹⁷ kg m⁻³') + ', ~10¹⁴ times that of water; comparable to a neutron star')
steps_card(d, 'Example 13.1 · nuclear density', 'Find the missing step.', 'Iron nucleus: mass 55.85 u = 9.27 × 10⁻²⁶ kg, A = 56. Find the nuclear density.',
           ['R = 1.2 × 10⁻¹⁵ × 56^{1/3} fm', 'Volume = (4/3)πR³ = (4/3)π(1.2 × 10⁻¹⁵)³ × 56', 'ρ = 9.27 × 10⁻²⁶ / [(4/3)π(1.2 × 10⁻¹⁵)³ × 56]', '<b>ρ ≈ 2.29 × 10¹⁷ kg m⁻³</b>'], 3,
           'Nuclear density of iron (Example 13.1)', 'ρ ≈ 2.29 × 10¹⁷ kg/m³')
d.basic('Exercise 13.4: ratio of the radii of ¹⁹⁷Au and ¹⁰⁷Ag?', 'R ∝ A^{1/3}: (197/107)^{1/3} = ' + N('1.23'))
d.basic('Exercise 13.10: show that nuclear density is nearly constant.', 'ρ = mass/volume = A m_p/[(4/3)π R₀³A] = ' + T('3m_p/(4πR₀³)') + ', independent of A (≈ 2.3 × 10¹⁷ kg/m³)')
d.basic('Points to ponder: why does the radius from electron scattering differ slightly from the α-scattering value?', 'Electrons sense the ' + T('charge distribution') + ' of the nucleus; α-particles and similar probes sense the ' + T('nuclear matter'))
d.basic('Teacher addition: radius of ⁶⁴Cu vs ²⁷Al?', 'R ∝ A^{1/3}: (64/27)^{1/3} = ' + N('1.33') + ' (R_Cu = 4.8 fm, R_Al = 3.6 fm)')

# ---------------------------------------------------------------- 13.4 Mass-energy and binding energy
d.sec('13.4-mass-energy-and-nuclear-binding-energy')
d.basic('Einstein’s mass–energy equivalence?', r'\( E = mc^2 \)' + '; mass is another form of energy. So mass and energy are conserved together, not separately')
d.basic('Example 13.2: energy equivalent of 1 g?', 'E = 10⁻³ × (3 × 10⁸)² = ' + N('9 × 10¹³ J'))
d.basic('Define mass defect.', r'\( \Delta M = [Zm_p + (A-Z)m_n] - M \)' + ': the constituent mass minus the actual nuclear mass (always positive)')
d.basic('Binding energy in terms of mass defect?', r'\( E_b = \Delta M\,c^2 \)' + ' (energy needed to separate the nucleus into free nucleons; energy released when it forms)')
d.basic('Energy equivalent of 1 u?', T('931.5 MeV') + ' (1 u = 931.5 MeV/c²; 1 u = 1.4924 × 10⁻¹⁰ J)')
d.basic('Atomic vs nuclear masses in mass-defect problems: what should you do?', 'Use ' + T('atomic masses with m_H') + ' for Z protons plus Z electrons:<br>ΔM = Z m_H + (A − Z)m_n − M_atom<br>(electron masses cancel; ignore electron binding)')
steps_card(d, 'Example 13.3 · oxygen-16', 'Find the missing step.', '¹⁶₈O: 8 protons, 8 neutrons, atomic mass 15.99493 u. Find the mass defect and binding energy.',
           ['Constituents: 8 × 1.00727 + 8 × 1.00866 = 16.12744 u (with 8 electrons: 16.13184 u)', 'Nuclear mass = 15.99493 − 8 × 0.00055 = 15.99053 u', 'ΔM = 16.12744 − 15.99053 = <b>0.13691 u</b>', 'E_b = 0.13691 × 931.5 = <b>127.5 MeV</b>; per nucleon ≈ <b>7.97 MeV</b>'], 3,
           'Mass defect of oxygen-16 (Example 13.3)', 'ΔM = 0.13691 u; E_b = 127.5 MeV')
d.basic('Define binding energy per nucleon.', r'\( E_{bn} = \dfrac{E_b}{A} \)' + ': the average energy per nucleon needed to remove all nucleons; a measure of ' + T('stability'))
d.basic('Describe the binding-energy-per-nucleon curve.', 'Rises steeply for light nuclei<br>Nearly flat (' + T('~8 MeV') + ') for 30 < A < 170, with a peak ' + N('8.75–8.8 MeV at A = 56 (Fe)') + '<br>Then falls slowly to ' + N('7.6 MeV') + ' at A = 238', **fig('fig_13_1_binding_energy'))
d.basic('Which nucleus is the most stable?', T('Iron (⁵⁶Fe) and its neighbours') + ' near the peak of the curve (highest B/A)')
d.basic('Why is B/A constant for 30 < A < 170?', 'The nuclear force is ' + T('short-ranged and saturating') + '.<br>Each nucleon interacts only with its few neighbours, so adding nucleons does not change B/A')
d.basic('What do the light-nuclei peaks at ⁴He and ¹⁶O suggest?', 'Extra stability: evidence of an atom-like ' + T('shell structure') + ' in nuclei (magic numbers)')
d.basic('B/A values to remember?', '²H ≈ 1.1, ³H ≈ 2.8, ⁴He ≈ ' + N('7.07') + ', ¹⁶O ≈ 7.98, ⁵⁶Fe ≈ ' + N('8.79') + ', ²³⁵U ≈ ' + N('7.6') + ' MeV')
d.basic('Why does fission of a heavy nucleus release energy?', 'Fragments (A ~ 120) have higher B/A (~8.5 MeV) than A ~ 240 (~7.6 MeV): a gain of ~' + T('0.9 MeV × 240 ≈ 216 MeV'))
d.basic('Why does fusion of light nuclei release energy?', 'Fusing light nuclei gives a heavier nucleus with ' + T('higher B/A') + ', a more tightly bound (lighter) system.<br>The mass difference is released')
sp.binding_energy_curve(d)
d.basic('Teacher addition: is energy released for fusion or fission per unit mass larger?', T('Fusion') + ' releases more per unit mass (about 3–4× that of fission per nucleon), e.g. D–T fusion ~ 17.6 MeV over 5 nucleons vs ~200 MeV over 236 for U fission')
d.basic('Teacher addition: Q value of a nuclear reaction?', r'\( Q = (m_i - m_f)c^2 \)' + ' with m_i, m_f the total initial and final rest masses; also Q = final KE − initial KE. Q > 0 exothermic (energy released); Q < 0 endothermic (energy must be supplied)')

# ---------------------------------------------------------------- 13.5 Nuclear force
d.sec('13.5-nuclear-force')
d.basic('Features of the nuclear force: strength?', 'Much ' + T('stronger') + ' than Coulomb and gravitational forces (must beat proton–proton repulsion at ~ fm distances)')
d.basic('Range of the nuclear force?', T('Short range') + ': falls rapidly to zero beyond a few femtometres, giving saturation and constant B/A')
d.basic('Nuclear force between p–p, n–n and p–n?', 'Approximately ' + T('the same') + ': independent of electric charge')
d.basic('Potential energy vs separation for two nucleons?', 'Minimum at r₀ ≈ ' + N('0.8 fm') + '; attractive for r > r₀, strongly ' + X('repulsive') + ' for r < r₀ (hard core)', **fig('fig_13_2_potential'))
d.basic('Is there a simple mathematical form for the nuclear force?', X('No') + ': unlike Coulomb’s or Newton’s laws it has no simple formula')
d.basic('Teacher addition: force at r = r₀ and beyond ~ 4–5 fm?', 'At r₀ the force is ' + T('zero') + ' (PE minimum); beyond ~ 4–5 fm the nuclear force is negligible')
d.basic('Teacher addition: the nuclear force compared with gravity in relative strength?', 'Strong : EM : weak : gravity ≈ ' + N('1 : 10⁻² : 10⁻⁶ : 10⁻³⁸'))
d.basic('Teacher addition: which particles mediate the nuclear force?', 'Exchange of ' + T('mesons (pions)') + ' (Yukawa): the nuclear force is ' + T('non-central') + ' and spin-dependent')

# ---------------------------------------------------------------- 13.6 Radioactivity
d.sec('13.6-radioactivity')
d.basic('Who discovered radioactivity and how?', T('Becquerel (1896)') + ':<br>uranium-potassium sulphate exposed to light blackened a photographic plate wrapped in black paper')
d.basic('What is radioactivity?', 'A ' + T('nuclear') + ' phenomenon: an unstable nucleus spontaneously ' + T('decays') + ' by emitting α, β or γ radiation')
d.basic('The three types of radioactive decay?', T('α-decay') + ': emission of ⁴₂He<br>' + T('β-decay') + ': emission of electrons or positrons<br>' + T('γ-decay') + ': emission of high-energy photons (100s of keV or more)')
d.basic('Positron: what is it?', 'The ' + T('antiparticle of the electron') + ': same mass, equal and opposite charge (+e). An electron and positron annihilate into γ-photons')
d.basic('What do α, β and γ rays consist of?', 'α: ' + T('helium nuclei') + ' (charge +2e); β: ' + T('electrons') + '; γ: ' + T('electromagnetic radiation') + ' shorter in wavelength than X-rays')
d.basic('Radioactivity as a sign of what?', T('Instability') + ' of the nucleus (neutron–proton ratio away from the stable band)')
d.basic('Teacher addition: change in Z and A in α-decay?', T('Z − 2, A − 4') + ' (parent → daughter + ⁴₂He)')
d.basic('Teacher addition: change in Z and A in β⁻ and β⁺ decay?', T('β⁻') + ': n → p + e⁻ + ν̄: Z + 1, A same. ' + T('β⁺') + ': p → n + e⁺ + ν: Z − 1, A same')
d.basic('Teacher addition: change in Z and A in γ-decay?', T('None') + ': the nucleus drops from an excited to a lower level, emitting a photon')
d.basic('Teacher addition: why is a neutrino needed in β-decay?', 'β-particles show a ' + T('continuous energy spectrum') + '.<br>Energy, momentum and angular momentum conservation require a third light neutral particle (neutrino/antineutrino)')
d.basic('Teacher addition: penetrating power and ionising power of α, β, γ?', 'Penetration: ' + T('γ > β > α') + ' (α stopped by paper). Ionisation: ' + T('α > β > γ'))
d.basic('Teacher addition: radioactive decay law?', r'\( N = N_0e^{-\lambda t} \)' + '; λ = decay constant (s⁻¹); the number decaying per second ∝ N (statistical, spontaneous, unaffected by temperature or pressure)')
d.basic('Teacher addition: activity of a sample?', r'\( R = \left|\dfrac{dN}{dt}\right| = \lambda N = R_0e^{-\lambda t} \)' + '; SI unit ' + T('becquerel (Bq)') + ' = 1 decay/s; 1 curie = 3.7 × 10¹⁰ Bq')
d.basic('Teacher addition: half-life and mean life?', r'\( T_{1/2} = \dfrac{\ln 2}{\lambda} = \dfrac{0.693}{\lambda},\quad \tau = \dfrac{1}{\lambda} = 1.44\,T_{1/2} \)' + ' (τ: time to fall to 1/e)')
d.basic('Teacher addition: number of nuclei left after n half-lives?', r'\( N = \dfrac{N_0}{2^n},\ n = \dfrac{t}{T_{1/2}} \)')
sp.half_life_dots(d)
d.basic('Teacher addition: a sample has half-life 8 days. Fraction left after 24 days? After 20 days?', '24 d = 3 half-lives: ' + N('1/8') + '. 20 d = 2.5 half-lives: (½)^2.5 = ' + N('0.177'))
d.basic('Teacher addition: half-life 5 min. Time for 87.5% to decay?', '12.5% = 1/8 left → 3 half-lives = ' + N('15 min'))
d.basic('Teacher addition: two samples with half-lives T and 2T and equal initial numbers. Ratio of initial activities?', 'R = λN: λ₁/λ₂ = 2, so R₁/R₂ = ' + N('2 : 1'))
d.basic('Teacher addition: does the half-life apply to a single nucleus?', X('No') + ': it is statistical; for a single nucleus the probability of surviving one half-life is exactly ½')

# ---------------------------------------------------------------- 13.7 Nuclear energy
d.sec('13.7-nuclear-energy')
d.basic('Nuclear vs chemical energy per unit mass?', 'Energy per reaction: MeV vs eV, so nuclear sources give about ' + T('a million times more') + '.<br>Fission of 1 kg U: ~ ' + N('10¹⁴ J') + '<br>Burning 1 kg coal: ~ 10⁷ J')
d.basic('Nuclear fission: definition and example?', 'A heavy nucleus splits into two intermediate-mass fragments after absorbing a neutron: ' + r'\( n + {}^{235}_{92}U \to {}^{236}_{92}U \to {}^{144}_{56}Ba + {}^{89}_{36}Kr + 3n \)')
d.basic('Other fission channels of ²³⁵U?', T('¹³³₅₁Sb + ⁹⁹₄₁Nb + 4n') + ' and ' + T('¹⁴⁰₅₄Xe + ⁹⁴₃₈Sr + 2n') + ': on average 2–3 neutrons per fission')
d.basic('Energy released per fission of a heavy nucleus?', 'About ' + N('200 MeV') + ' (216 MeV estimated from the B/A gain of 0.9 MeV × 240).<br>It first appears as kinetic energy of fragments and neutrons, then as heat')
d.basic('What happens to the fission fragments?', 'They are ' + T('radioactive') + ' and emit β-particles in succession until they reach stable end products')
d.basic('Uses of fission?', 'Controlled: ' + T('nuclear reactors') + ' (electricity). Uncontrolled: ' + T('atom bomb'))
d.basic('Teacher addition: chain reaction and multiplication factor k?', 'Neutrons released cause further fissions.<br>k = neutrons produced / neutrons used<br>k < 1 dies out<br>' + T('k = 1 critical (reactor)') + '<br>k > 1 explosive (bomb)')
d.basic('Teacher addition: role of the moderator and the control rods in a reactor?', T('Moderator') + ' (heavy water, graphite): slows fast neutrons to thermal energies so ²³⁵U captures them<br>' + T('Control rods') + ' (cadmium, boron): absorb neutrons to hold k = 1')
d.basic('Teacher addition: critical mass?', 'The minimum mass of fissile material that sustains a chain reaction (neutron loss through the surface < production inside)')
d.basic('Teacher addition: fissile materials?', T('²³⁵U, ²³⁹Pu') + ' (fissile with slow neutrons); ²³⁸U is fertile (converted to ²³⁹Pu in a breeder reactor)')

d.sec('13.7.2-nuclear-fusion')
d.basic('Nuclear fusion: definition and energy source?', 'Two light nuclei fuse into a heavier one, releasing energy since B/A rises; it powers ' + T('the Sun and all stars'))
d.basic('Fusion reactions in NCERT?', '¹H + ¹H → ²H + e⁺ + ν + ' + N('0.42 MeV') + '; ²H + ²H → ³He + n + ' + N('3.27 MeV') + '; ²H + ²H → ³H + ¹H + ' + N('4.03 MeV'))
d.basic('Why does fusion need very high temperature?', 'The nuclei must overcome their ' + T('Coulomb repulsion') + ' (barrier ~ 400 keV for two protons) so the short-range nuclear force can act.<br>This is thermonuclear fusion')
d.basic('Estimate the temperature for proton–proton fusion.', '(3/2)kT ≈ 400 keV gives ' + N('T ≈ 3 × 10⁹ K') + '<br>The Sun’s core is only 1.5 × 10⁷ K.<br>Fusion happens through high-energy protons in the tail of the distribution (and tunnelling)')
d.basic('Proton–proton cycle in the Sun: net reaction?', r'\( 4\,{}^1_1H + 2e^- \to {}^4_2He + 2\nu + 6\gamma + 26.7\ \) MeV'.replace(r'\ \) MeV', r' \) MeV') + ': four hydrogen atoms give one helium atom')
d.basic('Steps of the p–p cycle?', '(i) ¹H + ¹H → ²H + e⁺ + ν (0.42 MeV); (ii) e⁺ + e⁻ → γ + γ (1.02 MeV); (iii) ²H + ¹H → ³He + γ (5.49 MeV); (iv) ³He + ³He → ⁴He + ¹H + ¹H (12.86 MeV)')
d.basic('What happens when a star exhausts core hydrogen?', 'The core contracts and heats to ~ ' + N('10⁸ K') + ': helium fuses to carbon.<br>Fusion proceeds up to elements near the ' + T('iron peak') + ' of the binding-energy curve, not beyond')
d.basic('Age of the Sun and its fate?', 'About ' + N('5 × 10⁹ years') + ' old with hydrogen for another 5 billion; then it swells into a ' + T('red giant'))
d.basic('Controlled thermonuclear fusion: main challenge?', 'Fuel is a hot ' + T('plasma') + ' (~10⁸ K) that no container can hold; it must be confined (magnetic confinement, e.g. tokamak; ITER). India is participating')
d.basic('Teacher addition: fission vs fusion table?', T('Fission') + ': heavy nucleus splits, neutron-induced, chain reaction, radioactive waste, ~ 200 MeV per event<br>' + T('Fusion') + ': light nuclei combine, needs 10⁷–10⁸ K, little radioactive waste, more energy per unit mass')
d.basic('Teacher addition: hydrogen bomb principle?', 'Uncontrolled ' + T('fusion') + ' triggered by a fission bomb that supplies the required temperature')
steps_card(d, 'Example 13.4 · reactions and energy', 'Find the missing step.', 'Are nuclear equations “balanced” like chemical equations? How does mass turn into energy if proton and neutron numbers are both conserved? Is mass–energy interconversion absent in chemical reactions?',
           ['Chemical: atoms of each element are the same on both sides. Nuclear: elements are transmuted, but <b>protons and neutrons (charge and baryon number) are conserved</b>', 'Rest masses of nucleons match on both sides; the <b>total binding energy differs</b> and binding energy adds a negative contribution to nuclear mass', 'The mass difference of nuclei on the two sides is released or absorbed as energy', 'Chemical reactions also convert mass to energy, but mass defects are <b>~10⁶ times smaller</b>, so the effect is unnoticed'], 3,
           'Mass–energy in nuclear and chemical reactions (Example 13.4)', 'Nucleon numbers conserved; binding energy differences appear as Q; chemical reactions do it too but 10⁶ times less')

# ---------------------------------------------------------------- Points to ponder
d.sec('points-to-ponder')
d.basic('Is there a separate law of conservation of mass and of energy?', X('No') + ': a unified law of ' + T('conservation of mass–energy') + ' (E = mc²)')
d.basic('Which processes are exothermic on the binding-energy curve?', T('Fusion of two light nuclei') + ' and ' + T('fission of a heavy nucleus') + ' into intermediate-mass nuclei')
d.basic('What is the fusion condition?', 'Sufficient initial energy to overcome the ' + T('Coulomb barrier') + ' (hence very high temperatures)')
d.basic('Stable nuclei and the neutron–proton ratio?', 'About ' + T('1 : 1') + ' for light nuclei rising to ' + T('3 : 2') + ' for heavy ones; nuclei off this ratio are radioactive')
d.basic('Do all fission products stay stable?', X('No') + ': fragments are neutron-rich and undergo successive β-decays')

# ---------------------------------------------------------------- Exam patterns
d.sec('exam-patterns')
d.basic('NEET pattern: nucleus ²³⁸₉₂U emits one α and two β⁻. Final Z and A?', 'α: Z 90, A 234; two β⁻: Z 92. Final ' + T('²³⁴₉₂U'))
d.basic('NEET pattern: binding energy of a nucleus is the energy…?', 'Released when the nucleus forms from free nucleons (and needed to separate it): ' + T('E_b = Δm c²'))
d.basic('NEET pattern: nuclear density of ¹²⁵Te vs ⁶⁴Cu?', T('Equal') + ' (density independent of A). Their radii are in the ratio (125/64)^{1/3} = 1.25')
d.basic('NEET pattern: which has higher B/A: ⁷Li or ⁵⁶Fe? Which is more stable?', T('⁵⁶Fe') + ' (peak of the curve)')
d.basic('JEE pattern: half-life 10 days; N₀ = 10⁶. Activity after 30 days relative to initially?', '1/8 of the initial: R = R₀/8 (three half-lives)')
d.basic('JEE pattern: what fraction of the original mass converts to energy in the Sun’s p–p cycle?', '26.7 MeV out of 4 × 938 MeV ≈ ' + N('0.7%'))
d.basic('JEE pattern: energy released when one ²³⁵U undergoes fission (200 MeV): energy per gram?', 'Atoms per gram = 6.02 × 10²³/235 = 2.56 × 10²¹; × 200 MeV = ' + N('5.1 × 10²³ MeV ≈ 8.2 × 10¹⁰ J') + ' per gram')
d.basic('Board pattern: differentiate nuclear fission and fusion.', 'Fission: heavy nucleus splits (chain reaction, ~200 MeV per event, neutron induced). Fusion: light nuclei join (needs ~ 10⁷–10⁸ K, source of stellar energy)')
d.basic('Board pattern: why is nuclear density so much larger than atomic density?', 'The nucleus holds > 99.9% of the atom’s mass in ~10⁻¹² of its volume: density ~ 10¹⁷ kg/m³ vs ~10³ for ordinary matter')

# ---------------------------------------------------------------- Exercises
d.sec('exercises')
steps_card(d, 'Exercise 13.1 · nitrogen-14', 'Find the missing step.', 'Binding energy of ¹⁴₇N given m(¹⁴₇N) = 14.00307 u. (Use m_H = 1.007825 u, m_n = 1.008665 u.)',
           ['ΔM = 7 m_H + 7 m_n − m = 7 × 1.007825 + 7 × 1.008665 − 14.00307', '7.054775 + 7.060655 − 14.00307 = <b>0.11236 u</b>', 'E_b = 0.11236 × 931.5 MeV', '<b>E_b ≈ 104.7 MeV</b> (7.48 MeV per nucleon)'], 2,
           'Binding energy of nitrogen-14 (Exercise 13.1)', '104.7 MeV')
d.basic('Exercise 13.2: binding energy of ⁵⁶Fe (55.934939 u) and ²⁰⁹Bi (208.980388 u)?', 'Fe: ΔM = 0.528461 u → ' + N('492.3 MeV') + ', per nucleon ' + N('8.79 MeV') + '. Bi: ΔM = 1.760877 u → ' + N('1640 MeV') + ', per nucleon ' + N('7.85 MeV') + ' (key gives 7.84)')
d.basic('Exercise 13.3: energy to separate all nucleons in a 3.0 g copper coin (⁶³Cu, 62.92960 u)?', 'ΔM per atom = 0.591935 u = 551.4 MeV; atoms = (3/62.9296) × 6.023 × 10²³ = 2.87 × 10²²; total ' + N('1.58 × 10²⁵ MeV = 2.5 × 10¹² J'))
d.basic('Exercise 13.5: Q for (i) ¹H + ³H → 2 ²H? (ii) ¹²C + ¹²C → ²⁰Ne + ⁴He?', '(i) Q = ' + N('−4.03 MeV') + ': endothermic. (ii) Q = ' + N('+4.62 MeV') + ': exothermic')
d.basic('Exercise 13.6: is fission of ⁵⁶Fe into two ²⁸Al nuclei energetically possible?', 'Q = [55.93494 − 2 × 27.98191] × 931.5 = ' + N('−26.9 MeV') + ' < 0: ' + X('not possible') + '<br>Fe is at the peak of B/A; both fragments are less bound')
d.basic('Exercise 13.7: energy from fission of all atoms in 1 kg of ²³⁹Pu at 180 MeV each?', 'N = 6.023 × 10²³ × 1000/239 = 2.52 × 10²⁴ atoms; E = ' + N('4.5 × 10²⁶ MeV'))
steps_card(d, 'Exercise 13.8 · lamp powered by fusion', 'Find the missing step.', 'How long can a 100 W lamp glow on the fusion of 2.0 kg of deuterium, ²H + ²H → ³He + n + 3.27 MeV?',
           ['Deuterium atoms: 2000/2 × 6.023 × 10²³ = 6.02 × 10²⁶', 'Each reaction uses 2 nuclei: 3.0 × 10²⁶ reactions', 'Energy = 3.0 × 10²⁶ × 3.27 MeV = 9.85 × 10²⁶ MeV = 1.58 × 10¹⁴ J', 't = E/P = 1.58 × 10¹² s ≈ <b>5 × 10⁴ years</b>'], 3,
           'Fusion energy of 2 kg deuterium (Exercise 13.8)', 'About 4.9–5 × 10⁴ years')
d.basic('Exercise 13.9: Coulomb barrier for a head-on collision of two deuterons of radius 2.0 fm?', 'Touching distance 4 fm: U = (9 × 10⁹)(1.6 × 10⁻¹⁹)²/(4 × 10⁻¹⁵) = 5.8 × 10⁻¹⁴ J ≈ ' + N('360 keV'))

# ---------------------------------------------------------------- Summary
d.sec('summary')
table_card(d, 'Summary', 'Formula?', [
    ('Mass number', 'A = Z + N', False), ('Nuclear radius', 'R = R₀A^{1/3}, R₀ = 1.2 fm', False), ('Mass–energy', 'E = mc², 1 u = 931.5 MeV/c²', False),
    ('Mass defect', 'ΔM = Zm_p + (A − Z)m_n − M', False), ('Binding energy', 'E_b = ΔM c²', False), ('Q value', 'Q = (m_initial − m_final)c²', False),
    ('Decay law', 'N = N₀e^{−λt}', False), ('Half-life', 'T = 0.693/λ; τ = 1/λ', False), ('Activity', 'R = λN (Bq)', False)],
    term='Chapter 13 formula sheet')
table_card(d, 'Concept checks', 'True or false?', [
    ('Nuclear density depends on the mass number', 'False (constant ≈ 2.3 × 10¹⁷ kg/m³)', True), ('B/A is maximum near A = 56', 'True', False),
    ('The nuclear force depends on electric charge', 'False', True), ('Fusion needs very high temperature to overcome Coulomb repulsion', 'True', False),
    ('The decay of a single nucleus can be predicted exactly', 'False (statistical)', True), ('Fission of ⁵⁶Fe releases energy', 'False', True)],
    term='Chapter 13 concept checks')

print(d.write(os.path.join(OUT, 'deck.json')), 'cards')
