import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Physics', 'class12-physics-ch02-electrostatic-potential-and-capacitance')
d = Deck('Chapter 2: Electrostatic Potential and Capacitance', 'Class 12', ['class-12', 'physics', 'ch-2'])
d.description = 'Potential and potential energy, dipole potential, equipotentials, E from V, conductors, dielectrics, capacitors, combinations, stored energy'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- 2.1 Potential energy
d.sec('2.1-introduction')
d.basic('Why can we define electrostatic potential energy at all?', 'The Coulomb force between static charges is ' + T('conservative') + ': work done depends only on the end points, not the path', **fig('fig_2_2_path'))
d.basic('Define potential energy difference U(P) − U(R) of a charge q.', 'Work done by an ' + T('external force') + ' in moving q from R to P ' + T('without acceleration') + ' (F_ext = −F_E)')
d.basic('Why must the charge be moved “without acceleration”?', 'Then no kinetic energy is gained: all the external work is ' + T('stored as potential energy'))
d.basic('Work done by the field vs by the external agent (R → P)?', 'Equal and opposite: W_field = ' + X('−W_ext') + ' = −ΔU')
d.basic('Is the absolute value of potential energy meaningful?', X('No') + ': only differences are; adding a constant to U everywhere changes nothing. We choose ' + T('U = 0 at infinity'))
d.basic('Define potential energy of q at a point (U(∞) = 0).', 'Work done by an external force in bringing q from ' + T('infinity') + ' to that point')

# ---------------------------------------------------------------- 2.2 Potential
d.sec('2.2-electrostatic-potential')
d.basic('Define electrostatic potential at a point.', 'Work done by an external force in bringing a ' + T('unit positive charge') + ' from infinity to the point, without acceleration: V = W/q')
d.basic('Why divide work by q to define potential?', 'Work ∝ q, so W/q depends only on the ' + T('charge configuration') + ', not on the test charge')
d.basic('Potential: scalar or vector? SI unit and dimensions?', T('Scalar') + '; volt, 1 V = 1 J C⁻¹; [ML²T⁻³A⁻¹]')
d.basic('Potential difference V_P − V_R in terms of work?', r'\( V_P - V_R = \dfrac{U_P - U_R}{q} \)' + ' = work per unit positive charge from R to P')
d.basic('Alessandro Volta: what did he show about Galvani’s “animal electricity”?', 'It was not special to animal tissue: any ' + T('wet body between dissimilar metals') + ' produces it → the first ' + T('voltaic pile') + ' (battery)')
d.basic('Intuition: what is potential, in one picture?', 'Electric “height”. A + charge rolls ' + T('downhill') + ' from high V to low V (a − charge rolls uphill); V tells you energy per coulomb, like gh is energy per kg')

# ---------------------------------------------------------------- 2.3 Point charge
d.sec('2.3-potential-due-to-point-charge')
d.basic('Potential of a point charge Q at distance r?', r'\( V = \dfrac{1}{4\pi\varepsilon_0}\dfrac{Q}{r} \)' + ' — valid for either sign of Q', **fig('fig_2_3_point'))
d.basic('Sketch the key steps deriving V = Q/4πε₀r.', 'Work against the field along the radial path from ∞: ' + r'\( W = -\int_\infty^r \dfrac{Q}{4\pi\varepsilon_0 r^{\prime 2}}\,dr^\prime = \dfrac{Q}{4\pi\varepsilon_0 r} \)')
d.basic('Sign of V near a negative charge? Meaning?', X('Negative') + ': the field itself does positive work bringing a unit + charge in from ∞ (attraction)')
d.basic('How do V and E of a point charge fall off with r?', 'V ∝ ' + N('1/r') + '; E ∝ ' + N('1/r²') + ' (E falls faster)', **fig('fig_2_4_V_E_graph'))
d.basic('Example 2.1: V at 9 cm from 4 × 10⁻⁷ C? Work to bring 2 × 10⁻⁹ C from ∞? Path-dependent?', 'V = ' + N('4 × 10⁴ V') + '; W = qV = ' + N('8 × 10⁻⁵ J') + '; ' + X('no') + ' — any path splits into radial and perpendicular steps, the latter doing no work')

