import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase_phy as sp

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Physics', 'class11-physics-ch08-mechanical-properties-of-solids')
d = Deck('Chapter 8: Mechanical Properties of Solids', 'Class 11', ['class-11', 'physics', 'ch-8'])
d.description = 'Elasticity, stress and strain, Hooke’s law, stress-strain curve, Young’s, shear and bulk moduli, Poisson’s ratio, elastic energy, applications'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- 8.1 Introduction
d.sec('8.1-introduction')
d.basic('Are real solids perfectly rigid?', X('No') + ': even a steel bar deforms under a large enough force')
d.basic('Define elasticity and elastic deformation.', 'The property by which a body ' + T('regains its original size and shape') + ' when the deforming force is removed')
d.basic('Define plasticity. Example?', 'No tendency to regain shape: the body is ' + T('permanently deformed') + '. ' + E('Putty, mud') + ' are near-ideal plastics')
d.basic('Why does elasticity matter in engineering?', 'Designing buildings, bridges, cranes, aircraft and artificial limbs needs the elastic properties of steel, concrete etc.')

# ---------------------------------------------------------------- 8.2 Stress and strain
d.sec('8.2-stress-and-strain')
d.basic('Define stress. Unit and dimensions?', 'Restoring force per unit area, ' + r'\( \sigma = \dfrac{F}{A} \)' + '; ' + N('N m⁻² = Pa') + ', [M L⁻¹ T⁻²]')
d.basic('When a body is deformed, how big is the restoring force?', T('Equal and opposite') + ' to the applied force (body in equilibrium)')
table_card(d, '8.2 · three kinds of stress', 'Strain produced?', [
    ('Tensile / compressive (longitudinal) stress', 'longitudinal strain ΔL/L', False),
    ('Tangential (shearing) stress', 'shearing strain Δx/L = tan θ ≈ θ', False),
    ('Hydraulic stress (pressure on all sides)', 'volume strain ΔV/V, no change in shape', False)], term='Stress types and their strains')
d.basic('Identify the four deformations in Fig. 8.1.', '(a) tensile stretching; (b) shear of a cylinder; (c) shear of a book pushed sideways; (d) hydraulic compression of a body in a fluid', **img('fig_8_1_stress_types'))
d.basic('Why is shearing strain ≈ θ?', 'For small θ, tan θ ≈ θ (at 10° they differ by only about 1 %)')
d.basic('Units of strain?', X('None') + ': a ratio of like quantities, dimensionless')
d.basic('Correction: NCERT says the book-pushing example is "Fig. 8.2(c)". Which figure is it?', T('Fig. 8.1(c)') + '. Fig. 8.2 is the stress–strain curve')
d.basic('Is stress a vector (Points to ponder)?', X('No') + ': it cannot be given a single direction; the force on a given side of a section has a direction')
d.basic('A wire hangs from the ceiling with weight F at its end. Tension at a cross-section: F or 2F?', T('F') + ': the ceiling’s pull balances the weight; stress = F/A')

# ---------------------------------------------------------------- 8.3 Hooke's law
d.sec('8.3-hookes-law')
d.cloze('Hooke’s law: for small deformations, {{c1::stress ∝ strain}}; the constant of proportionality is the {{c2::modulus of elasticity}}.')
d.basic('Is Hooke’s law a fundamental law?', X('No') + ': it is ' + T('empirical') + ', valid only in the linear part of the stress–strain curve; some materials never obey it')

# ---------------------------------------------------------------- 8.4 Stress-strain curve
d.sec('8.4-stress-strain-curve')
sp.stress_strain_story(d)
d.basic('Stress–strain curve, O to A?', T('Linear') + ': Hooke’s law holds; the body is elastic', **fig('fig_8_2_stress_strain'))
d.basic('Stress–strain curve, A to B?', 'Not proportional, but the body ' + T('still returns') + ' to its original size. B = ' + T('yield point / elastic limit') + ', stress there = yield strength σᵧ', **fig('fig_8_2_stress_strain'))
d.basic('What is a permanent set?', 'Loaded beyond B and unloaded (e.g. at C), the strain does not return to zero: ' + T('plastic deformation'))
d.basic('Ultimate tensile strength and fracture point?', T('D') + ': maximum stress (σᵤ); beyond it strain grows even with less force, fracture at ' + T('E'))
d.basic('Brittle vs ductile from the stress–strain curve?', T('Brittle') + ': D and E close together (e.g. glass). ' + T('Ductile') + ': D and E far apart (e.g. copper, mild steel)')
d.basic('What are elastomers? Example?', 'Materials stretched to ' + T('large strains') + ' that still return, without obeying Hooke’s law and with no clear plastic region: ' + E('rubber, aorta tissue'), **fig('fig_8_3_aorta'))
d.basic('Exercise 8.2: from the given graph, stress 150 × 10⁶ Pa gives strain 0.002. Young’s modulus and yield strength?', 'Y = ' + N('7.5 × 10¹⁰ Pa') + '; yield strength ≈ ' + N('3 × 10⁸ Pa'), **fig('fig_8_9_ex_curve'))
d.basic('Exercise 8.3: A’s curve is steeper and goes higher than B’s. Greater Young’s modulus? Stronger?', T('A') + ' for both: steeper slope → larger Y; higher breaking stress → stronger', **img('fig_8_10_two_materials'))

