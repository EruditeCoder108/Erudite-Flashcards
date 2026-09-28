import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase_phy as sp

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Physics', 'class11-physics-ch07-gravitation')
d = Deck('Chapter 7: Gravitation', 'Class 11', ['class-11', 'physics', 'ch-7'])
d.description = 'Kepler’s laws, universal gravitation, G, variation of g, gravitational potential energy, escape speed, satellites and their energy'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- 7.1 Introduction
d.sec('7.1-introduction')
d.basic('Who first recognised that all bodies fall with the same constant acceleration?', T('Galileo') + ' (1564–1642), using bodies rolling down inclined planes')
d.basic('Geocentric vs heliocentric model: who proposed each?', T('Ptolemy') + ': geocentric (~2000 years ago). ' + T('Aryabhatta') + ' (5th century AD) mentioned a heliocentric model; ' + T('Copernicus') + ' (1473–1543) gave the definitive one')
d.basic('Whose observations did Kepler analyse?', 'Those of his master ' + T('Tycho Brahe') + ' (1546–1601), made with the naked eye')

# ---------------------------------------------------------------- 7.2 Kepler's laws
d.sec('7.2-keplers-laws')
d.cloze('Kepler’s law of orbits: all planets move in {{c1::elliptical}} orbits with the Sun at {{c2::one of the foci}}.', extra='This broke from Copernicus’s circles.')
d.basic('Perihelion and aphelion?', T('Perihelion') + ' P: closest point to the Sun. ' + T('Aphelion') + ' A: farthest. Semi-major axis a = AP/2', **fig('fig_7_1a_ellipse'))
d.basic('How can you draw an ellipse with a string?', 'Pin the ends at F₁ and F₂ and move a pencil keeping the string taut: ' + T('F₁T + F₂T = constant'), **fig('fig_7_1b_drawing_ellipse'))
d.basic('An ellipse whose two foci merge is a…?', T('Circle') + ' (semi-major axis = radius)')
d.cloze('Kepler’s law of areas: the line joining a planet to the Sun sweeps {{c1::equal areas in equal times}}.')
sp.kepler_second_law(d)
d.basic('Kepler’s second law follows from which conservation law?', 'Conservation of ' + T('angular momentum') + ': ΔA/Δt = L/2m, constant because gravity is a ' + T('central force'), **fig('fig_7_2_law_of_areas'))
d.basic('Is the law of areas special to the inverse-square law?', X('No') + ': it holds for ' + T('any central force'))
d.basic('Example 7.1: relate the speeds at perihelion and aphelion.', r'\( m r_P v_P = m r_A v_A \Rightarrow \dfrac{v_P}{v_A} = \dfrac{r_A}{r_P} \)' + '; the planet takes longer on the far arc BAC than on CPB')
d.cloze('Kepler’s law of periods: {{c1::T² ∝ a³}}, where a is the semi-major axis.')
d.basic('Table 7.1: what does Q = T²/a³ show for the eight planets?', 'Q ≈ ' + N('3 × 10⁻³⁴ y² m⁻³') + ' for all: the same constant → the law of periods', **fig('tab_7_1_kepler_data'))
d.basic('Kepler’s third law in full (circular orbit, radius R)?', r'\( T^2 = \dfrac{4\pi^2}{GM_S}R^3 \)' + '; also valid for ellipses with R → a')
d.basic('Exercise 7.3: a planet goes round the Sun twice as fast as the Earth. Orbital size?', r'\( (1/2)^{2/3} \approx \)' + ' ' + N('0.63') + ' times the Earth’s')

