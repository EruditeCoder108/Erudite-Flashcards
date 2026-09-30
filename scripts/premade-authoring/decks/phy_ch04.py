import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase_phy as sp

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Physics', 'class11-physics-ch04-laws-of-motion')
d = Deck('Chapter 4: Laws of Motion', 'Class 11', ['class-11', 'physics', 'ch-4'])
d.description = 'Inertia, Newton’s three laws, momentum, impulse, equilibrium, friction, banking, free-body diagrams, lifts and pulleys'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- 4.1-4.3 Aristotle, Galileo, inertia
d.sec('4.2-aristotle')
d.basic('Aristotle’s law of motion?', 'An external force is needed to ' + X('keep') + ' a body moving (e.g. air behind an arrow "pushes" it)')
d.basic('What was the flaw in Aristotle’s argument?', 'He ignored ' + T('friction') + '.<br>A toy car stops because the floor’s friction opposes it.<br>The pull only cancels friction, so the net force in uniform motion is zero')
d.basic('Is a force needed to keep a body in uniform motion if there is no friction?', X('No') + ': a force is needed only to change the motion, or in practice to cancel friction')

d.sec('4.3-law-of-inertia')
d.basic('Galileo’s single inclined planes: what happens to a ball moving (i) down, (ii) up, (iii) along a smooth horizontal plane?',
        '(i) ' + T('accelerates') + ', (ii) ' + T('retards') + ', (iii) neither: ' + T('constant velocity'), **fig('fig_4_1a_galileo_planes'))
d.basic('Galileo’s double inclined plane: what happens as the second slope is made flatter?', 'The ball still rises to the ' + T('same height') + ' but travels farther; on a horizontal plane it would move ' + T('forever'), **fig('fig_4_1b_double_incline'))
d.basic('Galileo’s key insight?', 'The state of ' + T('rest') + ' and of ' + T('uniform linear motion') + ' are equivalent: in both the net force is zero')
d.cloze('Inertia means {{c1::resistance to change}}: a body does not change its state of rest or uniform motion unless an {{c2::external force}} compels it.')
d.basic('What is the measure of inertia (of translation)?', T('Mass') + ': a larger mass needs a larger force for the same change in velocity')
d.basic('Ancient Indian ideas on motion: which concept came closest to inertia?', T('Vega') + ' (Vaisesika theory): the tendency to move in a straight line, opposed by contact with objects and the air')
d.basic('Who introduced "instantaneous motion" (tatkaliki gati), anticipating instantaneous velocity?', T('Bhaskara') + ' (' + N('1150 A.D.') + ')')

# ---------------------------------------------------------------- 4.4 First law
d.sec('4.4-first-law')
d.cloze('Newton’s first law: every body continues in its state of {{c1::rest or of uniform motion in a straight line}} unless compelled by some {{c2::external force}} to act otherwise.')
d.basic('First law in one line?', 'If the net external force is ' + N('zero') + ', the acceleration is ' + N('zero') + ' (and vice versa)')
d.basic('A spaceship in interstellar space has all rockets off. What is its motion?', 'Zero net force → zero acceleration: it moves with ' + T('uniform velocity') + ' (or stays at rest)')
d.basic('A book rests on a table. Which statement is the correct reasoning: "W = R, so the book is at rest", or "the book is at rest, so R = W"?',
        T('The book is at rest, so the net force is zero, so R = W') + '<br>We infer the force from the observed state; R is self-adjusting', **fig('fig_4_15_fbd'))
d.basic('A car speeds up from rest. Which external force accelerates it?', T('Friction') + ' from the road on the tyres. ' + X('Internal forces') + ' (engine, pistons) cannot accelerate the car as a whole')
d.basic('A bus starts suddenly. Why are standing passengers thrown backward?', 'Friction carries the ' + T('feet') + ' forward with the bus; the upper body stays behind by ' + T('inertia') + ' (the body is not rigid)')
d.basic('A speeding bus stops suddenly. Why are passengers thrown forward? (Exercise 4.23 b)', 'Friction stops the feet with the bus; the upper body ' + T('keeps moving') + ' by inertia')
d.basic('Example 4.1: an astronaut slips out of a spaceship accelerating at 100 m/s² in deep space. His acceleration just after?', N('Zero') + ': once outside, no force acts on him (no stars nearby; the ship’s gravity is negligible)')
d.basic('Intuition: why does a tablecloth jerked fast leave the dishes in place?', 'The friction acts for a ' + T('very short time') + ', so it gives the dishes only a tiny momentum.<br>Their inertia keeps them almost at rest')

