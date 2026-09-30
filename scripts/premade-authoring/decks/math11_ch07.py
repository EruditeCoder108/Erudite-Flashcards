import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase_math as sm

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Mathematics', 'class11-mathematics-ch07-binomial-theorem')
d = Deck('Chapter 7: Binomial Theorem', 'Class 11', ['class-11', 'mathematics', 'ch-7'])
d.description = 'Pascal’s triangle, binomial theorem, special cases, general and middle terms, coefficients, approximations, divisibility and remainders.'
b = d.basic

# ---------------------------------------------------------------- 7.2 Pattern of expansions
d.sec('7.2-patterns')
b('Expand (a + b)², (a + b)³, (a + b)⁴.', 'a² + 2ab + b²;  a³ + 3a²b + 3ab² + b³;  a⁴ + 4a³b + 6a²b² + 4ab³ + b⁴')
b('Three patterns seen in the expansion of (a + b)ⁿ?', '(i) ' + T('n + 1 terms') + '. (ii) Powers of a ' + T('decrease') + ' by 1 while powers of b ' + T('increase') + ' by 1. (iii) In every term the powers of a and b ' + T('add to n'))
b('What is Pascal’s triangle? Its rule?', 'Rows of coefficients of (a + b)ⁿ.<br>1 at both ends; every other entry is the ' + T('sum of the two above it') + '<br>Called Meru Prastara by Pingala')
b('Write the Pascal row for n = 5 and n = 6.', N('1 5 10 10 5 1') + ' and ' + N('1 6 15 20 15 6 1'))
b('Pascal’s triangle in terms of ⁿCᵣ?', 'Row n is ⁿC₀, ⁿC₁, …, ⁿCₙ. So the row for any n can be written down without the earlier rows')
b('Expand (2x + 3y)⁵ using the Pascal row 1 5 10 10 5 1.', '32x⁵ + 240x⁴y + 720x³y² + 1080x²y³ + 810xy⁴ + 243y⁵<br><small>Each term: coefficient × (2x)^(5−k) × (3y)^k</small>')
table_card(d, '7.2 · (2x + 3y)⁵ term by term', 'Evaluate each term.', [
    ('T₁ = (2x)⁵', '32x⁵', False), ('T₂ = 5(2x)⁴(3y)', '240x⁴y', False), ('T₃ = 10(2x)³(3y)²', '720x³y²', False),
    ('T₄ = 10(2x)²(3y)³', '1080x²y³', False), ('T₅ = 5(2x)(3y)⁴', '810xy⁴', False), ('T₆ = (3y)⁵', '243y⁵', False)], term='(2x+3y)^5 expanded')
sm.expansion_choices(d)

# ---------------------------------------------------------------- 7.2.1 Binomial theorem
d.sec('7.2.1-binomial-theorem')
b('State the binomial theorem for a positive integer n.', r'\((a+b)^n = {}^nC_0\,a^n + {}^nC_1\,a^{n-1}b + {}^nC_2\,a^{n-2}b^2 + \cdots + {}^nC_n\,b^n = \sum_{k=0}^{n}{}^nC_k\,a^{n-k}b^k\)')
b('Binomial coefficients: what are they?', 'The numbers ' + T('ⁿC₀, ⁿC₁, …, ⁿCₙ') + ' that appear in the expansion. There are ' + N('n + 1') + ' of them (and n + 1 terms)')
steps_card(d, '7.2.1 · Proof by induction', 'Prove the binomial theorem: what is the key step?', 'P(n): (a + b)ⁿ = Σ ⁿCᵣ aⁿ⁻ʳ bʳ',
           ['Base: P(1): (a + b)¹ = ¹C₀a + ¹C₁b = a + b ✓', 'Assume P(k) is true for some k.', 'Multiply by (a + b): (a + b)ᵏ⁺¹ = (a + b) · Σ ᵏCᵣ aᵏ⁻ʳ bʳ',
            'Collect like terms: the coefficient of aᵏ⁺¹⁻ʳ bʳ is ᵏCᵣ + ᵏCᵣ₋₁', 'Pascal’s rule: ᵏCᵣ + ᵏCᵣ₋₁ = ᵏ⁺¹Cᵣ, so the pattern continues for k + 1',
            'So P(k) ⇒ P(k + 1); by induction P(n) holds for all n'], hide=4,
           term='Induction proof of the binomial theorem', definition='The key step is Pascal’s rule kCr + kC(r−1) = (k+1)Cr applied to the coefficients after multiplying by (a+b)')