# ---------------------------------------------------------------- 8.5 Elastic moduli
d.sec('8.5.1-youngs-modulus')
d.basic('Define Young’s modulus.', r'\( Y = \dfrac{\sigma}{\varepsilon} = \dfrac{FL}{A\,\Delta L} \)' + ' (tensile or compressive stress ÷ longitudinal strain)')
d.basic('Unit of Young’s modulus?', 'Same as stress: ' + N('N m⁻² (Pa)'))
d.basic('Table 8.1: Young’s modulus of steel, copper, aluminium, bone?', 'Steel ' + N('200 GPa') + ', copper ' + N('110 GPa') + ', aluminium ' + N('70 GPa') + ', bone ' + N('9.4 GPa'), **fig('tab_8_1_youngs_moduli'))
d.basic('Force to stretch a 0.1 cm² wire by 0.1 %: steel vs aluminium, brass, copper?', 'Steel ' + N('2000 N') + '; Al 690 N, brass 900 N, Cu 1100 N')
d.basic('Why is steel called "more elastic" than rubber?', 'Elasticity is about ' + T('resisting deformation') + ': steel stretches far less for the same stress (larger Y). "Stretches more = more elastic" is a misconception')
d.basic('Exercise 8.4(a): is Young’s modulus of rubber greater than that of steel?', X('False') + ': steel’s is far greater')
d.basic('Exercise 8.4(b): the stretching of a coil spring is determined by which modulus?', T('Shear modulus') + ' (true): the wire of a spring twists rather than stretches')
steps_card(d, 'Example 8.1 · steel rod', 'Find the missing step.', 'Steel rod, r = 10 mm, L = 1.0 m, pulled by 100 kN; Y = 2.0 × 10¹¹ Pa. Stress, elongation, strain?',
           ['A = π(0.01)² = 3.14 × 10⁻⁴ m²', 'Stress = 10⁵ / 3.14 × 10⁻⁴ = 3.18 × 10⁸ Pa', 'ΔL = stress × L / Y = 1.59 × 10⁻³ m', 'Strain = 1.59 × 10⁻³ = <b>0.16 %</b>'], 2,
           'Steel rod under tension', 'Stress 3.18 × 10⁸ Pa, elongation 1.59 mm, strain 0.16 %')
steps_card(d, 'Example 8.2 · wires in series', 'Find the missing step.', 'Copper (2.2 m) and steel (1.6 m) wires, both 3.0 mm diameter, joined end to end; total stretch 0.70 mm. Load?',
           ['Same tension and area → Y_c ΔL_c/L_c = Y_s ΔL_s/L_s', 'ΔL_c/ΔL_s = (2.0/1.1)(2.2/1.6) = 2.5', 'ΔL_c = 0.50 mm, ΔL_s = 0.20 mm', 'W = A Y_c ΔL_c / L_c = <b>1.8 × 10² N</b>'], 1,
           'Copper and steel wires in series', 'Equal stress: ΔLc/ΔLs = 2.5 → ΔLc = 0.5 mm → W ≈ 180 N')
d.basic('Example 8.3: circus human pyramid, 220 kg on a performer’s two thighbones (L 0.5 m, r 2.0 cm, Y 9.4 GPa). Compression of each?', N('4.55 × 10⁻⁵ m') + ' (strain ≈ 0.009 %)', **fig('fig_8_4_pyramid'))
d.basic('Correction: NCERT Examples 8.2–8.4 cite "Table 9.1" and "Eq. (9.8)". What do they mean?', T('Table 8.1') + ' and ' + T('Eq. (8.8)') + ': references left over from the old chapter numbering')
d.basic('Exercise 8.1: steel wire (4.7 m, 3.0 × 10⁻⁵ m²) and copper wire (3.5 m, 4.0 × 10⁻⁵ m²) stretch equally under the same load. Y(steel)/Y(copper)?', N('1.8') + ' (Y ∝ L/A for equal F and ΔL)')
d.basic('Exercise 8.5: steel (1.5 m) holds 4 kg + brass, brass (1.0 m) holds 6 kg; diameter 0.25 cm. Elongations?', 'Steel ' + N('1.5 × 10⁻⁴ m') + ' (carries 10 kg); brass ' + N('1.3 × 10⁻⁴ m'), **fig('fig_8_11_two_wires'))
d.basic('Exercise 8.9: steel cable, radius 1.5 cm, stress limit 10⁸ Pa. Maximum load?', 'F = 10⁸ × π(0.015)² ≈ ' + N('7.07 × 10⁴ N'))

