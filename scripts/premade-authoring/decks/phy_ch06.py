import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase_phy as sp

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Physics', 'class11-physics-ch06-systems-of-particles-and-rotational-motion')
d = Deck('Chapter 6: Systems of Particles and Rotational Motion', 'Class 11', ['class-11', 'physics', 'ch-6'])
d.description = 'Centre of mass, cross product, torque, angular momentum, equilibrium, moment of inertia, rotational kinematics and dynamics, rolling'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- 6.1 Introduction
d.sec('6.1-rigid-body-motion')
d.basic('What is a rigid body?', 'A body whose shape never changes: the ' + T('distance between every pair of particles') + ' stays fixed. No real body is perfectly rigid')
d.basic('What is pure translation?', 'Every particle of the body has the ' + T('same velocity') + ' at any instant', **fig('fig_6_1_sliding'))
d.basic('Why is a rolling cylinder not in pure translation?', 'Its points have ' + T('different velocities') + '; the contact point is momentarily at rest', **fig('fig_6_2_rolling'))
d.basic('In rotation about a fixed axis, how does each particle move?', 'In a ' + T('circle') + ' in a plane ⟂ to the axis, centred on the axis. Points on the axis stay at rest', **fig('fig_6_4_fixed_axis'))
d.basic('What is precession? Example?', 'The axis of a spinning body sweeps out a ' + T('cone') + ' about the vertical; a spinning ' + E('top') + ' (only its tip is fixed)', **fig('fig_6_5a_top'))
d.basic('Motion of a rigid body that is pivoted vs not pivoted?', T('Pivoted/fixed') + ': rotation only. ' + T('Free') + ': pure translation, or translation + rotation')

# ---------------------------------------------------------------- 6.2 Centre of mass
d.sec('6.2-centre-of-mass')
d.basic('Centre of mass of two particles on the x-axis?', r'\( X = \dfrac{m_1x_1 + m_2x_2}{m_1 + m_2} \)' + ': a mass-weighted mean; midway if masses are equal')
d.basic('Centre of mass of n particles (vector form)?', r'\( \vec R = \dfrac{\sum m_i \vec r_i}{M} \)' + ', M = total mass')
d.basic('CM of a continuous body?', r'\( \vec R = \dfrac{1}{M}\int \vec r\,dm \)' + '; if the origin is at the CM, ∫r dm = 0')
d.basic('CM of three equal masses at the corners of a triangle?', 'At the ' + T('centroid') + ' of the triangle')
d.basic('Where is the CM of a uniform rod, ring, disc, sphere, cube?', 'At the ' + T('geometric centre') + ', by reflection symmetry')
d.basic('Must the CM lie inside the body? (Exercise 6.1)', X('No') + ': e.g. a ' + E('ring, hollow sphere, hollow cylinder') + ' have their CM in empty space')
d.basic('Example 6.1: 100 g, 150 g, 200 g at the corners of an equilateral triangle of side 0.5 m (100 g at origin, 150 g at (0.5, 0)). CM?', 'X = ' + N('5/18 m') + ', Y = ' + N('1/(3√3) m') + ' — not the geometric centre, as the masses differ', **fig('fig_6_9_triangle'))
d.basic('Example 6.2: CM of a triangular lamina?', 'At the ' + T('centroid') + ': each strip parallel to a side has its CM on the median, so the CM lies on all three medians', **fig('fig_6_10_lamina'))
d.basic('Example 6.3: uniform L-shaped lamina of three 1 m squares (3 kg). CM?', N('(5/6 m, 5/6 m)') + ': on the line of symmetry OD', **fig('fig_6_11_l_lamina'))
d.basic('Exercise 6.2: HCl, bond 1.27 Å, Cl is 35.5 × H. Location of the CM?', N('1.24 Å') + ' from the H nucleus (very close to Cl)')
d.basic('Teacher addition: CM of a uniform semicircular ring and disc (radius R) from the centre?', 'Ring: ' + r'\( \dfrac{2R}{\pi} \)' + '; disc: ' + r'\( \dfrac{4R}{3\pi} \)')
d.basic('Exercise 6.15: a hole of radius R/2 is cut from a disc of radius R, centred R/2 from the centre. CM of the rest?', N('R/6') + ' from the centre, on the side ' + T('opposite') + ' the hole (treat the hole as negative mass)')

