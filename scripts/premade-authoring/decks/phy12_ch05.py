import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Physics', 'class12-physics-ch05-magnetism-and-matter')
d = Deck('Chapter 5: Magnetism and Matter', 'Class 12', ['class-12', 'physics', 'ch-5'])
d.description = 'Bar magnet, field lines, dipole in B, Gauss’s law for magnetism, M, H, χ, dia-, para- and ferromagnetism'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- 5.1 Introduction
d.sec('5.1-introduction')
d.basic('Origin of the word “magnet”, per NCERT?', 'From ' + T('Magnesia') + ' in Greece, where magnetic ore was found as early as ' + N('600 BC'))
d.basic('Correction: NCERT calls Magnesia “an island”. Is it?', X('No') + ': Magnesia is a ' + T('region of Thessaly') + ' on the Greek mainland (there was also a city Magnesia in Asia Minor). Exams only ask “Magnesia”')
d.basic('Earth’s magnetic field points roughly which way?', 'From geographic ' + T('south to north') + ' (so Earth’s magnetic S pole is near the geographic North)')
d.basic('Which end of a freely suspended bar magnet is its north pole?', 'The end that points to the ' + T('geographic north'))
d.basic('Force between like and unlike magnetic poles?', 'Like poles ' + X('repel') + ', unlike poles ' + T('attract'))
d.basic('A bar magnet is broken in two. What do you get?', T('Two smaller magnets') + ', each with N and S poles and weaker properties — poles cannot be isolated')
d.basic('What are magnetic monopoles? Do they exist?', 'Isolated N or S poles; ' + X('not known to exist') + ' (unlike isolated electric charges)')

# ---------------------------------------------------------------- 5.2 Bar magnet
d.sec('5.2-the-bar-magnet')
d.basic('What does the iron-filing pattern around a bar magnet suggest?', 'The magnet is a ' + T('magnetic dipole') + ' — two poles, like + and − of an electric dipole. A current-carrying solenoid gives the same pattern')
d.basic('Compare the field lines of a bar magnet, a finite solenoid and an electric dipole.', 'Far away they look ' + T('almost identical') + '. Inside, the magnet’s and solenoid’s lines run S → N (closing the loops); the electric dipole’s run + → − (opposite)', **fig('fig_5_2_field_lines'))

d.sec('5.2.1-magnetic-field-lines')
d.cloze('Magnetic field lines form {{c1::continuous closed loops}}; electric field lines {{c2::start on + charges and end on − charges (or at infinity)}}.')
d.basic('What does the tangent to a magnetic field line give?', 'The direction of the net ' + T('B') + ' at that point')
d.basic('What does the density of field lines tell you?', 'Magnitude of B: more lines per unit area (normal to them) → ' + T('stronger field'))
d.basic('Why can’t two magnetic field lines intersect?', 'At the crossing the field would have ' + T('two directions') + ' — B must be unique')
d.basic('How can you plot field lines without iron filings?', 'Move a small ' + T('compass needle') + ' around and note its orientation at each point')
d.basic('Why does NCERT avoid the term “magnetic lines of force”?', 'The force on a moving charge is ' + X('perpendicular to B') + ' (qv × B), not along the line — so the lines do not show the direction of force')

d.sec('5.2.2-bar-magnet-as-equivalent-solenoid')
d.basic('Why can a bar magnet be treated as an equivalent solenoid?', 'Same field-line pattern; by ' + T('Ampere’s hypothesis') + ' a magnet is a large number of circulating currents. Cutting either gives two weaker ones')
d.basic('Far axial field of a solenoid (or bar magnet) of moment m?', r'\( B = \dfrac{\mu_0}{4\pi}\dfrac{2m}{r^3} \)' + ' (r ≫ size)')
d.basic('Magnetic moment of a bar magnet equals…?', 'The moment of the ' + T('equivalent solenoid') + ' that produces the same field (NIA)')

