import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase_phy as sp

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Physics', 'class12-physics-ch10-wave-optics')
d = Deck('Chapter 10: Wave Optics', 'Class 12', ['class-12', 'physics', 'ch-10'])
d.description = 'Huygens principle, interference, Young’s double slit, single-slit diffraction, polarisation and Malus’s law'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- 10.1 Introduction
d.sec('10.1-introduction')
d.basic('Corpuscular vs wave model: what does each predict for the speed of light in water?', 'Corpuscular (Descartes/Newton): light is ' + X('faster') + ' in the denser medium. Wave (Huygens): ' + T('slower') + '. Foucault (1850) measured slower in water, so the wave model won')
d.basic('Who proposed the wave theory of light and when? Who firmly established it?', T('Huygens') + ' (1678); ' + T('Young’s') + ' interference experiment (1801) established it')
d.basic('Why was the wave theory accepted slowly?', 'Newton’s authority, and the belief that a wave needs a ' + T('medium') + ' (light crosses vacuum). Maxwell’s EM theory removed the difficulty')
d.basic('What is geometrical optics?', 'The branch that neglects the ' + T('finite wavelength') + ' (λ → 0); a ray is the path of energy propagation in that limit')
d.basic('Why can light be treated as rays in mirrors and lenses?', 'λ ≈ ' + N('0.6 µm') + ' (yellow) is tiny compared with the dimensions of typical mirrors and lenses')
d.basic('Wave optics covers which phenomena?', T('Interference') + ', ' + T('diffraction') + ' and ' + T('polarisation') + ' (plus derivation of reflection and refraction by Huygens’ principle)')

# ---------------------------------------------------------------- 10.2 Huygens principle
d.sec('10.2-huygens-principle')
d.basic('Define a wavefront.', 'A surface of ' + T('constant phase') + ' (all points oscillate in phase). Energy travels ' + T('perpendicular') + ' to the wavefront (along rays)')
d.basic('Shape of wavefronts: point source, line source, very distant source?', 'Point source: ' + T('spherical') + '<br>Line (slit) source: ' + T('cylindrical') + '<br>Very distant source: ' + T('plane') + ' (a small piece of a huge sphere)', **fig('fig_10_1a_spherical'))
d.basic('Plane wavefront: rays and wavefronts?', 'Rays are ' + T('parallel straight lines perpendicular') + ' to the parallel plane wavefronts', **fig('fig_10_1b_plane'))
d.basic('State Huygens’ principle.', 'Every point of a wavefront is a source of ' + T('secondary wavelets') + ' spreading with the speed of the wave.<br>The new wavefront is the ' + T('forward envelope') + ' (common tangent) of the wavelets after time t')
d.basic('Huygens’ construction for a spherical wavefront: how do you find the wavefront after time t?', 'Draw spheres of radius ' + T('vt') + ' from every point of the old wavefront; draw their common tangent (G₁G₂)', **fig('fig_10_2_huygens'))
d.basic('Why does Huygens’ principle seem to give a “backwave”? How was it dealt with?', 'The envelope also gives D₁D₂ going backwards. Huygens assumed ad hoc that wavelet amplitude is ' + T('maximum forward, zero backward') + '; a rigorous wave theory justifies its absence')
d.basic('Huygens’ construction for a plane wave?', 'The new wavefront is another plane parallel to the old one, at distance ' + T('vt'), **fig('fig_10_3_plane_huygens'))

