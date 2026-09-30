import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase_phy as sp

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Physics', 'class11-physics-ch01-units-and-measurement')
d = Deck('Chapter 1: Units and Measurement', 'Class 11', ['class-11', 'physics', 'ch-1'])
d.description = 'SI base units, significant figures, rounding, error in results, dimensions, dimensional analysis and unit conversion'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}

# ---------------------------------------------------------------- 1.1 Introduction
d.sec('1.1-introduction')
d.basic('What is a unit?', 'An internationally accepted ' + T('reference standard') + ' used to measure a physical quantity')
d.basic('A measurement is written as…?', 'A ' + T('number') + ' (numerical measure) × a ' + T('unit') + ', e.g. ' + N('5 kg'))
d.cloze('Units of base quantities are {{c1::fundamental (base) units}}; units made from them are {{c2::derived units}}; the full set is a {{c3::system of units}}.')
d.basic('Why do we need only a few base units?', 'All physical quantities are ' + T('inter-related') + ', so the rest can be built from a few')

# ---------------------------------------------------------------- 1.2 SI
d.sec('1.2-si-units')
table_card(d, 'Older systems', 'Base units of length, mass, time?', [
    ('CGS', 'centimetre, gram, second', False), ('FPS (British)', 'foot, pound, second', False),
    ('MKS', 'metre, kilogram, second', False)], term='CGS, FPS and MKS systems')
d.basic('What does SI stand for, and who developed it?', T('Système International d’Unités') + '; by BIPM (International Bureau of Weights and Measures) in ' + N('1971'))
d.basic('When was SI last revised?', N('November 2018') + ', by the General Conference on Weights and Measures')
d.basic('Why is SI convenient?', 'It uses the ' + T('decimal system') + ', so conversions within it are simple')
table_card(d, 'Table 1.1 · SI base units', 'SI unit (symbol) of each base quantity?', [
    ('Length', 'metre (m)', False), ('Mass', 'kilogram (kg)', False), ('Time', 'second (s)', False),
    ('Electric current', 'ampere (A)', False), ('Thermodynamic temperature', 'kelvin (K)', False),
    ('Amount of substance', 'mole (mol)', False), ('Luminous intensity', 'candela (cd)', False)],
    note='Mnemonic for the units in this order: <b>M</b>any <b>K</b>ids <b>S</b>ing <b>A</b>nd <b>K</b>ick <b>M</b>any <b>C</b>ans → m, kg, s, A, K, mol, cd.',
    term='Seven SI base quantities and units')
d.cloze('There are {{c1::seven}} SI base units.')
d.basic('Since 2018, how are SI base units defined?', 'By fixing the exact numerical value of a ' + T('fundamental constant') + ' (c, h, e, k, N<sub>A</sub>, the caesium frequency)')
table_card(d, 'Table 1.1 · Revised SI (2018)', 'Which constant defines each unit?', [
    ('second', 'caesium-133 hyperfine frequency Δν<sub>Cs</sub> = 9 192 631 770 Hz', False),
    ('metre', 'speed of light c = 299 792 458 m s⁻¹', False),
    ('kilogram', 'Planck constant h = 6.626 070 15 × 10⁻³⁴ J s', False),
    ('ampere', 'elementary charge e = 1.602 176 634 × 10⁻¹⁹ C', False),
    ('kelvin', 'Boltzmann constant k = 1.380 649 × 10⁻²³ J K⁻¹', False),
    ('mole', 'Avogadro constant N<sub>A</sub> = 6.022 140 76 × 10²³ mol⁻¹', False)],
    note='NCERT: the numbers need not be memorised; know which constant goes with which unit.', term='Constants that define the SI units')