# ---------------------------------------------------------------- 6.3-6.4 Motion of CM, momentum
d.sec('6.3-motion-of-centre-of-mass')
d.basic('Equation of motion of the centre of mass?', r'\( M\vec A = \vec F_{ext} \)' + ': the CM moves as if all mass were there and all ' + T('external') + ' forces acted there')
d.basic('Why do internal forces not affect the CM?', 'By the third law they come in ' + T('equal and opposite pairs') + ' and cancel in the sum')
sp.explosion_cm(d)
d.basic('Total momentum of a system and the CM velocity?', r'\( \vec P = M\vec V \)' + ' ; ' + r'\( \dfrac{d\vec P}{dt} = \vec F_{ext} \)' + ' (second law for a system)')
d.basic('If the net external force is zero?', 'Total momentum is ' + T('conserved') + ' and the CM moves with ' + T('constant velocity'))
d.basic('Radium nucleus decays into radon + α. Seen from the CM frame?', 'The two products fly apart ' + T('back to back') + '; the CM stays at rest (or keeps moving uniformly in the lab)', **fig('fig_6_13_decay'))
d.basic('Binary stars: what do their paths look like in the CM frame?', T('Circles') + ' about the CM, diametrically opposite; in the lab, circles + uniform drift of the CM', **fig('fig_6_14_binary'))
d.basic('Exercise 6.3: a child runs about on a trolley moving at V on a smooth floor. Speed of the CM of (trolley + child)?', T('Still V') + ': the running forces are internal')
d.basic('Useful split of kinetic energy of a system (Points to ponder)?', r"\( K = K' + \tfrac12 MV^2 \)" + ' : KE about the CM + KE of the CM')

# ---------------------------------------------------------------- 6.5 Vector product
d.sec('6.5-vector-product')
d.basic('Define the vector (cross) product a × b.', 'Magnitude ' + r'\( ab\sin\theta \)' + '<br>Direction ⟂ to both a and b by the ' + T('right-hand rule') + ' (curl fingers from a to b; thumb gives c)', **fig('fig_6_15_screw_rule'))
d.basic('Is the cross product commutative?', X('No') + ': ' + r'\( \vec b \times \vec a = -\vec a \times \vec b \)')
d.basic('a × a = ?', 'The ' + T('null vector') + ' (sin 0 = 0)')
d.cloze('î × ĵ = {{c1::k̂}}, ĵ × k̂ = {{c2::î}}, k̂ × î = {{c3::ĵ}}; in reverse order the sign is negative.')
d.basic('Mnemonic for unit-vector cross products?', 'Write ' + T('i → j → k → i') + ' in a circle: going clockwise gives +, anticlockwise gives −')
d.basic('a × b in components?', 'Determinant with rows (î ĵ k̂), (aₓ aᵧ a𝓏), (bₓ bᵧ b𝓏)')
d.basic('Example 6.4: a = 3î − 4ĵ + 5k̂, b = −2î + ĵ − 3k̂. a·b and a × b?', 'a·b = ' + N('−25') + '; a × b = ' + N('7î − ĵ − 5k̂'))
d.basic('Does a × b change sign under reflection?', X('No') + ': both a and b flip sign, so a × b does not (it is an axial vector)')
d.basic('Exercise 6.4: area of the triangle formed by a and b?', r'\( \tfrac12 |\vec a \times \vec b| \)')
d.basic('Exercise 6.5: what does a·(b × c) represent?', 'The ' + T('volume') + ' of the parallelepiped on a, b, c')

# ---------------------------------------------------------------- 6.6 Angular velocity
d.sec('6.6-angular-velocity')
d.basic('Relation between linear and angular velocity (vector form)?', r'\( \vec v = \vec\omega \times \vec r \)' + ' ; magnitude ' + r'\( v = \omega r_\perp \)', **fig('fig_6_17b_v_omega_r'))
d.basic('Direction of the angular velocity vector?', 'Along the ' + T('axis') + ', the way a right-handed screw turning with the body would advance', **fig('fig_6_17a_omega'))
d.basic('What characterises pure rotation about a fixed axis?', 'Every particle has the ' + T('same angular velocity') + ' (but different linear speeds, ∝ distance from the axis)')
d.basic('Define angular acceleration.', r'\( \vec\alpha = \dfrac{d\vec\omega}{dt} \)' + '; for a fixed axis, α = dω/dt (scalar)')

