import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Physics', 'class11-physics-ch12-kinetic-theory')
d = Deck('Chapter 12: Kinetic Theory', 'Class 11', ['class-11', 'physics', 'ch-12'])
d.description = 'Molecular nature of matter, gas laws, pressure of an ideal gas, kinetic interpretation of temperature, rms speed, equipartition, specific heats, mean free path'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- 12.1-12.2
d.sec('12.1-introduction')
d.basic('What is the basic idea of kinetic theory?', 'A gas is made of rapidly moving molecules with ' + T('negligible interactions') + ' except during collisions')
d.basic('Who developed kinetic theory, and what does it explain?', T('Maxwell, Boltzmann') + ' and others (19th century): pressure, temperature, gas laws, Avogadro’s hypothesis, specific heats, viscosity, diffusion')
d.basic('State Feynman’s "atomic hypothesis".', 'All things are made of atoms in perpetual motion, ' + T('attracting') + ' when a little apart and ' + T('repelling') + ' when squeezed together')

d.sec('12.2-molecular-nature-of-matter')
d.basic('Ancient atomic ideas: who in India and Greece?', T('Kanada') + ' (Vaiseshika school, ~6th century BC; paramanu) and ' + T('Democritus') + ' (4th century BC; "atom" = indivisible)')
d.basic('Who is credited with the scientific atomic theory, and which laws did it explain?', T('John Dalton') + ': laws of definite and multiple proportions')
d.basic('State Gay Lussac’s law and Avogadro’s law.', 'Gay Lussac: reacting gas volumes are in ' + T('small-integer ratios') + '. Avogadro: equal volumes of gases at the same T and P have the ' + T('same number of molecules'))
table_card(d, '12.2 · molecular distances', 'Typical value?', [
    ('Size of an atom', '≈ 1 Å (10⁻¹⁰ m)', False), ('Spacing in solids and liquids', '≈ 2 Å', False),
    ('Spacing in gases', 'tens of Å', False), ('Mean free path in gases', 'thousands of Å', False)], term='Molecular sizes and spacings')
d.basic('Why is a gas at equilibrium called a dynamic equilibrium?', 'Molecules keep colliding and changing speeds; only ' + T('average properties') + ' stay constant')

# ---------------------------------------------------------------- 12.3 Behaviour of gases
d.sec('12.3-behaviour-of-gases')
d.basic('Ideal gas equation in terms of molecules?', r'\( PV = Nk_BT \)' + ', or ' + r'\( P = nk_BT \)' + ' (n = number density); k_B = '.replace('k_B', 'k') + N('1.38 × 10⁻²³ J K⁻¹'))
d.basic('Relation between R, k_B and N_A?'.replace('k_B', 'k').replace('N_A', 'Nₐ'), r'\( R = N_A k_B \)' + ' = ' + N('8.314 J mol⁻¹ K⁻¹'))
d.basic('Ideal gas equation in terms of density?', r'\( P = \dfrac{\rho RT}{M_0} \)' + ' (M₀ = molar mass)')
d.basic('Molar volume at STP? Avogadro number?', N('22.4 L') + ' at 273 K and 1 atm; ' + N('6.02 × 10²³') + ' molecules')
d.basic('When does a real gas behave ideally?', 'At ' + T('low pressure and high temperature') + ' (molecules far apart, interactions negligible)', **fig('fig_12_1_real_gas'))
d.basic('Boyle’s law and Charles’ law from PV = μRT?', 'Fix μ, T: ' + T('PV = constant') + '. Fix P: ' + T('V ∝ T'), **fig('fig_12_2_boyle_steam'))
d.basic('How do experimental T–V curves of CO₂ compare with Charles’ law?', 'They agree at ' + T('low pressure') + '; deviate more at high pressure', **fig('fig_12_3_charles_co2'))
d.basic('Dalton’s law of partial pressures?', r'\( P = P_1 + P_2 + \dots \)' + ', each Pᵢ = μᵢRT/V as if that gas alone filled the vessel')
d.basic('Example 12.1: water density 1000 kg/m³, vapour at 100 °C 0.6 kg/m³. Fraction of vapour volume occupied by molecules?', N('≈ 6 × 10⁻⁴'))
d.basic('Example 12.2: estimate the size of a water molecule.', 'Mass = 0.018/(6 × 10²³) = 3 × 10⁻²⁶ kg → volume 3 × 10⁻²⁹ m³ → radius ≈ ' + N('2 Å'))
d.basic('Example 12.3: average distance between molecules in water vapour?', 'Volume grows ~10³ ×, spacing ~10 × radius → ≈ ' + N('40 Å'))
d.basic('Example 12.4: Ne and O₂ with partial pressures 3 : 2. Ratio of molecules and of mass densities?', 'Molecules ' + N('3 : 2') + '; densities (3/2)(20.2/32.0) = ' + N('0.947'))
d.basic('Exercise 12.2: show molar volume at STP is 22.4 L.', 'V = RT/P = 8.31 × 273 / 1.013 × 10⁵ ≈ ' + N('0.0224 m³'))
d.basic('Exercise 12.3: PV/T vs P for 1.00 g of O₂. Meaning of the dotted line, and the common intercept?', 'Dotted = ideal gas; intercept = μR = (1/32) × 8.31 = ' + N('0.26 J/K') + '; T₁ > T₂ (closer to ideal)', **img('fig_12_8_ex_pv_t'))
d.basic('Exercise 12.4: 30 L O₂ cylinder, gauge 15 atm at 27 °C falls to 11 atm at 17 °C. Mass taken out?', N('≈ 0.14 kg') + ' (use absolute pressures 16 and 12 atm)')
d.basic('Exercise 12.5: 1.0 cm³ bubble rises from 40 m depth (12 °C) to the surface (35 °C). New volume?', N('≈ 5.3 cm³') + ' (P₁V₁/T₁ = P₂V₂/T₂)')
d.basic('Exercise 12.6: molecules in a 25.0 m³ room at 27 °C and 1 atm?', 'N = PV/kT ≈ ' + N('6.1 × 10²⁶'))