d.basic('Correction: NCERT Table 1.1 writes e = 1.602176634 × 10¹⁹ C. What is right?', 'e = 1.602 × 10' + X('⁻¹⁹') + ' C: the minus sign is missing in the book. (It also writes k⁻¹ for ' + T('K⁻¹') + ' in the kelvin row.)')
d.basic('When using the mole, what must be specified?', 'The ' + T('elementary entities') + ': atoms, molecules, ions, electrons, other particles or groups')
d.basic('Define the radian (plane angle).', r'\( d\theta = \dfrac{ds}{r} \)' + ' : arc length ÷ radius', **fig('fig_1_1_angles'))
d.basic('Define the steradian (solid angle).', r'\( d\Omega = \dfrac{dA}{r^2} \)' + ' : intercepted spherical area ÷ radius²', **fig('fig_1_1_angles'))
d.basic('Dimensions of the radian and steradian?', T('Dimensionless') + ' (ratio of like quantities). Symbols ' + N('rad') + ' and ' + N('sr'))
d.basic('Total solid angle around a point? Total plane angle?', N('4π sr') + ' (4πr² / r²) and ' + N('2π rad'))
d.basic('1° in radians?', r'\( 1^\circ = \dfrac{\pi}{180} \)' + ' rad ≈ ' + N('0.01745 rad'), **fig('tab_1_2_units_outside_si'))
table_card(d, 'Table 1.2 · units outside SI', 'Value in SI?', [
    ('1 litre (L)', '1 dm³ = 10⁻³ m³', False), ('1 tonne (t)', '10³ kg', False), ('1 quintal (q)', '100 kg', False),
    ('1 bar', '0.1 MPa = 10⁵ Pa', False), ('1 atm', '101325 Pa ≈ 1.013 × 10⁵ Pa', False),
    ('1 hectare (ha)', '1 hm² = 10⁴ m²', False)], term='Units retained for general use (Table 1.2)')
table_card(d, 'Table 1.2 · units outside SI', 'Value in SI?', [
    ('1 carat', '200 mg', False), ('1 barn (b)', '100 fm² = 10⁻²⁸ m²', False), ('1 curie (Ci)', '3.7 × 10¹⁰ s⁻¹', False),
    ('1 roentgen (R)', '2.58 × 10⁻⁴ C/kg', False), ('1 year', '365.25 d = 3.156 × 10⁷ s', False), ('1 are (a)', '1 dam² = 10² m²', False)],
    term='More units outside SI (Table 1.2)')
table_card(d, 'Teacher addition · handy length units', 'Value in metres?', [
    ('1 fermi (fm)', '10⁻¹⁵ m', False), ('1 ångström (Å)', '10⁻¹⁰ m', False), ('1 light year (ly)', '9.46 × 10¹⁵ m', False),
    ('1 astronomical unit (AU)', '1.496 × 10¹¹ m', False), ('1 parsec (pc)', '3.08 × 10¹⁶ m ≈ 3.26 ly', False)],
    note='Light year is a unit of <b>distance</b>, not time.', term='Fermi, angstrom, light year, AU, parsec')
d.basic('Trap: is a light year a unit of time?', X('No') + ': it is the ' + T('distance') + ' light travels in one year, ≈ ' + N('9.46 × 10¹⁵ m'))
d.basic('Exercise 1.5: a unit of length is chosen so that c = 1. Sun–Earth distance if light takes 8 min 20 s?', N('500') + ' new units (= 500 light-seconds)')

# ---------------------------------------------------------------- 1.3 Significant figures
d.sec('1.3-significant-figures')
d.cloze('Significant figures = the {{c1::reliable digits}} plus the {{c2::first uncertain digit}}.')
sp.ruler_sig_figs(d)
d.basic('Pendulum period 1.62 s: which digits are certain?', T('1 and 6') + ' certain; ' + N('2') + ' uncertain → 3 significant figures')
d.basic('What do significant figures indicate?', 'The ' + T('precision') + ' of a measurement, set by the ' + T('least count') + ' of the instrument')
d.basic('Does changing units change the number of significant figures?', X('No') + ': 2.308 cm = 0.02308 m = 23.08 mm, all four significant figures')
d.basic('Correction: NCERT writes 2.308 cm = "23080 mm". What is right?', '2.308 cm = 23.08 mm = ' + T('23080 μm') + ' (micrometres); the book has a typo')
table_card(d, 'Significant figure rules', 'Significant or not?', [
    ('All non-zero digits', 'Significant', False),
    ('Zeros between non-zero digits (2.0308)', 'Significant', False),
    ('Leading zeros in a number < 1 (0.002308)', 'Not significant', True),
    ('Trailing zeros, no decimal point (12300)', 'Not significant', True),
    ('Trailing zeros after a decimal point (3.500)', 'Significant', False)],
    note='The 0 written before the decimal point (0.1250) is never significant.', term='Rules for counting significant figures')