# ---------------------------------------------------------------- 6.7 Torque and angular momentum
d.sec('6.7-torque')
d.basic('Why does pushing a door at the hinge not open it?', 'Rotation depends on ' + T('where and how') + ' the force acts, not the force alone: at the hinge the lever arm is zero')
d.basic('Define torque (moment of force).', r'\( \vec\tau = \vec r \times \vec F \)' + '; ' + r'\( \tau = rF\sin\theta = r_\perp F \)', **fig('drawn_torque_lever_arm'))
d.basic('Unit and dimensions of torque; is it the same as work?', T('N m') + ', [M L² T⁻²] like work, but torque is a ' + T('vector') + ' and is never called joule')
d.basic('When is the torque of a force zero?', 'F = 0, r = 0, or the ' + T('line of action passes through the origin') + ' (θ = 0° or 180°)', **fig('fig_6_18_torque'))
d.basic('Example 6.5: τ of F = 7î + 3ĵ − 5k̂ acting at r = î − ĵ + k̂?', N('2î + 12ĵ + 10k̂'))
d.basic('Define the angular momentum of a particle.', r'\( \vec l = \vec r \times \vec p \)' + ' ; ' + r'\( l = rp\sin\theta = r_\perp p \)')
d.basic('Relation between torque and angular momentum?', r'\( \dfrac{d\vec l}{dt} = \vec\tau \)' + ': the rotational analogue of F = dp/dt')
d.basic('For a system, which torques change L?', 'Only ' + T('external') + ' torques: ' + r'\( \dfrac{d\vec L}{dt} = \vec\tau_{ext} \)' + ' (internal forces along the joining lines cancel)')
d.basic('State conservation of angular momentum.', 'If ' + r'\( \vec\tau_{ext} = 0 \)' + ', ' + T('L is constant') + ' (each component separately)')
d.basic('Example 6.6: angular momentum of a particle moving with constant velocity, about any point?', T('Constant') + ': r sin θ (perpendicular distance of the line of motion) and p stay fixed; no torque acts', **fig('fig_6_19_const_velocity'))
d.basic('Exercise 6.6: components of l = r × p?', r'\( l_x = yp_z - zp_y,\ l_y = zp_x - xp_z,\ l_z = xp_y - yp_x \)' + '; motion in the x-y plane gives only l𝓏')
d.basic('Bicycle-rim experiment: spinning rim held by one string. What happens?', 'Instead of falling, its axis (angular momentum) ' + T('precesses') + ' about the string')

# ---------------------------------------------------------------- 6.8 Equilibrium
d.sec('6.8-equilibrium')
d.basic('Conditions for mechanical equilibrium of a rigid body?', T('Translational') + ': ΣF = 0. ' + T('Rotational') + ': Στ = 0')
d.basic('How many conditions for coplanar forces?', N('Three') + ': two force components and one torque component (⟂ to the plane)')
d.basic('Equal parallel forces, same direction, at the ends of a light rod?', T('Rotational') + ' equilibrium but ' + X('not translational'), **fig('fig_6_20a_parallel_forces'))
d.basic('What is a couple? Effect?', 'Two equal and opposite forces with different lines of action: ' + T('rotation without translation'), **fig('fig_6_20b_couple'))
d.basic('Two examples of a couple?', 'Fingers turning a ' + E('bottle lid') + '; Earth’s field on a ' + E('compass needle'), **fig('fig_6_21b_compass'))
d.basic('Example 6.7: does the moment of a couple depend on the reference point?', X('No') + ': moment = AB × F for any origin')
d.basic('When is total torque independent of the origin?', 'When the ' + T('total external force is zero'))
d.basic('Principle of moments for a lever?', r'\( d_1F_1 = d_2F_2 \)' + ': load arm × load = effort arm × effort', **fig('fig_6_23_lever'))
d.basic('Mechanical advantage of a lever?', r'\( MA = \dfrac{F_1}{F_2} = \dfrac{d_2}{d_1} \)' + '; > 1 when the effort arm is longer than the load arm')
d.basic('Define the centre of gravity.', 'The point about which the ' + T('total gravitational torque') + ' on the body is zero', **fig('fig_6_24_balance'))
d.basic('When do the centre of gravity and centre of mass coincide?', 'When ' + T('g is uniform') + ' over the body. For a very tall body (g varies) they differ')
d.basic('How to find the CG of an irregular lamina by suspension?', 'Hang it from two or three points; the ' + T('verticals') + ' through the suspension points meet at the CG', **fig('fig_6_25_suspension'))
steps_card(d, 'Example 6.8 · knife edges', 'Find the missing step.', '70 cm, 4.00 kg bar on knife edges 10 cm from each end; 6.00 kg hung 30 cm from end A. Reactions?',
           ['R₁ + R₂ = 10.00g = 98.0 N', 'Moments about G: −0.25R₁ + 0.05 × 6g + 0.25R₂ = 0', 'R₁ − R₂ = 1.2g = 11.76 N', '<b>R₁ ≈ 55 N, R₂ ≈ 43 N</b>'], 1,
           'Bar on two knife edges: reactions', 'R₁ + R₂ = 98 N and R₁ − R₂ = 11.76 N give R₁ ≈ 55 N, R₂ ≈ 43 N', )