# ---------------------------------------------------------------- 2.4 Dipole
d.sec('2.4-potential-due-to-dipole')
d.basic('Potential of a dipole (r ≫ a)?', r'\( V = \dfrac{1}{4\pi\varepsilon_0}\dfrac{p\cos\theta}{r^2} = \dfrac{1}{4\pi\varepsilon_0}\dfrac{\vec p\cdot\hat r}{r^2} \)', **fig('fig_2_5_dipole'))
d.basic('Dipole potential on the axis and on the equatorial plane?', 'Axis: ' + r'\( \pm\dfrac{p}{4\pi\varepsilon_0 r^2} \)' + ' (+ on the +q side). Equatorial plane: ' + N('V = 0'))
d.basic('Equatorial plane of a dipole: V = 0. Is E zero there too?', X('No') + ': E = p/4πε₀r³, opposite to p. Zero potential does not mean zero field')
d.basic('Two ways the dipole potential differs from a point charge’s?', '(1) Depends on the ' + T('angle θ') + ' (axially symmetric about p); (2) falls as ' + T('1/r²') + ', not 1/r')
d.basic('Mnemonic: powers of r for a point charge vs dipole?', '“' + T('Dipole adds one') + '”: charge V ∝ 1/r, E ∝ 1/r²; dipole V ∝ 1/r², E ∝ 1/r³')
d.basic('For which dipole is V = p cos θ/4πε₀r² exact?', 'A ' + T('point dipole') + ' (2a → 0, p finite); otherwise only for r ≫ a')
d.basic('Correction: NCERT (Sec 2.4) says graphs of 1/r² and 1/r vs r are in “Fig. 2.5”. Which figure is it?', T('Fig. 2.4') + ' (V and E of a point charge); Fig. 2.5 is the dipole geometry')

# ---------------------------------------------------------------- 2.5 System of charges
d.sec('2.5-potential-due-to-system-of-charges')
d.basic('Potential due to a system of point charges?', 'Algebraic (scalar) sum: ' + r'\( V = \dfrac{1}{4\pi\varepsilon_0}\sum_i \dfrac{q_i}{r_{iP}} \)' + ' — no vector addition needed', **fig('fig_2_6_system'))
d.basic('Potential of a uniformly charged spherical shell (radius R), outside and inside?', 'Outside: ' + r'\( \dfrac{q}{4\pi\varepsilon_0 r} \)' + '. Inside: ' + T('constant') + ' = ' + r'\( \dfrac{q}{4\pi\varepsilon_0 R} \)' + ' (E = 0 inside, so no work is done)', **fig('drawn_sphere_V_E'))
d.basic('Across a charged shell’s surface, which is continuous: E or V?', T('V') + ' is continuous; ' + X('E jumps') + ' from 0 to σ/ε₀')
steps_card(d, 'Example 2.2 · zero potential', 'Find the missing step.', '3 × 10⁻⁸ C at x = 0 and −2 × 10⁻⁸ C at x = 15 cm. Where on the line is V = 0?',
           ['V = 0 only where the + charge’s larger |q| is offset by being farther: x > 0', 'Between: 3/x − 2/(15 − x) = 0 → <b>x = 9 cm</b>',
            'Beyond the − charge: 3/x − 2/(x − 15) = 0', '→ <b>x = 45 cm</b> (from the + charge)'], 2,
           'Points of zero potential for two unlike charges', 'x = 9 cm (between) and x = 45 cm (beyond the negative charge)')
d.basic('Exercise 2.1: 5 × 10⁻⁸ C and −3 × 10⁻⁸ C, 16 cm apart. Points of zero potential?', N('10 cm') + ' and ' + N('40 cm') + ' from the positive charge, both on the side of the negative charge')
d.basic('Exercise 2.2: 5 μC at each vertex of a regular hexagon of side 10 cm. V at the centre?', '6 × kq/a = 6 × 4.5 × 10⁵ = ' + N('2.7 × 10⁶ V') + ' (E at the centre is zero, V is not)')
d.basic('Example 2.3: for a positive charge, which is higher, V_P (nearer) or V_Q? For a negative charge, V_B (farther) or V_A?', 'V_P > V_Q, and V_B > V_A: potential always ' + T('falls along field lines'), **img('fig_2_8_example'))
d.basic('Example 2.3(e): a small negative charge moves from B to A (towards a negative charge). Its KE?', T('Decreases') + ': it is repelled, the field does negative work')