# ---------------------------------------------------------------- 7.3 Universal law
d.sec('7.3-universal-law')
d.basic('Newton’s moon test: ratio g / a(moon)?', r'\( \dfrac{g}{a_m} = \dfrac{R_m^2}{R_E^2} \approx 3600 \)' + ': gravity falls as ' + T('1/r²'))
d.basic('State Newton’s universal law of gravitation.', 'Every body attracts every other with a force ' + r'\( F = G\dfrac{m_1m_2}{r^2} \)' + ', along the line joining them')
d.basic('Vector form of the law?', r'\( \vec F = -G\dfrac{m_1m_2}{r^2}\hat r \)' + ' ; force on m₁ due to m₂ and on m₂ due to m₁ are equal and opposite')
d.basic('Principle of superposition for gravity?', 'The net force on a mass is the ' + T('vector sum') + ' of the forces from each other mass, each acting as if the others were absent', **fig('fig_7_4_superposition'))
d.basic('Example 7.2: equal masses m at the corners of an equilateral triangle, 2m at the centroid. Net force on 2m? And if the mass at A is doubled?', N('Zero') + ' (symmetry); with 2m at A: ' + r'\( 2Gm^2\,\hat j \)' + ' (towards A, AG = 1 m)', **fig('fig_7_5_triangle'))
d.basic('Force between a uniform spherical shell and a point mass outside it?', 'As if the whole mass were at the ' + T('centre'))
d.basic('Force on a point mass inside a uniform spherical shell?', N('Zero') + ': pulls from different parts cancel')
d.basic('Can a body be shielded from gravity (Exercise 7.1a)?', X('No') + ': a shell gives zero force only from itself; outside bodies still pull. Gravitational shielding is impossible')
d.basic('Is the force between two extended bodies along the line joining their CMs?', X('Not necessarily') + '; it is for spherically symmetric bodies')

# ---------------------------------------------------------------- 7.4 G
d.sec('7.4-gravitational-constant')
d.basic('Who first measured G, and when?', T('Henry Cavendish') + ', ' + N('1798'), **fig('fig_7_6_cavendish'))
d.basic('Principle of Cavendish’s experiment?', 'Big spheres pull small ones on a suspended bar; the gravitational torque twists the wire until ' + r'\( \tau\theta = \dfrac{GMm}{d^2}L \)' + '; measure θ → G')
d.basic('Value and SI unit of G?', N('6.67 × 10⁻¹¹ N m² kg⁻²') + '; dimensions [M⁻¹ L³ T⁻²]')
d.basic('Why is Cavendish said to have "weighed the Earth"?', 'With G known, ' + r'\( M_E = \dfrac{gR_E^2}{G} \)' + ' follows from g and R_E')

# ---------------------------------------------------------------- 7.5-7.6 g
d.sec('7.5-acceleration-due-to-gravity')
d.basic('g at the Earth’s surface in terms of G?', r'\( g = \dfrac{GM_E}{R_E^2} \)')
d.basic('Example 7.6: find M_E from g = 9.81, R = 6.37 × 10⁶ m. And from the Moon’s orbit?', N('5.97 × 10²⁴ kg') + ' from g; ' + N('6.02 × 10²⁴ kg') + ' from Kepler’s third law — within 1 %')
d.basic('Force on a mass m inside the (uniform) Earth at distance r from the centre?', 'Only the sphere of radius r pulls: ' + r'\( F = \dfrac{GM_E m}{R_E^3}r \)' + ' (∝ r)', **fig('fig_7_7_mine'))
d.basic('g at height h above the surface?', r'\( g(h) = \dfrac{GM_E}{(R_E + h)^2} \approx g\left(1 - \dfrac{2h}{R_E}\right) \)' + ' for h ≪ R', **fig('fig_7_8a_height'))
d.basic('g at depth d below the surface?', r'\( g(d) = g\left(1 - \dfrac{d}{R_E}\right) \)' + ' (exact for uniform Earth)', **fig('fig_7_8b_depth'))
d.basic('Where is g maximum? Its value at the centre?', 'Maximum at the ' + T('surface') + '; ' + N('zero') + ' at the centre', **fig('drawn_g_vs_r'))
d.basic('Trap: for small h and d = h, where is g smaller — at height h or depth h?', 'At ' + T('height h') + ': it falls twice as fast (2h/R vs h/R)')
d.basic('Exercise 7.16: a body weighs 250 N on the surface. Weight halfway to the centre?', N('125 N') + ' (g ∝ r inside)')
d.basic('Exercise 7.15: 63 N on the surface. Force at height R/2?', '63 × (1/1.5)² = ' + N('28 N'))
d.basic('Exercise 7.2(c): g depends on the mass of the Earth or the mass of the body?', 'The ' + T('Earth') + '; g is independent of the body’s mass')
d.basic('Teacher addition: effect of Earth’s rotation on g at latitude λ?', r'\( g_\lambda = g - \omega^2R\cos^2\lambda \)' + ': least at the equator, unchanged at the poles')

