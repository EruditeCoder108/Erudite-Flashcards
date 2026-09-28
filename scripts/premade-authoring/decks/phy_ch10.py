import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Physics', 'class11-physics-ch10-thermal-properties-of-matter')
d = Deck('Chapter 10: Thermal Properties of Matter', 'Class 11', ['class-11', 'physics', 'ch-10'])
d.description = 'Temperature scales, ideal gas, thermal expansion, specific heat, calorimetry, change of state, latent heat, conduction, convection, radiation, Newton’s cooling'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- 10.2 Temperature and heat
d.sec('10.2-temperature-and-heat')
d.basic('Temperature vs heat?', T('Temperature') + ': measure of hotness (K, °C). ' + T('Heat') + ': energy transferred because of a ' + T('temperature difference') + ' (J)')
d.basic('Why is touch not a good thermometer?', 'It is ' + X('unreliable') + ' and its range is too limited')
d.basic('Any energy transfer without a temperature difference: is it heat?', X('No') + ' (e.g. work done by stirring is not heat)')

# ---------------------------------------------------------------- 10.3 Measurement
d.sec('10.3-measurement-of-temperature')
d.basic('Why does a temperature scale need fixed points?', 'All substances expand, so there is no absolute reference; we use phenomena that always happen at the ' + T('same temperature') + ' (ice point, steam point)')
d.basic('Ice and steam points on the Celsius and Fahrenheit scales?', 'Celsius: ' + N('0 °C, 100 °C') + ' (100 divisions). Fahrenheit: ' + N('32 °F, 212 °F') + ' (180 divisions)', **fig('fig_10_1_f_vs_c'))
d.basic('Celsius–Fahrenheit conversion?', r'\( \dfrac{t_F - 32}{180} = \dfrac{t_C}{100} \)' + ', i.e. ' + r'\( t_F = \tfrac95 t_C + 32 \)')
d.basic('At what temperature do Celsius and Fahrenheit readings agree?', N('−40°') + ' (solve x = 9x/5 + 32)')
d.basic('Teacher addition: general rule to convert between any two linear scales?', r'\( \dfrac{X - \text{LFP}}{\text{UFP} - \text{LFP}} \)'.replace(r'\text{LFP}', 'L').replace(r'\text{UFP}', 'U') + ' is the same on every scale (L = lower, U = upper fixed point)')

# ---------------------------------------------------------------- 10.4 Ideal gas, absolute temperature
d.sec('10.4-ideal-gas-and-absolute-temperature')
d.basic('Boyle’s law and Charles’ law?', T('Boyle') + ' (T constant): PV = constant. ' + T('Charles') + ' (P constant): V/T = constant')
d.basic('Ideal gas equation?', r'\( PV = \mu RT \)' + ', R = ' + N('8.31 J mol⁻¹ K⁻¹') + ', μ = number of moles')
d.basic('Why is a gas thermometer better than a liquid-in-glass one?', 'All low-density gases expand the same way, so a gas thermometer reads the same ' + T('whichever gas') + ' is used')
d.basic('Constant-volume gas thermometer: what is read?', T('Pressure') + ': at constant V, P ∝ T', **fig('fig_10_2_p_vs_t'))
d.basic('How is absolute zero found?', 'Extrapolate P–T lines of low-density gases to P = 0: all meet at ' + N('−273.15 °C'), **fig('fig_10_3_absolute_zero'))
d.basic('Kelvin–Celsius relation?', r'\( T = t_C + 273.15 \)' + '; one kelvin = one Celsius degree', **fig('fig_10_4_scales'))
d.basic('Absolute zero in °F?', N('−459.67 °F') + ' (NCERT’s Fig. 10.4 prints −459.69 °F; the accepted value is −459.67 °F)')
d.basic('Why is the triple point of water the modern fixed point (Exercise 10.4a)?', 'It has a ' + T('unique temperature') + ' (273.16 K); melting and boiling points depend on pressure')
d.basic('Why is T = t_C + 273.15 and not + 273.16 (Exercise 10.4c)?'.replace('t_C', 'tc'), 'The triple point is ' + T('0.01 °C') + ' = 273.16 K; the melting point of ice (0 °C) is 273.15 K')
d.basic('Exercise 10.4(d): triple point of water on an absolute scale with Fahrenheit-sized degrees?', N('491.69') + ' (273.16 × 9/5)')
d.basic('Exercise 10.2: absolute scales A and B give the triple point as 200 A and 350 B. Relation?', r'\( T_A = \tfrac47 T_B \)')
d.basic('Exercise 10.3: R = 101.6 Ω at 273.16 K, 165.5 Ω at 600.5 K (linear). Temperature when R = 123.4 Ω?', N('≈ 384.8 K'))
d.basic('Exercise 10.5: why do oxygen and hydrogen gas thermometers disagree slightly? Remedy?', 'Real gases are ' + T('not perfectly ideal') + '. Take readings at lower and lower pressures and extrapolate to P → 0')