# ---------------------------------------------------------------- 2.6 Equipotentials
d.sec('2.6-equipotential-surfaces')
d.basic('Define an equipotential surface.', 'A surface on which the potential has the ' + T('same value everywhere'))
d.basic('Equipotential surfaces of a point charge?', T('Concentric spheres') + ' centred on the charge', **fig('fig_2_9_point_equi'))
d.basic('Equipotential surfaces of a uniform field?', T('Parallel planes') + ' normal to the field', **fig('fig_2_10_uniform_equi'))
d.basic('Identify: equipotentials of which two configurations?', '(a) An ' + T('electric dipole') + '; (b) ' + T('two identical positive charges'), **img('fig_2_11_dipole_equi'))
d.basic('Why is E always normal to an equipotential surface?', 'A component along the surface would mean ' + T('work is done moving charge along it') + ' — contradicting ΔV = 0')
d.basic('Work done moving a charge along an equipotential?', N('Zero'))
d.basic('Can two equipotential surfaces intersect?', X('No') + ': the point of intersection would have two values of potential')
d.basic('Exercise 2.3: 2 μC and −2 μC, 6 cm apart. An equipotential surface? Direction of E on it?', 'The ' + T('plane perpendicular to AB through its midpoint') + ' (V = 0); E is normal to it, pointing from the + charge towards the − charge')

d.sec('2.6.1-relation-between-field-and-potential')
d.basic('Relation between E and V?', r'\( E = -\dfrac{dV}{dl} \)' + ' (along the normal to equipotentials)', **fig('fig_2_12_E_from_V'))
d.cloze('Electric field points in the direction in which potential {{c1::decreases steepest}}; its magnitude is the {{c2::change in potential per unit normal displacement}}.')
d.basic('Close equipotentials vs widely spaced ones: what does it say about E?', 'Close spacing = ' + T('strong field') + ' (steep slope); wide spacing = weak field')
d.basic('Teacher addition: E from V(x, y, z)?', r'\( E_x = -\dfrac{\partial V}{\partial x},\ E_y = -\dfrac{\partial V}{\partial y},\ E_z = -\dfrac{\partial V}{\partial z} \)' + ' (E = −grad V)')
d.basic('Teacher addition: uniform field E between two points d apart along E. Potential difference?', 'V = ' + N('Ed') + ' (higher potential at the start); unit of E is also ' + N('V/m'))
d.basic('Trap: can V be zero where E ≠ 0, and E be zero where V ≠ 0?', 'Yes to both: ' + E('equatorial plane of a dipole') + ' (V = 0, E ≠ 0); ' + E('inside a charged shell') + ' (E = 0, V ≠ 0)')

# ---------------------------------------------------------------- 2.7 PE of a system
d.sec('2.7-potential-energy-of-system-of-charges')
d.basic('Potential energy of two charges q₁, q₂ at separation r₁₂?', r'\( U = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q_1q_2}{r_{12}} \)' + ' = work to assemble them from infinity')
d.basic('Sign of U for like and unlike charges? Meaning?', 'Like: ' + N('U > 0') + ' (work needed to push them together). Unlike: ' + X('U < 0') + ' (work needed to pull them apart)')
d.basic('Potential energy of three charges?', r'\( U = \dfrac{1}{4\pi\varepsilon_0}\left(\dfrac{q_1q_2}{r_{12}} + \dfrac{q_1q_3}{r_{13}} + \dfrac{q_2q_3}{r_{23}}\right) \)' + ' — one term per pair', **fig('fig_2_14_three'))
d.basic('Does the order of assembling charges change U?', X('No') + ': the force is conservative, so U depends only on the ' + T('final configuration'))
d.basic('Teacher addition: how many pair terms for n charges?', r'\( \dfrac{n(n-1)}{2} \)' + ' (e.g. 6 for four charges)')
steps_card(d, 'Example 2.4 · square of charges', 'Find the missing step.', '+q, −q, +q, −q at corners A, B, C, D of a square of side d. Work to assemble? Extra work to bring q₀ to the centre?',
           ['4 adjacent unlike pairs: 4 × (−q²/4πε₀d)', '2 diagonal like pairs: 2 × q²/(4πε₀ d√2) = +√2 q²/4πε₀d',
            'U = <b>−(4 − √2) q²/4πε₀d</b>', 'V at the centre = 0 (± cancel) → <b>no extra work</b> for q₀'], 1,
           'Energy of a square of alternating charges (Example 2.4)', 'U = −(4 − √2) q²/(4πε₀d); bringing q₀ to the centre needs zero work since V = 0 there')
