import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase_math as sm

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Mathematics', 'class11-mathematics-ch01-sets')
d = Deck('Chapter 1: Sets', 'Class 11', ['class-11', 'mathematics', 'ch-1'])
d.description = 'Sets, roster and set-builder forms, subsets, intervals, Venn diagrams, union, intersection, complement and De Morgan’s laws.'
b = d.basic

# ---------------------------------------------------------------- 1.2 Sets and their representation
d.sec('1.2-sets-representation')
d.cloze('A set is a {{c1::well-defined}} collection of {{c2::objects}}.',
        extra='Well-defined: for any object we can decide definitely whether it belongs or not.')
b('Is “the ten most talented writers of India” a set?', X('No') + ': it is not ' + T('well-defined') + ': “most talented” depends on who is judging')
b('Is “the months of a year beginning with the letter J” a set?', E('Yes') + ': {January, June, July}. Membership can be decided with certainty')
b('Objects, elements and members of a set: same or different?', T('Synonymous') + '. Sets are named with capitals (A, B, X), elements with small letters (a, b, x)')
b(r'Read the symbols: \(a \in A\) and \(b \notin A\).', '“a ' + T('belongs to') + ' A” and “b ' + X('does not belong to') + ' A”')
table_card(d, '1.2 · Standard sets', 'Name the set.', [
    ('N', 'natural numbers {1, 2, 3, …}', False), ('Z', 'integers {…, −2, −1, 0, 1, 2, …}', False),
    ('Q', 'rational numbers', False), ('T', 'irrational numbers (R − Q)', False), ('R', 'real numbers', False),
    ('Z⁺, Q⁺, R⁺', 'positive integers, rationals, reals', False)], term='Symbols of standard number sets')
b('Does N include 0?', X('No') + ': in NCERT, ' + T('N = {1, 2, 3, …}') + '. Z⁺ is the same set. Whole numbers W = {0, 1, 2, …}')
b('Two methods of writing a set?', T('Roster (tabular) form') + ' and ' + T('set-builder form'))
b('Roster form: rules?', 'List elements in braces { } separated by commas. ' + T('Order does not matter') + '; ' + X('an element is not repeated'))
b('Roster form of the set of letters in “SCHOOL”?', N('{S, C, H, O, L}') + ' (the repeated O is listed once; 5 elements)')
b('In {x : x is a vowel}, what do the braces and the colon mean?', 'Braces: “the set of all”. Colon: “' + T('such that') + '”')
b('Set-builder form of the vowels V in English?', 'V = {x : x is a vowel in the English alphabet}')
b('Roster form of {x : x is a natural number and 3 < x < 10}?', N('{4, 5, 6, 7, 8, 9}'))
b('Example: roster form of the solution set of x² + x − 2 = 0?', '(x − 1)(x + 2) = 0 → ' + N('{1, −2}'))
b('Roster form of {x : x is a positive integer and x² < 40}?', N('{1, 2, 3, 4, 5, 6}') + '  (6² = 36 < 40, 7² = 49)')
b('Set-builder form of {1, 4, 9, 16, 25, …}?', T('{x : x = n², n ∈ N}') + ', or “x is the square of a natural number”')
b('Set-builder form of {1/2, 2/3, 3/4, 4/5, 5/6, 6/7}?', r'\(\left\{x : x = \dfrac{n}{n+1},\ n \in \mathbb{N},\ 1 \le n \le 6\right\}\)' +
  '<br><small>Numerator one less than denominator, n from 1 to 6</small>')
b('Roster form of {x : x is an integer and −3 ≤ x < 7}?', N('{−3, −2, −1, 0, 1, 2, 3, 4, 5, 6}') + '<br><small>−3 is included, 7 is not</small>')
b('Roster form of {x : x is a two-digit natural number with digit sum 8}?', N('{17, 26, 35, 44, 53, 62, 71, 80}') + ' (8 elements)')
b('Roster form of {x : x is a prime divisor of 60}?', 'Prime factorisation 60 = 2² · 3 · 5 → ' + N('{2, 3, 5}'))
b('Roster form of the set of letters in TRIGONOMETRY?', N('{T, R, I, G, O, N, M, E, Y}') + ' (9 distinct letters)')
b('List {x : x is an integer, −½ < x < 9/2}.', N('{0, 1, 2, 3, 4}'))
b('List {x : x is an integer, x² ≤ 4}.', N('{−2, −1, 0, 1, 2}') + '<br><small>Trap: don’t forget the negatives.</small>')
b('List {x : x is a month of a year not having 31 days}.', N('{February, April, June, September, November}') + ' (5)')
b('List {x : x is a consonant preceding k}.', N('{b, c, d, f, g, h, j}'))
b('Match: {P, R, I, N, C, A, L} in set-builder form?', '{x : x is a letter of the word PRINCIPAL}: 9 letters but P and I repeat, so 7 distinct')
b('Match: {0} ↔ ? (a) {x : x is an integer and x + 1 = 1}, (b) {x : x is a positive integer dividing 18}', E('(a)') + ': x + 1 = 1 gives x = 0. (b) is {1, 2, 3, 6, 9, 18}')
b('Which sets can never be written in roster form?', 'Sets whose elements follow no pattern, e.g. ' + T('R') + ' (the real numbers) or the set of irrational numbers')

