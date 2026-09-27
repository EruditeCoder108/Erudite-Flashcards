import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase as sc
M = 'media/'

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Physics', 'class11-physics-ch04-laws-of-motion')
d = Deck('Chapter 4: Laws of Motion', 'Class 11', ['class-11', 'physics', 'ch-4'])

# ---------------------------------------------------------------- Aristotle, Galileo, inertia
d.sec('4.2-4.3-inertia')
d.basic("What was Aristotle's mistake about motion?", 'He thought a force is needed to ' + X('keep') + ' a body in uniform motion')
d.basic('Why does a real object need a push to keep moving at constant speed?', 'Only to ' + T('cancel friction') + '. With no friction, no force is needed')
d.basic("What did Galileo's double inclined plane show?", 'A ball rises to the ' + T('same height') + ' on the other side; make that side flat and it would roll ' + T('forever'), definitionImage=M + 'fig_4_1b_double_incline.webp')
d.basic('A ball rolls (i) down, (ii) up and (iii) along a smooth plane. What happens to its speed?',
        '(i) ' + T('speeds up') + ', (ii) ' + T('slows down') + ', (iii) ' + T('stays constant') + ' (no force along the plane)',
        definitionImage=M + 'fig_4_1a_galileo_planes.webp')
d.basic('What is inertia?', "A body's resistance to any " + T('change in its state') + ' of rest or uniform motion')
d.basic('What is the measure of inertia?', T('Mass'))

# ---------------------------------------------------------------- First law
d.sec('4.4-first-law')
d.cloze("Newton's first law: every body continues in its state of {{c1::rest or uniform motion in a straight line}} unless compelled by an {{c2::external force}} to change it.")
d.basic('First law in one line?', 'Net external force ' + N('= 0') + '  ⇔  acceleration ' + N('= 0'))
d.basic('A book rests on a table. What is the correct reasoning?', 'It is at rest, so net force ' + N('= 0') + ', so the normal force ' + T('equals') + ' the weight. (Not "forces cancel, so it rests")')
d.basic('What external force accelerates a car on a road?', T('Friction') + ' from the road. Internal forces cannot accelerate the car as a whole')
d.basic('A bus starts suddenly. Which way are standing passengers thrown, and why?', T('Backward') + ': friction moves the feet with the bus while the upper body stays at rest (inertia)')
d.basic('A bus stops suddenly. Which way are passengers thrown?', T('Forward') + ' (upper body keeps moving)')
d.basic('In deep space, a stone is released from a spaceship accelerating at 1 m/s². Acceleration of the stone just after release?',
        N('0') + '. Once released, no force acts on it')

# ---------------------------------------------------------------- Second law
d.sec('4.5-second-law')
d.basic('Define momentum.', r'\(\vec p = m\vec v\)' + ', a ' + T('vector'))
d.basic('Why does a cricketer draw the hands back while catching?', 'To ' + T('increase the time') + ' of stopping the ball, so the force on the hands is smaller', definitionImage=M + 'fig_4_3_catch.webp')
d.cloze("Newton's second law: the rate of change of momentum is {{c1::proportional to the applied force}} and takes place {{c2::in the direction of the force}}.")
d.basic('Second law as an equation (constant mass)?', r'\(\vec F = \dfrac{d\vec p}{dt} = m\vec a\)')
d.basic('Define 1 newton.', N('1 N = 1 kg m s⁻²') + ': the force that gives ' + N('1 kg') + ' an acceleration of ' + N('1 m s⁻²'))
d.basic('Is the second law a scalar or vector law?', T('Vector') + ': it holds separately for each component')
d.basic('A force acts perpendicular to the velocity. What changes?', 'Only the ' + T('direction') + ' of velocity, not its magnitude', definitionImage=M + 'fig_4_4_stone_string.webp')
d.basic("What does 'the second law is a local law' mean?", 'Acceleration at an instant depends only on the force ' + T('at that instant') + ', not on past motion')
d.basic('Which F and a go into F = ma for a system of particles?', 'The ' + T('total external force') + ' and the acceleration of the system as a whole')
steps_card(d, 'Example 4.2', 'Find the missing step.',
           'A 0.04 kg bullet at 90 m/s stops after 60 cm in a wooden block. Average resistive force?',
           ['v² = u² − 2as with v = 0', 'a = 90² / (2 × 0.6) = 6750 m s⁻²', 'F = ma = 0.04 × 6750 = <b>270 N</b>'], 2,
           'Bullet stopped in block: resistive force', 'F = ma = 0.04 × 6750 = 270 N')

