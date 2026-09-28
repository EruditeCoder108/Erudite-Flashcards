import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase_phy as sp

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Physics', 'class11-physics-ch09-mechanical-properties-of-fluids')
d = Deck('Chapter 9: Mechanical Properties of Fluids', 'Class 11', ['class-11', 'physics', 'ch-9'])
d.description = 'Pressure, Pascal’s law, hydraulics, continuity, Bernoulli’s principle, Torricelli, lift, viscosity, Stokes’ law, surface tension, capillarity'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- 9.1 Introduction
d.sec('9.1-introduction')
d.basic('What makes a substance a fluid?', 'It can ' + T('flow') + ': liquids and gases')
d.basic('Key mechanical difference between fluids and solids?', 'Fluids offer very little resistance to ' + T('shear stress') + ' (about a million times less than solids); they have no shape of their own')
d.basic('Liquid vs gas: volume?', 'A liquid has a fixed volume and a free surface; a gas fills its container and is highly ' + T('compressible'))

# ---------------------------------------------------------------- 9.2 Pressure
d.sec('9.2-pressure')
d.basic('Why does a needle pierce the skin but a spoon does not, for the same force?', 'Smaller area → larger ' + T('pressure') + ' (force per unit area)')
d.basic('Why is the force of a fluid at rest always normal to a surface?', 'A parallel component would make the fluid ' + T('flow') + ' (third law); a fluid at rest cannot', **fig('fig_9_1_normal_force'))
d.basic('Define pressure; scalar or vector?', r'\( P = \lim_{\Delta A \to 0}\dfrac{\Delta F}{\Delta A} \)' + ' (normal force per area): a ' + T('scalar') + '; unit pascal, [M L⁻¹ T⁻²]')
d.basic('1 atm, 1 bar, 1 torr in Pa?', '1 atm = ' + N('1.013 × 10⁵ Pa') + '; 1 bar = ' + N('10⁵ Pa') + '; 1 torr = 1 mm Hg = ' + N('133 Pa'))
d.basic('Relative density; density of water at 4 °C?', 'Density ÷ density of water at 4 °C (dimensionless). Water: ' + N('1.0 × 10³ kg m⁻³'), **fig('tab_9_1_densities'))
d.basic('Example 9.1: two femurs (10 cm² each) carry 40 kg. Average pressure?', '400 N / 20 × 10⁻⁴ m² = ' + N('2 × 10⁵ Pa'))
d.basic('Exercise 9.5: a 50 kg girl balances on one circular heel of diameter 1.0 cm. Pressure?', N('6.2 × 10⁶ Pa'))

d.sec('9.2.1-pascals-law')
d.cloze('Pascal’s law: in a fluid at rest, pressure is the {{c1::same in all directions}} and the same at all points at the {{c2::same height}}.')
d.basic('How is Pascal’s law proved with a small prism?', 'Balance forces on a tiny right-angled prism: Fb sin θ = Fc, Fb cos θ = Fa with Ab sin θ = Ac, Ab cos θ = Aa → ' + T('Pa = Pb = Pc'), **fig('fig_9_2_pascal_prism'))
d.basic('Why must pressure be equal at points on the same horizontal level?', 'Otherwise a horizontal fluid bar would have a net force and ' + T('flow'))

