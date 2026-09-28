import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Physics', 'class12-physics-ch04-moving-charges-and-magnetism')
d = Deck('Chapter 4: Moving Charges and Magnetism', 'Class 12', ['class-12', 'physics', 'ch-4'])
d.description = 'Lorentz force, motion in B, Biot–Savart law, circular loop, Ampere’s law, solenoid, parallel currents, torque on a loop, galvanometer'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- 4.1 Introduction
d.sec('4.1-introduction')
d.basic('Who discovered that a current deflects a compass needle? When?', T('Hans Christian Oersted') + ' (Danish), ' + N('1820') + ', during a lecture demonstration')
d.basic('How does a compass needle align near a long straight current?', T('Tangent to circles') + ' centred on the wire, in a plane perpendicular to it; reversing the current reverses the needle', **fig('drawn_wire_field'))
d.basic('How do iron filings arrange around a straight current-carrying wire?', 'In ' + T('concentric circles') + ' centred on the wire')
d.basic('Oersted’s conclusion?', T('Moving charges (currents) produce a magnetic field') + ' in the surrounding space')
d.basic('Who unified electricity and magnetism, and when? What did he realise?', T('James Maxwell') + ', ' + N('1864') + '; light is an electromagnetic wave')
d.basic('Who discovered and who produced radio waves?', 'Discovered by ' + T('Hertz') + '; produced by ' + T('J. C. Bose') + ' and ' + T('G. Marconi'))
d.basic('Convention: dot ⊙ and cross ⊗ for a field or current?', '⊙ = ' + T('out of the page') + ' (arrow tip towards you); ⊗ = ' + T('into the page') + ' (feathered tail going away)')

# ---------------------------------------------------------------- 4.2 Magnetic force
d.sec('4.2-magnetic-force')
d.basic('Properties the magnetic field shares with the electric field?', 'Defined at every point (vector field), can vary with time, obeys ' + T('superposition'))
d.basic('Lorentz force on a charge q?', r'\( \vec F = q\left[\vec E + \vec v\times\vec B\right] \)')
d.basic('Three features of the magnetic force q(v × B)?', '(1) Opposite for − charges; (2) ' + T('perpendicular to v and B') + ', zero if v ∥ B; (3) ' + X('zero for a charge at rest'), **fig('fig_4_2_force_direction'))
d.basic('Define 1 tesla.', 'Field in which a charge of ' + N('1 C') + ' moving at ' + N('1 m/s') + ' perpendicular to B feels ' + N('1 N') + ': 1 T = 1 N s C⁻¹ m⁻¹')
d.basic('Gauss in tesla? Earth’s field?', '1 G = ' + N('10⁻⁴ T') + '; Earth ≈ ' + N('3.6 × 10⁻⁵ T') + ' (≈ 0.4 G)')
d.basic('Dimensions of B?', '[M T⁻² A⁻¹]')
d.basic('Force on a straight current-carrying rod in a uniform B?', r'\( \vec F = I\,\vec l\times\vec B \)' + ', with ' + r'\( \vec l \)' + ' along the current (current itself is not a vector)')
d.basic('In F = Il × B, whose field is B?', 'The ' + T('external') + ' field — not the field of the rod itself')
d.basic('Force on a wire of arbitrary shape?', 'Sum over elements: ' + r'\( \vec F = \sum I\,d\vec l_j\times\vec B \)' + ' (an integral)')
d.basic('Teacher addition: force on a closed loop or a bent wire in a uniform B?', 'Closed loop: ' + N('zero') + '. Bent wire from P to Q: same as a ' + T('straight wire PQ') + ' carrying I')
d.basic('Example 4.1: 200 g, 1.5 m wire with 2 A suspended by a horizontal B. B?', 'mg = IlB → B = 0.2 × 9.8/(2 × 1.5) = ' + N('0.65 T'), **fig('fig_4_3_suspended_wire'))
d.basic('Example 4.2: B along +y, particle moves along +x. Force on an electron? On a proton?', 'v × B is along +z: proton ' + T('+z') + ', electron ' + T('−z'), **fig('fig_4_4_example'))
d.basic('Exercise 4.5: 8 A wire at 30° to B = 0.15 T. Force per unit length?', 'IB sin 30° = ' + N('0.6 N/m'))
d.basic('Exercise 4.6: 3.0 cm wire with 10 A inside a solenoid, perpendicular to its axis, B = 0.27 T. Force?', 'IlB = 10 × 0.03 × 0.27 = ' + N('8.1 × 10⁻² N'))
d.basic('Mnemonic: direction of force on a current (or + charge) in B?', T('Right-hand rule') + ': fingers along v (or I), curl towards B; thumb gives F. For an electron, reverse it. (Fleming’s left-hand rule gives the same: Field, Current, Motion)')