# ---------------------------------------------------------------- 7.7 Potential energy
d.sec('7.7-gravitational-potential-energy')
d.basic('Notation: NCERT writes W (and V) for potential energy. What do most books use?', T('U') + ' for potential energy and ' + T('V') + ' for gravitational potential (energy per unit mass). This deck follows that')
d.basic('Why is mgh only an approximation?', 'It assumes g constant; valid only for heights ' + T('≪ R_E') + '. mgh is the ' + T('difference') + ' in PE near the surface')
d.basic('Gravitational PE of two masses at distance r (zero at infinity)?', r'\( U = -\dfrac{Gm_1m_2}{r} \)')
d.basic('Why is gravitational PE negative?', 'Zero is chosen at infinity and gravity is attractive: work is needed to pull the masses ' + T('apart to infinity'))
d.basic('Work done by gravity in moving m from r₁ to r₂?', r'\( W = -GM_Em\left(\dfrac{1}{r_2} - \dfrac{1}{r_1}\right) \)' + '; it depends only on the end points (conservative)')
d.basic('Define gravitational potential.', 'PE per unit mass: ' + r'\( V = -\dfrac{GM}{r} \)' + ' (scalar, J kg⁻¹)')
d.basic('Gravitational intensity (field) and its relation to g?', 'Force per unit mass, ' + r'\( \dfrac{GM}{r^2} \)' + ' towards the mass; at the surface it equals g (vector, m s⁻²)')
d.basic('PE of a system of many particles?', 'Sum over ' + T('all pairs') + ' of −Gmᵢmⱼ/rᵢⱼ (superposition)')
d.basic('Example 7.3: four masses m at the corners of a square of side l. Total PE and potential at the centre?', r'\( U = -\dfrac{Gm^2}{l}(4 + \sqrt2) \approx -5.41\dfrac{Gm^2}{l} \)' + '; ' + r'\( V = -\dfrac{4\sqrt2\,Gm}{l} \)', **fig('fig_7_9_square'))
d.basic('Exercise 7.2(d): is −GMm(1/r₂ − 1/r₁) more or less accurate than mg(r₂ − r₁)?', T('More') + ' accurate; mg(r₂ − r₁) holds only near the surface')
d.basic('Exercise 7.21: two 100 kg spheres 1.0 m apart. Force and potential at the midpoint? Equilibrium?', 'Force ' + N('0') + ', potential ' + N('−2.7 × 10⁻⁸ J/kg') + '; ' + X('unstable') + ' equilibrium')

# ---------------------------------------------------------------- 7.8 Escape speed
d.sec('7.8-escape-speed')
d.basic('Escape speed from the Earth’s surface?', r'\( v_e = \sqrt{\dfrac{2GM_E}{R_E}} = \sqrt{2gR_E} \approx \)' + ' ' + N('11.2 km/s'))
d.basic('Derive the escape speed idea in one line.', 'Total energy must be ≥ 0: ' + r'\( \tfrac12 mv^2 - \dfrac{GMm}{R} \ge 0 \)')
d.basic('Exercise 7.7: does escape speed depend on the mass of the body or the direction of projection?', X('No') + ' to both; it depends on the ' + T('location') + ' (potential there): slightly on latitude and height')
d.basic('Why does the Moon have no atmosphere?', 'Its escape speed is only ' + N('2.3 km/s') + ' (≈ 1/5 of Earth’s); gas molecules faster than that escape')
d.basic('Example 7.4: spheres M and 4M (radius R), 6R apart. Where is the neutral point, and what minimum speed from M’s surface reaches 4M?', 'Neutral point ' + N('2R') + ' from M’s centre; ' + r'\( v_{min} = \sqrt{\dfrac{3GM}{5R}} \)', **fig('fig_7_10_two_spheres'))
d.basic('Exercise 7.18: a body is projected at 3 × escape speed. Speed far away?', r'\( \sqrt{9 - 1}\,v_e = 2\sqrt2 \times 11.2 \approx \)' + ' ' + N('31.7 km/s'))
d.basic('Exercise 7.17: rocket fired up at 5 km/s. How far does it go?', 'To r ≈ ' + N('8.0 × 10⁶ m') + ' from the centre (≈ 1600 km above the surface)')

