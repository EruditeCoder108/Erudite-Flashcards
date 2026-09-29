import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Physics', 'class12-physics-ch06-electromagnetic-induction')
d = Deck('Chapter 6: Electromagnetic Induction', 'Class 12', ['class-12', 'physics', 'ch-6'])
d.description = 'Faraday’s experiments, flux, Faraday’s and Lenz’s laws, motional emf, mutual and self inductance, magnetic energy, ac generator'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- 6.1-6.2 Introduction and experiments
d.sec('6.1-introduction')
d.basic('Who showed around 1830 that changing magnetic fields induce currents in closed coils?', T('Michael Faraday') + ' (England) and ' + T('Joseph Henry') + ' (USA)')
d.basic('Define electromagnetic induction.', 'Generation of an ' + T('emf / current') + ' in a circuit by a ' + T('changing magnetic flux') + ' through it')
d.basic('Which two devices came directly from Faraday and Henry’s work?', T('Generators') + ' and ' + T('transformers'))

d.sec('6.2-experiments-of-faraday-and-henry')
d.basic('Experiment 6.1: N-pole pushed towards a coil joined to a galvanometer. What happens?', 'The pointer ' + T('deflects') + ' while the magnet moves; no deflection when it is held still', **fig('fig_6_1_magnet_coil'))
d.basic('Experiment 6.1: what happens when the magnet is pulled away, or the S-pole is used?', 'Deflection ' + X('reverses') + ' for withdrawing; S-pole gives the opposite deflection to N-pole for the same motion')
d.basic('Effect of moving the magnet faster?', 'Larger deflection: a larger ' + T('rate of change of flux') + ' gives a larger emf and current')
d.basic('Magnet fixed, coil moved instead. Result?', 'Same effects: only the ' + T('relative motion') + ' matters')
d.basic('Experiment 6.2: coil C₂ (with battery) moved towards coil C₁. Result?', 'Current is induced in C₁ (reverses when C₂ moves away). C₂’s steady current acts like a ' + T('bar magnet'))
d.basic('Experiment 6.3: coils held fixed, key K pressed or released. What is observed?', T('Momentary') + ' deflection on making and (opposite) on breaking; ' + X('none') + ' while K is held closed', **fig('fig_6_3_two_coils'))
d.basic('Experiment 6.3: effect of inserting an iron rod along the coils?', 'Deflection increases ' + T('dramatically') + ': iron concentrates the flux')
d.basic('Key idea of all three experiments?', 'Steady flux, however large, induces ' + X('nothing') + '. Only a ' + T('changing') + ' flux does')
d.basic('Correction: the Faraday box says he found that light’s plane of polarisation is rotated “in an electric field”. Right?', X('No') + ': it is rotated in a ' + T('magnetic field') + ' along the direction of propagation (the ' + T('Faraday effect') + ', 1845)')
d.basic('Example 6.1(a): three ways to get a larger deflection in Experiment 6.2?', 'Soft-iron core in C₂; more powerful battery; move the arrangement faster')
d.basic('Example 6.1(b): show induced current without a galvanometer?', 'Replace it with a small ' + T('torch bulb') + ': it glows during relative motion')

# ---------------------------------------------------------------- 6.3 Magnetic flux
d.sec('6.3-magnetic-flux')
d.basic('Magnetic flux through a plane area A in a uniform B?', r'\( \Phi_B = \vec B\cdot\vec A = BA\cos\theta \)' + ', θ = angle between B and the ' + T('area vector (normal)'))
d.basic('Flux through a curved surface or non-uniform field?', r'\( \Phi_B = \int \vec B\cdot d\vec A = \sum \vec B_i\cdot d\vec A_i \)')
d.basic('Unit and nature of magnetic flux?', T('weber') + ' (Wb = T m²); a ' + T('scalar'))
d.basic('Flux is maximum and zero when?', 'Max BA at θ = ' + N('0°') + ' (plane ⊥ B). Zero at θ = ' + N('90°') + ' (plane ∥ B, field lines in the plane)')
d.basic('Trap: θ in Φ = BA cos θ is the angle between B and what?', X('The normal') + ' to the plane, not the plane itself. If given the angle with the plane, use sin')
d.basic('Three ways to change the flux through a loop?', 'Change ' + T('B') + ', change the ' + T('area A') + ' (shrink or stretch), change the ' + T('angle θ') + ' (rotate)')

