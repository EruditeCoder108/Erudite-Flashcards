import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Chemistry', 'class12-chemistry-ch03-chemical-kinetics')
d = Deck('Chapter 3: Chemical Kinetics', 'Class 12', ['class-12', 'chemistry', 'ch-3'])
d.description = 'Reaction rates, rate law, order and molecularity, zero and first order integrated laws, half-life, Arrhenius equation, catalysts, collision theory'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- intro
d.sec('3.0-introduction')
d.basic('Thermodynamics vs kinetics: what does each tell you?', T('Thermodynamics') + ': feasibility (ΔG < 0) and extent. ' + T('Kinetics') + ': rate and mechanism.')
d.basic('Why is "diamond is forever" true though diamond → graphite is spontaneous?', 'ΔG < 0, but the rate is ' + X('imperceptibly slow') + ': feasible does not mean fast')
d.basic('Origin of the word kinetics?', 'Greek ' + I('kinesis') + ': movement')
d.cloze('Reaction speeds: very fast = {{c1::precipitation of AgCl (ionic)}}; very slow = {{c2::rusting of iron}}; moderate = {{c3::inversion of cane sugar, hydrolysis of starch}}.')

# ---------------------------------------------------------------- 3.1 Rate
d.sec('3.1-rate-of-reaction')
d.basic('Define rate of reaction.', 'Change in ' + T('concentration') + ' of a reactant or product per unit time')
d.basic('Average rate for R → P?', r'\( r_{av} = -\frac{\Delta [R]}{\Delta t} = \frac{\Delta [P]}{\Delta t} \)')
d.basic('Why the minus sign for reactants?', 'Δ[R] is negative; the minus sign makes the rate ' + T('positive'))
d.basic('Instantaneous rate?', r'\( r_{inst} = -\frac{d[R]}{dt} = \frac{d[P]}{dt} \)' + ': slope of the ' + T('tangent') + ' to the concentration–time curve', **fig('fig_3_1_average_instantaneous'))
d.basic('Units of rate?', N('mol L⁻¹ s⁻¹') + '; for gases ' + N('atm s⁻¹') + ' (partial pressures)')
d.basic('Why does the average rate of butyl chloride hydrolysis fall with time?', 'Reactant concentration ' + X('decreases') + ', so collisions and rate fall (1.90 → 0.4 × 10⁻⁴ mol L⁻¹ s⁻¹)', **fig('tab_3_1_butyl_chloride'))
d.basic('How is the instantaneous rate at 600 s found from Fig. 3.2?', 'Draw the ' + T('tangent at t = 600 s') + '; −slope = ' + N('5.12 × 10⁻⁵ mol L⁻¹ s⁻¹'), **fig('fig_3_2_tangent'))
d.basic('Rate of 2HI → H₂ + I₂ in terms of each species?', r'\( -\frac{1}{2}\frac{d[HI]}{dt} = \frac{d[H_2]}{dt} = \frac{d[I_2]}{dt} \)')
d.basic('General rule for rate with stoichiometric coefficients?', 'Divide each species’ rate of change by its ' + T('coefficient') + ' (minus sign for reactants)')
d.basic('For 5Br⁻ + BrO₃⁻ + 6H⁺ → 3Br₂ + 3H₂O, rate in terms of Br⁻ and Br₂?', r'\( -\frac{1}{5}\frac{d[Br^-]}{dt} = \frac{1}{3}\frac{d[Br_2]}{dt} \)')
steps_card(d, 'Example 3.2', '2N₂O₅ → 4NO₂ + O₂: [N₂O₅] 2.33 → 2.08 M in 184 min. Rate, and rate of NO₂ formation?', 'Rate = −½ Δ[N₂O₅]/Δt.',
           ['Rate = ½ × 0.25/184 = <b>6.79 × 10⁻⁴ M min⁻¹</b>', '= 4.07 × 10⁻² M h⁻¹ = 1.13 × 10⁻⁵ M s⁻¹', 'd[NO₂]/dt = 4 × rate', '= <b>2.72 × 10⁻³ M min⁻¹</b>'], 3, 'Rate of N₂O₅ decomposition', '6.79 × 10⁻⁴ M/min; NO₂ 2.72 × 10⁻³')
