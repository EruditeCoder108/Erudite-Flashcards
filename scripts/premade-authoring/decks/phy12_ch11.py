import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase_phy as sp

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Physics', 'class12-physics-ch11-dual-nature-of-radiation-and-matter')
d = Deck('Chapter 11: Dual Nature of Radiation and Matter', 'Class 12', ['class-12', 'physics', 'ch-11'])
d.description = 'Electron emission, photoelectric effect, Einstein’s equation, photons, de Broglie waves and NEET/JEE-style problems'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- 11.1 Introduction
d.sec('11.1-introduction')
d.basic('Cathode rays: what are they, and who confirmed it?', 'Streams of fast, ' + T('negatively charged particles') + ' (electrons), seen in low-pressure gas discharge.<br>' + T('J. J. Thomson') + ' confirmed it with crossed E and B fields')
d.basic('What did Thomson measure for cathode-ray particles?', 'Their speed (0.1–0.2 c) and the ' + T('specific charge e/m = 1.76 × 10¹¹ C/kg') + '.<br>Both are independent of cathode material and gas: the particles are universal')
d.basic('Thomson and the electron: when and what prize?', 'Named the particles ' + T('electrons') + ' (1897); Nobel Prize in Physics ' + N('1906'))
d.basic('Millikan’s oil-drop experiment (1913): what did it show?', 'The charge on a drop is always an ' + T('integral multiple of e = 1.602 × 10⁻¹⁹ C') + ': charge is quantised. With e/m, the electron mass follows')
d.basic('Milestones near 1895–1897?', T('X-rays') + ' discovered by Röntgen (1895); ' + T('electron') + ' by Thomson (1897)')
d.basic('History note: NCERT credits Crookes with discovering cathode rays in 1870. Is that the whole story?', 'Cathode rays were observed earlier (Plücker, Hittorf 1850s–60s); Crookes studied them in the 1870s and suggested they are charged particles (1879). Exams ask ' + T('Thomson → electron, Crookes → cathode-ray tube'))

# ---------------------------------------------------------------- 11.2 Electron emission
d.sec('11.2-electron-emission')
d.basic('Why can’t free electrons simply leave a metal?', 'A departing electron leaves the surface positively charged, which pulls it back.<br>It needs a ' + T('minimum energy') + ' to escape')
d.basic('Define work function φ₀. Unit?', 'The ' + T('minimum energy') + ' needed to remove an electron from the metal surface.<br>Measured in ' + T('eV') + ' (depends on the metal and its surface)')
d.basic('Define electron volt.', 'The energy gained by an electron accelerated through ' + T('1 V') + ': 1 eV = ' + N('1.602 × 10⁻¹⁹ J'))
d.basic('Three ways to supply the energy for electron emission?', T('Thermionic') + ' (heating)<br>' + T('Field') + ' (very strong E ~ 10⁸ V/m, as in a spark plug)<br>' + T('Photoelectric') + ' (light of suitable frequency)')
d.basic('Photoelectrons: definition?', 'Electrons ejected from a metal surface by ' + T('incident light of suitable frequency'))
d.basic('Teacher addition: typical work functions (eV)?', 'Cs ' + N('2.1') + ', K 2.3, Na 2.3, Ca 2.9, Zn 4.3, Cu 4.7, Pt 5.6 (alkali metals have the smallest, so respond to visible light)')

# ---------------------------------------------------------------- 11.3 Photoelectric effect (Hertz, Hallwachs, Lenard)
d.sec('11.3-photoelectric-effect')
d.basic('Who discovered photoelectric emission and how?', T('Hertz (1887)') + ': sparks in the detector loop were enhanced when the emitter plate was lit by UV light')
d.basic('Hallwachs’ observation with a zinc plate and an electroscope?', 'A negatively charged zinc plate ' + T('lost its charge') + ' in UV.<br>An uncharged one became ' + T('positively') + ' charged.<br>So negative particles are emitted')
d.basic('Lenard’s observation in an evacuated tube?', 'UV falling on emitter C causes a current to flow to collector A.<br>It ' + T('stops as soon as the UV stops') + ' (electrons attracted by the positive plate)')
d.basic('Which metals respond to visible light and which only to UV?', 'Alkali metals (Li, Na, K, Cs, Rb) respond even to ' + T('visible') + ' light; Zn, Cd, Mg need ' + T('UV'))
d.basic('Threshold frequency: definition?', 'The ' + T('minimum frequency') + ' of incident light below which no photoemission occurs, whatever the intensity.<br>It depends on the material')