d.sec('9.2.2-variation-with-depth')
d.basic('Pressure difference between two points h apart vertically?', r'\( P_2 - P_1 = \rho g h \)', **fig('fig_9_3_fluid_column'))
d.basic('Pressure at depth h in a liquid open to the air?', r'\( P = P_a + \rho g h \)' + '; P − Pₐ is the ' + T('gauge pressure'))
d.basic('What is the hydrostatic paradox?', 'Vessels of different shapes joined at the bottom fill to the ' + T('same height') + ': pressure depends only on depth, not on shape or amount of liquid', **fig('fig_9_4_hydrostatic_paradox'))
d.basic('Example 9.2: pressure on a swimmer 10 m below a lake surface?', N('2.01 × 10⁵ Pa ≈ 2 atm') + ' (a 100 % increase)')
d.basic('Example 9.4: at 1000 m in the sea (ρ = 1.03 × 10³): absolute and gauge pressure; force on a 20 cm × 20 cm submarine window?', N('≈ 104 atm') + ' and ' + N('≈ 103 atm') + '; F = gauge pressure × 0.04 m² = ' + N('4.12 × 10⁵ N'))
d.basic('Exercise 9.1(a): why is blood pressure greater at the feet than at the brain?', 'The blood column above the feet is taller: extra ' + T('ρgh'))
d.basic('Exercise 9.7: an off-shore structure can take 10⁹ Pa. Suitable for 3 km of ocean?', T('Yes') + ': pressure there ≈ 3 × 10⁷ Pa, far less')

d.sec('9.2.3-atmospheric-and-gauge-pressure')
d.basic('Who invented the mercury barometer, and how does it work?', T('Torricelli') + ': a mercury-filled tube inverted in mercury; the column height h gives ' + r'\( P_a = \rho g h \)' + ' (≈ 76 cm Hg)', **fig('fig_9_5a_barometer'))
d.basic('What does an open-tube manometer measure?', 'The ' + T('gauge pressure') + ' P − Pₐ = ρgh; oil for small differences, mercury for large ones', **fig('fig_9_5b_manometer'))
d.basic('Example 9.3: if air had constant density 1.29 kg/m³, how high would the atmosphere reach?', '≈ ' + N('8 km') + ' (in reality density and g fall; the atmosphere extends beyond 100 km)')
d.basic('What does a drop of 10 mm or more in a barometer reading signal?', 'An approaching ' + T('storm'))
d.basic('Exercise 9.6: height of a French-wine barometer (ρ = 984 kg/m³)?', N('≈ 10.5 m'))
d.basic('Exercise 9.1(b): why does air pressure halve by 6 km though the atmosphere is > 100 km thick?', 'Air is compressible: most of it is ' + T('packed near the ground') + ', so density falls rapidly with height')
d.basic('Exercise 9.9: 10.0 cm of water balances 12.5 cm of spirit over mercury. Specific gravity of spirit?', N('0.800'))

d.sec('9.2.4-hydraulic-machines')
d.basic('Pascal’s law, second form?', 'Pressure applied to an enclosed fluid is transmitted ' + T('undiminished and equally in all directions'), **fig('fig_9_6a_pascal_transmission'))
d.basic('Force on the big piston of a hydraulic lift?', r'\( F_2 = F_1\dfrac{A_2}{A_1} \)' + '; mechanical advantage A₂/A₁', **fig('fig_9_6b_hydraulic_lift'))
d.basic('Trap: does a hydraulic lift give free energy?', X('No') + ': the large piston moves a smaller distance; ' + T('A₁d₁ = A₂d₂') + ' (same volume), so work in = work out')
d.basic('Example 9.5: syringes of diameter 1.0 cm and 3.0 cm; 10 N on the small one, pushed in 6.0 cm. Force and movement of the big one?', N('90 N') + ' and ' + N('0.67 cm'))
d.basic('Example 9.6: car lift, pistons of radius 5.0 cm and 15 cm, car 1350 kg. Force F₁ and air pressure needed?', N('≈ 1.5 × 10³ N') + ' and ' + N('1.9 × 10⁵ Pa') + ' (about 2 atm)')
d.basic('Why do hydraulic brakes brake all wheels equally?', 'The pedal’s pressure is transmitted ' + T('equally to all four wheel cylinders') + ' through the brake oil')
d.basic('Exercise 9.8: hydraulic lift for 3000 kg, load piston 425 cm². Maximum pressure on the small piston?', N('6.92 × 10⁵ Pa') + ' (same pressure everywhere)')