d.basic('Example 6.8: why take moments about G?', 'The rod’s own weight then has ' + T('zero moment') + ', removing one unknown term', **fig('fig_6_26_bar'))
d.basic('Example 6.9: 3 m, 20 kg ladder on a frictionless wall, foot 1 m out. Reactions?', 'Wall F₁ = ' + N('34.6 N') + '; floor: N = ' + N('196 N') + ', friction 34.6 N, total ≈ ' + N('199 N') + ' at ≈ 80° to the horizontal', **fig('fig_6_27_ladder'))
d.basic('Exercise 6.9: 1800 kg car, axles 1.8 m apart, CG 1.05 m behind the front axle. Force on each front and back wheel?', 'Front ' + N('3675 N') + ' each; back ' + N('5145 N') + ' each')
d.basic('Exercise 6.16: two 5 g coins at the 12.0 cm mark shift the balance point of a metre stick to 45.0 cm. Mass of the stick?', N('66.0 g') + ' (10 g × 33 cm = m × 5 cm)')
d.basic('Exercise 6.8: bar hung by strings at 36.9° and 53.1° to the vertical, length 2 m. CG from the left end?', N('72 cm'), **fig('fig_6_33_bar_strings'))

# ---------------------------------------------------------------- 6.9 Moment of inertia
d.sec('6.9-moment-of-inertia')
d.basic('Define moment of inertia.', r'\( I = \sum m_i r_i^2 \)' + ' (rᵢ = perpendicular distance from the axis); unit ' + N('kg m²'))
d.basic('Rotational kinetic energy?', r'\( K = \tfrac12 I\omega^2 \)')
d.basic('Why is I the rotational analogue of mass?', 'It measures ' + T('resistance to change') + ' in rotational motion, just as mass does for translation.<br>(Compare ½Iω² with ½mv²)')
d.basic('Does a body have a fixed moment of inertia like its mass?', X('No') + ': I depends on the ' + T('axis') + ' and on how mass is distributed about it')
d.basic('I of a pair of masses M/2 on a light rod of length l, about the perpendicular axis through the centre?', r'\( \dfrac{Ml^2}{4} \)', **fig('fig_6_28_dumbbell'))
table_card(d, 'Table 6.1 · moments of inertia', 'I about the given axis?', [
    ('Ring, ⟂ axis through centre', 'MR²', False), ('Ring, about a diameter', 'MR²/2', False),
    ('Thin rod, ⟂ axis at midpoint', 'ML²/12', False), ('Disc, ⟂ axis through centre', 'MR²/2', False),
    ('Disc, about a diameter', 'MR²/4', False)], term='Moments of inertia (Table 6.1, part 1)')
table_card(d, 'Table 6.1 · moments of inertia', 'I about the given axis?', [
    ('Hollow cylinder, own axis', 'MR²', False), ('Solid cylinder, own axis', 'MR²/2', False),
    ('Solid sphere, diameter', '2MR²/5', False), ('Teacher addition: hollow sphere, diameter', '2MR²/3', False),
    ('Teacher addition: rod about one end', 'ML²/3', False)], term='Moments of inertia (Table 6.1, part 2)')