# ---------------------------------------------------------------- 10.5 Thermal expansion
d.sec('10.5-thermal-expansion')
d.basic('Why does dipping a tight metal lid in hot water help open a bottle?', 'The metal lid ' + T('expands') + ' more than the glass')
d.basic('Three kinds of thermal expansion?', T('Linear') + ' (length), ' + T('area') + ', ' + T('volume'), **fig('fig_10_5_expansion'))
d.basic('Coefficient of linear expansion?', r'\( \dfrac{\Delta l}{l} = \alpha_l\,\Delta T \)')
d.basic('Table 10.1: αₗ of copper vs glass (pyrex)?', 'Copper ' + N('1.7 × 10⁻⁵ K⁻¹') + ' vs pyrex ' + N('0.32 × 10⁻⁵ K⁻¹') + ': copper expands about 5 times more', **fig('tab_10_1_linear_expansion'))
d.basic('Coefficient of volume expansion?', r'\( \dfrac{\Delta V}{V} = \alpha_V\,\Delta T \)' + '; not strictly constant — depends on temperature', **fig('fig_10_6_copper_alpha_v'))
d.basic('Relations between αₗ, α_A and α_V (isotropic solid)?'.replace('α_A', 'αA').replace('α_V', 'αV'), r'\( \alpha_A = 2\alpha_l,\quad \alpha_V = 3\alpha_l \)')
steps_card(d, 'Example 10.1 · area expansion', 'Find the missing step.', 'Show that the coefficient of area expansion of a rectangular sheet is 2αₗ.',
           ['Δa = αₗaΔT, Δb = αₗbΔT', 'ΔA = aΔb + bΔa + ΔaΔb', '= αₗAΔT(2 + αₗΔT)', 'αₗΔT ≪ 2, so <b>ΔA/A = 2αₗΔT</b>'], 2,
           'Coefficient of area expansion = 2αl', 'ΔA = aΔb + bΔa + ΔaΔb = αl A ΔT (2 + αl ΔT) ≈ 2αl A ΔT')
d.basic('Identify: which strips make up the extra area in Fig. 10.8?', 'ΔA₁ = aΔb, ΔA₂ = bΔa and the tiny corner ΔaΔb (neglected)', **fig('fig_10_8_area_expansion'))
d.basic('Which have very low expansion: name two.', T('Invar') + ' (iron–nickel alloy, αV ≈ 2 × 10⁻⁶ K⁻¹) and ' + T('pyrex glass'))
d.basic('Which expands more for the same rise: alcohol or mercury?', T('Alcohol') + ' (αV ≈ 110 × 10⁻⁵ vs 18.2 × 10⁻⁵ K⁻¹)')
d.basic('Anomalous expansion of water?', 'Water ' + X('contracts') + ' on heating from 0 °C to 4 °C; density is ' + T('maximum at 4 °C'), **fig('fig_10_7_water_anomaly'))
d.basic('Why do lakes freeze from the top, and why does it matter?', 'Water below 4 °C is less dense and stays on top where it freezes; the water underneath stays near 4 °C, so ' + T('aquatic life survives'))
d.basic('Volume expansivity of an ideal gas at constant pressure?', r'\( \alpha_V = \dfrac1T \)' + ' (≈ 3.7 × 10⁻³ K⁻¹ at 0 °C) — far larger than for solids and liquids')
d.basic('What is thermal stress?', 'Stress in a body ' + T('prevented from expanding') + ': strain = αΔT, stress = YαΔT')
d.basic('Steel rail (40 cm², α = 1.2 × 10⁻⁵ K⁻¹, Y = 2 × 10¹¹ Pa) fixed at both ends, heated 10 °C. Thermal stress and force?', 'Stress = ' + N('2.4 × 10⁷ Pa') + '; force ≈ ' + N('10⁵ N') + ' — enough to bend rails (hence gaps between rails)')
d.basic('Example 10.2: iron ring 5.231 m fits a 5.243 m wooden rim at 27 °C. To what temperature must the ring be heated?', N('≈ 218 °C'))
d.basic('Exercise 10.7: steel shaft 8.70 cm, wheel hole 8.69 cm at 27 °C. Cool the shaft to what temperature?', N('≈ −69 °C'))
d.basic('Exercise 10.8: a hole of 4.24 cm in a copper sheet, heated from 27 °C to 227 °C. Change in diameter?', T('Increases') + ' by ' + N('1.44 × 10⁻² cm') + ': a hole expands like the material around it')
d.basic('Exercise 10.9: brass wire 1.8 m, 2.0 mm diameter, held taut and cooled from 27 °C to −39 °C. Tension?', 'F = YAαΔT ≈ ' + N('3.8 × 10² N'))
d.basic('Exercise 10.10: brass and steel rods (50 cm each) joined, heated 40 → 250 °C, ends free. Change in length? Thermal stress?', N('0.34 cm') + ' total; ' + X('no') + ' thermal stress (free to expand)')
d.basic('Exercise 10.11: fractional change in density of glycerine (αV = 49 × 10⁻⁵ K⁻¹) for a 30 °C rise?', N('≈ 1.5 × 10⁻² decrease') + ' (Δρ/ρ ≈ −αVΔT)')
d.basic('Exercise 10.6: a steel tape calibrated at 27 °C reads 63.0 cm at 45 °C. Actual length that day?', N('63.0136 cm') + ' (≈ 63.0 cm to 3 s.f.)')

