import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase_phy as sp

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Physics', 'class12-physics-ch09-ray-optics-and-optical-instruments')
d = Deck('Chapter 9: Ray Optics and Optical Instruments', 'Class 12', ['class-12', 'physics', 'ch-9'])
d.description = 'Mirrors, refraction, total internal reflection, lenses, prisms, microscopes and telescopes with NEET/JEE-style problems'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- 9.1 Introduction
d.sec('9.1-introduction')
d.basic('Speed of light in vacuum: exact value and the value used in problems?', T('2.998 × 10⁸ m/s') + ' (c = 2.99792458 × 10⁸); use ' + N('3 × 10⁸ m/s') + '. It is the maximum speed attainable in nature')
d.basic('Light is a wave, yet appears to travel in straight lines. Why?', 'Its wavelength (~ ' + N('500 nm') + ') is ' + T('tiny compared with everyday objects') + ', so it can be treated as a ray (ray optics)')
d.basic('What is a ray and what is a beam of light?', 'Ray: the straight-line path along which light travels between two points. Beam: a ' + T('bundle of rays'))
d.basic('When does ray optics fail?', 'When the sizes of obstacles or apertures become comparable to λ: then ' + T('diffraction and interference') + ' matter (Chapter 10)')

# ---------------------------------------------------------------- 9.2 Reflection by spherical mirrors
d.sec('9.2-reflection-of-light-by-spherical-mirrors')
d.basic('Laws of reflection?', T('∠i = ∠r') + ' and the incident ray, reflected ray and normal lie in the ' + T('same plane') + '. They hold at every point of any surface', **fig('fig_9_1_reflection'))
d.basic('For a spherical mirror, what is the normal at the point of incidence?', 'The ' + T('radius') + ': the line joining the centre of curvature C to that point')
d.basic('Define pole, centre of curvature, principal axis of a mirror.', 'Pole P: geometric centre of the mirror. Centre of curvature C: centre of the sphere it is part of. Principal axis: the line through P and C')

d.sec('9.2.1-sign-convention')
d.basic('State the Cartesian sign convention.', 'All distances from the ' + T('pole / optical centre') + '. Along the incident light: ' + T('positive') + '; against it: ' + X('negative') + '. Heights above the axis positive, below negative', **fig('fig_9_2_sign'))
d.basic('Sign of u, f, R for a concave mirror with a real object?', 'u ' + X('< 0') + ', f ' + X('< 0') + ', R ' + X('< 0') + ' (all measured against the incident light)')
d.basic('Sign of f and R for a convex mirror?', T('Positive') + ' (focus and centre lie behind the mirror, along the direction of incident light)')
d.basic('Exam trap: object distance and height for a real object in front of a mirror or lens?', 'u is ' + X('always negative') + ' (object on the incident side); height h is positive if the object stands upward')
d.basic('Mnemonic: signs of f for the four devices?', T('Concave mirror −, convex mirror +, convex lens +, concave lens −') + '. Like “C-C-negative, x-x-positive” for mirrors; lenses are the opposite')

d.sec('9.2.2-focal-length-of-spherical-mirrors')
d.basic('Paraxial rays: meaning?', 'Rays close to the principal axis, making ' + T('small angles') + ' with it (so tan θ ≈ θ)')
d.basic('Where does a parallel beam focus for a concave mirror?', 'Rays converge at the ' + T('principal focus F') + ' (real)', **fig('fig_9_3a_concave_focus'))
d.basic('Where does a parallel beam focus for a convex mirror?', 'Reflected rays appear to ' + T('diverge from F behind the mirror') + ' (virtual focus)', **fig('fig_9_3b_convex_focus'))
d.basic('What is the focal plane?', 'The plane through F ⟂ the axis, where a parallel beam at an angle to the axis focuses', **fig('fig_9_3c_focal_plane'))
d.basic('Relation between focal length and radius of curvature?', r'\( f = \dfrac{R}{2} \)')
d.basic('Derive f = R/2.', 'Ray parallel to axis hits M; ∠MCP = θ so ∠MFP = 2θ. tan θ = MD/CD, tan 2θ = MD/FD → for small θ: FD = CD/2, i.e. ' + T('f = R/2'), **fig('fig_9_4a_geometry'))

d.sec('9.2.3-the-mirror-equation')
d.basic('When is an image real, and when virtual?', 'Real: rays actually ' + T('converge') + ' at the point. Virtual: they only ' + T('appear to diverge') + ' from it (cannot be caught on a screen)')
d.basic('Which two rays are easiest to draw for a mirror?', '(i) Parallel to axis → reflects through ' + T('F') + '. (ii) Through ' + T('C') + ' → retraces its path. (iii) Through F → reflects parallel. (iv) At P → reflects with i = r')
d.basic('Mirror equation?', r'\( \dfrac{1}{v} + \dfrac{1}{u} = \dfrac{1}{f} \)' + ' (valid for concave and convex mirrors, real and virtual images)')
d.basic('Linear magnification of a mirror?', r'\( m = \dfrac{h\prime}{h} = -\dfrac{v}{u} \)' + '. m < 0: real, inverted. m > 0: virtual, erect. |m| > 1: magnified', **fig('fig_9_5_concave_real'))
d.basic('Derive the mirror equation (outline).', 'Similar triangles A′B′F ∼ MPF and A′B′P ∼ ABP give (B′P − FP)/FP = B′P/BP. With B′P = −v, FP = −f, BP = −u this becomes ' + T('1/v + 1/u = 1/f'))
d.basic('Concave mirror, virtual image: object between P and F. Nature of image?', T('Virtual, erect, magnified') + ', behind the mirror (used in shaving mirrors)', **fig('fig_9_6a_concave_virtual'))
d.basic('Convex mirror: nature of image for any object position?', T('Always virtual, erect, diminished') + ', between P and F', **fig('fig_9_6b_convex_virtual'))
table_card(d, 'Concave mirror', 'Image formed for object at…?', [
    ('At infinity', 'At F; real, inverted, highly diminished', False), ('Beyond C', 'Between F and C; real, inverted, diminished', False),
    ('At C', 'At C; real, inverted, same size', False), ('Between C and F', 'Beyond C; real, inverted, magnified', False),
    ('At F', 'At infinity; real, inverted, highly magnified', False), ('Between F and P', 'Behind the mirror; virtual, erect, magnified', True)],
    term='Concave mirror: position of object → image')