# ---------------------------------------------------------------- 4.5 Second law, momentum
d.sec('4.5-second-law')
d.basic('Define momentum.', r'\( \vec p = m\vec v \)' + ': a ' + T('vector') + ' along the velocity; SI unit ' + N('kg m s⁻¹'))
d.basic('Why is it easier to catch a light stone than a heavy one dropped from the same height?', 'Same speed, but the heavy stone has more ' + T('momentum') + ', so a larger force is needed to stop it in the same time')
d.basic('Why does a cricketer draw the hands back while catching? (Exercise 4.23 d)', 'He ' + T('increases the time') + ' over which the ball stops. Same Δp in a longer time → ' + T('smaller force') + ' on the hands', **fig('fig_4_3_catch'))
d.basic('The same force acts for the same time on a light and a heavy body at rest. What is the same for both afterwards?', 'The ' + T('momentum') + ' gained (the lighter one moves faster)')
d.basic('A stone is whirled in a horizontal circle at constant speed. Is a force needed?', T('Yes') + ': the magnitude of p is constant but its ' + T('direction') + ' changes; the string supplies the force', **fig('fig_4_4_stone_string'))
d.cloze('Newton’s second law: the rate of change of momentum of a body is {{c1::directly proportional to the applied force}} and takes place {{c2::in the direction in which the force acts}}.')
d.basic('Second law as an equation?', r'\( \vec F = \dfrac{d\vec p}{dt} = m\vec a \)' + ' (fixed mass), with the constant k chosen as 1')
d.basic('Define one newton.', N('1 N = 1 kg m s⁻²') + ': the force that gives a 1 kg mass an acceleration of 1 m s⁻²')
d.basic('Is the second law consistent with the first law?', T('Yes') + ': F = 0 gives a = 0')
d.basic('Second law is a vector law. What does that mean in practice?', 'Three separate equations: ' + r'\( F_x = ma_x,\ F_y = ma_y,\ F_z = ma_z \)' + '. A force changes only the velocity component ' + T('along itself'))
d.basic('Why does a projectile keep its horizontal velocity?', 'Gravity is vertical; the component of velocity ' + T('normal to the force') + ' is unchanged')
d.basic('To a system of particles, what do F and a mean in F = ma?', 'F = total ' + T('external') + ' force (internal forces excluded); a = acceleration of the ' + T('centre of mass'))
d.basic('What does "the second law is a local relation" mean?', 'Force ' + T('here and now') + ' decides acceleration here and now; a does ' + X('not') + ' depend on the history of motion')
sp.train_drop(d)
d.basic('Example 4.2: a 0.04 kg bullet at 90 m/s stops in 60 cm of wood. Average resistive force?', 'a = −90²/(2 × 0.6) = −6750 m/s² → F = 0.04 × 6750 = ' + N('270 N') + ' (average; the real force need not be uniform)')
d.basic('Example 4.3: y = ut + ½gt². Force on the particle?', 'a = d²y/dt² = g → ' + T('F = mg') + ': motion under gravity with y along g')
d.basic('Trap: is "ma" a force acting on the body?', X('No') + '.<br>F is the net force from external agencies; ma is its ' + T('effect') + '.<br>Never draw ma on a free-body diagram as an extra force')
d.basic('Trap: a ball thrown up is momentarily at rest at the top. Is the force on it zero there?', X('No') + ': v = 0 but the force is still ' + T('mg') + ' and a = g (Points to ponder 2)')
d.basic('Is force always along the velocity?', X('No') + ': it can be along, opposite, perpendicular or at any angle to v, but it is always along the ' + T('acceleration'))

# ---------------------------------------------------------------- Impulse
d.sec('4.5-impulse')
d.basic('Define impulse.', 'Impulse = ' + T('force × time') + ' = ' + T('change in momentum') + '; unit ' + N('N s = kg m s⁻¹'))
d.basic('What is an impulsive force?', 'A ' + T('large force acting for a short time') + ' that produces a finite change in momentum (bat on ball, ball on wall). Newtonian mechanics treats it like any other force')
d.basic('Why use impulse instead of force for a bat hitting a ball?', 'The force and the contact time are hard to measure separately, but their product = Δp is easy to find')
d.basic('Impulse from a force–time graph?', T('Area under the F–t graph') + '; the average force × Δt gives the same area', **fig('drawn_impulse'))
d.basic('Example 4.4: a 0.15 kg ball at 12 m/s is hit straight back at the same speed. Impulse?', '0.15 × 12 − (−0.15 × 12) = ' + N('3.6 N s') + ', from the batsman towards the bowler')
d.basic('Trap: a ball rebounds from a wall with the same speed. Is the impulse zero because the speed is unchanged?', X('No') + ': the ' + T('velocity reverses') + ', so Δp = ' + N('2mu') + ' (momentum is a vector)')
d.basic('Exercise 4.18: two 0.05 kg billiard balls at 6 m/s collide head-on and rebound with the same speed. Impulse on each?', N('0.6 kg m s⁻¹') + ' each, in ' + T('opposite directions') + ' (0.05 × 12)')
d.basic('Exercise 4.20: a batsman deflects a 0.15 kg ball at 54 km/h through 45° without changing its speed. Impulse?', '2mv cos 22.5° = 2 × 0.15 × 15 × 0.924 ≈ ' + N('4.2 kg m s⁻¹') + ', along the ' + T('bisector') + ' of the initial and final directions')