# ---------------------------------------------------------------- 9.3 Streamline flow
d.sec('9.3-streamline-flow')
d.basic('When is flow steady?', 'When the velocity of fluid at ' + T('each point') + ' stays constant in time (it may differ from point to point)')
d.basic('Define a streamline.', 'The path of a fluid particle in steady flow; its ' + T('tangent') + ' gives the fluid velocity at each point', **fig('fig_9_7_streamlines'))
d.basic('Why can two streamlines never cross?', 'At the crossing a particle would have ' + T('two velocities') + '; the flow would not be steady')
d.basic('Equation of continuity?', r'\( A_1v_1 = A_2v_2 \)' + ' (Av = constant) for an incompressible fluid: ' + T('conservation of mass'))
d.basic('What do crowded streamlines mean?', T('Higher speed') + ' (narrow cross-section)')
d.basic('Laminar vs turbulent flow?', T('Laminar') + ': layers slide smoothly, parallel velocities. ' + T('Turbulent') + ': irregular, eddies, above a ' + T('critical speed'), **fig('fig_9_8_laminar_turbulent'))
d.basic('Teacher addition (JEE): Reynolds number and its meaning?', r'\( R_e = \dfrac{\rho v d}{\eta} \)' + ': < ~1000 laminar, > ~2000 turbulent')
d.basic('Exercise 9.4(b): why does water gush out fast when you cover most of a tap with your fingers?', 'Smaller outlet area → larger speed (Av = constant)')
d.basic('Exercise 9.16: spray pump tube 8.0 cm², 40 holes of 1.0 mm diameter, flow 1.5 m/min inside. Ejection speed?', N('0.64 m/s') + ' (continuity)')

# ---------------------------------------------------------------- 9.4 Bernoulli
d.sec('9.4-bernoullis-principle')
d.basic('State Bernoulli’s equation.', r'\( P + \tfrac12\rho v^2 + \rho g h = \text{constant} \)'.replace(r'\text{constant}', 'constant') + ' along a streamline')
d.basic('What does each term of Bernoulli’s equation mean?', 'P: pressure (work per volume); ½ρv²: ' + T('KE per unit volume') + '; ρgh: ' + T('PE per unit volume'))
d.basic('Bernoulli’s equation is an expression of which principle?', 'Conservation of ' + T('energy') + ' (work-energy theorem applied to a fluid element)', **fig('fig_9_9_bernoulli_pipe'))
d.basic('Correction: NCERT says the work-energy theorem is in "Chapter 6". Where is it?', T('Chapter 5') + ' (Work, Energy and Power); left over from the old numbering')
table_card(d, '9.4 · limits of Bernoulli', 'Assumption needed?', [
    ('Viscosity', 'zero (non-viscous fluid)', False), ('Compressibility', 'incompressible', False),
    ('Type of flow', 'steady, streamline (not turbulent)', False)], term='When Bernoulli’s equation applies')
d.basic('Bernoulli’s equation for a fluid at rest?', 'Reduces to ' + r'\( P_1 - P_2 = \rho g(h_2 - h_1) \)' + ' — the hydrostatic result')
d.basic('Daniel Bernoulli gave the equation in which year?', N('1738'))
sp.venturi_flow(d)
d.basic('Exercise 9.15: which of the two flows through a constriction is wrong?', 'The one showing ' + X('higher') + ' liquid level (pressure) at the constriction: there v is larger, so P must be lower', **img('fig_9_20_flow_ex'))
d.basic('Exercise 9.11: can Bernoulli’s equation describe water through river rapids?', X('No') + ': the flow is turbulent, not streamline')
d.basic('Exercise 9.12: does it matter if gauge pressure is used in Bernoulli’s equation?', X('No') + ', unless the atmospheric pressure differs significantly between the two points')