b('Special case: expansion of (x − y)ⁿ?', r'\((x-y)^n = {}^nC_0x^n - {}^nC_1x^{n-1}y + {}^nC_2x^{n-2}y^2 - \cdots + (-1)^n\,{}^nC_ny^n\)' + ': signs alternate')
b('Special case: (1 + x)ⁿ?', r'\((1+x)^n = {}^nC_0 + {}^nC_1x + {}^nC_2x^2 + \cdots + {}^nC_nx^n\)')
b('Put x = 1 in (1 + x)ⁿ. What do you get?', r'\(2^n = {}^nC_0 + {}^nC_1 + \cdots + {}^nC_n\)' + ': the number of subsets of an n-element set')
b('Put x = 1 in (1 − x)ⁿ. What do you get?', r'\(0 = {}^nC_0 - {}^nC_1 + {}^nC_2 - \cdots + (-1)^n\,{}^nC_n\)' + ' (n ≥ 1): the alternating sum is 0')
b('Example 1: expand (x² + 3/x)⁴, x ≠ 0.', 'x⁸ + 4x⁶·(3/x) + 6x⁴·(9/x²) + 4x²·(27/x³) + 81/x⁴ = ' + N('x⁸ + 12x⁵ + 54x² + 108/x + 81/x⁴'))
b('Ex 7.1 Q1: expand (1 − 2x)⁵.', N('1 − 10x + 40x² − 80x³ + 80x⁴ − 32x⁵'))
b('Ex 7.1 Q2: expand (2/x − x/2)⁵.', N('32/x⁵ − 40/x³ + 20/x − 5x + (5/8)x³ − x⁵/32') + '<br><small>Tₖ₊₁ = ⁵Cₖ 2⁵⁻²ᵏ (−1)ᵏ x²ᵏ⁻⁵</small>')
b('Ex 7.1 Q3: expand (2x − 3)⁶.', N('64x⁶ − 576x⁵ + 2160x⁴ − 4320x³ + 4860x² − 2916x + 729'))
b('Ex 7.1 Q4: expand (x/3 + 1/x)⁵.', N('x⁵/243 + 5x³/81 + 10x/27 + 10/(9x) + 5/(3x³) + 1/x⁵'))
b('Ex 7.1 Q5: expand (x + 1/x)⁶.', N('x⁶ + 6x⁴ + 15x² + 20 + 15/x² + 6/x⁴ + 1/x⁶'))
b('Method: expanding a binomial with fractions or negative terms.', '1) Write it as (a + b)ⁿ with a and b ' + T('including their signs and coefficients') + ' (e.g. b = −2x).<br>2) Expand.<br>3) Simplify each term’s coefficient and power separately')
b('Misc Q5: expand (1 + x/2 − 2/x)⁴, x ≠ 0.', 'Group as ((1 + x/2) − 2/x)⁴ and expand twice: ' + N('x⁴/16 + x³/2 + x²/2 − 4x − 5 + 16/x + 8/x² − 32/x³ + 16/x⁴'))
b('Misc Q6: expand (3x² − 2ax + 3a²)³.', N('27x⁶ − 54ax⁵ + 117a²x⁴ − 116a³x³ + 117a⁴x² − 54a⁵x + 27a⁶'))

