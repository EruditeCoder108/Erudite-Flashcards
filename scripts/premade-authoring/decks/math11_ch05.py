import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase_math as sm

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Mathematics', 'class11-mathematics-ch05-linear-inequalities')
d = Deck('Chapter 5: Linear Inequalities', 'Class 11', ['class-11', 'mathematics', 'ch-5'])
d.description = 'Inequalities, rules for solving, number-line graphs, double inequalities, systems, word problems, modulus and quadratic inequalities, half-planes.'
b = d.basic

# ---------------------------------------------------------------- 5.2 Inequalities
d.sec('5.2-inequalities')
b('Define an inequality.', 'Two real numbers or algebraic expressions related by ' + T('<, >, ≤ or ≥'))
b('Numerical, literal and double inequalities: one example each?', 'Numerical: 3 < 5. Literal: x ≥ 3. Double: ' + T('3 < x < 5') + ' (x is between 3 and 5)')
b('Strict vs slack inequalities?', T('Strict') + ': < and > (endpoint excluded). ' + T('Slack') + ' (non-strict): ≤ and ≥ (endpoint included)')
b('When is ax + b < 0 a linear inequality in one variable?', 'When ' + T('a ≠ 0') + '. In two variables, ax + by < c with a ≠ 0, b ≠ 0')
b('Is ax² + bx + c ≤ 0 linear?', X('No') + ': it is a quadratic inequality in one variable (a ≠ 0)')
b('Ravi has ₹200 and buys x packets of rice at ₹30 each (whole packets only). Write the inequality.', T('30x < 200') + ': he cannot spend exactly ₹200 with whole packets, so the spending is strictly less')
b('Reshma has ₹120; registers cost ₹40, pens ₹20. Write the inequality for x registers and y pens.', T('40x + 20y ≤ 120') + ', which combines 40x + 20y < 120 (inequality) and 40x + 20y = 120 (equation)')
b('What is a solution and a solution set of an inequality?', 'A value of the variable that makes it a ' + T('true statement') + '; the solution set is all such values. E.g. 30x < 200 (whole numbers): {0, 1, 2, 3, 4, 5, 6}')