d.sec('9.4.1-torricelli')
d.basic('Torricelli’s law: speed of efflux from a hole h below the surface of an open tank?', r'\( v = \sqrt{2gh} \)' + ' — same as free fall from h', **fig('fig_9_10_torricelli'))
d.basic('Speed of efflux from a closed tank at pressure P?', r'\( v = \sqrt{2gh + \dfrac{2(P - P_a)}{\rho}} \)' + '; if P ≫ Pₐ the pressure term dominates (rocket propulsion)')
d.basic('Exercise 9.4(d): why does fluid leaving a hole push the vessel backwards?', 'The out-flowing fluid carries momentum; by the third law the vessel gets an equal ' + T('backward thrust'))

d.sec('9.4.2-dynamic-lift')
d.basic('What is dynamic lift?', 'Force on a body such as a wing, hydrofoil or spinning ball due to its ' + T('motion through a fluid'))
d.basic('Magnus effect: why does a spinning ball swerve?', 'Spin drags air: relative air speed is larger on one side → ' + T('lower pressure') + ' there → sideways/upward force', **fig('fig_9_11_lift'))
d.basic('Why does an aerofoil give lift?', 'Its shape and tilt crowd streamlines ' + T('above') + ' the wing: faster air, lower pressure above than below')
d.basic('Example 9.7: 3.3 × 10⁵ kg aircraft, wing area 500 m², 960 km/h. Pressure difference and speed difference?', 'ΔP = ' + N('6.5 × 10³ Pa') + '; air above needs to be only ≈ ' + N('8 %') + ' faster')
d.basic('Exercise 9.14: wind-tunnel wing, speeds 70 and 63 m/s, area 2.5 m², ρ = 1.3. Lift?', '½ρ(v₂² − v₁²)A ≈ ' + N('1.5 × 10³ N'))
d.basic('Exercise 9.4(a): to keep paper horizontal, blow over it or under it?', T('Over') + ': faster air above → lower pressure above → paper lifts')

# ---------------------------------------------------------------- 9.5 Viscosity
d.sec('9.5-viscosity')
d.basic('What is viscosity?', 'Internal ' + T('friction') + ' between fluid layers moving relative to each other')
d.basic('Velocity profile of a liquid between a fixed and a moving plate; in a pipe?', 'Plates: rises ' + T('uniformly') + ' from 0 to v. Pipe: maximum at the ' + T('axis') + ', zero at the walls', **fig('fig_9_12_viscous_layers'))
d.basic('Define the coefficient of viscosity.', r'\( \eta = \dfrac{F/A}{v/l} \)' + ': shear stress ÷ ' + T('rate of shear strain'))
d.basic('Solid vs fluid under shear: stress depends on what?', 'Solid: on shear ' + T('strain') + '. Fluid: on the ' + T('rate') + ' of shear strain (Exercise 9.3c)')
d.basic('SI unit and dimensions of viscosity?', T('poiseuille (Pl)') + ' = N s m⁻² = Pa s; [M L⁻¹ T⁻¹]')
d.basic('Effect of temperature on viscosity?', 'Liquids: η ' + X('decreases') + ' (molecules more mobile). Gases: η ' + T('increases') + ' (more random motion)', **fig('tab_9_2_viscosities'))
d.basic('Example 9.8: 0.10 m² block on a 0.30 mm oil film pulled by 0.010 kg at a steady 0.085 m/s. η?', 'η = (0.098/0.10) / (0.085/3 × 10⁻⁴) = ' + N('3.46 × 10⁻³ Pa s'), **fig('fig_9_13_viscosity_block'))
d.basic('Exercise 9.4(c): why does needle size control injection flow better than thumb pressure?', 'Flow through a narrow tube depends very strongly on its radius (∝ r⁴ in viscous flow), much more than on pressure')