# ---------------------------------------------------------------- Evaluation, comparison, divisibility
d.sec('7.2-applications')
b('Method: evaluate (98)⁵ or (101)⁴ by hand.', 'Split into ' + T('(round number ± small number)') + ' like 100 − 2 and use the binomial theorem.<br>The small powers make each term easy')
b('Example 2: compute (98)⁵.', '(100 − 2)⁵ = 10¹⁰ − 5·10⁸·2 + 10·10⁶·4 − 10·10⁴·8 + 5·100·16 − 32 = ' + N('9039207968'))
b('Ex 7.1 Q6–9: (96)³, (102)⁵, (101)⁴, (99)⁵.', N('884736') + ',  ' + N('11040808032') + ',  ' + N('104060401') + ',  ' + N('9509900499'))
b('Example 3 / Ex 10: which is larger, (1.01)¹⁰⁰⁰⁰⁰⁰ or 10,000? (1.1)¹⁰⁰⁰⁰ or 1000?', 'Write (1 + 0.01)ⁿ = 1 + n(0.01) + (positive terms) > 1 + 10000. So ' + N('(1.01)¹⁰⁰⁰⁰⁰⁰ > 10,000') + '. Similarly (1.1)¹⁰⁰⁰⁰ > 1 + 1000 > 1000')
b('Method: comparing a large power with a number.', 'Split the base as 1 + small, keep the first two terms 1 + n·(small) (all others are positive), and compare')
b('Example 4: prove 6ⁿ − 5ⁿ always leaves remainder 1 when divided by 25.', '(1 + 5)ⁿ = 1 + 5n + 25·(ⁿC₂ + 5ⁿC₃ + …) so 6ⁿ − 5ⁿ = ' + N('25k + 1'))
b('Method: proving divisibility with the binomial theorem.', 'Write the base as (multiple of d) + 1 (or − 1), e.g. 9 = 1 + 8, 6 = 1 + 5. Expand: all terms from the third onwards contain a factor d², and the first two terms cancel against the rest of the expression')
b('Ex 7.1 Q13: show 9ⁿ⁺¹ − 8n − 9 is divisible by 64.', '9ⁿ⁺¹ = (1 + 8)ⁿ⁺¹ = 1 + 8(n + 1) + 64(…) so 9ⁿ⁺¹ − 8n − 9 = ' + N('64 × (positive integer)'))
b('Ex 7.1 Q14: prove Σ 3ʳ · ⁿCᵣ = 4ⁿ (r = 0 to n).', 'This is (1 + 3)ⁿ expanded with x = 3: (1 + x)ⁿ = Σ ⁿCᵣ xʳ → ' + N('4ⁿ'))
b('Ex 7.1 Q11: find (a + b)⁴ − (a − b)⁴; hence evaluate (√3 + √2)⁴ − (√3 − √2)⁴.', 'Odd-power terms double: 2(4a³b + 4ab³) = 8ab(a² + b²). With a = √3, b = √2: 8√6 · 5 = ' + N('40√6'))
b('Ex 7.1 Q12: find (x + 1)⁶ + (x − 1)⁶; hence evaluate (√2 + 1)⁶ + (√2 − 1)⁶.', 'Even-power terms double: 2(x⁶ + 15x⁴ + 15x² + 1). At x = √2: 2(8 + 60 + 30 + 1) = ' + N('198'))
b('Trick: (a + b)ⁿ + (a − b)ⁿ and (a + b)ⁿ − (a − b)ⁿ contain which terms?', 'Sum: ' + T('even powers of b') + ' only (doubled). Difference: ' + T('odd powers of b') + ' only (doubled)')
b('Misc Q1: a and b distinct integers. Prove a − b divides aⁿ − bⁿ.', 'Write aⁿ = ((a − b) + b)ⁿ = bⁿ + (a − b)·(…) by the theorem, so aⁿ − bⁿ is a multiple of (a − b)')
b('Misc Q2: evaluate (√3 + √2)⁶ − (√3 − √2)⁶.', '2[⁶C₁(√3)⁵√2 + ⁶C₃(√3)³(√2)³ + ⁶C₅√3(√2)⁵] = 2(54 + 120 + 24)√6 = ' + N('396√6'))
b('Misc Q3: (a² + √(a² − 1))⁴ + (a² − √(a² − 1))⁴ = ?', '2[a⁸ + 6a⁴(a² − 1) + (a² − 1)²] = ' + N('2a⁸ + 12a⁶ − 10a⁴ − 4a² + 2'))
b('Misc Q4: approximate (0.99)⁵ using the first three terms.', '(1 − 0.01)⁵ ≈ 1 − 5(0.01) + 10(0.01)² = 1 − 0.05 + 0.001 = ' + N('0.951'))
sm.small_x_approx(d)