d.basic('Trap: 2A → products, [A] 0.5 → 0.4 M in 10 min. Rate? (Intext 3.2)', '½ × 0.1/10 = ' + N('5 × 10⁻³ M min⁻¹') + ' (don’t forget the ½)')
d.basic('R → P, [R] 0.03 → 0.02 M in 25 min. Rate in min and s? (Intext 3.1)', N('4 × 10⁻⁴ M min⁻¹') + ' = ' + N('6.67 × 10⁻⁶ M s⁻¹'))

# ---------------------------------------------------------------- 3.2 Factors
d.sec('3.2-rate-law')
d.basic('Factors affecting rate?', T('Concentration') + ' (pressure for gases), ' + T('temperature') + ', ' + T('catalyst'))
d.basic('What is a rate law (rate equation)?', 'Rate expressed in terms of reactant concentrations, each raised to a power: ' +r'\( Rate = k[A]^x[B]^y \)')
d.basic('Are x and y the stoichiometric coefficients?', X('Not necessarily') + ': they must be found ' + T('experimentally'))
d.basic('What is k?', 'The ' + T('rate constant') + ': the rate when all concentrations are 1 M; depends on T, not on concentration')
steps_card(d, 'Table 3.2', '2NO + O₂ → 2NO₂. From initial-rate data, find the rate law.', 'Double one concentration at a time.',
           ['[NO] 0.30 → 0.60, [O₂] fixed: rate 0.096 → 0.384 (×4)', 'So order in NO = 2', '[O₂] 0.30 → 0.60, [NO] fixed: rate ×2, order in O₂ = 1', '<b>Rate = k[NO]²[O₂]</b>'], 3, 'Initial-rate method', 'Rate = k[NO]²[O₂]')
d.basic('Initial-rate data for NO + O₂?', 'Table 3.2', **fig('tab_3_2_no_rates'))
d.basic('Experimental rate law of CHCl₃ + Cl₂ → CCl₄ + HCl?', r'\( Rate = k[CHCl_3][Cl_2]^{1/2} \)' + ': order ' + N('1.5'))
d.basic('Experimental rate law of ester hydrolysis (CH₃COOC₂H₅ + H₂O)?', r'\( Rate = k[ester]^1[H_2O]^0 \)')
d.basic('Intuition: how to read an order from a doubling experiment?', 'Rate ×1 → order 0; ×2 → order 1; ×4 → order 2; ×8 → order 3 (rate multiplies by 2ⁿ)')

d.sec('3.2.3-order')
d.basic('Define order of reaction.', 'Sum of the ' + T('powers of concentration') + ' in the experimental rate law')
d.basic('Possible values of order?', '0, 1, 2, 3, and even ' + T('fractions') + ' or negative values')
d.basic('Zero order means?', 'Rate is ' + T('independent of reactant concentration'))
d.basic('Order of Rate = k[A]¹ᐟ²[B]³ᐟ² and Rate = k[A]³ᐟ²[B]⁻¹? (Example 3.3)', N('2') + ' and ' + N('½'))
d.basic('Order of r = k[A]¹ᐟ²[B]²? (Intext 3.3)', N('2.5'))
d.basic('Second order in X; [X] tripled. Effect on rate? (Intext 3.4)', 'Rate × 3² = ' + N('9 times'))
d.basic('Elementary vs complex reaction?', T('Elementary') + ': occurs in one step. ' + T('Complex') + ': a sequence of elementary steps (mechanism).')
d.basic('Types of complex reactions (NCERT examples)?', 'Consecutive (ethane → alcohol → aldehyde → acid → CO₂)<br>Reverse<br>Side reactions (phenol → o- and p-nitrophenol)')
d.basic('General unit of k for order n?', r'\( (mol \, L^{-1})^{1-n} \, s^{-1} \)')
table_card(d, 'Units of k', 'Unit of k?', [
    ('Zero order', 'mol L⁻¹ s⁻¹', False), ('First order', 's⁻¹', False), ('Second order', 'L mol⁻¹ s⁻¹', False), ('Third order', 'L² mol⁻² s⁻¹', False)],
    term='Units of rate constant by order')