d.sec('9.5.1-stokes-law')
d.basic('State Stokes’ law.', r'\( F = 6\pi\eta a v \)' + ': viscous drag on a sphere of radius a moving at v')
d.basic('Terminal velocity of a sphere in a fluid?', r'\( v_t = \dfrac{2a^2(\rho - \sigma)g}{9\eta} \)' + ' (ρ sphere, σ fluid)')
sp.terminal_velocity(d)
d.basic('Why do raindrops not hit us at bullet speeds?', 'Air drag grows with speed; they reach a small ' + T('terminal velocity'))
d.basic('Example 9.9: copper ball (radius 2.0 mm) reaches 6.5 cm/s in oil (1.5 × 10³ kg/m³). η of oil?', N('≈ 0.99 Pa s'))
d.basic('Correction: NCERT 9.5.1 says "refer back to Example 6.2". Which example?', 'The raindrop example is ' + T('Example 5.2') + ' (Work, Energy and Power)')
d.basic('Exercise 9.13: glycerine through a 1.5 m tube (r = 1.0 cm), 4.0 × 10⁻³ kg/s. Pressure difference?', N('≈ 9.8 × 10² Pa') + ' (Poiseuille; Reynolds number ≈ 0.3, so laminar)')

# ---------------------------------------------------------------- 9.6 Surface tension
d.sec('9.6-surface-tension')
d.basic('Why do surface molecules have extra energy?', 'They have neighbours on only one side, so less (negative) binding energy — about ' + T('half') + ' that of a molecule inside', **fig('fig_9_14_surface_molecules'))
d.basic('Why does a liquid tend to minimise its surface area?', 'Creating surface costs energy; the liquid takes the ' + T('least area') + ' that conditions allow')
d.basic('Define surface tension (two ways).', 'Force per unit length in the surface, or ' + T('surface energy per unit area') + '; unit N/m = J/m²')
d.basic('A film on a wire frame with a slider of length l needs force F. Surface tension?', r'\( S = \dfrac{F}{2l} \)' + ' — the film has ' + T('two surfaces'), **fig('fig_9_15_film'))
d.basic('Effect of temperature on surface tension?', 'Usually ' + X('decreases') + ' as temperature rises', **fig('tab_9_3_surface_tension'))
d.basic('Surface tension of water and mercury at 20 °C?', 'Water ' + N('0.0727 N/m') + '; mercury ' + N('0.4355 N/m'))
d.basic('How can surface tension be measured with a balance?', 'Raise a liquid to touch a glass plate hung from the balance; extra weight to free it: ' + r'\( S = \dfrac{mg}{2l} \)', **fig('fig_9_16_balance'))
d.basic('Is surface tension a property of one liquid alone?', X('No') + ': it belongs to the ' + T('interface') + ' between two substances, at least one a fluid')
d.basic('Exercise 9.2(c): why is surface tension independent of surface area?', 'It is energy per unit area (or force per unit length) — a property of the interface, not of its size')
d.basic('Exercise 9.17: a soap film on a 30 cm slider supports 1.5 × 10⁻² N. Surface tension?', 'S = F/2l = ' + N('2.5 × 10⁻² N/m'))
d.basic('Exercise 9.18: a film supports 4.5 × 10⁻² N in (a). In the other frames with the same slider length?', 'The ' + T('same 4.5 × 10⁻² N') + ': the force depends only on the length of the slider', **img('fig_9_21_films_ex'))

d.sec('9.6.3-angle-of-contact')
d.basic('Define angle of contact.', 'Angle between the ' + T('tangent to the liquid surface') + ' at the point of contact and the solid surface, measured inside the liquid', **fig('fig_9_17_contact_angle'))
d.basic('Equilibrium of interfacial tensions at the contact line?', r'\( S_{la}\cos\theta + S_{sl} = S_{sa} \)')
d.basic('Acute vs obtuse angle of contact: wetting?', T('Acute') + ' (water on glass, kerosene on anything): liquid wets and spreads. ' + T('Obtuse') + ' (water on lotus leaf, mercury on glass): forms drops')
d.basic('Why is mercury’s contact angle with glass obtuse?', 'Mercury molecules attract ' + T('each other') + ' more strongly than they attract glass')
d.basic('Why do detergents help cleaning, and waterproofing agents do the opposite?', 'Detergents make the contact angle ' + T('small') + ' (penetrate fibres); waterproofing makes it ' + T('large'))