d.basic('Identify: which shapes in Table 6.1 have the largest and smallest I for the same M and R?', 'Largest: ' + T('ring / hollow cylinder (MR²)') + '; smallest: ' + T('disc about a diameter (MR²/4)'), **img('tab_6_1_moment_of_inertia'))
d.basic('Mnemonic: why does a ring have more I than a disc of the same mass and radius?', 'All the ring’s mass sits at the ' + T('rim') + ' (distance R); the disc’s mass is spread inwards.<br>"Mass far out, spin hard to start"')
d.basic('Define radius of gyration.', r'\( I = Mk^2 \)' + ': k is the distance at which the whole mass, as a point, would give the same I')
d.basic('Radius of gyration of a rod (⟂ axis at centre) and a disc (about a diameter)?', r'\( k = \dfrac{L}{\sqrt{12}} \)' + ' and ' + r'\( k = \dfrac{R}{2} \)')
d.basic('What is a flywheel and why is it used?', 'A disc with ' + T('large I') + ' in engines; it resists sudden changes of speed, giving smooth motion', **fig('fig_6_31_flywheel'))
d.basic('Teacher addition (not in rationalised NCERT, needed for JEE): parallel axis theorem?', r'\( I = I_{cm} + Md^2 \)' + ' for a parallel axis at distance d from the axis through the CM', **fig('drawn_axis_theorems'))
d.basic('Teacher addition: perpendicular axis theorem?', r'\( I_z = I_x + I_y \)' + ' for a ' + T('plane lamina') + ' (x, y in its plane, z ⟂ through the same point)', **fig('drawn_axis_theorems'))
d.basic('Teacher addition: I of a disc about a tangent in its plane?', r'\( \tfrac14 MR^2 + MR^2 = \tfrac54 MR^2 \)' + ' (perpendicular then parallel axis theorem)')

# ---------------------------------------------------------------- 6.10 Kinematics of rotation
d.sec('6.10-rotational-kinematics')
d.cloze('Equations of rotational motion with constant α: {{c1::ω = ω₀ + αt}},  {{c2::θ = θ₀ + ω₀t + ½αt²}},  {{c3::ω² = ω₀² + 2α(θ − θ₀)}}.')
d.basic('How many degrees of freedom does rotation about a fixed axis have?', N('One') + ' (the angle θ), like motion along a line')
steps_card(d, 'Example 6.11 · motor wheel', 'Find the missing step.', 'A motor goes from 1200 rpm to 3120 rpm in 16 s (uniform). α and revolutions?',
           ['ω₀ = 2π × 1200/60 = 40π rad/s; ω = 104π rad/s', 'α = (104π − 40π)/16 = 4π rad/s²', 'θ = 40π × 16 + ½ × 4π × 16² = 1152π rad', '<b>576 revolutions</b>'], 2,
           'Motor wheel: angular acceleration and revolutions', 'α = 4π rad/s²; θ = 1152π rad = 576 revolutions')
d.basic('Trap: converting rpm to rad/s?', 'Multiply by ' + N('2π/60') + ': 1200 rpm = 20 rev/s = 40π rad/s')

# ---------------------------------------------------------------- 6.11 Dynamics
d.sec('6.11-rotational-dynamics')
d.basic('Which forces matter for rotation about a fixed axis?', 'Only components in planes ⟂ to the axis, with position vectors ⟂ to the axis.<br>The rest are cancelled by the ' + T('constraint forces') + ' of the bearings')
d.basic('Work and power of a torque?', r'\( dW = \tau\,d\theta,\quad P = \tau\omega \)')
d.basic('Newton’s second law for rotation about a fixed axis?', r'\( \tau = I\alpha \)')
table_card(d, 'Table 6.2 · linear vs rotational', 'Rotational analogue?', [
    ('Mass M', 'moment of inertia I', False), ('Force F = Ma', 'torque τ = Iα', False), ('Work F ds', 'τ dθ', False),
    ('KE ½Mv²', '½Iω²', False), ('Power Fv', 'τω', False), ('Momentum Mv', 'L = Iω', False)], term='Translational and rotational analogues (Table 6.2)')
steps_card(d, 'Example 6.12 · flywheel', 'Find the missing step.', '25 N pull on a cord round a 20 kg, 20 cm radius flywheel (disc) from rest. α, work and KE after 2 m of cord?',
           ['τ = FR = 25 × 0.2 = 5 N m; I = ½MR² = 0.4 kg m²', 'α = τ/I = 12.5 rad/s²', 'W = F × 2 m = 50 J; θ = 2/0.2 = 10 rad', 'ω² = 2αθ = 250 → KE = ½Iω² = <b>50 J</b> = W'], 1,
           'Flywheel pulled by a cord', 'α = 5/0.4 = 12.5 rad/s²; work 50 J = rotational KE gained (no friction)')