d.basic('Identify the arrangement and its electrostatic energy.', 'Alternating ±q on a square of side d: ' + r'\( U = -\dfrac{(4-\sqrt2)\,q^2}{4\pi\varepsilon_0 d} \)', **img('fig_2_15_square'))

# ---------------------------------------------------------------- 2.8 PE in external field
d.sec('2.8-potential-energy-in-external-field')
d.basic('Potential energy of a charge q in an external potential V(r)?', N('U = qV(r)') + ', where V is due to ' + T('external charges only'))
d.basic('Why can V in qV(r) not include q’s own potential?', 'A charge’s potential at its own location is ' + X('infinite / undefined'))
d.basic('Define 1 electron volt.', 'Energy gained by an electron accelerated through ' + N('1 V') + ': 1 eV = ' + N('1.6 × 10⁻¹⁹ J'))
table_card(d, 'Energy units', 'In joules?', [
    ('1 keV', '1.6 × 10⁻¹⁶ J', False), ('1 MeV', '1.6 × 10⁻¹³ J', False), ('1 GeV', '1.6 × 10⁻¹⁰ J', False), ('1 TeV', '1.6 × 10⁻⁷ J', False)],
    term='eV multiples')
d.basic('Potential energy of two charges in an external field?', r'\( U = q_1V(\vec r_1) + q_2V(\vec r_2) + \dfrac{q_1q_2}{4\pi\varepsilon_0 r_{12}} \)')
d.basic('Example 2.5: 7 μC at (−9 cm, 0, 0) and −2 μC at (9 cm, 0, 0). U? Work to separate them to infinity?', 'U = 9 × 10⁹ × (7 × −2) × 10⁻¹² / 0.18 = ' + N('−0.7 J') + '; work needed = ' + N('+0.7 J'))
d.basic('Example 2.5(c): same pair in an external field E = A/r² (A = 9 × 10⁵ N C⁻¹ m²). Total energy?', 'V = A/r: q₁V₁ + q₂V₂ = 70 − 20 = 50 J; total = 50 − 0.7 = ' + N('49.3 J'))
d.basic('Potential energy of a dipole in a uniform field?', r'\( U(\theta) = -pE\cos\theta = -\vec p\cdot\vec E \)' + ' (zero chosen at θ = 90°)', **fig('fig_2_16_dipole_pe'))
d.basic('Work done by an external torque to rotate a dipole from θ₁ to θ₂?', r'\( W = pE(\cos\theta_1 - \cos\theta_2) \)')
table_card(d, 'Dipole in a uniform field', 'U and nature?', [
    ('θ = 0° (p along E)', 'U = −pE, stable equilibrium (minimum)', False), ('θ = 90°', 'U = 0, maximum torque pE', False),
    ('θ = 180°', 'U = +pE, unstable equilibrium (maximum)', True)], term='Dipole energy at key angles')
d.basic('Why is θ = 90° the natural zero of dipole potential energy?', 'There, the work against E in bringing +q and −q in from infinity is ' + T('equal and opposite') + ' and cancels')
d.basic('Example 2.6: 1 mole of dipoles (p = 10⁻²⁹ C m each), fully aligned in 10⁶ V/m; the field turns by 60°. Heat released?', 'Total p = 6 × 10⁻⁶ C m; Uᵢ = −6 J, U_f = −3 J → ' + N('3 J') + ' of heat')
d.basic('Points to ponder: a dipole released at an angle in a uniform field — does it just align with E?', X('No') + ': the torque makes it ' + T('oscillate') + ' about E; it settles only if there is damping')

