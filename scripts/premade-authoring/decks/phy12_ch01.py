import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Physics', 'class12-physics-ch01-electric-charges-and-fields')
d = Deck('Chapter 1: Electric Charges and Fields', 'Class 12', ['class-12', 'physics', 'ch-1'])
d.description = 'Charge and its properties, Coulomb’s law, superposition, electric field and field lines, flux, dipoles, Gauss’s law and its applications'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- 1.1 Introduction
d.sec('1.1-introduction')
d.basic('Why do you get a shock touching a car door after sliding off the seat?', T('Discharge') + ' through your body of charge built up by rubbing of insulating surfaces (static electricity)')
d.basic('What does electrostatics study?', 'Forces, fields and potentials arising from ' + T('static charges'))

# ---------------------------------------------------------------- 1.2 Electric charge
d.sec('1.2-electric-charge')
d.basic('Who first noticed that rubbed amber attracts light objects? Origin of the word “electricity”?', T('Thales of Miletus') + ', about 600 BC; from Greek ' + I('elektron') + ' = amber')
d.basic('Glass rod rubbed with silk vs plastic rod rubbed with fur: what do they do to each other?', T('Attract') + ' (unlike charges); two glass rods or two plastic rods ' + T('repel'), **fig('fig_1_1_rods'))
d.cloze('Like charges {{c1::repel}}; unlike charges {{c2::attract}}. The property that distinguishes the two kinds of charge is called {{c3::polarity}}.')
d.basic('Who named charges positive and negative? Why those names?', T('Benjamin Franklin') + ': the two kinds ' + T('cancel') + ' each other when brought in contact, like + and − numbers')
table_card(d, 'Convention', 'Sign of charge?', [
    ('Glass rod (rubbed with silk)', 'positive', False), ('Silk', 'negative', True),
    ('Plastic rod (rubbed with fur)', 'negative', True), ('Cat’s fur', 'positive', False)], term='Frictional electricity: signs by convention')
d.basic('Identify this device and how it shows charge.', T('Gold-leaf electroscope') + ': charge flows down the rod to the leaves, which ' + T('diverge') + '; divergence indicates the amount of charge', **img('fig_1_2_electroscope'))
d.occlusion('Figure 1.2(a) · Gold-leaf electroscope', M + 'fig_1_2_electroscope.webp', (860, 1001), [
    ('Metal knob', pad([302, 30, 180, 36], 4), True),
    ('Metal rod', pad([305, 76, 152, 36], 4), True),
    ('Rubber (insulating stopper)', pad([268, 174, 120, 36], 4), False),
    ('Glass window', pad([108, 408, 124, 62], 4), True),
    ('Gold leaves', pad([275, 408, 180, 38], 4), True),
], guess='hide-all')
d.basic('What actually moves when a glass rod is rubbed with silk?', T('Electrons') + ' move from the rod to the silk: rod becomes +, silk −. No charge is created')
d.basic('Which everyday forces are basically electrical?', 'Forces holding atoms and molecules together, ' + E('glue adhesion') + ', ' + E('surface tension') + ', contact forces, friction')
d.basic('Does rubbing transfer a large share of a body’s electrons?', X('No') + ': only a very small fraction of the electrons is transferred')

# ---------------------------------------------------------------- 1.3 Conductors and insulators
d.sec('1.3-conductors-and-insulators')
d.basic('Conductors vs insulators?', T('Conductors') + ': charges (electrons) move freely — ' + E('metals, human body, earth') + '<br>' + T('Insulators') + ': high resistance — ' + E('glass, porcelain, plastic, nylon, wood'))
d.basic('Charge given to a conductor vs an insulator: where does it go?', 'Conductor: spreads over the whole ' + T('surface') + '. Insulator: ' + T('stays where it was put'))
d.basic('Why does a metal spoon held in the hand not get charged on rubbing?', 'The charge ' + T('leaks through your body to earth') + ' (both conductors); with an insulating handle it does charge')
d.basic('What is the third category besides conductors and insulators?', T('Semiconductors') + ': resistance intermediate between the two')
d.basic('Mobile charges in metals vs electrolytes?', 'Metals: ' + T('electrons') + '. Electrolytes: both ' + T('positive and negative ions'))