sp.concave_mirror_walk(d)
d.basic('Uses of concave and convex mirrors?', 'Concave: shaving/make-up mirrors, torches and headlights, dentists’ mirrors, solar cookers. Convex: ' + T('vehicle rear-view mirrors') + ', street lights (wide field of view)')
d.basic('Why do rear-view mirrors use convex mirrors?', 'Always an erect, diminished image and a ' + T('wide field of view'))
d.basic('Example 9.1: lower half of a concave mirror is covered. Effect on the image?', 'The ' + T('whole image') + ' still forms (every point reflects), but its ' + T('intensity is halved'))
d.basic('Example 9.2: why is the image of a phone lying along the principal axis distorted?', 'Different parts are at different u, so different ' + T('magnification') + ' (longitudinal ≠ lateral). Only the part in the plane ⟂ axis keeps its size', **fig('fig_9_7_phone'))
steps_card(d, 'Example 9.3 · concave mirror', 'Find the missing step.', 'Concave mirror of R = 15 cm. Object at (i) 10 cm, (ii) 5 cm. Find v, nature and m.',
           ['f = −R/2 = <b>−7.5 cm</b>', '(i) u = −10: 1/v = 1/f − 1/u = −1/7.5 + 1/10 → <b>v = −30 cm</b>, m = −v/u = <b>−3</b> (real, inverted, magnified)', '(ii) u = −5: 1/v = −1/7.5 + 1/5 → <b>v = +15 cm</b>', 'm = −15/(−5) = <b>+3</b>: virtual, erect, magnified'], 1,
           'Position, nature, magnification (Example 9.3)', 'Case (i): v = −30 cm, m = −3; case (ii): v = +15 cm, m = +3 (virtual)')
d.basic('Example 9.4: jogger approaches a convex side mirror (R = 2 m) at 5 m/s. How does the image speed change?', 'Image speed rises steeply as the jogger nears: 1/280, 1/150, 1/60, 1/10 m/s at 39, 29, 19, 9 m. Since ' + T('v = fu/(u − f)') + ' changes ever faster near the mirror (an “objects are closer than they appear” effect)')
d.basic('Teacher addition: speed of the image relative to the mirror, in terms of the object’s speed?', r'\( v_I = -\dfrac{v^2}{u^2}\,v_O \)' + ' (differentiate 1/v + 1/u = 1/f). The longitudinal magnification is ' + T('m²'))
d.basic('Teacher addition: object at 2f from a concave mirror moves 1 cm towards it. Image position and size change?', 'Longitudinal magnification = m² = 1, so the image moves 1 cm ' + T('away') + ' from the mirror (at C the image and object move equal distances)')
d.basic('Teacher addition: plane mirror in this language?', 'R → ∞, so f → ∞: ' + T('v = −u') + ', m = +1 (virtual, erect, same size, as far behind as the object is in front)')
d.basic('Teacher addition: a plane mirror rotates by θ. Rotation of the reflected ray?', T('2θ') + ' (used in galvanometer lamp-and-scale arrangements)')

# ---------------------------------------------------------------- 9.3 Refraction
d.sec('9.3-refraction')
d.basic('What is refraction?', 'Change in the ' + T('direction') + ' of a ray as it passes obliquely into another transparent medium (speed changes; frequency does not)', **fig('fig_9_8_refraction'))
d.basic('State Snell’s laws.', '(i) Incident ray, refracted ray and normal are coplanar. (ii) ' + r'\( \dfrac{\sin i}{\sin r} = n_{21} \)' + ' (constant for the pair of media and the wavelength)')
d.basic('Meaning of n₂₁ and its relation to speeds?', 'Refractive index of medium 2 w.r.t. 1: ' + r'\( n_{21} = \dfrac{n_2}{n_1} = \dfrac{v_1}{v_2} \)')
d.basic('Absolute refractive index?', r'\( n = \dfrac{c}{v} \)' + ' (medium’s index w.r.t. vacuum); for two media: n₂₁ = n₂/n₁')
d.basic('Denser medium: bending of the ray?', 'Entering a denser medium (n₂₁ > 1): ray bends ' + T('towards') + ' the normal (r < i). Into a rarer medium: ' + T('away') + ' (r > i)')
d.basic('Optical density vs mass density?', 'Optical density is the ratio of ' + T('speeds of light') + '; not mass per volume. Turpentine has lower mass density than water but higher optical density')
d.basic('Relations among n₁₂, n₂₁ and n₃₁?', T('n₁₂ = 1/n₂₁') + ', and ' + T('n₃₁ = n₃₂ × n₂₁'))
d.basic('What changes and what stays the same for light entering glass from air?', 'Speed and wavelength ' + T('decrease') + ' (λ_m = λ/n); frequency ' + T('unchanged') + ', so colour is unchanged')
d.basic('Parallel-sided glass slab: deviation and lateral shift?', T('Emergent ray is parallel') + ' to the incident ray (no deviation) but ' + T('laterally shifted'), **fig('fig_9_9_slab'))
d.basic('Teacher addition: lateral shift by a slab of thickness t?', r'\( d = \dfrac{t\sin(i-r)}{\cos r} \)' + '; zero for normal incidence, max as i → 90°')
d.basic('Apparent depth (near-normal viewing)?', r'\( \text{apparent depth} = \dfrac{\text{real depth}}{n} \)'.replace(r'\text{apparent depth}', 'h_app').replace(r'\text{real depth}', 'h_real') + ': a tank of depth h_real appears raised to h_real/n', **fig('fig_9_10_apparent_depth'))
d.basic('Teacher addition: apparent shift of the bottom of a tank of depth h?', r'\( h\left(1-\dfrac{1}{n}\right) \)' + ' (raised). For a glass slab of thickness t viewed normally: shift t(1 − 1/n) as well')
d.basic('Teacher addition: an object at depth in medium 1 (n₁) seen from medium 2 (n₂). Apparent depth?', 'h_app = h × (n₂/n₁) (viewer’s medium over object’s medium). Layered media: apparent depth = Σ tᵢ/nᵢ')
d.basic('Exam trap: does the apparent depth depend on how deep the observer is above the water?', X('No') + ' (for near-normal viewing). It depends only on n and real depth; oblique viewing distorts it')