# ---------------------------------------------------------------- 4.6 Third law
d.sec('4.6-third-law')
d.cloze('Newton’s third law: to every action, there is always {{c1::an equal and opposite reaction}}.')
d.basic('The third law in plain words (NCERT)?', 'Forces always occur in ' + T('pairs') + ': force on A by B = − force on B by A: ' + r'\( \vec F_{AB} = -\vec F_{BA} \)')
d.basic('Does action come before reaction?', X('No') + ': they act at the ' + T('same instant') + '; there is no cause and effect, and either can be called the action')
d.basic('Why can action and reaction never cancel each other?', 'They act on ' + T('different bodies') + '. For one body, only one of the pair matters')
d.basic('When do action–reaction pairs add to zero?', 'When both bodies are inside the system: they are ' + T('internal forces') + ' and cancel in pairs')
d.basic('The Earth pulls a falling stone. Does the stone pull the Earth?', T('Yes') + ', with an equal and opposite force; the Earth’s huge mass makes its acceleration negligible')
d.basic('Trap: a book on a table. Are its weight and the normal force an action–reaction pair?', X('No') + ': both act on the ' + T('same body') + ' (the book). Weight pairs with the book’s pull on the Earth; the normal force pairs with the book’s push on the table')
d.basic('Example 4.12: before the floor yields, name the two action–reaction pairs for the 2 kg block.', '(i) Earth pulls the block 20 N down ↔ block pulls the Earth 20 N up. (ii) Block pushes the floor 20 N down ↔ floor pushes the block 20 N up', **fig('fig_4_15_fbd'))
d.basic('Example 4.12: a 25 kg cylinder is placed on the 2 kg block and both sink at 0.1 m/s². Force of the block on the floor?', '270 − R′ = 27 × 0.1 → R′ = ' + N('267.3 N') + ' downward (less than the weight 270 N, since they accelerate)')
d.basic('Exercise 4.23 (a): why can a horse not pull a cart and run in empty space?', 'The horse moves forward only because the ' + T('ground pushes it') + ' (friction, by the third law). In empty space there is nothing to push against, and internal forces cannot move the horse–cart system')
d.basic('How do we walk?', 'The foot pushes the ground ' + T('backward') + '.<br>Static friction from the ground pushes us ' + T('forward') + '.<br>(No friction, no walking)')
d.basic('Why is it hard to walk on ice or step out of a boat onto a bank?', 'Ice: little ' + T('friction') + ' to push you. Boat: your push sends the ' + T('boat backward') + ' (third law), so you move forward less')

# ---------------------------------------------------------------- Example 4.5
d.basic('Example 4.5: identical balls hit a wall at the same speed, (a) along the normal, (b) at 30° to it, and bounce off with the same speed. Direction of the force on the wall?',
        T('Normal to the wall') + ' in both cases: only pₓ reverses; the parallel component p_y is unchanged', **fig('fig_4_6_billiard'))
d.basic('Example 4.5: ratio of impulses on the balls, (a) : (b)?', '2mu : 2mu cos 30° = 2/√3 ≈ ' + N('1.2'))

# ---------------------------------------------------------------- 4.7 Conservation of momentum
d.sec('4.7-conservation-of-momentum')
d.cloze('Law of conservation of momentum: the total momentum of an {{c1::isolated}} system of interacting particles is {{c2::conserved}}.')
d.basic('Conservation of momentum follows from which laws?', 'The ' + T('second') + ' (F Δt = Δp) and ' + T('third') + ' (F_AB = −F_BA) laws')
d.basic('What is an isolated system?', 'One with ' + T('no net external force') + ' on it')
d.basic('A gun fires a bullet. How are their momenta related?', r'\( \vec p_{gun} = -\vec p_{bullet} \)' + ': total momentum stays ' + N('zero') + ' (the gun recoils)')
d.basic('Exercise 4.19: a 0.020 kg shell leaves a 100 kg gun at 80 m/s. Recoil speed?', '100 v = 0.02 × 80 → v = ' + N('0.016 m/s') + ' (1.6 cm/s)')
d.basic('Exercise 4.17: a nucleus at rest splits into two. Why must the pieces fly apart in opposite directions?', 'Total momentum is ' + N('zero') + '; two momentum vectors add to zero only if they are ' + T('equal and opposite'))
d.basic('Is momentum conserved in an inelastic collision?', T('Yes') + ': momentum is conserved in every collision; only ' + X('kinetic energy') + ' is lost in inelastic ones')
d.basic('NEET/JEE addition: why does a rocket accelerate in space with nothing to push against?', 'It pushes exhaust gas ' + T('backward') + '; the gas pushes the rocket forward. Thrust = ' + r'\( v_{rel}\,\dfrac{dm}{dt} \)' + ' (momentum conservation)')
d.basic('Exercise 4.9: a 20 000 kg rocket lifts off with a = 5.0 m/s². Initial thrust? (g = 10)', 'F − mg = ma → F = 20 000 × 15 = ' + N('3.0 × 10⁵ N'))