# ---------------------------------------------------------------- 1.4 Properties of charge
d.sec('1.4-basic-properties-of-charge')
d.basic('When can a charged body be treated as a point charge?', 'When its size is ' + T('very small compared with the distances') + ' involved')
d.cloze('Three basic properties of electric charge: {{c1::additivity}}, {{c2::conservation}} and {{c3::quantisation}}.')
d.basic('Additivity of charge: how is it like mass, and how is it unlike mass?', 'Like mass: a ' + T('scalar') + ' that adds algebraically. Unlike mass: charge can be ' + X('negative') + ', so signs matter')
d.basic('Total charge of +1, +2, −3, +4, −5 (same units)?', N('−1'))
d.basic('State conservation of charge.', 'The total charge of an ' + T('isolated system') + ' never changes.<br>Charge carriers can be created or destroyed only in equal and opposite pairs')
d.basic('A neutron decays into a proton and an electron. Is charge conserved?', 'Yes: 0 = (+e) + (−e)')
d.basic('State quantisation of charge.', r'\( q = ne \)' + ', n an integer: every free charge is an ' + T('integral multiple of e'))
d.basic('Who suggested and who demonstrated quantisation of charge?', 'Suggested by ' + T('Faraday') + '’s laws of electrolysis; demonstrated by ' + T('Millikan') + ' (' + N('1912') + ', oil-drop experiment)')
d.basic('Value of e (NCERT) and number of electrons in 1 C?', 'e = ' + N('1.602192 × 10⁻¹⁹ C') + '; about ' + N('6 × 10¹⁸') + ' electrons in −1 C')
d.basic('Update: is e still a measured constant in SI?', X('No') + ': since the ' + T('2019 SI redefinition') + ', e is fixed exactly at ' + N('1.602176634 × 10⁻¹⁹ C') + '. Use 1.6 × 10⁻¹⁹ C in problems')
d.basic('Define 1 coulomb (via current).', 'Charge flowing through a wire in ' + N('1 s') + ' when the current is ' + N('1 A') + ': 1 C = 1 A s')
d.basic('Why can quantisation be ignored for macroscopic charges?', '1 μC ≈ ' + N('10¹³ e') + ': steps of e are too tiny to notice, so charge looks continuous (like a dotted line from far away)')
d.basic('Update: quarks carry ±e/3 and ±2e/3. Does this break q = ne?', X('Not for free charges') + ': quarks are always confined inside hadrons, so every observed free charge is still a multiple of e')
d.basic('Example 1.1: 10⁹ electrons leave a body every second. Time to collect 1 C?', '1 / (1.6 × 10⁻¹⁰ C/s) = 6.25 × 10⁹ s ≈ ' + N('200 years') + ': 1 C is a huge unit')
d.basic('Example 1.2: total positive (and negative) charge in a cup of water (250 g)?', '(250/18) × 6.02 × 10²³ × 10 × 1.6 × 10⁻¹⁹ ≈ ' + N('1.34 × 10⁷ C') + ' (10 protons, 10 electrons per molecule)')
d.basic('Roughly how many electrons in a 1 cm³ copper cube?', 'About ' + N('2.5 × 10²⁴'))
d.basic('Exercise 1.11: polythene rubbed with wool gets −3 × 10⁻⁷ C. Electrons transferred? Mass transferred?', N('1.9 × 10¹²') + ' electrons, from ' + T('wool to polythene') + '. Yes, mass is transferred, but only ~' + N('2 × 10⁻¹⁸ kg') + ' (negligible)')
d.basic('Exercise 1.5: glass rubbed with silk — how is charging consistent with conservation?', 'Electrons are only ' + T('transferred') + ': the rod’s + charge exactly equals the silk’s − charge; the total stays zero')

