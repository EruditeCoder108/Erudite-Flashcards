import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase_phy as sp

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Physics', 'class11-physics-ch05-work-energy-and-power')
d = Deck('Chapter 5: Work, Energy and Power', 'Class 11', ['class-11', 'physics', 'ch-5'])
d.description = 'Dot product, work, kinetic energy, work-energy theorem, potential energy, springs, conservation of energy, power, collisions'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- 5.1 Scalar product
d.sec('5.1-scalar-product')
d.basic('Define the scalar (dot) product.', r'\( \vec A \cdot \vec B = AB\cos\theta \)' + ': a ' + T('scalar') + ', θ = angle between the vectors')
d.basic('Geometric meaning of A · B?', '|A| × (component of B along A) = |B| × (' + T('projection') + ' of A on B)')
d.cloze('The dot product is {{c1::commutative}} (A·B = B·A) and {{c2::distributive}} (A·(B + C) = A·B + A·C).')
d.basic('î·î and î·ĵ?', 'î·î = ĵ·ĵ = k̂·k̂ = ' + N('1') + '; î·ĵ = ĵ·k̂ = k̂·î = ' + N('0'))
d.basic('A · B in components?', r'\( A_xB_x + A_yB_y + A_zB_z \)')
d.basic('What does A · B = 0 mean (non-zero vectors)?', 'A and B are ' + T('perpendicular'))
d.basic('A · A = ?', r'\( A^2 = A_x^2 + A_y^2 + A_z^2 \)')
d.basic('Example 5.1: F = 3î + 4ĵ − 5k̂, d = 5î + 4ĵ + 3k̂. Angle between them?', 'F·d = 15 + 16 − 15 = 16; |F| = |d| = √50 → cos θ = 16/50 = ' + N('0.32'))
d.basic('Teacher addition: projection of A on B?', r'\( \dfrac{\vec A \cdot \vec B}{|\vec B|} \)')

# ---------------------------------------------------------------- 5.2 Work-energy theorem
d.sec('5.2-work-energy-theorem')
d.basic('How does v² − u² = 2as lead to the work-energy idea?', 'Multiply by m/2: ½mv² − ½mu² = mas = ' + T('Fs'))
d.basic('State the work-energy theorem.', 'Change in kinetic energy of a particle = work done on it by the ' + T('net force') + ': K𝒻 − Kᵢ = W')
d.basic('Correction: NCERT 5.2 says v² − u² = 2as was met "in Chapter 3". Where was it?', 'In ' + T('Chapter 2') + ' (Motion in a Straight Line); the reference is left over from the old numbering')
steps_card(d, 'Example 5.2 · raindrop', 'Find the missing step.', '1.00 g drop falls 1.00 km and hits the ground at 50.0 m/s (g = 10). Work by the resistive force?',
           ['ΔK = ½ × 10⁻³ × 50² = 1.25 J', 'W(gravity) = mgh = 10⁻³ × 10 × 10³ = 10.0 J', 'W-E theorem: ΔK = W(gravity) + W(resistive)',
            'W(resistive) = 1.25 − 10 = <b>−8.75 J</b>'], 2, 'Raindrop: work by air resistance', 'W(resistive) = ΔK − W(gravity) = 1.25 − 10 = −8.75 J')
d.basic('What does Example 5.2 show about unknown forces?', 'The work of a force can be found from the W-E theorem ' + T('without knowing the force law'))

# ---------------------------------------------------------------- 5.3 Work
d.sec('5.3-work')
d.basic('Define work done by a constant force.', r'\( W = Fd\cos\theta = \vec F \cdot \vec d \)' + ': component of force along the displacement × displacement', **fig('drawn_work_angle'))
table_card(d, '5.3 · zero work', 'Why is no work done?', [
    ('Pushing a rigid wall', 'displacement = 0', False), ('Weightlifter holding 150 kg steady', 'displacement = 0', False),
    ('Block sliding on a smooth table (horizontal)', 'horizontal force = 0', False), ('Gravity on a block moving horizontally', 'F ⟂ d', False),
    ('Earth’s pull on the Moon (circular orbit)', 'F ⟂ d', False)], term='When is no work done?')