# ---------------------------------------------------------------- 12.4 Kinetic theory of ideal gas
d.sec('12.4-kinetic-theory-of-ideal-gas')
table_card(d, '12.4 · assumptions of kinetic theory', 'Assumption?', [
    ('Molecules', 'huge number, in random motion', False), ('Size', 'negligible vs distances between them', False),
    ('Forces', 'none except during collisions', False), ('Collisions', 'elastic, very short', False)], term='Assumptions of kinetic theory of gases')
d.basic('Momentum given to a wall when a molecule rebounds elastically?', r'\( 2mv_x \)', **fig('fig_12_4_wall_collision'))
steps_card(d, '12.4.1 · pressure of an ideal gas', 'Find the missing step.', 'Derive P = ⅓ nm⟨v²⟩ for a gas in a box.',
           ['Each hit gives the wall 2mvₓ', 'In time Δt, ½ nAvₓΔt molecules hit area A', 'P = nm⟨vₓ²⟩', 'Isotropy: ⟨vₓ²⟩ = ⟨v²⟩/3 → <b>P = ⅓ nm⟨v²⟩</b>'], 1,
           'Pressure of an ideal gas from kinetic theory', 'Momentum 2mvx per hit, ½ nAvxΔt hits → P = nm⟨vx²⟩ = ⅓ nm⟨v²⟩')