d.sec('10.3-refraction-and-reflection-of-plane-waves')
d.basic('Huygens’ derivation of Snell’s law: setup and result?', 'Wavefront AB reaches the surface at C after time τ: BC = v₁τ. From A a wavelet radius v₂τ; tangent CE is the refracted wavefront. sin i = v₁τ/AC, sin r = v₂τ/AC → ' + r'\( \dfrac{\sin i}{\sin r} = \dfrac{v_1}{v_2} \)', **fig('fig_10_4_refraction'))
d.basic('With n = c/v, what form does Snell’s law take?', T('n₁ sin i = n₂ sin r'))
d.basic('What does the wave theory conclude if the ray bends towards the normal?', T('v₂ < v₁') + ': the light is slower in the second medium. The corpuscular model predicted the opposite')
d.basic('What changes and what stays the same on refraction: speed, wavelength, frequency?', 'Speed and wavelength ' + T('decrease') + ' entering a denser medium; ' + T('frequency stays the same') + ': ' + r'\( \dfrac{v_1}{v_2} = \dfrac{\lambda_1}{\lambda_2} \)')
d.basic('Refraction into a rarer medium: what does the wavefront construction show?', 'The ray bends ' + T('away') + ' from the normal; critical angle ' + r'\( \sin i_c = \dfrac{n_2}{n_1} \)' + '; beyond it, total internal reflection', **fig('fig_10_5_rarer'))
d.basic('Derive the law of reflection with Huygens’ principle.', 'Triangles EAC and BAC are congruent (AE = BC = vt, common AC, right angles), so ' + T('∠i = ∠r'), **fig('fig_10_6_reflection'))
d.basic('How does a thin prism tilt a plane wavefront?', 'Light is slower in glass, so the part crossing more glass is ' + T('delayed more') + ' and the emerging wavefront tilts', **fig('fig_10_7_wavefronts'))
d.basic('How does a convex lens turn a plane wavefront into a spherical one?', 'The centre traverses the thickest glass and is ' + T('delayed most') + '.<br>The emerging front is depressed at the centre, converging spherically to F')
d.basic('A concave mirror reflects a plane wave. Emerging wavefront?', 'A ' + T('spherical wave converging to F') + ' (radius of curvature R/2)')
d.basic('Fermat-type conclusion from Huygens’ construction?', 'The ' + T('time of travel is the same along every ray') + ' from an object point to its image point.<br>(The slower path through the thick centre of a lens compensates for its shorter length)')
d.basic('Example 10.1(a): why do reflected and refracted light have the same frequency as the incident light?', 'Atoms act as ' + T('forced oscillators') + ' and re-radiate at the driving frequency')
d.basic('Example 10.1(b): light slows on entering a denser medium. Does it lose energy?', X('No') + ': energy depends on amplitude (and frequency), not on the speed of propagation')
d.basic('Example 10.1(c): what fixes intensity in the photon picture?', 'The ' + T('number of photons') + ' crossing unit area per unit time (for a given frequency)')