d.basic('How many significant figures in 123 m = 12300 cm = 123000 mm?', N('3') + ' in each (trailing zeros without a decimal are not significant)')
d.basic('How many significant figures in 3.500 and in 0.06900?', N('4') + ' each')
d.basic('4.700 m = 4700 mm. Why does "4700 mm" mislead?', 'By the trailing-zero rule it looks like ' + X('2') + ' significant figures, but it has ' + T('4') + '; a unit change cannot change that')
d.basic('How does scientific notation remove the trailing-zero confusion?', 'Write a × 10ᵇ: ' + T('every digit in a is significant') + '. 4.700 × 10³ mm has 4')
d.basic('Is the power of 10 counted in significant figures?', X('No') + '; it is irrelevant to the count')
table_card(d, 'Exercise 1.10', 'Number of significant figures?', [
    ('0.007 m²', '1', False), ('2.64 × 10²⁴ kg', '3', False), ('0.2370 g cm⁻³', '4', False),
    ('6.320 J', '4', False), ('6.032 N m⁻²', '4', False), ('0.0006032 m²', '4', False)], term='Count significant figures (Exercise 1.10)')
d.basic('How many significant figures does an exact number like the 2 in s = 2πr have?', T('Infinite') + ': exact counts and factors do not limit the result')

d.sec('1.3-order-of-magnitude')
d.basic('What is the order of magnitude of a quantity?', 'Write it as a × 10ᵇ, round a to 1 (a ≤ 5) or 10 (a > 5); the resulting power ' + T('b') + ' is the order of magnitude')
d.basic('Order of magnitude of Earth’s diameter (1.28 × 10⁷ m) and an H atom (1.06 × 10⁻¹⁰ m)?', N('7') + ' and ' + N('−10') + '; Earth is ' + N('17 orders') + ' larger')
d.basic('Note: order of magnitude of 4 × 10⁶ — NCERT rule vs √10 rule?', 'NCERT (round a ≤ 5 down): ' + N('6') + '. Many JEE books round down only if a < √10 ≈ 3.16, giving ' + N('7') + '. In boards and NEET, follow ' + T('NCERT'))

d.sec('1.3.1-arithmetic-rules')
d.cloze('In multiplication or division, keep as many {{c1::significant figures}} as the number with the {{c2::fewest significant figures}}.')
d.cloze('In addition or subtraction, keep as many {{c1::decimal places}} as the number with the {{c2::fewest decimal places}}.')
d.basic('Density = 4.237 g ÷ 2.51 cm³ = 1.688047… Report?', N('1.69 g cm⁻³') + ' (3 significant figures, from 2.51)')
d.basic('436.32 g + 227.2 g + 0.301 g = 663.821 g. Report?', N('663.8 g') + ' (one decimal place, from 227.2)')
d.basic('0.307 m − 0.304 m. Report?', N('0.003 m = 3 × 10⁻³ m') + ', ' + X('not') + ' 3.00 × 10⁻³ m')
d.basic('Light year from c = 3.00 × 10⁸ m/s and 1 y = 3.1557 × 10⁷ s?', N('9.47 × 10¹⁵ m') + ' (3 significant figures)')
steps_card(d, 'Example 1.1', 'Find the missing step.', 'Each side of a cube is 7.203 m. Surface area and volume?',
           ['Side has 4 significant figures → answers keep 4', 'Area = 6(7.203)² = 311.299254 m²', 'Report area = <b>311.3 m²</b>',
            'Volume = (7.203)³ = 373.714754 → <b>373.7 m³</b>'], 2, 'Cube side 7.203 m: area and volume', 'Area 311.3 m², volume 373.7 m³ (4 significant figures)')
d.basic('Example 1.2: 5.74 g occupies 1.2 cm³. Density?', N('4.8 g cm⁻³') + ' (only 2 significant figures, from 1.2)')
d.basic('Exercise 1.11: sheet 4.234 m × 1.005 m × 2.01 cm. Area and volume?', 'Area ' + N('8.72 m²') + ', volume ' + N('0.0855 m³') + ' (3 significant figures, from 2.01)')
d.basic('Exercise 1.12: a 2.30 kg box plus gold pieces 20.15 g and 20.17 g. Difference of the pieces?', N('0.02 g') + ' (two decimal places)')
d.basic('Note: Exercise 1.12(a) total mass — NCERT key says 2.3 kg. What does the decimal-place rule give?',
        '2.30 + 0.02015 + 0.02017 = 2.34032 kg → ' + T('2.34 kg') + ' (2.30 has two decimal places). The key’s 2.3 kg drops a digit; if asked in a test, show the rule and write 2.34 kg')

