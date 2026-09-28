import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase_phy as sp

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Physics', 'class11-physics-ch03-motion-in-a-plane')
d = Deck('Chapter 3: Motion in a Plane', 'Class 11', ['class-11', 'physics', 'ch-3'])
d.description = 'Vectors, resolution, addition, motion in a plane, projectile motion, relative velocity, uniform circular motion'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- 3.2 Scalars and vectors
d.sec('3.2-scalars-and-vectors')
d.basic('Scalar vs vector?', T('Scalar') + ': magnitude only (mass, time, temperature). ' + T('Vector') + ': magnitude and direction, and it obeys the ' + T('triangle/parallelogram law') + ' of addition')
d.basic('Is having magnitude and direction enough to be a vector?', X('No') + ': it must also add by the triangle law. ' + E('Electric current') + ' has a direction but adds like a scalar, so it is a scalar')
table_card(d, 'Exercises 3.1–3.3', 'Scalar or vector?', [
    ('Volume, mass, speed, density, moles', 'scalar', False), ('Angular frequency', 'scalar', False),
    ('Displacement, velocity, acceleration', 'vector', False), ('Angular velocity, impulse', 'vector', False),
    ('Work, current, pressure, energy', 'scalar', False)], term='Scalar or vector (NCERT exercises)')
d.basic('How is a vector written by hand and in print?', 'An arrow over the letter, ' + r'\( \vec v \)' + ', or bold ' + T('v') + '. Its magnitude is |v| or v')
d.basic('Position vector vs displacement vector?', T('Position vector') + ' r: from the origin to the object. ' + T('Displacement') + ' PP′: from the initial to the final position', **fig('fig_3_1_position_paths'))
d.basic('Does displacement depend on the path taken?', X('No') + ': only on the ' + T('end points') + '; every path from P to Q gives the same PQ', **fig('fig_3_1_position_paths'))
d.basic('When are two vectors equal?', 'Same ' + T('magnitude') + ' and same ' + T('direction') + '. Shift one parallel to itself: the tails and tips coincide', **fig('fig_3_2_equal_vectors'))
d.basic('Free vector vs localised vector?', T('Free') + ': can be shifted parallel to itself without change. ' + T('Localised') + ': its line of action matters (e.g. a force producing torque)')
d.basic('Exercise 3.8: three skaters go from P to Q across a circular rink of radius 200 m by different paths. Displacement of each?', N('400 m') + ' each; only ' + T('B') + ' (straight along the diameter) has path length = displacement', **fig('fig_3_19_skaters'))

# ---------------------------------------------------------------- 3.3 Multiplication by a real number
d.sec('3.3-multiplication-by-number')
d.basic('λA for λ > 0 and λ < 0?', 'λ > 0: same direction, magnitude λ|A|. λ < 0: ' + T('opposite') + ' direction, magnitude |λ||A|', **fig('fig_3_3_scalar_multiple'))
d.basic('Dimensions of λA when λ has units?', 'Product of the two, e.g. velocity × time = ' + T('displacement'))

# ---------------------------------------------------------------- 3.4 Graphical addition
d.sec('3.4-graphical-addition')
d.basic('Triangle (head-to-tail) law?', 'Place the tail of B at the head of A; the resultant R = A + B runs from the ' + T('tail of A to the head of B'), **fig('fig_3_4_addition_laws'))
d.cloze('Vector addition is {{c1::commutative}} (A + B = B + A) and {{c2::associative}} ((A + B) + C = A + (B + C)).')
d.basic('Parallelogram law?', 'Put A and B tail to tail; the ' + T('diagonal') + ' from the common tail is A + B. Equivalent to the triangle law', **fig('fig_3_6_parallelogram'))
d.basic('What is a null (zero) vector? Its properties?', 'Magnitude 0, direction undefined. A + 0 = A, λ0 = 0, 0A = 0. E.g. displacement after returning to the start')
d.basic('How is A − B defined?', r'\( \vec A - \vec B = \vec A + (-\vec B) \)' + ': add the reverse of B', **fig('fig_3_5_subtraction'))
d.basic('Correction: NCERT 3.4 says "as mentioned in section 4.2". Which section?', 'Section ' + T('3.2') + ' (Scalars and vectors). The reference is left over from the old chapter numbering')
d.basic('Example 3.1: rain falls at 35 m/s, wind blows east to west at 12 m/s. How should the umbrella be held?', 'Resultant ' + N('37 m/s') + ' at tan⁻¹(12/35) ≈ ' + N('19°') + ' to the vertical; tilt the umbrella ' + T('towards the east'), **fig('drawn_rain_umbrella'))