d.basic('Order from k = 2.3 × 10⁻⁵ L mol⁻¹ s⁻¹ and k = 3 × 10⁻⁴ s⁻¹? (Example 3.4)', T('Second') + ' order and ' + T('first') + ' order')

d.sec('3.2.4-molecularity')
d.basic('Define molecularity.', 'Number of reacting species that must ' + T('collide simultaneously') + ' in an ' + T('elementary') + ' reaction')
d.cloze('Molecularity examples: unimolecular = {{c1::NH₄NO₂ → N₂ + 2H₂O}}; bimolecular = {{c2::2HI → H₂ + I₂}}; termolecular = {{c3::2NO + O₂ → 2NO₂}}.')
d.basic('Why are reactions of molecularity > 3 not seen?', 'The chance of ' + X('more than three') + ' molecules colliding at once is negligible')
d.basic('KClO₃ + 6FeSO₄ + 3H₂SO₄ → … looks 10th order. Actual order?', N('Second order') + ': it goes in several steps')
d.basic('What is the rate-determining step?', 'The ' + T('slowest step') + ' of a mechanism; it controls the overall rate (like the slowest runner in a relay)')
d.basic('Mechanism of I⁻-catalysed decomposition of H₂O₂ (alkaline)?', '(1) H₂O₂ + I⁻ → H₂O + IO⁻ (' + T('slow') + '); (2) H₂O₂ + IO⁻ → H₂O + I⁻ + O₂. Rate = k[H₂O₂][I⁻].')
d.basic('What is IO⁻ in that mechanism?', 'An ' + T('intermediate') + ': formed and used up; not in the overall equation')
table_card(d, 'Order vs molecularity', 'Which one?', [
    ('Found experimentally', 'Order', False), ('Can be zero or fractional', 'Order', False), ('Always a whole number 1–3', 'Molecularity', True),
    ('Meaningful only for elementary steps', 'Molecularity', True), ('Applies to complex reactions too', 'Order', False)], term='Order vs molecularity')
d.basic('NCERT: for a complex reaction, molecularity of the slowest step = order. Correction?', 'True only when the slow step is the ' + T('first step') + ' (or involves only reactants). If fast steps come first, intermediates in the slow step change the order.')

# ---------------------------------------------------------------- 3.3 Integrated rate laws
d.sec('3.3-integrated-rate-equations')
d.basic('Why integrate rate laws?', 'Instantaneous rates (tangents) are hard to measure; integrated laws link ' + T('concentration directly to time'))
d.sec('3.3.1-zero-order')
d.basic('Integrated zero-order rate law?', r'\( [R] = [R]_0 - kt \)' + ', so ' + r'\( k = \frac{[R]_0 - [R]}{t} \)')
d.basic('Straight-line plot for zero order?', T('[R] vs t') + ': slope = −k, intercept = [R]₀', **fig('fig_3_3_zero_order'))
d.basic('Examples of zero-order reactions?', 'Some ' + T('enzyme') + ' reactions and reactions on metal surfaces:<br>2NH₃ → N₂ + 3H₂ on hot ' + T('Pt') + ' (1130 K, high pressure)<br>HI on ' + T('gold'))
d.basic('Why is NH₃ decomposition on Pt zero order at high pressure?', 'The Pt ' + T('surface is saturated') + '; extra NH₃ can’t find sites, so rate is independent of [NH₃]')
d.basic('Intuition: zero order is like…?', 'A ticket counter with one clerk: the queue length (concentration) doesn’t change how fast people are served')