# ---------------------------------------------------------------- 6.4 Faraday's law
d.sec('6.4-faradays-law-of-induction')
d.basic('State Faraday’s law of induction.', 'The magnitude of the induced emf equals the ' + T('rate of change of magnetic flux') + ' through the circuit')
d.basic('Mathematical form of Faraday’s law? Coil of N turns?', r'\( \varepsilon = -\dfrac{d\Phi_B}{dt} \)' + '; for N turns ' + r'\( \varepsilon = -N\dfrac{d\Phi_B}{dt} \)' + ' (Φ per turn)')
d.basic('What does the negative sign stand for?', 'The ' + T('direction') + ' of the induced emf (Lenz’s law): it opposes the flux change')
d.basic('Induced current in a closed loop of resistance R?', r'\( I = \dfrac{\varepsilon}{R} = -\dfrac{N}{R}\dfrac{d\Phi_B}{dt} \)')
d.basic('Teacher addition: charge that flows through the loop when flux changes by ΔΦ?', r'\( q = \int I\,dt = \dfrac{N\,\Delta\Phi}{R} \)' + ': independent of ' + T('how fast') + ' the flux changes')
d.basic('Why is the total induced emf in a coil of N turns N times larger?', 'Each turn sees the same flux change; the ' + T('emfs add in series') + '. Hence more turns → more emf')
d.basic('Faraday explained Experiment 6.3 how?', 'Pressing K raises C₂’s current, so flux through C₁ ' + T('rises') + ' → emf. Steady current: flux constant → none. Releasing K: flux falls → emf of ' + T('opposite sign'))
steps_card(d, 'Example 6.2 · decreasing field', 'Find the missing step.', 'Square loop of side 10 cm, R = 0.5 Ω. B = 0.10 T at 45° to the loop’s area vector falls to zero uniformly in 0.70 s. Find emf and I.',
           ['Φ₁ = BA cos 45° = 0.1 × 10⁻² × 0.707 = <b>7.1 × 10⁻⁴ Wb</b>', 'Φ₂ = 0, so ΔΦ = 7.1 × 10⁻⁴ Wb', '|ε| = ΔΦ/Δt = 7.1 × 10⁻⁴/0.7 ≈ <b>1.0 mV</b>', 'I = ε/R = 1.0 × 10⁻³/0.5 = <b>2 mA</b>'], 0,
           'Induced emf when B decreases (Example 6.2)', 'ε ≈ 1.0 mV, I = 2 mA')
d.basic('Example 6.2: does Earth’s magnetic field also add an emf?', X('No') + ': it is steady over the experiment, so its flux does not change')
steps_card(d, 'Example 6.3 · coil flipped', 'Find the missing step.', 'Circular coil, r = 10 cm, N = 500, R = 2 Ω, plane ⊥ horizontal B = 3.0 × 10⁻⁵ T. Turned through 180° about a vertical diameter in 0.25 s. Estimate emf and I.',
           ['Φ_initial = BA cos 0° = 3 × 10⁻⁵ × π × 10⁻² = <b>3π × 10⁻⁷ Wb</b>', 'Φ_final = BA cos 180° = <b>−3π × 10⁻⁷ Wb</b>, so |ΔΦ| = 6π × 10⁻⁷ Wb', 'ε = NΔΦ/Δt = 500 × 6π × 10⁻⁷/0.25 ≈ <b>3.8 × 10⁻³ V</b>', 'I = ε/R ≈ <b>1.9 mA</b> (average value)'], 1,
           'Flipping a coil in Earth’s field (Example 6.3)', 'ε ≈ 3.8 mV, I ≈ 1.9 mA')
d.basic('Trap in Example 6.3: why does a 180° flip give ΔΦ = 2BA, not zero?', 'Flux changes sign, ' + T('+BA → −BA') + ', so |ΔΦ| = ' + N('2BA'))