d.sec('5.2.3-dipole-in-uniform-field')
d.basic('Torque on a magnetic dipole in a uniform B?', r'\( \vec\tau = \vec m\times\vec B,\quad \tau = mB\sin\theta \)' + ' (restoring)')
d.basic('Net force on a magnetic dipole in a uniform B?', N('Zero') + ' — equal and opposite forces on the two poles; only a torque')
d.basic('Potential energy of a magnetic dipole in B? Where is its zero?', r'\( U_m = -\vec m\cdot\vec B = -mB\cos\theta \)' + '; zero at ' + T('θ = 90°') + ' (m ⊥ B)')
d.basic('Minimum and maximum potential energy of a dipole in B?', 'Minimum ' + N('−mB') + ' at θ = 0° (' + T('most stable') + '); maximum ' + N('+mB') + ' at θ = 180° (' + X('most unstable') + ')')
d.basic('Work needed to turn a dipole from θ₁ to θ₂ in B?', r'\( W = mB(\cos\theta_1 - \cos\theta_2) \)' + '; from 0° to 180° it is ' + N('2mB'))
d.basic('Teacher addition: period of small oscillations of a needle (moment of inertia 𝐼) in B?', r'\( T = 2\pi\sqrt{\dfrac{I}{mB}} \)' + ' — the Fig. 5.3(b) set-up; measure T to find B or m')
d.basic('Intuition: why does a compass needle oscillate before settling?', 'Displaced from θ = 0, τ = −mB sin θ ≈ −mBθ acts like a ' + T('spring') + ' → SHM about the field direction, damped by friction')
d.basic('Example 5.1(a): a bar magnet is cut (i) across its length, (ii) along its length. Result?', 'Either way, ' + T('two magnets') + ', each with a N and S pole')
d.basic('Example 5.1(b): a needle in a uniform B feels only a torque, but an iron nail near a magnet is attracted. Why?', 'The magnet’s field is ' + T('non-uniform') + '. The nail gets an ' + T('induced moment') + '; its induced S pole is nearer the magnet’s N pole, so net attraction')
d.basic('Example 5.1(c): must every magnetic configuration have N and S poles?', X('No') + ': only if it has a net non-zero moment. A ' + T('toroid') + ' or a straight infinite wire has no poles')
d.basic('Example 5.1(d): two identical iron bars, one surely a magnet. How to tell which, using only the bars?', 'Lower an end of A onto the end and then the middle of B. If the pull ' + T('vanishes at B’s middle') + ', B is the magnet; if no change, A is. (Repulsion anywhere → both magnetised)')

d.sec('5.2.4-electrostatic-analog')
d.basic('Replacements that turn electric dipole results into bar-magnet results?', r'\( \vec E\to\vec B,\ \vec p\to\vec m,\ \dfrac{1}{4\pi\varepsilon_0}\to\dfrac{\mu_0}{4\pi} \)')
d.basic('Equatorial field of a short bar magnet (r ≫ l)?', r'\( \vec B_E = -\dfrac{\mu_0}{4\pi}\dfrac{\vec m}{r^3} \)' + ' — ' + X('opposite to m'))
d.basic('Axial field of a short bar magnet (r ≫ l)?', r'\( \vec B_A = \dfrac{\mu_0}{4\pi}\dfrac{2\vec m}{r^3} \)' + ' — along m; ' + N('twice') + ' the equatorial value at the same r', **fig('drawn_axial_equatorial'))
table_card(d, 'Table 5.1', 'Magnetic analogue?', [
    ('1/ε₀', 'μ₀', False), ('Dipole moment p', 'm', False), ('Equatorial field −p/4πε₀r³', '−μ₀m/4πr³', False),
    ('Axial field 2p/4πε₀r³', 'μ₀2m/4πr³', False), ('Torque p × E', 'm × B', False), ('Energy −p·E', '−m·B', False)],
    term='Table 5.1 · The dipole analogy')
d.basic('Example 5.2: needle P at O (moment up); identical needle Q at positions Q₁–Q₆. Which are not in equilibrium?', T('PQ₁ and PQ₂') + ': on P’s equator the field is downward, but Q points sideways → torque', **img('fig_5_4_needles'))
d.basic('Example 5.2: which configurations are stable and which unstable?', 'Stable (Q ∥ B_P): ' + T('PQ₃, PQ₆') + '. Unstable (Q antiparallel): ' + X('PQ₅, PQ₄'), **img('fig_5_4_needles'))
d.basic('Example 5.2: which configuration has the lowest potential energy? Why?', T('PQ₆') + ': Q is along the field and on P’s axis, where B is ' + N('twice') + ' the equatorial value at the same distance', **img('fig_5_4_needles'))
d.basic('Trick for Example 5.2 type questions?', 'Find the direction of P’s field at Q (axis: along m_P; equator: opposite). Q ∥ B → stable, antiparallel → unstable, at an angle → not in equilibrium')