# ---------------------------------------------------------------- 4.8 Equilibrium
d.sec('4.8-equilibrium')
d.basic('When is a particle in equilibrium?', 'When the ' + T('net external force') + ' on it is zero: it is at rest or in uniform motion')
d.basic('Condition for equilibrium under three concurrent forces?', r'\( \vec F_1 + \vec F_2 + \vec F_3 = 0 \)' + ': the resultant of any two is equal and opposite to the third; they form a ' + T('closed triangle'), **fig('fig_4_7_force_triangle'))
d.basic('Equilibrium under n forces, graphically?', 'The forces form a ' + T('closed n-sided polygon') + ' with arrows in the same sense')
d.basic('Equilibrium in components?', r'\( \sum F_x = 0,\ \sum F_y = 0,\ \sum F_z = 0 \)')
d.basic('Does zero net force guarantee full equilibrium of an extended body?', X('No') + ': it also needs zero net ' + T('torque') + ' (rotational equilibrium, Chapter 6)')
steps_card(d, 'Example 4.6 · rope pulled sideways', 'Find the missing step.', 'A 6 kg mass hangs by a rope; a 50 N horizontal force pulls the midpoint P. Angle of the upper rope with the vertical? (g = 10)',
           ['Lower rope: T₂ = mg = 60 N', 'At P, vertical: T₁ cos θ = T₂ = 60 N', 'At P, horizontal: T₁ sin θ = 50 N',
            'tan θ = 50/60 → <b>θ ≈ 40°</b>'], 3, 'Example 4.6: angle of the rope',
           'tan θ = 50/60, θ ≈ 40°; independent of the rope’s length and where the force acts')
d.basic('Example 4.6: does the answer depend on the rope’s length or where the 50 N acts?', X('No') + ': only on the two forces (60 N and 50 N)', **fig('fig_4_8_hanging_mass'))
d.basic('What is a free-body diagram?', 'A sketch of ' + T('one chosen system') + ' with all forces ' + T('on it') + ' from other bodies; forces it exerts on others are left out')
d.basic('Lami’s theorem (teacher addition)?', 'For three concurrent forces in equilibrium: ' + r'\( \dfrac{F_1}{\sin\alpha} = \dfrac{F_2}{\sin\beta} = \dfrac{F_3}{\sin\gamma} \)' + ', each angle being the one ' + T('opposite') + ' that force')

# ---------------------------------------------------------------- 4.9 Common forces
d.sec('4.9-common-forces')
d.basic('Which common force in mechanics is not a contact force?', T('Gravity') + ' (it acts at a distance, with no medium)')
d.basic('The contact force between two surfaces splits into which two components?', 'Perpendicular to the surfaces: ' + T('normal reaction') + '. Parallel to them: ' + T('friction'))
d.basic('Give contact forces from fluids.', T('Buoyant force') + ' (weight of fluid displaced), ' + T('viscous force') + ', ' + T('air resistance'))
d.basic('Spring force?', r'\( F = -kx \)' + ': proportional to the extension or compression x, opposite to it; k = force constant')
d.basic('When is the tension the same all along a string?', 'When the string is ' + T('massless') + ' (and passes over smooth pulleys only)')
d.basic('What is the fundamental origin of all contact forces (friction, normal force, tension)?', T('Electrical forces') + ' between the charged constituents (nuclei and electrons) of the bodies')
d.basic('Of the four fundamental forces, which matter in mechanics?', T('Gravitational') + ' and ' + T('electromagnetic') + '; the weak and strong forces act only inside nuclei')