# ---------------------------------------------------------------- 1.5 Coulomb's law
d.sec('1.5-coulombs-law')
d.basic('State Coulomb’s law.', 'Force between two point charges ∝ ' + T('product of charges') + ', ∝ ' + T('1/r²') + ', along the line joining them: ' + r'\( F = \dfrac{1}{4\pi\varepsilon_0}\dfrac{|q_1 q_2|}{r^2} \)')
d.basic('What instrument did Coulomb use? Who else used it?', 'A ' + T('torsion balance') + '; later ' + T('Cavendish') + ' used one to measure gravitational force')
d.basic('Coulomb did not know the charges. How did he vary them?', 'By touching a charged sphere with an ' + T('identical uncharged sphere') + ': charge halves each time (q/2, q/4…)<br>This relies on additivity and conservation of charge')
d.basic('Values of k and ε₀?', r'\( k = \dfrac{1}{4\pi\varepsilon_0} \approx 9\times10^{9} \)' + ' N m² C⁻²' + '; ε₀ = ' + N('8.854 × 10⁻¹² C² N⁻¹ m⁻²'))
d.basic('What is ε₀ called?', T('Permittivity of free space'))
d.basic('Force between two 1 C charges 1 m apart in vacuum?', N('9 × 10⁹ N') + ' — why 1 C is far too big for electrostatics (use μC, mC)')
d.basic('Vector form of Coulomb’s law: force on q₂ due to q₁?', r'\( \vec F_{21} = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q_1q_2}{r_{21}^2}\,\hat r_{21} \)' + ', with ' + r'\( \hat r_{21} \)' + ' pointing from 1 to 2', **fig('fig_1_3_coulomb_vectors'))
d.basic('Why does the vector form need no separate formula for attraction?', 'If q₁q₂ < 0, F₂₁ points along ' + r'\( -\hat r_{21} \)' + ' (towards q₁): the sign of q₁q₂ handles it')
d.basic('Does Coulomb’s law obey Newton’s third law?', 'Yes: ' + r'\( \vec F_{12} = -\vec F_{21} \)')
d.basic('Down to what distance has Coulomb’s law been verified?', 'Subatomic distances, ' + N('r ~ 10⁻¹⁰ m') + ' (and below)')
d.basic('Charles Augustin de Coulomb: nationality, first career, year of the law?', T('French') + ' physicist, earlier a ' + T('military engineer') + ' (West Indies); inverse-square law in ' + N('1785'))
d.basic('Who anticipated Coulomb’s law?', T('Priestley') + ' and ' + T('Cavendish') + ' (Cavendish never published)')
d.basic('Example 1.3: ratio of electric to gravitational force, electron–proton? proton–proton?', r'\( \dfrac{e^2}{4\pi\varepsilon_0 G m_e m_p} \approx 2.4\times10^{39} \)' + '; for two protons ≈ ' + N('1.3 × 10³⁶') + ' — independent of distance')
d.basic('Example 1.3(b): accelerations of an electron and a proton 1 Å apart (mutual attraction)?', 'F = ' + N('2.3 × 10⁻⁸ N') + '; aₑ ≈ ' + N('2.5 × 10²² m/s²') + ', aₚ ≈ ' + N('1.4 × 10¹⁹ m/s²') + ' — gravity is negligible')
d.basic('Force between two protons inside a nucleus (~10⁻¹⁵ m apart)? Why don’t they fly apart?', 'Fₑ ≈ ' + N('230 N') + ' (F_G ~ 10⁻³⁴ N); the ' + T('strong nuclear force') + ' (range ~10⁻¹⁴ m) holds them')
d.basic('Why does gravity dominate large scales if it is 10³⁹ times weaker?', 'Gravity is ' + T('always attractive') + '; electric forces come in both signs and ' + T('cancel') + ' in neutral matter')
d.basic('Example 1.4: charges on A and B are both halved by touching identical neutral spheres, and the separation is halved. New force?', T('Unchanged') + ': (¼)/(¼) = 1')
steps_card(d, 'Exercise 1.12 · scaling', 'Find the missing step.', 'Two spheres each 6.5 × 10⁻⁷ C, 50 cm apart. Force? Then each charge doubled and distance halved?',
           ['F = 9 × 10⁹ × (6.5 × 10⁻⁷)² / 0.5²', 'F = <b>1.5 × 10⁻² N</b>', 'Doubling both charges → ×4; halving r → ×4',
            'New F = 16 × 1.5 × 10⁻² = <b>0.24 N</b>'], 2, 'Coulomb force scaling (Exercise 1.12)', 'F = 1.5 × 10⁻² N; with 2q, 2q and r/2 the force becomes 16F = 0.24 N')
d.basic('Exercise 1.1: 2 × 10⁻⁷ C and 3 × 10⁻⁷ C, 30 cm apart in air. Force?', N('6 × 10⁻³ N') + ', repulsive')
d.basic('Exercise 1.2: 0.4 μC and −0.8 μC attract with 0.2 N. Separation? Force on the second?', 'r = ' + N('12 cm') + '; 0.2 N, ' + T('attractive') + ' (towards the first) — Newton’s third law')
d.basic('Exercise 1.3: what does the dimensionless ratio ke²/(G mₑ mₚ) ≈ 2.3 × 10³⁹ signify?', 'Electric force between an electron and proton is ~10³⁹ times the ' + T('gravitational force') + ' between them, at any distance')
d.basic('Points to ponder: why is k so large (why is 1 C so big)?', 'The coulomb is defined through the ' + T('ampere') + ' (magnetic effects, which are much weaker than electric ones).<br>1 A is a sensible current, but 1 C = 1 A s is huge electrically')
d.basic('Update: NCERT says the ampere is defined via the force between current-carrying wires. Still true?', X('Not since 2019') + ': the SI now fixes ' + T('e exactly') + '.<br>The ampere (and coulomb) follow from e.<br>k ≈ 8.99 × 10⁹ N m² C⁻² is unchanged')

# ---------------------------------------------------------------- 1.6 Multiple charges
d.sec('1.6-forces-between-multiple-charges')
d.basic('State the principle of superposition (forces).', 'Force on a charge = ' + T('vector sum') + ' of the forces from each other charge taken ' + T('one at a time') + '.<br>Each force is unaffected by the presence of the others', **fig('fig_1_5_superposition'))
d.basic('Points to ponder: superposition says two things beyond “add vectors”. What?', '(1) Each pair force is ' + T('unaffected') + ' by other charges; (2) there are ' + X('no extra three-body') + ' (or more) forces')
d.basic('“All of electrostatics is basically a consequence of…”?', T('Coulomb’s law') + ' and the ' + T('superposition principle'))
d.basic('Example 1.5: equal charges q at the corners of an equilateral triangle. Force on Q at the centroid?', N('Zero') + ' — by symmetry (rotate the figure by 120°: the answer must not change)', **img('fig_1_6_triangle'))
d.basic('Example 1.6: q, q, −q at the corners of an equilateral triangle. Net force on each? Sum of all three?', 'F on each q, ' + N('√3 F') + ' on −q (F = q²/4πε₀l²); the three forces add to ' + N('zero') + ' (Newton’s third law)', **fig('fig_1_7_triangle_qqq'))
d.basic('Exercise 1.6: +2, −5, +2, −5 μC at corners A, B, C, D of a 10 cm square. Force on 1 μC at the centre?', N('Zero') + ': equal charges at opposite corners cancel in pairs')

