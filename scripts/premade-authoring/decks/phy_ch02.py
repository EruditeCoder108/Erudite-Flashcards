import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase_phy as sp

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Physics', 'class11-physics-ch02-motion-in-a-straight-line')
d = Deck('Chapter 2: Motion in a Straight Line', 'Class 11', ['class-11', 'physics', 'ch-2'])
d.description = 'Displacement, velocity, acceleration, x-t and v-t graphs, equations of motion, free fall, relative velocity'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- 2.1 Introduction
d.sec('2.1-introduction')
d.basic('What is motion?', 'Change in ' + T('position') + ' of an object with time')
d.basic('What is rectilinear motion?', 'Motion along a ' + T('straight line'))
d.basic('What is kinematics?', 'Describing motion ' + X('without') + ' going into its causes (forces)')
d.basic('When can a body be treated as a point object?', 'When its size is much smaller than the ' + T('distance it moves') + ' in the time considered')
d.basic('Exercise 2.1: which are point objects? (a) carriage between stations (b) monkey on a cyclist on a circular track (c) spinning ball turning sharply (d) tumbling beaker',
        T('(a) and (b)') + '. In (c) and (d) the size matters compared with the distance moved')

d.sec('2.1-displacement-and-velocity')
d.basic('Path length vs displacement?', T('Path length') + ': total distance travelled (scalar, never decreases). ' + T('Displacement') + ': change in position Δx = x₂ − x₁ (vector, can be 0 or negative)')
d.basic('Can displacement be larger than path length?', X('Never') + '. |displacement| ≤ path length; equal only for motion in ' + T('one direction') + ' without turning back')
d.basic('Define average velocity and average speed.', 'Average velocity = ' + r'\( \dfrac{\Delta x}{\Delta t} \)' + '; average speed = ' + T('total path length') + ' ÷ time')
d.basic('A man walks 2.5 km to a market in 30 min and returns home in 20 min. Average velocity and average speed for the full 50 min?',
        'Velocity ' + N('0') + ' (back home). Speed = 5 km ÷ (5/6 h) = ' + N('6 km/h'))
d.basic('Exercise 2.10(c): the same man, 0 to 40 min (30 min out at 5 km/h, then 10 min back at 7.5 km/h)?',
        'Displacement 1.25 km, path 3.75 km in 2/3 h → average velocity ' + N('15/8 km/h') + ', average speed ' + N('45/8 km/h'))
d.basic('Why define average speed as path length ÷ time, not |average velocity|?', 'Otherwise a tired man who walks to the market and back would have ' + X('zero') + ' average speed')

# ---------------------------------------------------------------- 2.2 Instantaneous velocity
d.sec('2.2-instantaneous-velocity')
d.basic('Define instantaneous velocity.', r'\( v = \lim_{\Delta t \to 0} \dfrac{\Delta x}{\Delta t} = \dfrac{dx}{dt} \)' + ': rate of change of position at that instant')
d.basic('How do you read instantaneous velocity from an x–t graph?', T('Slope of the tangent') + ' at that instant', **fig('drawn_tangent_velocity'))
d.basic('Table 2.1 (x = 0.08t³): what happens to Δx/Δt at t = 4 s as Δt shrinks from 2 s to 0.01 s?', 'It falls 3.92 → 3.86 → 3.845 → … and ' + T('approaches 3.84 m/s') + ', the instantaneous velocity (= 0.24t²)', **fig('tab_2_1_limit'))
d.basic('Example 2.1: x = a + bt² with a = 8.5 m, b = 2.5 m s⁻². Velocity at t = 0 and 2 s?', 'v = dx/dt = 2bt = 5t: ' + N('0') + ' and ' + N('10 m/s'))
d.basic('Example 2.1: average velocity between t = 2 s and 4 s?', '[x(4) − x(2)] / 2 = 6b = ' + N('15 m/s') + ' (the a cancels)')
d.basic('For uniform motion, instantaneous vs average velocity?', T('Equal') + ' at every instant')
d.basic('What is instantaneous speed?', 'The ' + T('magnitude of instantaneous velocity') + '. +24 m/s and −24 m/s both have speed 24 m/s')
d.basic('Why is instantaneous speed always equal to |instantaneous velocity|, while average speed can exceed |average velocity|?',
        'Over an ' + T('infinitesimally small') + ' interval the particle cannot turn back, so |displacement| = path length')