# ---------------------------------------------------------------- 4.9.1 Friction
d.sec('4.9.1-friction')
d.basic('What is static friction?', 'Friction that opposes ' + T('impending') + ' relative motion between surfaces at rest relative to each other', **fig('fig_4_10_friction'))
d.basic('What is "impending motion"?', 'The motion that ' + T('would') + ' occur under the applied force if friction were absent (but does not actually occur)')
d.basic('Why is static friction called self-adjusting?', 'With no push, fₛ = ' + N('0') + '. As the push grows, fₛ grows ' + T('equal and opposite') + ' to it, up to a maximum', **fig('drawn_friction_graph'))
d.cloze('Law of static friction: {{c1::fₛ ≤ μₛN}}, where the maximum {{c2::(fₛ)ₘₐₓ = μₛN}} is independent of the area of contact.')
d.cloze('Kinetic friction: {{c1::fₖ = μₖN}}; it is independent of the area of contact and nearly independent of {{c2::velocity}}.')
d.basic('Which is larger, μₛ or μₖ?', T('μₛ > μₖ') + ': it is harder to start a body sliding than to keep it sliding')
d.basic('On what do μₛ and μₖ depend?', 'Only on the ' + T('nature of the two surfaces') + ' in contact; ' + X('not') + ' on the area of contact')
d.basic('Are the laws of friction fundamental laws?', X('No') + ': they are ' + T('empirical') + ' and only approximately true, but very useful')
d.basic('A body slides with an applied force F. Acceleration? And after F is removed?', r'\( a = \dfrac{F - f_k}{m} \)' + '; after removal a = −fₖ/m and it stops. Constant velocity means F = fₖ')
d.basic('Trap: when may you put fₛ = μₛN?', 'Only when the body is ' + T('just about to slip') + ' (limiting friction). Otherwise fₛ is whatever keeps the body at rest (Points to ponder 6)')
d.basic('Friction opposes motion or relative motion?', T('Relative motion') + '. A box on an accelerating train floor is carried forward ' + T('by') + ' static friction')
d.basic('Example 4.7: μₛ = 0.15 between a box and a train floor. Maximum acceleration of the train so the box stays put?', 'ma = fₛ ≤ μₛmg → aₘₐₓ = μₛg = ' + N('1.5 m/s²'))
d.basic('Exercise 4.3(d): a 0.1 kg stone lies at rest on the floor of a train accelerating at 1 m/s². Net force on it?', N('0.1 N') + ' horizontal, along the train’s acceleration (supplied by static friction)')
d.basic('Example 4.8: a block starts to slide when the plane is tilted to 15°. μₛ?', 'tan θₘₐₓ = μₛ → μₛ = tan 15° = ' + N('0.27'), **fig('fig_4_11_incline'))
d.basic('Why is the angle of repose (θₘₐₓ = tan⁻¹ μₛ) independent of mass?', 'Both mg sin θ (down the slope) and μₛmg cos θ (friction) are proportional to ' + T('m') + ', so m cancels')
d.basic('NEET/JEE addition: acceleration of a block sliding down a rough incline?', r'\( a = g(\sin\theta - \mu_k\cos\theta) \)' + '; on a smooth incline ' + r'\( a = g\sin\theta \)')
d.basic('NEET/JEE addition: a block is pushed up a rough incline. Retardation?', r'\( a = g(\sin\theta + \mu_k\cos\theta) \)' + ': gravity and friction both act down the slope')
steps_card(d, 'Example 4.9 · block and trolley', 'Find the missing step.', 'A 3 kg block hangs from a string over a smooth pulley and pulls a 20 kg trolley; μₖ = 0.04 (g = 10). Acceleration and tension?',
           ['Block: 30 − T = 3a', 'Trolley: T − fₖ = 20a, with fₖ = μₖN = 0.04 × 200 = 8 N', 'Add: 30 − 8 = 23a',
            '<b>a = 22/23 ≈ 0.96 m/s²</b>, T = 30 − 3a ≈ 27.1 N'], 2, 'Example 4.9: block and trolley',
           'a = 22/23 ≈ 0.96 m/s², T ≈ 27.1 N', )
d.basic('Example 4.9 shortcut: acceleration of a connected system?', 'a = (net driving force) ÷ (' + T('total mass') + ') = (30 − 8)/23; then one body’s own equation gives T', **fig('fig_4_12_block_trolley'))
d.basic('Exercise 4.23 (c): why is it easier to pull a lawn mower than to push it?', 'Pulling at an angle ' + T('lifts') + ' it (N = mg − F sin θ) → less friction. Pushing ' + T('presses it down') + ' (N = mg + F sin θ) → more friction', **fig('drawn_mower'))
d.basic('NEET/JEE addition: at what angle should you pull a block to need the least force on a rough floor?', 'At ' + r'\( \tan\phi = \mu \)' + ' above the horizontal; then ' + r'\( F_{min} = \dfrac{\mu mg}{\sqrt{1+\mu^2}} \)')
d.basic('NEET/JEE addition: block A on block B, only B is pulled; μₛ between them. Largest common acceleration?', r'\( a_{max} = \mu_s g \)' + ' (the only horizontal force on A is friction from B, at most μₛm_A g)')