# ---------------------------------------------------------------- 1.3 Empty set
d.sec('1.3-empty-set')
b('Define the empty set. Its symbol?', 'A set with ' + T('no element') + '. Called null or void set; written ' + N('φ') + ' or ' + N('{ }'))
b('Why is {x : 1 < x < 2, x ∈ N} empty?', 'There is no natural number between 1 and 2')
b('Why is {x : x² − 2 = 0, x rational} empty?', 'x = ±√2 is irrational: no rational solution')
b('Why is {x : x is an even prime greater than 2} empty?', '2 is the ' + T('only even prime'))
b('Why is {x : x² = 4, x odd} empty?', 'Solutions ±2 are even')
b('Is {x : x is a point common to two parallel lines} empty?', E('Yes') + ': parallel lines never meet')
b('Trap: φ, {φ} and {0}: how many elements?', X('φ') + ' has 0; ' + T('{φ}') + ' has 1 (the element is φ); ' + T('{0}') + ' has 1 (the number 0)')
b('Intuition: an empty box, and a box that contains an empty box?',
  'φ is the empty box (0 items). {φ} is a box holding an empty box (1 item). So n(φ) = 0 but n({φ}) = 1')
b('Is the empty set finite or infinite?', T('Finite') + ': it has 0 elements. n(φ) = 0')

# ---------------------------------------------------------------- 1.4 Finite and infinite
d.sec('1.4-finite-infinite')
b('Define a finite set and an infinite set.', T('Finite') + ': empty or has a definite number of elements. ' + T('Infinite') + ': otherwise')
b('What does n(S) denote?', 'The ' + T('number of distinct elements') + ' of S')
b('Is the set of days of a week finite?', E('Finite') + ': n(W) = 7')
b('Is the set of points on a line finite?', X('Infinite'))
b('Classify: {x : x ∈ N, (x − 1)(x − 2) = 0}, {x : x ∈ N, 2x − 1 = 0}.', 'First = {1, 2} → finite. Second: x = ½ ∉ N → φ → ' + T('finite') + '.<br><small>Empty sets are finite.</small>')
b('Classify: {x ∈ N : x is prime} and {x ∈ N : x is odd}.', X('Both infinite') + ' (infinitely many primes, infinitely many odd numbers)')
b('Classify: the set of lines parallel to the x-axis; the set of circles through the origin.', X('Both infinite') + ' (y = c for any c; centres can be anywhere on suitable loci)')
b('Classify: the set of multiples of 5; the set of prime numbers less than 99.', 'Multiples of 5: ' + X('infinite') + '. Primes < 99: ' + E('finite') + ' (25 of them, up to 97)')
b('Roster form of an infinite set: how?', 'Write a few elements showing the pattern followed by three dots, e.g. {1, 3, 5, 7, …}')

# ---------------------------------------------------------------- 1.5 Equal sets
d.sec('1.5-equal-sets')
b('Define equal sets.', 'A = B if they have ' + T('exactly the same elements') + ' (every element of A is in B and every element of B is in A)')
b('Are {1, 2, 3, 4} and {3, 1, 4, 2} equal?', E('Yes') + ': order does not matter')
b('Are {1, 2, 3} and {2, 2, 1, 3, 3} equal?', E('Yes') + ': repetition does not change a set')
b('Are the letter sets of ALLOY and LOYAL equal?', E('Yes') + ': both are {A, L, O, Y}')
b('A = {x ∈ Z : x² ≤ 4}, B = {x ∈ R : x² − 3x + 2 = 0}: equal?', X('No') + ': A = {−2, −1, 0, 1, 2}, B = {1, 2}; 0 ∈ A but 0 ∉ B')
b('Prime numbers less than 6 and prime factors of 30: equal?', E('Yes') + ': both are {2, 3, 5}')
b('Trap: is {0} = φ?', X('No') + ': {0} has one element (0); φ has none')
b('From Ex 1.2: B = {1, 2, 3, 4} and D = {3, 1, 4, 2}; E = {−1, 1} and G = {1, −1}. Which are equal?', 'B = D and E = G')
b('Two sets: A = {x : x is a multiple of 10} and B = {10, 15, 20, 25, …}. Equal?', X('No') + ': 15 ∈ B but 15 is not a multiple of 10')