# ---------------------------------------------------------------- 2.3 Acceleration
d.sec('2.3-acceleration')
d.basic('Galileo: is change of velocity constant per unit time or per unit distance in free fall?', 'Per unit ' + T('time') + ' (constant); per unit distance it ' + X('decreases') + '. Hence acceleration = rate of change of velocity with time')
d.basic('Define average and instantaneous acceleration.', r'\( \bar a = \dfrac{v_2 - v_1}{t_2 - t_1} \)' + ' ; ' + r'\( a = \dfrac{dv}{dt} \)' + '. SI unit ' + N('m s⁻²'))
d.basic('How do you read acceleration from a v–t graph?', 'The ' + T('slope') + ' of the v–t graph (tangent for instantaneous, chord for average)')
d.basic('Can acceleration arise without a change in speed?', T('Yes') + ': a change in ' + T('direction') + ' alone is an acceleration')
d.basic('Shape of the x–t graph for a > 0, a < 0 and a = 0?', 'Curves ' + T('upward') + ' (concave up), curves ' + T('downward') + ', ' + T('straight line'), **fig('drawn_xt_acceleration'))
d.basic('Fig. 2.3: describe the four v–t graphs.', '(a) moving +, speeding up; (b) moving +, slowing down; (c) moving −, speeding up; (d) slows, stops at t₁ and ' + T('turns back'), **fig('drawn_vt_cases'))
d.basic('What does the area under a v–t graph give?', 'The ' + T('displacement') + ' in that time interval', **fig('drawn_vt_area'))
d.basic('How can an area equal a distance?', 'The axes are velocity [L T⁻¹] and time [T], so "area" has dimensions ' + T('[L]'))
d.basic('What does the area under an a–t graph give?', 'The ' + T('change in velocity') + ' Δv')
table_card(d, 'Graph toolkit', 'What does it give?', [
    ('Slope of x–t', 'velocity', False), ('Slope of v–t', 'acceleration', False),
    ('Area under v–t', 'displacement', False), ('Area under a–t', 'change in velocity', False),
    ('Area under x–t', 'nothing useful', True)], term='Slopes and areas of motion graphs')
d.basic('Why can real x–t and v–t graphs not have sharp kinks?', 'A kink means velocity or acceleration changes ' + T('instantly') + '; real changes are always continuous')
table_card(d, 'Exercise 2.12 · Fig. 2.10', 'Why is each graph impossible?', [
    ('(a) x–t curve loops back in time', 'two positions at one instant', True), ('(b) v–t circle', 'two velocities at one instant', True),
    ('(c) speed–t goes below axis', 'speed cannot be negative', True), ('(d) path length–t falls', 'path length never decreases', True)],
    term='Impossible motion graphs (Fig. 2.10)')
d.basic('Identify: which graph cannot describe one-dimensional motion, and why?', 'All four: two positions or velocities at one time, negative speed, falling path length', **img('fig_2_10_impossible'))
d.basic('Exercise 2.13 (Fig. 2.11): does the particle move in a straight line for t < 0 and on a parabola for t > 0?',
        X('No') + ': an x–t graph is not the path. Example: a body at rest at x = 0 is ' + T('dropped at t = 0'), **fig('fig_2_11_xt'))