# ---------------------------------------------------------------- 5.3 Rules
d.sec('5.3-rules')
b('Rule 1 for solving inequalities?', T('Add or subtract the same number') + ' on both sides: the sign is unchanged')
b('Rule 2 for solving inequalities?', 'Multiply or divide both sides by the same ' + T('positive') + ' number: sign unchanged. By a ' + X('negative') + ' number: ' + X('reverse the sign') + ' (< ↔ >, ≤ ↔ ≥)')
b('Why does multiplying by a negative reverse the inequality? Examples?', '3 > 2 but −3 < −2; −8 < −7 but (−8)(−2) = 16 > 14 = (−7)(−2)')
sm.sign_flip(d)
b('Trap: solve −2x < 4.', 'Divide by −2 and ' + X('flip') + ': ' + N('x > −2') + '. Forgetting the flip is the most common mistake')
b('Trap: if 0 < a < b, compare 1/a and 1/b.', N('1/a > 1/b') + '. Taking reciprocals of positive numbers reverses the order (1/2 > 1/3). If a < 0 < b, then 1/a < 1/b')
b('Can you square both sides of an inequality?', 'Only when both sides are ' + T('non-negative') + '. −3 < 2 but (−3)² = 9 > 4. Safe form: a² < b² ⟺ |a| < |b|')
b('Trap: solve (x + 1)/(x − 2) ≥ 0 by cross-multiplying?', X('Never multiply by an expression of unknown sign') + '.<br>Use signs instead: the answer is x ≤ −1 or x > 2<br>The point 2 is excluded because it makes the denominator 0')
b('Example 1: solve 30x < 200 for (i) natural x, (ii) integer x.', 'x < 20/3 ≈ 6.67. (i) ' + N('{1, 2, 3, 4, 5, 6}') + ' (ii) ' + N('{…, −2, −1, 0, 1, 2, 3, 4, 5, 6}'))
b('Ex 5.1 Q1: solve 24x < 100 for natural and integer x.', 'x < 25/6 ≈ 4.17: natural ' + N('{1, 2, 3, 4}') + '; integers ' + N('{…, −1, 0, 1, 2, 3, 4}'))
b('Ex 5.1 Q2: solve −12x > 30 for natural and integer x.', 'Divide by −12 and flip: x < −5/2. Natural: ' + N('no solution (φ)') + '; integers: ' + N('{…, −4, −3}'))
b('Example 2: solve 5x − 3 < 3x + 1 for (i) integer x, (ii) real x.', '2x < 4 → x < 2. (i) ' + N('{…, −1, 0, 1}') + ' (ii) ' + N('(−∞, 2)'))
b('Example 3: solve 4x + 3 < 6x + 7.', '−2x < 4 → x > −2: ' + N('(−2, ∞)'))
b('Example 4: solve (5 − 2x)/3 ≤ x/6 − 5.', 'Multiply by 6: 2(5 − 2x) ≤ x − 30 → 10 − 4x ≤ x − 30 → −5x ≤ −40 → ' + N('x ≥ 8') + ', i.e. [8, ∞)')
b('Method: solving a linear inequality with fractions.', '1) Multiply by the ' + T('LCD (positive)') + ' to clear fractions. 2) Expand brackets. 3) Collect x on one side. 4) Divide by its coefficient, ' + X('flipping if negative') + '. 5) Write the answer as an interval')
b('Ex 5.1 Q5–8: solve 4x + 3 < 5x + 7; 3x − 7 > 5x − 1; 3(x − 1) ≤ 2(x − 3); 3(2 − x) ≥ 2(1 − x).', N('x > −4') + ';  ' + N('x < −3') + ';  ' + N('x ≤ −3') + ';  ' + N('x ≤ 4'))
b('Ex 5.1 Q13: solve 2(2x + 3) − 10 < 6(x − 2).', '4x + 6 − 10 < 6x − 12 → −4 + 12 < 2x → ' + N('x > 4'))
b('Ex 5.1 Q14: solve 37 − (3x + 5) > 9x − 8(x − 3).', '32 − 3x > x + 24 → 8 > 4x → ' + N('x < 2'))

d.sec('5.3-graphs')
b('Number line: how do you graph x < a and x > a?', T('Open circle') + ' at a (a excluded), thick line to the left for x < a, to the right for x > a')
b('Number line: how do you graph x ≤ a and x ≥ a?', T('Filled circle') + ' at a (a included), thick line to the left (≤) or right (≥)')
sm.nl_answer(d, 'Example 5: solve 7x + 3 < 5x + 9 and graph the solution.', [(None, 3, False, False, 'c1')],
             '<p>2x &lt; 6 → <b>x &lt; 3</b>, i.e. (−∞, 3). Open circle at 3, ray to the left.</p>', 'Example 5: graph of x < 3',
             '7x+3<5x+9 gives x<3; open circle at 3 with the ray to the left')
sm.nl_answer(d, 'Example 6: solve (3x − 4)/2 ≥ (x + 1)/4 − 1 and graph the solution.', [(1, None, True, False, 'c1')],
             '<p>Multiply by 4: 2(3x − 4) ≥ x − 3 → 6x − 8 ≥ x − 3 → 5x ≥ 5 → <b>x ≥ 1</b>, i.e. [1, ∞). Filled circle at 1, ray to the right.</p>',
             'Example 6: graph of x ≥ 1', '(3x−4)/2 ≥ (x+1)/4 − 1 gives x ≥ 1; filled circle at 1 with the ray to the right')
b('Ex 5.1 Q17–19: solve 3x − 2 < 2x + 1; 5x − 3 > 3x − 5; 3(1 − x) < 2(x + 4).', N('x < 3') + ';  ' + N('x > −1') + ';  3 − 3x < 2x + 8 → ' + N('x > −1'))