d.basic('Why do you get tired pushing a wall though no work is done on it?', 'Your muscles repeatedly ' + T('contract and relax') + ', using internal energy')
d.basic('Sign of work for θ < 90°, θ = 90°, θ > 90°?', N('Positive') + ', ' + N('zero') + ', ' + N('negative') + ' (friction usually has θ = 180°)')
d.basic('Dimensions and SI unit of work and energy?', '[M L² T⁻²]; ' + T('joule') + ' (J), after James Prescott Joule')
table_card(d, 'Table 5.1', 'Value in joules?', [
    ('1 erg', '10⁻⁷ J', False), ('1 electron volt (eV)', '1.6 × 10⁻¹⁹ J', False),
    ('1 calorie (cal)', '4.186 J', False), ('1 kilowatt hour (kWh)', '3.6 × 10⁶ J', False)], term='Alternative units of work and energy (Table 5.1)')
d.basic('Example 5.3: a cyclist skids to a stop in 10 m; road force 200 N. Work by the road on the cycle, and by the cycle on the road?',
        N('−2000 J') + ' on the cycle; ' + N('zero') + ' on the road (the road does not move)')
d.basic('Lesson of Example 5.3?', 'Action and reaction are equal and opposite, but the ' + X('work') + ' they do need not be equal and opposite')
table_card(d, 'Exercise 5.1', 'Sign of the work?', [
    ('Man lifting a bucket out of a well', 'positive', False), ('Gravity on that bucket', 'negative', True),
    ('Friction on a body sliding down an incline', 'negative', True), ('Applied force, body moving uniformly on rough floor', 'positive', False),
    ('Air resistance on a swinging pendulum', 'negative', True)], term='Signs of work (Exercise 5.1)')
d.basic('Exercise 5.11: F = (−î + 2ĵ + 3k̂) N; the body moves 4 m along z. Work?', 'Only the z-component works: ' + N('3 × 4 = 12 J'))

# ---------------------------------------------------------------- 5.4 Kinetic energy
d.sec('5.4-kinetic-energy')
d.basic('Kinetic energy formula; scalar or vector?', r'\( K = \tfrac12 mv^2 = \tfrac12 m\,\vec v \cdot \vec v \)' + ' ; a ' + T('scalar') + ', never negative')
d.basic('Relation between kinetic energy and momentum?', r'\( K = \dfrac{p^2}{2m}, \quad p = \sqrt{2mK} \)')
d.basic('Same kinetic energy: which has more momentum, a heavy or a light body?', 'The ' + T('heavier') + ' (p = √(2mK))')
d.basic('Same momentum: which has more kinetic energy?', 'The ' + T('lighter') + ' (K = p²/2m)')
d.basic('Table 5.2: typical kinetic energies of a car, a bullet, an air molecule?', 'Car ~' + N('6 × 10⁵ J') + ', bullet ~' + N('10³ J') + ', air molecule ~' + N('10⁻²¹ J'), **fig('tab_5_2_kinetic_energies'))
d.basic('Example 5.4: 50 g bullet at 200 m/s keeps 10 % of its KE after passing through plywood. Emergent speed?', N('63.2 m/s') + ': speed falls by about 68 %, ' + X('not 90 %') + ' (K ∝ v²)')
d.basic('Exercise 5.12: electron with 10 keV, proton with 100 keV. Which is faster?', 'The ' + T('electron') + ', about ' + N('13.5×') + ' faster (v = √(2K/m))')