d.sec('2.3-signs-of-acceleration')
d.basic('When is a particle speeding up? Slowing down?', T('Speeding up') + ': a in the same direction as v. ' + T('Slowing down') + ': a opposite to v')
d.basic('Does a negative acceleration mean slowing down?', X('No') + ': the sign depends on the chosen axis. A ball falling with "up" positive has a = −g yet ' + T('speeds up'))
d.basic('Exercise 2.7(d): must a particle with positive acceleration be speeding up?', X('No') + ': only if v is also positive. With v < 0, a > 0 means slowing down')
d.basic('Exercise 2.7(c): must a particle with constant speed have zero acceleration (1D)?', T('Yes') + ' in 1D: constant speed with no turning means constant velocity. (An instant rebound would need infinite acceleration.)')

# ---------------------------------------------------------------- 2.4 Kinematic equations
d.sec('2.4-equations-of-motion')
d.cloze('Equations of motion for constant acceleration: {{c1::v = v₀ + at}},  {{c2::x = v₀t + ½at²}},  {{c3::v² = v₀² + 2ax}}.')
d.basic('Which quantity is missing from each equation of motion?', r'\( v = v_0 + at \)' + ': x.  ' + r'\( x = v_0t + \tfrac12 at^2 \)' + ': v.  ' + r'\( v^2 = v_0^2 + 2ax \)' + ': t.  ' + r'\( x = \tfrac{v_0 + v}{2}t \)' + ': a')
d.basic('How to pick the right equation fast?', 'Find the one quantity the question neither gives nor asks for, and use the equation ' + T('without it'))
d.basic('Average velocity under constant acceleration?', r'\( \bar v = \dfrac{v_0 + v}{2} \)' + ' (true ' + X('only') + ' for constant acceleration)')
steps_card(d, 'Derivation · area of v–t graph', 'Find the missing step.', 'Derive x = v₀t + ½at² from the v–t graph of v = v₀ + at.',
           ['Area = rectangle + triangle', 'Rectangle = v₀t', 'Triangle = ½(v − v₀)t = ½(at)t', 'x = v₀t + ½at²'], 2,
           'Deriving x = v₀t + ½at² from the v–t area', 'Rectangle v₀t plus triangle ½(v − v₀)t = ½at²')
d.basic('Equations of motion when the particle starts at x₀?', 'Replace x by ' + T('(x − x₀)') + ': ' + r'\( x = x_0 + v_0t + \tfrac12 at^2 \)' + ', ' + r'\( v^2 = v_0^2 + 2a(x - x_0) \)')
steps_card(d, 'Example 2.2 · calculus method', 'Find the missing step.', 'Derive v² = v₀² + 2a(x − x₀) by calculus.',
           ['a = dv/dt = (dv/dx)(dx/dt) = v dv/dx', 'v dv = a dx', 'Integrate: (v² − v₀²)/2 = a(x − x₀)', 'v² = v₀² + 2a(x − x₀)'], 1,
           'Deriving v² = v₀² + 2a(x − x₀) by calculus', 'Write a = v dv/dx, so v dv = a dx, then integrate')
d.basic('Advantage of the calculus method?', 'It also works for ' + T('non-uniform acceleration') + ' (a as a function of t, x or v)')
d.basic('Are the quantities in the equations of motion scalars?', 'They are ' + T('algebraic') + ': put in + or − signs according to the chosen positive direction')
d.basic('When are v = dx/dt and a = dv/dt valid vs the equations of motion?', 'Definitions: ' + T('always') + '. Equations of motion: ' + X('only') + ' when a is constant in magnitude and direction')
d.basic('Teacher addition: distance covered in the nth second?', r'\( s_n = u + \dfrac{a}{2}(2n - 1) \)')
d.basic('Teacher addition: a body starts from rest with uniform a. Ratio of distances in the 1st, 2nd, 3rd seconds?', N('1 : 3 : 5') + ' (sₙ ∝ 2n − 1)')

