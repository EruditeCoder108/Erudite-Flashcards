import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase_math as sm

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Mathematics', 'class11-mathematics-ch02-relations-and-functions')
d = Deck('Chapter 2: Relations and Functions', 'Class 11', ['class-11', 'mathematics', 'ch-2'])
d.description = 'Cartesian products, relations, domain and range, functions, standard graphs, modulus, signum and greatest integer, algebra of functions.'
b = d.basic

# ---------------------------------------------------------------- 2.2 Cartesian products
d.sec('2.2-cartesian-products')
b('What is an ordered pair?', 'Two elements grouped in a ' + T('particular order') + ', written (p, q). So (p, q) ≠ (q, p) unless p = q')
b('When are two ordered pairs (a, b) and (x, y) equal?', 'Iff ' + T('a = x') + ' and ' + T('b = y') + ' (first with first, second with second)')
b('Example 1: if (x + 1, y − 2) = (3, 1), find x and y.', 'x + 1 = 3, y − 2 = 1 → ' + N('x = 2, y = 3'))
b('Ex 2.1 Q1: (x/3 + 1, y − 2/3) = (5/3, 1/3). Find x, y.', 'x/3 + 1 = 5/3 → x = 2;  y − 2/3 = 1/3 → ' + N('x = 2, y = 1'))
b('Define the Cartesian product P × Q.', r'\(P \times Q = \{(p, q) : p \in P,\ q \in Q\}\)' + '<br><small>All ordered pairs: first from P, second from Q</small>')
b('A = {red, blue}, B = {b, c, s}. Write A × B. How many pairs?', '{(red,b), (red,c), (red,s), (blue,b), (blue,c), (blue,s)}: ' + N('6 pairs'))
b('n(A) = p, n(B) = q. n(A × B) = ?', N('pq'))
b('If either P or Q is empty, what is P × Q?', N('φ') + '. So A × φ = φ')
b('Is A × B = B × A?', X('Not in general') + '. P = {a, b, c}, Q = {r}: P × Q = {(a,r),(b,r),(c,r)} but Q × P = {(r,a),(r,b),(r,c)}. Same count, different pairs')
sm.cartesian_grid(d)
b('When is A × B = B × A (for non-empty sets)?', 'Only when ' + T('A = B'))
b('If A or B is infinite (and both non-empty), what about A × B?', T('Infinite'))
b('What is A × A × A?', r'\(\{(a, b, c) : a, b, c \in A\}\)' + ': ordered triplets. n = (n(A))³')
b('What do R × R and R × R × R represent?', T('R × R') + ': all points of the plane (x, y). ' + T('R × R × R') + ': all points of 3-D space (x, y, z)')
b('If P = {1, 2}, list P × P × P.', '{(1,1,1), (1,1,2), (1,2,1), (1,2,2), (2,1,1), (2,1,2), (2,2,1), (2,2,2)}: ' + N('8') + ' triplets')
b('Example 6: A × B = {(p, q), (p, r), (m, q), (m, r)}. Find A and B.', 'A = set of first elements = ' + N('{p, m}') + '; B = set of second elements = ' + N('{q, r}'))
b('Ex 2.1: n(A) = 3, B = {3, 4, 5}. n(A × B)?', N('9'))
b('Ex 2.1 Q3: G = {7, 8}, H = {5, 4, 2}. Write G × H and H × G.', 'G × H = {(7,5),(7,4),(7,2),(8,5),(8,4),(8,2)}<br>H × G = {(5,7),(5,8),(4,7),(4,8),(2,7),(2,8)}')
b('Trap (Ex 2.1 Q4): P = {m, n}, Q = {n, m}. Is P × Q = {(m, n), (n, m)}?', X('False') + '. P × Q takes ALL pairs: ' + T('{(m,m), (m,n), (n,m), (n,n)}') + '. P and Q are the same set, but the product still has 2 × 2 = 4 pairs')
b('A = {1, 2}, B = {3, 4}. Is A × (B ∩ φ) = φ?', E('True') + ': B ∩ φ = φ and A × φ = φ')
b('A = {−1, 1}. Write A × A × A.', '{(−1,−1,−1), (−1,−1,1), (−1,1,−1), (−1,1,1), (1,−1,−1), (1,−1,1), (1,1,−1), (1,1,1)}')
b('Ex 2.1 Q6: A × B = {(a,x), (a,y), (b,x), (b,y)}. Find A, B.', N('A = {a, b}, B = {x, y}'))
b('Ex 2.1 Q9: n(A) = 3, n(B) = 2, and (x,1), (y,2), (z,1) ∈ A × B, x, y, z distinct. Find A, B.', 'First elements are in A: ' + N('A = {x, y, z}') + ' (3 elements); second in B: ' + N('B = {1, 2}'))
b('Ex 2.1 Q10: A × A has 9 elements, including (−1, 0) and (0, 1). Find A.', 'n(A) = 3, and −1, 0, 1 all appear: ' + N('A = {−1, 0, 1}') + '<br><small>Remaining pairs: (−1,−1), (−1,1), (0,−1), (0,0), (1,−1), (1,0), (1,1)</small>')
table_card(d, '2.2 · Products and set operations', 'Example 3: A = {1,2,3}, B = {3,4}, C = {4,5,6}. Find:', [
    ('A × (B ∩ C)', '{(1,4), (2,4), (3,4)}', False), ('(A × B) ∩ (A × C)', '{(1,4), (2,4), (3,4)}: same', False),
    ('A × (B ∪ C)', '12 pairs = (A × B) ∪ (A × C)', False)], term='Products distribute over ∪ and ∩',
    note='A × (B ∩ C) = (A × B) ∩ (A × C) and A × (B ∪ C) = (A × B) ∪ (A × C)')