# ---------------------------------------------------------------- 4.3 Motion in B
d.sec('4.3-motion-in-magnetic-field')
d.basic('Does a magnetic force change a particle’s speed or kinetic energy? Why?', X('No') + ': F ⊥ v, so it does ' + T('no work') + '; only the direction changes')
d.basic('Charge moving perpendicular to a uniform B: path and radius?', T('Circle') + ' in the plane ⊥ B; ' + r'\( r = \dfrac{mv}{qB} = \dfrac{p}{qB} \)', **fig('fig_4_5_circular'))
d.basic('Angular frequency and period of circular motion in B?', r'\( \omega = \dfrac{qB}{m},\ T = \dfrac{2\pi m}{qB} \)' + ' — ' + T('independent of speed and radius'))
d.basic('Velocity at an angle to B: path? Pitch?', T('Helix') + ' with axis along B; pitch ' + r'\( p = v_\parallel T = \dfrac{2\pi m v_\parallel}{qB} \)' + '; radius uses v⊥', **fig('fig_4_6_helical'))
d.basic('Define cyclotron frequency.', r'\( \nu_c = \dfrac{qB}{2\pi m} \)' + ': frequency of circular motion in B, independent of energy')
d.basic('Note: NCERT’s introduction and summary mention the cyclotron. Is its section in the book?', X('No') + ': it was removed in the rationalised syllabus. Just know it uses ν_c being ' + T('independent of speed') + ' to accelerate particles')
steps_card(d, 'Example 4.3 · electron in B', 'Find the missing step.', 'Electron (9 × 10⁻³¹ kg) at 3 × 10⁷ m/s perpendicular to B = 6 × 10⁻⁴ T. Radius, frequency, energy?',
           ['r = mv/qB = 9 × 10⁻³¹ × 3 × 10⁷ / (1.6 × 10⁻¹⁹ × 6 × 10⁻⁴) = <b>28 cm</b>', 'ν = v/2πr = <b>17 MHz</b>',
            'E = ½mv² = ½ × 9 × 10⁻³¹ × 9 × 10¹⁴ ≈ 4 × 10⁻¹⁶ J', '= 4 × 10⁻¹⁶ / 1.6 × 10⁻¹⁹ eV = <b>2.5 keV</b>'], 1,
           'Electron circling in a magnetic field (Example 4.3)', 'r = 28 cm, ν = 17 MHz, E ≈ 2.5 keV')
d.basic('Exercise 4.11: electron at 4.8 × 10⁶ m/s normal to B = 6.5 G. Why a circle? Radius?', 'F ⊥ v provides centripetal force; r = mv/eB ≈ ' + N('4.2 cm'))
d.basic('Correction: NCERT Exercise 4.11 gives e = 1.5 × 10⁻¹⁹ C. Right value, and does it matter?', 'e = ' + T('1.6 × 10⁻¹⁹ C') + ' (typo). With 1.6, r = 4.2 cm (the answer key value); with 1.5 you would get 4.5 cm')
d.basic('Exercise 4.12: frequency of that electron? Depends on speed?', 'ν = eB/2πm ≈ ' + N('18 MHz') + '; ' + X('independent of speed') + ' (r grows with v, time per turn stays the same)')
d.basic('Teacher addition: an electron and a proton enter the same B with equal momenta. Compare radii.', 'Equal (r = p/qB, same |q|). With equal kinetic energy, r ∝ √m, so the proton’s circle is larger')