# ---------------------------------------------------------------- 6.5 Lenz's law
d.sec('6.5-lenzs-law-and-conservation-of-energy')
d.basic('State Lenz’s law.', 'The polarity of the induced emf is such that it tends to produce a current which ' + T('opposes the change in flux') + ' that produced it')
d.basic('Lenz’s law opposes the ______, not the ______.', 'Opposes the ' + T('change') + ' in flux, not the flux itself (a decreasing flux is supported, not opposed)')
d.basic('N-pole of a magnet approaches a closed coil. Induced current direction and pole faced?', T('Anticlockwise') + ' as seen from the magnet’s side; the coil face acts as an ' + T('N-pole') + ' (repels the magnet)', **fig('fig_6_6_lenz'))
d.basic('N-pole withdrawn from a coil. Induced current?', T('Clockwise') + ' (seen from the magnet); near face is a ' + T('S-pole') + ', attracts the receding magnet')
d.basic('Quick rule for the coil face nearest an approaching or receding pole?', T('Approach → same pole (repel)') + '; ' + T('recede → opposite pole (attract)') + '. Both oppose the motion')
d.basic('Intuition: how can you remember Lenz’s law?', 'Nature is “lazy”: it resists change. Flux up → induced field points ' + T('against') + ' B. Flux down → induced field points ' + T('along') + ' B')
d.basic('Direction of the current in an open circuit?', 'None flows, but an ' + T('emf') + ' still appears across the open ends, with polarity given by Lenz’s law')
d.basic('Why must Lenz’s law hold? (energy argument)', 'If the induced current aided the change, the magnet would accelerate itself: ' + X('perpetual motion') + ', violating ' + T('conservation of energy'))
d.basic('Where does the work done pulling the magnet against repulsion go?', 'Into ' + T('Joule heating') + ' in the coil (I²R losses)')
d.basic('Example 6.4: Fig 6.7(i): rectangular loop moving into a field pointing into the page. Direction of I?', 'Flux ' + T('increases') + ', so induced current is anticlockwise as needed: along ' + T('bcdab'), **fig('fig_6_7_loops'))
d.basic('Example 6.4: triangular loop (ii) moving out of the field, and irregular loop (iii)?', 'Flux ' + T('decreases') + ' in both, so current supports it. (ii) along ' + T('bacb') + ', (iii) along ' + T('cdabc'), **img('fig_6_7_loops'))
d.basic('Example 6.4: when is there no induced current?', 'While the loop is ' + T('completely inside or completely outside') + ' the field: flux is constant')
d.basic('Example 6.5(a): stationary closed loop between fixed strong magnets. Can it carry current?', X('No') + ': flux must ' + T('change') + '; strength alone does nothing')
d.basic('Example 6.5(b): closed loop moves normal to a constant E between capacitor plates. Current?', X('None') + ' in both cases (wholly or partly inside): changing electric flux does not induce current here')
d.basic('Example 6.5(c): a rectangular and a circular loop leave a uniform B at constant speed. Which has constant emf?', T('Rectangular') + ': its area inside changes at a constant rate. The circle’s rate ' + X('varies'), **fig('fig_6_8_rect_circle'))
d.basic('Example 6.5(d): polarity of the capacitor plates in Fig 6.9?', 'Plate ' + T('A is positive') + ' with respect to B (approaching magnets raise the flux; Lenz’s law sets the sense)', **fig('fig_6_9_capacitor'))