b('Distributive laws for the Cartesian product?', T('A × (B ∪ C) = (A × B) ∪ (A × C)') + ',  ' + T('A × (B ∩ C) = (A × B) ∩ (A × C)') + ',  ' + T('A × (B − C) = (A × B) − (A × C)'))
b('Ex 2.1 Q7: A = {1,2}, B = {1,2,3,4}, C = {5,6}, D = {5,6,7,8}. Is A × C ⊂ B × D?', E('Yes') + '. A ⊂ B and C ⊂ D, so every pair of A × C lies in B × D. In general A ⊂ B, C ⊂ D ⇒ A × C ⊂ B × D')
b('Ex 2.1 Q8: how many subsets does A × B have, A = {1,2}, B = {3,4}?', 'n(A × B) = 4, so ' + N('2⁴ = 16') + ' subsets')

# ---------------------------------------------------------------- 2.3 Relations
d.sec('2.3-relations')
b('Define a relation R from A to B.', 'A ' + T('subset of A × B') + ', found by describing how the first element x is related to the second y. y is the ' + T('image') + ' of x')
b('Relation: define domain, range and codomain.', T('Domain') + ' = set of all first elements. ' + T('Range') + ' = set of all second elements. ' + T('Codomain') + ' = the whole target set B. Range ⊂ codomain')
b('Trap: is the range always the whole codomain?', X('No') + '. Range ⊂ codomain; codomain is the set B named in the problem, range is only the values actually hit')
b('A relation from A to A is called?', 'A relation ' + T('on') + ' A')
sm.relation_arrow(d)
b('Example 8: P = {4, 9, 25}, Q = {1, ±2, ±3, ±5}, R = {(x, y) : x is the square of y}. Roster, domain, range?', 'R = {(9,3), (9,−3), (4,2), (4,−2), (25,5), (25,−5)}. Domain {4, 9, 25}; range {±2, ±3, ±5}. ' + T('1 ∈ Q is not an image') + ' (range ⊂ codomain). Not a function: each x has two images')
b('n(A) = p, n(B) = q. Total number of relations from A to B?', N('2^(pq)') + ': each relation is a subset of A × B, which has pq elements')
b('Example 9: A = {1, 2}, B = {3, 4}. Number of relations from A to B?', 'n(A × B) = 4 → ' + N('2⁴ = 16'))
b('Ex 2.2 Q8: A = {x, y, z}, B = {1, 2}. Relations from A to B?', N('2⁶ = 64'))
b('Ex 2.2 Q1: R = {(x, y) : 3x − y = 0} on A = {1, …, 14}. Roster, domain, range?', 'y = 3x ≤ 14 → x ≤ 4: R = ' + N('{(1,3), (2,6), (3,9), (4,12)}') + '. Domain {1,2,3,4}; range {3,6,9,12}; codomain {1,…,14}')
b('Ex 2.2 Q2: R = {(x, y) : y = x + 5, x ∈ N, x < 4}. Roster, domain, range?', N('{(1,6), (2,7), (3,8)}') + '. Domain {1,2,3}; range {6,7,8}')
b('Ex 2.2 Q3: A = {1,2,3,5}, B = {4,6,9}; R = {(x, y) : x − y is odd}. Roster form?', N('{(1,4), (1,6), (2,9), (3,4), (3,6), (5,4), (5,6)}') + '<br><small>Odd difference means opposite parity</small>')
b('Ex 2.2 Q5: A = {1,2,3,4,6}, R = {(a, b) : b is exactly divisible by a}. Roster, domain, range?',
  '(1,1),(1,2),(1,3),(1,4),(1,6),(2,2),(2,4),(2,6),(3,3),(3,6),(4,4),(6,6): ' + N('12 pairs') + '. Domain = range = A')