d.sec('2.4-examples')
d.basic('Example 2.3: ball thrown up at 20 m/s from a 25 m high building (g = 10). How high does it rise?', N('20 m') + ' above the roof (0 = 20² − 2 × 10 × h)', **fig('fig_2_6_building'))
steps_card(d, 'Example 2.3', 'Find the missing step.', 'Ball thrown up at 20 m/s from 25 m high roof (g = 10). Time to hit the ground?',
           ['Take up +, origin at ground: y₀ = 25, v₀ = 20, a = −10', 'y = y₀ + v₀t + ½at² with y = 0', '0 = 25 + 20t − 5t²',
            't² − 4t − 5 = 0 → (t − 5)(t + 1) = 0 → <b>t = 5 s</b>'], 2, 'Ball from a roof: time to hit the ground', '0 = 25 + 20t − 5t² gives t = 5 s')
d.basic('Why is the single-equation method better in Example 2.3?', 'Acceleration is constant throughout, so there is ' + T('no need to split') + ' the path at the top')
d.basic('Exercise 2.5: 126 km/h car stops in 200 m. Retardation and time?', N('3.06 m s⁻²') + ' and ' + N('11.4 s') + ' (v₀ = 35 m/s)')
d.basic('Exercise 2.4: a drunkard goes 5 steps forward, 3 back (1 m, 1 s each). Time to fall into a pit 13 m away?', N('37 s') + ': 2 m net per 8 s; after 32 s he is at 8 m, then 5 more steps')

d.sec('2.4-free-fall')
d.basic('What is free fall?', 'Motion under gravity alone (air resistance neglected): uniform acceleration ' + N('g = 9.8 m s⁻²') + ' downward')
d.basic('Free fall from rest, upward positive: equations?', r'\( v = -gt, \quad y = -\tfrac12 gt^2, \quad v^2 = -2gy \)', **fig('drawn_freefall_graphs'))
d.basic('a–t, v–t, y–t graphs in free fall (up positive)?', 'a–t: ' + T('horizontal line at −g') + '; v–t: straight line with slope −g; y–t: downward parabola', **fig('drawn_freefall_graphs'))
sp.vertical_throw(d)
d.basic('Ball thrown up: velocity and acceleration at the highest point?', 'v = ' + N('0') + ', a = ' + N('g downward') + ' (Exercise 2.6)')
table_card(d, 'Teacher addition · vertical throw at u', 'Formula?', [
    ('Maximum height', 'H = u² / 2g', False), ('Time to rise', 'u / g', False), ('Time of flight (back to hand)', '2u / g', False),
    ('Speed on return to launch point', 'u (same as launch)', False)], note='Time up = time down only when air resistance is neglected.', term='Vertical throw formulas')
d.basic('Exercise 2.6: ball thrown up at 29.4 m/s (g = 9.8). Height and time to return?', N('44.1 m') + ' and ' + N('6 s'))
d.basic('Teacher addition: dropped from height h. Time to fall and speed on hitting ground?', r'\( t = \sqrt{\dfrac{2h}{g}}, \quad v = \sqrt{2gh} \)')
d.basic('Trap: a stone is dropped from a balloon rising at 5 m/s. Initial velocity of the stone?', N('5 m/s upward') + ' (the balloon’s velocity), not zero')

d.sec('2.4-galileo-stopping-reaction')
sp.odd_numbers_strobe(d)
d.basic('Table 2.2: positions after τ, 2τ, 3τ… in units of ½gτ²?', N('1, 4, 9, 16, 25…') + ' (∝ n²), so gaps are ' + N('1, 3, 5, 7, 9'), **fig('tab_2_2_odd_numbers'))
d.basic('Stopping distance of a vehicle braking with deceleration a?', r'\( d_s = \dfrac{v_0^2}{2a} \)' + ' : ∝ ' + T('square of the speed'))
d.basic('Double the speed of a car. Stopping distance (same braking)?', N('4 times') + '. This is why speed limits in school zones are low')
d.basic('What is reaction time?', 'Time a person takes to ' + T('observe, think and act'))
d.basic('Example 2.7: a falling ruler is caught after 21.0 cm. Reaction time?', r'\( t_r = \sqrt{\dfrac{2d}{g}} = \sqrt{\dfrac{2 \times 0.21}{9.8}} \approx \)' + ' ' + N('0.2 s'), **fig('fig_2_8_ruler'))