# ---------------------------------------------------------------- 9.4 TIR
d.sec('9.4-total-internal-reflection')
d.basic('What happens to a ray going from a denser to a rarer medium as i increases?', 'The refracted ray bends away from the normal until r = ' + N('90°') + ' at i = i_c; beyond that ' + T('no refraction: total internal reflection'), **fig('fig_9_11_tir'))
d.basic('Define the critical angle.', 'The angle of incidence in the denser medium for which the angle of refraction is ' + T('90°'))
d.basic('Critical angle formula?', r'\( \sin i_c = \dfrac{n_2}{n_1} = \dfrac{1}{n_{12}} \)' + ' (n₁ denser, n₂ rarer); against air: sin i_c = 1/n')
d.basic('Two conditions for TIR?', '(1) light goes from a ' + T('denser to a rarer') + ' medium; (2) angle of incidence ' + T('> i_c'))
d.basic('Critical angles with respect to air (Table 9.1)?', 'Water (1.33): ' + N('48.75°') + '; crown glass (1.52): ' + N('41.14°') + '; dense flint (1.62): ' + N('37.31°') + '; diamond (2.42): ' + N('24.41°'))
d.basic('Why does diamond sparkle?', 'Its very small critical angle (' + N('24.4°') + ') means light entering is ' + T('totally internally reflected many times') + ' before emerging')
d.basic('Difference between ordinary reflection and TIR in intensity?', 'Ordinary reflection always loses some light to transmission. TIR has ' + T('no transmission') + ': reflected intensity ≈ 100%')
sp.tir_angle_sweep(d)
d.basic('Demonstrating TIR with a laser pointer and turbid water?', 'Milk makes the beam visible. Aiming it up at the surface: partial reflection and refraction; at a shallow angle: ' + T('TIR') + ' (same as light along a test tube or optical fibre)', **fig('fig_9_12b_laser'))
d.basic('Prism that bends light by 90°: condition on i_c?', 'A right-angled isosceles prism (45°–45°–90°) works if ' + T('i_c < 45°') + ': true for crown and flint glass', **fig('fig_9_13a_prism90'))
d.basic('Prism to turn light by 180° and to invert an image?', 'Two TIRs at the 45° faces reverse the beam (180°); the arrangement of Fig 9.13(c) ' + T('inverts the image') + ' without changing size (binoculars, periscopes)', **fig('fig_9_13b_prism180'))
d.basic('Optical fibre: structure and principle?', T('Core') + ' of high n inside a ' + T('cladding') + ' of lower n; light undergoes repeated ' + T('TIR') + ' along the length', **fig('fig_9_14_fibre'))
d.basic('Why is there little loss in an optical fibre?', 'TIR at each reflection (no transmission) and very pure quartz: > 95% of light survives 1 km')
d.basic('Uses of optical fibres?', 'Telecommunication signals, ' + T('endoscopy') + ' (light pipe for esophagus, stomach, intestine), decorative lamps, sensors')
d.basic('Natural examples of TIR?', T('Mirage') + ', sparkle of diamond, shine of an air bubble in water, glittering of a cracked glass')
d.basic('Exam trap: a fibre has core n = 1.5 and cladding n = 1.4. What condition ensures TIR inside?', 'Angle of incidence on the core–cladding boundary must exceed i_c = ' + N('sin⁻¹(1.4/1.5) ≈ 69°') + ', i.e. the ray stays close to the axis')
d.basic('Teacher addition: numerical aperture / acceptance angle of a fibre?', r'\( \sin i_{max} = \sqrt{n_{core}^2 - n_{clad}^2} \)' + ' (light entering from air within this cone is guided)')

# ---------------------------------------------------------------- 9.5 Spherical surfaces and lenses
d.sec('9.5-refraction-at-spherical-surfaces-and-by-lenses')
d.basic('What is a thin lens?', 'A transparent medium bounded by two surfaces (at least one spherical) whose ' + T('thickness is small') + ' compared with the radii of curvature and distances')

d.sec('9.5.1-refraction-at-a-spherical-surface')
d.basic('Refraction at a single spherical surface: formula?', r'\( \dfrac{n_2}{v} - \dfrac{n_1}{u} = \dfrac{n_2 - n_1}{R} \)' + ' (light from n₁ to n₂; u, v, R with the Cartesian convention)', **fig('fig_9_15_spherical'))
d.basic('Derive the formula (outline).', 'i = ∠NOM + ∠NCM, r = ∠NCM − ∠NIM (small angles). Snell: n₁i = n₂r. Substituting tan ≈ angle and signs OM = −u, MI = +v, MC = +R gives ' + T('n₂/v − n₁/u = (n₂ − n₁)/R'))
steps_card(d, 'Example 9.5 · glass surface', 'Find the missing step.', 'Point source in air 100 cm from a spherical glass surface (n = 1.5, R = +20 cm). Find the image.',
           ['n₁ = 1, n₂ = 1.5, u = −100, R = +20', 'n₂/v − n₁/u = (n₂ − n₁)/R → 1.5/v + 1/100 = 0.5/20', '1.5/v = 0.025 − 0.01 = 0.015', '<b>v = +100 cm</b>: image forms 100 cm inside the glass, along the incident light'], 2,
           'Single spherical refracting surface (Example 9.5)', 'v = +100 cm')
d.basic('Teacher addition: plane refracting surface (R → ∞)?', T('n₂/v = n₁/u') + ', i.e. v/u = n₂/n₁ (this reproduces apparent depth)')

d.sec('9.5.2-refraction-by-a-lens')
d.basic('How do you get the lens formula from two spherical surfaces?', 'Image of the first surface acts as (virtual) object for the second. Adding the two equations for a thin lens gives ' + T('1/v − 1/u = (n₂/n₁ − 1)(1/R₁ − 1/R₂)'), **fig('fig_9_16a_lens'))
d.basic('First and second surface images for a double-convex lens?', 'First surface: real image I₁, which is a ' + T('virtual object') + ' for the second surface, which forms the final image I', **fig('fig_9_16b_first_surface'))
d.basic('Lens maker’s formula (lens of index n in air)?', r'\( \dfrac{1}{f} = (n-1)\left(\dfrac{1}{R_1} - \dfrac{1}{R_2}\right) \)' + ' (sign convention; true for concave lenses too)', **fig('fig_9_16c_second_surface'))
d.basic('Lens maker’s formula when the lens (n₂) is in a medium (n₁)?', r'\( \dfrac{1}{f} = \left(\dfrac{n_2}{n_1} - 1\right)\left(\dfrac{1}{R_1} - \dfrac{1}{R_2}\right) \)')
d.basic('Signs of R₁ and R₂ for a double convex lens? Double concave?', 'Biconvex: R₁ ' + T('> 0') + ', R₂ ' + X('< 0') + ' (so f > 0). Biconcave: R₁ < 0, R₂ > 0 (f < 0)')
d.basic('Thin lens formula?', r'\( \dfrac{1}{v} - \dfrac{1}{u} = \dfrac{1}{f} \)' + ' (all signs by Cartesian convention). Note the minus sign, unlike the mirror’s plus')
d.basic('Exam trap: mirror vs lens formula?', 'Mirror: ' + T('1/v + 1/u = 1/f') + '. Lens: ' + T('1/v − 1/u = 1/f') + '. Both m = v/u for a lens; mirror m = −v/u')
d.basic('Lens magnification?', r'\( m = \dfrac{h\prime}{h} = \dfrac{v}{u} \)' + '. Negative: real, inverted. Positive: virtual, erect')
d.basic('First and second principal foci?', 'F (on the source side) and F′ (other side), ' + T('equidistant') + ' from the optical centre for a lens with the same medium on both sides')
d.basic('Ray rules for a convex lens?', '(i) Parallel to axis → through ' + T('F′') + '. (ii) Through the optical centre → ' + T('undeviated') + '. (iii) Through F → emerges parallel', **fig('fig_9_17a_convex_rays'))
d.basic('Ray rules for a concave lens?', 'Parallel ray appears to come from ' + T('F (on the incident side)') + '; ray through optical centre undeviated; ray directed to F′ emerges parallel', **fig('fig_9_17b_concave_rays'))
table_card(d, 'Convex lens', 'Image for object at…?', [
    ('At infinity', 'At F′; real, inverted, highly diminished', False), ('Beyond 2F', 'Between F′ and 2F′; real, inverted, diminished', False),
    ('At 2F', 'At 2F′; real, inverted, same size', False), ('Between F and 2F', 'Beyond 2F′; real, inverted, magnified', False),
    ('At F', 'At infinity; real, inverted, highly magnified', False), ('Between F and O', 'Same side; virtual, erect, magnified (magnifier)', True)],
    term='Convex lens: position of object → image')