# ---------------------------------------------------------------- 4.4 Biot–Savart
d.sec('4.4-biot-savart-law')
d.basic('Sources of all known magnetic fields?', T('Currents / moving charges') + ' and ' + T('intrinsic magnetic moments') + ' of particles')
d.basic('State the Biot–Savart law.', r'\( d\vec B = \dfrac{\mu_0}{4\pi}\dfrac{I\,d\vec l\times\vec r}{r^3} \)' + '; magnitude ' + r'\( \dfrac{\mu_0}{4\pi}\dfrac{I\,dl\sin\theta}{r^2} \)', **fig('fig_4_7_biot_savart'))
d.basic('Value of μ₀/4π? Name of μ₀?', r'\( \dfrac{\mu_0}{4\pi} = 10^{-7} \)' + ' T m/A; μ₀ = ' + T('permeability of free space'))
d.basic('Update: NCERT says μ₀ = 4π × 10⁻⁷ exactly. Still exact?', X('Not since 2019') + ': fixing e made μ₀ a measured constant, 1.25663706… × 10⁻⁶ T m/A — equal to 4π × 10⁻⁷ to 10 digits, so use it freely')
d.basic('Biot–Savart vs Coulomb: similarities?', 'Both ' + T('inverse-square') + ' and long range; both obey superposition; both linear in their source')
d.basic('Biot–Savart vs Coulomb: differences?', 'Source: ' + T('vector I dl') + ' vs scalar q. Direction: B ⊥ plane of dl and r vs E along r. B has a ' + T('sin θ') + ' dependence')
d.basic('Magnetic field of a current element at a point along its own line?', N('Zero') + ' (θ = 0, sin θ = 0)')
d.basic('Relation between ε₀, μ₀ and c?', r'\( c = \dfrac{1}{\sqrt{\mu_0\varepsilon_0}} \)' + ' — fixing one of μ₀, ε₀ fixes the other')
d.basic('Example 4.4: element Δl = 1 cm along x at the origin, I = 10 A. B at 0.5 m on the y-axis?', 'dB = 10⁻⁷ × 10 × 10⁻² / 0.25 = ' + N('4 × 10⁻⁸ T') + ', along ' + T('+z') + ' (î × ĵ = k̂)', **fig('fig_4_8_element'))

# ---------------------------------------------------------------- 4.5 Circular loop
d.sec('4.5-field-on-axis-of-circular-loop')
d.basic('Field on the axis of a circular loop (radius R) at distance x?', r'\( B = \dfrac{\mu_0 I R^2}{2(x^2 + R^2)^{3/2}} \)' + ', along the axis', **fig('fig_4_9_loop_axis'))
d.basic('Why does only the axial component survive for a circular loop?', 'The perpendicular components dB⊥ of ' + T('diametrically opposite') + ' elements cancel')
d.basic('Field at the centre of a circular loop? N turns?', r'\( B = \dfrac{\mu_0 I}{2R} \)' + '; with N turns ' + r'\( \dfrac{\mu_0 NI}{2R} \)')
d.basic('Right-hand thumb rule for a loop?', 'Curl the fingers along the current; the ' + T('thumb') + ' gives B (and the loop’s N face)', **fig('fig_4_10_loop_lines'))
d.basic('Two right-hand rules: how do fingers and thumb swap roles?', 'Straight wire: ' + T('thumb = current') + ', fingers = B. Loop: ' + T('fingers = current') + ', thumb = B')
d.basic('Example 4.5: 12 A wire bent into a semicircle (R = 2 cm) with straight leads. B at the centre?', 'Straight parts: 0 (dl ∥ r). Semicircle: half a loop, ' + r'\( \mu_0 I/4R \)' + ' = ' + N('1.9 × 10⁻⁴ T') + ' into the page; bent the other way, same size, opposite direction', **fig('fig_4_11_semicircle'))
d.basic('Example 4.6: 100 turns, R = 10 cm, I = 1 A. B at the centre?', r'\( \mu_0NI/2R \)' + ' = ' + N('6.28 × 10⁻⁴ T'))
d.basic('Exercise 4.1: 100 turns, R = 8.0 cm, 0.40 A. B at the centre?', N('3.1 × 10⁻⁴ T'))
d.basic('Teacher addition: field at the centre of an arc subtending angle φ (radians)?', r'\( B = \dfrac{\mu_0 I\varphi}{4\pi R} \)' + ' (φ = 2π gives the loop, φ = π the semicircle)')