# ---------------------------------------------------------------- 2.5 Relative velocity
d.sec('2.5-relative-velocity')
d.basic('Note: NCERT lists 2.5 Relative velocity, but the rationalised text dropped it. Is it still needed?', T('Yes') + ': Exercise 2.14 and Chapter 3 use it, and JEE/NEET ask it every year')
d.basic('Velocity of B relative to A (1D)?', r'\( v_{BA} = v_B - v_A \)' + ' : velocity of B as seen by an observer moving with A')
sp.relative_velocity_1d(d)
d.basic('Relation between v_AB and v_BA?', r'\( v_{AB} = -v_{BA} \)')
d.basic('Two trains at 54 km/h and 72 km/h approach each other. Relative speed?', N('126 km/h = 35 m/s') + ' (opposite directions: speeds add)')
d.basic('Two bodies with equal velocities: how does each look to the other?', T('At rest') + '; their separation stays constant and x–t lines are parallel')
d.basic('Exercise 2.14: police van at 30 km/h fires a bullet (150 m/s) at a thief’s car at 192 km/h ahead. Speed of impact?',
        'Bullet: 150 + 8.33 = 158.33 m/s; car: 53.33 m/s; relative ' + N('105 m/s'))
d.basic('Why does the relative speed matter for damage in Exercise 2.14?', 'The damage depends on how fast the bullet ' + T('meets the car') + ', i.e. relative to the car')

# ---------------------------------------------------------------- Graph exercises
d.sec('exercises-graphs')
d.basic('Exercise 2.2 (Fig. 2.9): who lives closer, who starts earlier, who walks faster?', T('A') + ' lives closer; ' + T('A') + ' starts earlier; ' + T('B') + ' walks faster (steeper), overtakes A once', **fig('fig_2_9_children'))
d.basic('Exercise 2.15(a): suggest a situation for this x–t graph.', 'A ball at rest on a smooth floor is kicked, rebounds from a wall with ' + T('reduced speed') + ' and is stopped by the opposite wall', **img('fig_2_12_situations'))
d.basic('Exercise 2.15(b), (c): situations for the v–t and a–t graphs?', '(b) A ball thrown up that rebounds from the floor with ' + T('less speed each time') + '. (c) A cricket ball moving uniformly, hit back by a bat for a ' + T('very short time'), **img('fig_2_12_situations'))
d.basic('Exercise 2.16 (SHM x–t): signs of x, v, a at t = 0.3 s?', 'x < 0, v < 0, a > 0. (In SHM, a is always opposite to x)', **img('fig_2_13_shm'))
d.basic('Exercise 2.17 (Fig. 2.14): which interval has the greatest and least average speed?', 'Greatest in ' + N('3') + ' (steepest), least in ' + N('2') + '; v > 0 in 1 and 2, v < 0 in 3', **img('fig_2_14_xt'))
d.basic('Exercise 2.18 (Fig. 2.15): acceleration at the points A, B, C, D (speed–time graph)?', N('Zero') + ' at all four: the tangent is horizontal there. |a| greatest in interval 2', **img('fig_2_15_speed'))

# ---------------------------------------------------------------- Summary
d.sec('summary')
table_card(d, 'Points to ponder', 'True or false?', [
    ('Zero velocity means zero acceleration', 'False (top of a throw)', True),
    ('Negative a means slowing down', 'False (depends on axis)', True),
    ('Average speed ≥ |average velocity|', 'True', False),
    ('Kinematic equations hold for any motion', 'False (constant a only)', True),
    ('Origin and positive direction are a choice', 'True', False)], term='Chapter 2 traps')
table_card(d, 'Summary', 'Shape of the graph for uniform acceleration?', [
    ('x–t', 'parabola', False), ('v–t', 'inclined straight line', False), ('a–t', 'horizontal line', False)],
    term='Graph shapes for uniformly accelerated motion')

print(d.write(os.path.join(OUT, 'deck.json')), 'cards')