d.basic('Concave lens: image for any object position?', T('Always virtual, erect, diminished') + ', between F and the lens')
d.basic('Example 9.6: how can a glass lens (n = 1.47) “disappear” in a liquid?', 'When n_liquid = ' + T('1.47') + ', 1/f = 0, f → ∞, so it acts like a plane glass sheet. Not water (1.33); could be glycerine')
d.basic('Teacher addition: a convex lens is placed in a liquid of larger index than the lens. Behaviour?', 'n₂/n₁ < 1, so the sign of f flips: it acts like a ' + T('diverging') + ' lens. (Air bubble in water: a concave-behaving “lens”)')

d.sec('9.5.3-power-of-a-lens')
d.basic('Define power of a lens, and its unit.', r'\( P = \dfrac{1}{f} \)' + ' (f in metres); unit ' + T('dioptre (D)') + ' = m⁻¹; + for convex, − for concave', **fig('fig_9_18_power'))
d.basic('Prescription +2.5 D and −4.0 D: what lenses?', '+2.5 D: convex, f = ' + N('+40 cm') + '. −4.0 D: concave, f = ' + N('−25 cm'))
steps_card(d, 'Example 9.7 · lens in different media', 'Find the missing step.', '(i) f = 0.5 m: P? (ii) Biconvex R₁ = 10 cm, R₂ = −15 cm, f = 12 cm: n? (iii) A glass lens (n = 1.5) has f = 20 cm in air. Find f in water (n = 1.33).',
           ['(i) P = 1/0.5 = <b>+2 D</b>', '(ii) 1/12 = (n − 1)(1/10 + 1/15) = (n − 1)/6 → <b>n = 1.5</b>', '(iii) In air: 1/20 = 0.5 (1/R₁ − 1/R₂) → (1/R₁ − 1/R₂) = 1/10', 'In water: 1/f = (1.5/1.33 − 1)(1/10) → <b>f ≈ +78.2 cm</b> (weaker lens)'], 3,
           'Lens power, refractive index and lens in water (Example 9.7)', 'P = +2 D, n = 1.5, f in water ≈ 78.2 cm')
d.basic('Exam trap: what happens to the focal length of a glass lens when moved from air into water?', 'It ' + T('increases') + ' (about 4×): the relative index n_g/n_w = 1.13 is less than n_g/n_a = 1.5, so the lens is weaker')

d.sec('9.5.4-combination-of-thin-lenses-in-contact')
d.basic('Focal length of thin lenses in contact?', r'\( \dfrac{1}{f} = \dfrac{1}{f_1} + \dfrac{1}{f_2} + \dots \)' + ', or ' + T('P = P₁ + P₂ + …') + ' (algebraic sum)', **fig('fig_9_19_contact'))
d.basic('Magnification of a lens combination?', T('m = m₁ × m₂ × m₃ …'))
d.basic('Example 9.8: image position for the three-lens system f = +10, −10, +30 cm; first object at 30 cm, gaps 5 cm and 10 cm.', 'Lens 1: v₁ = 15 cm. Object for lens 2 is 10 cm beyond it (virtual): v₂ = ' + T('∞') + '. Lens 3 gets a parallel beam, so the final image is at its focus: ' + N('30 cm') + ' right of lens 3')
d.basic('Exercise 9.10: 30 cm convex lens in contact with a 20 cm concave lens. System?', '1/f = 1/30 − 1/20 = −1/60: ' + T('diverging, f = −60 cm'))
d.basic('Teacher addition: two thin lenses separated by a distance d (in air)?', r'\( \dfrac{1}{f} = \dfrac{1}{f_1} + \dfrac{1}{f_2} - \dfrac{d}{f_1f_2} \)' + '. The effective focal length depends on which side the light enters (see Exercise 9.20)')
d.basic('Teacher addition: a convex lens is cut into two halves (a) along the axis (b) across the axis. Focal length of each half?', '(a) Cut ' + T('along the principal axis') + ' (two thin halves): f ' + T('unchanged') + ' (the intensity of the image halves). (b) Cut ⟂ to the axis: each half is a plano-convex lens with f ' + T('doubled'))
d.basic('Teacher addition: object between two lenses, or a lens and a plane mirror behind it?', 'Use the formula lens by lens; for a mirror behind the lens, light passes the lens ' + T('twice') + ' (equivalent power: 2P_lens + P_mirror)')