# ---------------------------------------------------------------- 5.3 Gauss's law
d.sec('5.3-magnetism-and-gausss-law')
d.basic('State Gauss’s law for magnetism.', 'The net magnetic flux through ' + T('any closed surface') + ' is zero: ' + r'\( \oint \vec B\cdot d\vec S = 0 \)')
d.basic('Gauss’s law: electrostatics vs magnetism?', 'Electric flux = q/ε₀ (charges are sources and sinks). Magnetic flux = ' + N('0') + ' — ' + X('no monopoles') + ', no sources or sinks of B')
d.basic('Magnetic flux through a small area ΔS? Unit?', r'\( \Delta\phi_B = \vec B\cdot\Delta\vec S \)' + '; ' + T('weber') + ' (Wb = T m²)')
d.basic('Simplest magnetic element, according to Gauss’s law?', 'A ' + T('dipole') + ' or current loop — all magnetism can be built from these')
d.basic('Why is the magnetic flux zero through the Gaussian surfaces i and ii around a bar magnet?', 'Field lines are closed loops: every line that ' + T('leaves also enters') + ' the surface, even around a pole', **fig('fig_5_2_field_lines'))
d.basic('Example 5.3(a): are these magnetic field lines right?', X('Wrong') + ': lines can’t spring from a point (net flux ≠ 0). This is the ' + T('electric field of a charged wire') + '; B around a wire is circles', **img('fig_5_6a'))
d.basic('Example 5.3(b): are these magnetic field lines right?', X('Wrong') + ': lines cross, and a static B line can’t loop around ' + T('empty space') + ' — a closed B loop must enclose a current', **img('fig_5_6b'))
d.basic('Example 5.3(c): field lines of a toroid. Right?', T('Right') + ': confined inside the toroid; each loop encloses current', **img('fig_5_6c'))
d.basic('Example 5.3(d): straight, confined lines through a solenoid. Right?', X('Wrong') + ': at the ends the lines must ' + T('curve out') + ' and close; perfectly straight lines violate Ampere’s law', **img('fig_5_6d'))
d.basic('Example 5.3(e): lines outside and inside a bar magnet. Right?', T('Right') + ': inside they run S → N; the net flux around each pole is zero', **img('fig_5_6e'))
d.basic('Example 5.3(f): lines pouring out of a plate. Magnetic?', X('Wrong') + ' for B (net flux out of the plate ≠ 0). It is the ' + T('electric field') + ' of a + upper and − lower plate', **img('fig_5_6f'))
d.basic('Example 5.3(g): perfectly straight lines between two pole pieces. Right?', X('Wrong') + ': some ' + T('fringing') + ' at the edges is inevitable (true for E between plates too)', **img('fig_5_6g'))
d.basic('Example 5.4(a): are magnetic field lines lines of force on a moving charge?', X('No') + ': the force qv × B is always ' + T('normal to B'))
d.basic('Example 5.4(b): Gauss’s law for magnetism if monopoles existed?', r'\( \oint \vec B\cdot d\vec S = \mu_0 q_m \)' + ', q_m = enclosed magnetic charge')
d.basic('Example 5.4(c): does a magnet exert a torque on itself? Does one element of a wire push another element of the same wire?', 'No self-force or self-torque on an element from ' + T('its own field') + '. But one element does act on ' + T('another') + ' element of the same wire (zero for a straight wire)')
d.basic('Example 5.4(d): can a system with zero net charge have a magnetic moment?', T('Yes') + ': e.g. atoms of paramagnetic materials — neutral, but with net current loops')