d.sec('3.3.2-first-order')
d.basic('Integrated first-order rate law?', r'\( k = \frac{2.303}{t} \log \frac{[R]_0}{[R]} \)' + ' or ' + r'\( [R] = [R]_0 e^{-kt} \)')
d.basic('Straight-line plots for first order?', T('ln[R] vs t') + ': slope −k. ' + T('log([R]₀/[R]) vs t') + ': slope k/2.303, through origin.')
d.basic('Identify the plot and give its slope.', 'First order: ln[R] vs t, slope = ' + T('−k'), **img('fig_3_4_ln_r_vs_t'))
d.basic('Identify the plot and give its slope.', 'First order: log([R]₀/[R]) vs t, slope = ' + T('k/2.303'), **img('fig_3_5_log_ratio_vs_t'))
d.basic('k from two times t₁, t₂?', r'\( k = \frac{2.303}{t_2 - t_1} \log \frac{[R]_1}{[R]_2} \)')
d.basic('Examples of first-order reactions?', 'Hydrogenation of ethene, ' + T('all radioactive decay') + ' (e.g. ²²⁶Ra → ²²²Rn + ⁴He), decomposition of N₂O₅ and N₂O')
steps_card(d, 'Example 3.5', '[N₂O₅] 1.24 × 10⁻² → 0.20 × 10⁻² M in 60 min, first order. k?', 'k = (2.303/t) log([R]₀/[R])',
           ['Ratio = 1.24/0.20 = 6.2', 'log 6.2 = 0.792', 'k = 2.303 × 0.792/60', '= <b>0.0304 min⁻¹</b>'], 3, 'First-order rate constant of N₂O₅', '0.0304 min⁻¹')
d.basic('First-order gas reaction A(g) → B(g) + C(g): k in terms of total pressure?', r'\( k = \frac{2.303}{t} \log \frac{p_i}{2p_i - p_t} \)' + ' (p_A = 2pᵢ − pₜ)')
steps_card(d, 'Example 3.6', '2N₂O₅ → 2N₂O₄ + O₂ at constant V: pₜ = 0.5 atm at 0 s, 0.512 atm at 100 s. k?', 'N₂O₅ falls by 2x, total rises by x.',
           ['pₜ = 0.5 + x ⇒ x = 0.012', 'p(N₂O₅) = 0.5 − 2x = 1.5 − 2pₜ = 0.476 atm', 'k = (2.303/100) log(0.5/0.476)', '= 0.02303 × 0.0214 = <b>4.92 × 10⁻⁴ s⁻¹</b>'], 1, 'k from total pressure', '4.92 × 10⁻⁴ s⁻¹')
d.basic('Correction: NCERT’s Example 3.6 gives k = 4.98 × 10⁻⁴ s⁻¹. Exact value?', 'log(0.5/0.476) = 0.02136 (NCERT rounds to 0.0216), so k = ' + T('4.92 × 10⁻⁴ s⁻¹') + '. Small rounding slip, same method.')
d.basic('Trap: in pressure problems, why not use pₜ directly?', 'Only the ' + T('reactant’s partial pressure') + ' follows the first-order law; build it from the stoichiometry first')