# ---------------------------------------------------------------- 9.6 Prism
d.sec('9.6-refraction-through-a-prism')
d.basic('Prism relations for angle of deviation?', 'r₁ + r₂ = A and ' + T('δ = i + e − A'), **fig('fig_9_21_prism'))
d.basic('How does δ vary with the angle of incidence?', 'It falls to a minimum ' + T('D_m') + ' at i = e and rises again; for a given δ (other than D_m) there are two values of i (i and e interchange)', **fig('fig_9_22_deviation_curve'))
d.basic('Condition and results at minimum deviation?', T('i = e') + ', r₁ = r₂ = A/2; the ray inside is parallel to the base. ' + r'\( D_m = 2i - A \)')
d.basic('Prism formula for refractive index?', r'\( n_{21} = \dfrac{\sin[(A + D_m)/2]}{\sin(A/2)} \)')
d.basic('Thin prism (small A): deviation?', r'\( \delta = (n-1)A \)' + ': a thin prism does not deviate light much; independent of i for small angles')
d.basic('Prism in a medium of index n₁?', r'\( n_{21} = \dfrac{n_2}{n_1} = \dfrac{\sin[(A + D_m)/2]}{\sin(A/2)} \)' + ': D_m decreases if the surrounding medium is denser')
d.basic('Exam trap: a prism is placed in water. What happens to its deviation?', 'It ' + T('decreases') + ' (relative index falls); Exercise 9.6: D_m falls from 40° to about 10°')
d.basic('Dispersion (NCERT summary)?', T('Splitting of white light into its colours') + ' due to the different refractive indices for different wavelengths')
d.basic('Teacher addition: which colour deviates most in a prism? Why?', T('Violet') + ' (shortest λ, largest n; Cauchy: n = A + B/λ²). Red deviates least, moves fastest in glass')
d.basic('Teacher addition: angular dispersion and dispersive power of a thin prism?', 'Angular dispersion: ' + r'\( \delta_v - \delta_r = (n_v - n_r)A \)' + '. Dispersive power ' + r'\( \omega = \dfrac{n_v - n_r}{n_y - 1} \)')
d.basic('Teacher addition: rainbow and blue sky in one line each?', 'Rainbow: ' + T('dispersion + total internal reflection') + ' inside raindrops. Sky is blue and sunset red because of ' + T('Rayleigh scattering ∝ 1/λ⁴'))
d.basic('Exercise 9.21: incidence angle so a ray just undergoes TIR on the second face (A = 60°, n = 1.524)?', 'i_c = sin⁻¹(1/1.524) ≈ 41°; r₁ = 60° − 41° = 19°; sin i = 1.524 sin 19° = 0.496 → ' + N('i ≈ 30°'))

# ---------------------------------------------------------------- 9.7 Optical instruments
d.sec('9.7-optical-instruments')
d.basic('Least distance of distinct vision D?', 'About ' + N('25 cm') + ': the nearest distance at which a normal eye sees comfortably (the near point)')
d.basic('What is angular magnification (magnifying power)?', 'Ratio of the angle subtended by the ' + T('image') + ' to the angle subtended by the ' + T('object at the near point D'))

d.sec('9.7.1-the-microscope')
d.basic('Simple microscope: what is it and how is it used?', 'A ' + T('convex lens of small f') + ' held near the object (u ≤ f), giving an erect, magnified, virtual image at ≥ 25 cm', **fig('fig_9_23a_magnifier_near'))
d.basic('Magnifying power of a simple microscope: image at the near point?', r'\( m = 1 + \dfrac{D}{f} \)')
d.basic('Magnifying power of a simple microscope: image at infinity?', r'\( m = \dfrac{D}{f} \)' + ' (relaxed eye; one less than the near-point value)', **fig('fig_9_23c_magnifier_inf'))
d.basic('Derive m = 1 + D/f for the near-point image.', 'm = v/u = v(1/v − 1/f) = 1 − v/f. With v = −D: ' + T('m = 1 + D/f'))
d.basic('How does a magnifier give angular magnification if image angle = object angle?', 'It lets you place the object ' + T('much closer than 25 cm') + ' so it subtends a larger angle; without it the object must stay at D (Exercise 9.25a)', **fig('fig_9_23b_magnifier_angle'))
d.basic('Maximum magnification of a single simple microscope in practice?', 'About ' + T('≤ 9') + ' for realistic f (aberrations rise as f shrinks)')
d.basic('Compound microscope: parts and image nature?', T('Objective') + ' (small f, near the object): real, inverted, magnified image near the focal plane of the ' + T('eyepiece') + ', which acts as a magnifier giving a final ' + T('virtual, inverted, enlarged') + ' image', **fig('fig_9_24_compound'))
d.occlusion('Figure 9.24 · Compound microscope', M + 'fig_9_24_compound.webp', (1001, 692), [
    ('Objective', [190, 308, 135, 35], True), ('Eyepiece', [728, 148, 130, 32], True)], guess='hide-all')
d.basic('Magnification due to the objective? Tube length?', r'\( m_o = \dfrac{L}{f_o} \)' + '; L = distance between the second focus of the objective and first focus of the eyepiece (tube length)')
d.basic('Magnifying power of a compound microscope, image at infinity?', r'\( m = m_o m_e = \dfrac{L}{f_o}\cdot\dfrac{D}{f_e} \)')
d.basic('Magnifying power of a compound microscope, image at near point?', r'\( m = \dfrac{v_o}{|u_o|}\left(1 + \dfrac{D}{f_e}\right) \approx \dfrac{L}{f_o}\left(1 + \dfrac{D}{f_e}\right) \)')
d.basic('Why must both lenses of a compound microscope have short focal lengths?', 'm ∝ 1/(f_o f_e): the objective must form a large image of a close object and the eyepiece must magnify strongly (Exercise 9.25d)')
d.basic('Example: f_o = 1 cm, f_e = 2 cm, tube length 20 cm. Magnifying power (image at infinity)?', 'm = (20/1)(25/2) = ' + N('250'))
d.basic('Why should the eye sit at the “eye-ring” and not touching the eyepiece?', 'The eye-ring is the ' + T('image of the objective formed by the eyepiece') + ': all refracted rays pass through it, so the pupil there collects all the light (Exercise 9.25e)')
d.basic('Teacher addition: how do you increase resolving power of a microscope?', 'Use a smaller λ and larger numerical aperture: ' + r'\( R.P. = \dfrac{2\mu\sin\theta}{1.22\,\lambda} \)' + ' (oil immersion increases μ)')

d.sec('9.7.2-telescope')
d.basic('Refracting astronomical telescope: purpose and lenses?', 'Angular magnification of ' + T('distant') + ' objects. Objective: ' + T('large f, large aperture') + '; eyepiece: small f. Final image inverted', **fig('fig_9_25_telescope'))
d.basic('Magnifying power of a telescope in normal adjustment (image at infinity)?', r'\( m = \dfrac{\beta}{\alpha} = \dfrac{f_o}{f_e} \)' + '; tube length ' + N('f_o + f_e'))
d.basic('Telescope with the final image at the near point?', r'\( m = \dfrac{f_o}{f_e}\left(1 + \dfrac{f_e}{D}\right) \)' + ' and tube length f_o + u_e')
d.basic('Terrestrial telescope: what is added?', 'A pair of inverting lenses (or a prism) to make the final image ' + T('erect'))
d.basic('Two main considerations for an astronomical telescope?', T('Light-gathering power') + ' (∝ aperture area) and ' + T('resolving power') + ' (∝ aperture diameter)')
d.basic('Why do modern telescopes use mirrors as objectives?', 'A mirror has ' + T('no chromatic aberration') + ', is lighter, can be supported over its whole back, and is easier to make large and free of distortion')
d.basic('Cassegrain telescope: layout and advantages?', 'Concave primary + convex secondary sending light through a hole in the primary: ' + T('long focal length in a short tube') + ', observer not in the way', **fig('fig_9_26_cassegrain'))
d.occlusion('Figure 9.26 · Cassegrain telescope', M + 'fig_9_26_cassegrain.webp', (1001, 485), [
    ('Objective mirror', [725, 70, 130, 58], True), ('Secondary mirror', [90, 145, 145, 58], True), ('Eyepiece', [855, 315, 125, 38], True)], guess='hide-all')