# ---------------------------------------------------------------- 1.6 Subsets
d.sec('1.6-subsets')
b('Define a subset.', 'A ⊂ B if ' + T('every element of A is also in B') + ': a ∈ A ⇒ a ∈ B')
b('Read: A ⊂ B, A ⊄ B, ⇒, ⇔.', 'A is a subset of B; A is not a subset of B; implies; ' + T('if and only if') + ' (iff)')
b('Every set is a subset of itself. True?', E('True') + ': A ⊂ A')
b('Is the empty set a subset of every set?', E('Yes') + ': φ ⊂ A for every A (agreed by definition)')
b('Intuition: why is φ a subset of every set?',
  'To fail, φ would need an element that is not in A. φ has ' + T('no elements') + ', so nothing can fail: the condition holds ' + T('vacuously'))
b('A ⊂ B and B ⊂ A implies?', T('A = B') + '. This is how equality is proved in set problems: show both inclusions')
b('Proper subset and superset?', 'A ⊂ B and A ≠ B: A is a ' + T('proper subset') + ' of B, and B is a ' + T('superset') + ' of A')
b('What is a singleton set?', 'A set with exactly one element, like {a}')
b('Notation note: ⊂ or ⊆?', 'NCERT writes ' + T('⊂') + ' for “subset (may be equal)”. Many books and JEE papers use ⊆ for that and reserve ⊂ for ' + T('proper') + ' subset; read the context')
b('Relations among N, Z, Q, R, T?', r'\(\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}\)' + ',  T ⊂ R,  ' + X('N ⊄ T'))
b('Define Q (rational numbers) in set-builder form.', r'\(\mathbb{Q} = \left\{x : x = \dfrac{p}{q},\ p, q \in \mathbb{Z},\ q \neq 0\right\}\)')
b('Define the set T of irrational numbers.', r'\(T = \{x : x \in \mathbb{R},\ x \notin \mathbb{Q}\} = \mathbb{R} - \mathbb{Q}\)' + '; e.g. √2, √5, π')
b('Trap: A ∈ B and B ⊂ C. Does A ⊂ C follow?', X('No') + '. A = {1}, B = {{1}, 2}, C = {{1}, 2, 3}: A ∈ B ⊂ C, but 1 ∈ A and 1 ∉ C')
table_card(d, '1.6 · ∈ versus ⊂', 'A = {1, 2, {3, 4}, 5}. True or false?', [
    ('{3, 4} ∈ A', 'True: {3, 4} is an element', False), ('{3, 4} ⊂ A', 'False: 3 ∉ A', True),
    ('{{3, 4}} ⊂ A', 'True: its only element {3,4} is in A', False), ('1 ⊂ A', 'False: 1 is an element, not a set', True),
    ('{1, 2, 5} ⊂ A', 'True', False), ('{1, 2, 5} ∈ A', 'False: not an element', True),
    ('φ ∈ A', 'False: φ is not listed', True), ('φ ⊂ A', 'True', False), ('{φ} ⊂ A', 'False: φ ∉ A', True)],
    note='Elements go with ∈. Sets go with ⊂. A set in braces inside A counts as one element.', term='Ex 1.3 Q3: ∈ versus ⊂')
b('Trap: {a} ∈ {a, b, c} is true or false?', X('False') + ': the elements are a, b, c. Correct: ' + T('{a} ⊂ {a, b, c}') + ' or ' + T('a ∈ {a, b, c}'))
b('Is {a, b} ⊄ {b, c, a} true?', X('False') + ': every element of {a, b} lies in {b, c, a}, so {a, b} ⊂ {b, c, a}')
b('List all subsets of {a, b}.', 'φ, {a}, {b}, {a, b}: ' + N('4') + ' subsets')
b('List all subsets of {1, 2, 3}.', 'φ; {1}, {2}, {3}; {1, 2}, {1, 3}, {2, 3}; {1, 2, 3}: ' + N('8') + ' subsets')
b('List all subsets of φ.', 'Only ' + T('φ itself') + ': 2⁰ = 1 subset')
b('List all subsets of {−1, 0, 1} by size.', 'Size 0: φ. Size 1: {−1}, {0}, {1}. Size 2: {−1,0}, {−1,1}, {0,1}. Size 3: {−1,0,1}. Total 8')