b('Ex 2.2 Q7: R = {(x, x³) : x is a prime less than 10}. Roster?', N('{(2,8), (3,27), (5,125), (7,343)}') + ' (primes below 10: 2, 3, 5, 7)')
b('Ex 2.2 Q6: R = {(x, x + 5) : x ∈ {0,…,5}}. Domain and range?', 'Domain {0,1,2,3,4,5}; range ' + N('{5, 6, 7, 8, 9, 10}'))
b('Ex 2.2 Q9: R = {(a, b) : a − b ∈ Z} on Z. Domain and range?', 'The difference of integers is always an integer, so R = Z × Z. Domain = ' + N('Z') + ', range = ' + N('Z'))
b('Preview (Ex 19): R on Q, (a, b) ∈ R iff a − b ∈ Z. Which three properties does it have?', T('Reflexive') + ' (a − a = 0 ∈ Z), ' + T('symmetric') + ' (b − a = −(a − b) ∈ Z), ' + T('transitive') + ' (a − c = (a − b) + (b − c) ∈ Z). Such a relation is an equivalence relation (Class 12)')
b('Misc Q9: R = {(a, b) : a = b², a, b ∈ N}. Reflexive? Symmetric? Transitive?', X('None') + '. (a,a) ∈ R needs a = a²: fails for a = 2. (4,2) ∈ R but (2,4) ∉ R. (16,4), (4,2) ∈ R but (16,2) ∉ R')

# ---------------------------------------------------------------- 2.4 Functions
d.sec('2.4-functions')
b('Define a function from A to B.', 'A relation in which ' + T('every element of A has one and only one image') + ' in B. Written f: A → B, f(a) = b')
b('Function, in terms of the relation’s ordered pairs?', 'Its ' + T('domain is all of A') + ' and ' + X('no two distinct pairs share the same first element'))
b('If (a, b) ∈ f, what are a and b called?', 'b = f(a) is the ' + T('image') + ' of a; a is a ' + T('preimage') + ' of b')
sm.arrow_diagrams(d)
b('Can two different inputs share the same output in a function?', E('Yes') + ' (many-to-one, e.g. f(x) = x²: f(2) = f(−2)). ' + X('No') + ' input may have two outputs')
b('Must every element of the codomain be used?', X('No') + '. Unused codomain elements are allowed; the set of used ones is the range')
sm.vertical_line_test(d)
b('Method: how do you test if a relation given as a list of pairs is a function?', 'Check the ' + T('first elements') + ': none may repeat with different second elements, and every element of the domain set must appear')
b('Ex 11: is {(2,1), (3,1), (4,2)} a function? {(2,2), (2,4), (3,3), (4,4)}?', E('First: yes') + ' (unique images). ' + X('Second: no') + ': 2 has images 2 and 4')
b('Is {(1,2), (2,3), (3,4), (4,5), (5,6), (6,7)} a function?', E('Yes') + ': every first element has exactly one image')
b('Ex 2.3 Q1: which are functions? (i) {(2,1),(5,1),(8,1),(11,1),(14,1),(17,1)} (ii) {(2,1),(4,2),(6,3),(8,4),(10,5),(12,6),(14,7)} (iii) {(1,3),(1,5),(2,5)}',
  E('(i) yes') + ', domain {2,5,8,11,14,17}, range {1}. ' + E('(ii) yes') + ', domain {2,4,…,14}, range {1,…,7}. ' + X('(iii) no') + ': 1 has two images')