d.sec('4.5-impulse')
d.basic('Define impulse.', r'\(J = F\,\Delta t = \Delta p\)' + '<br>Unit: ' + N('N s'))
d.basic('What is an impulsive force?', 'A ' + T('large force') + ' acting for a ' + T('very short time') + ' (e.g. bat on ball)')
d.basic('Why use impulse instead of force for a bat hitting a ball?', 'Force and contact time are hard to measure separately, but ' + T('Δp') + ' is easy')
d.basic('A 0.15 kg ball at 12 m/s is hit straight back at the same speed. Impulse?', N('3.6 N s') + '  (0.15 × 12 − (−0.15 × 12))')
d.basic('A ball of mass m and speed u rebounds from a wall at angle θ to the normal, same speed. Impulse?',
        N('2mu cos θ') + ', along the ' + T('normal') + ' to the wall (parallel component unchanged)',
        definitionImage=M + 'fig_4_6_billiard.webp')

# ---------------------------------------------------------------- Third law
d.sec('4.6-third-law')
d.basic("State Newton's third law.", 'To every action there is an ' + T('equal and opposite reaction') + ': force on A by B = − force on B by A')
d.basic('Do action and reaction cancel each other?', X('No') + '. They act on ' + T('different bodies'))
d.basic('Which comes first: action or reaction?', X('Neither') + '. They are simultaneous; either can be called the action')
d.basic('Weight of a book and the normal force on it: action–reaction pair?', X('No') + '. Both act on the ' + T('same body') + ' (the book)')
d.basic("What is the reaction to the Earth's pull on a book?", "The book's pull on the " + T('Earth') + ' (equal, upward)')
d.basic('What do the internal action–reaction forces in a body add up to?', N('Zero'))

# ---------------------------------------------------------------- Momentum conservation
d.sec('4.7-momentum-conservation')
d.basic('State the law of conservation of momentum.', 'Total momentum of an ' + T('isolated system') + ' (no external force) stays constant')
d.basic('Which laws does momentum conservation follow from?', 'The ' + T('second') + ' and ' + T('third') + ' laws')
d.basic('Recoil velocity of a gun (mass M) firing a bullet (mass m, velocity v)?', r'\(V = -\dfrac{m v}{M}\)' + '<br>Opposite to the bullet')
d.basic('Is momentum conserved in an inelastic collision?', 'Yes. Momentum is conserved in ' + T('all') + ' collisions (kinetic energy only in elastic ones)')

# ---------------------------------------------------------------- Equilibrium
d.sec('4.8-equilibrium')
d.basic('When is a particle in equilibrium?', 'When the ' + T('net external force') + ' on it is ' + N('zero'))
d.basic('Three concurrent forces keep a particle in equilibrium. Geometric condition?', 'They form a ' + T('closed triangle') + ' when drawn head to tail', definitionImage=M + 'fig_4_7_force_triangle.webp')
d.basic('A 6 kg mass hangs from a 2 m rope. A 50 N horizontal force pulls the midpoint. Angle of the upper rope with the vertical? (g = 10)',
        r'\(\tan\theta = \dfrac{50}{60}\)' + ', so θ ≈ ' + N('40°'), definitionImage=M + 'fig_4_8_hanging_mass.webp')
d.basic("Lami's theorem for three forces in equilibrium?",
        r'\(\dfrac{F_1}{\sin\alpha} = \dfrac{F_2}{\sin\beta} = \dfrac{F_3}{\sin\gamma}\)' + '<br><small>each angle is opposite its force</small>')