# ---------------------------------------------------------------- Word problems
d.sec('5.3-word-problems')
b('Method: translating a word problem into an inequality.', 'Let x be the unknown. Translate: “at least” → ' + T('≥') + ', “at most / not more than” → ' + T('≤') + ', “more than” → >, “less than” → <. Solve, then interpret (integers? natural numbers?)')
b('Example 7: marks 62 and 48 in two terms. Minimum marks in the annual exam for an average of at least 60?', '(62 + 48 + x)/3 ≥ 60 → 110 + x ≥ 180 → ' + N('x ≥ 70'))
b('Ex 5.1 Q21: Ravi scored 70 and 75. Minimum in the third test for an average of at least 60?', '(145 + x)/3 ≥ 60 → x ≥ ' + N('35'))
b('Ex 5.1 Q22: Sunita has 87, 92, 94, 95. Minimum in the fifth exam to average at least 90?', '(368 + x)/5 ≥ 90 → 368 + x ≥ 450 → x ≥ ' + N('82'))
b('Example 8: pairs of consecutive odd naturals, both larger than 10, sum less than 40?', 'x > 10 and 2x + 2 < 40 → 10 < x < 19, x odd → ' + N('(11,13), (13,15), (15,17), (17,19)'))
b('Ex 5.1 Q23: consecutive odd positive integers, both smaller than 10, sum more than 11?', 'x + 2 < 10 and 2x + 2 > 11 → 4.5 < x < 8, x odd: ' + N('(5, 7) and (7, 9)'))
b('Ex 5.1 Q24: consecutive even positive integers, both larger than 5, sum less than 23?', 'x > 5 and 2x + 2 < 23 → 5 < x < 10.5, x even: ' + N('(6, 8), (8, 10), (10, 12)'))
b('Ex 5.1 Q25: longest side = 3 × shortest, third side = longest − 2. Perimeter ≥ 61. Minimum shortest side?', 'x + 3x + (3x − 2) ≥ 61 → 7x ≥ 63 → x ≥ ' + N('9 cm'))
b('Ex 5.1 Q26: board of 91 cm cut into x, x + 3, 2x; the third must be at least 5 cm longer than the second. Range of x?', 'x + (x + 3) + 2x ≤ 91 → x ≤ 22; 2x ≥ (x + 3) + 5 → x ≥ 8. So ' + N('8 ≤ x ≤ 22'))

# ---------------------------------------------------------------- Double inequalities and systems
d.sec('5.x-double-and-systems')
b('Method: solve a double inequality like a ≤ f(x) < b.', 'Apply every operation to ' + T('all three parts') + ' at once<br>(add, multiply, flip the signs if you multiply by a negative)<br>until x is alone in the middle')
b('Example 9: solve −8 ≤ 5x − 3 < 7.', '−5 ≤ 5x < 10 → ' + N('−1 ≤ x < 2'))
b('Example 10: solve −5 ≤ (5 − 3x)/2 ≤ 8.', '−10 ≤ 5 − 3x ≤ 16 → −15 ≤ −3x ≤ 11 → divide by −3 (flip both): ' + N('−11/3 ≤ x ≤ 5'))
b('Trap: after dividing a double inequality by a negative number, what changes?', X('Both signs flip and the two end values swap places') + '<br>−15 ≤ −3x ≤ 11 becomes 5 ≥ x ≥ −11/3<br>written −11/3 ≤ x ≤ 5')
b('Misc Q1 and Q2: solve 2 ≤ 3x − 4 ≤ 5 and 6 ≤ −3(2x − 4) < 12.', '6 ≤ 3x ≤ 9 → ' + N('[2, 3]') + '. Second: 6 ≤ −6x + 12 < 12 → −6 ≤ −6x < 0 → ' + N('0 < x ≤ 1'))
b('Method: solving a system of inequalities in one variable.', '1) Solve each inequality separately.<br>2) Graph both on one number line.<br>3) Take the ' + T('overlap (intersection)') + ' of the solution sets')
b('Example 11: solve 3x − 7 < 5 + x and 11 − 5x ≤ 1.', 'x < 6 and x ≥ 2 → common part ' + N('[2, 6)'))
sm.nl_answer(d, 'Example 11: show the solution of {3x − 7 < 5 + x, 11 − 5x ≤ 1} on the number line.', [(2, 6, True, False, 'c3')],
             '<p>x &lt; 6 and x ≥ 2. The bold stretch where both hold: <b>2 ≤ x &lt; 6</b>.</p>', 'Example 11: system solution on the number line',
             '3x−7<5+x gives x<6; 11−5x≤1 gives x≥2; the common part is 2≤x<6')