# ---------------------------------------------------------------- 1.7 Electric field
d.sec('1.7-electric-field')
d.basic('Define electric field at a point.', 'Force per unit positive test charge: ' + r'\( \vec E = \lim_{q\to0}\dfrac{\vec F}{q} \)')
d.basic('Why take the limit q → 0 for the test charge?', 'So the test charge does ' + T('not disturb the source charges') + '; F/q stays finite')
d.basic('Field of a point charge Q?', r'\( \vec E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{Q}{r^2}\hat r \)' + ': radially outward for +Q, inward for −Q', **fig('fig_1_8_point_field'))
d.basic('SI unit of electric field (two forms)?', N('N C⁻¹') + ' = ' + N('V m⁻¹'))
d.basic('Source charge vs test charge?', T('Source') + ': produces the field. ' + T('Test') + ': small charge used to detect it')
d.basic('Does the field of Q depend on the test charge q?', X('No') + ': F ∝ q, so F/q is independent of q; E depends only on position')
d.basic('What symmetry does the field of a point charge have?', T('Spherical') + ': |E| is the same everywhere on a sphere centred on the charge')
d.basic('Field due to a system of charges?', 'Vector sum: ' + r'\( \vec E(\vec r) = \dfrac{1}{4\pi\varepsilon_0}\sum_i \dfrac{q_i}{r_{iP}^2}\hat r_{iP} \)', **fig('fig_1_9_system_field'))
d.basic('Physical significance: why are fields “real” and not just a device?', 'Beyond electrostatics, effects travel at speed ' + T('c') + '.<br>Fields account for the ' + T('time delay') + ', carry energy and have their own dynamics')
d.basic('Who introduced the concept of field?', T('Faraday'))
d.basic('Example 1.7: electron and proton each fall 1.5 cm in a 2 × 10⁴ N/C field. Times of fall?', 'tₑ = ' + N('2.9 × 10⁻⁹ s') + ', tₚ = ' + N('1.3 × 10⁻⁷ s') + ' (t = √(2hm/eE))', **fig('fig_1_10_fall'))
d.basic('Example 1.7: how does fall in an electric field differ from free fall under gravity?', 'Time depends on ' + T('mass') + ' (a = eE/m): the heavier proton takes longer. In free fall, time is independent of mass')
d.basic('Why can gravity be ignored in Example 1.7?', 'aₚ = eE/mₚ ≈ ' + N('1.9 × 10¹² m/s²') + ' ≫ g')
steps_card(d, 'Example 1.8 · two charges', 'Find the missing step.', '+10⁻⁸ C and −10⁻⁸ C, 0.1 m apart. Field at A, midway between them?',
           ['Each charge is 0.05 m from A', 'E from each = 9 × 10⁹ × 10⁻⁸ / 0.05² = 3.6 × 10⁴ N/C',
            'Both point from + towards −, so they add', 'E<sub>A</sub> = <b>7.2 × 10⁴ N/C</b>, towards the negative charge'], 2,
           'Field midway between +q and −q (Example 1.8)', 'Both fields point towards −q and add: 7.2 × 10⁴ N/C')
d.basic('Example 1.8: fields at B (5 cm outside the + charge) and C (0.1 m from both)?', 'E_B = 3.6 × 10⁴ − 0.4 × 10⁴ = ' + N('3.2 × 10⁴ N/C') + ' away from the pair<br>E_C = ' + N('9 × 10³ N/C') + ' parallel to the line (+ to −)', **img('fig_1_11_example'))
d.basic('Exercise 1.8: +3 μC and −3 μC, 20 cm apart. Field at the midpoint? Force on −1.5 × 10⁻⁹ C there?', 'E = ' + N('5.4 × 10⁶ N/C') + ' towards the negative charge; F = ' + N('8.1 × 10⁻³ N') + ' towards the positive charge')