d.sec('4.9.1-rolling-friction')
d.basic('Why should an ideal ball rolling without slipping feel no friction?', 'The contact point is ' + T('momentarily at rest') + ' relative to the surface, so there is no relative motion to oppose')
d.basic('Why does rolling friction arise in practice?', 'The surfaces ' + T('deform') + ' slightly, so contact is over a small area, not a point')
d.basic('How does rolling friction compare with sliding friction?', 'Much smaller: by ' + N('2 to 3 orders of magnitude') + ' for the same weight (hence the importance of the wheel)')
d.basic('Two ways of reducing friction in machines (Fig. 4.13)?', T('Ball bearings') + ' (rolling instead of sliding) and a ' + T('cushion of compressed air') + '; also ' + T('lubricants'), **fig('fig_4_13_bearings'))
d.basic('Where is friction essential?', T('Walking') + ', ' + T('brakes') + ', and ' + T('tyres') + ' accelerating a car (a car cannot move on a very slippery road)')

# ---------------------------------------------------------------- 4.10 Circular motion
d.sec('4.10-circular-motion')
d.basic('Centripetal force?', r'\( f_c = \dfrac{mv^2}{R} \)' + ', directed ' + T('towards the centre'))
d.basic('Correction: NCERT 4.10 says the centripetal acceleration v²/R was seen "in Chapter 4". Where was it?', 'In ' + T('Chapter 3') + ' (Motion in a Plane); the reference is left over from the old chapter numbering')
d.basic('Trap: is centripetal force a new kind of force?', X('No') + ': it is a name for whatever real force points to the centre:<br>' + T('tension, gravity, friction, normal force') + '<br>(Points to ponder 5)')
table_card(d, '4.10 · who supplies mv²/R?', 'Which real force is the centripetal force?', [
    ('Stone whirled on a string', 'tension', False), ('Planet round the Sun', 'gravity', False),
    ('Car turning on a level road', 'static friction', False), ('Car on a smooth banked road', 'horizontal component of N', False),
    ('Electron round a nucleus (Bohr)', 'electrostatic attraction', False)], term='Sources of centripetal force')
d.basic('Car on a level curve: maximum safe speed?', r'\( v_{max} = \sqrt{\mu_s R g} \)' + ', independent of the car’s ' + T('mass'))
d.basic('Why is it static (not kinetic) friction that turns a car on a level road?', 'The tyres do not slide sideways; static friction opposes the ' + T('impending') + ' motion of the car out of the circle')
d.basic('Example 4.10: a cyclist at 18 km/h turns on a level road with R = 3 m, μₛ = 0.1. Will he slip?', T('Yes') + ': v² = 25 but μₛRg = 2.94 m²/s², so v² > μₛRg')
d.basic('Car on a banked road: equations (friction down the slope, at v_max)?', r'\( N\cos\theta = mg + f\sin\theta,\quad N\sin\theta + f\cos\theta = \dfrac{mv^2}{R} \)', **fig('drawn_banked_road'))
d.basic('Maximum speed on a banked road?', r'\( v_{max} = \sqrt{Rg\,\dfrac{\mu_s + \tan\theta}{1 - \mu_s\tan\theta}} \)' + ': greater than on a level road')
d.basic('Optimum speed on a banked road, and its meaning?', r'\( v_0 = \sqrt{Rg\tan\theta} \)' + ': the ' + T('horizontal component of N alone') + ' supplies mv²/R; no friction needed, least tyre wear')
d.basic('Banked road: which way does friction act if v < v₀?', T('Up the slope') + ' (the car tends to slide down and in)')
d.basic('When can a car be parked on a banked road without sliding?', 'If ' + r'\( \tan\theta \le \mu_s \)')
d.basic('Example 4.11: track R = 300 m, banked at 15°, μₛ = 0.2. Optimum and maximum speeds?', 'v₀ = √(300 × 9.8 × tan 15°) = ' + N('28.1 m/s') + '; vₘₐₓ = √(2940 × 0.468/0.946) ≈ ' + N('38.1 m/s'))
d.basic('NEET/JEE addition: why are railway tracks banked (outer rail raised)?', 'So the ' + T('normal force') + ' supplies the centripetal force, saving the rails and flanges from wear; tan θ = v²/(Rg)')
d.basic('NEET/JEE addition: maximum speed over a convex bridge (hump) of radius R without losing contact?', r'\( v = \sqrt{gR} \)' + ': at that speed N = 0 at the top')
d.basic('Exercise 4.4: a particle on a smooth table circles a peg on a string of tension T. Net force towards the centre?', T('T') + ' (option i). Gravity and the normal force cancel vertically')
d.basic('Exercise 4.21: a 0.25 kg stone on a 1.5 m string makes 40 rev/min. Tension? Max speed if the string can take 200 N?', 'v = 2π × 1.5 × 40/60 = 6.28 m/s → T = mv²/r ≈ ' + N('6.6 N') + '. 200 = 0.25v²/1.5 → vₘₐₓ ≈ ' + N('35 m/s'))
d.basic('Exercise 4.22: the string breaks while a stone is whirled. Its path?', T('Tangential') + ' from the instant the string breaks (option b): no force → straight line along the velocity it had')
d.basic('Trap: on a merry-go-round you feel pushed outward. Is there an outward force?', X('No') + ': every part of you gets an ' + T('inward') + ' force.<br>The "outward push" is the feeling of the impending motion (Points to ponder 11)')