# ---------------------------------------------------------------- 10.6 Specific heat
d.sec('10.6-specific-heat-capacity')
d.basic('Heat needed to warm a substance depends on…?', T('Mass') + ', ' + T('temperature change') + ' and the ' + T('nature of the substance'))
d.basic('Define heat capacity and specific heat capacity.', r'\( S = \dfrac{\Delta Q}{\Delta T} \)' + ' ; ' + r'\( s = \dfrac{1}{m}\dfrac{\Delta Q}{\Delta T} \)' + ' (J kg⁻¹ K⁻¹)')
d.basic('Define molar specific heat capacity.', r'\( C = \dfrac{1}{\mu}\dfrac{\Delta Q}{\Delta T} \)' + ' (J mol⁻¹ K⁻¹)')
d.basic('Why do gases have two molar specific heats?', 'Heat can be supplied at constant ' + T('pressure') + ' (Cₚ) or constant ' + T('volume') + ' (Cᵥ); Cₚ > Cᵥ', **fig('tab_10_4_molar_heats'))
d.basic('Which common substance has the highest specific heat? Value?', T('Water') + ': ' + N('4186 J kg⁻¹ K⁻¹'), **fig('tab_10_3_specific_heats'))
d.basic('Uses and effects of water’s high specific heat?', 'Coolant in car radiators, hot-water bags; sea warms slowly, so ' + T('sea breeze') + ' cools the coast; deserts heat and cool quickly')
d.basic('Exercise 10.15: why are Cᵥ values of diatomic gases (~5 cal/mol K) higher than monatomic (2.92)? Chlorine is higher still.', 'Diatomic molecules also store energy in ' + T('rotation') + ' (Cᵥ ≈ 5R/2); chlorine’s ' + T('vibrational') + ' modes are active too')

# ---------------------------------------------------------------- 10.7 Calorimetry
d.sec('10.7-calorimetry')
d.cloze('Principle of calorimetry: in an isolated system, {{c1::heat lost by the hotter part = heat gained by the colder part}}.')
d.basic('Construction of a calorimeter?', 'Copper/aluminium vessel and stirrer inside a wooden jacket with insulating material (glass wool); thermometer through the lid')
steps_card(d, 'Example 10.3 · aluminium sphere', 'Find the missing step.', '0.047 kg Al at 100 °C dropped into 0.25 kg water + 0.14 kg copper calorimeter at 20 °C; final 23 °C. s(Al)?',
           ['Heat lost by Al = 0.047 × s × 77', 'Heat gained = (0.25 × 4180 + 0.14 × 386) × 3', '≈ 3297 J', 's(Al) = 3297 / (0.047 × 77) ≈ <b>911 J kg⁻¹ K⁻¹</b>'], 1,
           'Specific heat of aluminium by mixtures', 'Heat lost by Al = heat gained by water + calorimeter → s ≈ 0.911 kJ kg⁻¹ K⁻¹')