# ---------------------------------------------------------------- 3.5 Resolution
d.sec('3.5-resolution')
d.basic('Resolving A along two non-collinear vectors a and b in its plane?', r'\( \vec A = \lambda \vec a + \mu \vec b \)' + ' for suitable real numbers λ, μ')
d.basic('What is a unit vector?', 'A vector of magnitude ' + N('1') + ' that only gives a direction; ' + X('no') + ' unit or dimension. ' + r'\( \hat n = \dfrac{\vec A}{|\vec A|} \)')
d.basic('î, ĵ, k̂?', 'Unit vectors along x, y and z; mutually ' + T('perpendicular') + '; |î| = |ĵ| = |k̂| = 1')
d.basic('Components of A making angle θ with the x-axis?', r'\( A_x = A\cos\theta,\ A_y = A\sin\theta \)', **fig('drawn_components'))
d.basic('Magnitude and direction from components?', r'\( A = \sqrt{A_x^2 + A_y^2},\ \tan\theta = \dfrac{A_y}{A_x} \)', **fig('drawn_components'))
d.basic('Is Aₓ a vector?', X('No') + ': Aₓ is a real number (can be +, − or 0); ' + T('Aₓî') + ' is the vector component')
d.basic('3D components with direction angles α, β, γ?', r'\( A_x = A\cos\alpha,\ A_y = A\cos\beta,\ A_z = A\cos\gamma,\ A = \sqrt{A_x^2 + A_y^2 + A_z^2} \)')
d.basic('Teacher addition: sum of squares of direction cosines?', r'\( \cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1 \)')
d.basic('Exercise 3.19: magnitude and direction of î + ĵ and î − ĵ?', N('√2') + ' at ' + N('45°') + ' and ' + N('√2') + ' at ' + N('−45°') + ' to the x-axis')

# ---------------------------------------------------------------- 3.6 Analytical addition
d.sec('3.6-analytical-addition')
d.basic('Adding vectors by components?', 'Add like components: ' + r'\( R_x = A_x + B_x,\ R_y = A_y + B_y,\ R_z = A_z + B_z \)')
d.basic('Why prefer the analytical method?', 'The graphical method is ' + X('tedious and less accurate'))
d.basic('Resultant of A and B at angle θ (law of cosines)?', r'\( R = \sqrt{A^2 + B^2 + 2AB\cos\theta} \)', **fig('drawn_resultant'))
d.basic('Direction of the resultant (angle α with A)?', r'\( \tan\alpha = \dfrac{B\sin\theta}{A + B\cos\theta} \)', **fig('drawn_resultant'))
d.basic('Law of sines for the vector triangle (Fig. 3.10)?', r'\( \dfrac{R}{\sin\theta} = \dfrac{A}{\sin\beta} = \dfrac{B}{\sin\alpha} \)', **fig('fig_3_10_resultant'))
table_card(d, 'Teacher addition · resultant of A and B', 'Resultant R?', [
    ('θ = 0° (parallel)', 'A + B (maximum)', False), ('θ = 180° (antiparallel)', '|A − B| (minimum)', False),
    ('θ = 90°', '√(A² + B²)', False), ('A = B, θ = 120°', 'A (same size as each)', False), ('A = B, any θ', '2A cos(θ/2)', False)],
    term='Resultant in special cases')
d.basic('Range of possible resultants of A and B?', r'\( |A - B| \le R \le A + B \)' + ' (Exercise 3.6; equality only for collinear vectors)')
d.basic('Example 3.3: boat heads north at 25 km/h; current 10 km/h at 60° east of south. Resultant?', r'\( R = \sqrt{25^2 + 10^2 + 2(25)(10)\cos 120^\circ} \approx \)' + ' ' + N('22 km/h') + ', about ' + N('23.4°') + ' east of north', **fig('fig_3_11_boat'))
d.basic('Exercise 3.5(e): can three vectors not in one plane add to zero?', X('No') + ': the sum of two lies in their plane, so the third must lie there too')
d.basic('Exercise 3.7: a + b + c + d = 0. Must each be zero?', X('No') + '. But |a + c| = |b + d| and |a| ≤ |b| + |c| + |d| are true')