# ---------------------------------------------------------------- 6.6 Motional emf
d.sec('6.6-motional-electromotive-force')
d.basic('Rod PQ (length l) slides at speed v in a uniform B ⊥ the circuit. Flux and emf?', 'Φ = Blx, so ' + r'\( \varepsilon = -\dfrac{d(Blx)}{dt} = Blv \)' + ' (motional emf)', **fig('fig_6_10_motional'))
d.basic('Motional emf from the Lorentz force?', 'Force on a charge = qvB along the rod. Work carrying it across l: W = qvBl, so ' + r'\( \varepsilon = \dfrac{W}{q} = Blv \)')
d.basic('Condition for ε = Blv?', T('B, l and v mutually perpendicular') + '. In general ' + r'\( \varepsilon = (\vec v\times\vec B)\cdot\vec l \)')
d.basic('Trap: rod moves parallel to B, or the rod is parallel to v. Emf?', N('Zero') + ': the rod does not cut field lines. Only the component ⊥ to both counts')
d.basic('If the field is uniform and the rod slides, why is emf across it Blv even without a closed circuit?', 'Lorentz force separates charge to the ends until ' + T('qE = qvB') + '; the ends stay at potential difference Blv')
d.basic('Which end of the rod is at higher potential?', 'The end towards which the ' + T('force on positive charges') + ' (q v × B) pushes; current inside the rod flows from low to high potential (source)')
d.basic('Teacher addition: rod PQ on rails of resistance R pulled at constant v. Current, force and power?', 'I = Blv/R; magnetic drag ' + r'\( F = BIl = \dfrac{B^2l^2v}{R} \)' + '; power = Fv = ' + r'\( \dfrac{B^2l^2v^2}{R} \)' + ' = I²R (' + T('mechanical → heat') + ')')
d.basic('Why is there a magnetic force opposing the rod (Lenz’s law in disguise)?', 'The induced current in a field feels ' + T('F = I l × B') + ' opposing v; otherwise energy would be created')
d.basic('Faraday’s law when the conductor is stationary and B changes: which force acts on the charges?', 'Only ' + T('qE') + ' (v = 0): a ' + T('time-varying magnetic field creates an electric field') + ', unlike an electrostatic one')
d.basic('How does the induced E-field differ from an electrostatic E?', 'Its field lines form ' + T('closed loops') + '; it is non-conservative (∮E·dl = −dΦ/dt ≠ 0)')
d.basic('Fundamental significance of Faraday’s discovery?', 'A moving magnet or changing B exerts force on a ' + T('stationary charge') + ': electricity and magnetism are ' + T('related'))
d.basic('Example 6.6: rod of length R rotating at ω about one end in a field B ⊥ its plane. Emf between centre and rim?', r'\( \varepsilon = \tfrac12 B\omega R^2 \)' + ', from ' + r'\( \int_0^R B\omega r\,dr \)' + ' (mean speed ωR/2)', **fig('fig_6_11_rotating_rod'))
d.basic('Example 6.6: second method for the rotating rod?', 'Rate of area swept: dA/dt = ½R²ω, so ' + r'\( \varepsilon = B\dfrac{dA}{dt} = \tfrac12 B\omega R^2 \)')
d.basic('Example 6.6: R = 1 m, 50 rev/s, B = 1 T. Emf?', '½ × 1 × (2π × 50) × 1² = ' + N('≈ 157 V'))
d.basic('Example 6.7: wheel with 10 spokes of 0.5 m, 120 rev/min, H_E = 0.4 G. Emf between axle and rim?', T('½ω B R²') + ' = ½ × 4π × 0.4 × 10⁻⁴ × 0.25 = ' + N('6.28 × 10⁻⁵ V') + '. The 10 spokes are ' + T('in parallel') + ', so their number does not matter')
d.basic('Trap: which component of Earth’s field induces emf in a spinning wheel or falling wire?', 'The component ' + T('perpendicular to the plane of motion') + ' (vertical for a wheel in a horizontal plane; horizontal for a wire falling east–west)')

# ---------------------------------------------------------------- 6.7 Inductance
d.sec('6.7-inductance')
d.basic('Flux linkage for a closely wound coil of N turns?', T('NΦ_B') + ' (proportional to the current I)')
d.basic('Define inductance. Unit and dimensions?', 'Ratio of ' + T('flux linkage to current') + ': NΦ/I. Unit ' + T('henry (H)') + ' = Wb/A; [ML²T⁻²A⁻²]. It is a scalar')
d.basic('Dimensions of flux? Of emf?', 'Flux: [ML²T⁻²A⁻¹]; emf: [ML²T⁻³A⁻¹]')
d.basic('Inductance depends on what? Analogy?', 'Geometry and intrinsic material properties only (like capacitance: area, separation, dielectric constant)')