d.basic('Largest telescopes named in NCERT?', 'India’s largest: ' + T('2.34 m, Kavalur (Tamil Nadu)') + ', Cassegrain reflector. Largest lens: 1.02 m (Yerkes). Keck (Hawaii): 10 m; Mt. Palomar: 5.08 m')
d.basic('Example: f_o = 100 cm, f_e = 1 cm. Magnifying power and angle for stars 1′ apart?', 'm = 100; the stars appear ' + N('100′ = 1.67°') + ' apart')
d.basic('Exam trap: telescope in normal adjustment: distance between lenses?', 'f_o + f_e (final image at infinity); a compound microscope has an entirely different separation set by L and the eyepiece position')

# ---------------------------------------------------------------- NEET/JEE problem patterns
d.sec('exam-patterns')
d.basic('NEET/JEE pattern: image of an object placed at 2f from a convex lens is seen on a screen. What if the lens is covered halfway?', 'Full image still forms, ' + T('dimmer') + ' (half the light)')
d.basic('Pattern: a convex lens forms real images of the same object at two positions 20 cm apart with object–screen distance 90 cm. Find f.', 'Displacement (Bessel) method: ' + r'\( f = \dfrac{D^2 - d^2}{4D} = \dfrac{90^2 - 20^2}{360} \approx 21.4 \) cm' + ' (Exercise 9.19)')
d.basic('Pattern: for a real image on a screen a distance D from the object, what is the maximum focal length of the lens?', T('f ≤ D/4') + ' (at f = D/4 the two image positions coincide: u = v = 2f)')
d.basic('Pattern: magnification and distances when a convex lens gives m = −2 with object at 15 cm?', 'v = mu → v = +30 cm (real); 1/f = 1/30 + 1/15 → ' + N('f = 10 cm'))
d.basic('Pattern: lens power P in air; power in liquid of index μ_l?', r'\( P_l = P_{air}\,\dfrac{n_g/\mu_l - 1}{n_g - 1} \)' + ' (from the lens-maker relation)')
d.basic('Pattern: minimum deviation D_m = A for a prism. Refractive index?', 'n = sin(A)/sin(A/2) = ' + T('2 cos(A/2)') + '; e.g. A = 60° gives n = √3')
d.basic('Pattern: prism of A = 60° and n = √2. Angle of incidence for minimum deviation?', 'r = 30°, sin i = √2 × ½ → ' + N('i = 45°') + ', D_m = 2i − A = 30°')
d.basic('Pattern: a ray enters a glass slab at 60° with n = √3. Angle of refraction and lateral shift for t = 3 cm?', 'sin r = sin 60°/√3 = 0.5 → r = 30°; shift = t sin(i − r)/cos r = 3 × 0.5/0.866 ≈ ' + N('1.73 cm'))
d.basic('Pattern: a microscope has objective f = 1 cm, eyepiece f = 5 cm. Magnifying power scales how with f_o?', T('m ∝ 1/f_o') + ' (and 1/f_e): halving f_o doubles m')
d.basic('Pattern: telescope objective diameter doubled. Change in light-gathering power and resolving power?', 'Light gathered ' + N('×4') + ' (∝ D²); resolving power ' + N('×2') + ' (∝ D)')

# ---------------------------------------------------------------- Points to ponder
d.sec('points-to-ponder')
d.basic('Do the laws of reflection and refraction hold for curved surfaces?', T('Yes') + ', at every point of incidence for any surface and any pair of media')
d.basic('Is a real image still there when the screen is removed?', T('Yes') + ': rays converge to the image point and diverge beyond it; the screen only diffuses them so that the image can be seen (laser shows in air)')
d.basic('Why can’t you see your image in a page of a book?', 'A rough surface reflects irregularly: rays from a point do not reach one image point (' + T('diffuse') + ' instead of regular reflection)')
d.basic('Why do thick lenses show coloured images?', T('Dispersion') + ' (chromatic aberration): different colours focus at different points')
d.basic('Why do objects change colour under monochromatic light?', 'Colour perception depends on which ' + T('constituent wavelengths') + ' are present in the incident light')

# ---------------------------------------------------------------- Exercises
d.sec('exercises')
steps_card(d, 'Exercise 9.1 · candle in front of a concave mirror', 'Find the missing step.', 'Candle 2.5 cm tall at 27 cm from a concave mirror of R = 36 cm. Where should the screen be? Nature and size? What if the candle moves closer?',
           ['f = −18 cm, u = −27 cm', '1/v = 1/f − 1/u = −1/18 + 1/27 = −1/54 → <b>v = −54 cm</b> (screen 54 cm in front)', 'm = −v/u = −(−54)/(−27) = <b>−2</b>: real, inverted, height <b>5.0 cm</b>', 'Moving the candle closer (towards F): the screen must move <b>farther</b>; for u < f the image is virtual (no screen)'], 2,
           'Real image on a screen (Exercise 9.1)', 'v = −54 cm, real, inverted, 5.0 cm; screen moves away as u → f')
d.basic('Exercise 9.2: 4.5 cm needle 12 cm from a convex mirror (f = 15 cm). Image and magnification?', '1/v = 1/15 + 1/12 → v = ' + N('+6.7 cm') + ' (behind); m = −v/u = ' + N('5/9') + ', image 2.5 cm, virtual and erect. As u → ∞, v → f and m → 0')
d.basic('Exercise 9.3: tank filled to 12.5 cm appears 9.4 cm deep. n? If the liquid has n = 1.63, how far must the microscope move?', 'n = 12.5/9.4 = ' + N('1.33') + '. New apparent depth = 12.5/1.63 = 7.67 cm; move ' + N('1.7 cm') + ' (upward)')
d.basic('Exercise 9.4: given the glass–air and water–air figures, angle of refraction for a ray in water at 45° meeting glass?', 'n_ga = sin 60°/sin 35° = 1.51; n_wa ≈ 1.32; n_gw = 1.51/1.32 ≈ 1.144; sin r = sin 45°/1.144 = 0.618 → ' + N('r ≈ 38°'), **img('fig_9_27a'))
d.basic('Note on Exercise 9.4: is Fig 9.27(b) consistent with n_wa = 1.32?', 'With 60° in air, 1.32 needs r ≈ 41°, but the figure prints 47° (sin 60°/sin 47° = 1.18). Exams use the key’s ' + T('n_wa = 1.32–1.33') + ' and get r ≈ 38°', **img('fig_9_27b'))
steps_card(d, 'Exercise 9.5 · light from a bulb in a tank', 'Find the missing step.', 'Point bulb at the bottom of a tank, water depth 80 cm (n = 1.33). Area of the surface through which light emerges?',
           ['Light escapes only within the cone of half-angle i_c: sin i_c = 1/1.33 = 0.75', 'tan i_c = 0.75/√(1 − 0.5625) = 1.134', 'Radius r = h tan i_c = 0.8 × 1.134 = <b>0.907 m</b>', 'Area = πr² = <b>2.6 m²</b>'], 3,
           'Escape circle for a submerged source (Exercise 9.5)', 'Area ≈ 2.6 m²')