# ---------------------------------------------------------------- 5.5-5.6 Variable force
d.sec('5.5-variable-force')
d.basic('Work done by a variable force?', r'\( W = \int_{x_i}^{x_f} F(x)\,dx \)' + ' = ' + T('area under the F–x graph'), **fig('drawn_variable_force'))
d.basic('Area below the x-axis on an F–x graph?', T('Negative work') + ' (force opposite to displacement)')
d.basic('Example 5.5: a woman pushes a trunk with 100 N for 10 m, then her force falls linearly to 50 N at 20 m; friction is 50 N. Work by each?', 'Woman: 1000 + 750 = ' + N('1750 J') + '; friction: ' + N('−1000 J'), **fig('drawn_ex_5_5'))
d.basic('Proof of the W-E theorem for a variable force?', r'\( \dfrac{dK}{dt} = mv\dfrac{dv}{dt} = Fv = F\dfrac{dx}{dt} \Rightarrow dK = F\,dx \)' + ', then integrate')
d.basic('W-E theorem vs Newton’s second law: what information is lost?', 'It is a ' + T('scalar, integrated') + ' form: the ' + X('time') + ' and ' + X('direction') + ' information of F = ma is not available')
d.basic('Example 5.6: 1 kg block at 2 m/s crosses a patch with F = −k/x (k = 0.5 J) from 0.1 m to 2.01 m. Final speed?', 'K𝒻 = 2 − 0.5 ln(20.1) = 2 − 1.5 = 0.5 J → v = ' + N('1 m/s'))
d.basic('Exercise 5.20: 0.5 kg body moves with v = a x^(3/2), a = 5 m^(−1/2) s⁻¹. Work by the net force from x = 0 to 2 m?', 'v² at x = 2 is 25 × 8 = 200, so W = ΔK = ½ × 0.5 × 200 = ' + N('50 J'))
d.basic('Exercise 5.2: 2 kg body pulled by 7 N on a table, μₖ = 0.1, for 10 s. Work by F, friction, net force?', N('882 J') + ', ' + N('−247 J') + ', ' + N('635 J') + ' = ΔK (W-E theorem)')

# ---------------------------------------------------------------- 5.7 Potential energy
d.sec('5.7-potential-energy')
d.basic('What is potential energy?', '"Stored" energy due to the ' + T('position or configuration') + ' of a body (stretched bowstring, strained fault lines)')
d.basic('Gravitational PE near Earth’s surface?', r'\( V(h) = mgh \)' + ' (for h ≪ R, g constant), with V = 0 at the ground')
d.basic('Relation between a conservative force and its potential energy (1D)?', r'\( F(x) = -\dfrac{dV}{dx} \)' + ' ; ΔV = −(work done by the force)')
d.basic('Why the minus sign in F = −dV/dx?', 'The force points towards ' + T('decreasing potential energy') + ' (gravity pulls down as V = mgh grows upward)')
d.basic('Block slides from rest down a smooth incline of height h. Speed at the bottom?', r'\( \sqrt{2gh} \)' + ', ' + T('independent of the angle') + ' (gravity is conservative)')
d.basic('Is potential energy defined for friction?', X('No') + ': friction is non-conservative; its work depends on the path')

# ---------------------------------------------------------------- 5.8 Conservation of mechanical energy
d.sec('5.8-conservation-of-energy')
d.basic('State the conservation of mechanical energy.', 'If only ' + T('conservative forces') + ' do work, K + V stays constant')
table_card(d, '5.8 · conservative force', 'Three equivalent definitions?', [
    ('1', 'F = −dV/dx for some scalar V(x)', False), ('2', 'Work depends only on the end points', False),
    ('3', 'Work over any closed path is zero', False)], term='Definitions of a conservative force')
d.basic('Ball dropped from height H: speed at height h?', r'\( v = \sqrt{2g(H - h)} \)' + '; at the ground, ' + r'\( \sqrt{2gH} \)')
d.basic('Example 5.7: a bob just completes a vertical circle (string slack only at the top). v at A (bottom), B (side), C (top)?', r'\( \sqrt{5gL},\ \sqrt{3gL},\ \sqrt{gL} \)', **fig('drawn_vertical_circle'))
d.basic('Why is v = √(gL) at the top of the vertical circle?', 'Tension is zero there, so gravity alone provides the centripetal force: mg = mv²/L')
d.basic('Example 5.7: ratio of kinetic energies at B and C?', N('3 : 1'))
d.basic('Example 5.7: what happens if the string is cut at C?', 'The bob has horizontal velocity √(gL) → a ' + T('projectile') + ' path, like a stone kicked off a cliff')
d.basic('Why does tension do no work on a pendulum bob?', 'Tension is always ' + T('perpendicular') + ' to the bob’s displacement')
d.basic('Is the zero of potential energy fixed?', X('No') + ': it is ' + T('arbitrary') + ', but once chosen it must be kept throughout the problem')
d.basic('Energy with a non-conservative force?', r'\( E_f - E_i = W_{nc} \)' + ' : change in mechanical energy = work by non-conservative forces (path dependent)')
d.basic('Exercise 5.18: bob released from horizontal, L = 1.5 m, loses 5 % of its energy. Speed at the bottom?', N('5.3 m/s') + ' (½v² = 0.95 gL)')