# ---------------------------------------------------------------- 2.9 Conductors
d.sec('2.9-electrostatics-of-conductors')
d.basic('Free electrons in a metal: free to do what, and not to do what?', 'Free to move ' + T('within') + ' the metal (like a gas), ' + X('not free to leave') + ' it')
d.cloze('In electrostatics, the field {{c1::inside a conductor is zero}}; just outside a charged conductor it is {{c2::normal to the surface}}.')
d.basic('Why is E = 0 inside a conductor in the static situation?', 'Otherwise free charges would keep ' + T('drifting') + '; they rearrange until the field inside vanishes (this can be taken as the defining property of a conductor)')
d.basic('Why is the field at a conductor’s surface normal to it?', 'A tangential component would ' + T('move surface charges') + ' — not static')
d.basic('Where does excess charge on a conductor reside? Why?', 'Only on the ' + T('surface') + ': Gauss’s law on any tiny surface inside (E = 0) gives zero enclosed charge')
d.basic('Potential of a conductor?', T('Same everywhere') + ' in its volume and on its surface (an equipotential)')
d.basic('Field just outside a charged conductor?', r'\( \vec E = \dfrac{\sigma}{\varepsilon_0}\hat n \)' + ' — derived with a ' + T('pill-box') + ' Gaussian surface', **fig('fig_2_17_pillbox'))
d.basic('Charged conductor surface: σ/ε₀. Infinite charged sheet: σ/2ε₀. Why the factor 2?', 'A conductor has ' + T('E = 0 inside') + ', so all the flux leaves through one face of the pill-box; a thin sheet sends flux out both sides')
d.basic('State electrostatic shielding.', 'Field inside a ' + T('charge-free cavity') + ' of a conductor is zero, whatever the outside charges and fields; any charge sits on the outer surface', **fig('fig_2_18_cavity'))
d.basic('Use of electrostatic shielding?', 'Protecting sensitive instruments; why you are safe inside a ' + E('car') + ' in a thunderstorm')
d.basic('Points to ponder: does shielding work the other way round?', X('No') + ': charges placed inside the cavity do produce fields outside the conductor')
d.basic('Identify: what does this figure summarise?', 'Electrostatic properties of conductors: E = 0 and V constant inside, E = σ/ε₀ normal at the surface, E = 0 in a cavity', **img('fig_2_19_properties'))
d.basic('Teacher addition: on an irregular conductor, where is σ largest?', 'At ' + T('sharp points') + ' (small radius of curvature) — hence corona discharge and lightning conductors')
d.basic('Exercise 2.4: sphere (R = 12 cm) with 1.6 × 10⁻⁷ C. E inside, just outside, and at 18 cm?', N('0') + '; ' + N('10⁵ N/C') + '; ' + N('4.4 × 10⁴ N/C'))
d.basic('Example 2.7: why are aircraft tyres slightly conducting, and fuel trucks fitted with ground-touching chains?', 'To ' + T('leak frictional charge to the ground') + ' before it builds up and sparks a fire')
d.basic('Example 2.7: why is a bird on a live wire safe, but a man on the ground touching it is not?', 'Current needs a ' + T('potential difference') + ': the bird is at one potential; the man bridges the line and earth')
d.basic('Example 2.7: why does a comb fail to pick up paper on a rainy day?', 'Moist air/wet hair ' + X('prevents charging') + ' (charge leaks away), so the comb cannot polarise the paper')

# ---------------------------------------------------------------- 2.10 Dielectrics
d.sec('2.10-dielectrics-and-polarisation')
d.basic('Conductor vs dielectric in an external field?', 'Conductor: induced field ' + T('cancels') + ' E₀ inside (net 0). Dielectric: induced field only ' + T('reduces') + ' it', **fig('fig_2_20_conductor_dielectric'))
d.basic('Non-polar vs polar molecules? Examples?', T('Non-polar') + ': + and − centres coincide — ' + E('O₂, H₂') + '. ' + T('Polar') + ': permanent dipole — ' + E('HCl, H₂O'), **fig('fig_2_21_molecules'))
d.basic('Correction: NCERT calls HCl “an ionic molecule”. Is it?', X('No') + ': HCl is a ' + T('polar covalent') + ' molecule (partial ionic character); the example of a polar molecule is still correct')
d.basic('How does a non-polar dielectric get polarised?', 'The field ' + T('displaces') + ' + and − charges oppositely → an ' + T('induced dipole moment') + ' along E')
d.basic('How does a polar dielectric get polarised?', 'Permanent dipoles, randomly oriented by thermal agitation, partly ' + T('align') + ' with E; alignment competes with thermal energy', **fig('fig_2_22_polarisation'))
d.basic('Define polarisation P. Relation to E for a linear isotropic dielectric?', 'Dipole moment per unit volume: ' + r'\( \vec P = \varepsilon_0\chi_e\vec E \)' + ' (χₑ = electric susceptibility); unit C m⁻²')
d.basic('Uniformly polarised slab: where is the net induced charge?', 'Only on the ' + T('surfaces normal to the field') + ' (±σₚ); the interior is neutral', **fig('fig_2_23_slab'))
d.basic('Are the induced charges ±σₚ free or bound?', T('Bound') + ' charges of the dielectric')