d.sec('6.7.1-mutual-inductance')
d.basic('Define mutual inductance M₁₂.', 'Flux linkage in coil 1 per unit current in coil 2: ' + r'\( N_1\Phi_1 = M_{12}I_2 \)')
d.basic('Mutual inductance of two long coaxial solenoids (inner radius r₁, length l)?', r'\( M = \mu_0 n_1 n_2 \pi r_1^2 l \)', **fig('fig_6_12_coaxial'))
d.basic('How is this derived?', 'B₂ = μ₀n₂I₂ (outer). Flux linkage with inner: N₁Φ = (n₁l)(πr₁²)(μ₀n₂I₂), so M = μ₀n₁n₂πr₁²l')
d.basic('Relation between M₁₂ and M₂₁?', T('M₁₂ = M₂₁ = M') + ' (general result, shown here for coaxial solenoids)')
d.basic('Why is M₁₂ = M₂₁ useful?', 'Compute whichever flux is ' + T('easy') + ' (small coil inside a big one: uniform field) and use the equality for the hard direction')
d.basic('Solenoids filled with a medium of relative permeability μᵣ. Mutual inductance?', r'\( M = \mu_r\mu_0 n_1 n_2 \pi r_1^2 l \)')
d.basic('What else does M depend on for a pair of coils?', 'Their ' + T('separation') + ' and ' + T('relative orientation'))
d.basic('Example 6.8: concentric coils, r₁ ≪ r₂. Mutual inductance?', r'\( M_{12} = M_{21} = \dfrac{\mu_0\pi r_1^2}{2r_2} \)' + ' (B₂ = μ₀I₂/2r₂ taken uniform over the small coil)')
d.basic('EMF induced in coil 1 when the current in coil 2 varies?', r'\( \varepsilon_1 = -M\dfrac{dI_2}{dt} \)')
d.basic('Teacher addition: coupling coefficient k?', r'\( M = k\sqrt{L_1L_2} \)' + ', 0 ≤ k ≤ 1; k = 1 for perfect flux linkage')

d.sec('6.7.2-self-inductance')
d.basic('Define self-induction and self-inductance L.', 'Emf induced in a coil by its own changing current. ' + r'\( N\Phi_B = LI \)')
d.basic('Self-induced emf?', r'\( \varepsilon = -L\dfrac{dI}{dt} \)' + ': it opposes any ' + T('increase or decrease') + ' of current (“back emf”)')
d.basic('Self-inductance of a long solenoid (area A, length l, n turns per length)?', r'\( L = \mu_0 n^2 A l \)' + '; with a core ' + r'\( L = \mu_r\mu_0 n^2 A l \)')
d.basic('Derive L of a solenoid.', 'B = μ₀nI; N = nl. NΦ = (nl)(μ₀nI)A = μ₀n²AlI, so L = NΦ/I = ' + T('μ₀n²Al'))
d.basic('Teacher addition: L in terms of total turns N?', r'\( L = \dfrac{\mu_0 N^2 A}{l} \)' + ': ' + N('L ∝ N²') + '. Doubling the turns (same length) quadruples L')
d.basic('Physical role of self-inductance?', 'Electrical ' + T('inertia') + ': analogue of ' + T('mass') + ' in mechanics; opposes growth and decay of current')
d.basic('Energy needed to build up current I in an inductor?', r'\( W = \int LI\,dI = \tfrac12 LI^2 \)' + ' (analogue of ½mv²)')
d.basic('Where is that energy stored?', 'In the ' + T('magnetic field') + ' (magnetic potential energy)')
d.basic('Two coils carrying currents together: emf in coil 1?', r'\( \varepsilon_1 = -L_1\dfrac{dI_1}{dt} - M_{12}\dfrac{dI_2}{dt} \)' + ' (M₁₁ = L₁ is self-inductance)')
d.basic('Example 6.9(a): magnetic energy stored in a solenoid in terms of B, A, l?', r'\( U_B = \dfrac{1}{2}LI^2 = \dfrac{B^2}{2\mu_0}Al \)' + ', using I = B/μ₀n and L = μ₀n²Al')
d.basic('Energy density of a magnetic field?', r'\( u_B = \dfrac{B^2}{2\mu_0} \)' + ', valid for ' + T('any region') + ' with a B-field, not just a solenoid')
d.basic('Magnetic vs electric energy density?', T('u_B = B²/2μ₀') + ' and ' + T('u_E = ½ε₀E²') + ': both ∝ (field)²')
d.basic('Teacher addition: why does a spark appear when a circuit with a big coil is broken?', 'Current falls fast: large dI/dt gives a big ' + T('back emf') + ' (L·dI/dt) that can exceed the supply and ionise air across the switch')
d.basic('Teacher addition: LR growth and decay in one line?', 'Current in an LR circuit changes over time constant ' + T('τ = L/R') + '; the inductor opposes an ' + T('instantaneous') + ' change. Not in NCERT text but often asked')
d.basic('Teacher addition: inductors in series (no coupling) and in parallel?', 'Series: ' + T('L = L₁ + L₂') + '. Parallel: ' + T('1/L = 1/L₁ + 1/L₂'))