# ---------------------------------------------------------------- 5.4 M and H
d.sec('5.4-magnetisation-and-magnetic-intensity')
d.basic('Define magnetisation M. Unit and dimensions?', r'\( \vec M = \dfrac{\vec m_{net}}{V} \)' + ' (net moment per unit volume); ' + T('A m⁻¹') + ', [L⁻¹A]')
d.basic('Field inside a solenoid filled with a magnetised core?', r'\( B = B_0 + B_m = \mu_0 nI + \mu_0 M \)' + ' — the core adds B_m = μ₀M')
d.basic('Define magnetic intensity H. Unit?', r'\( \vec H = \dfrac{\vec B}{\mu_0} - \vec M \)' + '; A m⁻¹ (same as M)')
d.basic('Total B in terms of H and M?', r'\( \vec B = \mu_0(\vec H + \vec M) \)')
d.basic('What do H and M separately represent?', 'H: the part due to ' + T('external causes') + ' (e.g. solenoid current, H = nI). M: the part due to the ' + T('material') + ' itself')
d.basic('Define magnetic susceptibility χ.', r'\( \chi = \dfrac{M}{H} \)' + ' — dimensionless; how strongly a material responds to H')
d.basic('Sign of χ for para- and diamagnets?', 'Paramagnetic: ' + T('small, positive') + '. Diamagnetic: ' + X('small, negative') + ' (M opposite to H)')
d.cloze('Relative permeability: {{c1::μᵣ = 1 + χ}}; permeability: {{c2::μ = μ₀μᵣ = μ₀(1 + χ)}}, so {{c3::B = μH}}.')
d.basic('μᵣ is the magnetic analogue of what?', 'The ' + T('dielectric constant K') + ' in electrostatics')
d.basic('Of χ, μᵣ and μ, how many are independent?', N('One') + ': given any one, the other two follow')
steps_card(d, 'Example 5.5 · cored solenoid', 'Find the missing step.', 'Solenoid, n = 1000 turns/m, I = 2 A, core μᵣ = 400. Find H, B, M and the magnetising current I_M.',
           ['H = nI = 1000 × 2 = <b>2 × 10³ A/m</b> (independent of the core)', 'B = μᵣμ₀H = 400 × 4π × 10⁻⁷ × 2 × 10³ ≈ <b>1.0 T</b>',
            'M = (μᵣ − 1)H = 399 × 2 × 10³ ≈ <b>8 × 10⁵ A/m</b>', 'Without the core: B = μ₀n(I + I_M) → 2 + I_M = 1/(4π × 10⁻⁴) ≈ 796 → <b>I_M ≈ 794 A</b>'], 2,
           'Solenoid with a magnetic core (Example 5.5)', 'H = 2 × 10³ A/m, B ≈ 1 T, M ≈ 8 × 10⁵ A/m, I_M ≈ 794 A')
d.basic('What is the magnetising current I_M?', 'The ' + T('extra current') + ' the windings would need, without the core, to produce the same B as with the core')
d.basic('Correction: NCERT Example 5.5 has three slips. What are they?', '(1) “H is ' + X('dependent') + ' of the material” should read ' + T('independent') + '. (2) The parts (b), (c) solve B then M, swapping the question’s order. (3) I_M uses B = ' + X('μᵣ') + 'n(I + I_M); it must be ' + T('μ₀') + 'n(I + I_M) — only that gives 794 A')

# ---------------------------------------------------------------- 5.5 Magnetic properties of materials
d.sec('5.5-magnetic-properties-of-materials')
d.basic('Classify materials by χ.', T('Diamagnetic') + ': χ negative. ' + T('Paramagnetic') + ': χ small positive. ' + T('Ferromagnetic') + ': χ large positive')
table_card(d, 'Table 5.2', 'Range?', [
    ('Diamagnetic χ', '−1 ≤ χ < 0', False), ('Diamagnetic μᵣ', '0 ≤ μᵣ < 1  (μ < μ₀)', False),
    ('Paramagnetic χ', '0 < χ < ε (small)', False), ('Paramagnetic μᵣ', '1 < μᵣ < 1 + ε  (μ > μ₀)', False),
    ('Ferromagnetic χ', 'χ ≫ 1', False), ('Ferromagnetic μᵣ', 'μᵣ ≫ 1  (μ ≫ μ₀)', False)],
    term='Table 5.2 · χ and μᵣ by class')