d.basic('Exercise 10.14: 0.20 kg metal at 150 °C into water (150 g) + calorimeter (water equivalent 25 g) at 27 °C; final 40 °C. s? Effect of heat loss?', N('0.43 J g⁻¹ K⁻¹') + '; with losses, the calculated value is ' + X('smaller') + ' than the true value')
d.basic('Exercise 10.12: 10 kW drill, half the power heats an 8.0 kg aluminium block (0.91 J/g K) for 2.5 min. Temperature rise?', N('≈ 103 °C'))
d.basic('Exercise 10.13: 2.5 kg copper at 500 °C on a large ice block. Maximum ice melted?', N('≈ 1.5 kg'))

# ---------------------------------------------------------------- 10.8 Change of state
d.sec('10.8-change-of-state')
d.basic('Temperature of ice being heated while it melts?', T('Stays constant') + ' (0 °C) until all the ice melts; the heat goes into changing state', **fig('fig_10_9_heating_curve'))
d.basic('Define melting point.', 'The temperature at which solid and liquid ' + T('coexist in equilibrium') + '; depends on pressure. At 1 atm: normal melting point')
d.basic('What is regelation? Example?', 'Ice melts under pressure (below a loaded wire) and ' + T('refreezes') + ' when the pressure is removed; the wire passes through without splitting the slab. Also makes skating possible', **fig('fig_10_10_regelation'))
d.basic('Define boiling point; effect of pressure?', 'Liquid and vapour coexist in equilibrium; boiling point ' + T('rises with pressure'), **fig('fig_10_11_boiling'))
d.basic('Why is cooking hard on hills but fast in a pressure cooker?', 'Lower pressure on hills → ' + X('lower') + ' boiling point; a pressure cooker raises pressure → ' + T('higher') + ' boiling point')
d.basic('What is sublimation? Examples?', 'Solid → vapour directly: ' + E('dry ice (solid CO₂), iodine'))
d.basic('What is the triple point? Water’s?', 'Where solid, liquid and vapour coexist (sublimation, fusion and vaporisation curves meet). Water: ' + N('273.16 K, 0.006 atm'), **fig('fig_10_phase_diagrams'))
d.basic('Correction: NCERT’s box gives the triple-point pressure of water as 6.11 × 10⁻³ Pa. What is right?', T('611 Pa') + ' = 6.11 × 10⁻³ bar ≈ 0.006 atm (as its own phase diagram shows). The book wrote Pa where it meant bar')
d.basic('Fusion curve of water vs CO₂: slope?', 'Water: ' + T('negative') + ' slope (melting point falls with pressure — regelation). CO₂: positive; at 1 atm CO₂ sublimes (triple point 5.11 atm)')

d.sec('10.8.1-latent-heat')
d.basic('Define latent heat.', r'\( Q = mL \)' + ': heat per unit mass for a change of state at constant temperature (J kg⁻¹)')
d.basic('Latent heats of water?', 'Fusion Lf = ' + N('3.33 × 10⁵ J/kg') + '; vaporisation Lv = ' + N('22.6 × 10⁵ J/kg'), **fig('tab_10_5_latent_heats'))
d.basic('Why do steam burns hurt more than boiling-water burns?', 'Steam at 100 °C carries an extra ' + N('22.6 × 10⁵ J/kg') + ' of latent heat')
d.basic('In the temperature–heat graph of water, why do the sloping parts differ in slope?', 'Slope ∝ 1/(ms): ice, water and steam have ' + T('different specific heats'), **fig('fig_10_12_temp_vs_heat'))
d.basic('Example 10.4: 0.15 kg ice at 0 °C + 0.30 kg water at 50 °C → 6.7 °C. Lf?', N('3.34 × 10⁵ J/kg'))
steps_card(d, 'Example 10.5 · ice to steam', 'Find the missing step.', 'Heat to turn 3 kg of ice at −12 °C into steam at 100 °C?',
           ['Ice −12 → 0 °C: 3 × 2100 × 12 = 75 600 J', 'Melt: 3 × 3.35 × 10⁵ = 1 005 000 J', 'Water 0 → 100 °C: 3 × 4186 × 100 = 1 255 800 J',
            'Boil: 3 × 2.256 × 10⁶ = 6 768 000 J → total <b>≈ 9.1 × 10⁶ J</b>'], 2, 'Ice at −12 °C to steam at 100 °C', 'Four stages add to about 9.1 × 10⁶ J')