# ---------------------------------------------------------------- 1.8 Field lines
d.sec('1.8-electric-field-lines')
d.basic('Define an electric field line.', 'A curve whose ' + T('tangent at each point') + ' gives the direction of the net field there (arrow gives the sense)')
d.basic('How do field lines show field strength?', 'By their ' + T('density') + ' (lines per unit area normal to them): crowded = strong, spread out = weak', **fig('fig_1_13_density'))
d.basic('Why is the number of field lines crossing any sphere around a point charge the same?', 'E ∝ 1/r² while the area ∝ r²: lines per area fall as 1/r².<br>The field-line picture ' + T('builds in the inverse-square law'))
d.basic('Define solid angle.', r'\( \Delta\Omega = \Delta S/r^2 \)' + ' (area on a sphere ÷ radius²); unit steradian')
d.basic('What did Faraday call field lines? Why is the modern name better?', '“' + T('Lines of force') + '” — misleading, especially for magnetic fields; “field lines” is preferred')
d.cloze('Field lines start on {{c1::positive}} charges and end on {{c2::negative}} charges (or at infinity for a single charge).')
d.basic('Why can two field lines never cross?', 'The field at the crossing would have ' + X('two directions') + ' — impossible, E is unique')
d.basic('Why can’t electrostatic field lines form closed loops?', 'The electrostatic field is ' + T('conservative') + ' (Chapter 2)')
d.basic('Exercise 1.7(a): why can’t a field line have sudden breaks?', 'A break would mean E suddenly vanishes; in a ' + T('charge-free region E varies continuously') + ', so lines are continuous')
d.basic('What do field lines look like in a uniform field?', T('Equally spaced parallel straight lines'))
d.basic('Identify: field lines of which configuration?', T('Positive point charge') + ' (q > 0): radially outward', **img('fig_1_14a_pos'))
d.basic('Identify: field lines of which configuration?', T('Negative point charge') + ' (q < 0): radially inward', **img('fig_1_14b_neg'))
d.basic('Identify: field lines of which configuration? What does it show?', T('Two equal positive charges') + ': lines bend away, a ' + T('neutral point') + ' midway — pictures repulsion', **img('fig_1_14c_like'))
d.basic('Identify: field lines of which configuration? What does it show?', T('Electric dipole') + ' (+q, −q): lines go from + to −, picturing attraction', **img('fig_1_14d_dipole'))
d.basic('Is a field line the path a charge follows?', X('Not in general') + ': it gives the direction of force (acceleration), not velocity. Only a charge released from rest in straight field lines follows the line')
d.basic('Exercise 1.13 (Fig 1.30): signs of the three particles? Largest q/m?', '1 and 2 bend towards the + plate → ' + T('negative') + '<br>3 bends towards − → ' + T('positive') + '<br>Particle ' + N('3') + ' deflects most → largest q/m', **img('fig_1_30_tracks'))

# ---------------------------------------------------------------- 1.9 Electric flux
d.sec('1.9-electric-flux')
d.basic('Define electric flux through a small area.', r'\( \Delta\phi = \vec E\cdot\Delta\vec S = E\,\Delta S\cos\theta \)' + ', θ between E and the normal', **fig('fig_1_15_flux_tilt'))
d.basic('What does flux measure pictorially?', 'The ' + T('number of field lines') + ' crossing the area (proportional to, not equal to)')
d.basic('Direction of an area vector? For a closed surface?', 'Along the ' + T('normal') + '; for a closed surface, the ' + T('outward normal'), **fig('fig_1_16_normal'))
d.basic('When is the flux through a flat area zero?', 'When E is ' + T('parallel to the surface') + ' (θ = 90° with the normal)')
d.basic('Unit and dimensions of electric flux?', N('N C⁻¹ m²') + ' = ' + N('V m') + '; [ML³T⁻³A⁻¹]')
d.basic('Liquid flux analogy: what is different about electric flux?', X('Nothing physical actually flows') + ' in electric flux')
d.basic('Exercise 1.14: E = 3 × 10³ î N/C through a 10 cm square. Flux if the plane is parallel to yz? If the normal is at 60° to x?', N('30 N m²/C') + '; ' + N('15 N m²/C') + ' (× cos 60°)')
d.basic('Exercise 1.15: flux of the same uniform field through a 20 cm cube?', N('Zero') + ': what enters one face leaves the opposite one')

# ---------------------------------------------------------------- 1.10 Electric dipole
d.sec('1.10-electric-dipole')
d.basic('Define an electric dipole and its dipole moment.', 'Charges +q and −q separated by 2a; ' + r'\( \vec p = q\times 2a\,\hat p \)' + ', directed ' + T('from −q to +q'))
d.basic('Unit and dimensions of dipole moment?', N('C m') + '; [LTA]')
d.basic('Total charge of a dipole is zero. Is its field zero?', X('No') + ': the charges are separated, so their fields don’t cancel exactly; far away it falls as ' + T('1/r³'))
d.basic('Dipole field on the axis (exact and r ≫ a)?', r'\( E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{4qar}{(r^2-a^2)^2} \to \dfrac{1}{4\pi\varepsilon_0}\dfrac{2p}{r^3} \)' + ', along p', **fig('fig_1_17_dipole'))
d.basic('Dipole field on the equatorial plane (exact and r ≫ a)?', r'\( E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{p}{(r^2+a^2)^{3/2}} \to \dfrac{1}{4\pi\varepsilon_0}\dfrac{p}{r^3} \)' + ', ' + X('opposite to p'))
d.basic('Mnemonic: axial vs equatorial dipole field at the same large r?', '“' + T('Axis is double, equator is reversed') + '”: E_axial = 2 E_equatorial, and the equatorial field points opposite to p')
d.basic('Why does the dipole field fall as 1/r³ instead of 1/r²?', 'Far away the +q and −q fields ' + T('nearly cancel') + '.<br>Only their small difference (∝ separation/r) survives, adding one more power of r')
d.basic('What is a point dipole?', '2a → 0 and q → ∞ with p = 2qa finite; the r ≫ a formulas become ' + T('exact for all r'))
d.basic('Polar vs non-polar molecules?', T('Polar') + ': permanent dipole moment, e.g. ' + E('H₂O') + '<br>' + T('Non-polar') + ': centres of + and − coincide, e.g. ' + E('CO₂, CH₄') + ' (they get induced dipoles in a field)')
d.basic('Example 1.9: ±10 μC, 5 mm apart. Field 15 cm away on the axis and on the equatorial line?', 'Axis: ' + N('2.6 × 10⁵ N/C') + ' along p. Equator: ' + N('1.33 × 10⁵ N/C') + ' opposite to p (exact and r ≫ a answers agree since r/a = 60)')
d.basic('Exercise 1.9: +2.5 × 10⁻⁷ C at (0, 0, −15 cm), −2.5 × 10⁻⁷ C at (0, 0, +15 cm). Total charge and dipole moment?', 'Total ' + N('0') + '; p = 2.5 × 10⁻⁷ × 0.30 = ' + N('7.5 × 10⁻⁸ C m') + ' along ' + T('−z') + ' (− to +)')