# ---------------------------------------------------------------- 3.7 Motion in a plane
d.sec('3.7-motion-in-a-plane')
d.basic('Position and displacement in a plane?', r'\( \vec r = x\hat i + y\hat j \)' + ', ' + r'\( \Delta\vec r = \Delta x\,\hat i + \Delta y\,\hat j \)', **fig('fig_3_12_position_velocity'))
d.basic('Average velocity in a plane: direction?', 'Along the ' + T('displacement Δr') + ' (chord), since v̄ = Δr/Δt')
d.basic('Direction of instantaneous velocity?', 'Along the ' + T('tangent') + ' to the path, in the direction of motion')
d.basic('Velocity components and magnitude?', r'\( v_x = \dfrac{dx}{dt},\ v_y = \dfrac{dy}{dt},\ v = \sqrt{v_x^2 + v_y^2},\ \tan\theta = \dfrac{v_y}{v_x} \)')
d.basic('Angle between v and a in 1D vs 2D?', '1D: ' + T('0° or 180°') + '. In 2D/3D: ' + T('any angle') + ' from 0° to 180°')
d.basic('Example 3.4: r = 3.0t î + 2.0t² ĵ + 5.0 k̂. v, a, and v at t = 1 s?', 'v = 3.0î + 4.0t ĵ; a = ' + N('4.0 ĵ m s⁻²') + '; at 1 s: ' + N('5.0 m/s') + ' at ' + N('53°') + ' to x')
d.basic('Exercise 3.17: r = 3.0t î − 2.0t² ĵ + 4.0 k̂. Speed at t = 2 s?', 'v = 3î − 8ĵ → ' + N('8.54 m/s') + ', 70° below the x-axis; a = ' + N('−4.0 ĵ'))
table_card(d, 'Exercise 3.20', 'True for any motion?', [
    ('v_avg = ½[v(t₁) + v(t₂)]', 'No (constant a only)', True), ('v_avg = [r(t₂) − r(t₁)]/(t₂ − t₁)', 'Yes', False),
    ('v(t) = v(0) + at', 'No', True), ('r(t) = r(0) + v(0)t + ½at²', 'No', True), ('a_avg = [v(t₂) − v(t₁)]/(t₂ − t₁)', 'Yes', False)],
    note='Definitions always hold; the kinematic equations need constant acceleration.', term='Which relations hold for arbitrary motion')

# ---------------------------------------------------------------- 3.8 Constant acceleration
d.sec('3.8-constant-acceleration')
d.basic('Vector equations for constant acceleration in a plane?', r'\( \vec v = \vec v_0 + \vec a t,\quad \vec r = \vec r_0 + \vec v_0 t + \tfrac12 \vec a t^2 \)')
d.basic('Key idea of 3.8?', 'Motion in a plane = ' + T('two independent 1D motions') + ' along perpendicular axes, linked only by time')
steps_card(d, 'Example 3.5', 'Find the missing step.', 'Starts at origin with 5.0î m/s; a = (3.0î + 2.0ĵ) m/s². y and speed when x = 84 m?',
           ['x = 5t + 1.5t², y = 1.0t²', '5t + 1.5t² = 84 → t = 6 s', 'y = 36 m', 'v = (5 + 3t)î + 2tĵ = 23î + 12ĵ → <b>26 m/s</b>'], 1,
           'Example 3.5: constant acceleration in a plane', 't = 6 s from x = 84 m; y = 36 m; speed ≈ 26 m/s')
d.basic('Exercise 3.18: from origin with 10ĵ m/s, a = (8î + 2ĵ) m/s². When is x = 16 m? y then?', 't = ' + N('2 s') + ', y = ' + N('24 m') + ', speed ' + N('21.26 m/s'))

# ---------------------------------------------------------------- 3.9 Projectile motion
d.sec('3.9-projectile-motion')
d.basic('What is a projectile?', 'An object in flight after being thrown or projected, moving under ' + T('gravity alone') + ' (air resistance neglected)')
d.basic('Who first stated that horizontal and vertical motions of a projectile are independent?', T('Galileo') + ' (Dialogue on the Great World Systems, 1632)')
sp.projectile_shadows(d)
d.basic('Acceleration and initial velocity components of a projectile?', r'\( a_x = 0,\ a_y = -g;\ \ u_x = u\cos\theta,\ u_y = u\sin\theta \)', **fig('drawn_projectile'))
d.basic('Position and velocity of a projectile at time t?', r'\( x = (u\cos\theta)t,\ y = (u\sin\theta)t - \tfrac12 gt^2;\ v_x = u\cos\theta,\ v_y = u\sin\theta - gt \)')
d.basic('Equation of trajectory?', r'\( y = x\tan\theta - \dfrac{g x^2}{2u^2\cos^2\theta} \)' + ': form y = ax − bx², a ' + T('parabola'))
table_card(d, '3.9 · projectile formulas', 'Formula?', [
    ('Time to reach the top tₘ', 'u sin θ / g', False), ('Time of flight T', '2u sin θ / g', False),
    ('Maximum height H', 'u² sin²θ / 2g', False), ('Horizontal range R', 'u² sin 2θ / g', False), ('Maximum range', 'u²/g at θ = 45°', False)],
    term='Projectile formulas (ground to ground)')