# ---------------------------------------------------------------- 4.6 Ampere's law
d.sec('4.6-amperes-circuital-law')
d.basic('State Ampere’s circuital law.', r'\( \oint \vec B\cdot d\vec l = \mu_0 I \)' + ', I = net current through the surface bounded by the loop', **fig('fig_4_12_amperian'))
d.basic('Sign convention in Ampere’s law?', T('Right-hand rule') + ': curl the fingers along the direction of traversal; the thumb gives the positive current direction')
d.basic('Simplified form for symmetric cases?', r'\( BL = \mu_0 I_e \)' + ' where B is tangential and constant over length L of the loop (elsewhere B ⊥ loop or zero)')
d.basic('Field of a long straight wire from Ampere’s law?', r'\( B\cdot2\pi r = \mu_0 I \Rightarrow B = \dfrac{\mu_0 I}{2\pi r} \)' + ', tangential circles')
d.basic('Four lessons from B = μ₀I/2πr?', '(1) ' + T('Cylindrical symmetry') + '; (2) field lines are closed circles; (3) finite at finite r even for an infinite wire; (4) direction by the right-hand grip rule')
d.basic('Ampere’s law is to Biot–Savart as ___ is to ___?', T('Gauss’s law') + ' to ' + T('Coulomb’s law') + ': same content, handy under symmetry')
d.basic('Can Ampere’s law give B at the centre of a circular loop?', X('No') + ': no suitable symmetric loop; use Biot–Savart')
d.basic('Ampere’s law as given here holds for what kind of currents?', T('Steady') + ' currents only')
d.basic('Example 4.7: thick wire (radius a, uniform current I). B inside and outside?', 'Outside: ' + r'\( \dfrac{\mu_0I}{2\pi r} \)' + ' (∝ 1/r). Inside: ' + r'\( \dfrac{\mu_0 I r}{2\pi a^2} \)' + ' (∝ r, enclosed current Ir²/a²)', **fig('fig_4_13_thick_wire'))
d.basic('Sketch B versus r for a thick wire with uniform current.', 'Rises ' + T('linearly') + ' from 0 at the centre to a maximum at r = a, then falls as ' + T('1/r'), **fig('fig_4_14_B_vs_r'))
d.basic('Exercise 4.2: 35 A wire. B at 20 cm?', N('3.5 × 10⁻⁵ T'))
d.basic('Exercise 4.3: 50 A flowing north to south in a horizontal wire. B at 2.5 m east of it?', N('4 × 10⁻⁶ T') + ', vertically ' + T('upward'))
d.basic('Exercise 4.4: overhead line, 90 A east to west. B 1.5 m below it?', N('1.2 × 10⁻⁵ T') + ', towards the ' + T('south'))

# ---------------------------------------------------------------- 4.7 Solenoid
d.sec('4.7-the-solenoid')
d.basic('What is a long solenoid? Why enamelled wire?', 'A tightly wound helix whose length ≫ radius; enamel ' + T('insulates') + ' neighbouring turns')
d.basic('Field pattern of a finite solenoid?', 'Inside: ' + T('strong, uniform, along the axis') + '; outside: weak; fields between neighbouring turns cancel', **fig('fig_4_15_solenoid'))
d.basic('Field inside a long solenoid? Derive with Ampere’s law.', 'Rectangular loop abcd: only side ab (length h) inside contributes; Bh = μ₀(nh)I → ' + r'\( B = \mu_0 n I \)', **fig('fig_4_16_long_solenoid'))
d.basic('How can the field of a solenoid be made much larger?', 'Insert a ' + T('soft iron core'))
d.basic('Teacher addition: field at the end of a long solenoid?', r'\( \tfrac12\mu_0 nI \)' + ' — half the value at the centre')
d.basic('Example 4.8: 0.5 m solenoid, 500 turns, 5 A. B inside?', 'n = 1000/m; B = 4π × 10⁻⁷ × 10³ × 5 = ' + N('6.28 × 10⁻³ T'))
d.basic('Correction: NCERT Example 4.8 cites “Eq. (4.20)” for the long-solenoid field. Right equation?', T('Eq. (4.16)') + ', B = μ₀nI; Eq. (4.20) is the torque on a loop')
d.basic('Exercise 4.8: 80 cm long, 5 layers of 400 turns, 8.0 A. B near the centre?', 'n = 2000/0.8 = 2500 m⁻¹ → B = ' + N('2.5 × 10⁻² T') + ' (diameter doesn’t matter)')