# ---------------------------------------------------------------- 1.11 Dipole in uniform field
d.sec('1.11-dipole-in-uniform-field')
d.basic('Dipole in a uniform field: net force and torque?', 'Net force ' + N('zero') + '; torque ' + r'\( \vec\tau = \vec p\times\vec E \)' + ', |τ| = pE sin θ', **fig('fig_1_19_dipole_uniform'))
d.basic('What does the torque on a dipole try to do? When is it zero?', 'Align ' + T('p along E') + '; zero when p ∥ E or antiparallel')
d.basic('Dipole in a non-uniform field with p ∥ E or antiparallel: net force?', 'p ∥ E: force towards ' + T('increasing field') + '. p antiparallel: towards ' + T('decreasing field') + '. Torque zero in both', **fig('fig_1_20_dipole_nonuniform'))
d.basic('Why does a charged comb attract uncharged bits of paper?', 'The comb ' + T('polarises') + ' the paper (induced dipole along E).<br>Its field is ' + T('non-uniform') + ', so the dipole is pulled towards the stronger field: the comb')
d.basic('Exercise 1.10: p = 4 × 10⁻⁹ C m at 30° to E = 5 × 10⁴ N/C. Torque?', 'τ = pE sin 30° = ' + N('10⁻⁴ N m'))

# ---------------------------------------------------------------- 1.12 Continuous distributions
d.sec('1.12-continuous-charge-distribution')
table_card(d, 'Fig. 1.21 · charge densities', 'Definition and unit?', [
    ('Linear λ', 'ΔQ/Δl, C m⁻¹', False), ('Surface σ', 'ΔQ/ΔS, C m⁻²', False), ('Volume ρ', 'ΔQ/ΔV, C m⁻³', False)],
    term='Linear, surface and volume charge densities')
d.basic('Identify the three kinds of charge distribution shown.', T('Line') + ' (ΔQ = λΔl), ' + T('surface') + ' (ΔQ = σΔS), ' + T('volume') + ' (ΔQ = ρΔV)', **img('fig_1_21_densities'))
d.basic('How small is the element ΔS used to define σ?', 'Small ' + T('macroscopically') + ' but large enough to contain very many ' + T('microscopic') + ' charges.<br>σ is a smoothed average that ignores quantisation')
d.basic('Field of a continuous distribution?', r"\( \vec E \approx \dfrac{1}{4\pi\varepsilon_0}\sum \dfrac{\rho\,\Delta V}{r'^2}\hat r' \)" + ' — Coulomb + superposition, an integral in the limit')
d.basic('Points to ponder: where is the electric field undefined or discontinuous?', T('Undefined') + ' at the location of a point charge; ' + T('discontinuous') + ' across a surface charge; defined everywhere inside a volume distribution')