d.sec('1.6-power-set')
sm.subsets_doubling(d)
b('Number of subsets, proper subsets and non-empty proper subsets of a set with n elements?', r'\(2^n,\quad 2^n - 1,\quad 2^n - 2\)')
b('Power set: definition and size?', 'P(A) = the set of ' + T('all subsets') + ' of A; ' + N('n(P(A)) = 2ⁿ'))
b('Trap: what is P(φ), and how many elements has P(P(φ))?', 'P(φ) = {φ} (1 element). P({φ}) = {φ, {φ}} → ' + N('2 elements') + '. A classic exam trap')

# ---------------------------------------------------------------- 1.6.2 Intervals
d.sec('1.6.2-intervals')
table_card(d, '1.6.2 · Intervals', 'Set-builder form of each interval.', [
    ('(a, b)', '{x : a < x < b}  open', False), ('[a, b]', '{x : a ≤ x ≤ b}  closed', False),
    ('[a, b)', '{x : a ≤ x < b}', False), ('(a, b]', '{x : a < x ≤ b}', False)],
    note='Square bracket includes the endpoint; round bracket excludes it.', term='Types of intervals')
b('Length of the interval (a, b), [a, b], [a, b) or (a, b]?', N('b − a') + ' for every type')
b('Draw: how are open and closed endpoints marked on the number line?', T('Open circle ○') + ' = excluded (round bracket); ' + T('filled dot ●') + ' = included (square bracket)')
sm.interval_cards(d)
b('Why must ∞ always have a round bracket?', '∞ is ' + X('not a number') + ', so it can never be an endpoint that belongs to the set: (−∞, 3], [2, ∞)')
b('Interval for the non-negative reals? For the negative reals?', T('[0, ∞)') + ' and ' + T('(−∞, 0)'))
b('Write {x ∈ R : −5 < x ≤ 7} as an interval.', N('(−5, 7]'))
b('Write [−3, 5) in set-builder form.', T('{x : −3 ≤ x < 5}'))
table_card(d, 'Exercise 1.3 · Interval ↔ set-builder', 'Convert.', [
    ('−4 < x ≤ 6', '(−4, 6]', False), ('−12 < x < −10', '(−12, −10)', False),
    ('0 ≤ x < 7', '[0, 7)', False), ('3 ≤ x ≤ 4', '[3, 4]', False),
    ('[−23, 5)', '−23 ≤ x < 5', False), ('(6, 12]', '6 < x ≤ 12', False)], term='Interval conversions')
b('Is (−3, 5) ⊂ [−7, 9]?', E('Yes') + ': every real between −3 and 5 lies in [−7, 9]')
b('How many points does an interval contain?', X('Infinitely many') + ', however short it is')
sm.interval_ops_cards(d)
b('Trap: is (1, 3) ∪ (3, 5) equal to (1, 5)?', X('No') + ': 3 is in neither open interval, so it is missing. The union is (1, 5) − {3}')
b('Find [−3, 2) ∩ (0, 6].', r'\((0, 2)\)' + '<br><small>0 is not in (0, 6]; 2 is not in [−3, 2)</small>')
b('Find (−∞, 4) ∪ [4, ∞).', N('R') + ': the point 4 is covered by the second interval')
b('Find (−∞, 2] ∩ [2, ∞).', N('{2}') + ': a single point')

# ---------------------------------------------------------------- 1.7 Universal set
d.sec('1.7-universal-set')
b('What is a universal set?', 'The ' + T('basic set') + ' in a given context of which all sets under discussion are subsets. Denoted ' + N('U'))
b('Suggest a universal set for right triangles and for isosceles triangles.', 'The set of ' + T('all triangles') + ' in a plane (both are subsets of it)')
b('Is the universal set unique?', X('No') + ': for integers, U can be Q or R. Any set that contains all the sets in the problem will do')
b('A = {1, 3, 5}, B = {2, 4, 6}, C = {0, 2, 4, 6, 8}. Which is a valid universal set: (i) {0..6}, (iii) {0..10}, (iv) {1..8}?',
  E('Only (iii) {0, 1, …, 10}') + '. It must contain 0 (from C) and 8 (from C), and 1, 3, 5, 2, 4, 6: (i) lacks 8, (iv) lacks 0')

# ---------------------------------------------------------------- 1.8 Venn diagrams
d.sec('1.8-venn-diagrams')
b('How does a Venn diagram show sets?', T('Rectangle') + ' = universal set; ' + T('circles') + ' inside it = subsets. Named after John Venn (1834–1883)')
b('In a Venn diagram, how is B ⊂ A drawn?', 'Circle B lies ' + T('completely inside') + ' circle A')
b('How are disjoint sets drawn?', 'Two circles that ' + T('do not overlap'))
sm.venn_cards(d)