d.basic('Exercise 9.6: D_m = 40° for a 60° prism. n? In water (1.33), new D_m?', 'n = sin 50°/sin 30° = ' + N('1.53') + '. In water: n_gw = 1.15; sin((60 + D)/2) = 1.15 × 0.5 → D ≈ ' + N('10°'))
d.basic('Exercise 9.7: double-convex lens, both faces the same R, n = 1.55, f = 20 cm. R?', '1/f = (n − 1)(2/R) → R = 2(n − 1)f = 2 × 0.55 × 20 = ' + N('22 cm'))
d.basic('Exercise 9.8: a convergent beam meets at P; a lens is placed 12 cm before P. Where does it converge for (a) f = +20 cm (b) f = −16 cm?', 'Object is virtual: u = +12 cm. (a) 1/v = 1/20 + 1/12 → ' + N('v = 7.5 cm') + ' (real, right). (b) 1/v = −1/16 + 1/12 → ' + N('v = 48 cm') + ' (real, right)')
d.basic('Exercise 9.9: 3.0 cm object 14 cm from a concave lens (f = −21 cm). Image? As the object moves away?', '1/v = −1/21 − 1/14 → v = ' + N('−8.4 cm') + ', m = 0.6: virtual, erect, ' + N('1.8 cm') + '. As u → ∞, v → f (never beyond); at u = f the image is at 10.5 cm, not at infinity')
d.basic('Exercise 9.11: compound microscope f_o = 2.0 cm, f_e = 6.25 cm, lenses 15 cm apart. Object distance and magnifying power for image at (a) 25 cm, (b) infinity?', '(a) u_e = −5 cm, v_o = 10 cm, ' + N('u_o = −2.5 cm') + ', m = (10/2.5)(1 + 25/6.25) = ' + N('20') + '. (b) v_o = 8.75, ' + N('u_o = −2.59 cm') + ', m = 3.38 × 4 = ' + N('13.5'))
d.basic('Exercise 9.12: f_o = 8.0 mm, f_e = 2.5 cm, object at 9.0 mm from the objective, normal eye. Separation and magnifying power?', 'v_o = 7.2 cm; eyepiece object distance 2.27 cm: separation ' + N('9.47 cm') + '; m = (7.2/0.9)(1 + 25/2.5) = ' + N('88'))
d.basic('Exercise 9.13: f_o = 144 cm, f_e = 6.0 cm. Magnifying power and separation?', 'm = 144/6 = ' + N('24') + '; separation f_o + f_e = ' + N('150 cm'))
d.basic('Exercise 9.14: refractor with f_o = 15 m, f_e = 1.0 cm. (a) m (b) diameter of the Moon’s image formed by the objective?', '(a) m = 1500. (b) Moon subtends 3.48 × 10⁶/3.8 × 10⁸ = 9.16 × 10⁻³ rad; image diameter = 15 × 9.16 × 10⁻³ = ' + N('13.7 cm'))
d.basic('Exercise 9.15: use the mirror equation to show a convex mirror always gives a virtual, diminished image between F and P.', 'f > 0, u < 0: 1/v = 1/f − 1/u > 0, so ' + T('v > 0 (virtual)') + '. v = fu/(u − f): |v| < f, so image lies between P and F; m = f/(f − u) < 1: ' + T('diminished'))
d.basic('Exercise 9.15(a),(d): concave mirror properties from the equation?', '(a) f < 0, u < 0 with |f| < |u| < 2|f|: v = fu/(u − f) has |v| > 2|f|, real and beyond C. (d) f < u < 0 (object inside F): u − f > 0 so v > 0: ' + T('virtual') + ', and m = f/(f − u) = ' + N('> 1') + ': enlarged')
d.basic('Exercise 9.16: pin viewed from 50 cm above through a 15 cm glass slab (n = 1.5). Apparent raise? Depends on slab position?', 'Shift = t(1 − 1/n) = 15 × (1/3) = ' + N('5 cm') + '. ' + T('Independent') + ' of where the slab is (for small angles)')
d.basic('Exercise 9.17(a): light pipe, core n = 1.68, cladding 1.44. Range of incidence angles that get totally reflected?', 'sin i′_c = 1.44/1.68 → i′_c = 59°; r_max = 31°; sin i_max = 1.68 sin 31° → ' + N('0 < i < 60°'), **img('fig_9_28_lightpipe'))
d.basic('Exercise 9.17(b): with no cladding (n = 1.68 in air)?', 'i′_c = sin⁻¹(1/1.68) = 36.5°. Even i = 90° gives r = 36.5°, i′ = 53.5° > i′_c, so ' + T('all rays (0–90°) are totally reflected'))
d.basic('Exercise 9.18: image of a bulb on the opposite wall, 3 m away, by a convex lens. Maximum focal length?', 'Real image needs D ≥ 4f, so ' + N('f_max = 0.75 m'))
d.basic('Exercise 9.19: object–screen 90 cm, two lens positions 20 cm apart. f?', 'f = (D² − d²)/4D = (8100 − 400)/360 = ' + N('21.4 cm'))
steps_card(d, 'Exercise 9.20 · separated lenses', 'Find the missing step.', 'The 30 cm convex and 20 cm concave lenses are 8.0 cm apart. Effective focal length? Does it depend on the side of incidence? Magnification for a 1.5 cm object 40 cm from the convex lens?',
           ['Parallel beam from the convex side: v₁ = +30, then u₂ = +22 (virtual object): v₂ = <b>−220 cm</b>', 'From the concave side: v₁ = −20, u₂ = −28: v₂ = <b>−420 cm</b> (different!)', 'So the notion of effective focal length is <b>not useful</b> here (depends on the side)', 'Object 40 cm: v₁ = 120 (m₁ = 3); u₂ = +112, v₂ = −92 (m₂ = 20/92); <b>m = 0.652</b>, image size <b>0.98 cm</b>'], 3,
           'Two lenses 8 cm apart (Exercise 9.20)', 'Side-dependent; m = 0.652; image 0.98 cm')