d.basic('Mnemonic for the ice-to-steam heating curve?', '"' + T('Slope, flat, slope, flat, slope') + '": heat (s), melt (Lf), heat (s), boil (Lv), heat (s)')
d.basic('Exercise 10.16: a child (30 kg) cools from 101 °F to 98 °F in 20 min by sweating (L = 580 cal/g). Rate of evaporation?', N('≈ 4.3 g/min'))

# ---------------------------------------------------------------- 10.9 Heat transfer
d.sec('10.9-heat-transfer')
d.basic('Three modes of heat transfer?', T('Conduction, convection, radiation'), **fig('fig_10_13_modes'))
d.basic('What is conduction?', 'Heat transfer between neighbouring parts of a body through molecular collisions, ' + X('without') + ' bulk flow of matter')
d.basic('Rate of heat flow through a bar in steady state?', r'\( H = KA\dfrac{T_C - T_D}{L} \)' + ' (K = thermal conductivity, W m⁻¹ K⁻¹)', **fig('fig_10_14_conducting_bar'))
d.basic('Table 10.6: best and worst conductors?', 'Silver ' + N('406') + ', copper ' + N('385') + ' W/m K; air ' + N('0.024') + ', glass wool 0.04', **fig('tab_10_6_conductivities'))
d.basic('Why do cooking pots have copper bottoms, and why are plastic foams good insulators?', 'Copper spreads heat evenly (large K); foams trap ' + T('pockets of air') + ' (very small K)')
d.basic('Why is a layer of earth or foam put on concrete roofs?', 'Concrete’s K is not small enough; the layer ' + T('insulates') + ' and keeps rooms cool')
d.basic('Example 10.6: steel (15 cm, area 2A, K = 50.2) and copper (10 cm, area A, K = 385) in series, 300 °C to 0 °C. Junction temperature?', N('≈ 44.4 °C'), **fig('fig_10_15_steel_copper'))
d.basic('Example 10.7: iron (K = 79) and brass (K = 109) bars of equal size in series, 373 K to 273 K. Junction temperature, K(equivalent)?', 'T₀ = ' + N('315 K') + '; K′ = 2K₁K₂/(K₁ + K₂) = ' + N('91.6 W m⁻¹ K⁻¹') + '; H ≈ 916 W', **fig('fig_10_16_iron_brass'))
d.basic('Teacher addition: thermal resistance and bars in series/parallel?', r'\( R_{th} = \dfrac{L}{KA} \)' + '; in series resistances add, in parallel their reciprocals add (like resistors)')
d.basic('Exercise 10.17: thermacole icebox (30 cm cube, walls 5 cm, K = 0.01), 4 kg ice, outside 45 °C, 6 h. Ice left?', N('≈ 3.7 kg'))
d.basic('Exercise 10.18: brass boiler base 0.15 m², 1.0 cm thick, boils 6.0 kg/min. Flame temperature?', N('≈ 238 °C'))
d.basic('Exercise 10.19(b): why does a brass tumbler feel colder than a wooden tray on a chilly day?', 'Brass is a good ' + T('conductor') + ': it draws heat from your hand quickly')

d.sec('10.9.2-convection')
d.basic('What is convection? Where is it possible?', 'Heat transfer by ' + T('actual bulk motion') + ' of matter; only in ' + T('fluids'))
d.basic('Natural vs forced convection? Examples?', T('Natural') + ': driven by gravity/buoyancy (sea breeze). ' + T('Forced') + ': by a pump or fan (house heating, blood circulation, car cooling system)')
d.basic('Sea breeze and land breeze?', 'Day: land heats faster, warm air rises over land, cool air flows in from the sea (' + T('sea breeze') + '). Night: reversed (' + T('land breeze') + ')', **fig('fig_10_17_convection'))
d.basic('What are trade winds?', 'Steady surface winds blowing from the north-east towards the equator: convection modified by Earth’s ' + T('rotation') + '; air descends near 30° N')
d.basic('A hot bar under a running tap loses heat mainly by…?', T('Conduction') + ' between the bar and water, not convection within the water')
d.basic('Exercise 10.19(e): why is steam heating more efficient than hot-water heating?', 'Condensing steam releases a large ' + T('latent heat') + ' per kg')