# ---------------------------------------------------------------- 1.9 Operations
d.sec('1.9.1-union')
b('Define A ∪ B.', T('A ∪ B = {x : x ∈ A or x ∈ B}') + '; common elements are written once')
b('A = {2, 4, 6, 8}, B = {6, 8, 10, 12}. A ∪ B?', N('{2, 4, 6, 8, 10, 12}'))
b('Interpret X ∪ Y, X = hockey team, Y = football team of Class XI.', 'Students in the hockey team ' + T('or') + ' the football team ' + T('or both'))
b('Mnemonic for ∪ and ∩?', T('∪') + ' looks like a “U” for ' + T('Union') + ' and means ' + T('or') + '. ' + T('∩') + ' means ' + T('and') + ' (∧ without the bar)')
b('If B ⊂ A, then A ∪ B = ?', N('A'))
table_card(d, '1.9.1 · Properties of union', 'Name the law.', [
    ('A ∪ B = B ∪ A', 'Commutative', False), ('(A ∪ B) ∪ C = A ∪ (B ∪ C)', 'Associative', False),
    ('A ∪ φ = A', 'Identity (φ is the identity of ∪)', False), ('A ∪ A = A', 'Idempotent', False),
    ('A ∪ U = U', 'Law of U', False)], term='Laws of union')
d.sec('1.9.2-intersection')
b('Define A ∩ B.', T('A ∩ B = {x : x ∈ A and x ∈ B}') + ': elements common to both')
b('A = {2, 4, 6, 8}, B = {6, 8, 10, 12}. A ∩ B?', N('{6, 8}'))
b('X = {Ram, Geeta, Akbar}, Y = {Geeta, David, Ashok}. X ∩ Y?', N('{Geeta}'))
b('If B ⊂ A, then A ∩ B = ?', N('B'))
b('When are A and B disjoint?', 'When ' + T('A ∩ B = φ') + ' (no common element)')
table_card(d, '1.9.2 · Properties of intersection', 'Name the law.', [
    ('A ∩ B = B ∩ A', 'Commutative', False), ('(A ∩ B) ∩ C = A ∩ (B ∩ C)', 'Associative', False),
    ('φ ∩ A = φ,  U ∩ A = A', 'Laws of φ and U', False), ('A ∩ A = A', 'Idempotent', False),
    ('A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)', 'Distributive: ∩ over ∪', False)], term='Laws of intersection')
b('Second distributive law: A ∪ (B ∩ C) = ?', T('(A ∪ B) ∩ (A ∪ C)') + '. Unlike numbers, each of ∪ and ∩ distributes over the other')
b('Distributive laws: an everyday picture.', 'Multiplication distributes over addition only one way. Sets are more symmetric: ' + T('“or” spreads over “and”, and “and” spreads over “or”'))
d.sec('1.9.3-difference')
b('Define A − B.', T('A − B = {x : x ∈ A and x ∉ B}') + ': in A but not in B. Also A ∩ B′')
b('A = {1, 2, 3, 4, 5, 6}, B = {2, 4, 6, 8}. A − B and B − A?', N('{1, 3, 5}') + ' and ' + N('{8}'))
b('V = {a, e, i, o, u}, B = {a, i, k, u}. V − B and B − V?', N('{e, o}') + ' and ' + N('{k}'))
b('Is A − B = B − A?', X('Not in general') + '. They are disjoint, and equal only when both are φ (i.e. A = B)')
b('A − B, A ∩ B and B − A: how are they related?', 'They are ' + T('mutually disjoint') + ' and together make A ∪ B')
b('Ex 1.4: A = {3, 6, 9, 12, 15, 18, 21}, B = {4, 8, 12, 16, 20}. A − B and B − A?', N('{3, 6, 9, 15, 18, 21}') + ' and ' + N('{4, 8, 16, 20}') + '<br><small>Only 12 is common</small>')
b('What is R − Q?', T('T') + ', the set of irrational numbers')
b('Which pairs are disjoint? (a) evens and odds in Z, (b) {a,e,i,o,u} and {c,d,e,f}, (c) {1,2,3,4} and {x∈N : 4 ≤ x ≤ 6}', E('(a) disjoint') + '; ' + X('(b) not: e is common') + '; ' + X('(c) not: 4 is common'))
b('A ⊂ B and A ≠ B. What is A − B?', N('φ') + ', because every element of A is already in B')