d.sec('9.6.4-drops-and-bubbles')
d.basic('Why are free drops and bubbles spherical?', 'For a given volume a ' + T('sphere has the least surface area') + ' (least surface energy)')
table_card(d, '9.6.4 · excess pressure inside', 'Pᵢ − P₀ = ?', [
    ('Liquid drop (one surface)', '2S / r', False), ('Air bubble in a liquid (one surface)', '2S / r', False),
    ('Soap bubble in air (two surfaces)', '4S / r', False)], note='The concave side is always at higher pressure.', term='Excess pressure in drops and bubbles', )
d.basic('Identify: which of (a), (b), (c) is a drop, a cavity (air bubble in liquid) and a soap bubble?', '(a) drop, (b) cavity: 2S/r; (c) soap bubble with two surfaces: 4S/r', **fig('fig_9_18_drop_bubble'))
d.basic('Example 9.10: capillary (diameter 2.00 mm) 8.00 cm under water; pressure to blow a hemispherical bubble at its end?', 'P₀ = 1.01784 × 10⁵ Pa; excess 2S/r = ' + N('146 Pa') + ' → ' + N('1.02 × 10⁵ Pa'))
d.basic('Exercise 9.19: mercury drop, r = 3.00 mm, S = 0.465 N/m. Excess pressure?', '2S/r = ' + N('310 Pa'))
d.basic('Exercise 9.20: soap bubble, r = 5.00 mm, S = 2.50 × 10⁻² N/m. Excess pressure?', '4S/r = ' + N('20 Pa'))

d.sec('9.6.5-capillary-rise')
d.basic('Height of capillary rise?', r'\( h = \dfrac{2S\cos\theta}{\rho g a} \)' + ' (a = tube radius)', **fig('fig_9_19_capillary'))
d.basic('Why does water rise in a capillary tube?', 'The meniscus is ' + T('concave') + ', so the pressure just under it is below atmospheric; water rises until ρgh makes up the difference')
d.basic('Capillary rise of water in a tube of radius 0.05 cm?', N('≈ 2.98 cm') + ' — larger for thinner tubes (h ∝ 1/a)')
d.basic('What happens to mercury in a glass capillary?', 'It is ' + X('depressed') + ' below the outside level (θ obtuse, cos θ < 0)')
d.basic('Everyday examples of capillarity?', 'Oil rising up a ' + E('lamp wick') + ', sap and water rising in ' + E('plants') + ', paint-brush hairs forming a tip when wet')

# ---------------------------------------------------------------- Buoyancy (teacher addition)
d.sec('buoyancy-teacher-addition')
d.basic('Teacher addition: Archimedes’ principle?', 'A body in a fluid feels an upward ' + T('buoyant force') + ' equal to the weight of fluid displaced: F = σVg')
d.basic('Teacher addition: fraction of a floating body that is submerged?', r'\( \dfrac{V_{in}}{V} = \dfrac{\rho_{body}}{\rho_{fluid}} \)' + ' (ice in water: about 90 %)')

d.sec('summary')
table_card(d, 'Exercise 9.3', 'Fill in the blank?', [
    ('Surface tension with temperature', 'decreases', False), ('Viscosity of gases with temperature', 'increases', False),
    ('Viscosity of liquids with temperature', 'decreases', True), ('Speed-up at a constriction follows', 'conservation of mass', False),
    ('Turbulence speed for a wind-tunnel model vs real plane', 'greater', False)], term='Fluid facts (Exercise 9.3)')
table_card(d, 'Summary', 'Formula?', [
    ('Pressure at depth', 'P = Pₐ + ρgh', False), ('Continuity', 'A₁v₁ = A₂v₂', False), ('Bernoulli', 'P + ½ρv² + ρgh = constant', False),
    ('Stokes’ drag', '6πηav', False), ('Capillary rise', 'h = 2S cos θ / ρga', False)], term='Chapter 9 formula sheet')

print(d.write(os.path.join(OUT, 'deck.json')), 'cards')