# ---------------------------------------------------------------- 4.11 Solving problems
d.sec('4.11-solving-problems')
table_card(d, '4.11 · method', 'Step?', [
    ('1', 'Sketch the assembly of bodies, links and supports', False),
    ('2', 'Choose one part as the system', False),
    ('3', 'Free-body diagram: all forces ON the system (not by it)', False),
    ('4', 'Mark known forces; treat the rest as unknowns', False),
    ('5', 'Repeat for another part, using −F by the third law', False)], term='Steps for solving mechanics problems')
d.basic('In a free-body diagram of a system of two blocks, do you draw the forces between them?', X('No') + ': they are ' + T('internal') + ' and cancel. Draw them only when each block is taken separately')
d.basic('Every force should be read as…?', '"Force ' + T('on A by B') + '": friction, normal reaction, tension, thrust, buoyancy, weight are all just forces (Points to ponder 9)')
d.basic('Trap: is mg = N for a body on a floor a consequence of the third law?', X('No') + ': it holds only if the body is in ' + T('equilibrium') + ' (e.g. not in an accelerating lift).<br>mg and N act on the same body (Points to ponder 7)')

# ---------------------------------------------------------------- Lifts, pulleys, connected bodies
d.sec('lifts-and-pulleys')
d.basic('What does a weighing scale in a lift actually read?', 'The ' + T('normal force') + ' N between you and the scale (divided by g), not your true weight', **fig('drawn_lift'))
d.basic('Apparent weight in a lift accelerating up, down, and in free fall?', 'Up: ' + r'\( m(g+a) \)' + '; down: ' + r'\( m(g-a) \)' + '; free fall: ' + N('0') + ' (weightlessness)')
table_card(d, 'Exercise 4.13', 'Scale reading for a 70 kg man (g = 10)?', [
    ('Lift going up at a uniform 10 m/s', '70 kg (a = 0)', False), ('Accelerating down at 5 m/s²', '35 kg', False),
    ('Accelerating up at 5 m/s²', '105 kg', False), ('Cable snaps: free fall', '0', True)], term='Apparent weight in a lift (Exercise 4.13)')
d.basic('Trap: a lift moves up at constant speed. Does the scale read more?', X('No') + ': uniform velocity means a = 0, so N = mg; only ' + T('acceleration') + ' changes the reading')
d.basic('Atwood machine (m₂ > m₁, light string, smooth pulley): acceleration and tension?', r'\( a = \dfrac{(m_2 - m_1)g}{m_1 + m_2},\quad T = \dfrac{2m_1m_2\,g}{m_1 + m_2} \)', **fig('drawn_atwood'))
d.basic('Exercise 4.16: 8 kg and 12 kg hang over a frictionless pulley. a and T? (g = 10)', 'a = 4 × 10/20 = ' + N('2 m/s²') + '; T = 8(10 + 2) = ' + N('96 N'))
d.basic('Exercise 4.15: 10 kg and 20 kg on a smooth floor, joined by a string; 600 N pulls one of them. Tension if the 20 kg is pulled? If the 10 kg is pulled?', 'a = 600/30 = 20 m/s² either way. Pull 20 kg: T = 10 × 20 = ' + N('200 N') + '. Pull 10 kg: T = 20 × 20 = ' + N('400 N'), **fig('drawn_connected_blocks'))
d.basic('Shortcut for the tension in a string joining bodies pulled by F on a smooth floor?', 'T = F × (mass ' + T('behind') + ' the string) / (total mass): the string only has to accelerate what trails it')
d.basic('NEET/JEE addition: a uniform rope of mass M is pulled by F on a smooth floor. Tension at a distance x from the free end (length L)?', r'\( T = F\,\dfrac{x}{L} \)' + ': a heavy rope’s tension ' + X('varies') + ' along its length')
d.basic('NEET/JEE addition: what is a pseudo force?', 'In a frame accelerating with a, add a fictitious force ' + r'\( -m\vec a \)' + ' on every body so Newton’s laws can be used there. It has ' + X('no reaction') + ' partner')
d.basic('NEET/JEE addition: a pendulum hangs in a car accelerating at a. Angle of the string with the vertical?', r'\( \tan\theta = \dfrac{a}{g} \)' + ', bob tilting ' + T('backward') + ' (opposite to a)')