# ---------------------------------------------------------------- 10.4 Coherent and incoherent addition
d.sec('10.4-coherent-and-incoherent-addition-of-waves')
d.basic('State the principle of superposition.', 'At a point, the resultant displacement is the ' + T('sum of the displacements') + ' produced by each wave')
d.basic('When are two sources coherent?', 'When the ' + T('phase difference between them stays constant in time') + ' (same frequency needed)', **fig('fig_10_8b_ripple'))
d.basic('Two coherent sources in phase: what happens at a point equidistant from both?', 'y = 2a cos ωt, so I = ' + N('4I₀') + ' (constructive interference)')
d.basic('Path difference for constructive interference?', r'\( \Delta x = n\lambda,\ n = 0, 1, 2, \dots \)' + '; phase difference φ = 0, 2π, 4π, …', **fig('fig_10_9a_constructive'))
d.basic('Path difference for destructive interference?', r'\( \Delta x = \left(n+\tfrac12\right)\lambda \)' + '; φ = π, 3π, 5π, …; resultant intensity zero', **fig('fig_10_9b_destructive'))
d.basic('Relation between path difference and phase difference?', r'\( \phi = \dfrac{2\pi}{\lambda}\,\Delta x \)')
d.basic('Resultant intensity for a general phase difference φ (equal amplitudes)?', r'\( I = 4I_0\cos^2\!\dfrac{\phi}{2} \)' + ' (resultant amplitude 2a cos(φ/2))')
sp.interference_phase_stages(d)
d.basic('Incoherent sources: resultant intensity?', 'Intensities just add: ' + r'\( I = 2I_0 \)' + ' everywhere (no stable pattern)')
d.basic('Interference and energy conservation?', 'Energy is only ' + T('redistributed') + ': dark fringes lose what bright fringes gain; average intensity is still 2I₀')
d.basic('Locus of points with constant path difference from two sources?', T('Hyperbolas') + ' with the sources as foci; n = 0 is the perpendicular bisector', **fig('fig_10_10_hyperbolas'))
d.basic('Teacher addition: resultant intensity for two waves of amplitudes a₁, a₂ with phase difference φ?', r'\( I = I_1 + I_2 + 2\sqrt{I_1I_2}\cos\phi \)' + ', so ' + r'\( \dfrac{I_{max}}{I_{min}} = \left(\dfrac{a_1+a_2}{a_1-a_2}\right)^2 \)')
d.basic('Teacher addition: intensity ratio 9:1 for two sources. I_max/I_min?', 'a₁/a₂ = 3/1: ' + r'\( \dfrac{(3+1)^2}{(3-1)^2} = 4 \)' + ', i.e. 16:4 = ' + N('4:1'))
d.basic('Teacher addition: how does slit width relate to intensity and amplitude?', 'Intensity ∝ slit width w; amplitude ∝ √w. Slits of widths 4w and w give I ratio 4:1, amplitude ratio 2:1, fringe visibility ' + r'\( \dfrac{I_{max}-I_{min}}{I_{max}+I_{min}} = \dfrac{2\sqrt{I_1I_2}}{I_1+I_2} \)')
d.basic('Exam trap: can two independent sodium lamps produce fringes? Why not?', X('No') + ': ordinary sources change phase abruptly in about ' + N('10⁻¹⁰ s') + ', so two lamps are ' + T('incoherent') + ' and intensities add', **fig('fig_10_11_two_lamps'))

# ---------------------------------------------------------------- 10.5 Young's experiment
d.sec('10.5-interference-of-light-waves-and-youngs-experiment')
d.basic('How did Young make two coherent light sources?', 'Two pinholes/slits S₁ and S₂ illuminated by the ' + T('same source S') + '.<br>Phase changes in S appear identically in both, so they are locked in phase', **fig('fig_10_12_young'))
d.basic('Young’s double slit: position of the nth bright fringe?', r'\( x_n = \dfrac{n\lambda D}{d},\ n = 0, \pm1, \pm2, \dots \)' + ' (d = slit separation, D = screen distance)')
d.basic('Position of the nth dark fringe?', r'\( x_n = \left(n+\tfrac12\right)\dfrac{\lambda D}{d} \)')
d.basic('Derive x_n = nλD/d.', 'Path difference to point P at height x: ' + T('Δ = S₂P − S₁P ≈ xd/D') + ' (for d ≪ D). Set Δ = nλ for bright fringes and (n + ½)λ for dark ones')
d.basic('Fringe width β?', r'\( \beta = \dfrac{\lambda D}{d} \)' + ': bright and dark fringes are ' + T('equally spaced') + ', each of width β', **fig('fig_10_13_fringes'))
d.basic('Fringe width: effect of increasing d, D, λ?', 'β ∝ λD/d: ' + T('increases with λ and D') + ', ' + T('decreases with d'))
d.basic('Angular fringe width?', r'\( \theta = \dfrac{\beta}{D} = \dfrac{\lambda}{d} \)' + ' (independent of D)')
d.basic('Fringe width if the whole apparatus is immersed in a liquid of index n?', r'\( \beta' + "' = \\dfrac{\\beta}{n} \\)" + ': λ shrinks to λ/n, so fringes get ' + T('narrower'))
d.basic('Teacher addition: red vs blue light in the same setup?', 'β_red > β_blue (λ_red is longer): the ' + T('red fringes are wider'))
d.basic('Teacher addition: white light in Young’s experiment?', T('Central fringe white') + ' (all colours in phase); the first fringes are coloured with violet nearest the centre and red farthest; only a few fringes are visible before they overlap')
d.basic('Teacher addition: a thin transparent sheet (thickness t, index μ) covers one slit. Fringe shift?', 'Extra path (μ − 1)t: pattern shifts by ' + r'\( \Delta x = \dfrac{(\mu-1)tD}{d} \)' + ' towards the covered slit (= (μ − 1)t/λ fringes)')
d.basic('Teacher addition: the central maximum when the source S moves off the axis?', 'The fringe pattern shifts ' + T('in the opposite direction') + ' to keep the total path difference zero')
d.basic('Teacher addition: conditions for sustained interference?', 'Coherent sources, same frequency, comparable amplitudes, slit separation d ≪ D, and narrow (point/line) slits')
d.basic('Teacher addition: what happens to the fringes if one slit is closed?', 'Fringes disappear; a broad ' + T('single-slit diffraction') + ' pattern remains')
d.basic('Teacher addition: intensity at a point where path difference = λ/4 if the maximum intensity is I_max?', 'φ = π/2 → I = I_max cos²(π/4) = ' + N('I_max/2'))
steps_card(d, 'Exercise 10.4 · finding λ', 'Find the missing step.', 'Slits 0.28 mm apart, screen 1.4 m away. Distance between the central bright fringe and the 4th bright fringe = 1.2 cm. Find λ.',
           ['x₄ = 4λD/d → λ = x₄ d/(4D)', 'λ = (1.2 × 10⁻² × 0.28 × 10⁻³)/(4 × 1.4)', 'λ = 3.36 × 10⁻⁶/5.6 = <b>6.0 × 10⁻⁷ m</b>', 'λ = <b>600 nm</b>'], 2,
           'Young’s double slit, λ from fringes (Exercise 10.4)', 'λ = 600 nm')