# ---------------------------------------------------------------- 11.4 Experimental study
d.sec('11.4-experimental-study-of-photoelectric-effect')
d.basic('Apparatus for studying photoelectric effect?', 'Evacuated quartz-window tube with emitter C and collector A; commutator to reverse the polarity; voltmeter and microammeter', **fig('fig_11_1_apparatus'))
d.basic('Why is the tube evacuated and fitted with a quartz window?', 'Vacuum: electrons reach A without collisions with gas molecules. Quartz: transmits ' + T('UV') + ' (ordinary glass absorbs it)')
d.basic('Effect of intensity on photocurrent (potential fixed, ν > ν₀)?', 'Photocurrent is ' + T('directly proportional to intensity') + ' (number of photoelectrons per second ∝ intensity)', **fig('fig_11_2_current_intensity'))
d.basic('Saturation current: definition and dependence?', 'The maximum current, when ' + T('all emitted electrons reach A') + '; ∝ intensity (for fixed ν)', **fig('fig_11_3_current_potential'))
d.basic('Stopping (cut-off) potential V₀?', 'The minimum ' + T('negative (retarding) potential') + ' on A that reduces the photocurrent to zero')
d.basic('Relation between stopping potential and maximum kinetic energy?', r'\( K_{max} = eV_0 = \tfrac12 mv_{max}^2 \)')
d.basic('Effect of intensity on V₀ (same ν)?', 'None: V₀ is ' + T('independent of intensity') + ', so K_max is independent of intensity.<br>Curves for I₁ < I₂ < I₃ saturate at different heights but cut the axis at the same −V₀')
d.basic('Effect of frequency on V₀, and on the saturation current?', 'V₀ ' + T('increases with ν') + ' (V₀₃ > V₀₂ > V₀₁ for ν₃ > ν₂ > ν₁)<br>For the same intensity the saturation current is the same', **fig('fig_11_4_frequencies'))
d.basic('V₀ vs ν graph: shape and meaning?', T('Straight line') + ' with slope h/e and intercept on the ν-axis = ν₀ (threshold). Different metals give ' + T('parallel lines') + ' (same slope) with different ν₀', **fig('fig_11_5_v0_vs_nu'))
d.basic('Summarise the four experimental facts of photoemission.', '(i) I_photo ∝ intensity (ν > ν₀). (ii) Saturation current ∝ intensity; V₀ independent of intensity. (iii) ' + T('Threshold frequency') + ' exists; K_max rises linearly with ν. (iv) ' + T('Instantaneous') + ' (~ 10⁻⁹ s or less)')
d.basic('Time lag between light hitting the metal and emission?', 'Essentially none: about ' + N('10⁻⁹ s') + ' or less, even for very dim light')
d.basic('Teacher addition: photocurrent vs applied voltage: what is the shape for V positive and negative?', 'Current rises with accelerating V until ' + T('saturation') + '; for negative V it falls to zero at −V₀. At V = 0 the current is non-zero (fast electrons still reach A)')
d.basic('Exam trap: which quantities depend on intensity, and which on frequency?', 'Intensity → ' + T('number of photoelectrons / saturation current') + '<br>Frequency → ' + T('K_max and stopping potential') + ' (and whether emission occurs at all)')

# ---------------------------------------------------------------- 11.5 Wave theory
d.sec('11.5-photoelectric-effect-and-wave-theory-of-light')
d.basic('Wave-theory expectation for K_max with increasing intensity?', 'K_max should ' + X('increase') + ' (larger E-field amplitude gives more energy per electron), contradicting observation')
d.basic('Wave theory and the threshold frequency?', 'Predicts ' + X('no threshold') + ': a sufficiently intense beam over enough time should always free electrons')
d.basic('Wave theory and the time lag?', 'Energy spreads over the wavefront, so an electron would need ' + T('hours') + ' to gather φ₀.<br>Observed emission is instantaneous')
d.basic('Which three observations does wave theory fail to explain?', T('Independence of K_max from intensity') + ', ' + T('existence of ν₀') + ' and the ' + T('instantaneous emission'))