b('Example 10: R = {(x, y) : y = 2x, x, y ∈ N}. Domain, codomain, range? Function?', 'Domain N, codomain N, range = ' + T('even naturals') + '. Every n has exactly one image 2n → ' + E('a function'))
b('Real valued function vs real function?', T('Real valued') + ': range ⊂ R. ' + T('Real function') + ': domain ⊂ R as well')
b('Example 12: f: N → N, f(x) = 2x + 1. Values for x = 1 to 7?', N('3, 5, 7, 9, 11, 13, 15') + ' (the odd numbers from 3)')
b('Ex 2.3 Q3: f(x) = 2x − 5. f(0), f(7), f(−3)?', N('−5') + ', ' + N('9') + ', ' + N('−11'))
b('Ex 2.3 Q4: t(C) = 9C/5 + 32. t(0), t(28), t(−10), and C when t(C) = 212?', N('32') + ', ' + N('412/5 = 82.4') + ', ' + N('14') + ', ' + N('C = 100'))

d.sec('2.4.1-standard-functions')
b('Identity function: rule, domain, range, graph?', T('f(x) = x') + '; domain R, range R; a line through the origin at 45°')
b('Constant function: rule, domain, range, graph?', T('f(x) = c') + '; domain R, range ' + N('{c}') + '; a horizontal line')
b('Polynomial function: definition?', r'\(f(x) = a_0 + a_1 x + a_2 x^2 + \cdots + a_n x^n\)' + ', where n is a ' + T('non-negative integer') + ' and the aᵢ are real')
b('Which are polynomials: x³ − x² + 2, x⁴ + √2 x, x^(2/3) + 2x, x + 1/x?', E('First two: yes') + '. ' + X('x^(2/3) + 2x') + ' (exponent 2/3 is not a non-negative integer) and ' + X('x + 1/x') + ' (1/x = x⁻¹) are not')
b('Rational function: definition and domain?', r'\(\dfrac{f(x)}{g(x)}\)' + ' with f, g polynomials; defined where ' + T('g(x) ≠ 0'))
b('What is a linear function?', T('f(x) = mx + c') + ' (m, c constants). Its graph is a straight line with slope m, y-intercept c')
b('Ex 20: f is linear with f(1) = 1 and f(0) = −1. Find f(x).', 'c = f(0) = −1; m + c = 1 → m = 2. ' + N('f(x) = 2x − 1') + '. Check: f(2) = 3 ✓ and f(−1) = −3 ✓')
sm.standard_graphs(d)
b('f(x) = x²: table for x = −4 … 4?', N('16, 9, 4, 1, 0, 1, 4, 9, 16') + ': symmetric because f(−x) = f(x)')
b('f(x) = 1/x: domain and range?', 'Domain ' + N('R − {0}') + '; range ' + N('R − {0}') + ' (1/x can never equal 0)')
b('Modulus function: definition?', r'\(f(x) = |x| = \begin{cases} x, & x \ge 0 \\ -x, & x < 0 \end{cases}\)' + '. Domain R, range [0, ∞)')
sm.modulus_flip(d)
b('Trap: |x| = x is true for?', 'Only ' + T('x ≥ 0') + '. For x < 0, |x| = −x (positive). E.g. |−3| = 3, not −3')
b('|x| in terms of a square root?', T('|x| = √(x²)') + ', so √(x²) ≠ x for negative x')
b('Signum function: definition, domain, range?', r'\(f(x) = \begin{cases} 1, & x > 0 \\ 0, & x = 0 \\ -1, & x < 0 \end{cases}\)' + '. Domain R, range ' + N('{−1, 0, 1}'))
sm.signum_graph(d)
b('Greatest integer function: definition and range?', T('[x]') + ' = greatest integer ≤ x. Domain R, range ' + N('Z') + '. [x] = n for n ≤ x < n + 1')
sm.greatest_integer_graph(d)
b('Evaluate [3.7], [−3.7], [−2], [0.999].', N('3') + ', ' + N('−4') + ', ' + N('−2') + ', ' + N('0') + '<br><small>Trap: [−3.7] is −4, not −3</small>')
b('Fractional part {x}: definition, range?', T('{x} = x − [x]') + ', so ' + N('0 ≤ {x} < 1') + '. e.g. {−3.7} = −3.7 − (−4) = 0.3')
b('Properties of [x]: [x + n] for integer n; x − 1 < [x] ≤ x; [x] + [−x]?', T('[x + n] = [x] + n') + ';  ' + T('x − 1 < [x] ≤ x') + ';  [x] + [−x] = ' + N('0') + ' if x is an integer, ' + N('−1') + ' otherwise')