d.sec('5.5.1-diamagnetism')
d.basic('What are diamagnetic substances?', 'Substances that tend to move from ' + T('stronger to weaker') + ' parts of a field — they are ' + X('repelled') + ' by a magnet')
d.basic('Field lines through a diamagnetic and a paramagnetic bar?', 'Diamagnetic (a): lines are ' + X('expelled') + ', field inside slightly reduced. Paramagnetic (b): lines ' + T('concentrate') + ', field inside slightly enhanced (about 1 part in 10⁵)', **fig('fig_5_7_dia_para'))
d.basic('Explain diamagnetism.', 'Atoms have ' + T('zero net moment') + '. An applied field slows electrons whose orbital moment is along B and speeds up those opposite (' + T('Lenz’s law') + '), giving a net moment ' + X('opposite to B') + ' → repulsion')
d.cloze('Diamagnetic examples: {{c1::bismuth, copper, lead, silicon, nitrogen (at STP), water and sodium chloride}}.')
d.basic('Mnemonic: diamagnetic examples?', '“' + T('B') + 'right ' + T('C') + 'opper ' + T('L') + 'eads ' + T('Si') + 'lly ' + T('N') + 'ew ' + T('W') + 'orkers to ' + T('S') + 'alt” — Bi, Cu, Pb, Si, N₂, water, NaCl')
d.basic('Is diamagnetism found in all substances?', T('Yes') + ', it is universal — but so weak that para- or ferromagnetism masks it')
d.basic('What is the Meissner effect?', T('Perfect diamagnetism') + ' of a superconductor: field lines are completely expelled; χ = ' + N('−1') + ', μᵣ = ' + N('0'))
d.basic('Two properties of superconductors?', T('Perfect conductivity') + ' and ' + T('perfect diamagnetism') + ', at very low temperatures')
d.basic('Application of superconducting magnets named by NCERT?', 'Magnetically ' + T('levitated superfast trains') + ' (maglev)')
d.basic('Which theory explains superconductivity? When, and when was the Nobel prize?', T('BCS theory') + ' (Bardeen, Cooper, Schrieffer), ' + N('1957') + '; NCERT dates its Nobel Prize to 1970')
d.basic('Correction: NCERT says the BCS Nobel Prize came in 1970. Right year?', T('1972') + ' (Nobel Prize in Physics to Bardeen, Cooper and Schrieffer)')

d.sec('5.5.2-paramagnetism')
d.basic('What are paramagnetic substances?', 'Substances ' + T('weakly magnetised') + ' in an external field; they move from weak to strong field — ' + T('weakly attracted'))
d.basic('Explain paramagnetism.', 'Atoms have ' + T('permanent dipole moments') + ', randomised by thermal motion (no net M). A strong field at low temperature ' + T('aligns') + ' them along B₀')
d.cloze('Paramagnetic examples: {{c1::aluminium, sodium, calcium, oxygen (at STP) and copper chloride}}.')
d.basic('Mnemonic: paramagnetic examples?', '“' + T('Al') + 'l ' + T('Na') + 'ughty ' + T('Ca') + 'ts ' + T('O') + 'ften ' + T('C') + 'hew ' + T('C') + 'hillies” — Al, Na, Ca, O₂, CuCl₂')
d.basic('How does a paramagnet’s magnetisation change with field and temperature?', 'Increases with ' + T('stronger field') + ' and ' + T('lower temperature') + ', until ' + T('saturation') + ' (all dipoles aligned)')
d.basic('Teacher addition: Curie’s law?', r'\( \chi = \dfrac{C\mu_0}{T} \)' + ' — paramagnetic susceptibility ∝ 1/T (dia- and ferromagnetic χ don’t follow this)')
d.basic('Oxygen vs nitrogen at STP: magnetic nature?', 'O₂ ' + T('paramagnetic') + '; N₂ ' + X('diamagnetic') + ' (liquid O₂ sticks between magnet poles; liquid N₂ doesn’t)')
d.basic('Water and copper: magnetic nature? Copper chloride?', 'Water and Cu: ' + X('diamagnetic') + '. CuCl₂: ' + T('paramagnetic') + ' (Cu²⁺ has an unpaired electron)')