# ---------------------------------------------------------------- 5.9 Spring
d.sec('5.9-spring')
d.basic('Hooke’s law and unit of k?', r'\( F_s = -kx \)' + '; k in ' + N('N m⁻¹') + '. Stiff spring: large k')
d.basic('Work done by the spring force when it is stretched by xₘ from its natural length?', r'\( W_s = -\tfrac12 kx_m^2 \)' + ' (triangle under the Fₛ–x line); the pulling force does +½kxₘ²', **fig('drawn_spring'))
d.basic('Work done by the spring force from xᵢ to x𝒻?', r'\( W_s = -\tfrac12 k(x_f^2 - x_i^2) \)' + '; zero over a closed cycle → ' + T('conservative'))
d.basic('Potential energy of a spring?', r'\( V(x) = \tfrac12 kx^2 \)' + ', zero at the natural length')
sp.spring_energy_bars(d)
d.basic('Block on a spring released from xₘ: maximum speed, and where?', r'\( v_m = x_m\sqrt{\dfrac{k}{m}} \)' + ' at the ' + T('equilibrium position') + ' x = 0', **fig('drawn_spring'))
d.basic('Exercise 5.4: V = ½kx², k = 0.5 N/m, total energy 1 J. Where does the particle turn back?', 'Where V = E: ½ × 0.5 × x² = 1 → ' + N('x = ±2 m') + ' (KE would be negative beyond)')
d.basic('Example 5.8 (NCERT): a 1000 kg car at 18 km/h hits a spring, k = 5.25 × 10³ N/m. NCERT’s maximum compression?', N('2.00 m') + ' (½mv² = ½kxₘ², K = 1.25 × 10⁴ J)', **fig('fig_5_9_car_spring'))
d.basic('Correction: recompute Example 5.8 with k = 5.25 × 10³ N/m as printed.', 'xₘ = √(2 × 12500 / 5250) = ' + T('2.18 m') + '<br>NCERT’s 2.00 m (and 1.35 m in Example 5.9) fit ' + T('k = 6.25 × 10³ N/m') + '<br>The printed k is a typo')
d.basic('Example 5.9: the same car with friction μ = 0.5. Equation for xₘ?', r'\( \tfrac12 mv^2 = \tfrac12 kx_m^2 + \mu mg\,x_m \)' + ' → with k = 6.25 × 10³: ' + N('1.35 m') + ' (less than without friction)')
d.basic('Useful conversion from Example 5.8?', N('36 km/h = 10 m/s') + ' (multiply km/h by 5/18)')
d.basic('What can energy conservation NOT tell you in the car–spring problem?', 'The ' + X('time') + ' taken to compress; that needs Newton’s second law')

# ---------------------------------------------------------------- 5.10 Power
d.sec('5.10-power')
d.basic('Define average and instantaneous power.', r'\( P_{av} = \dfrac{W}{t},\quad P = \dfrac{dW}{dt} = \vec F \cdot \vec v \)')
d.basic('Unit and dimensions of power; 1 hp?', T('watt') + ' (1 W = 1 J/s), [M L² T⁻³]; 1 hp = ' + N('746 W'))
d.basic('Is kWh a unit of power?', X('No') + ': of energy. 1 kWh = ' + N('3.6 × 10⁶ J') + ' (a 100 W bulb for 10 h)')
steps_card(d, 'Example 5.10 · elevator', 'Find the missing step.', '1800 kg elevator rises at a constant 2 m/s against 4000 N friction (g = 10). Minimum motor power?',
           ['Constant speed → motor force balances the downward forces', 'F = mg + f = 18000 + 4000 = 22000 N', 'P = Fv = 22000 × 2 = 44000 W', '= 44000 / 746 ≈ <b>59 hp</b>'], 1,
           'Elevator motor power', 'P = (mg + f) v = 22000 × 2 = 44 kW ≈ 59 hp')