d.basic('Why doesn’t the container’s shape or molecular collisions spoil the pressure formula?', 'Pressure is the same everywhere (Pascal); collisions just swap velocities in a ' + T('steady distribution'))
d.basic('Pressure in terms of kinetic energy?', r'\( PV = \tfrac23 E \)' + ' (E = total translational KE)')
d.basic('Kinetic interpretation of temperature?', r'\( \tfrac12 m\langle v^2\rangle = \tfrac32 k_BT \)' + ': average translational KE per molecule ∝ T, independent of P, V and the gas')
d.basic('Internal energy of an ideal gas depends on…?', T('Temperature only') + ' (E = 3/2 NkT for monatomic)')
d.basic('Define rms speed. Formula?', r'\( v_{rms} = \sqrt{\langle v^2\rangle} = \sqrt{\dfrac{3k_BT}{m}} = \sqrt{\dfrac{3RT}{M_0}} \)')
d.basic('rms speed of N₂ at 300 K?', N('≈ 516 m/s') + ' — about the speed of sound')
d.basic('At the same temperature, which molecules are faster?', 'The ' + T('lighter') + ' ones (vᵣₘₛ ∝ 1/√m)')
d.basic('Trap: is ⟨v²⟩ equal to ⟨v⟩²?', X('Not in general') + ': the mean of squares exceeds the square of the mean (e.g. speeds 1 and 3: ⟨v²⟩ = 5, ⟨v⟩² = 4)')
d.basic('Example 12.5: argon and chlorine (2 : 1 by mass) at 27 °C. Ratio of average KE per molecule and of rms speeds?', 'KE ' + N('1 : 1') + '; vᵣₘₛ(Ar)/vᵣₘₛ(Cl₂) = √(70.9/39.9) = ' + N('1.33') + ' (mass ratio irrelevant)')
d.basic('Example 12.6: ²³⁵UF₆ vs ²³⁸UF₆. Which is faster and by how much?', '²³⁵UF₆, by √(352/349) − 1 ≈ ' + N('0.44 %') + ' — used for uranium enrichment by diffusion', **fig('fig_12_5_porous_wall'))
d.basic('Graham’s law of diffusion (Exercise 12.12 idea)?', 'Rate of diffusion ∝ ' + T('1/√(molar mass)'))
d.basic('Example 12.7: why does a gas heat up when compressed by a moving piston?', 'Molecules rebound from the ' + T('approaching piston faster') + ' (like a ball off a moving bat), so average KE and T rise; expansion cools it')
d.basic('Exercise 12.7: average thermal energy of a helium atom at 300 K, 6000 K, 10⁷ K?', N('6.2 × 10⁻²¹ J') + ', ' + N('1.24 × 10⁻¹⁹ J') + ', ' + N('2.1 × 10⁻¹⁶ J') + ' (3/2 kT)')
d.basic('Exercise 12.8: equal vessels of Ne, Cl₂, UF₆ at the same T, P. Same number of molecules? Largest vᵣₘₛ?', T('Yes') + ' (Avogadro); vᵣₘₛ largest for ' + T('neon') + ' (lightest)')
d.basic('Exercise 12.9: at what temperature is vᵣₘₛ of argon equal to that of helium at −20 °C?', 'T = 253 × 39.9/4.0 ≈ ' + N('2.52 × 10³ K'))
d.basic('Why don’t air molecules settle on the floor?', 'Their KE (~kT) is much larger than mgh for room heights; collisions keep them spread out')
d.basic('Correction: NCERT 12.4.2 begins "Equation (13.14) can be written as". Which equation?', T('Eq. (12.14)') + ', P = ⅓ nm⟨v²⟩; the number is left over from the old chapter order')

# ---------------------------------------------------------------- 12.5 Equipartition
d.sec('12.5-equipartition')
d.basic('What is a degree of freedom?', 'An independent way a molecule can store energy: each ' + T('squared term') + ' in its energy (½mvₓ², ½Iω², ½ky²…)')
d.basic('Degrees of freedom of a monatomic and a rigid diatomic molecule?', 'Monatomic: ' + N('3') + ' (translation). Rigid diatomic: ' + N('5') + ' (3 translation + 2 rotation)', **fig('fig_12_6_diatomic_axes'))
d.basic('Why only 2 rotational degrees for a diatomic molecule?', 'Rotation about the line joining the atoms has almost ' + T('zero moment of inertia') + ' and does not come into play (quantum reasons)')
d.cloze('Law of equipartition: in equilibrium, each quadratic energy mode has average energy {{c1::½ kT}}; a vibrational mode contributes {{c2::kT}} (kinetic + potential).')
d.basic('Who first proved the equipartition law?', T('Maxwell'))

# ---------------------------------------------------------------- 12.6 Specific heats
d.sec('12.6-specific-heat-capacity')
table_card(d, 'Table 12.1 · predicted molar heats', 'Cᵥ, Cₚ, γ?', [
    ('Monatomic (3 dof)', 'Cᵥ = 3R/2, Cₚ = 5R/2, γ = 5/3', False),
    ('Rigid diatomic (5 dof)', 'Cᵥ = 5R/2, Cₚ = 7R/2, γ = 7/5', False),
    ('Diatomic with vibration', 'Cᵥ = 7R/2, Cₚ = 9R/2, γ = 9/7', False),
    ('Polyatomic, f vibrational modes', 'Cᵥ = (3 + f)R, Cₚ = (4 + f)R', False)], term='Molar specific heats from equipartition')