# ---------------------------------------------------------------- 4.8 Parallel currents
d.sec('4.8-force-between-parallel-currents')
d.basic('Force per unit length between two long parallel currents?', r'\( f = \dfrac{\mu_0 I_a I_b}{2\pi d} \)', **fig('fig_4_17_parallel_wires'))
d.basic('Parallel vs antiparallel currents?', T('Parallel attract') + ', ' + X('antiparallel repel') + ' — the opposite of the charge rule (like charges repel)')
d.basic('Do forces between parallel steady currents obey Newton’s third law?', 'Yes: F_ba = −F_ab. (For time-varying fields, only if field momentum is included)')
d.basic('NCERT’s definition of the ampere (1946)?', 'Current in two infinitely long parallel thin wires ' + N('1 m') + ' apart in vacuum giving a force of ' + N('2 × 10⁻⁷ N per metre'))
d.basic('Update: is the ampere still defined by parallel wires?', X('No') + ': since 2019 it is defined by fixing ' + T('e = 1.602176634 × 10⁻¹⁹ C') + ' (1 A = 1 C/s with e exact); the wire result still holds')
d.basic('Instrument used to measure the force between currents?', 'A ' + T('current balance'))
d.basic('Example 4.9: 1 A on a table, Earth’s horizontal field 3.0 × 10⁻⁵ T (S → N). Force per metre for current E → W? S → N?', 'E → W: ' + N('3 × 10⁻⁵ N/m') + ', downward. S → N: ' + N('0') + ' (parallel to B)')
d.basic('Exercise 4.7: 8.0 A and 5.0 A in the same direction, 4.0 cm apart. Force on 10 cm of A?', N('2 × 10⁻⁵ N') + ', attractive')
d.basic('Intuition: why do parallel currents attract?', 'Between the wires their circular fields ' + T('oppose') + ' (weak); outside they add (strong). Wires get pushed towards the weak-field region — towards each other')

# ---------------------------------------------------------------- 4.9 Torque on a loop
d.sec('4.9-torque-on-current-loop')
d.basic('Rectangular loop in a uniform B: net force? Torque?', 'Net force ' + N('0') + '; torque ' + r'\( \tau = IAB\sin\theta \)' + ' (θ between normal and B)', **fig('fig_4_18_coil_torque'))
d.basic('Why does the torque on a loop fall as it turns towards θ = 0?', 'The forces on AB and CD stay IbB but the ' + T('perpendicular distance between them') + ' (a sin θ) shrinks', **fig('fig_4_19_coil_angle'))
d.basic('Magnetic moment of a current loop? Unit and dimensions?', r'\( \vec m = NI\vec A \)' + ' (direction by right-hand thumb rule); A m² (= J/T), [L²A]')
d.basic('Torque on a magnetic dipole in B (vector)?', r'\( \vec\tau = \vec m\times\vec B \)' + ' — analogue of τ = p × E')
d.basic('Stable and unstable equilibrium of a loop in B?', T('Stable') + ': m parallel to B. ' + X('Unstable') + ': m antiparallel')
d.basic('Teacher addition: potential energy of a magnetic dipole in B?', r'\( U = -\vec m\cdot\vec B = -mB\cos\theta \)')
steps_card(d, 'Example 4.10 · coil released in B', 'Find the missing step.', '100 turns, R = 10 cm, 3.2 A; B = 2 T with the axis initially along B; the coil turns 90°. Torques, and angular speed (moment of inertia 0.1 kg m²)?',
           ['m = NIπR² = 100 × 3.2 × 3.14 × 10⁻² ≈ <b>10 A m²</b>', 'τ = mB sin θ: 0 at the start, <b>20 N m</b> at 90°',
            'Work done by field over 90° = mB(1 − cos 90°) = 20 J = ½ 𝐼ω²', 'ω = √(2 × 20/0.1) = <b>20 rad/s</b>'], 2,
           'Coil rotating in a magnetic field (Example 4.10)', 'm ≈ 10 A m²; τ from 0 to 20 N m; ½𝐼ω² = mB → ω = 20 s⁻¹')