d.sec('1.3.2-rounding-off')
d.basic('Round 2.746 and 1.743 to 3 significant figures.', N('2.75') + ' and ' + N('1.74'))
d.cloze('Rounding when the dropped digit is exactly 5: if the preceding digit is {{c1::even}}, just drop the 5; if it is {{c2::odd}}, raise it by 1.')
d.basic('Round 2.745 and 2.735 to 3 significant figures (NCERT rule).', 'Both → ' + N('2.74') + ' (4 is even: drop; 3 is odd: raise)')
d.basic('Intuition: why the "round half to even" rule?', 'Rounding 5 always up biases a long calculation upward.<br>Going to the even digit rounds up half the time and down half the time')
d.basic('In a multi-step calculation, how many digits do you keep in intermediate steps?', T('One more') + ' than the least precise measurement; round only at the end')
d.basic('Why keep an extra digit? (1/9.58 example)', '1/9.58 = 0.104 → 1/0.104 = ' + X('9.62') + '. With 0.1044 you get back ' + T('9.58'))
d.basic('What value of π to use?', '3.142 or 3.14, as the other data require (π is known to many figures)')

d.sec('1.3.3-uncertainty-in-results')
d.basic('A metre scale reads l = 16.2 cm. Absolute and percentage error?', N('± 0.1 cm') + ', i.e. ± 0.6 %')
d.basic('Combining errors in a product l × b?', T('Percentage errors add') + ': 0.6 % + 1 % = 1.6 %')
steps_card(d, '1.3.3 · Error in a product', 'Find the missing step.', 'l = 16.2 ± 0.1 cm, b = 10.1 ± 0.1 cm. Area with its error?',
           ['Δl/l = 0.6 %, Δb/b = 1 %', 'ΔA/A = 0.6 % + 1 % = 1.6 %', 'A = 163.62 cm², ΔA = 1.6 % of 163.62 ≈ 2.6 cm²',
            'Report <b>A = 164 ± 3 cm²</b>'], 1, 'Error in area of a sheet', 'Relative errors add: 1.6 %, so A = 164 ± 3 cm²')
d.basic('12.9 g − 7.06 g: report?', N('5.8 g') + ', not 5.84 g (subtraction can reduce significant figures)')
d.basic('1.02 g and 9.89 g are both ± 0.01 g. Relative errors?', N('± 1 %') + ' and ' + N('± 0.1 %') + ': relative error depends on the ' + T('size of the number') + ', not just the digits')
table_card(d, 'Teacher addition · error propagation', 'Error in Z?', [
    ('Z = A ± B', 'ΔZ = ΔA + ΔB (absolute errors add)', False),
    ('Z = AB or A/B', 'ΔZ/Z = ΔA/A + ΔB/B (relative errors add)', False),
    ('Z = Aⁿ', 'ΔZ/Z = n · ΔA/A', False),
    ('Z = Aᵖ Bᑫ / Cʳ', 'ΔZ/Z = pΔA/A + qΔB/B + rΔC/C', False)],
    note='Errors never cancel: always add, even for subtraction or division.', term='Rules for combining errors')
d.basic('Trap: Z = A − B. Do the errors subtract?', X('No') + ': ΔZ = ΔA + ΔB. Worst case, both errors push the same way')
d.basic('Teacher addition: g = 4π²L/T². L has 2 % error, T has 1 %. Error in g?', '2 % + 2 × 1 % = ' + N('4 %') + ' (T is squared)')
d.basic('Why should the quantity with the highest power be measured most precisely?', 'Its relative error is ' + T('multiplied by the power') + ' in the result')