# ---------------------------------------------------------------- Common forces
d.sec('4.9-common-forces')
d.basic('Which two kinds of force appear in mechanics problems?', T('Gravity') + ' (non-contact) and ' + T('contact forces') + ' (normal, friction, tension, spring)')
d.cloze('The contact force between two surfaces has a component perpendicular to the surface, the {{c1::normal reaction}}, and a component along it, {{c2::friction}}.')
d.basic("Hooke's law for a spring?", r'\(F = -kx\)' + '<br>k = spring constant; force opposes the displacement')
d.basic('Tension in a massless string over a smooth pulley?', 'The ' + T('same') + ' at every point')

d.sec('4.9-friction')
d.basic('What does friction oppose?', T('Relative motion') + ' (actual or impending) between surfaces, ' + X('not') + ' motion itself')
d.basic('Why is static friction called self-adjusting?', 'It grows to ' + T('match the applied force') + ', up to a maximum')
d.basic('Law of static friction?', r'\(f_s \le \mu_s N\)' + '<br>Limiting friction: ' + r'\(f_{s,\max} = \mu_s N\)', definitionImage=M + 'fig_4_10_friction.webp')
d.basic('Law of kinetic friction?', r'\(f_k = \mu_k N\)')
d.basic('Which is larger: μₛ or μₖ?', T('μₛ') + ': it is harder to start motion than to keep it going')
d.basic('Does friction depend on the area of contact?', X('No') + '. It depends on N and the nature of the surfaces')
sc.friction_graph(d)
table_card(d, 'Friction · order', 'Arrange by size for the same load.', [
    ('Largest', 'Limiting static friction', False), ('Middle', 'Kinetic (sliding) friction', False),
    ('Smallest', 'Rolling friction (2–3 orders smaller)', False)], term='Static vs kinetic vs rolling friction')
d.basic('Why does rolling friction exist at all?', 'The surfaces ' + T('deform') + ' slightly, so contact is an area, not a point')
d.basic('Three ways to reduce friction?', 'Lubricants, ' + T('ball bearings') + ', a cushion of air', definitionImage=M + 'fig_4_13_bearings.webp')
d.basic('Three places where friction is needed?', 'Walking, a car accelerating on a road, brakes')
d.basic('Max acceleration of a truck so a box on it does not slide (μₛ)?', r'\(a_{\max} = \mu_s g\)' + '<br>e.g. μₛ = 0.15 → ' + N('1.5 m s⁻²'))
d.basic('A block just starts to slide when the incline reaches angle θ. Relation with μₛ?', r'\(\tan\theta = \mu_s\)' + ' (angle of repose). Independent of mass')
d.occlusion('Fig. 4.11 · Forces on a block resting on an incline', M + 'fig_4_11_incline.webp', (1001, 477), [
    ('N (normal reaction)', [528, 20, 50, 48]), ('f<sub>s</sub> (static friction, up the slope)', [662, 90, 55, 45]),
    ('mg sin θ', rot([291, 222, 168, 44], -24)), ('mg cos θ', rot([648, 312, 172, 46], -24)), ('mg (weight)', [538, 370, 85, 45])], printed=True)
d.basic('Acceleration down a rough incline (angle θ, μₖ)?', r'\(a = g(\sin\theta - \mu_k\cos\theta)\)')
d.basic('Why is it easier to pull a roller than to push it (force at an angle)?',
        'Pulling ' + T('reduces N') + ' (mg − F sin θ), so friction is less; pushing increases N')
d.basic('Example 4.9: which horizontal forces act on the 20 kg trolley?', 'Tension ' + T('T') + ' forward and kinetic friction ' + T('fₖ') + ' backward',
        definitionImage=M + 'fig_4_12_block_trolley.webp')
steps_card(d, 'Example 4.9', 'Find the missing step.',
           '3 kg block hangs from a string over a smooth pulley, pulling a 20 kg trolley (μₖ = 0.04). g = 10 m/s².',
           ['Block: 30 − T = 3a', 'Trolley: T − f<sub>k</sub> = 20a', 'f<sub>k</sub> = μ<sub>k</sub>N = 0.04 × 200 = 8 N',
            'Add: 30 − 8 = 23a → <b>a = 0.96 m s⁻²</b>', 'T = 30 − 3a = 27.1 N'], 3,
           'Block and trolley: acceleration', 'a = 22/23 = 0.96 m s⁻², T = 27.1 N')