d.basic('Correction: in Example 4.10, “initially the axis of the coil is along the field” and the coil then rotates 90°. Would it rotate on its own?', X('No') + ': θ = 0 is ' + T('stable equilibrium') + ' (zero torque); the example only works if it starts at 90° and swings to 0°. The numbers (τ 0 ↔ 20 N m, ω = 20 s⁻¹) are unaffected')
d.basic('Example 4.11(a): can a uniform B spin a horizontal loop about the vertical axis?', X('No') + ': τ = IA × B is always in the plane of the loop, never vertical')
d.basic('Example 4.11(b): stable orientation of a loop in B? What about the flux?', 'Area vector ' + T('along B') + '; then the loop’s own field adds to B, giving ' + T('maximum total flux'))
d.basic('Example 4.11(c): why does a flexible irregular current loop become circular?', 'To ' + T('maximise flux') + ': a circle encloses the most area for a given perimeter')
d.basic('Exercise 4.9: square coil, side 10 cm, 20 turns, 12 A; normal at 30° to B = 0.80 T. Torque?', 'NIAB sin 30° = ' + N('0.96 N m'))
d.basic('Exercise 4.13: 30 turns, R = 8.0 cm, 6.0 A, B = 1.0 T at 60° to the normal. Counter-torque? Irregular coil of equal area?', N('3.1 N m') + '; ' + T('unchanged') + ' — torque depends only on area, not shape')

d.sec('4.9.2-current-loop-as-magnetic-dipole')
d.basic('Field of a current loop far away on its axis?', r'\( B \approx \dfrac{\mu_0}{4\pi}\dfrac{2m}{x^3} \)' + ' — like the axial field of an electric dipole')
d.basic('Field of a loop far away in its own plane?', r'\( B \approx \dfrac{\mu_0}{4\pi}\dfrac{m}{x^3} \)' + ' (equatorial field)')
d.basic('Substitutions that turn electric dipole formulas into magnetic ones?', r'\( p \to m,\ E \to B,\ \dfrac{1}{\varepsilon_0} \to \mu_0 \)')
d.basic('Fundamental difference between electric and magnetic dipoles?', 'An electric dipole is made of two charges; ' + X('magnetic monopoles are not known') + ' — the current loop is the most elementary magnetic element')
d.basic('Ampere’s hypothesis? Is it the whole story?', 'All magnetism comes from ' + T('circulating currents') + '. Partly true: electrons and protons also have ' + T('intrinsic') + ' magnetic moments')