# ---------------------------------------------------------------- 1.4–1.5 Dimensions
d.sec('1.4-dimensions')
d.basic('What are the dimensions of a physical quantity?', 'The ' + T('powers') + ' to which the base quantities are raised to represent it')
table_card(d, '1.4 · Dimension symbols', 'Symbol of each base dimension?', [
    ('Length', '[L]', False), ('Mass', '[M]', False), ('Time', '[T]', False), ('Electric current', '[A]', False),
    ('Temperature', '[K]', False), ('Luminous intensity', '[cd]', False), ('Amount of substance', '[mol]', False)],
    note='Many books use [I] for current and [θ] for temperature; [A] and [K] are NCERT’s.', term='Symbols of the seven dimensions')
d.basic('Which three dimensions are enough for mechanics?', '[M], [L], [T]')
d.basic('Dimensions of force from F = ma?', '[M L T⁻²]: one in mass, one in length, −2 in time')
d.basic('Why do speed, initial velocity and change in velocity all have the same dimensions?', 'Dimensions ignore magnitude and type; all are ' + T('length/time') + ' = [L T⁻¹]')
d.cloze('The {{c1::dimensional formula}} shows which base quantities, with which powers, make up a quantity, e.g. [M⁰ L T⁻¹] for velocity; equating the quantity to it, [v] = [M⁰ L T⁻¹], is its {{c2::dimensional equation}}.')
table_card(d, '1.5 · dimensional formulae', 'Dimensional formula?', [
    ('Volume', '[M⁰ L³ T⁰]', False), ('Density', '[M L⁻³]', False), ('Acceleration', '[L T⁻²]', False),
    ('Momentum, impulse', '[M L T⁻¹]', False), ('Work, energy, torque', '[M L² T⁻²]', False), ('Power', '[M L² T⁻³]', False)],
    term='Dimensional formulae: mechanics set 1')
table_card(d, 'Teacher addition · dimensional formulae', 'Dimensional formula?', [
    ('Pressure, stress, Young’s modulus', '[M L⁻¹ T⁻²]', False), ('Surface tension, spring constant', '[M T⁻²]', False),
    ('Gravitational constant G', '[M⁻¹ L³ T⁻²]', False), ('Planck constant h, angular momentum', '[M L² T⁻¹]', False),
    ('Coefficient of viscosity η', '[M L⁻¹ T⁻¹]', False), ('Frequency, angular velocity', '[T⁻¹]', False)],
    term='Dimensional formulae: set 2')
table_card(d, 'Teacher addition · dimensionless', 'Dimensions?', [
    ('Strain', 'none', False), ('Angle (rad), solid angle (sr)', 'none', False), ('Refractive index', 'none', False),
    ('Relative density', 'none', False), ('Coefficient of friction μ', 'none', False)],
    note='Ratios of like quantities are dimensionless. A dimensionless quantity may still have a unit (rad).', term='Dimensionless quantities')
d.basic('Mnemonic: quantities sharing [M L² T⁻²]?', T('Work, energy, torque') + ': "a torque does the Work of Energy". Torque is N m, but never called joule')
d.basic('Trap: can a quantity have a unit but no dimensions?', T('Yes') + ': angle has the unit radian but is dimensionless')

# ---------------------------------------------------------------- 1.6 Dimensional analysis
d.sec('1.6-dimensional-analysis')
d.cloze('Principle of {{c1::homogeneity}} of dimensions: only quantities with the {{c2::same dimensions}} can be added, subtracted or equated.')
d.basic('Can velocity be added to force?', X('No') + ': different dimensions')
d.basic('What must be true of the argument of sin, log or exp?', 'It must be ' + T('dimensionless') + ' (e.g. ωt in sin ωt)')
d.basic('Check x = x₀ + v₀t + ½at².', 'Each term is [L]: [x₀] = L, [v₀t] = L T⁻¹·T = L, [at²] = L T⁻²·T² = L → ' + T('consistent'))
d.basic('An equation is dimensionally correct. Is it right?', X('Not necessarily') + ': dimensionless factors (½, 2π) are unchecked. A dimensionally ' + T('wrong') + ' equation is ' + T('surely wrong'))
d.basic('Example 1.3: is ½mv² = mgh dimensionally correct?', T('Yes') + ': both sides [M L² T⁻²]')
d.basic('Example 1.4: which formulas for kinetic energy fail? (a) m²v³ (b) ½mv² (c) ma (d) (3/16)mv² (e) ½mv² + ma',
        X('(a), (c), (e)') + '. Dimensions cannot choose between (b) and (d); the definition gives (b)')