d.basic('Exercise 9.22: card of 1 mm² squares viewed through a magnifier held close to the eye, card at 9 cm. Magnification, area of each square, magnifying power?', 'Key: 1/v − 1/u with v = −90 cm gives ' + T('m = 10') + ', area = 10 × 10 × 1 mm² = ' + N('1 cm²') + ', magnifying power = 25/9 = ' + N('2.8') + '. They differ: m = |v/u| but MP = 25/|u|; equal only when the image is at 25 cm')
d.basic('Correction: Exercise 9.22 says f = 9 cm and the card is at 9 cm. Does the key match?', X('No') + ': the printed question says f = 9 cm, but the key’s v = −90 cm only works with ' + T('f = 10 cm') + ' (u = −9 cm). With f = 9 cm and u = 9 cm the image would be at infinity. The key’s numbers come from an older f = 10 cm version; the concept (m ≠ MP) is what is examined')
d.basic('Exercise 9.23: viewing the squares distinctly with maximum magnifying power. Where to hold the lens? m? Is m = MP?', 'Image at 25 cm. Key (f = 10 cm): u = −7.14 cm, m = 3.5, and yes m = MP ' + T('when the image is at the near point') + '. Recomputed with f = 9 cm: u = −6.6 cm, m = 1 + 25/9 = ' + N('3.8'))
d.basic('Exercise 9.24: how far should the card be to get a virtual square area of 6.25 mm² (m = 2.5)? Seen distinctly?', 'Key: u = −6 cm, |v| = 15 cm (f = 10 cm). With f = 9 cm: u = −5.4 cm, |v| = 13.5 cm. Either way the image is ' + X('closer than 25 cm') + ', so the eye cannot see it distinctly')
d.basic('Exercise 9.25(a),(b): magnifier: angle of object = angle of image, so in what sense does it magnify? Effect of moving the eye back?', '(a) The object can be placed ' + T('much closer than 25 cm') + ', at a larger angle than at D. (b) Angular magnification decreases slightly as the angle subtended at the eye falls')
d.basic('Exercise 9.25(c): why can’t we keep reducing the focal length of a simple lens to get more magnifying power?', 'Grinding very short f lenses is hard, and ' + T('spherical and chromatic aberrations') + ' grow; a simple lens is limited to about 3× (aberration-corrected systems reach 10× more)')
steps_card(d, 'Exercise 9.26 · setting up a compound microscope', 'Find the missing step.', 'Angular magnification 30× with f_o = 1.25 cm and f_e = 5 cm (image at 25 cm). How to set up the microscope?',
           ['Eyepiece magnification: 1 + 25/5 = <b>6</b>, so objective m_o = 30/6 = <b>5</b>', 'v_o/|u_o| = 5 and 1/v_o − 1/u_o = 1/1.25 → <b>u_o = −1.5 cm, v_o = 7.5 cm</b>', 'Eyepiece image at 25 cm: 1/u_e = −1/25 − 1/5 → |u_e| = <b>4.17 cm</b>', 'Separation = 7.5 + 4.17 = <b>11.67 cm</b>; object 1.5 cm from the objective'], 1,
           'Design for 30× (Exercise 9.26)', 'Object 1.5 cm from objective; lenses 11.67 cm apart')
d.basic('Exercise 9.27: telescope with f_o = 140 cm, f_e = 5.0 cm. m for (a) normal adjustment (b) final image at 25 cm?', '(a) m = 140/5 = ' + N('28') + '. (b) m = (140/5)(1 + 5/25) = ' + N('33.6'))
d.basic('Exercise 9.28: same telescope on a 100 m tower 3 km away: separation? Image height by the objective and final image height at 25 cm?', 'Separation ' + N('145 cm') + '. Angle = 1/30 rad → objective image = 140/30 = ' + N('4.7 cm') + '; eyepiece magnification 6 → final image ≈ ' + N('28 cm'))
d.basic('Exercise 9.29: Cassegrain with mirrors 20 mm apart, R = 220 mm (primary), 140 mm (secondary). Final image of a far object?', 'Primary f = 110 mm; image would form 90 mm beyond the secondary (virtual object). Secondary f = 70 mm: 1/v = 1/70 − 1/90 → ' + N('v = 315 mm') + ' from the secondary')
d.basic('Exercise 9.30: mirror on a galvanometer coil deflects 3.5°. Shift of the reflected spot on a screen 1.5 m away?', 'Reflected ray turns by 2θ = 7°: d = 1.5 tan 7° = ' + N('18.4 cm'), **img('fig_9_29_galvo'))
d.basic('Exercise 9.31: needle over a convex lens (n = 1.50) on a liquid layer on a plane mirror: image at needle position at 45.0 cm; without liquid at 30.0 cm. n_liquid?', 'Without liquid f = 30 cm, so R = 30 cm (biconvex). With liquid: 1/45 = 1/30 + 1/f_liq → f_liq = −90 cm (plano-concave liquid lens: −(n − 1)/30). So n − 1 = 1/3: ' + N('n = 1.33'), **img('fig_9_30_liquid_lens'))

# ---------------------------------------------------------------- Summary
d.sec('summary')
table_card(d, 'Summary', 'Formula?', [
    ('Mirror equation', '1/v + 1/u = 1/f, f = R/2', False), ('Mirror magnification', 'm = −v/u', False), ('Snell’s law', 'sin i/sin r = n₂₁ = n₂/n₁', False),
    ('Critical angle', 'sin i_c = n₂/n₁ (n₁ > n₂)', False), ('Spherical surface', 'n₂/v − n₁/u = (n₂ − n₁)/R', False),
    ('Lens formula', '1/v − 1/u = 1/f', False), ('Lens maker', '1/f = (n − 1)(1/R₁ − 1/R₂)', False), ('Lens power, contact', 'P = 1/f; P = P₁ + P₂', False),
    ('Prism', 'n = sin[(A + D_m)/2]/sin(A/2); δ = (n − 1)A', False), ('Simple microscope', 'm = 1 + D/f (near), D/f (∞)', False),
    ('Compound microscope', 'm = (L/f_o)(D/f_e)', False), ('Telescope', 'm = f_o/f_e; length f_o + f_e', False)],
    term='Chapter 9 formula sheet')
table_card(d, 'Concept checks', 'True or false?', [
    ('A convex mirror can form a real image of a real object', 'False (always virtual)', True), ('Frequency changes when light enters glass', 'False (λ and v change)', True),
    ('TIR needs light going from a denser to a rarer medium', 'True', False), ('A glass lens in water has a longer focal length than in air', 'True', False),
    ('Compound microscope: objective has the smaller focal length', 'True', False), ('Refracting telescope objective has a small aperture', 'False (large)', True)],
    term='Chapter 9 concept checks')

print(d.write(os.path.join(OUT, 'deck.json')), 'cards')