steps_card(d, 'Ex 1.4 Q6 · Combining operations', 'Find (A ∪ D) ∩ (B ∪ C).',
           'A = {3, 5, 7, 9, 11}, B = {7, 9, 11, 13}, C = {11, 13, 15}, D = {15, 17}',
           ['Brackets first: A ∪ D = {3, 5, 7, 9, 11, 15, 17}', 'B ∪ C = {7, 9, 11, 13, 15}',
            'Keep only elements in both lists: <b>{7, 9, 11, 15}</b>'], hide=2,
           term='(A ∪ D) ∩ (B ∪ C) worked example', definition='{7, 9, 11, 15}')
b('Same sets: A ∩ (B ∪ C) and A ∩ C ∩ D?', N('{7, 9, 11}') + ' and ' + N('φ') + '<br><small>A ∩ C = {11}, and 11 ∉ D</small>')
b('Ex 1.4 Q7: N ∩ (evens), (evens) ∩ (odds), (evens) ∩ (primes), (odds) ∩ (primes)?', 'Evens; ' + N('φ') + '; ' + N('{2}') + '; ' + N('odd primes {3, 5, 7, …}'))

# ---------------------------------------------------------------- 1.10 Complement
d.sec('1.10-complement')
b('Define the complement A′.', T('A′ = {x : x ∈ U and x ∉ A} = U − A'))
b('U = {1, …, 10}, A = {1, 3, 5, 7, 9}. A′?', N('{2, 4, 6, 8, 10}'))
b('U = the girls and boys of Class XI, A = the girls. A′?', 'The ' + E('boys'))
b('(A′)′ = ?', N('A') + ': law of double complementation')
table_card(d, '1.10 · Complement laws', 'Fill in.', [
    ('A ∪ A′', 'U', False), ('A ∩ A′', 'φ', False), ('φ′', 'U', False), ('U′', 'φ', False), ('(A′)′', 'A', False)],
    term='Complement laws')
b('State De Morgan’s laws.', T('(A ∪ B)′ = A′ ∩ B′') + ' and ' + T('(A ∩ B)′ = A′ ∪ B′') +
  '<br><small>The complement of a union is the intersection of complements, and vice versa</small>')
b('Mnemonic for De Morgan’s laws?', T('Break the bar, change the sign') + ': break the bar over the bracket and swap ∪ ↔ ∩ (and complement each piece)')
sm.de_morgan_cards(d)
b('Verify with U = {1, …, 6}, A = {2, 3}, B = {3, 4, 5}: (A ∪ B)′ = ?', 'A′ = {1, 4, 5, 6}, B′ = {1, 2, 6}, so A′ ∩ B′ = {1, 6}; and A ∪ B = {2, 3, 4, 5} → (A ∪ B)′ = ' + N('{1, 6}'))
b('U = {1, …, 9}, A = {1, 2, 3, 4}, B = {2, 4, 6, 8}, C = {3, 4, 5, 6}. Find (A ∪ C)′, (A ∪ B)′, (B − C)′.',
  '(A ∪ C)′ = ' + N('{7, 8, 9}') + '; (A ∪ B)′ = ' + N('{5, 7, 9}') + '; B − C = {2, 8}, so (B − C)′ = ' + N('{1, 3, 4, 5, 6, 7, 9}'))
b('With U = N, complement of the even naturals? Of the multiples of 3?', 'The ' + T('odd') + ' naturals; the naturals ' + T('not divisible by 3'))
b('With U = N, complement of the primes?', N('{1} ∪ composite numbers') + ': remember that 1 is neither prime nor composite')
b('With U = N, complement of {x : 2x + 5 = 9} and of {x : x ≥ 7}?', 'Set = {2} → complement N − {2}. Second: ' + N('{1, 2, 3, 4, 5, 6}'))
b('U = all triangles in a plane, A = triangles with at least one angle ≠ 60°. A′?', 'Triangles with ' + T('all angles equal to 60°') + ' → equilateral triangles')
table_card(d, 'Ex 1.5 Q7 · Fill in the blanks', 'Simplify.', [
    ('A ∪ A′', 'U', False), ('φ′ ∩ A', 'U ∩ A = A', False), ('A ∩ A′', 'φ', False), ('U′ ∩ A', 'φ ∩ A = φ', False)],
    term='Complement blanks')