steps_card(d, 'Exercise 10.5 · intensity at λ/3', 'Find the missing step.', 'Intensity at a point where the path difference is λ is K. Find the intensity where it is λ/3.',
           ['Path difference λ → φ = 2π: I = 4I₀ cos²(π) = 4I₀ = K, so <b>I₀ = K/4</b>', 'Path difference λ/3 → φ = 2π/3', 'I = 4I₀ cos²(π/3) = 4I₀ × (1/4) = I₀', '<b>I = K/4</b>'], 1,
           'Intensity at different path differences (Exercise 10.5)', 'I = K/4')
steps_card(d, 'Exercise 10.6 · two wavelengths', 'Find the missing step.', 'Wavelengths 650 nm and 520 nm are used in Young’s experiment. (a) Third bright fringe of 650 nm from the centre. (b) Least distance where bright fringes of both coincide. (Key uses D/d = 600.)',
           ['(a) x₃ = 3λD/d = 3 × 650 × 10⁻⁹ × 600 = <b>1.17 mm</b>', '(b) Coincide when n₁ × 650 = n₂ × 520 → n₁ : n₂ = 4 : 5', 'Least common fringe: n₁ = 4 for 650 nm (n₂ = 5 for 520 nm)', 'x = 4 × 650 × 10⁻⁹ × 600 = <b>1.56 mm</b>'], 1,
           'Coinciding fringes of two colours (Exercise 10.6)', '(a) 1.17 mm, (b) 1.56 mm')
d.basic('Note on Exercise 10.6: the printed question gives no D or d. What does the key assume?', 'The key’s answers (1.17 mm, 1.56 mm) correspond to ' + T('D/d = 600') + ' (e.g. d = 2 mm and D = 1.2 m, as in earlier editions). Use β = λD/d and the LCM method')