d.basic('Why is T = 2tₘ?', 'The parabola is ' + T('symmetric') + ': rising and falling take equal time (same level, no air)')
d.basic('Velocity at the highest point?', r'\( u\cos\theta \)' + ', horizontal (vᵧ = 0). Acceleration there is still ' + T('g downward'), **fig('drawn_projectile'))
d.basic('Speed and angle at landing (same level)?', 'Speed ' + T('u') + ' again, at θ ' + T('below') + ' the horizontal')
d.basic('Minimum speed of a projectile and where?', r'\( u\cos\theta \)' + ' at the ' + T('top') + '. Minimum kinetic energy = K cos²θ')
sp.complementary_ranges(d)
d.basic('Example 3.6: prove that 45° + α and 45° − α give equal ranges.', 'sin 2θ = sin(90° ± 2α) = ' + T('cos 2α') + ' for both')
d.basic('Teacher addition: relation between range and maximum height?', r'\( R = 4H\cot\theta \)' + '; at θ = 45°, ' + r'\( H = R/4 \)')
d.basic('Teacher addition: projectiles at θ and 90° − θ (same u). Product of their times of flight?', r'\( T_1 T_2 = \dfrac{2R}{g} \)')
d.basic('Example 3.8: cricket ball at 28 m/s, 30° above horizontal. H, T, R?', 'H = ' + N('10.0 m') + ', T = ' + N('2.9 s') + ', R = ' + N('69 m'))
d.basic('Exercise 3.13: a cricketer can throw 100 m at most. How high can he throw the same ball?', N('50 m') + ' (u²/g = 100 m; H = u²/2g)')
steps_card(d, 'Exercise 3.12', 'Find the missing step.', 'Ceiling 25 m high, ball thrown at 40 m/s. Max horizontal distance without hitting the ceiling?',
           ['Set H = 25: u² sin²θ / 2g = 25', 'sin²θ = 2 × 9.8 × 25 / 1600 = 0.306 → θ ≈ 33.6°', 'R = u² sin 2θ / g = 1600 × sin 67.2° / 9.8', '<b>R ≈ 150.5 m</b>'], 1,
           'Ball under a 25 m ceiling', 'Choose θ so that H = 25 m (θ ≈ 33.6°), then R ≈ 150.5 m')

d.sec('3.9-horizontal-projection')
d.basic('Thrown horizontally at u from height h: time to reach the ground?', r'\( t = \sqrt{\dfrac{2h}{g}} \)' + ', ' + T('independent of u'))
d.basic('Thrown horizontally at u from height h: horizontal distance?', r'\( x = u\sqrt{\dfrac{2h}{g}} \)')
d.basic('Example 3.7: stone thrown horizontally at 15 m/s from a 490 m cliff. Time and impact speed?', N('10 s') + '; vᵧ = 98 m/s, speed = √(15² + 98²) ≈ ' + N('99 m/s'))
d.basic('One ball is dropped and another thrown horizontally from the same height at the same time. Which lands first?', T('Together') + ': vertical motion is identical (uᵧ = 0 for both)')
d.basic('Trap: does a projectile’s path depend only on its acceleration?', X('No') + ': the same g gives a straight line (thrown vertically) or a parabola, depending on the ' + T('initial velocity'))

# ---------------------------------------------------------------- Relative velocity in 2D
d.sec('3.x-relative-velocity-2d')
d.basic('Resultant velocity vs relative velocity?', T('Resultant') + ': an object with two velocities has v = v₁ + v₂. ' + T('Relative') + ': v₁₂ = v₁ − v₂ (velocity of 1 as seen from 2)')
d.basic('Rain falls vertically; you walk forward. Which way should you tilt the umbrella?', T('Forward') + ': the rain relative to you is v_rain − v_you, which slants towards you')
d.basic('Crossing a river of width d in the least time: heading and time?', 'Head ' + T('perpendicular') + ' to the bank; t = d/vʙ; drift = vᵣd/vʙ', **fig('drawn_river'))
d.basic('Crossing a river along the shortest path (straight across): heading?', 'Upstream at angle θ to the normal with ' + r'\( \sin\theta = \dfrac{v_r}{v_b} \)' + '; time ' + r'\( \dfrac{d}{\sqrt{v_b^2 - v_r^2}} \)', **fig('drawn_river'))
d.basic('Trap: can a boat reach the opposite point if the river is faster than the boat?', X('No') + ': sin θ = vᵣ/vʙ > 1 is impossible; it will always drift downstream')