# ---------------------------------------------------------------- 11.6 Einstein
d.sec('11.6-einsteins-photoelectric-equation')
d.basic('Einstein’s picture of radiation (1905)?', 'Radiation consists of discrete ' + T('quanta of energy hν') + '; an electron absorbs ' + T('one quantum') + ' at a time')
d.basic('Einstein’s photoelectric equation?', r'\( K_{max} = h\nu - \phi_0 \)' + ', i.e. ' + r'\( eV_0 = h\nu - \phi_0 \)' + ' (more tightly bound electrons come out with less energy)')
d.basic('Threshold frequency and wavelength in terms of φ₀?', r'\( \nu_0 = \dfrac{\phi_0}{h},\quad \lambda_0 = \dfrac{hc}{\phi_0} \)' + '; λ₀ (nm) = 1240/φ₀(eV)')
d.basic('Equation of V₀ versus ν?', r'\( V_0 = \dfrac{h}{e}\,(\nu - \nu_0) \)' + ': slope h/e (same for all metals)')
d.basic('How does Einstein’s equation explain the intensity-independence of K_max?', 'One photon is absorbed by one electron.<br>Intensity only changes ' + T('how many photons') + ' arrive (number of emitted electrons)')
d.basic('How does it explain the threshold?', 'Need hν > φ₀ for K_max > 0: ' + T('below ν₀ a single photon is too weak') + ' and electrons cannot pool energy from several photons')
d.basic('How does it explain instantaneous emission?', 'Absorption of one photon by one electron is ' + T('instantaneous') + ' regardless of the beam’s intensity')
d.basic('Teacher addition: graph of K_max vs ν?', T('Straight line') + ', slope h (Planck’s constant), x-intercept ν₀, y-intercept −φ₀; all metals give parallel lines', )
d.basic('Teacher addition: two metals with work functions φ₁ < φ₂ under the same light. Which gives more K_max?', 'Metal 1: K_max = hν − φ₁ is ' + T('larger') + ' (V₀ larger, ν₀ smaller)')
d.basic('Teacher addition: if the frequency is doubled, does K_max double?', X('No') + ': K_max = hν − φ₀. It more than doubles: K₂ = 2hν − φ₀ = 2K₁ + φ₀')
d.basic('Teacher addition: how is photocurrent related to intensity numerically?', 'If a fraction η of photons ejects an electron: ' + r'\( i = \eta\,\dfrac{P}{h\nu}\,e \)' + ' (P = power of light)')
d.basic('Millikan and Einstein’s equation (1906–1916)?', 'Millikan set out to disprove it, but his slope of V₀ vs ν gave ' + T('h = 6.6 × 10⁻³⁴ J s') + ', confirming it (1916).<br>Nobel Prize 1923 (also for e)')
d.basic('Who got the Nobel Prize for the photoelectric effect and when?', T('Einstein, 1921') + ' (for the explanation of the photoelectric effect and contributions to theoretical physics)')

# ---------------------------------------------------------------- 11.7 Photon
d.sec('11.7-particle-nature-of-light-the-photon')
sp.photoelectric_stages(d)
d.basic('Energy and momentum of a photon?', r'\( E = h\nu = \dfrac{hc}{\lambda},\quad p = \dfrac{h\nu}{c} = \dfrac{h}{\lambda} \)' + ' (speed c, rest mass zero)')
d.basic('Useful shortcuts: photon energy in eV and momentum?', 'E (eV) ≈ ' + T('1240 / λ (nm)') + '; p = E/c. e.g. 620 nm → 2 eV')
d.basic('Photon picture: five key points?', '(1) Light acts as particles in interactions. (2) E = hν, p = hν/c, speed c. (3) ' + T('Energy independent of intensity') + ' (intensity = photons per second per area). (4) Photons are ' + T('neutral') + ' (not deflected by E or B). (5) Energy and momentum conserved in collisions; photon ' + T('number need not be'))
d.basic('Which experiment confirmed the particle nature of light (momentum)?', T('Compton') + ' scattering of X-rays by electrons (Compton, 1923–24; NCERT says 1924)')
d.basic('Intensity in the photon picture?', r'\( I = \dfrac{N\,h\nu}{A\,t} \)' + ': number of photons crossing unit area per second × energy per photon')
steps_card(d, 'Example 11.1 · laser photons', 'Find the missing step.', 'Laser light of ν = 6.0 × 10¹⁴ Hz emits 2.0 mW. Find the photon energy and the photons emitted per second.',
           ['E = hν = 6.63 × 10⁻³⁴ × 6.0 × 10¹⁴ = <b>3.98 × 10⁻¹⁹ J</b>', 'P = N E', 'N = P/E = 2.0 × 10⁻³/3.98 × 10⁻¹⁹', '<b>N ≈ 5.0 × 10¹⁵ photons/s</b>'], 3,
           'Photons per second from a laser (Example 11.1)', 'E = 3.98 × 10⁻¹⁹ J; N = 5.0 × 10¹⁵ per second')