d.sec('5.5.3-ferromagnetism')
d.basic('What are ferromagnetic substances?', 'Substances ' + T('strongly magnetised') + ' in a field, strongly attracted, moving towards strong field')
d.basic('What is a magnetic domain? Typical size and atoms?', 'A region where atomic moments ' + T('align spontaneously') + ' (a quantum cooperative effect); ~' + N('1 mm') + ', ~' + N('10¹¹ atoms'))
d.basic('What happens to domains in an external field B₀?', 'Domains ' + T('rotate') + ' towards B₀, and those along B₀ ' + T('grow') + ', merging into one giant domain', **fig('fig_5_8_domains'))
d.basic('Why does an unmagnetised iron bar show no magnetisation?', 'Its domains point in ' + T('random directions') + ', so their moments cancel', **img('fig_5_8_domains'))
d.basic('Are domains real? How are they seen?', T('Yes') + ': sprinkle a liquid suspension of ferromagnetic powder and watch its motion under a ' + T('microscope'))
d.basic('Hard vs soft ferromagnets?', T('Hard') + ': magnetisation persists after the field is removed (permanent magnets). ' + T('Soft') + ': it disappears (electromagnet cores)')
d.basic('Examples of hard and soft ferromagnetic materials?', 'Hard: ' + E('Alnico') + ' (Fe, Al, Ni, Co, Cu), ' + E('lodestone') + '. Soft: ' + E('soft iron'))
d.basic('Use of hard ferromagnets named by NCERT?', 'Permanent magnets, e.g. a ' + T('compass needle'))
d.cloze('Ferromagnetic elements: {{c1::iron, cobalt, nickel, gadolinium}}; their μᵣ is {{c2::> 1000}}.')
d.basic('Effect of heating a ferromagnet?', 'Domains disintegrate and it becomes ' + T('paramagnetic') + ' at high enough temperature; the loss of magnetisation is gradual')
d.basic('Teacher addition: Curie temperature? Susceptibility above it?', 'T_C: temperature above which a ferromagnet turns paramagnetic; above it ' + r'\( \chi = \dfrac{C}{T - T_C} \)' + ' (Curie–Weiss). Iron ≈ ' + N('1043 K'))
d.basic('Intuition: why do soft iron cores make strong electromagnets?', 'Huge μᵣ: domains line up with H and add μ₀M ≫ μ₀H; being soft, they ' + T('switch off') + ' when the current stops')
quadrant_card(d, 'Classification', 'Fill each class.', [
    ('Diamagnetic', 'χ < 0, repelled, Bi Cu water'), ('Paramagnetic', 'χ small +, weakly attracted, Al O₂'),
    ('Ferromagnetic', 'χ ≫ 1, domains, Fe Co Ni'), ('Superconductor', 'χ = −1, perfect diamagnet')],
    'Only ferro- has domains; only para- follows χ ∝ 1/T', 'Magnetic materials at a glance', 'Dia (χ<0), para (small +), ferro (≫1), superconductor (−1)')

# ---------------------------------------------------------------- Points to ponder
d.sec('points-to-ponder')
d.basic('Points to ponder: what does the compass teach about science and engineering?', 'Magnets were used for ~' + N('2000 years') + ' before magnetism was understood (after 1800) — understanding is ' + X('not a precondition') + ' for applications')
d.basic('Consequence of the non-existence of magnetic monopoles?', 'Magnetic field lines are ' + T('continuous closed loops'))
d.basic('Typical χ of diamagnetic vs paramagnetic materials?', '≈ ' + N('−10⁻⁵') + ' vs ' + N('+10⁻⁵') + ' — a tiny difference, radically different behaviour')
d.basic('Other magnetic classes beyond dia-, para- and ferro-?', T('Ferrimagnetic') + ', ' + T('antiferromagnetic') + ', spin glass, …')
d.basic('Dimensions of μ₀ and of B?', 'μ₀: [MLT⁻²A⁻²]; B: [MT⁻²A⁻¹]')
d.basic('Correction: NCERT’s table gives the magnetic moment’s dimensions as [L⁻²A]. Right?', X('Typo') + ': m = IA, so [' + T('L²A') + '] (unit A m²)')
d.basic('Correction: the Gauss box says he built the first electric telegraph with “Wilhelm Welser”. Who?', T('Wilhelm Weber') + ' (Gauss–Weber telegraph, Göttingen, 1833); the SI unit of flux is named after him')
d.basic('Magnetic flux: unit, dimensions?', T('Weber') + ' (Wb = T m²); [ML²T⁻²A⁻¹]')
d.basic('Note: are Earth’s magnetism and hysteresis in this chapter now?', X('No') + ': they were removed in the rationalised NCERT, but some state boards and older papers still ask them')