d.sec('8.5.2-shear-modulus')
d.basic('Define shear modulus (modulus of rigidity).', r'\( G = \dfrac{F/A}{\Delta x/L} = \dfrac{F}{A\theta} \)')
d.basic('Typical relation between G and Y?', r'\( G \approx \dfrac{Y}{3} \)' + ' for most materials', **fig('tab_8_2_shear_moduli'))
d.basic('Which moduli apply only to solids?', 'Young’s and shear moduli: only ' + T('solids') + ' have fixed lengths and shapes')
d.basic('Example 8.4: lead slab 50 cm × 50 cm × 10 cm, shear force 9.0 × 10⁴ N on the narrow face, lower edge riveted, G = 5.6 GPa. Displacement of the top edge?', 'Stress = 9.0 × 10⁴ / 0.05 = 1.8 × 10⁶ Pa; Δx = stress × L / G = ' + N('0.16 mm'), **fig('fig_8_5_lead_slab'))
d.basic('Correction: NCERT Example 8.4 writes the stress as 9.4 × 10⁴ N / 0.05 m². What is right?', 'The force is ' + T('9.0 × 10⁴ N') + ' (as given); 9.0 × 10⁴ / 0.05 = 1.8 × 10⁶ Pa, which is the value NCERT then uses')
d.basic('Exercise 8.6: Al cube, edge 10 cm, one face fixed to a wall, 100 kg hung on the opposite face, G = 25 GPa. Vertical deflection?', 'Δx = FL/(AG) = 980 × 0.1 / (0.01 × 2.5 × 10¹⁰) ≈ ' + N('3.9 × 10⁻⁷ m'))
d.basic('Correction: NCERT’s answer key gives 4 × 10⁻⁶ m for Exercise 8.6. Check.', 'Recomputing: 98 / (2.5 × 10⁸) = ' + T('3.92 × 10⁻⁷ m') + '. The key is ten times too large')

d.sec('8.5.3-bulk-modulus')
d.basic('Define bulk modulus.', r'\( B = -\dfrac{p}{\Delta V/V} \)' + '; the minus sign makes B positive, since ΔV < 0 when p rises')
d.basic('Define compressibility.', r'\( k = \dfrac{1}{B} = -\dfrac{1}{\Delta p}\dfrac{\Delta V}{V} \)' + ': fractional volume change per unit pressure')
d.basic('Order of bulk moduli: solids, liquids, gases?', 'Solids > liquids ≫ gases; gases are about a ' + T('million times') + ' more compressible than solids', **fig('tab_8_3_bulk_moduli'))
d.basic('Why are solids so incompressible?', 'Tight coupling between neighbouring ' + T('atoms') + '; in liquids the coupling is weaker, in gases very weak')
d.basic('Which modulus applies to solids, liquids and gases?', T('Bulk modulus') + ' only')
d.basic('Bulk modulus of water and of air (STP)?', 'Water ' + N('2.2 × 10⁹ Pa') + '; air ' + N('1.0 × 10⁵ Pa'))
d.basic('Example 8.5: fractional compression of water at the bottom of the Indian Ocean (3000 m)?', 'p = hρg = 3 × 10⁷ Pa; ΔV/V = p/B = ' + N('1.36 %'))
table_card(d, 'Table 8.4 · summary of moduli', 'Change in shape / volume?', [
    ('Young’s modulus Y (tensile/compressive)', 'shape: yes, volume: no', False),
    ('Shear modulus G', 'shape: yes, volume: no', False),
    ('Bulk modulus B (hydraulic)', 'shape: no, volume: yes', False)], term='Stress, strain and moduli at a glance (Table 8.4)')
d.basic('Exercise 8.12: 100.0 L of water compressed by 0.5 L under 100 atm. Bulk modulus? Compare with air.', N('2.0 × 10⁹ Pa') + ', about ' + N('2 × 10⁴') + ' times that of air (B = p ≈ 10⁵ Pa at constant T): molecules in a liquid are tightly packed')
d.basic('Exercise 8.16: pressure change to compress a litre of water by 0.10 %?', 'Δp = B × 0.001 = ' + N('2.2 × 10⁶ Pa'))
d.basic('Exercise 8.13: density of water at 80.0 atm if 1.03 × 10³ kg/m³ at the surface?', r'\( \rho = \dfrac{\rho_0}{1 - p/B} \approx \)' + ' ' + N('1.034 × 10³ kg/m³'))