# ---------------------------------------------------------------- 2.11 Capacitance
d.sec('2.11-capacitors-and-capacitance')
d.basic('What is a capacitor?', 'Two conductors separated by an ' + T('insulator') + ', usually carrying +Q and −Q', **fig('fig_2_24_two_conductors'))
d.basic('Define capacitance. Unit?', r'\( C = \dfrac{Q}{V} \)' + '; farad, 1 F = 1 C V⁻¹')
d.basic('On what does capacitance depend?', 'Only on ' + T('geometry') + ' (shape, size, separation) and the ' + T('dielectric') + ' — not on Q or V')
d.basic('“Charge on a capacitor” Q: what is the total charge?', 'Q is the charge on one plate; the total is ' + N('zero'))
d.basic('Why is a large capacitance useful?', 'It stores large Q at ' + T('low V') + ', so the field stays below the breakdown limit')
d.basic('Dielectric strength? Value for air?', 'Maximum field a dielectric can bear without breakdown; air ≈ ' + N('3 × 10⁶ V/m'))
d.basic('Dimensions of capacitance?', '[M⁻¹L⁻²T⁴A²]')
d.basic('Symbols: fixed vs variable capacitor?', 'Fixed: two parallel lines ─┤├─. Variable: the same with an ' + T('arrow') + ' across it')

# ---------------------------------------------------------------- 2.12 Parallel plate
d.sec('2.12-parallel-plate-capacitor')
d.basic('Field of a parallel-plate capacitor: between and outside the plates?', 'Between: ' + r'\( E = \dfrac{\sigma}{\varepsilon_0} = \dfrac{Q}{\varepsilon_0 A} \)' + ', uniform, + to −. Outside: ' + N('0'), **fig('fig_2_25_parallel_plate'))
d.basic('Capacitance of a parallel-plate capacitor (vacuum)?', r'\( C = \dfrac{\varepsilon_0 A}{d} \)')
d.basic('What is fringing?', 'Field lines ' + T('bend outward at the edges') + ' of finite plates; ignored when d² ≪ A')
d.basic('C for A = 1 m², d = 1 mm? Plate size for 1 F at d = 1 cm?', N('8.85 nF') + '; A ≈ 10⁹ m² — a plate about ' + N('30 km') + ' on a side. The farad is huge')
d.basic('Correction: NCERT (Sec 2.12) uses the sheet result from “Section 1.15”. Right section?', T('Section 1.14.2') + ' (field of an infinite plane sheet, Eq. 1.33)')
d.basic('Exercise 2.8: air capacitor, A = 6 × 10⁻³ m², d = 3 mm, on 100 V. C and Q?', 'C = ' + N('17.7 pF') + '; Q = ' + N('1.77 × 10⁻⁹ C'))
d.basic('Teacher addition: force of attraction between the plates?', r'\( F = \dfrac{Q^2}{2\varepsilon_0 A} \)' + ' — each plate feels only the other plate’s field σ/2ε₀')
d.basic('Teacher addition: capacitance of an isolated sphere of radius R?', r'\( C = 4\pi\varepsilon_0 R \)' + ' (Earth ≈ 711 μF)')
d.basic('Points to ponder: why is V small in a capacitor even when E is large?', 'The field is confined to a ' + T('small gap d') + ': V = Ed stays small')