# ---------------------------------------------------------------- 2.4.2 Algebra
d.sec('2.4.2-algebra-of-functions')
table_card(d, '2.4.2 · Algebra of real functions', 'Define each on the common domain X.', [
    ('(f + g)(x)', 'f(x) + g(x)', False), ('(f − g)(x)', 'f(x) − g(x)', False), ('(αf)(x)', 'α · f(x)', False),
    ('(fg)(x)', 'f(x) · g(x)  (pointwise product)', False), ('(f/g)(x)', 'f(x) / g(x),  provided g(x) ≠ 0', True)],
    term='Algebra of real functions')
b('What is the domain of f + g, f − g and fg? Of f/g?', 'The ' + T('common domain') + ' X of f and g. For f/g, remove every x with ' + X('g(x) = 0'))
b('Example 16: f(x) = x², g(x) = 2x + 1. Find f + g, f − g, fg, f/g.', 'x² + 2x + 1;  x² − 2x − 1;  2x³ + x²;  x²/(2x + 1) with ' + X('x ≠ −½'))
b('Example 17: f(x) = √x, g(x) = x on [0, ∞). Find f + g, f − g, fg, f/g.', '√x + x;  √x − x;  x^(3/2);  1/√x, ' + X('x ≠ 0'))
sm.sum_of_graphs(d)
b('Is (fg)(x) the same as (f∘g)(x) = f(g(x))?', X('No') + '. (fg)(x) = f(x) × g(x). Composition (Class 12) feeds g’s output into f')

# ---------------------------------------------------------------- Domain and range technique
d.sec('2.z-domain-range')
table_card(d, 'Domain rules', 'What must hold for f to be defined?', [
    ('√(g(x))', 'g(x) ≥ 0', False), ('1 / g(x)', 'g(x) ≠ 0', True), ('1 / √(g(x))', 'g(x) > 0', False),
    ('ratio of polynomials', 'denominator ≠ 0', True), ('|g(x)|, g(x)²', 'no restriction beyond g', False)],
    term='Domain restrictions cheat-sheet')