steps_card(d, 'Example 11.2 · caesium', 'Find the missing step.', 'Work function of caesium = 2.14 eV. (a) Threshold frequency. (b) Wavelength of light whose stopping potential is 0.60 V.',
           ['(a) ν₀ = φ₀/h = 2.14 × 1.6 × 10⁻¹⁹/6.63 × 10⁻³⁴ = <b>5.16 × 10¹⁴ Hz</b>', '(b) eV₀ = hc/λ − φ₀ → λ = hc/(eV₀ + φ₀)', 'eV₀ + φ₀ = 0.60 + 2.14 = 2.74 eV', 'λ = 1240/2.74 nm ≈ <b>454 nm</b>'], 1,
           'Threshold and stopping potential for caesium (Example 11.2)', 'ν₀ = 5.16 × 10¹⁴ Hz; λ ≈ 454 nm')

# ---------------------------------------------------------------- 11.8 Wave nature of matter
d.sec('11.8-wave-nature-of-matter')
d.basic('Wave or particle: which description for what?', 'Interference, diffraction, polarisation: ' + T('wave') + '<br>Photoelectric and Compton effects (energy/momentum transfer): ' + T('particle') + '<br>Both matter, e.g. the eye’s lens (wave) and retina (photon)')
d.basic('De Broglie’s hypothesis (1924)?', 'Moving particles have waves associated with them: ' + r'\( \lambda = \dfrac{h}{p} = \dfrac{h}{mv} \)' + '. Reasoned from the symmetry of nature between matter and radiation')
d.basic('Which quantity is the wave attribute and which the particle attribute in λ = h/p?', 'λ is the ' + T('wave') + ' attribute; p is the ' + T('particle') + ' attribute; Planck’s constant h links them')
d.basic('Does the de Broglie relation hold for a photon?', T('Yes') + ': p = hν/c gives λ = h/p = c/ν, the wavelength of the radiation (Exercise 11.11)')
d.basic('Why don’t everyday objects show wave nature?', 'λ = h/mv is ' + T('immeasurably small') + ' for large m: a 0.12 kg ball at 20 m/s has λ ≈ 2.8 × 10⁻³⁴ m')
d.basic('Does the de Broglie wavelength depend on charge?', X('No') + ': only on momentum (mass and speed)')
d.basic('De Broglie wavelength in terms of kinetic energy?', r'\( \lambda = \dfrac{h}{\sqrt{2mK}} \)')
d.basic('De Broglie wavelength of a charged particle accelerated through potential V?', r'\( \lambda = \dfrac{h}{\sqrt{2mqV}} \)')
d.basic('Teacher addition: electron accelerated through V volts. λ?', 'λ ≈ ' + T('12.27/√V Å') + ' (V in volts); proton ≈ 0.286/√V Å; α-particle ≈ 0.101/√V Å')
d.basic('Teacher addition: same kinetic energy: electron, proton, α-particle. Order of λ?', 'λ ∝ 1/√m: ' + T('λ_e > λ_p > λ_α') + '. For the same accelerating voltage λ ∝ 1/√(mq): electron > proton > α')
d.basic('Teacher addition: same de Broglie wavelength: photon energy vs electron kinetic energy?', 'Same p: photon E = pc; electron K = p²/2m. So ' + r'\( \dfrac{E_\gamma}{K_e} = \dfrac{2mc}{p} = \dfrac{2c}{v} \)' + ' (photon much more energetic)')
d.basic('Teacher addition: de Broglie wavelength of a gas molecule at temperature T?', r'\( \lambda = \dfrac{h}{\sqrt{3mkT}} \)' + ' (using ½mv² = 3kT/2 for rms speed); for thermal neutrons, use ' + r'\( \dfrac{h}{\sqrt{2mkT}} \)')
d.basic('Teacher addition: Davisson–Germer experiment (beyond the rationalised NCERT text)?', 'Electrons of 54 eV scattered from a nickel crystal show a strong peak at a scattering angle of ' + N('50°') + ' (Bragg glancing angle 65°): λ = 2d sin θ ≈ 1.65 Å from Bragg’s law matches h/√(2meV), confirming ' + T('electron diffraction'))
d.basic('Teacher addition: uses of matter waves?', T('Electron microscope') + ' (λ ≪ light, so higher resolving power)<br>Neutron and electron diffraction for crystal structure')
d.basic('Points to ponder: what is physically meaningful for a matter wave?', 'Its ' + T('wavelength') + ' and its ' + T('group velocity') + ' (equals the particle’s speed); phase velocity has no physical meaning')
steps_card(d, 'Example 11.3 · electron and ball', 'Find the missing step.', 'de Broglie wavelength of (a) an electron at 5.4 × 10⁶ m/s, (b) a 150 g ball at 30 m/s.',
           ['(a) p = 9.11 × 10⁻³¹ × 5.4 × 10⁶ = <b>4.92 × 10⁻²⁴ kg m/s</b>', 'λ = h/p = 6.63 × 10⁻³⁴/4.92 × 10⁻²⁴ = <b>0.135 nm</b> (X-ray size)', '(b) p = 0.150 × 30 = 4.50 kg m/s', 'λ = 6.63 × 10⁻³⁴/4.50 = <b>1.47 × 10⁻³⁴ m</b> (unmeasurably small)'], 1,
           'Wavelengths of an electron and a ball (Example 11.3)', 'Electron: 0.135 nm; ball: 1.47 × 10⁻³⁴ m')