# ---------------------------------------------------------------- 10.6 Diffraction
d.sec('10.6-diffraction')
d.basic('What is diffraction?', 'Bending of waves around obstacles and apertures into the geometrical shadow, producing bright and dark bands.<br>It happens for ' + T('all types of waves'))
d.basic('When is diffraction of light noticeable?', 'When the obstacle or aperture size is ' + T('comparable to λ') + '.<br>Everyday objects are much larger than λ, so we rarely notice it')
d.basic('Where does diffraction limit us?', 'The ' + T('resolution of the eye, telescopes and microscopes') + '; also CD colours are due to diffraction')
d.basic('Single slit (width a), monochromatic light: what pattern appears?', 'A broad ' + T('central maximum') + ' with weaker alternate dark and bright bands on both sides', **fig('fig_10_15_diffraction'))
d.basic('Single-slit diffraction: conditions for minima?', r'\( a\sin\theta = n\lambda \)' + ', i.e. θ ≈ nλ/a, n = ±1, ±2, … (zero intensity)', **fig('fig_10_14_single_slit'))
d.basic('Single-slit diffraction: secondary maxima?', 'Approximately at ' + r'\( \theta \approx \left(n+\tfrac12\right)\dfrac{\lambda}{a} \)' + ', getting weaker with n')
d.basic('Why does a single slit give minima? (path-difference argument)', 'Divide the slit into two halves: pairs of points a/2 apart have path difference (a/2) sin θ.<br>When this is λ/2 (i.e. a sin θ = λ) every pair cancels, giving the ' + T('first minimum'))
d.basic('Angular width of the central maximum of a single slit?', T('2λ/a') + ' (from −λ/a to +λ/a); linear width on a screen at D: ' + r'\( \dfrac{2\lambda D}{a} \)')
d.basic('Single slit: effect of narrowing the slit or increasing λ?', 'Central maximum ' + T('widens') + ' (λ/a grows): more diffraction')
d.basic('Teacher addition: relative intensities of the secondary maxima in a single slit?', 'Central 1 : first secondary ≈ 0.047 : second ≈ 0.017: most energy is in the ' + T('central maximum'))
d.basic('Teacher addition: interference vs diffraction (single slit) in a table?', T('Interference') + ': two/few coherent sources, equal fringe widths, all bright fringes of similar intensity<br>' + T('Diffraction') + ': a single wavefront (many secondary sources), unequal widths (central twice as wide), intensity falls quickly')
d.basic('Feynman on interference vs diffraction (quoted in NCERT)?', 'No specific important physical difference: with ' + T('few sources') + ' it is called interference, with a ' + T('large number') + ' of sources diffraction')
d.basic('The double-slit pattern actually is what?', 'The ' + T('double-slit interference') + ' pattern multiplied by the ' + T('single-slit diffraction envelope') + ' of each slit')
d.basic('Teacher addition: number of interference fringes within the central diffraction maximum (slit separation d, slit width a)?', 'Central maximum width 2λD/a; fringe width λD/d: about ' + r'\( \dfrac{2d}{a} \)' + ' fringes<br>(e.g. d = 5a gives about 10, with missing orders at multiples of d/a)')
d.basic('Teacher addition: Fresnel distance and Rayleigh’s criterion?', 'Ray optics holds for distances up to ' + r'\( z_F = \dfrac{a^2}{\lambda} \)' + '. Two points are just resolved when their angular separation is ' + r'\( 1.22\,\dfrac{\lambda}{D} \)' + ' (aperture D)')
d.basic('Seeing single-slit diffraction at home?', 'Two ' + T('razor blades') + ' held to form a narrow slit parallel to a straight bulb filament.<br>A red filter gives wider fringes than blue', **fig('fig_10_16_blades'))
d.basic('Why can’t you see fringes with direct sunlight (Young’s demonstration at home)?', 'The Sun subtends about ' + N('½°') + ' at the eye: it is not a point/line source, and direct sunlight can damage the eye')
d.basic('Diffraction and energy conservation?', 'Light energy is ' + T('redistributed') + ': what disappears at dark bands appears in bright bands')