# ---------------------------------------------------------------- Exercises
d.sec('exercises')
d.basic('Exercise 5.1: bar magnet at 30° to B = 0.25 T feels τ = 4.5 × 10⁻² J. m?', 'm = τ/(B sin 30°) = ' + N('0.36 J/T'))
d.basic('Exercise 5.2: m = 0.32 J/T in B = 0.15 T. Stable and unstable orientations and energies?', 'Stable: m ∥ B, U = −mB = ' + N('−4.8 × 10⁻² J') + '. Unstable: m antiparallel, U = ' + N('+4.8 × 10⁻² J'))
d.basic('Exercise 5.3: 800 turns, A = 2.5 × 10⁻⁴ m², 3.0 A. In what sense is it a bar magnet? m?', 'Same field pattern and it aligns with an external field, with m along the axis (right-hand rule); m = NIA = ' + N('0.60 J/T'))
d.basic('Exercise 5.4: that solenoid at 30° to a horizontal B = 0.25 T. Torque?', 'τ = mB sin 30° = 0.6 × 0.25 × 0.5 = ' + N('7.5 × 10⁻² N m'))
d.basic('Correction: NCERT Exercise 5.4 refers to “the solenoid in Exercise 5.5”. Which one?', T('Exercise 5.3') + ' (m = 0.60 J/T); 5.5 is about a bar magnet')
steps_card(d, 'Exercise 5.5 · turning a magnet', 'Find the missing step.', 'm = 1.5 J/T aligned with B = 0.22 T. Work to turn it (i) normal to B, (ii) opposite to B; torque in each case?',
           ['W = mB(cos θ₁ − cos θ₂), with θ₁ = 0', '(i) θ₂ = 90°: W = mB = <b>0.33 J</b>', '(ii) θ₂ = 180°: W = 2mB = <b>0.66 J</b>',
            'τ = mB sin θ: (i) <b>0.33 N m</b>, (ii) <b>0</b> (unstable equilibrium)'], 2,
           'Work to rotate a bar magnet (Exercise 5.5)', 'W = 0.33 J and 0.66 J; τ = 0.33 N m and 0')
d.basic('Exercise 5.6: 2000 turns, A = 1.6 × 10⁻⁴ m², 4.0 A; B = 7.5 × 10⁻² T at 30° to the axis. m, force, torque?', 'm = ' + N('1.28 A m²') + '; force ' + N('0') + ' (uniform B); τ = mB sin 30° = ' + N('4.8 × 10⁻² N m'))
d.basic('Exercise 5.7: m = 0.48 J/T. B at 10 cm on the axis and on the equator?', 'Axis: 10⁻⁷ × 2 × 0.48/10⁻³ = ' + N('0.96 G') + ' (9.6 × 10⁻⁵ T) along S → N. Equator: ' + N('0.48 G') + ', N → S (opposite to m)')

# ---------------------------------------------------------------- Summary
d.sec('summary')
table_card(d, 'Summary', 'Formula?', [
    ('Torque on dipole', 'τ = m × B', False), ('Energy of dipole', 'U = −m·B', False), ('Axial field', 'μ₀2m/4πr³', False),
    ('Equatorial field', '−μ₀m/4πr³', False), ('Gauss’s law', '∮B·dS = 0', False), ('Magnetisation', 'M = m_net/V', False),
    ('B from H, M', 'B = μ₀(H + M)', False), ('Susceptibility', 'χ = M/H', False), ('Permeability', 'μ = μ₀(1 + χ)', False)],
    term='Chapter 5 formula sheet')
table_card(d, 'Concept checks', 'True or false?', [
    ('A bar magnet in a uniform B feels a net force', 'False (torque only)', True), ('Magnetic flux through a closed surface can be non-zero', 'False', True),
    ('Diamagnets are repelled by magnets', 'True', False), ('Paramagnetic χ rises when cooled', 'True', False),
    ('Soft iron makes good permanent magnets', 'False (hard magnets do)', True), ('Superconductors have μᵣ = 0', 'True', False)],
    term='Chapter 5 concept checks')

print(d.write(os.path.join(OUT, 'deck.json')), 'cards')