# ---------------------------------------------------------------- Points to ponder
d.sec('points-to-ponder')
d.basic('Are free electrons in a metal truly free?', 'Free inside the metal (constant potential, approximately) but ' + T('not free to leave') + '.<br>They need extra energy to escape')
d.basic('Do all conduction electrons need the same energy to escape?', X('No') + ': they have an energy distribution (obeying Pauli’s principle). Work function is the ' + T('least') + ' energy for the most loosely bound electron')
d.basic('What does the photoelectric effect strictly show about light?', 'That energy is ' + T('absorbed in discrete units hν') + ' in matter–light interaction.<br>That is not quite the same as saying light is made of particles')
d.basic('What is the crucial discriminator between wave and photon pictures?', 'The ' + T('stopping potential') + ': independent of intensity, dependent on frequency')
table_card(d, 'NCERT quantity table', 'Symbol, unit, dimensions?', [
    ('Planck’s constant h', 'J s; [ML²T⁻¹]; E = hν', False), ('Stopping potential V₀', 'V; [ML²T⁻³A⁻¹]; eV₀ = K_max', False),
    ('Work function φ₀', 'J or eV; [ML²T⁻²]; K_max = E − φ₀', False), ('Threshold frequency ν₀', 'Hz; [T⁻¹]; ν₀ = φ₀/h', False),
    ('de Broglie wavelength λ', 'm; [L]; λ = h/p', False)],
    term='Chapter 11 quantities')