d.sec('3.3.3-half-life')
d.basic('Define half-life.', 'Time for the reactant concentration to fall to ' + T('half') + ' its initial value')
d.basic('Half-life of a zero-order reaction?', r'\( t_{1/2} = \frac{[R]_0}{2k} \)' + ': ∝ ' + T('[R]₀'))
d.basic('Half-life of a first-order reaction?', r'\( t_{1/2} = \frac{0.693}{k} \)' + ': ' + T('independent of [R]₀'))
d.basic('Half-life of a second-order reaction? (teacher addition)', r'\( t_{1/2} = \frac{1}{k[R]_0} \)' + '; general: ' + r'\( t_{1/2} \propto [R]_0^{\,1-n} \)')
d.basic('Integrated second-order law, 2A → P type with rate k[A]²? (teacher addition)', r'\( \frac{1}{[A]} - \frac{1}{[A]_0} = kt \)' + '; plot 1/[A] vs t is linear')
d.basic('t½ for k = 5.5 × 10⁻¹⁴ s⁻¹? (Example 3.7)', '0.693/k = ' + N('1.26 × 10¹³ s'))
d.basic('Show t(99.9%) = 10 t½ for first order. (Example 3.8)', 't = (2.303/k) log 1000 = 6.909/k; ÷ (0.693/k) = ' + N('10'))
d.basic('First-order shortcuts: t(75%) and t(87.5%)?', T('2 t½') + ' and ' + T('3 t½') + ' (halve, halve, halve)')
d.basic('Intuition: why is a first-order t½ constant?', 'A fixed ' + T('fraction') + ' reacts per unit time, however much is left.<br>Like radioactive atoms, each has the same chance to react each second')
d.basic('After n half-lives, fraction left (first order)?', r'\( \left(\frac{1}{2}\right)^n \)')
d.basic('5 g → 3 g, first order, k = 1.15 × 10⁻³ s⁻¹. Time? (Intext 3.5)', '(2.303/1.15 × 10⁻³) log(5/3) = ' + N('444 s'))
d.basic('SO₂Cl₂ half-life 60 min (first order). k? (Intext 3.6)', '0.693/60 = ' + N('1.16 × 10⁻² min⁻¹') + ' (1.93 × 10⁻⁴ s⁻¹)')
table_card(d, 'Table 3.4', 'Zero vs first order?', [
    ('Integrated law', '[R] = [R]₀ − kt  |  [R] = [R]₀e⁻ᵏᵗ', False), ('Straight-line plot', '[R] vs t  |  ln[R] vs t', False),
    ('Half-life', '[R]₀/2k  |  0.693/k', False), ('Units of k', 'mol L⁻¹ s⁻¹  |  s⁻¹', False)], term='Integrated rate laws: zero vs first order')
d.basic('Table 3.4 as printed?', 'Integrated rate laws summary', **fig('tab_3_4_integrated_laws'))

d.sec('3.3.4-pseudo-first-order')
d.basic('What is a pseudo first-order reaction?', 'A higher-order reaction that behaves as first order because one reactant is in ' + T('large excess') + ' (its concentration barely changes)')
d.basic('Why is acid hydrolysis of ethyl acetate pseudo first order?', 'Water is in huge excess (0.01 mol ester vs 10 mol water → 9.99 mol), so Rate = k′[ester]')
d.basic('Inversion of cane sugar: products and rate law?', 'Sucrose + H₂O →(H⁺) ' + T('glucose + fructose') + '; Rate = k[C₁₂H₂₂O₁₁] (pseudo first order)')

# ---------------------------------------------------------------- 3.4 Temperature
d.sec('3.4-temperature-dependence')
d.basic('Half-life of N₂O₅ at 50, 25, 0 °C?', N('12 min') + ', ' + N('5 h') + ', ' + N('10 days'))
d.basic('Rule of thumb for temperature (temperature coefficient)?', 'A 10° rise nearly ' + T('doubles') + ' the rate constant (k₃₀₈/k₂₉₈ ≈ 2–3)')
d.basic('Arrhenius equation?', r'\( k = A e^{-E_a/RT} \)' + '; A = frequency / pre-exponential factor, Eₐ = activation energy')
d.basic('Who proposed and who justified the Arrhenius equation?', 'Proposed by ' + T('van’t Hoff') + '; physical justification by ' + T('Arrhenius'))
d.basic('Activated complex in H₂ + I₂ → 2HI?', 'An unstable ' + T('intermediate') + ' H₂···I₂ that exists briefly then breaks into 2HI', **fig('fig_3_6_hi_intermediate'))
d.basic('Define activation energy.', 'Energy needed to form the ' + T('activated complex') + ' from reactants (the energy barrier)')
d.occlusion('Figure 3.7 · Potential energy vs reaction coordinate', M + 'fig_3_7_energy_profile.webp', (1001, 650), [
    ('Activated complex', [455, 25, 215, 100], True), ('Activation energy', [240, 225, 225, 105], True), ('ΔH', [495, 405, 85, 65], False),
    ('Reactants (H₂ + I₂)', [262, 432, 150, 72], False), ('Products (2HI)', [700, 452, 105, 62], False)])