# ---------------------------------------------------------------- 10.7 Polarisation
d.sec('10.7-polarisation')
d.basic('Wave on a string vibrating in one plane: what is it called?', T('Plane (linearly) polarised') + ' transverse wave, e.g. y = a sin(kx − ωt) is y-polarised', **fig('fig_10_17a_string'))
d.basic('What is an unpolarised wave?', 'The plane of vibration changes ' + T('randomly and rapidly') + ' while always staying ⟂ to the propagation direction')
d.basic('Which waves can be polarised, and what does this show about light?', 'Only ' + T('transverse') + ' waves. Light can be polarised, so light is transverse (E ⟂ direction of travel); sound in air is longitudinal and cannot be')
d.basic('What is a polaroid?', 'A thin plastic sheet of ' + T('long-chain molecules aligned in one direction') + ' that absorb the E-component along their length.<br>The perpendicular direction is the ' + T('pass axis'))
d.basic('Unpolarised light through one polaroid: what happens to intensity? Does rotating the polaroid matter?', 'Intensity falls to ' + T('half (I₀/2)') + ' and is linearly polarised; rotating the polaroid changes nothing')
d.basic('Two polaroids P₂ then P₁ (the analyser) rotated: what is seen?', 'Transmitted intensity varies from maximum to zero and back: ' + T('two maxima and two minima') + ' per full turn.<br>Crossed (90°) gives zero', **fig('fig_10_18a_polaroids'))
d.basic('State Malus’s law.', r'\( I = I_0\cos^2\theta \)' + ' (I₀ = intensity of polarised light incident on the analyser; θ = angle between pass axes)', **fig('fig_10_18b_polaroids'))
sp.malus_law_stages(d)
d.basic('Derive Malus’s law.', 'Polarised light has E along P₂’s pass axis. The component along P₁’s axis is ' + T('E cos θ') + '; intensity ∝ E², so I = I₀ cos²θ')
d.basic('Unpolarised light I₀ passes through two polaroids with axes at angle θ. Final intensity?', r'\( I = \dfrac{I_0}{2}\cos^2\theta \)')
d.basic('Example 10.2: a polaroid P₂ rotated between crossed polaroids P₁ and P₃. Transmitted intensity?', 'I = I₀ cos²θ cos²(π/2 − θ) = ' + r'\( \dfrac{I_0}{4}\sin^2 2\theta \)' + ': maximum ' + N('I₀/4') + ' at θ = ' + N('45°') + ', zero at 0° and 90°')
d.basic('Exam pattern: unpolarised light of intensity I passes through three polaroids at 0°, 45°, 90°. Output?', 'After P₁: I/2. After P₂ (45°): I/2 × ½ = I/4. After P₃ (45° again): I/4 × ½ = ' + N('I/8'))
d.basic('Teacher addition: polarisation by reflection: Brewster’s law?', 'At the polarising angle ' + r'\( \tan i_B = n \)' + ' the reflected light is completely plane-polarised (E ⟂ plane of incidence) and the reflected and refracted rays are at ' + T('90°') + ' to each other')
d.basic('Teacher addition: Brewster angle for glass n = 1.5 (in air)?', 'tan i_B = 1.5 → ' + N('i_B ≈ 56.3°') + ' (Exercise 10.8 in older editions)')
d.basic('Teacher addition: other ways to polarise light?', 'Scattering (blue sky light is partly polarised)<br>Double refraction (calcite; Huygens explained it)<br>Selective absorption (polaroids)')
d.basic('Uses of polaroids?', 'Sunglasses and windowpanes (cut glare and control intensity), photographic filters, ' + T('3D movies'), )
d.basic('Why do polarised sunglasses reduce glare from a road or water?', 'Glare is ' + T('partly polarised by reflection') + ' (horizontal E); the vertical pass axis blocks most of it')