# ---------------------------------------------------------------- 2.13 Dielectric
d.sec('2.13-effect-of-dielectric-on-capacitance')
d.basic('Field inside a dielectric filling a capacitor?', r'\( E = \dfrac{\sigma - \sigma_p}{\varepsilon_0} = \dfrac{E_0}{K} \)' + ' — reduced by the bound charges')
d.basic('Capacitance with a dielectric of constant K filling the gap?', r'\( C = \dfrac{K\varepsilon_0 A}{d} = KC_0 \)')
d.cloze('Permittivity of a medium: ε = {{c1::ε₀K}}. Dielectric constant (relative permittivity): K = {{c2::ε/ε₀}}, always {{c3::greater than 1}}.')
d.basic('General definition of dielectric constant (any capacitor)?', 'Factor by which capacitance increases when the dielectric ' + T('fills the space') + ': K = C/C₀')
d.basic('Example 2.8: slab of constant K, thickness 3d/4, inserted. New capacitance?', r'\( C = \dfrac{4K}{K+3}C_0 \)')
d.basic('Teacher addition: slab of thickness t (constant K) in a gap d. C?', r'\( C = \dfrac{\varepsilon_0 A}{d - t + t/K} \)' + '; for a metal slab (K → ∞): ' + r'\( \dfrac{\varepsilon_0 A}{d-t} \)')
d.basic('Exercise 2.5: 8 pF air capacitor; separation halved and gap filled with K = 6. New C?', '8 × 2 × 6 = ' + N('96 pF'))
table_card(d, 'Exercise 2.9 · inserting a dielectric (K = 6)', 'Q, V, C, E, U?', [
    ('Battery connected (V fixed)', 'C ×6, Q ×6, E same, U ×6', False),
    ('Battery disconnected (Q fixed)', 'C ×6, V ÷6, E ÷6, U ÷6', True)], term='Dielectric inserted: battery connected vs disconnected')
d.basic('Exercise 2.9: mica (K = 6) fills the 17.7 pF capacitor of Ex 2.8. (a) still on 100 V; (b) disconnected first?', '(a) C = 106 pF, Q = ' + N('1.06 × 10⁻⁸ C') + '. (b) Q stays 1.77 × 10⁻⁹ C, V = ' + N('16.7 V'))

# ---------------------------------------------------------------- 2.14 Combinations
d.sec('2.14-combination-of-capacitors')
d.basic('Capacitors in series: what is common, what adds?', 'Same ' + T('charge Q') + ' on each; voltages add: ' + r'\( \dfrac1C = \dfrac1{C_1} + \dfrac1{C_2} + \dots \)', **fig('fig_2_26_series_two'))
d.basic('Why do series capacitors all carry the same charge?', 'The inner plates plus connecting wire form an ' + T('isolated neutral conductor') + '; any imbalance would drive charge until each capacitor has ±Q', **fig('fig_2_27_series_n'))
d.basic('Capacitors in parallel: what is common, what adds?', 'Same ' + T('voltage V') + '; charges add: ' + r'\( C = C_1 + C_2 + \dots \)', **fig('fig_2_28_parallel'))
d.basic('Mnemonic: capacitors vs resistors?', 'Capacitors combine ' + T('opposite to resistors') + ': series uses reciprocals, parallel simply adds')
d.basic('Series combination: bigger or smaller than the smallest C?', X('Smaller') + ' than the smallest; parallel is larger than the largest')
steps_card(d, 'Example 2.9 · network', 'Find the missing step.', 'Four 10 μF capacitors: C₁, C₂, C₃ in series, with C₄ in parallel across the 500 V supply. C_eq and charges?',
           ['C₁, C₂, C₃ in series: C′ = 10/3 μF', 'C′ ∥ C₄: C = 10/3 + 10 = <b>13.3 μF</b>',
            'Series branch: Q = C′V = (10/3 μF)(500 V) = <b>1.7 × 10⁻³ C</b> on each of C₁–C₃', 'C₄: Q′ = 10 μF × 500 V = <b>5.0 × 10⁻³ C</b>'], 2,
           'Capacitor network (Example 2.9)', 'C = 13.3 μF; each series capacitor 1.7 × 10⁻³ C; C₄ 5.0 × 10⁻³ C')
d.basic('Identify: the network of Example 2.9.', 'C₁, C₂, C₃ in ' + T('series') + ', together in ' + T('parallel') + ' with C₄ across 500 V', **img('fig_2_29_network'))
d.basic('Exercise 2.6: three 9 pF in series on 120 V. C and voltage on each?', N('3 pF') + '; ' + N('40 V') + ' each')
d.basic('Exercise 2.7: 2, 3, 4 pF in parallel on 100 V. C and charges?', N('9 pF') + '; ' + N('2, 3, 4 × 10⁻¹⁰ C'))