b('Misc Q7: solve 5x + 1 > −24 and 5x − 1 < 24.', 'x > −5 and x < 5 → ' + N('(−5, 5)'))
b('Misc Q8: solve 2(x − 1) < x + 5 and 3(x + 2) > 2 − x.', 'x < 7 and x > −1 → ' + N('(−1, 7)'))
b('Misc Q9: solve 3x − 7 > 2(x − 6) and 6 − x > 11 − 2x.', 'x > −5 and x > 5 → the overlap is ' + N('(5, ∞)'))
b('Misc Q10: solve 5(2x − 7) − 3(2x + 3) ≤ 0 and 2x + 19 ≤ 6x + 47.', '4x ≤ 44 → x ≤ 11; −28 ≤ 4x → x ≥ −7: ' + N('[−7, 11]'))
b('When is the solution of a system empty?', 'When the individual solution sets ' + T('do not overlap') + ', e.g. x > 5 and x < 2')

# ---------------------------------------------------------------- Applications
d.sec('5.x-applications')
b('Example 12: acid to be kept between 30°C and 35°C. Range in °F using C = (5/9)(F − 32)?', '30 < (5/9)(F − 32) < 35 → 54 < F − 32 < 63 → ' + N('86 < F < 95'))
b('Misc Q11: solution between 68°F and 77°F. Range in °C (F = 9C/5 + 32)?', '68 ≤ 9C/5 + 32 ≤ 77 → 36 ≤ 9C/5 ≤ 45 → ' + N('20 ≤ C ≤ 25'))
b('Example 13: 600 L of 12% acid; how much 30% acid to add so the mixture is between 15% and 18%?', 'Acid: 0.30x + 72. Need 0.15(x + 600) < 0.30x + 72 < 0.18(x + 600) → x > 120 and x < 300: ' + N('120 < x < 300 litres'))
b('Method: mixture problems with percentages.', 'Write “acid in mixture = acid from each part”, and “total acid ÷ total volume” between the two limits; clear the decimals with the LCD; solve the double inequality')
b('Misc Q12: 640 L of 8% boric acid; add x L of 2% so that the mixture is between 4% and 6%. Range of x?', '51.2 + 0.02x > 0.04(640 + x) → x < 1280; 51.2 + 0.02x < 0.06(640 + x) → x > 320. So ' + N('320 < x < 1280'))
b('Misc Q13: 1125 L of 45% acid; how much water must be added for between 25% and 30% acid?', 'Acid = 506.25 L. 0.25 < 506.25/(1125 + x) < 0.30 → 562.5 < x < 900 litres: ' + N('562.5 < x < 900'))
b('Misc Q14: IQ = (MA/CA) × 100, children of age 12, 80 ≤ IQ ≤ 140. Range of MA?', '80 ≤ (MA/12)·100 ≤ 140 → ' + N('9.6 ≤ MA ≤ 16.8'))