# ---------------------------------------------------------------- 6.8 AC generator
d.sec('6.8-ac-generator')
d.basic('What does an ac generator do?', 'Converts ' + T('mechanical energy into electrical energy') + ' by electromagnetic induction')
d.basic('Basic parts of an ac generator?', T('Armature coil') + ' on a rotor shaft, uniform B from magnets, ' + T('slip rings') + ' and ' + T('carbon brushes') + ' to the external circuit', **fig('fig_6_13_generator'))
d.basic('Role of slip rings and brushes?', 'They connect the rotating coil to the ' + T('fixed external circuit') + ' without twisting the wires')
d.basic('Rotating coil: flux at time t? (θ = ωt, θ = 0 at t = 0)', r'\( \Phi_B = BA\cos\omega t \)')
d.basic('Instantaneous emf of a coil of N turns rotating in B?', r'\( \varepsilon = NBA\omega\sin\omega t = \varepsilon_0\sin\omega t \)' + ', ε₀ = ' + T('NBAω'))
d.basic('Same emf in terms of frequency ν?', r'\( \varepsilon = \varepsilon_0\sin 2\pi\nu t,\quad \varepsilon_0 = NBA(2\pi\nu) \)')
d.basic('When is the emf maximum and when zero?', 'Max at θ = ' + N('90°, 270°') + ' (plane ∥ B, flux changes fastest). Zero at ' + N('0°, 180°') + ' (plane ⊥ B, flux extreme)')
d.basic('Intuition: emf is zero when flux is maximum. Why?', 'ε = −dΦ/dt: at the peak of cos ωt the ' + T('slope is zero') + '. Flux and emf are ' + T('90° out of phase'), **fig('fig_6_14_ac_emf'))
d.basic('Trap: if the coil starts parallel to B (θ = 90° at t = 0), what is ε(t)?', T('ε = ε₀ cos ωt') + '. Always check the position at t = 0')
d.basic('What sets the frequency of the emf?', 'The coil’s ' + T('rotation frequency') + ' ν. Mains frequency: ' + N('50 Hz') + ' in India, ' + N('60 Hz') + ' in USA')
d.basic('Three ways to raise ε₀?', 'Increase ' + T('N') + ', ' + T('B') + ', ' + T('A') + ' or ' + T('ω'))
d.basic('Types of commercial generator by energy source?', T('Hydro-electric') + ' (falling water), ' + T('thermal') + ' (steam from coal etc.), ' + T('nuclear') + ' (nuclear fuel)')
d.basic('In most large generators, which part rotates?', 'The ' + T('electromagnets') + '; the coils stay stationary. Modern units reach ~500 MW (about 5 million 100 W bulbs)')
d.basic('Correction: NCERT calls Nikola Tesla “Yugoslav” and credits him with the machine. Better?', X('Loose') + ': Tesla (born in what is now Croatia) developed ' + T('polyphase ac systems and the induction motor') + '. Simple alternators go back to ' + T('Pixii (1832)') + '. Exams just say Tesla')
steps_card(d, 'Example 6.10 · peak emf', 'Find the missing step.', 'Coil of 100 turns, A = 0.10 m², rotating at 0.5 rev/s in B = 0.01 T ⊥ the axis. Maximum emf?',
           ['ε₀ = NBAω with ω = 2πν', 'ω = 2π × 0.5 = <b>π rad/s ≈ 3.14 rad/s</b>', 'ε₀ = 100 × 0.01 × 0.1 × 3.14 = <b>0.314 V</b>'], 1,
           'Kamla’s bicycle generator (Example 6.10)', 'ε₀ = 0.314 V')