# ---------------------------------------------------------------- 2.15 Energy
d.sec('2.15-energy-stored-in-capacitor')
d.basic('Energy stored in a capacitor (three forms)?', r'\( U = \dfrac{Q^2}{2C} = \dfrac12 CV^2 = \dfrac12 QV \)', **fig('fig_2_30_charging'))
d.basic('Why is the energy ½QV and not QV?', 'Early charge moves across a ' + T('small V') + ', later charge across larger V; the average potential during charging is ' + T('V/2'))
d.basic('Energy density of an electric field?', r'\( u = \dfrac12\varepsilon_0E^2 \)' + ' — true for any field, not just capacitors (Ad = volume of the field)')
d.basic('Where is a capacitor’s energy “stored”?', 'In the ' + T('electric field') + ' between the plates')
steps_card(d, 'Example 2.10 · sharing charge', 'Find the missing step.', '900 pF charged to 100 V, then disconnected and joined to an uncharged 900 pF. Energies?',
           ['Q = CV = 9 × 10⁻⁸ C; U₁ = ½QV = <b>4.5 × 10⁻⁶ J</b>', 'Charge shares equally: Q′ = Q/2, so V′ = 50 V',
            'U₂ = 2 × ½ (Q/2)(V/2) = <b>2.25 × 10⁻⁶ J</b>', 'Half the energy is lost as heat and EM radiation during the transient current'], 1,
           'Energy lost when capacitors share charge (Example 2.10)', 'Final energy is half the initial: 4.5 → 2.25 μJ, lost as heat and radiation')
d.basic('Identify: what happens in (a) and (b)?', '(a) Capacitor charged by 100 V; (b) connected to an identical uncharged one: charge ' + T('shared equally') + ', half the energy lost', **img('fig_2_31_sharing'))
d.basic('Teacher addition: energy lost when C₁ at V₁ is joined to C₂ at V₂ (like plates together)?', r'\( \Delta U = \dfrac{C_1C_2}{2(C_1+C_2)}(V_1 - V_2)^2 \)' + ' — never zero unless V₁ = V₂')
d.basic('Exercise 2.10: 12 pF on 50 V. Energy?', '½ × 12 × 10⁻¹² × 2500 = ' + N('1.5 × 10⁻⁸ J'))
d.basic('Exercise 2.11: 600 pF charged to 200 V, then joined to an uncharged 600 pF. Energy lost?', 'U₁ = 1.2 × 10⁻⁵ J → U₂ = 6 × 10⁻⁶ J; lost ' + N('6 × 10⁻⁶ J'))
d.basic('Teacher addition: a battery charges C to V. Work by the battery vs energy stored?', 'Battery supplies QV = CV²; capacitor stores ½CV²; ' + T('half is lost') + ' as heat in the wires, whatever the resistance')

# ---------------------------------------------------------------- Points to ponder / summary
d.sec('points-to-ponder')
d.basic('Points to ponder: if a charge feels a force, how can electrostatics treat it as at rest?', 'Each charge is assumed ' + T('held in place by unspecified forces') + ' balancing the Coulomb force')
d.basic('Is the potential of a point charge at its own location defined?', X('No') + ': it is infinite')

d.sec('summary')
table_card(d, 'Summary', 'Formula?', [
    ('Point charge', 'V = kq/r', False), ('Dipole (r ≫ a)', 'V = kp cos θ/r²', False), ('Field from potential', 'E = −dV/dl', False),
    ('Two-charge energy', 'U = kq₁q₂/r', False), ('Dipole in field', 'U = −p·E', False), ('Parallel plate', 'C = Kε₀A/d', False),
    ('Stored energy', 'U = Q²/2C = ½CV²', False), ('Energy density', 'u = ½ε₀E²', False)], term='Chapter 2 formula sheet')
table_card(d, 'Concept checks', 'True or false?', [
    ('E = 0 at a point implies V = 0 there', 'False (inside a shell)', True), ('Field lines are normal to equipotentials', 'True', False),
    ('Excess charge can sit inside a conductor', 'False (surface only)', True), ('A dielectric increases capacitance', 'True', False),
    ('Charge sharing between capacitors conserves energy', 'False (charge is conserved, energy is not)', True)],
    term='Chapter 2 concept checks')

print(d.write(os.path.join(OUT, 'deck.json')), 'cards')