d.sec('10.9.3-radiation')
d.basic('What is thermal radiation? Why needs no medium?', 'Electromagnetic waves emitted because of temperature; EM waves travel through ' + T('vacuum') + ' at 3 × 10⁸ m/s')
d.basic('Why wear white clothes in summer and dark ones in winter?', 'Dark bodies ' + T('absorb and emit') + ' radiation better; white reflects the Sun’s heat')
d.basic('How does a thermos (Dewar) flask reduce heat transfer?', 'Silvered walls (' + T('radiation') + '), vacuum between walls (' + T('conduction, convection') + '), cork support')
d.basic('State Wien’s displacement law.', r'\( \lambda_m T = b \)' + ', b = ' + N('2.9 × 10⁻³ m K'), **fig('fig_10_18_blackbody'))
d.basic('Why does heated iron glow dull red, then yellow, then white?', 'As T rises, λₘ shifts to ' + T('shorter wavelengths') + ' (Wien)')
d.basic('Surface temperatures of the Moon and Sun from Wien’s law?', 'Moon: λₘ ≈ 14 μm → ' + N('≈ 200 K') + '. Sun: λₘ = 4753 Å → ' + N('≈ 6000 K') + ' (surface, not interior)')
d.basic('State the Stefan–Boltzmann law.', r'\( H = Ae\sigma T^4 \)' + ', σ = ' + N('5.67 × 10⁻⁸ W m⁻² K⁻⁴') + ', e = emissivity (1 for a perfect radiator)')
d.basic('Net radiation loss of a body at T in surroundings at Tₛ?', r'\( H = e\sigma A\,(T^4 - T_s^4) \)')
d.basic('Heat radiated by a person (1.9 m², skin 28 °C, room 22 °C, e = 0.97)?', N('≈ 66 W') + ' — over half the body’s resting output (120 W); arctic clothing adds a shiny reflecting layer')
d.basic('Exercise 10.19(a): why is a good reflector a poor emitter?', 'Good reflectors are poor ' + T('absorbers') + ', and good absorbers are good emitters')
d.basic('Exercise 10.19(d): why would Earth be very cold without its atmosphere?', 'The atmosphere traps the Earth’s infrared radiation (' + T('greenhouse effect') + ')')

# ---------------------------------------------------------------- 10.10 Newton's law of cooling
d.sec('10.10-newtons-law-of-cooling')
d.basic('State Newton’s law of cooling.', r'\( -\dfrac{dQ}{dt} = k(T_2 - T_1) \)' + ': rate of heat loss ∝ excess temperature over the surroundings (small differences only)', **fig('fig_10_19_cooling_curve'))
d.basic('Temperature of a cooling body with time?', r'\( T_2 = T_1 + Ce^{-Kt} \)' + ', K = k/ms: an ' + T('exponential decay') + ' of the excess temperature')
d.basic('How is Newton’s law of cooling verified?', 'Plot ln(T₂ − T₁) against t: a ' + T('straight line with negative slope'), **fig('fig_10_20_newton_cooling'))
d.basic('Teacher addition: average form of Newton’s law used in problems?', r'\( \dfrac{\Delta T}{\Delta t} = K\left(\bar T - T_s\right) \)' + ' (use the average temperature over the interval)')
d.basic('Example 10.8: food cools 94 → 86 °C in 2 min (room 20 °C). Time for 71 → 69 °C?', '8/2 = K(70) and 2/t = K(50) → t = ' + N('0.7 min = 42 s'))
d.basic('Exercise 10.20: a body cools 80 → 50 °C in 5 min (room 20 °C). Time for 60 → 30 °C?', N('9 min'))

# ---------------------------------------------------------------- Summary
d.sec('summary')
table_card(d, 'Summary', 'Formula?', [
    ('Linear expansion', 'Δl = αₗ l ΔT', False), ('αV and αₗ', 'αV = 3αₗ', False), ('Heat for temperature change', 'Q = ms ΔT', False),
    ('Heat for change of state', 'Q = mL', False), ('Conduction', 'H = KA ΔT / L', False), ('Radiation', 'H = eσAT⁴', False)], term='Chapter 10 formula sheet')
table_card(d, 'Points to ponder', 'True or false?', [
    ('Melting and boiling points of water are exactly 0 °C and 100 °C today', 'False (very close)', True),
    ('Two phases in equilibrium have the same density', 'False (same P and T)', True),
    ('Heat transfer always involves a temperature difference', 'True', False)], term='Chapter 10 concept checks')

print(d.write(os.path.join(OUT, 'deck.json')), 'cards')