d.basic('Exercise 5.9: body from rest with constant acceleration. Power delivered ∝ ?', T('t') + ' (P = Fv = ma · at)')
d.basic('Exercise 5.10: body driven by a constant power. Displacement ∝ ?', T('t^(3/2)') + ' (½mv² = Pt → v ∝ t^½)')
d.basic('Exercise 5.15: a pump fills 30 m³ at 40 m height in 15 min with 30 % efficiency. Electric power?', 'Useful power = 30000 × 9.8 × 40 / 900 ≈ 13.1 kW → input ' + N('43.6 kW'))
d.basic('Exercise 5.21: windmill of area A, wind speed v, air density ρ. Mass and KE of the air in time t?', r'\( m = \rho A v t,\quad K = \tfrac12 \rho A v^3 t \)' + '; 25 % of that with A = 30 m², v = 10 m/s → ' + N('4.5 kW'))

# ---------------------------------------------------------------- 5.11 Collisions
d.sec('5.11-collisions')
d.basic('What is conserved in every collision?', 'Total ' + T('linear momentum') + ' (and total energy); kinetic energy ' + X('only in elastic') + ' collisions')
d.basic('Why is momentum conserved in a collision whatever the forces?', 'By the ' + T('third law') + ', the impulses on the two bodies are equal and opposite at every instant')
table_card(d, '5.11.1 · types of collision', 'Kinetic energy after the collision?', [
    ('Elastic', 'conserved', False), ('Inelastic', 'partly lost (heat, sound, deformation)', True),
    ('Completely inelastic', 'maximum loss; bodies move together', True)], term='Elastic, inelastic and completely inelastic collisions')
d.basic('During an elastic collision (balls in contact), is KE conserved?', X('No') + ': KE is conserved only ' + T('after') + ' the collision; during contact some is stored as deformation. Momentum is conserved at every instant')
d.basic('Completely inelastic collision: m₁ at v hits m₂ at rest. Common velocity?', r'\( v_f = \dfrac{m_1 v}{m_1 + m_2} \)')
d.basic('KE lost in that completely inelastic collision?', r'\( \Delta K = \dfrac{1}{2}\dfrac{m_1 m_2}{m_1 + m_2}v^2 \)')
d.basic('Elastic 1D collision, m₂ at rest: final velocities?', r'\( v_{1f} = \dfrac{m_1 - m_2}{m_1 + m_2}v_{1i},\quad v_{2f} = \dfrac{2m_1}{m_1 + m_2}v_{1i} \)')
d.basic('Elastic 1D collision: relative velocity before and after?', 'Speed of separation = speed of approach: ' + r'\( v_{2f} - v_{1f} = v_{1i} - v_{2i} \)' + ' (coefficient of restitution e = 1)')
sp.collision_1d(d)
table_card(d, '5.11.2 · special cases (elastic, m₂ at rest)', 'Result?', [
    ('m₁ = m₂', 'm₁ stops, m₂ moves off with v₁ᵢ (velocities exchange)', False),
    ('m₂ ≫ m₁ (ball on a wall)', 'm₁ bounces back with −v₁ᵢ; m₂ stays at rest', False),
    ('m₁ ≫ m₂', 'm₁ barely slows; m₂ flies off at ≈ 2v₁ᵢ', False)], term='Special cases of elastic collisions')