# ---------------------------------------------------------------- Points to ponder
d.sec('points-to-ponder')
d.basic('Points to ponder: which principle does the conservation of energy demand in a closed circuit?', 'Induced currents flow so as to ' + T('oppose') + ' the flux change (' + T('Lenz’s law') + ')')
d.basic('Points to ponder: how is an open-circuit emf related to the flux change?', 'Still ' + T('ε = −dΦ/dt') + ' for the loop; just no current flows')
d.basic('Points to ponder: moving charge in a static B vs static charge in a changing B?', 'Both give emf: a ' + T('symmetric situation') + ' hinting at the ' + T('principle of relativity') + ' behind Faraday’s law')
d.basic('Correction: Points to Ponder refers to motional emf in “Section 6.5”. Which?', T('Section 6.6') + ' (6.5 is Lenz’s law)')
d.basic('Note: eddy currents in this chapter now?', X('No') + ': removed from rationalised NCERT, but JEE, NEET and boards still ask them: currents induced in a bulk conductor by changing flux; used in induction furnaces, damping, magnetic braking')
d.basic('Note: LR circuit and transformer here?', X('Not in this chapter') + ': the transformer comes in Ch 7; LR growth/decay is in JEE though')
table_card(d, 'Summary table', 'Symbol, unit, dimensions?', [
    ('Magnetic flux Φ_B', 'Wb; [ML²T⁻²A⁻¹]', False), ('EMF ε', 'V; [ML²T⁻³A⁻¹]', False),
    ('Mutual inductance M', 'H; [ML²T⁻²A⁻²]', False), ('Self inductance L', 'H; [ML²T⁻²A⁻²]', False)],
    term='NCERT quantity table')

# ---------------------------------------------------------------- Exercises
d.sec('exercises')
d.basic('Exercise 6.1(a): direction of induced current as the magnet approaches the coil pq (Fig 6.15a)?', 'Along ' + T('q → r → p → q'), **img('fig_6_15a'))
d.basic('Exercise 6.1(b): Fig 6.15(b) with two coils, magnet moving between them. Directions?', 'Coil pq: along ' + T('prq') + '; coil xy: along ' + T('yzx'), **img('fig_6_15b'))
d.basic('Exercise 6.1(c): tapping key just closed. Direction in the other loop (x, y, z)?', 'Along ' + T('y → z → x'), **img('fig_6_15c'))
d.basic('Exercise 6.1(d): rheostat setting being changed. Direction?', 'Along ' + T('z → y → x'), **img('fig_6_15d'))
d.basic('Exercise 6.1(e): tapping key just released. Direction?', 'Along ' + T('x → r → y'), **img('fig_6_15e'))
d.basic('Exercise 6.1(f): loop around a straight wire with decreasing current. Direction?', X('No induced current') + ': the wire’s field circles lie ' + T('in the plane') + ' of the loop, so flux is zero', **img('fig_6_15f'))
d.basic('Exercise 6.1: general method for these?', '(1) Direction of B through the loop. (2) Is flux rising or falling? (3) Induced field ' + T('opposes rise, supports fall') + '. (4) Right-hand rule for the current')
d.basic('Exercise 6.2(a): irregular wire pulled into a circle in a field into the page. Direction?', 'Area (flux) ' + T('increases') + ', so induced B points out: ' + T('anticlockwise, a → d → c → b → a'), **img('fig_6_16_deform'))
d.basic('Exercise 6.2(b): circle deformed into a narrow strip, field out of the page. Direction?', 'Flux ' + T('decreases') + ', induced B also out: ' + T('anticlockwise, a′ → d′ → c′ → b′'), **img('fig_6_16_deform'))
d.basic('Correction: the answer key writes 6.2(a) as “adcd”. What is right?', X('Typo') + ': the loop has four labelled points, so the path is ' + T('a → d → c → b → a') + ' (anticlockwise)')
steps_card(d, 'Exercise 6.3 · solenoid and small loop', 'Find the missing step.', 'Solenoid, 15 turns/cm. Small loop of area 2.0 cm² inside, normal to the axis. I changes 2.0 A → 4.0 A in 0.1 s. Induced emf?',
           ['n = 15 × 100 = <b>1500 m⁻¹</b>', 'B = μ₀nI, so ε = μ₀nA(dI/dt), dI/dt = 20 A/s', 'ε = 4π × 10⁻⁷ × 1500 × 2 × 10⁻⁴ × 20', 'ε ≈ <b>7.5 × 10⁻⁶ V</b>'], 0,
           'Induced emf in a small loop inside a solenoid (Exercise 6.3)', 'ε ≈ 7.5 × 10⁻⁶ V')