d.sec('8.5.4-poissons-ratio')
d.basic('Define Poisson’s ratio.', r'\( \dfrac{\text{lateral strain}}{\text{longitudinal strain}} = \dfrac{\Delta d/d}{\Delta L/L} \)'.replace(r'\text{lateral strain}', 'lateral\\ strain').replace(r'\text{longitudinal strain}', 'longitudinal\\ strain') + '; no units')
d.basic('Typical Poisson’s ratio for steel and aluminium alloys?', 'Steel ' + N('0.28–0.30') + '; aluminium alloys ≈ ' + N('0.33'))
d.basic('What is lateral strain?', 'Strain ' + T('perpendicular') + ' to the applied force (the wire gets thinner as it lengthens)')

d.sec('8.5.5-elastic-potential-energy')
d.basic('Elastic potential energy stored in a stretched wire?', r'\( U = \tfrac12 \dfrac{YAl^2}{L} = \tfrac12 \times \sigma \times \varepsilon \times \text{volume} \)'.replace(r'\text{volume}', 'V'))
d.basic('Elastic energy per unit volume?', r'\( u = \tfrac12\,\sigma\varepsilon = \tfrac12 Y\varepsilon^2 = \dfrac{\sigma^2}{2Y} \)')
d.basic('Teacher addition: why is the energy ½ F l, not F l?', 'The force grows from 0 to F as the wire stretches; the average force is F/2 (triangle under the F–l line)')

# ---------------------------------------------------------------- 8.6 Applications
d.sec('8.6-applications')
d.basic('Crane rope for 10 tonnes, mild steel σᵧ = 300 MPa. Minimum area and practical radius?', 'A ≥ Mg/σᵧ = ' + N('3.3 × 10⁻⁴ m²') + ' (r ≈ 1 cm); with a safety factor of 10, r ≈ ' + N('3 cm'))
d.basic('Why are crane ropes made of many braided thin wires?', 'For ease of manufacture, ' + T('flexibility') + ' and strength; a single 3 cm wire would be a rigid rod')
d.basic('Sag of a beam loaded at the centre?', r'\( \delta = \dfrac{Wl^3}{4bd^3Y} \)', **fig('fig_8_6_beam'))
d.basic('To reduce bending of a beam, increase breadth or depth?', T('Depth') + ': δ ∝ 1/d³ but only 1/b')
d.basic('Why are beams given an I-shaped cross-section?', 'Enough depth to resist bending, less material and weight, and it avoids ' + T('buckling') + ' of a deep thin bar', **fig('fig_8_7_beam_sections'))
d.basic('Pillar with rounded ends vs distributed (flared) ends?', 'The one with ' + T('distributed ends') + ' supports more load', **fig('fig_8_8_pillars'))
d.basic('Why can mountains on Earth not be much higher than ~10 km?', 'At height h the base shear stress ≈ hρg; rock flows beyond ~3 × 10⁸ Pa: h ≈ 3 × 10⁸ / (3 × 10³ × 10) = ' + N('10 km'))
d.basic('Exercise 8.7: four hollow steel columns (radii 30 and 60 cm) share 50 000 kg. Compressional strain of each?', 'F = 50 000 × 9.8 / 4, A = π(0.6² − 0.3²) = 0.848 m² → strain ≈ ' + N('7.2 × 10⁻⁷') + ' (Y = 2 × 10¹¹ Pa)')
d.basic('Correction: NCERT’s key gives 2.8 × 10⁻⁶ for Exercise 8.7. Check.', 'That equals the strain if ' + X('one column carried the whole load') + '. Shared by four columns, as the question says: ' + T('7.2 × 10⁻⁷'))

d.sec('summary')
table_card(d, 'Points to ponder', 'True or false?', [
    ('Hooke’s law holds all the way to the breaking point', 'False (linear part only)', True),
    ('A material that stretches more is more elastic', 'False', True),
    ('Bulk modulus applies to gases too', 'True', False),
    ('Stress is a vector', 'False', True),
    ('A longitudinal stress also changes the width of a wire', 'True (Poisson’s ratio)', False)], term='Chapter 8 concept checks')
table_card(d, 'Summary', 'Formula?', [
    ('Young’s modulus', 'Y = FL / (AΔL)', False), ('Shear modulus', 'G = F / (Aθ)', False),
    ('Bulk modulus', 'B = −p / (ΔV/V)', False), ('Elastic energy density', 'u = ½ stress × strain', False)], term='Chapter 8 formula sheet')

print(d.write(os.path.join(OUT, 'deck.json')), 'cards')