# ---------------------------------------------------------------- Exercises
d.sec('exercises')
table_card(d, 'Exercise 4.1', 'Net force?', [
    ('Raindrop falling at constant speed', 'zero', False), ('10 g cork floating on water', 'zero', False),
    ('Kite held stationary', 'zero', False), ('Car at a constant 30 km/h on a rough road', 'zero', False),
    ('Fast electron far from all matter and fields', 'zero', False)], term='Net force in uniform motion or rest (Exercise 4.1)')
d.basic('Exercise 4.2: a 0.05 kg pebble is thrown up. Net force going up, coming down, and at the top? (g = 10)', N('0.5 N vertically down') + ' in all three; the same if thrown at 45° (air resistance ignored)')
d.basic('Exercise 4.3: a 0.1 kg stone is dropped from the window of a train that is (a) stationary, (b) moving at a constant 36 km/h, (c) accelerating at 1 m/s². Net force just after release?', N('1 N vertically down') + ' in all three: once released, only gravity acts')
d.basic('Exercise 4.5: a 50 N retarding force acts on a 20 kg body at 15 m/s. Time to stop?', 'a = −2.5 m/s² → t = 15/2.5 = ' + N('6.0 s'))
d.basic('Exercise 4.6: a constant force takes a 3.0 kg body from 2.0 to 3.5 m/s in 25 s, same direction. Force?', 'a = 1.5/25 = 0.06 m/s² → F = ' + N('0.18 N') + ' along the motion')
d.basic('Exercise 4.7: perpendicular forces 8 N and 6 N act on 5 kg. Acceleration?', 'Resultant ' + N('10 N') + ' → a = ' + N('2 m/s²') + ' at tan⁻¹(3/4) = 37° to the 8 N force')
d.basic('Exercise 4.8: a 400 kg three-wheeler with a 65 kg driver stops from 36 km/h in 4.0 s. Average retarding force?', 'a = 10/4 = 2.5 m/s²; F = 465 × 2.5 ≈ ' + N('1.2 × 10³ N') + ' (use the total mass)')
d.basic('Exercise 4.10: a 0.40 kg body moves north at 10 m/s; 8.0 N acts south for 30 s from t = 0 at x = 0. Position at t = −5 s, 25 s, 100 s?', 'a = −20 m/s². ' + N('−50 m') + ', ' + N('−6 km') + ', ' + N('−50 km') + ' (after 30 s it coasts at −590 m/s)')
d.basic('Exercise 4.11: a truck accelerates from rest at 2 m/s²; at t = 10 s a stone is dropped from its top (6 m). Velocity and acceleration of the stone at t = 11 s?', 'vₓ = 20 m/s (kept), v_y = 10 m/s → ' + N('22.4 m/s') + ' at tan⁻¹(½) below the horizontal; a = ' + N('10 m/s² down'))
d.basic('Exercise 4.12: a pendulum’s string is cut (a) at an extreme position, (b) at the mean position. Path?', '(a) v = 0 → falls ' + T('vertically') + '. (b) horizontal velocity → ' + T('parabola'))
d.basic('Exercise 4.14: a 4 kg particle is at rest at x = 0 until t = 0, moves uniformly to x = 3 m at t = 4 s, then stays at rest. Force in each interval? Impulses?', 'Force ' + N('zero') + ' in all three intervals (uniform motion). Impulse at t = 0: ' + N('+3 kg m s⁻¹') + '; at t = 4 s: ' + N('−3 kg m s⁻¹'))

# ---------------------------------------------------------------- Summary
d.sec('summary')
table_card(d, 'Summary', 'Formula?', [
    ('Second law', 'F = dp/dt = ma', False), ('Impulse', 'F Δt = Δp', False), ('Static friction', 'fₛ ≤ μₛN', False),
    ('Angle of repose', 'tan θ = μₛ', False), ('Level curve', 'vₘₐₓ = √(μₛRg)', False), ('Banked, no friction', 'v₀ = √(Rg tan θ)', False),
    ('Lift, a up / down', 'N = m(g ± a)', False)], term='Chapter 4 formula sheet')
table_card(d, 'Summary · third law', 'True or false?', [
    ('Action and reaction act on the same body', 'false: different bodies', True), ('Action comes before reaction', 'false: simultaneous', True),
    ('They are equal and opposite', 'true', False), ('Weight and normal force form a pair', 'false: both on one body', True)], term='Third law concept check')

print(d.write(os.path.join(OUT, 'deck.json')), 'cards')