# ---------------------------------------------------------------- 1.13 Gauss's law
d.sec('1.13-gausss-law')
d.basic('Flux through a sphere of radius r around a point charge q at its centre?', r'\( \phi = \dfrac{q}{4\pi\varepsilon_0 r^2}\cdot 4\pi r^2 = \dfrac{q}{\varepsilon_0} \)' + ' — independent of r', **fig('fig_1_22_sphere_flux'))
d.basic('State Gauss’s law.', 'Flux through any closed surface = ' + r'\( \dfrac{q_{enc}}{\varepsilon_0} \)' + ', where q_enc is the total charge enclosed')
d.basic('Uniform field through a closed cylinder with axis along E: net flux?', '−ES (entry face) + ES (exit face) + 0 (curved) = ' + N('0') + ': no enclosed charge', **fig('fig_1_23_cylinder'))
d.basic('Gauss’s law: whose field appears in the flux, and whose charge on the right side?', 'E is due to ' + T('all charges, inside and outside') + '; q counts ' + T('only the charge inside'))
d.basic('What is a Gaussian surface? One restriction on choosing it?', 'Any closed surface used to apply Gauss’s law.<br>It must ' + X('not pass through a discrete point charge') + ' (field undefined there), though it may cut a continuous distribution')
d.basic('When is Gauss’s law useful for finding E?', 'When the charge distribution has ' + T('symmetry') + ' (spherical, cylindrical, planar)')
d.basic('On what property of Coulomb’s law does Gauss’s law rest?', 'The ' + T('inverse-square') + ' dependence; a violation of Gauss’s law would signal a departure from 1/r²')
d.basic('Exercise 1.16(b): zero net flux out of a box. Is there no charge inside?', X('Not necessarily') + ': the ' + T('net') + ' charge is zero; equal + and − charges could be inside')
d.basic('Charge q at the centre of a cube. Flux through one face?', r'\( \dfrac{q}{6\varepsilon_0} \)' + ' by symmetry (Exercise 1.17: +10 μC 5 cm above a 10 cm square → ' + N('1.9 × 10⁵ N m²/C') + ')', **img('fig_1_31_square'))
steps_card(d, 'Example 1.10 · non-uniform field', 'Find the missing step.', 'Eₓ = αx^½ (α = 800 N C⁻¹ m^-½), Eᵧ = E_z = 0. Cube of side a = 0.1 m from x = a to x = 2a. Charge inside?',
           ['Only the two faces normal to x have flux', 'φ = a²(E<sub>R</sub> − E<sub>L</sub>) = αa^(5/2)(√2 − 1)',
            'φ = 800 × (0.1)^2.5 × 0.414 = <b>1.05 N m²/C</b>', 'q = ε₀φ = <b>9.27 × 10⁻¹² C</b>'], 1,
           'Flux of a non-uniform field through a cube (Example 1.10)', 'φ = αa^(5/2)(√2 − 1) = 1.05 N m²/C, q = ε₀φ = 9.27 × 10⁻¹² C')
d.basic('Identify: in Example 1.10, which faces of the cube carry flux, and why?', 'Only the two shaded faces ' + T('normal to x') + ': E has only an x-component', **img('fig_1_24_cube'))
d.basic('Example 1.11: E = +200 î N/C for x > 0 and −200 î for x < 0; cylinder r = 5 cm, faces at x = ±10 cm. Net flux and charge?', 'Each face +' + N('1.57 N m²/C') + ', side 0 → φ = ' + N('3.14 N m²/C') + '; q = ε₀φ = ' + N('2.78 × 10⁻¹¹ C'), **fig('fig_1_25_cylinder_ex'))
d.basic('Exercise 1.16(a): net outward flux 8.0 × 10³ N m²/C. Charge inside?', 'q = ε₀φ ≈ ' + N('7.1 × 10⁻⁸ C') + ' (0.07 μC)')
d.basic('Exercise 1.18: 2.0 μC at the centre of a 9.0 cm cube. Net flux?', 'q/ε₀ ≈ ' + N('2.3 × 10⁵ N m²/C') + ' — cube size is irrelevant')
d.basic('Exercise 1.19: −1.0 × 10³ N m²/C through a 10 cm sphere. With radius doubled? Charge?', 'Still ' + N('−1.0 × 10³ N m²/C') + '; q = ε₀φ ≈ ' + N('−8.8 nC'))

# ---------------------------------------------------------------- 1.14 Applications
d.sec('1.14-applications-of-gausss-law')
d.basic('Field of an infinitely long line charge λ? Gaussian surface?', r'\( E = \dfrac{\lambda}{2\pi\varepsilon_0 r} \)' + ', radial; a ' + T('coaxial cylinder') + ' (flux only through the curved part)', **fig('drawn_line_charge_gauss'))
d.basic('Why must the field of an infinite line charge be radial?', 'Pairs of elements on either side of P cancel each other’s ' + T('components along the wire') + '; only radial parts survive')
d.basic('Why must the wire be “infinitely long” for E = λ/2πε₀r?', 'Otherwise ' + X('end effects') + ' spoil symmetry and E is not normal to the curved surface.<br>The result holds near the middle of a long wire')
d.basic('Field of an infinite plane sheet σ? Gaussian surface?', r'\( E = \dfrac{\sigma}{2\varepsilon_0} \)' + ', normal to the sheet; a ' + T('box or cylinder') + ' piercing the sheet (flux 2EA)', **fig('fig_1_27_sheet'))
d.basic('Intuition: why doesn’t the field of an infinite sheet weaken with distance?', 'Moving away, each patch is farther, but you ' + T('see more of the sheet') + ' at useful angles.<br>The two effects cancel exactly, like a wall of light that never looks dimmer')
d.basic('Field of a uniformly charged thin spherical shell, outside?', r'\( E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r^2} \)' + ' (r ≥ R): as if all charge were at the ' + T('centre'), **fig('fig_1_28_shell'))
d.basic('Field inside a uniformly charged thin spherical shell?', N('Zero') + ' everywhere inside (Gaussian sphere encloses no charge)')
d.basic('Sketch E versus r for a charged spherical shell.', '0 inside, jumps to ' + r'\( q/4\pi\varepsilon_0R^2 \)' + ' at r = R, then falls as 1/r²', **fig('drawn_shell_E_vs_r'))
d.basic('What does the experimental fact “E = 0 inside a charged shell” confirm?', 'The ' + T('1/r² law') + ' of Coulomb (precision tests of the inverse-square law use this)')
d.basic('Does the “charge acts from the centre” result hold for a solid uniformly charged sphere?', 'Yes, for points ' + T('outside') + ' it')
table_card(d, 'Gauss’s law results', 'E?', [
    ('Infinite line charge λ', 'λ / 2πε₀r (∝ 1/r)', False), ('Infinite plane sheet σ', 'σ / 2ε₀ (constant)', False),
    ('Thin shell, outside', 'q / 4πε₀r² (∝ 1/r²)', False), ('Thin shell, inside', '0', True),
    ('Two oppositely charged plates, between', 'σ / ε₀', False), ('Two oppositely charged plates, outside', '0', True)],
    term='Fields from Gauss’s law')