# ---------------------------------------------------------------- Exam patterns
d.sec('exam-patterns')
d.basic('NEET pattern: light of wavelength λ ejects electrons with K_max. If λ is halved, K_max becomes?', 'K′ = 2hc/λ − φ₀ = ' + T('2K + φ₀') + ' (more than doubled). If φ₀ = 0 it doubles')
d.basic('NEET pattern: intensity of light is doubled at fixed ν > ν₀. Change in stopping potential and saturation current?', 'Stopping potential: ' + T('unchanged') + '. Saturation current: ' + T('doubled'))
d.basic('JEE pattern: metal A and B have λ₀ in ratio 1 : 2 (A shorter). Same light on both: which has larger V₀?', 'φ₀ ∝ 1/λ₀, so A has the larger φ₀ and ' + T('B gives the larger stopping potential') + ' (K = hc/λ − φ₀)')
d.basic('JEE pattern: light of frequency ν gives stopping potential V₀; frequency 2ν gives 3V₀. Find ν₀ in terms of ν.', 'eV₀ = hν − φ₀ and 3eV₀ = 2hν − φ₀. Subtract: 2eV₀ = hν, so φ₀ = hν − hν/2 = hν/2: ' + N('ν₀ = ν/2'))
d.basic('JEE pattern: given the V₀ vs ν graph, find h and φ₀.', 'Slope = h/e, so h = e × slope; intercept on the ν-axis = ν₀; φ₀ = hν₀ = e × |intercept on the V₀-axis|')
d.basic('Board pattern: state three observations that wave theory cannot explain.', 'K_max independent of intensity; threshold frequency; instantaneous emission')
d.basic('Board pattern: why does a photocell need a quartz window for zinc?', 'Zinc responds only to ' + T('UV') + ', which quartz transmits and glass absorbs')
d.basic('Pattern: what is the momentum of a 6.63 × 10⁻²⁷ J photon?', 'p = E/c = 6.63 × 10⁻²⁷/3 × 10⁸ = ' + N('2.2 × 10⁻³⁵ kg m/s'))
d.basic('Pattern: relation between de Broglie wavelengths of two particles with masses m and 4m at the same kinetic energy?', 'λ ∝ 1/√m, so λ₁/λ₂ = ' + N('2 : 1'))
d.basic('Pattern: electron accelerated through 100 V. λ?', '12.27/√100 = ' + N('1.23 Å') + ' (about the spacing between atoms in a crystal)')
d.basic('Pattern: effect of accelerating voltage doubling on the electron’s λ?', 'λ ∝ 1/√V, so λ falls by a factor ' + N('√2') + ' (to 0.707 of its value)')

# ---------------------------------------------------------------- Exercises
d.sec('exercises')
d.basic('Exercise 11.1: X-rays produced by 30 kV electrons: maximum frequency and minimum wavelength?', 'eV = hν_max → ν_max = 30 × 10³ × 1.6 × 10⁻¹⁹/6.63 × 10⁻³⁴ = ' + N('7.24 × 10¹⁸ Hz') + '; λ_min = c/ν_max = ' + N('0.041 nm'))
d.basic('Exercise 11.2: Cs (φ₀ = 2.14 eV) with light of 6 × 10¹⁴ Hz. K_max, V₀, v_max?', 'hν = 2.48 eV, so K_max = ' + N('0.34 eV') + ' (0.54 × 10⁻¹⁹ J); V₀ = ' + N('0.34 V') + '; v = √(2K/m) ≈ ' + N('3.4 × 10⁵ m/s') + ' (key: 344 km/s)')
d.basic('Exercise 11.3: cut-off voltage 1.5 V. K_max?', 'K_max = eV₀ = ' + N('1.5 eV') + ' = 2.4 × 10⁻¹⁹ J')
steps_card(d, 'Exercise 11.4 · He–Ne laser', 'Find the missing step.', 'λ = 632.8 nm, power 9.42 mW. (a) Energy and momentum of a photon (b) photons per second (c) speed of a hydrogen atom with the same momentum.',
           ['(a) E = hc/λ = 3.14 × 10⁻¹⁹ J (1.96 eV); p = h/λ = <b>1.05 × 10⁻²⁷ kg m/s</b>', '(b) N = P/E = 9.42 × 10⁻³/3.14 × 10⁻¹⁹ = <b>3 × 10¹⁶ per second</b>', '(c) m_H = 1.67 × 10⁻²⁷ kg', 'v = p/m_H = <b>0.63 m/s</b>'], 3,
           'Photon energy, momentum and rate (Exercise 11.4)', 'E = 3.14 × 10⁻¹⁹ J, p = 1.05 × 10⁻²⁷ kg m/s, N = 3 × 10¹⁶/s, v = 0.63 m/s')