# ---------------------------------------------------------------- Points to ponder
d.sec('points-to-ponder')
d.basic('The crucial new feature of waves compared with particles?', T('Interference of amplitudes') + ' from different sources, constructive or destructive (Young)')
d.basic('What sets the limit of microscopes and telescopes?', T('Diffraction') + ': the wavelength of light limits how close two objects can be and still be distinguished')
d.basic('Which effects exist for longitudinal waves, and which are exclusive to transverse waves?', 'Interference and diffraction exist for sound too; ' + T('polarisation') + ' is special to transverse waves')

# ---------------------------------------------------------------- Exercises
d.sec('exercises')
steps_card(d, 'Exercise 10.1 · light meets water', 'Find the missing step.', '589 nm light in air strikes water (n = 1.33). Wavelength, frequency and speed of (a) reflected, (b) refracted light.',
           ['ν = c/λ = 3 × 10⁸/589 × 10⁻⁹ = <b>5.09 × 10¹⁴ Hz</b> (same for both)', '(a) Reflected: λ = <b>589 nm</b>, speed <b>3 × 10⁸ m/s</b>', '(b) Refracted: v = c/n = <b>2.26 × 10⁸ m/s</b>', 'λ = v/ν = 2.26 × 10⁸/5.09 × 10¹⁴ ≈ <b>444 nm</b> (= 589/1.33 ≈ 443 nm)'], 3,
           'Reflection and refraction at water (Exercise 10.1)', 'ν = 5.09 × 10¹⁴ Hz; refracted v = 2.26 × 10⁸ m/s, λ ≈ 444 nm')
d.basic('Exercise 10.2: shape of the wavefront for (a) a point source (b) a point source at the focus of a convex lens (c) starlight intercepted by Earth?', '(a) ' + T('Spherical') + '. (b) ' + T('Plane') + ' (parallel beam emerges). (c) ' + T('Plane') + ' (tiny part of a huge sphere)')
d.basic('Exercise 10.3: speed of light in glass (n = 1.5)? Is it colour-independent?', 'v = c/n = ' + N('2.0 × 10⁸ m/s') + '. ' + X('No') + ': n depends on wavelength; n_violet > n_red, so ' + T('violet travels slower') + ' in glass')

# ---------------------------------------------------------------- Summary
d.sec('summary')
table_card(d, 'Summary', 'Formula?', [
    ('Snell from Huygens', 'sin i/sin r = v₁/v₂ = n₂/n₁', False), ('Interference intensity', 'I = 4I₀ cos²(φ/2)', False), ('Bright / dark path difference', 'nλ / (n + ½)λ', False),
    ('Bright fringe position', 'x_n = nλD/d', False), ('Fringe width', 'β = λD/d', False), ('Single-slit minima', 'a sin θ = nλ', False),
    ('Central maximum width', '2λD/a', False), ('Malus’s law', 'I = I₀ cos²θ', False), ('Brewster’s law', 'tan i_B = n', False)],
    term='Chapter 10 formula sheet')
table_card(d, 'Interference vs diffraction', 'Compare.', [
    ('Sources', 'Interference: two coherent sources. Diffraction: one wavefront (many secondary sources)', False),
    ('Fringe widths', 'Interference: equal. Diffraction: central twice the others', False),
    ('Intensity of bright fringes', 'Interference: nearly equal. Diffraction: falls rapidly', False),
    ('Dark fringes', 'Interference: usually zero intensity. Diffraction: not always exactly zero in practice', False)],
    term='Interference and diffraction at a glance')
table_card(d, 'Concept checks', 'True or false?', [
    ('Frequency of light changes on entering water', 'False (λ and v change)', True), ('Two sodium lamps give clear fringes', 'False (incoherent)', True),
    ('In Young’s experiment fringe width increases with λ', 'True', False), ('Sound waves can be polarised', 'False (longitudinal)', True),
    ('Unpolarised light through a polaroid: intensity halves', 'True', False), ('Central maximum of a single slit is as wide as the others', 'False (twice as wide)', True)],
    term='Chapter 10 concept checks')

print(d.write(os.path.join(OUT, 'deck.json')), 'cards')