# ---------------------------------------------------------------- 3.10 Uniform circular motion
d.sec('3.10-uniform-circular-motion')
d.basic('What is uniform circular motion?', 'Motion in a circle at ' + T('constant speed'))
sp.circular_arrows(d)
d.basic('Magnitude and direction of centripetal acceleration?', r'\( a_c = \dfrac{v^2}{R} = \omega^2 R \)' + ', towards the ' + T('centre'), **fig('drawn_circular'))
d.basic('How is v²/R derived (Fig. 3.18)?', 'Triangles of position vectors and velocity vectors are ' + T('similar') + ': |Δv|/v = |Δr|/R, and |Δr| ≈ vΔt')
d.basic('Is centripetal acceleration a constant vector?', X('No') + ': constant magnitude, but its direction keeps changing')
d.basic('Can the kinematic equations be used for uniform circular motion?', X('No') + ': acceleration is not constant in direction')
d.basic('Who named centripetal acceleration, and who first published its analysis?', T('Newton') + ' named it ("centre-seeking"); ' + T('Huygens') + ' published the analysis in 1673')
d.basic('Define angular speed and relate it to v.', r'\( \omega = \dfrac{\Delta\theta}{\Delta t} \)' + ' ; ' + r'\( v = R\omega \)')
d.basic('ω, v, a in terms of frequency ν?', r'\( \omega = 2\pi\nu,\ v = 2\pi R\nu,\ a_c = 4\pi^2\nu^2 R \)')
d.basic('Example 3.9: insect in a 12 cm groove makes 7 revolutions in 100 s. ω, v, a?', 'ω = ' + N('0.44 rad/s') + ', v = ' + N('5.3 cm/s') + ', a = ' + N('2.3 cm/s²') + ' (not a constant vector)')
d.basic('Exercise 3.14: stone on an 80 cm string makes 14 revolutions in 25 s. Acceleration?', N('9.9 m s⁻²') + ' along the radius, towards the centre')
d.basic('Exercise 3.15: aircraft loop of radius 1.00 km at 900 km/h. a_c compared with g?', 'a = 250²/1000 = 62.5 m s⁻² ≈ ' + N('6.4 g'))
d.basic('Is the net acceleration in any circular motion towards the centre?', X('Only if the speed is constant') + '. If speed changes, there is also a tangential component')
d.basic('Exercise 3.16(c): average acceleration over one full cycle of uniform circular motion?', N('Zero') + ' (the velocity returns to its starting value)')

# ---------------------------------------------------------------- Exercises on path vs displacement
d.sec('exercises')
d.basic('Exercise 3.9: cyclist goes O → P (1 km), a quarter circle, then back to O in 10 min. Displacement, average velocity, average speed?', N('0') + ', ' + N('0') + ', and (2 + π/2) km ÷ 1/6 h ≈ ' + N('21.4 km/h'), **fig('fig_3_20_cyclist'))
d.basic('Exercise 3.11: cab takes 23 km in 28 min to reach a hotel 10 km away. Average speed and |average velocity|?', N('49.3 km/h') + ' and ' + N('21.4 km/h') + '; equal only for a straight path')
d.basic('Exercise 3.22: aircraft at 3400 m; positions 10 s apart subtend 30° at an observer. Speed?', 'Distance = 2 × 3400 tan 15° ≈ 1822 m → ' + N('182 m/s'))
table_card(d, 'Exercise 3.21', 'A scalar quantity is one that…', [
    ('is conserved in a process', 'False (e.g. KE in inelastic collision)', True), ('can never be negative', 'False (temperature in °C)', True),
    ('must be dimensionless', 'False (mass)', True), ('does not vary in space', 'False (temperature)', True),
    ('is the same for observers with rotated axes', 'True', False)], term='What makes a quantity a scalar')

# ---------------------------------------------------------------- Summary
d.sec('summary')
table_card(d, 'Summary · projectile at the top', 'Value at the highest point?', [
    ('Vertical velocity', '0', False), ('Horizontal velocity', 'u cos θ', False), ('Acceleration', 'g downward', False),
    ('Angle between v and a', '90°', False)], term='Projectile at its highest point')
table_card(d, 'Summary', 'Which is constant?', [
    ('Projectile: horizontal velocity', 'constant', False), ('Projectile: acceleration', 'constant (g)', False),
    ('Uniform circular motion: speed', 'constant', False), ('Uniform circular motion: velocity', 'not constant', True),
    ('Uniform circular motion: acceleration', 'not constant (direction turns)', True)], term='What stays constant: projectile vs circular motion')

print(d.write(os.path.join(OUT, 'deck.json')), 'cards')