# ---------------------------------------------------------------- Beyond the textbook: general term etc.
d.sec('7.z-general-term')
b('Beyond the textbook text (JEE/board): the general term of (a + b)ⁿ?', r'\(T_{r+1} = {}^nC_r\,a^{\,n-r}\,b^{\,r}\)' + ', r = 0, 1, …, n. Note the index is r + 1 for the (r + 1)th term')
b('Trap: is ⁿCᵣ aⁿ⁻ʳ bʳ the r-th term or the (r + 1)-th term?', X('(r + 1)-th') + '. The first term is r = 0. To find the 5th term use r = 4')
b('Find the 4th term of (2x − 1/x)⁷.', 'r = 3: ⁷C₃(2x)⁴(−1/x)³ = 35 · 16x⁴ · (−1/x³) = ' + N('−560x'))
b('Middle term(s) of (a + b)ⁿ?', 'n even: one middle term T₍ₙ/₂₎₊₁. n odd: two middle terms T₍ₙ₊₁₎/₂ and T₍ₙ₊₃₎/₂')
b('Middle term of (x + 1/x)¹⁰?', 'n = 10 is even → T₆ = ¹⁰C₅ x⁵ x⁻⁵ = ' + N('252'))
sm.coefficient_bars(d)
b('Method: coefficient of xᵏ in (x² + 1/x)⁹.', 'General term T_(r+1) = ⁹Cᵣ (x²)⁹⁻ʳ (1/x)ʳ = ⁹Cᵣ x¹⁸⁻³ʳ. Set 18 − 3r = k and solve for r (must be an integer in 0..9). For x⁶: r = 4 → ' + N('⁹C₄ = 126'))
b('Term independent of x in (x² + 1/x)⁹?', 'Need 18 − 3r = 0 → r = 6: ⁹C₆ = ' + N('84'))
b('Coefficient of x³ in (1 + 2x)⁷?', '⁷C₃ · 2³ = 35 × 8 = ' + N('280'))
b('Method: term independent of x.', 'Write the general term, collect the power of x, set it to ' + T('0') + ', solve for r. If r is not a non-negative integer ≤ n, there is no such term')
b('Sum of all coefficients of a polynomial expansion?', 'Put ' + T('x = 1') + ' (all variables 1). E.g. (2x − 3y)⁵ → (2 − 3)⁵ = −1; (1 + x)¹⁰ → 1024')
b('Sums of odd-indexed and even-indexed coefficients of (1 + x)ⁿ?', 'x = 1 and x = −1: ' + T('ⁿC₀ + ⁿC₂ + … = ⁿC₁ + ⁿC₃ + … = 2ⁿ⁻¹'))
b('Identity: r · ⁿCᵣ and Σ r · ⁿCᵣ?', T('r · ⁿCᵣ = n · ⁿ⁻¹Cᵣ₋₁') + '; hence ' + T('Σ r · ⁿCᵣ = n · 2ⁿ⁻¹') + ' (differentiate (1 + x)ⁿ or use the identity)')
b('Number of terms in (a + b + c)ⁿ? Multinomial coefficient?', N('(n + 1)(n + 2)/2') + ' terms; coefficient of aᵖbᑫcʳ (p + q + r = n) is ' + T('n!/(p! q! r!)'))
b('Ratio of consecutive terms? Use?', r'\(\dfrac{T_{r+1}}{T_r} = \dfrac{n - r + 1}{r}\cdot\dfrac{b}{a}\)' + '. Set ratio ≥ 1 to find the greatest term')
b('Classic (JEE): the coefficients of the 5th, 6th and 7th terms of (1 + x)ⁿ are in AP. Find n.', '2·ⁿC₅ = ⁿC₄ + ⁿC₆ → n² − 21n + 98 = 0 → ' + N('n = 7 or 14'))
b('Classic: if the coefficients of x² and x³ in (3 + ax)⁹ are equal, find a.', '⁹C₂·3⁷·a² = ⁹C₃·3⁶·a³ → 36·3 = 84a → ' + N('a = 9/7'))
d.sec('7.z-remainders')
b('Remainder when 2⁶⁰ is divided by 7?', '2⁶⁰ = 8²⁰ = (7 + 1)²⁰ ≡ ' + N('1') + ' (mod 7)')
b('Last two digits of 11¹⁰ and of 7¹⁰⁰?', '11¹⁰ = (1 + 10)¹⁰ = 1 + 100 + … → ' + N('01') + '. 7⁴ = 2401 = 1 + 2400, so 7¹⁰⁰ = (1 + 2400)²⁵ ends in ' + N('01'))
b('Method: remainders of large powers.', '1) Write the base, or a power of it, as (multiple of d) ± 1 (like 7⁴ = 2401).<br>2) Expand.<br>Only the last one or two terms survive mod d')
b('Remainder when 5⁹⁹ is divided by 13?', '5² = 25 = 26 − 1 ≡ −1, so 5⁹⁹ = 5·(5²)⁴⁹ ≡ 5·(−1)⁴⁹ = −5 ≡ ' + N('8') + ' (mod 13)')
d.sec('7.z-negative-index')
b('Beyond the syllabus core (JEE Main): (1 + x)ⁿ for negative or fractional n?', 'For |x| < 1, ' + T('(1 + x)ⁿ = 1 + nx + n(n − 1)x²/2! + n(n − 1)(n − 2)x³/3! + …') + ' (an infinite series)')
b('Expand 1/(1 + x) and 1/(1 − x)² for |x| < 1.', '1 − x + x² − x³ + …  and  ' + T('1 + 2x + 3x² + 4x³ + …'))
b('Approximate √(1 + x) and ∛(1 + x) for small x.', '1 + x/2 and 1 + x/3. Example: √1.02 ≈ 1.01, ∛1.03 ≈ 1.01')