# ---------------------------------------------------------------- Circular motion
d.sec('4.10-circular-motion')
d.basic('Centripetal force for a body moving in a circle?', r'\(F = \dfrac{mv^2}{R}\)' + ', towards the centre')
d.basic('What provides the centripetal force for a stone on a string, a planet, and a car on a level road?', 'Tension; gravity of the Sun; ' + T('static friction'))
d.basic('Max safe speed on a level curve?', r'\(v_{\max} = \sqrt{\mu_s R g}\)' + '<br>Independent of the mass of the car')
d.basic('Optimum speed on a banked road (no friction needed)?', r'\(v_0 = \sqrt{R g \tan\theta}\)')
d.basic('Max safe speed on a banked road?', r'\(v_{\max} = \sqrt{Rg\,\dfrac{\mu_s + \tan\theta}{1 - \mu_s\tan\theta}}\)')
sc.banked_road(d)
d.occlusion('Fig. 4.14 · Resolve the forces on a car on a banked road', M + 'fig_4_14b_banked_components.webp', (1001, 721), [
    ('N cos θ', [690, 36, 235, 80]), ('N sin θ', [405, 252, 215, 80]), ('f cos θ', [28, 300, 200, 80]),
    ('f sin θ', [696, 460, 205, 80]), ('mg', [700, 606, 130, 85])], printed=True)
d.basic('Why is driving at the optimum speed on a banked road good for tyres?', 'Friction is not needed, so there is ' + T('little wear and tear'))
d.basic('Car on a banked road at v < v₀: which way does friction act?', T('Up the slope'))
d.basic('When can a car stay parked on a banked road?', r'\(\tan\theta \le \mu_s\)')
d.basic('Cyclist: 5 m/s on a 3 m turn, μₛ = 0.1, g = 9.8. Slips?', X('Yes') + ': v² = ' + N('25') + ' > μₛRg = ' + N('2.94'))
d.basic('Racetrack R = 300 m, banked 15°. Optimum speed?', N('28.1 m s⁻¹') + '  (√(Rg tan θ))')

# ---------------------------------------------------------------- Exam favourites built on the laws
d.sec('applications')
table_card(d, 'Apparent weight in a lift', 'Reading of the weighing scale?', [
    ('At rest / uniform velocity', 'mg', False), ('Accelerating up at a', 'm(g + a)', False),
    ('Accelerating down at a', 'm(g − a)', False), ('Free fall (a = g)', 'Zero (weightless)', True)],
    term='Apparent weight in a lift')
d.basic('Atwood machine (m₁ > m₂): acceleration?', r'\(a = \dfrac{(m_1 - m_2)\,g}{m_1 + m_2}\)')
d.basic('Atwood machine: tension in the string?', r'\(T = \dfrac{2 m_1 m_2\,g}{m_1 + m_2}\)')

# ---------------------------------------------------------------- Solving problems
d.sec('4.11-solving-problems')
d.basic('What is a free-body diagram?', 'A diagram of the chosen system showing ' + T('all forces on it') + ' from everything else', definitionImage=M + 'fig_4_15_fbd.webp')
d.basic('Should a free-body diagram show forces the system exerts on its surroundings?', X('No'))
d.basic('If the force on A by B is F in A\'s free-body diagram, what goes in B\'s?', r'\(-\vec F\)' + ' (third law)')
steps_card(d, 'Example 4.12', 'Find the missing step.',
           'A 2 kg block and a 25 kg cylinder on it sink together at 0.1 m/s² into a soft floor. g = 10 m/s². Force of the floor?',
           ['Weight of system = 27 × 10 = 270 N', '270 − R′ = 27 × 0.1', '<b>R′ = 267.3 N</b>'], 2,
           'Block and cylinder sinking: normal force', "R' = 270 − 2.7 = 267.3 N")

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