d.basic('Example 5.11: why are heavy water or graphite used as moderators?', 'A neutron loses most of its KE to a ' + T('light') + ' nucleus.<br>Deuterium takes 8/9 of it per head-on collision, carbon 28.4 %')
d.basic('Fraction of KE a neutron keeps after a head-on elastic collision with a nucleus of mass m₂?', r'\( f_1 = \left(\dfrac{m_1 - m_2}{m_1 + m_2}\right)^2 \)' + '; deuterium: 1/9, carbon: 71.6 %')
d.basic('What is a head-on (1D) collision?', 'Initial and final velocities lie on one line: the path of body 1 passes through the ' + T('centre') + ' of body 2')
d.basic('2D collision, m₂ at rest: momentum equations?', r'\( m_1v_{1i} = m_1v_{1f}\cos\theta_1 + m_2v_{2f}\cos\theta_2;\ \ 0 = m_1v_{1f}\sin\theta_1 - m_2v_{2f}\sin\theta_2 \)', **fig('fig_5_10_collision_2d'))
d.basic('Why can a 2D elastic collision not be solved from the conservation laws alone?', 'Four unknowns (two final speeds, two angles) but only three equations; one (e.g. θ₁) must be measured')
d.basic('Example 5.12: equal billiard balls, elastic glancing collision, target goes off at 37°. Angle of the cue ball?', N('53°') + ': equal masses, one at rest → they move off at ' + T('90°') + ' to each other')
d.basic('What is scattering?', 'A "collision" through ' + T('action at a distance') + ' without touching (a comet near the Sun, an α-particle near a nucleus)')
d.basic('Exercise 5.16: a ball hits two identical touching balls head-on (elastic). Result?', 'The first two end at rest; the ' + T('last ball') + ' moves off with V', **fig('fig_5_14_ball_bearings'))
d.basic('Exercise 5.17: bob A released from 30° hits identical bob B at rest (elastic). How high does A rise?', X('Not at all') + ': equal masses exchange velocities; A stops and B moves on', **fig('fig_5_15_pendulum_bobs'))
d.basic('Exercise 5.19: sand leaks out of a trolley moving at 27 km/h on a frictionless track. Final speed?', N('27 km/h') + ': the sand leaves with the trolley’s own velocity, so no horizontal force acts')
d.basic('Exercise 5.14: a molecule hits a wall at 200 m/s, 30° to the normal, and rebounds with the same speed. Momentum conserved? Elastic?', 'Momentum of molecule + wall ' + T('is') + ' conserved (the wall’s recoil is negligible); KE is conserved → ' + T('elastic'))

# ---------------------------------------------------------------- Exercises
d.sec('exercises')
d.basic('Exercise 5.5(b): why is the work done by the Sun’s gravity on a comet zero over each full orbit?', 'Gravity is ' + T('conservative') + '; over a closed path the PE returns to its starting value')
d.basic('Exercise 5.5(c): a satellite loses energy to air drag, yet it speeds up as it spirals in. Why?', 'PE falls ' + T('twice as fast') + ' as the total energy, so KE rises (for a circular orbit KE = −E)')
d.basic('Exercise 5.5(a): the casing of a rocket burns up by friction. Whose energy is used?', 'The ' + T('rocket’s') + ' (its kinetic and potential energy)')
d.basic('Exercise 5.5(d): a man walks 2 m carrying 15 kg in his hands, or walks 2 m pulling a rope that lifts 15 kg over a pulley. When is more work done?', 'Pulling: the load rises, W = mgh = 15 × 9.8 × 2 = ' + N('294 J') + '. Carrying horizontally does ' + X('no work against gravity'), **fig('fig_5_13_man_load'))
table_card(d, 'Exercises 5.6–5.7', 'Correct choice?', [
    ('Conservative force does positive work → PE…', 'decreases', False), ('Work against friction costs…', 'kinetic energy', False),
    ('Inelastic collision: unchanged quantities', 'total momentum and total energy', False),
    ('Work over a closed loop is zero for every force', 'False (friction)', True),
    ('Inelastic collision: final KE < initial KE, always', 'False (usually, not always)', True)], term='Energy concept checks (Exercises 5.6–5.7)')
d.basic('Exercise 5.3 (Fig. 5.11): with total energy E, where can a particle NOT be found?', 'Where ' + T('V(x) > E') + ' (KE would be negative). The minimum energy needed is the lowest V', **img('fig_5_11_pe_functions'))
d.basic('Exercise 5.22: lifting 10 kg through 0.5 m, 1000 times. Work against gravity, and fat used at 20 % efficiency (3.8 × 10⁷ J/kg)?', N('49 000 J') + ' and ' + N('6.45 × 10⁻³ kg'))

d.sec('summary')
table_card(d, 'Summary', 'Formula?', [
    ('Work (constant F)', 'F · d = Fd cos θ', False), ('Kinetic energy', '½mv² = p²/2m', False), ('Gravitational PE', 'mgh', False),
    ('Spring PE', '½kx²', False), ('Power', 'dW/dt = F · v', False)], term='Chapter 5 formula sheet')

print(d.write(os.path.join(OUT, 'deck.json')), 'cards')