# ---------------------------------------------------------------- Beyond NCERT text: modulus, quadratic, rational, two variables
d.sec('5.z-modulus-inequalities')
sm.modulus_band(d)
table_card(d, 'Modulus inequalities · JEE/board', 'Rewrite (r > 0).', [
    ('|x| < r', '−r < x < r', False), ('|x| ≤ r', '−r ≤ x ≤ r', False), ('|x| > r', 'x < −r or x > r', False),
    ('|x| ≥ r', 'x ≤ −r or x ≥ r', False), ('|x − a| < r', 'a − r < x < a + r', False), ('|x| < negative number', 'no solution', True)],
    term='Modulus inequalities')
b('Solve |2x − 3| ≤ 5.', '−5 ≤ 2x − 3 ≤ 5 → −2 ≤ 2x ≤ 8 → ' + N('−1 ≤ x ≤ 4'))
b('Solve |x + 1| ≥ 3.', 'x + 1 ≤ −3 or x + 1 ≥ 3 → ' + N('x ≤ −4 or x ≥ 2'))
sm.nl_answer(d, 'Show the solution of |x − 1| ≥ 2 on the number line.', [(None, -1, False, True, 'c2'), (3, None, True, False, 'c2')],
             '<p>|x − 1| ≥ 2 → x − 1 ≤ −2 or x − 1 ≥ 2 → <b>x ≤ −1 or x ≥ 3</b>: two outer rays (a union).</p>',
             'Number line for |x − 1| ≥ 2', '|x−1|≥2 gives x≤−1 or x≥3: two rays, endpoints included', tag='Modulus · number line')
b('Triangle inequality for real numbers?', T('|a + b| ≤ |a| + |b|') + '; equality iff ab ≥ 0. Also |a − b| ≥ ||a| − |b||')
b('Trap: solving |x| < 3 as x < 3 only, or |x| > 3 as −3 < x?', X('Both wrong') + '. |x| < 3 is a band (AND): −3 < x < 3. |x| > 3 is two rays (OR): x < −3 or x > 3')
d.sec('5.z-quadratic-rational')
b('(x − a)(x − b) < 0 with a < b: solution?', T('a < x < b') + ' (between the roots). And (x − a)(x − b) > 0: x < a or x > b (outside the roots)')
b('Solve x² − 5x + 6 < 0.', '(x − 2)(x − 3) < 0 → ' + N('2 < x < 3'))
b('Solve x² − 5x + 6 > 0.', N('x < 2 or x > 3') + ' (outside the roots)')
b('Solve x² − 4 ≥ 0 and x² ≤ 9.', 'x² ≥ 4 → ' + N('x ≤ −2 or x ≥ 2') + '. x² ≤ 9 → ' + N('−3 ≤ x ≤ 3'))
b('Solve x² + x + 1 > 0.', 'D = 1 − 4 < 0 and a > 0, so the parabola is always above the axis: ' + N('all real x') + '<br>General rule: if D < 0, ax² + bx + c has the sign of a for every x')
sm.wavy_curve(d)
b('Method: solve a rational inequality such as (x + 1)/(x − 2) ≥ 0.', 'Critical points = zeros of numerator and denominator (−1, 2). Sign chart: + on the far right, alternate. Include numerator zeros only if ≥ or ≤; ' + X('always exclude denominator zeros') + '. Answer: (−∞, −1] ∪ (2, ∞)')
b('Solve (x − 3)/(x + 2) < 0.', 'Critical points −2, 3; the quotient is negative between them: ' + N('−2 < x < 3'))
b('AM–GM for positive numbers: x + 1/x ≥ ?', N('2') + ' for x > 0, with equality at x = 1. For x < 0, x + 1/x ≤ −2')
b('a > 0, b > 0: compare (a + b)/2 and √(ab).', T('(a + b)/2 ≥ √(ab)') + ' (AM ≥ GM), equality iff a = b. Proof: (√a − √b)² ≥ 0')
d.sec('5.z-two-variables')
b('Beyond the textbook text: how do you graph ax + by ≤ c?', '1) Draw the line ax + by = c (' + T('solid for ≤ ≥') + ', ' + T('dashed for < >') + '). 2) Test a point, usually the origin. 3) Shade the side that satisfies it')
sm.half_plane(d)
sm.feasible_region(d)
b('Which half-plane is x + y > 5 (test the origin)?', '0 + 0 > 5 is false, so shade the side ' + X('not') + ' containing the origin, with a dashed line')
b('What does x ≥ 0, y ≥ 0 mean geometrically?', 'The ' + T('first quadrant') + ' (including both axes)')
b('Vertices of the region 2x + y ≤ 8, x ≥ 0, y ≥ 0?', T('(0, 0), (4, 0), (0, 8)') + ': intercepts of 2x + y = 8 and the axes')