# ---------------------------------------------------------------- 7.9 Satellites
d.sec('7.9-earth-satellites')
d.basic('Speed of a satellite in a circular orbit at height h?', r'\( v = \sqrt{\dfrac{GM_E}{R_E + h}} \)' + ' — decreases with height, independent of the satellite’s mass')
d.basic('Orbital speed close to the surface?', r'\( v_0 = \sqrt{gR_E} \approx \)' + ' ' + N('7.9 km/s'))
sp.newtons_cannon(d)
d.basic('Relation between escape speed and orbital speed near the surface?', r'\( v_e = \sqrt2\,v_0 \)')
d.basic('Period of a satellite?', r'\( T = 2\pi\sqrt{\dfrac{(R_E + h)^3}{GM_E}} \)' + ' → T² ∝ (R + h)³ (Kepler’s third law)')
d.basic('Period of a satellite just above the surface?', r'\( T_0 = 2\pi\sqrt{\dfrac{R_E}{g}} \approx \)' + ' ' + N('85 min'))
d.basic('Moon’s period and a curiosity about it?', N('27.3 days') + ', roughly equal to its own spin period, so we always see the same face')
d.basic('Example 7.5: Phobos has period 7 h 39 min and orbit radius 9.4 × 10³ km. Mass of Mars? Martian year if its orbit is 1.52 × Earth’s?', N('6.48 × 10²³ kg') + '; ' + N('684 days') + ' (1.52^(3/2) × 365)')
d.basic('Example 7.7: k = 10⁻¹³ s² m⁻³ in T² = k r³. Moon at 3.84 × 10⁵ km: period?', 'k = 1.33 × 10⁻¹⁴ d² km⁻³ → T ≈ ' + N('27.3 days'))
d.basic('Why does an astronaut in an orbiting satellite feel weightless?', 'Not because gravity is small, but because astronaut and satellite are both in ' + T('free fall') + ' towards the Earth')
d.basic('Exercise 7.4: Io’s period 1.769 days, orbit 4.22 × 10⁸ m. Show M(Jupiter) ≈ M(Sun)/1000. Method?', 'Use M = 4π²R³/(GT²) for Io and for the Earth; the ratio comes to ≈ ' + N('1/1000'))
d.basic('Exercise 7.13: how to "weigh the Sun"?', r'\( M_S = \dfrac{4\pi^2 R^3}{GT^2} \)' + ' with R = 1.5 × 10¹¹ m, T = 1 year → ' + N('2.0 × 10³⁰ kg'))
d.basic('Exercise 7.14: a Saturn year is 29.5 Earth years. Distance from the Sun?', '(29.5)^(2/3) × 1.5 × 10⁸ km ≈ ' + N('1.43 × 10⁹ km'))
d.basic('Exercise 7.5: a star 50 000 ly from the centre of a galaxy of 2.5 × 10¹¹ solar masses. Period?', '≈ ' + N('3.5 × 10⁸ years'))

# ---------------------------------------------------------------- 7.10 Energy of a satellite
d.sec('7.10-energy-of-satellite')
table_card(d, '7.10 · satellite in a circular orbit of radius r', 'Energy?', [
    ('Kinetic energy K', '+GMm / 2r', False), ('Potential energy U', '−GMm / r', True),
    ('Total energy E', '−GMm / 2r', True), ('Relations', 'U = 2E,  K = −E', False)], term='Energies of an orbiting satellite')