d.basic('Exercise 1.23: two large parallel plates with ±σ on their inner faces (σ = 17.0 × 10⁻²² C/m²). E outside and between?', 'Outside: ' + N('0') + ' (fields of the two sheets cancel); between: σ/ε₀ = ' + N('1.9 × 10⁻¹⁰ N/C'))
d.basic('Example 1.12: atom = point nucleus +Ze with −Ze spread uniformly to radius R. E inside and outside?', r'\( E = \dfrac{Ze}{4\pi\varepsilon_0}\left(\dfrac{1}{r^2} - \dfrac{r}{R^3}\right) \)' + ' for r < R (outward); ' + N('0') + ' for r > R (neutral)', **fig('fig_1_29_atom'))
d.basic('Exercise 1.20: conducting sphere, radius 10 cm; E at 20 cm = 1.5 × 10³ N/C radially inward. Charge?', 'q = Er²/k = ' + N('−6.7 nC') + ' (inward → negative)')
d.basic('Exercise 1.21: sphere of diameter 2.4 m, σ = 80.0 μC/m². Charge and flux leaving?', 'Q = σ·4πR² ≈ ' + N('1.45 × 10⁻³ C') + '; φ = Q/ε₀ ≈ ' + N('1.6 × 10⁸ N m²/C'))
d.basic('Exercise 1.22: line charge gives 9 × 10⁴ N/C at 2 cm. λ?', 'λ = 2πε₀rE = ' + N('10⁻⁷ C/m') + ' (0.1 μC/m)')

# ---------------------------------------------------------------- Points to ponder / corrections
d.sec('points-to-ponder')
d.basic('Charge is a scalar. What extra invariance does it have that kinetic energy lacks?', 'Charge is the same in all ' + T('frames in relative motion') + '; kinetic energy is not')
d.basic('Is every scalar conserved? Is every conserved quantity a scalar?', X('No') + ' to both: KE is a scalar but not conserved in inelastic collisions; ' + E('angular momentum') + ' is a conserved vector')
d.basic('Is there a quantisation law for mass like that for charge?', X('No') + ': charge quantisation is a basic (unexplained) law with no mass analogue')
d.basic('Why can’t electrons sit on top of protons inside the nucleus?', 'The laws of ' + T('quantum mechanics') + ' forbid it; this gives atoms their structure')
d.basic('Correction: NCERT prints “1 mC (micro coulomb) = 10⁻⁶ C” in Section 1.4.3. Right symbol?', T('1 μC') + ' = 10⁻⁶ C (micro); 1 mC = 10⁻³ C (milli) — the μ was lost in typesetting')

d.sec('summary')
table_card(d, 'Summary', 'Formula?', [
    ('Coulomb’s law', 'F = kq₁q₂/r², k = 9 × 10⁹', False), ('Field of a point charge', 'E = kq/r²', False),
    ('Dipole moment', 'p = q × 2a (− to +)', False), ('Dipole field, axis / equator', '2kp/r³ / kp/r³', False),
    ('Torque on a dipole', 'τ = p × E', False), ('Flux', 'φ = E·ΔS', False), ('Gauss’s law', 'φ = q_enc/ε₀', False)],
    term='Chapter 1 formula sheet')
table_card(d, 'Concept checks', 'True or false?', [
    ('Field lines can cross', 'False', True), ('Net force on a dipole in a uniform field is zero', 'True', False),
    ('Zero flux means no charges inside', 'False (net charge zero)', True), ('E inside a charged shell is zero', 'True', False),
    ('A field line is the path of a charge', 'False (in general)', True)], term='Chapter 1 concept checks')

print(d.write(os.path.join(OUT, 'deck.json')), 'cards')