d.basic('General shortcut: Cᵥ and γ in terms of degrees of freedom f?', r'\( C_v = \dfrac f2 R,\quad \gamma = 1 + \dfrac 2f \)')
d.basic('Does Cₚ − Cᵥ = R depend on the type of gas?', X('No') + ': true for every ideal gas', **fig('tab_12_1_predicted_heats'))
d.basic('How well do the predictions match experiment (Table 12.2)?', 'Very well for He, Ne, Ar, H₂, O₂, N₂; gases like Cl₂, C₂H₆ are ' + T('higher') + ' because vibrations are active', **fig('tab_12_2_measured_heats'))
d.basic('Example 12.8: 44.8 L cylinder of helium at STP heated by 15 °C at constant volume. Heat needed?', '2 mol × (3/2)R × 15 = 45R ≈ ' + N('374 J'))
d.basic('Molar specific heat of solids from equipartition?', 'Each atom: 3D oscillator, energy 3kT → U = 3RT per mole → ' + T('C = 3R') + ' (carbon is an exception)', **fig('tab_12_3_solids'))

# ---------------------------------------------------------------- 12.7 Mean free path
d.sec('12.7-mean-free-path')
d.basic('Why does leaking cooking gas take a long time to spread though molecules move at ~500 m/s?', 'Molecules keep ' + T('colliding') + '; their paths zig-zag')
d.basic('Define mean free path.', 'Average distance a molecule travels ' + T('between successive collisions'))
d.basic('Formula for mean free path?', r'\( l = \dfrac{1}{\sqrt2\,n\pi d^2} \)' + ' (n = number density, d = molecular diameter)', **fig('fig_12_7_mean_free_path'))
d.basic('Why the √2 in the mean free path formula?', 'The other molecules also move; the ' + T('relative velocity') + ' sets the collision rate')
d.basic('Mean free path and collision time for air at STP?', 'l ≈ ' + N('2.9 × 10⁻⁷ m') + ' (~1500 d); τ ≈ ' + N('6 × 10⁻¹⁰ s'))
d.basic('How does mean free path depend on pressure and temperature?', r'\( l \propto \dfrac1n = \dfrac{kT}{P} \)' + ': larger at low pressure (vacuum tubes) and high temperature')
d.basic('Example 12.9: mean free path of water vapour at 373 K?', 'l scales with T: 2.9 × 10⁻⁷ × 373/273 ≈ ' + N('4 × 10⁻⁷ m') + ' — ~100 × the intermolecular distance')
d.basic('Exercise 12.10: N₂ at 2.0 atm, 17 °C, radius 1.0 Å. Mean free path and collision frequency?', 'l ≈ ' + N('1.0 × 10⁻⁷ m') + '; frequency ≈ ' + N('5 × 10⁹ s⁻¹') + '; free time ≈ 500 × collision time')
d.basic('Exercise 12.1: fraction of volume occupied by O₂ molecules at STP (d = 3 Å)?', N('≈ 4 × 10⁻⁴'))

# ---------------------------------------------------------------- Summary
d.sec('summary')
table_card(d, 'Summary', 'Formula?', [
    ('Pressure', 'P = ⅓ nm⟨v²⟩', False), ('Average KE per molecule', '(3/2) kT', False), ('rms speed', '√(3RT/M₀)', False),
    ('Energy per quadratic mode', '½ kT', False), ('Mean free path', '1/(√2 nπd²)', False)], term='Chapter 12 formula sheet')
table_card(d, 'Points to ponder', 'True or false?', [
    ('Pressure exists only at the walls of a container', 'False (everywhere in the gas)', True),
    ('Molecules in a gas are ~1000 molecular sizes apart', 'False (~10×; the mean free path is ~1000×)', True),
    ('A vibrational mode counts as two energy modes', 'True', False)], term='Chapter 12 concept checks')

print(d.write(os.path.join(OUT, 'deck.json')), 'cards')