# ---------------------------------------------------------------- How it's asked
d.sec('5.z-how-its-asked')
b('MCQ: The solution of 3x − 7 > 5x − 1 is<br>(a) x > −3 (b) x < −3 (c) x > 3 (d) x < 3', E('(b)') + ': −6 > 2x → x < −3')
b('MCQ: If −3x + 17 < −13, then x ∈<br>(a) (10, ∞) (b) [10, ∞) (c) (−∞, 10] (d) [−10, 10)', '−3x < −30 → x > 10: ' + E('(a)'))
b('MCQ: The solution set of |x − 2| < 3 is<br>(a) (−1, 5) (b) [−1, 5] (c) (−5, 1) (d) (5, ∞)', E('(a)') + ': −3 < x − 2 < 3')
b('Integer answer (JEE Main): the number of integers x with −5 < 2x + 1 < 9?', '−6 < 2x < 8 → −3 < x < 4 → x = −2, …, 3: ' + N('6'))
b('MCQ: The number of positive integers satisfying x² − 5x + 6 ≤ 0 is<br>(a) 1 (b) 2 (c) 3 (d) 0', '2 ≤ x ≤ 3 → 2 and 3: ' + E('(b) 2'))
b('MCQ: The solution of (x + 2)/(x − 1) > 0 is<br>(a) (−2, 1) (b) (−∞, −2) ∪ (1, ∞) (c) [−2, 1) (d) (1, ∞)', 'Positive outside the roots −2 and 1 (both excluded): ' + E('(b)'))
b('Assertion–Reason.<br><b>A:</b> If a > b then ac > bc.<br><b>R:</b> Multiplying an inequality by a negative number reverses it.<br>(a) Both true, R explains A (b) Both true, R does not explain A (c) A false, R true (d) Both false', E('(c)') + ': A is false when c < 0 (or 0); R is the correct rule')
b('Assertion–Reason.<br><b>A:</b> The solution of x² + 1 < 0 is φ.<br><b>R:</b> x² + 1 ≥ 1 for all real x.<br>(a) Both true, R explains A (b) Both true, R does not explain A (c) A true, R false (d) A false, R true', E('(a)'))
b('True/False (2 marks): if x < y and z < 0 then xz < yz.', X('False') + ': multiplying by a negative z reverses it, so xz > yz')
b('2-mark: solve 2(x − 1) < x + 5 and represent the solution on the number line.', 'x < 7: ' + N('(−∞, 7)') + ', open circle at 7 with the ray to the left')
b('3-mark: solve −4 ≤ (3 − 2x)/5 < 1 and list the integral solutions.', '−20 ≤ 3 − 2x < 5 → −23 ≤ −2x < 2 → −1 < x ≤ 11.5. Integers: ' + N('0, 1, 2, …, 11'))
b('Case-based: a phone plan costs ₹200 + ₹1.5 per minute. Budget is at most ₹500. How many whole minutes can be used?', '200 + 1.5x ≤ 500 → x ≤ 200: ' + N('at most 200 minutes'))
b('Case-based: a fence needs a perimeter of at least 60 m for a rectangle whose length is 2 m more than its width w. Find w.', '2(w + w + 2) ≥ 60 → 4w + 4 ≥ 60 → ' + N('w ≥ 14 m'))

print('cards', len(d.cards))
os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