d.basic('Exercise 6.10: equal torques on a hollow cylinder and a solid sphere (same M, R). Which spins faster after a time?', 'The ' + T('sphere') + ': smaller I (2MR²/5 < MR²), so larger α')
d.basic('Exercise 6.13: 30 N pulls a rope on a 3 kg hollow cylinder of radius 40 cm. α and linear acceleration of the rope?', 'α = 30 × 0.4 / (3 × 0.16) = ' + N('25 rad/s²') + '; a = αR = ' + N('10 m/s²'))
d.basic('Exercise 6.14: torque 180 N m at 200 rad/s. Power?', 'P = τω = ' + N('36 kW'))
d.basic('Exercise 6.11: solid cylinder 20 kg, R = 0.25 m, ω = 100 rad/s. KE and L?', 'I = 0.625 kg m²; KE = ' + N('3125 J') + ', L = ' + N('62.5 J s'))

# ---------------------------------------------------------------- 6.12 Angular momentum, fixed axis
d.sec('6.12-angular-momentum-fixed-axis')
d.basic('Angular momentum about a fixed axis?', r'\( L_z = I\omega \)' + '; for bodies symmetric about the axis, L = Iω along the axis')
d.basic('Are l and ω always parallel?', X('No') + ': for a single particle or an unsymmetric body, L is not along the axis; only for a symmetric body is L = Iω')
d.basic('Law for fixed-axis rotation with changing I?', r'\( \dfrac{d(I\omega)}{dt} = \tau \)' + '; with τ = 0: ' + T('Iω = constant'))
sp.spinning_arms(d)
d.basic('Why do divers and acrobats curl up in mid-air?', 'Curling up ' + T('reduces I') + ', so ω rises (L conserved) and they complete more somersaults', **fig('fig_6_32b_acrobat'))
d.basic('Swivel-chair demonstration?', 'Stretching the arms ' + T('slows') + ' the spin, pulling them in ' + T('speeds it up') + ' (Iω constant)', **fig('fig_6_32a_swivel'))
d.basic('Exercise 6.12: a child on a turntable at 40 rpm reduces I to 2/5. New speed and KE?', N('100 rpm') + '; KE becomes ' + N('2.5×') + ': the child’s ' + T('internal energy') + ' does the work')
d.basic('Exercise 6.17: O₂ molecule, I = 1.94 × 10⁻⁴⁶ kg m², m = 5.30 × 10⁻²⁶ kg, v = 500 m/s, rotational KE = ⅔ translational KE. ω?', N('6.75 × 10¹² rad/s'))

# ---------------------------------------------------------------- Rolling (teacher addition)
d.sec('rolling-motion-teacher-addition')
d.basic('Teacher addition (dropped from rationalised NCERT, still in JEE): condition for rolling without slipping?', r'\( v_{cm} = R\omega \)' + ': the contact point is instantaneously at rest')
sp.rolling_wheel(d)
d.basic('Speeds of the top point, centre and contact point of a rolling wheel?', N('2v') + ', ' + N('v') + ', ' + N('0'), **fig('drawn_rolling_velocities'))
d.basic('Kinetic energy of a rolling body?', r'\( K = \tfrac12 mv^2 + \tfrac12 I\omega^2 = \tfrac12 mv^2\left(1 + \dfrac{k^2}{R^2}\right) \)')
d.basic('Acceleration of a body rolling down an incline of angle θ?', r'\( a = \dfrac{g\sin\theta}{1 + k^2/R^2} \)')
table_card(d, 'Teacher addition · rolling race', 'k²/R² and order down an incline?', [
    ('Solid sphere', '2/5 — fastest', False), ('Solid cylinder / disc', '1/2 — second', False),
    ('Hollow sphere', '2/3 — third', False), ('Ring / hollow cylinder', '1 — slowest', True)],
    note='Smaller k²/R² → less energy locked in rotation → faster. Mass and radius do not matter.', term='Which rolls down an incline first?')

# ---------------------------------------------------------------- Summary
d.sec('summary')
table_card(d, 'Points to ponder', 'True or false?', [
    ('Internal forces can change the CM motion', 'False', True), ('Zero net force ⇒ zero net torque', 'False (couple)', True),
    ('CG = CM always', 'False (only in uniform g)', True), ('To prove dL/dt = τext you need the third law with central forces', 'True', False),
    ('Torque about any origin is the same if net force is zero', 'True', False)], term='Chapter 6 concept checks')

print(d.write(os.path.join(OUT, 'deck.json')), 'cards')