d.basic('On the energy profile, what gives ΔH?', 'Energy of ' + T('products − reactants') + ' (independent of the barrier)')
d.basic('Relation of forward and backward activation energies? (teacher addition)', r'\( E_{a,f} - E_{a,b} = \Delta H \)' + '; for endothermic reactions Eₐ,f ≥ ΔH')
d.basic('What does the Maxwell–Boltzmann curve show?', 'Fraction of molecules (N_E/N_T) vs kinetic energy; peak = ' + T('most probable kinetic energy'), **fig('fig_3_8_maxwell_boltzmann'))
d.basic('Effect of raising T on the distribution curve?', 'Peak shifts to ' + T('higher energy') + ' and the curve ' + T('broadens') + '; total area stays constant', **fig('fig_3_9_temperature_curve'))
d.basic('Why does a 10° rise roughly double the rate?', 'The fraction of molecules with E ≥ Eₐ (tail area) ' + T('about doubles'))
d.basic('Physical meaning of e^(−Eₐ/RT)?', 'Fraction of molecules with kinetic energy ' + T('≥ Eₐ'))
d.basic('Intuition: why does rate rise so steeply with T?', 'Only the tail of the distribution reacts.<br>A small shift of the curve adds many molecules to that thin tail (exponential, not linear)')
d.basic('Log form of Arrhenius and its plot?', r'\( \ln k = -\frac{E_a}{RT} + \ln A \)' + '; ln k vs 1/T: slope ' + T('−Eₐ/R') + ', intercept ' + T('ln A'), **fig('fig_3_10_arrhenius_plot'))
d.basic('Two-temperature Arrhenius equation?', r'\( \log \frac{k_2}{k_1} = \frac{E_a}{2.303R}\left(\frac{T_2 - T_1}{T_1 T_2}\right) \)')
d.basic('Trap: units in the two-temperature formula?', 'Eₐ in ' + T('J mol⁻¹') + ' with R = 8.314 J K⁻¹ mol⁻¹; T in ' + T('kelvin'))
steps_card(d, 'Example 3.9', 'k = 0.02 s⁻¹ at 500 K and 0.07 s⁻¹ at 700 K. Eₐ and A?', 'Use the two-temperature form.',
           ['log(0.07/0.02) = 0.544', '(T₂ − T₁)/(T₁T₂) = 200/350000 = 5.714 × 10⁻⁴', 'Eₐ = 0.544 × 19.15/5.714 × 10⁻⁴ = <b>18.23 kJ mol⁻¹</b>', 'A = 0.02/e^(−4.385) = 0.02/0.0125 = <b>1.61 s⁻¹</b>'], 2, 'Eₐ and A from two rate constants', 'Eₐ 18.23 kJ/mol; A 1.61')
steps_card(d, 'Example 3.10', 'C₂H₅I decomposition: k = 1.60 × 10⁻⁵ s⁻¹ at 600 K, Eₐ = 209 kJ/mol. k at 700 K?', 'log k₂ = log k₁ + (Eₐ/2.303R)(1/T₁ − 1/T₂).',
           ['Eₐ/2.303R = 209000/19.15 = 10914', '× (1/600 − 1/700) = 10914 × 2.381 × 10⁻⁴ = 2.599', 'log k₂ = −4.796 + 2.599 = −2.197', 'k₂ = <b>6.36 × 10⁻³ s⁻¹</b>'], 1, 'Rate constant at a new temperature', '6.36 × 10⁻³ s⁻¹')