d.basic('Exercise 6.4(a): 8 cm × 2 cm loop with a cut leaves a 0.3 T field at 1 cm/s, normal to the longer side. Emf and duration?', 'ε = Blv = 0.3 × 0.08 × 0.01 = ' + N('2.4 × 10⁻⁴ V') + '; lasts 2 cm ÷ 1 cm/s = ' + N('2 s'))
d.basic('Exercise 6.4(b): same loop moving normal to the shorter side?', 'ε = 0.3 × 0.02 × 0.01 = ' + N('0.6 × 10⁻⁴ V') + '; lasts 8 cm ÷ 1 cm/s = ' + N('8 s'))
d.basic('Trap: in Exercise 6.4 which side cuts the field lines?', 'Only the side ' + T('perpendicular to v') + ' and still in the field: length l = 8 cm in (a), 2 cm in (b). Emf lasts as long as the loop is partly in the field')
d.basic('Exercise 6.5: 1.0 m rod rotated at 400 rad/s about one end in B = 0.5 T. Emf?', '½BωR² = ½ × 0.5 × 400 × 1 = ' + N('100 V'))
steps_card(d, 'Exercise 6.6 · falling wire', 'Find the missing step.', '10 m east–west horizontal wire falls at 5.0 m/s. B_H = 0.30 × 10⁻⁴ T. (a) emf, (b) direction, (c) which end is higher?',
           ['ε = Blv = 0.30 × 10⁻⁴ × 10 × 5.0 = <b>1.5 × 10⁻³ V</b>', 'v is down, B horizontal north: v × B points <b>east</b>', 'Force on positive charges is eastward, so emf is directed <b>west → east</b>', 'The <b>eastern end</b> is at higher potential'], 1,
           'Emf in a falling wire (Exercise 6.6)', '1.5 mV, W → E, eastern end higher')
d.basic('Exercise 6.7: current falls 5.0 A → 0 in 0.1 s; average induced emf 200 V. Self-inductance?', 'L = ε/|dI/dt| = 200/(5/0.1) = ' + N('4 H'))
d.basic('Exercise 6.8: M = 1.5 H; current in one coil goes 0 → 20 A in 0.5 s. Change of flux linkage in the other?', 'ΔNΦ = MΔI = 1.5 × 20 = ' + N('30 Wb'))

# ---------------------------------------------------------------- Summary
d.sec('summary')
table_card(d, 'Summary', 'Formula?', [
    ('Flux', 'Φ_B = BA cos θ', False), ('Faraday’s law', 'ε = −N dΦ_B/dt', False), ('Motional emf', 'ε = Blv', False),
    ('Rotating rod', 'ε = ½Bωl²', False), ('Mutual inductance', 'ε₁ = −M dI₂/dt', False), ('Self-induced emf', 'ε = −L dI/dt', False),
    ('Solenoid L', 'μᵣμ₀n²Al', False), ('Energy in L', '½LI²', False), ('Energy density', 'B²/2μ₀', False), ('AC generator', 'ε = NBAω sin ωt', False)],
    term='Chapter 6 formula sheet')
table_card(d, 'Concept checks', 'True or false?', [
    ('A strong steady B through a loop induces emf', 'False (needs change)', True), ('Lenz’s law is a consequence of energy conservation', 'True', False),
    ('Self-induced emf opposes only an increase in current', 'False (opposes any change)', True), ('M₁₂ = M₂₁', 'True', False),
    ('Emf of a rotating coil is max when flux is max', 'False (flux max → emf 0)', True), ('Energy density of B is B²/2μ₀', 'True', False)],
    term='Chapter 6 concept checks')

print(d.write(os.path.join(OUT, 'deck.json')), 'cards')