d.basic('Exercise 1.13: fix m = m₀ / (1 − v²)^½ using dimensions.', r'\( m = \dfrac{m_0}{\sqrt{1 - v^2/c^2}} \)' + ' : 1 − v² needs v² divided by c² to be dimensionless')

d.sec('1.6.2-deducing-relations')
d.basic('How is dimensional analysis used to deduce a relation?', 'Assume a ' + T('product of powers') + ' Q = k aˣ bʸ cᶻ, then equate powers of M, L, T')
steps_card(d, 'Example 1.5 · pendulum', 'Find the missing step.', 'Period T depends on length l, mass m and g. Find the formula by dimensions.',
           ['T = k lˣ gʸ mᶻ', '[T] = [L]ˣ [L T⁻²]ʸ [M]ᶻ = Lˣ⁺ʸ T⁻²ʸ Mᶻ', 'x + y = 0, −2y = 1, z = 0',
            'x = ½, y = −½, z = 0 → <b>T = k√(l/g)</b>'], 2, 'Pendulum period by dimensions', 'T = k√(l/g); k = 2π comes from experiment/theory, not dimensions')
d.basic('What does the pendulum result say about the bob’s mass?', 'Period is ' + T('independent of mass') + ' (z = 0)')
table_card(d, 'Limits of dimensional analysis', 'Can dimensions do this?', [
    ('Find dimensionless constants (2π, ½)', 'No', True), ('Tell apart quantities with the same dimensions (work vs torque)', 'No', True),
    ('Derive relations with sin, log, exp', 'No', True), ('Handle a quantity depending on > 3 variables (in mechanics)', 'No', True),
    ('Check consistency, convert units, guess relations', 'Yes', False)], term='Limitations of dimensional analysis')

d.sec('1.6-unit-conversion')
d.basic('Teacher addition: rule for converting a value between unit systems?', r'\( n_1 u_1 = n_2 u_2 \)' + ', so ' + r'\( n_2 = n_1\left[\dfrac{M_1}{M_2}\right]^a\left[\dfrac{L_1}{L_2}\right]^b\left[\dfrac{T_1}{T_2}\right]^c \)' + ' for [MᵃLᵇTᶜ]')
steps_card(d, 'Unit conversion', 'Find the missing step.', 'Convert 1 J into erg (CGS).',
           ['[energy] = [M L² T⁻²]', 'n₂ = 1 × (1 kg / 1 g)¹ × (1 m / 1 cm)² × (1 s / 1 s)⁻²', '= 10³ × (10²)² = <b>10⁷ erg</b>'], 1,
           'Joule to erg', '1 J = 10⁷ erg')
d.basic('Exercise 1.2(d): G = 6.67 × 10⁻¹¹ N m² kg⁻² in cm³ s⁻² g⁻¹?', N('6.67 × 10⁻⁸') + '  ([M⁻¹ L³ T⁻²]: 10⁻³ × 10⁶ = 10³ factor)')
d.basic('Exercise 1.3: 1 cal = 4.2 J. Its value if units of mass, length, time are α kg, β m, γ s?', N('4.2 α⁻¹ β⁻² γ²'))
d.basic('Exercise 1.2(c): 3.0 m s⁻² in km h⁻²?', N('3.9 × 10⁴ km h⁻²') + ' (3.0 × 10⁻³ × 3600²)')
d.basic('Exercise 1.1(c): 18 km/h covers how far in 1 s?', N('5 m') + ' (× 5/18 converts km/h to m/s)')

# ---------------------------------------------------------------- Summary
d.sec('summary')
table_card(d, 'Summary', 'Which rule applies?', [
    ('Multiply / divide measured values', 'fewest significant figures', False),
    ('Add / subtract measured values', 'fewest decimal places', False),
    ('Dropped digit exactly 5', 'round to even preceding digit', False),
    ('Error of a product / quotient', 'add percentage errors', False),
    ('Error of a sum / difference', 'add absolute errors', False)], term='Chapter 1 rules at a glance')
d.basic('Exercise 1.17: estimate the Sun’s mean density (M = 2.0 × 10³⁰ kg, R = 7.0 × 10⁸ m).', N('≈ 1.4 × 10³ kg m⁻³') + ': like liquids/solids, not gases, because gravity compresses it')

print(d.write(os.path.join(OUT, 'deck.json')), 'cards')