d.basic('Effect of higher T or lower Eₐ on k?', 'Both give an ' + T('exponential increase') + ' in k')

d.sec('3.4.1-catalyst')
d.basic('Define a catalyst. Example?', 'Increases rate without permanent chemical change; ' + E('MnO₂ in 2KClO₃ → 2KCl + 3O₂'))
d.basic('What is an inhibitor?', 'A substance that ' + X('reduces') + ' the rate (not called a catalyst)')
d.basic('Intermediate complex theory?', 'Catalyst forms ' + T('temporary bonds') + ' with reactants → intermediate complex → products + catalyst')
d.basic('How does a catalyst speed up a reaction?', 'Provides an alternate pathway of ' + T('lower activation energy'), **fig('fig_3_11_catalyst'))
d.cloze('A catalyst does not change {{c1::ΔG}} or the {{c2::equilibrium constant}}; it speeds up forward and backward reactions {{c3::equally}}, so equilibrium is reached {{c4::faster}}.')
d.basic('Can a catalyst make a non-spontaneous reaction occur?', X('No') + ': it only speeds up reactions that are already spontaneous')
d.basic('Intuition: catalyst as a mountain tunnel?', 'Same start and end points (same ΔH, ΔG), but a ' + T('lower pass') + ' through the mountain.<br>So far more travellers make it across per hour')

# ---------------------------------------------------------------- 3.5 Collision theory
d.sec('3.5-collision-theory')
d.basic('Who developed collision theory, and its basis?', T('Trautz and Lewis') + ' (1916–18); based on kinetic theory of gases, molecules as hard spheres')
d.basic('Collision frequency Z?', 'Number of collisions per second per unit volume')
d.basic('Collision-theory rate for A + B?', r'\( Rate = Z_{AB} \, e^{-E_a/RT} \)' + '; A in Arrhenius is related to Z')
d.basic('What are effective collisions?', 'Collisions with energy ≥ ' + T('threshold energy') + ' and ' + T('proper orientation'))
d.basic('Threshold energy (footnote)?', 'Activation energy + energy possessed by the reacting species')
d.basic('Rate with steric factor P?', r'\( Rate = P \, Z_{AB} \, e^{-E_a/RT} \)' + '; P accounts for ' + T('orientation'))
d.basic('Identify the idea shown.', 'Only a ' + T('properly oriented') + ' collision (OH⁻ attacking C opposite Br) gives CH₃OH; others bounce back', **img('fig_3_12_orientation'))
d.basic('Correction: NCERT says "methanol from bromoethane" for Fig. 3.12. Right reactant?', T('Bromomethane') + ' (CH₃Br): the figure shows CH₃Br + OH⁻ → CH₃OH + Br⁻; bromoethane would give ethanol')
d.basic('Drawback of collision theory?', 'Treats molecules as ' + X('hard spheres') + ', ignoring their structure')

# ---------------------------------------------------------------- summary
d.sec('summary')
table_card(d, 'Summary', 'Formula?', [
    ('Zero order', 'k = ([R]₀ − [R])/t; t½ = [R]₀/2k', False), ('First order', 'k = (2.303/t) log([R]₀/[R]); t½ = 0.693/k', False),
    ('Arrhenius', 'k = A e^(−Eₐ/RT)', False), ('Two temperatures', 'log(k₂/k₁) = Eₐ(T₂ − T₁)/(2.303 R T₁T₂)', False),
    ('Collision theory', 'Rate = P Z e^(−Eₐ/RT)', False)], term='Chemical kinetics formula sheet')
table_card(d, 'Summary', 'What changes k?', [
    ('Temperature', 'Yes: exponential rise', False), ('Catalyst', 'Yes: lowers Eₐ', False),
    ('Concentration', 'No (changes rate, not k)', True), ('Reaction time elapsed', 'No', True)], term='What affects the rate constant')

n = d.write(os.path.join(OUT, 'deck.json'))
print(n, 'cards')