# ---------------------------------------------------------------- Proof patterns
d.sec('1.x-proof-patterns')
b('Method: how do you prove two sets are equal?', T('Element chase') + ': take x ∈ A and show x ∈ B (so A ⊂ B); then take x ∈ B and show x ∈ A. Conclude A = B')
b('Example 25: A ∪ B = A ∩ B ⇒ A = B. The trick?', 'Any a ∈ A lies in A ∪ B = A ∩ B, so a ∈ B; likewise any b ∈ B lies in A. Hence ' + T('A ⊂ B and B ⊂ A'))
b('Misc Q4: four equivalent conditions for A ⊂ B?', T('A − B = φ') + ',  ' + T('A ∪ B = B') + ',  ' + T('A ∩ B = A') + ',  and ' + T('B′ ⊂ A′'))
b('Misc Q3: A ∪ B = A ∪ C and A ∩ B = A ∩ C ⇒ B = C. Idea?', 'Write B = B ∩ (A ∪ B) = B ∩ (A ∪ C) = (B ∩ A) ∪ (B ∩ C) = (A ∩ C) ∪ (B ∩ C) = C ∩ (A ∪ B) = C ∩ (A ∪ C) = C')
b('Misc Q6: A = (A ∩ B) ∪ (A − B). Why?', 'Split A into the part inside B and the part outside B. Also A ∪ (B − A) = A ∪ B')
b('Absorption laws?', T('A ∪ (A ∩ B) = A') + ' and ' + T('A ∩ (A ∪ B) = A'))
b('Trap (Misc Q8): does A ∩ B = A ∩ C imply B = C?', X('No') + '. Counter-example: A = φ, B = {1}, C = {2}: A ∩ B = A ∩ C = φ but B ≠ C')
b('Trap: if x ∈ A and A ∈ B, is x ∈ B?', X('No') + '. x = 1, A = {1}, B = {{1}}: 1 ∈ A, A ∈ B, but 1 ∉ B. Membership is not transitive; ' + T('⊂ is'))
b('Misc Q10: three sets with non-empty pairwise intersections but A ∩ B ∩ C = φ?', 'A = {1, 2}, B = {2, 3}, C = {1, 3}. Pairwise: {2}, {3}, {1}; all three: φ')
b('Misc Q1: A = {x ∈ R : x² − 8x + 12 = 0}, B = {2, 4, 6}, C = {2, 4, 6, 8, …}, D = {6}. Subset relations?',
  'A = {2, 6}. So ' + T('A ⊂ B ⊂ C') + ', ' + T('D ⊂ A') + ', D ⊂ B, D ⊂ C (and A ⊂ C)')

# ---------------------------------------------------------------- Counting (beyond NCERT text, exam essentials)
d.sec('1.z-counting')
b(r'Formula for \(n(A \cup B)\)?', r'\(n(A \cup B) = n(A) + n(B) - n(A \cap B)\)' + '<br><small>Subtract the overlap, which was counted twice</small>')
b('If A and B are disjoint, n(A ∪ B) = ?', N('n(A) + n(B)'))
b('n(A − B) and n(A′)?', r'\(n(A - B) = n(A) - n(A \cap B)\)' + ',  ' + r"\(n(A') = n(U) - n(A)\)")
b('n(elements in exactly one of A, B)?', r'\(n(A) + n(B) - 2\,n(A \cap B)\)' + ' = n(A Δ B)')
sm.inclusion_exclusion3(d)
b('Given n(A) = p and n(B) = q: bounds on n(A ∩ B) and n(A ∪ B)?', r'\(0 \le n(A \cap B) \le \min(p, q)\)' + ',  ' + r'\(\max(p, q) \le n(A \cup B) \le p + q\)')
steps_card(d, 'Survey problem', 'In a class of 100, 60 like tea, 45 like coffee, 25 like both. How many like neither?',
           'n(U) = 100, n(T) = 60, n(C) = 45, n(T ∩ C) = 25',
           ['n(T ∪ C) = 60 + 45 − 25 = 80', 'Neither = outside the union: n(U) − n(T ∪ C) = 100 − 80 = <b>20</b>',
            'Only tea = 60 − 25 = 35; only coffee = 45 − 25 = 20'], hide=1,
           term='Survey problem: neither tea nor coffee', definition='n(T∪C) = 80, so neither = 20 (only tea 35, only coffee 20)')