d.basic('Why must the total energy of a satellite be negative?', 'It is a ' + T('bound') + ' system; E ≥ 0 would let it escape to infinity')
d.basic('Energy needed to take a satellite in orbit (radius r) out of Earth’s influence?', r'\( +\dfrac{GMm}{2r} \)' + ' (= −E). Less than for a body at rest at that height (Exercise 7.6b)')
d.basic('Exercise 7.19: 200 kg satellite at 400 km height. Energy to escape?', N('5.9 × 10⁹ J'))
steps_card(d, 'Example 7.8', 'Find the missing step.', '400 kg satellite moved from orbit radius 2R_E to 4R_E. Energy needed and changes in K and U?',
           ['Eᵢ = −GMm/4R, E𝒻 = −GMm/8R', 'ΔE = GMm/8R = gmR/8 = 3.13 × 10⁹ J', 'ΔK = −ΔE = −3.13 × 10⁹ J', 'ΔU = 2ΔE = <b>+6.25 × 10⁹ J</b>'], 3,
           'Raising a satellite from 2R to 4R', 'ΔE = +3.13 × 10⁹ J; ΔK = −3.13 × 10⁹ J; ΔU = +6.25 × 10⁹ J')
d.basic('Correction: NCERT Example 7.8 prints ΔV = −6.25 × 10⁹ J. What is the correct sign?', T('Positive') + ': Uᵢ = −GMm/2R, U𝒻 = −GMm/4R, so U rises (becomes less negative) by +6.25 × 10⁹ J. Check: ΔK + ΔU = ΔE = +3.13 × 10⁹ J')
d.basic('A satellite loses energy to air drag. What happens to its speed?', 'It ' + T('increases') + ': E falls, r shrinks, K = −E rises (Exercise 5.5c)')

# ---------------------------------------------------------------- Exercises and ponder
d.sec('exercises')
d.basic('Exercise 7.1(c): the Sun pulls the Earth harder than the Moon does, yet the Moon causes bigger tides. Why?', 'Tides depend on the ' + T('difference') + ' of pull across the Earth, ∝ M/r³, not M/r²; the nearby Moon wins')
d.basic('Exercise 7.1(b): can an astronaut in a very large space station detect gravity?', T('Yes') + ', through the variation of g across the station (tidal effect)')
table_card(d, 'Exercise 7.8 · comet in an elliptical orbit', 'Constant?', [
    ('Linear speed', 'no', True), ('Angular speed', 'no', True), ('Angular momentum', 'yes', False),
    ('Kinetic energy', 'no', True), ('Potential energy', 'no', True), ('Total energy', 'yes', False)], term='What stays constant for a comet')
d.basic('Exercise 7.9: which symptoms may an astronaut in space get?', T('Swollen face, headache, orientation problems') + ' (body fluids shift upwards); not swollen feet')
d.basic('Exercises 7.10–7.11: direction of the gravitational field at the centre C and at a point P on the open face of a hemispherical shell?', 'Along ' + T('c') + ' and ' + T('e') + ' (straight down): complete the sphere, where the field inside is zero', **img('fig_7_11_hemisphere'))
d.basic('Exercise 7.12: where between the Earth and Sun is the net gravitational force on a rocket zero?', 'About ' + N('2.6 × 10⁸ m') + ' from the Earth’s centre')
d.basic('Exercise 7.20: two solar-mass stars start at rest 10⁹ km apart. Speed at collision (radius 10⁴ km each)?', '≈ ' + N('2.6 × 10⁶ m/s') + ' each')
table_card(d, 'Points to ponder', 'In motion under gravity, is it conserved?', [
    ('Angular momentum (about the centre)', 'yes', False), ('Total mechanical energy', 'yes', False),
    ('Linear momentum of the orbiting body', 'no', True)], term='Conserved quantities under gravity')

d.sec('summary')
table_card(d, 'Summary', 'Formula?', [
    ('g at height h', 'GM/(R + h)² ≈ g(1 − 2h/R)', False), ('g at depth d', 'g(1 − d/R)', False),
    ('Orbital speed near surface', '√(gR) ≈ 7.9 km/s', False), ('Escape speed', '√(2gR) ≈ 11.2 km/s', False),
    ('Satellite energy', 'E = −GMm/2r', False)], term='Chapter 7 formula sheet')

print(d.write(os.path.join(OUT, 'deck.json')), 'cards')