# ---------------------------------------------------------------- 4.10 Galvanometer
d.sec('4.10-moving-coil-galvanometer')
d.basic('Principle of a moving coil galvanometer?', 'Torque ' + T('NIAB') + ' on a coil in a radial field is balanced by the spring’s restoring torque kφ', **fig('fig_4_20_mcg'))
d.basic('Why is the field in a galvanometer radial? Role of the soft-iron core?', 'Radial field keeps the coil’s plane along B, so ' + T('sin θ = 1') + ' at every deflection (linear scale); the core makes it radial and ' + T('stronger'))
d.basic('Deflection of a galvanometer?', r'\( \varphi = \left(\dfrac{NAB}{k}\right) I \)' + ' (k = torsional constant, restoring torque per unit twist)')
d.basic('Current sensitivity? Voltage sensitivity?', r'\( \dfrac{\varphi}{I} = \dfrac{NAB}{k},\quad \dfrac{\varphi}{V} = \dfrac{NAB}{kR} \)')
d.basic('Doubling the turns: effect on current and voltage sensitivity?', 'Current sensitivity ' + T('doubles') + '; resistance also doubles, so voltage sensitivity ' + X('is unchanged'))
d.basic('Why can’t a galvanometer be used directly as an ammeter?', 'It is very sensitive (full-scale ~' + N('μA') + ') and has a large resistance that would change the circuit current')
d.basic('How is a galvanometer converted to an ammeter?', 'A small ' + T('shunt r_s in parallel') + '; net resistance ≈ r_s', **fig('fig_4_21_ammeter'))
d.basic('How is a galvanometer converted to a voltmeter?', 'A large ' + T('resistance R in series') + '; net resistance ≈ R, so it draws little current', **fig('fig_4_22_voltmeter'))
d.basic('Teacher addition: shunt needed for full-scale current I (galvanometer G, full scale I_g)? Series R for voltage V?', r'\( S = \dfrac{I_g G}{I - I_g},\quad R = \dfrac{V}{I_g} - G \)')
d.basic('Ideal ammeter and ideal voltmeter resistances?', 'Ammeter: ' + N('zero') + '; voltmeter: ' + N('infinite'))
d.basic('Galvanometer used as a null detector (bridge): pointer zero where?', 'In the ' + T('middle') + ' of the scale, deflecting left or right with current direction')
d.basic('Example 4.12: 3 V across 3 Ω. Current read by (a) a 60 Ω galvanometer, (b) with a 0.02 Ω shunt, (c) an ideal ammeter?', '(a) 3/63 = ' + N('0.048 A') + '; (b) 3/3.02 = ' + N('0.99 A') + '; (c) ' + N('1.00 A'), **fig('fig_4_23_example'))
d.basic('Exercise 4.10: M1 (10 Ω, 30 turns, 3.6 × 10⁻³ m², 0.25 T) vs M2 (14 Ω, 42, 1.8 × 10⁻³ m², 0.50 T). Ratios M2:M1?', 'Current sensitivity ' + N('1.4') + '; voltage sensitivity ' + N('1'))

# ---------------------------------------------------------------- Points to ponder / summary
d.sec('points-to-ponder')
d.basic('Electric vs magnetic field lines?', 'Electric: start on + and end on − (or at infinity). Magnetic: ' + T('always closed loops'))
d.basic('Points to ponder: in a frame moving with the charge, the magnetic force vanishes. What explains the motion there?', 'An ' + T('electric field') + ' appears in that frame — E and B are parts of one electromagnetic field; no preferred frame')
d.basic('Is Ampere’s law independent of Biot–Savart?', X('No') + ': it can be derived from it')

d.sec('summary')
table_card(d, 'Summary', 'Formula?', [
    ('Lorentz force', 'F = q(E + v × B)', False), ('Force on a wire', 'F = I l × B', False), ('Radius in B', 'r = mv/qB', False),
    ('Cyclotron frequency', 'ν = qB/2πm', False), ('Loop centre', 'B = μ₀NI/2R', False), ('Long wire', 'B = μ₀I/2πr', False),
    ('Solenoid', 'B = μ₀nI', False), ('Parallel wires', 'f = μ₀I₁I₂/2πd', False), ('Torque on loop', 'τ = m × B, m = NIA', False)],
    term='Chapter 4 formula sheet')
table_card(d, 'Concept checks', 'True or false?', [
    ('A magnetic field can speed up a charge', 'False (no work)', True), ('Period of circular motion depends on speed', 'False', True),
    ('Parallel currents repel', 'False (attract)', True), ('Net force on a current loop in uniform B is zero', 'True', False),
    ('B inside a long solenoid is uniform', 'True', False)], term='Chapter 4 concept checks')

print(d.write(os.path.join(OUT, 'deck.json')), 'cards')