b('In the same survey, how many like exactly one drink?', N('55') + ': (60 − 25) + (45 − 25) = 35 + 20')
b('Method: a survey problem with 2 or 3 groups?', 'Start from the ' + T('innermost overlap') + ', work outwards by subtraction, fill each Venn region, and check that the regions add up to n(U)')
b('JEE style: number of subsets of {1, 2, …, 10} that contain 1 and 2 but not 3?', 'Fix three elements; the other 7 are free: ' + N('2⁷ = 128'))
b('Number of subsets of a set with n elements that contain a given element?', N('2ⁿ⁻¹') + ': that element is fixed “in”, the rest are free')
b(r'Number of subsets of \(\{1, 2, \ldots, n\}\) with exactly \(k\) elements?', r'\(\binom{n}{k}\)' + ' (Chapter 6)')
b('If A ⊂ B, then n(A) ≤ n(B). Converse true?', X('No') + '. {1, 2} and {3, 4, 5}: 2 ≤ 3, but {1, 2} ⊄ {3, 4, 5}')

# ---------------------------------------------------------------- Identities used in problems
d.sec('1.z-identities')
b('A − B in terms of complement and intersection?', T('A − B = A ∩ B′'))
b('De Morgan for differences: A − (B ∪ C) and A − (B ∩ C)?', T('A − (B ∪ C) = (A − B) ∩ (A − C)') + ';  ' + T('A − (B ∩ C) = (A − B) ∪ (A − C)'))
b('A Δ B (symmetric difference): three equivalent forms?', T('(A − B) ∪ (B − A)') + ' = ' + T('(A ∪ B) − (A ∩ B)') + ' = ' + T('(A ∩ B′) ∪ (A′ ∩ B)'))
b('A ⊂ B ⇒ what about B′ and A′?', T('B′ ⊂ A′') + ': the order reverses under complement')
b('A ∪ B = U and A ∩ B = φ. What is B in terms of A?', T('B = A′') + ': B is the complement of A')
b('Simplify A ∩ (A′ ∪ B).', 'Distribute: (A ∩ A′) ∪ (A ∩ B) = φ ∪ (A ∩ B) = ' + N('A ∩ B'))
b('Simplify (A ∪ B) ∩ (A ∪ B′).', 'A ∪ (B ∩ B′) = A ∪ φ = ' + N('A'))

# ---------------------------------------------------------------- How it's asked
d.sec('1.z-how-its-asked')
b('MCQ (JEE/board): A = {x : x is a multiple of 3}, B = {x : x is a multiple of 5}. Then A ∩ B is<br>(a) multiples of 8 (b) multiples of 15 (c) multiples of 2 (d) φ',
  E('(b)') + ': divisible by both 3 and 5 ⇒ divisible by lcm = 15')
b('MCQ: n(P(A)) = 64. n(A) = ?<br>(a) 5 (b) 6 (c) 8 (d) 32', E('(b) 6') + ': 2ⁿ = 64 = 2⁶')
b('MCQ: The number of proper subsets of {1, 2, 3, 4} is<br>(a) 16 (b) 15 (c) 14 (d) 8', E('(b) 15') + ': 2⁴ − 1. Exclude only the set itself')
b('Integer answer (JEE Main): A = {x ∈ Z : x² ≤ 9}. Find the number of subsets of A with exactly 2 elements.',
  'A = {−3, …, 3} has 7 elements; ' + r'\(\binom{7}{2} = 21\)')
b('Assertion–Reason (board).<br><b>A:</b> φ ⊂ {1, 2}.<br><b>R:</b> The empty set is a subset of every set.<br>(a) Both true, R explains A (b) Both true, R does not explain A (c) A true, R false (d) A false, R true',
  E('(a)') + ': R is the reason φ ⊂ {1, 2}')
b('Assertion–Reason.<br><b>A:</b> {1} ∈ {1, 2, 3}.<br><b>R:</b> {1} ⊂ {1, 2, 3}.<br>(a) Both true, R explains A (b) Both true, R does not explain A (c) A false, R true (d) Both false',
  E('(c)') + ': the elements of {1, 2, 3} are 1, 2, 3, so {1} ∈ … is false; but {1} ⊂ … is true')
b('True/False (2 marks): if A ⊂ B, then A ∪ B = A ∩ B.', X('False') + ': A ∪ B = B and A ∩ B = A. They are equal only if A = B')
b('Case-based: in a school, 40 students take Maths, 30 take Physics, 12 take both. How many take only Maths? Maths or Physics?',
  'Only Maths = 40 − 12 = ' + N('28') + '; Maths or Physics = 40 + 30 − 12 = ' + N('58'))
b('MCQ: Set of real solutions of x² + 1 = 0 is<br>(a) {i} (b) {−i, i} (c) {0} (d) φ', E('(d) φ') + ': no real x; i is not a real number')
b('MCQ: Which is a set: (a) good students of a class (b) all vowels of English (c) tall boys (d) beautiful girls', E('(b)') + ': the others are not well-defined')

print('cards', len(d.cards))
os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