b('Ex 2.3 Q2(ii): domain and range of f(x) = √(9 − x²).', 'Need 9 − x² ≥ 0 → ' + N('domain [−3, 3]') + '. Output between 0 (x = ±3) and 3 (x = 0): ' + N('range [0, 3]') + '. (It is the upper semicircle.)')
b('Ex 2.3 Q2(i): domain and range of f(x) = −|x|.', 'Domain ' + N('R') + '; |x| ≥ 0 so −|x| ≤ 0: range ' + N('(−∞, 0]'))
b('Ex 2.3 Q5: range of f(x) = 2 − 3x, x > 0; of x² + 2; of x?', 'x > 0 ⇒ 3x > 0 ⇒ ' + N('(−∞, 2)') + ';  x² + 2 ≥ 2 ⇒ ' + N('[2, ∞)') + ';  ' + N('R'))
b('Example 21: domain of f(x) = (x² + 3x + 5)/(x² − 5x + 4).', 'x² − 5x + 4 = (x − 1)(x − 4) = 0 at 1 and 4 → ' + N('R − {1, 4}'))
b('Misc Q3: domain of f(x) = (x² + 2x + 1)/(x² − 8x + 12).', '(x − 2)(x − 6) ≠ 0 → ' + N('R − {2, 6}'))
b('Misc Q4: domain and range of f(x) = √(x − 1).', 'x − 1 ≥ 0: domain ' + N('[1, ∞)') + '; range ' + N('[0, ∞)'))
b('Misc Q5: domain and range of f(x) = |x − 1|.', 'Domain ' + N('R') + '; range ' + N('[0, ∞)'))
b('Misc Q6: range of f(x) = x²/(1 + x²).', 'Let y = x²/(1 + x²) → x² = y/(1 − y) ≥ 0 → 0 ≤ y < 1: ' + N('[0, 1)'))
b('Method: finding the range by “solving for x”.', '1) Put y = f(x). 2) Solve for x in terms of y. 3) Find the y-values for which x is real and in the domain (e.g. discriminant ≥ 0, or an expression ≥ 0)')
b('Range of a quadratic ax² + bx + c on R?', 'Use the vertex value ' + r'\(f\!\left(-\tfrac{b}{2a}\right)\)' + ': if a > 0 the range is [vertex value, ∞); if a < 0, (−∞, vertex value]')
b('Misc Q2: f(x) = x². Find (f(1.1) − f(1))/(1.1 − 1).', '(1.21 − 1)/0.1 = ' + N('2.1') + '<br><small>This is an average rate of change: a preview of the derivative</small>')
b('Misc Q7: f(x) = x + 1, g(x) = 2x − 3. f + g, f − g, f/g?', N('3x − 2') + ',  ' + N('−x + 4') + ',  ' + N('(x + 1)/(2x − 3), x ≠ 3/2'))
b('Misc Q8: f = {(1,1), (2,3), (0,−1), (−1,−3)} with f(x) = ax + b. Find a, b.', 'f(0) = b = −1; f(1) = a + b = 1 → ' + N('a = 2, b = −1'))
b('Misc Q1: f(x) = x² (0 ≤ x ≤ 3), 3x (3 ≤ x ≤ 10); g(x) = x² (0 ≤ x ≤ 2), 3x (2 ≤ x ≤ 10). Which is a function?',
  T('f is a function') + ': at x = 3 both pieces give 9. ' + X('g is not') + ': at x = 2 the pieces give 4 and 6, so 2 has two images')
sm.piecewise_v(d)
b('Misc Q10: A = {1,2,3,4}, B = {1,5,9,11,15,16}, f = {(1,5), (2,9), (3,1), (4,5), (2,11)}. Relation? Function?', E('A relation from A to B: yes') + ' (all pairs lie in A × B). ' + X('Function: no') + ': 2 has two images (9 and 11)')
b('Misc Q11: f = {(ab, a + b) : a, b ∈ Z}. Function from Z to Z?', X('No') + '. ab = 0 arises from (a, b) = (0, 1) and (0, 2), giving (0, 1) and (0, 2): one input, two images')
b('Misc Q12: f(n) = highest prime factor of n, on {9, 10, 11, 12, 13}. Range?', '9 → 3, 10 → 5, 11 → 11, 12 → 3, 13 → 13: ' + N('{3, 5, 11, 13}'))

# ---------------------------------------------------------------- Even/odd, transformations (exam favourites)
d.sec('2.z-symmetry-and-shifts')
b('Even and odd functions: definition and graph symmetry?', T('Even') + ': f(−x) = f(x), symmetric about the y-axis (x², |x|). ' + T('Odd') + ': f(−x) = −f(x), symmetric about the origin (x, x³, 1/x, sgn x)')
b('Even × even, odd × odd, even × odd?', 'even × even = even; odd × odd = ' + T('even') + '; even × odd = ' + T('odd'))
b('Every function can be written as (even part) + (odd part). How?', r'\(f(x) = \dfrac{f(x) + f(-x)}{2} + \dfrac{f(x) - f(-x)}{2}\)')
sm.shift_parabola(d)
table_card(d, 'Graph transformations', 'What does each do to the graph of y = f(x)?', [
    ('f(x) + k', 'shift up k', False), ('f(x − h)', 'shift right h', False), ('−f(x)', 'reflect in x-axis', False),
    ('f(−x)', 'reflect in y-axis', False), ('|f(x)|', 'flip below-axis parts up', False), ('c f(x), c > 1', 'stretch vertically by c', False)],
    term='Graph transformations')