# ---------------------------------------------------------------- How it's asked
d.sec('7.z-how-its-asked')
b('MCQ: The number of terms in the expansion of (2x + 3y)¹⁰ is<br>(a) 10 (b) 11 (c) 12 (d) 20', E('(b) 11') + ' (n + 1)')
b('MCQ: The sum of the coefficients in (1 + x)¹⁰ is<br>(a) 512 (b) 1024 (c) 10 (d) 2048', E('(b) 1024') + ' = 2¹⁰')
b('MCQ: The coefficient of x³ in (1 + x)⁶ is<br>(a) 15 (b) 20 (c) 6 (d) 10', E('(b) 20') + ' = ⁶C₃')
b('MCQ: The middle term of (1 + x)⁸ is<br>(a) 56x⁴ (b) 70x⁴ (c) 56x⁵ (d) 70x⁵', E('(b) 70x⁴') + ' = ⁸C₄x⁴, the 5th term')
b('MCQ: The term independent of x in (x + 1/x)⁶ is<br>(a) 15 (b) 20 (c) 6 (d) 1', 'r = 3: ⁶C₃ = ' + E('(b) 20'))
b('MCQ: The 3rd term in the expansion of (x + 2)⁵ is<br>(a) 40x³ (b) 80x³ (c) 10x³ (d) 20x³', 'r = 2: ⁵C₂ x³ 2² = 10·4 = ' + E('(a) 40x³'))
b('Integer answer (JEE Main): the coefficient of x⁵ in (1 + x)²¹ + (1 + x)²² + … + (1 + x)³⁰ is ⁿC₆ − ²¹C₆. Find n.', 'Hockey stick: Σ ᵐC₅ (m = 21 to 30) = ³¹C₆ − ²¹C₆. So ' + N('n = 31'))
b('Integer answer: the value of ⁵⁰C₀ − ⁵⁰C₁ + ⁵⁰C₂ − … + ⁵⁰C₅₀ is?', N('0') + ' (alternating sum of a row)')
b('Assertion–Reason.<br><b>A:</b> The number of terms in (a + b)ⁿ is n + 1.<br><b>R:</b> The powers of b range from 0 to n.<br>(a) Both true, R explains A (b) Both true, R does not explain A (c) A true, R false (d) A false, R true', E('(a)'))
b('Assertion–Reason.<br><b>A:</b> 2ⁿ = ⁿC₀ + ⁿC₁ + … + ⁿCₙ.<br><b>R:</b> Put x = 1 in (1 + x)ⁿ.<br>(a) Both true, R explains A (b) Both true, R does not explain A (c) A false, R true (d) Both false', E('(a)'))
b('True/False: the binomial theorem as taught here (positive integer n) has finitely many terms, but for n = ½ it has infinitely many.', E('True') + ': for non-integer n the series does not terminate (valid for |x| < 1)')
b('3-mark: find the coefficient of x⁷ in (ax² + 1/(bx))¹¹.', 'T(r+1) = ¹¹Cᵣ a¹¹⁻ʳ x²²⁻²ʳ b⁻ʳ x⁻ʳ: power 22 − 3r = 7 → r = 5: ' + N('¹¹C₅ a⁶/b⁵ = 462 a⁶/b⁵'))
b('Case-based: a bank pays compound interest; ₹1000 at 10% for n years becomes 1000(1.1)ⁿ. Estimate for n = 3 using the first two terms, then exactly.', 'First two terms: (1 + 0.1)³ ≈ 1 + 0.3 = 1.3 → ₹1300<br>Exactly: 1 + 0.3 + 0.03 + 0.001 = 1.331 → ' + N('₹1331') + '<br>More terms give a better estimate')

print('cards', len(d.cards))
os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