d.basic('Exercise 11.5: slope of V₀ vs ν = 4.12 × 10⁻¹⁵ V s. h?', 'Slope = h/e → h = 4.12 × 10⁻¹⁵ × 1.6 × 10⁻¹⁹ = ' + N('6.59 × 10⁻³⁴ J s'))
d.basic('Exercise 11.6: ν₀ = 3.3 × 10¹⁴ Hz, ν = 8.2 × 10¹⁴ Hz. Cut-off voltage?', 'V₀ = h(ν − ν₀)/e = 6.63 × 10⁻³⁴ × 4.9 × 10¹⁴/1.6 × 10⁻¹⁹ = ' + N('≈ 2.0 V'))
d.basic('Exercise 11.7: φ₀ = 4.2 eV, radiation of 330 nm. Photoemission?', 'E = 1240/330 = 3.76 eV < 4.2 eV (equivalently ν < ν₀): ' + X('No emission'))
d.basic('Exercise 11.8: ν = 7.21 × 10¹⁴ Hz gives v_max = 6.0 × 10⁵ m/s. Threshold frequency?', 'hν₀ = hν − ½mv² = 4.78 × 10⁻¹⁹ − 1.64 × 10⁻¹⁹ = 3.14 × 10⁻¹⁹ J → ' + N('ν₀ = 4.73 × 10¹⁴ Hz'))
d.basic('Exercise 11.9: 488 nm light, V₀ = 0.38 V. Work function?', 'hc/λ = 1240/488 = 2.54 eV; φ₀ = 2.54 − 0.38 = ' + N('2.16 eV') + ' (3.46 × 10⁻¹⁹ J)')
d.basic('Exercise 11.10: de Broglie wavelength of (a) 0.040 kg bullet at 1 km/s, (b) 0.060 kg ball at 1 m/s, (c) 1.0 × 10⁻⁹ kg dust at 2.2 m/s?', '(a) ' + N('1.7 × 10⁻³⁵ m') + ' (b) ' + N('1.1 × 10⁻³² m') + ' (c) p = 2.2 × 10⁻⁹, so λ = ' + N('3.0 × 10⁻²⁵ m') + '. All immeasurably small')
d.basic('Correction: NCERT’s key prints 3.0 × 10⁻²³ m for Exercise 11.10(c). Right?', X('Slip') + ': 6.63 × 10⁻³⁴/(1.0 × 10⁻⁹ × 2.2) = ' + T('3.0 × 10⁻²⁵ m') + '<br>(3.0 × 10⁻²³ m would need m = 10⁻¹¹ kg.)<br>The conclusion is the same')
d.basic('Exercise 11.11: show that the de Broglie wavelength of a photon equals the wavelength of the radiation.', 'λ = h/p, and p = hν/c for a photon, so λ = h/(hν/c) = ' + T('c/ν') + ' = the wavelength of the em wave')

# ---------------------------------------------------------------- Summary
d.sec('summary')
table_card(d, 'Summary', 'Formula?', [
    ('Photon energy', 'E = hν = hc/λ = 1240/λ(nm) eV', False), ('Photon momentum', 'p = h/λ = E/c', False), ('Stopping potential', 'eV₀ = K_max', False),
    ('Einstein’s equation', 'K_max = hν − φ₀', False), ('Threshold frequency', 'ν₀ = φ₀/h', False), ('V₀ vs ν', 'V₀ = (h/e)(ν − ν₀); slope h/e', False),
    ('de Broglie', 'λ = h/p = h/mv', False), ('Through potential V', 'λ = h/√(2mqV); electron 12.27/√V Å', False)],
    term='Chapter 11 formula sheet')
table_card(d, 'Concept checks', 'True or false?', [
    ('K_max of photoelectrons increases with intensity', 'False (increases with frequency)', True), ('Saturation current is proportional to intensity', 'True', False),
    ('Photons are deflected by a magnetic field', 'False (neutral)', True), ('de Broglie wavelength depends on the charge of the particle', 'False', True),
    ('Different metals give parallel V₀–ν lines', 'True', False), ('Photoemission has a measurable time lag for dim light', 'False (instantaneous)', True)],
    term='Chapter 11 concept checks')

print(d.write(os.path.join(OUT, 'deck.json')), 'cards')