# ---------------------------------------------------------------- Counting functions and relations
d.sec('2.z-counting')
b('n(A) = m, n(B) = n. Number of functions from A to B?', N('nᵐ') + ': each of the m inputs independently picks one of n outputs')
b('A = {1, 2}, B = {3, 4}. Relations from A to B? How many are functions?', N('16') + ' relations; ' + N('2² = 4') + ' functions. So a function is a very special relation')
b('Number of one-one functions from A (m elements) to B (n elements)?', r'\(n(n-1)(n-2)\cdots(n-m+1)\)' + ' for m ≤ n; zero if m > n (Chapter 6)')
b('Number of relations on A with n(A) = n?', N('2^(n²)'))
b('Number of elements in A × B × C?', N('n(A) · n(B) · n(C)'))

# ---------------------------------------------------------------- How it's asked
d.sec('2.z-how-its-asked')
b('MCQ: If n(A) = 3, n(B) = 4, the number of relations from A to B is<br>(a) 12 (b) 2¹² (c) 3⁴ (d) 4³', E('(b) 2¹²') + ': subsets of the 12 pairs. (c) and (d) count functions from A to B or B to A')
b('MCQ: Domain of f(x) = √(x² − 5x + 6) is<br>(a) (2, 3) (b) [2, 3] (c) (−∞, 2] ∪ [3, ∞) (d) R', E('(c)') + ': (x − 2)(x − 3) ≥ 0 outside the roots, roots included')
b('MCQ: Range of f(x) = 3 + 2 sin x is<br>(a) [1, 5] (b) [−1, 1] (c) [3, 5] (d) [0, 5]', E('(a) [1, 5]') + ': sin x ∈ [−1, 1] → 3 ± 2')
b('MCQ: Which is not a function from R to R? (a) y = x² (b) y = |x| (c) x = y² (d) y = x³', E('(c)') + ': x = y² gives y = ±√x, two images (fails vertical line test)')
b('MCQ: [−2.5] + [2.5] = ?<br>(a) 0 (b) −1 (c) 1 (d) 5', E('(b) −1') + ': [−2.5] = −3, [2.5] = 2')
b('Integer answer (JEE Main): the number of functions from {1, 2, 3} to {a, b} is?', N('8') + ' = 2³')
b('Assertion–Reason.<br><b>A:</b> f = {(1, 2), (1, 3)} is a function.<br><b>R:</b> In a function each element of the domain has a unique image.<br>(a) Both true, R explains A (b) Both true, R does not explain A (c) A false, R true (d) Both false',
  E('(c)') + ': 1 has two images, so A is false; R is the correct definition')
b('Assertion–Reason.<br><b>A:</b> A × B = B × A for all non-empty sets A, B.<br><b>R:</b> (a, b) = (b, a).<br>(a) Both true (b) A true, R false (c) A false, R true (d) Both false', E('(d)') + ': (a, b) = (b, a) only if a = b; so the product is generally not commutative')
b('Case-based: a taxi fare is f(x) = 50 + 12x for x km (x ≥ 0). What is f(5)? What is the type of function?', 'f(5) = 50 + 60 = ' + N('₹110') + '. It is a ' + T('linear function') + ' (m = 12 per km, c = 50 fixed charge)')
b('2-mark: find the domain of f(x) = 1/(x² − 9) + √(x + 5).', 'Need x ≠ ±3 and x ≥ −5: ' + N('[−5, ∞) − {−3, 3}'))
b('3-mark: A = {1, 2, 3}, B = {4, 5}. Write the relation R = {(x, y) : x + y is odd}. Domain? Range?', 'Pairs with odd sum: (1,4), (2,5), (3,4). ' + N('R = {(1,4), (2,5), (3,4)}') + '. Domain {1, 2, 3}; range {4, 5}. It is also a function')

print('cards', len(d.cards))
os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
