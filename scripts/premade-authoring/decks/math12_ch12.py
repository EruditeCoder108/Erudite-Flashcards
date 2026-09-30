import sys, os, itertools
from fractions import Fraction as Fr
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase_math as sm

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Mathematics', 'class12-mathematics-ch12-linear-programming')
d = Deck('Chapter 12: Linear Programming', 'Class 12', ['class-12', 'mathematics', 'ch-12'])
d.description = 'Linear programming problems, constraints, feasible region, corner point method, unbounded, infeasible and multiple-optimum cases, formulating word problems, with every answer computed.'
b = d.basic


# ---------------------------------------------------------------- tiny LP solver (answers are computed, not typed)
def num(x):
    x = Fr(x)
    return str(x.numerator) if x.denominator == 1 else f'{x.numerator}/{x.denominator}'


def pt(p): return '(' + num(p[0]) + ', ' + num(p[1]) + ')'


def vertices(cons):
    """cons: list of (a, b, c, op) with op in '<=', '>=': a x + b y op c. x, y >= 0 are added."""
    allc = [(Fr(a), Fr(bb), Fr(c), op) for a, bb, c, op in cons] + [(Fr(1), Fr(0), Fr(0), '>='), (Fr(0), Fr(1), Fr(0), '>=')]
    pts = set()
    for (a1, b1, c1, _), (a2, b2, c2, _) in itertools.combinations(allc, 2):
        det = a1 * b2 - a2 * b1
        if det == 0:
            continue
        x = (c1 * b2 - c2 * b1) / det
        y = (a1 * c2 - a2 * c1) / det
        if all((a * x + bb * y <= c) if op == '<=' else (a * x + bb * y >= c) for a, bb, c, op in allc):
            pts.add((x, y))
    return sorted(pts)


def table(cons, zc):
    vs = vertices(cons)
    return [(v, zc[0] * v[0] + zc[1] * v[1]) for v in vs]


def rows_text(tb):
    return '; '.join(f'{pt(v)} → {num(z)}' for v, z in tb)


# ---------------------------------------------------------------- 12.2 Concepts
d.sec('12.2-concepts')
b('What is a linear programming problem (LPP)?', 'Finding the ' + T('maximum or minimum of a linear objective function Z = ax + by') + '<br>subject to linear inequality constraints (and x, y ≥ 0).<br>“Linear” because all relations are linear; “programming” means finding a plan of action')
b('Define objective function, constraints, decision variables.', T('Objective function') + ': the linear expression Z = ax + by to be optimised<br>' + T('Constraints') + ': the linear inequalities (or equations) on the variables<br>' + T('Decision variables') + ': x and y, with the non-negative restrictions x, y ≥ 0')
b('Define feasible region, feasible and infeasible solutions.', T('Feasible region') + ': the common region satisfying all constraints including x, y ≥ 0<br>' + T('Feasible solution') + ': any point in (or on the boundary of) it<br>' + T('Infeasible') + ': any point outside<br>' + T('Optimal solution') + ': a feasible point giving the optimal value of Z')
b('What is a corner point (vertex) of the feasible region?', 'A point of the region that is the ' + T('intersection of two boundary lines') + '.<br>The region is always convex (a convex polygon, bounded or not)')
b('Bounded vs unbounded feasible region?', T('Bounded') + ': it can be enclosed in a circle. ' + T('Unbounded') + ': it extends indefinitely in some direction')
b('Theorem 1 of LPP (fundamental).', 'If Z has an optimal value (max or min) on the feasible region R, it occurs at a ' + T('corner point') + ' of R')
b('Theorem 2 of LPP.', 'If R is ' + T('bounded') + ', Z has both a maximum and a minimum on R, and each occurs at a corner point. If R is unbounded an optimum may not exist')
b('Steps of the corner point method.', '1) Graph the constraints and find the feasible region and its corners. 2) Evaluate Z at each corner; let M be the largest, m the smallest. 3) If R is bounded, M is the max and m the min. 4) If R is unbounded: M is the max only if ax + by > M has no common point with R; m is the min only if ax + by < m has none; otherwise there is no such optimum')
b('Remark: multiple optimal solutions?', 'If two corner points give the same optimal value, then<br>' + T('every point on the line segment joining them') + ' gives that value too<br>(infinitely many optimal solutions)')
b('Types of outcomes of an LPP.', T('Unique optimum') + ' (one corner); ' + T('multiple optima') + ' (an edge); ' + T('unbounded') + ' (no max or no min); ' + T('infeasible') + ' (no feasible region)')
b('How to graph a constraint like 3x + 5y ≤ 15.', 'Draw the line 3x + 5y = 15 through (5, 0) and (0, 3). Test the origin: 0 ≤ 15 is true, so shade the ' + T('origin side') + '. For a ≥ constraint through the origin, use another test point')
b('Why is the feasible region of an LPP convex?', 'It is the intersection of half-planes, and each half-plane is convex. This is why optimal values occur at corners (a linear function on a convex polygon is extreme at a vertex)')
b('The furniture dealer problem: mathematical formulation.', 'Let x tables and y chairs. Maximise ' + T('Z = 250x + 75y') + ' subject to 2500x + 500y ≤ 50 000 (i.e. 5x + y ≤ 100), x + y ≤ 60, x, y ≥ 0')
sm.lp_corner_points(d)
sm.lp_iso_profit(d)

# ---------------------------------------------------------------- Examples
d.sec('12.3-worked-examples')
tb = table([(1, 1, 50, '<='), (3, 1, 90, '<=')], (4, 1))
b('Example 1: maximise Z = 4x + y subject to x + y ≤ 50, 3x + y ≤ 90, x, y ≥ 0.', 'Corner values: ' + rows_text(tb) + '. ' + N('Maximum Z = 120 at (30, 0)'))
tb = table([(1, 2, 10, '>='), (3, 4, 24, '<=')], (200, 500))
b('Example 2: minimise Z = 200x + 500y subject to x + 2y ≥ 10, 3x + 4y ≤ 24, x, y ≥ 0.', 'Bounded triangle with corners (0, 5), (4, 3), (0, 6): Z = ' + ', '.join(str(int(z)) for v, z in tb) + '. ' + N('Minimum Z = 2300 at (4, 3)'))
sm.lp_multiple_optima(d)
b('Example 3: minimise and maximise Z = 3x + 9y subject to x + 3y ≤ 60, x + y ≥ 10, x ≤ y, x, y ≥ 0.', 'Corners A(0, 10), B(5, 5), C(15, 15), D(0, 20): Z = 90, 60, 180, 180<br>' + N('Min 60 at (5, 5)') + '<br>' + N('Max 180 at every point of segment CD'))
sm.lp_unbounded_check(d)
b('Example 4: is the corner value −300 the minimum of Z = −50x + 20y on the unbounded region?', 'No: the half-plane −50x + 20y < −300 meets the region, so ' + N('Z has no minimum') + '<br>Likewise 100 at (0, 5) is not the maximum, since −50x + 20y > 100 also meets the region')
sm.lp_infeasible(d)
b('Example 5: minimise Z = 3x + 2y subject to x + y ≥ 8, 3x + 5y ≤ 15, x, y ≥ 0.', N('No feasible region, hence no feasible solution') + ' (the two half-planes do not overlap)')

# ---------------------------------------------------------------- Exercise 12.1
d.sec('12.4-exercise-12-1')
tb = table([(1, 1, 4, '<=')], (3, 4))
b('Ex 12.1 Q1: maximise Z = 3x + 4y subject to x + y ≤ 4, x, y ≥ 0.', 'Corners: ' + rows_text(tb) + '. ' + N('Maximum Z = 16 at (0, 4)'))
tb = table([(1, 2, 8, '<='), (3, 2, 12, '<=')], (-3, 4))
b('Ex 12.1 Q2: minimise Z = −3x + 4y subject to x + 2y ≤ 8, 3x + 2y ≤ 12, x, y ≥ 0.', 'Corners: ' + rows_text(tb) + '. ' + N('Minimum Z = −12 at (4, 0)'))
tb = table([(3, 5, 15, '<='), (5, 2, 10, '<=')], (5, 3))
b('Ex 12.1 Q3: maximise Z = 5x + 3y subject to 3x + 5y ≤ 15, 5x + 2y ≤ 10, x, y ≥ 0.', 'Corners: ' + rows_text(tb) + ' (20/19, 45/19 is where the two lines meet). ' + N('Maximum Z = 235/19 at (20/19, 45/19)'))
tb = table([(1, 3, 3, '>='), (1, 1, 2, '>=')], (3, 5))
b('Ex 12.1 Q4: minimise Z = 3x + 5y subject to x + 3y ≥ 3, x + y ≥ 2, x, y ≥ 0.', 'Unbounded region, corners: ' + rows_text(tb) + '. The smallest is 7; the half-plane 3x + 5y < 7 has no point in common with the region, so ' + N('minimum Z = 7 at (3/2, 1/2)'))
tb = table([(1, 2, 10, '<='), (3, 1, 15, '<=')], (3, 2))
b('Ex 12.1 Q5: maximise Z = 3x + 2y subject to x + 2y ≤ 10, 3x + y ≤ 15, x, y ≥ 0.', 'Corners: ' + rows_text(tb) + '. ' + N('Maximum Z = 18 at (4, 3)'))
tb = table([(2, 1, 3, '>='), (1, 2, 6, '>=')], (1, 2))
b('Ex 12.1 Q6: minimise Z = x + 2y subject to 2x + y ≥ 3, x + 2y ≥ 6, x, y ≥ 0. Show the minimum occurs at more than two points.', 'Corners: ' + rows_text(tb) + '. Both give 6, and the objective line x + 2y = 6 is the edge x + 2y ≥ 6. ' + N('Minimum Z = 6 at every point of the segment joining (0, 3) and (6, 0)'))
tb7 = table([(1, 2, 120, '<='), (1, 1, 60, '>='), (1, -2, 0, '>=')], (5, 10))
b('Ex 12.1 Q7: minimise and maximise Z = 5x + 10y subject to x + 2y ≤ 120, x + y ≥ 60, x − 2y ≥ 0, x, y ≥ 0.', 'Corners: ' + rows_text(tb7) + '<br>' + N('Minimum Z = 300 at (60, 0)') + '<br>' + N('Maximum Z = 600 at (120, 0) and (60, 30) and all points on the segment between them') + '<br>(the objective line is parallel to x + 2y = 120)')
tb8 = table([(1, 2, 100, '>='), (2, -1, 0, '<='), (2, 1, 200, '<=')], (1, 2))
b('Ex 12.1 Q8: minimise and maximise Z = x + 2y subject to x + 2y ≥ 100, 2x − y ≤ 0, 2x + y ≤ 200, x, y ≥ 0.', 'Corners: ' + rows_text(tb8) + '. ' + N('Minimum Z = 100 at every point of the segment joining (0, 50) and (20, 40)') + '; ' + N('maximum Z = 400 at (0, 200)'))
tb9 = table([(1, 0, 3, '>='), (1, 1, 5, '>='), (1, 2, 6, '>=')], (-1, 2))
b('Ex 12.1 Q9: maximise Z = −x + 2y subject to x ≥ 3, x + y ≥ 5, x + 2y ≥ 6, y ≥ 0.', 'Unbounded region with corners: ' + rows_text(tb9) + '. The corner maximum is 1, but −x + 2y > 1 has points in the region (take y large). ' + N('Z has no maximum value'))
b('Ex 12.1 Q10: maximise Z = x + y subject to x − y ≤ −1, −x + y ≤ 0, x, y ≥ 0.', 'x − y ≤ −1 gives y ≥ x + 1, while −x + y ≤ 0 gives y ≤ x. These cannot both hold: ' + N('no feasible region, so no maximum'))

# ---------------------------------------------------------------- Formulating word problems
d.sec('12.5-word-problems')
b('Formulating an LPP from words: method.', '1) Name the decision variables x, y. 2) Write the objective (profit, cost) as Z = ax + by. 3) Turn each limit (time, money, space, ingredients) into a linear inequality: “at most” → ≤, “at least” → ≥. 4) Add x, y ≥ 0. 5) Solve by corner points')
tbx = table([(2, 1, 100, '<='), (1, 1, 80, '<='), (1, 0, 40, '<=')], (40, 30))
b('Production plan: a factory makes products P and Q. Machine time: 2x + y ≤ 100; labour: x + y ≤ 80; demand for P at most 40. Profit ₹40 on P and ₹30 on Q. Maximise profit.', 'Maximise Z = 40x + 30y. Corners: ' + rows_text(tbx) + '. ' + N('Maximum profit ₹2600 at (20, 60)') + ' (20 of P and 60 of Q use exactly the machine time and labour)')
tbd = table([(2, 1, 8, '>='), (1, 3, 9, '>='), (1, 1, 0, '>=')], (5, 4))
b('Diet problem: food X costs ₹5/kg and gives 2 units of vitamin A and 1 of vitamin B; food Y costs ₹4/kg and gives 1 of A and 3 of B. Minimum daily need: 8 units of A and 9 of B. Cheapest mix?', 'Minimise Z = 5x + 4y subject to 2x + y ≥ 8, x + 3y ≥ 9, x, y ≥ 0 (unbounded region). Corners: ' + rows_text(tbd) + '. The half-plane 5x + 4y < 23 misses the region, so ' + N('minimum cost ₹23 with 3 kg of X and 2 kg of Y'))
b('A dealer has ₹15 000 and space for 20 items. A fan costs ₹1500 and yields ₹300 profit; a heater costs ₹500 and yields ₹200. Maximise profit.', 'Maximise Z = 300x + 200y subject to 1500x + 500y ≤ 15 000 (3x + y ≤ 30), x + y ≤ 20, x, y ≥ 0. Corners: ' + rows_text(table([(3, 1, 30, '<='), (1, 1, 20, '<=')], (300, 200))) + '. ' + N('Maximum ₹4500 at (5, 15)'))
b('A tailor has 24 hours of cutting time and 16 hours of stitching time. A shirt needs 3 h cutting and 2 h stitching (profit ₹30); a trouser needs 4 h cutting and 2 h stitching (profit ₹40). Maximise profit.', 'Maximise Z = 30x + 40y subject to 3x + 4y ≤ 24, 2x + 2y ≤ 16, x, y ≥ 0. The stitching constraint is redundant. Corners: ' + rows_text(table([(3, 4, 24, '<='), (1, 1, 8, '<=')], (30, 40))) + '. ' + N('Maximum ₹240 at (8, 0) and (0, 6), hence at every point of the segment between them') + ' (Z = 10(3x + 4y), parallel to the cutting constraint)')
b('Multiple optimum test: when is the optimal solution not unique?', 'When the objective line is parallel to a ' + T('boundary edge') + ' that touches the optimum:<br>the two ends of that edge give equal Z (as in Example 3 and Ex 12.1 Q6–Q8)')

# ---------------------------------------------------------------- Exam patterns
d.sec('12.z-exam-patterns')
b('Iso-profit / iso-cost line method.', 'Draw Z = 0 and slide it parallel to itself: the last feasible point it touches (largest c for max, smallest for min) is the optimum. It is a picture of the corner-point method')
b('How do you find corner points quickly?', '1) Intersect pairs of boundary lines (including the axes).<br>2) Keep only those points that satisfy ' + T('all') + ' the other constraints.<br>(The solver above does exactly this.)')
b('Can the maximum of an LPP occur at an interior point?', X('No') + ': by Theorem 1 an optimum (if it exists) is at a corner point. For a constant objective (all zero) every point is optimal, but that is not a real LPP')
b('What if the objective function is a multiple of one of the constraint lines?', 'Then there are ' + T('multiple optimal solutions') + ': the whole edge on that line, from vertex to vertex')
b('Does every LPP with a feasible region have a maximum?', X('No') + ': if the region is unbounded the maximum may not exist (Ex 12.1 Q9). A bounded feasible region always has both max and min')
b('How can you check that the LPP has no solution at all?', 'Look for contradictory constraints (like y ≥ x + 1 and y ≤ x),<br>or plot the half-planes and see that there is no common shaded region')
b('Two-phase check for an unbounded minimisation problem.', 'Compute Z at the corners and take the smallest m. Then draw ax + by < m. If that half-plane misses the region, m is the minimum; otherwise there is no minimum')
b('A quick sanity check for a computed optimum.', '1) Substitute the optimum point into every constraint; it must satisfy all of them.<br>2) Check that Z at neighbouring corners is not better')

# ---------------------------------------------------------------- How it is asked
d.sec('12.z-how-its-asked')
b('MCQ: the maximum value of Z = 4x + 3y subject to x + y ≤ 5, x ≤ 3, x, y ≥ 0 is<br>(a) 15 (b) 18 (c) 17 (d) 12', 'Corners (0,0), (3,0), (3,2), (0,5): Z = 0, 12, 18, 15: ' + E('(b) 18'))
b('MCQ: the corner points of a feasible region are (0, 0), (4, 0), (2, 3), (0, 2). Z = 5x + 2y is maximum at<br>(a) (0, 0) (b) (4, 0) (c) (2, 3) (d) (0, 2)', 'Z = 0, 20, 16, 4: ' + E('(b) (4, 0)'))
b('MCQ: which is a feasible solution of x + y ≤ 4, x, y ≥ 0?<br>(a) (3, 2) (b) (1, 2) (c) (5, 0) (d) (−1, 2)', '(1, 2): 3 ≤ 4 and non-negative: ' + E('(b)'))
b('MCQ: a feasible region that can be enclosed within a circle is called<br>(a) bounded (b) unbounded (c) infeasible (d) optimal', E('(a) bounded'))
b('MCQ: the constraints x ≥ 0, y ≥ 0 are called<br>(a) non-negativity restrictions (b) objective function (c) decision variables (d) optimal solutions', E('(a)'))
b('MCQ: if Z = ax + by has the same maximum at two corner points, then<br>(a) the maximum occurs at every point of the segment joining them (b) no maximum (c) a unique maximum (d) the region is unbounded', E('(a)'))
b('MCQ: the number of corner points of a feasible region defined by x + y ≤ 4, x ≤ 3, x, y ≥ 0 is<br>(a) 4 (b) 5 (c) 3 (d) 6', 'Corners (0,0), (3,0), (3,1), (0,4): ' + E('(a) 4'))
b('Integer answer (JEE Main): the maximum value of Z = x + 2y subject to x + y ≤ 6, x ≤ 4, x, y ≥ 0 is?', 'Corners (0, 0), (4, 0), (4, 2), (0, 6): Z = 0, 4, 8, 12: ' + N('12'))
b('Integer answer: the minimum value of Z = 2x + 3y subject to x + y ≥ 5, x ≥ 1, y ≥ 1 is?', 'Corners (1, 4) and (4, 1) give Z = 14 and 11. The region is unbounded but Z only increases away from the corners: ' + N('11'))
b('Assertion–Reason.<br><b>A:</b> the optimal value of an LPP occurs at a corner point of the feasible region.<br><b>R:</b> the objective function is linear and the region is convex.<br>(a) Both true, R explains A (b) Both true, R does not (c) A true, R false (d) A false, R true', E('(a)'))
b('Assertion–Reason.<br><b>A:</b> every LPP with an unbounded feasible region has no maximum.<br><b>R:</b> in an unbounded region, values of Z may increase indefinitely.<br>(a) Both true, R explains A (b) A false, R true (c) A true, R false (d) Both false', E('(b)') + ': in an unbounded region a maximum or minimum may or may not exist (Ex 12.1 Q4 has a minimum)')
b('True/False: the feasible region of an LPP is always convex.', E('True'))
b('True/False: an LPP can have exactly two optimal solutions.', X('False') + ': two optimal corners force infinitely many optimal points (the whole segment)')
b('2-mark: define feasible region.', 'The common region determined by all the constraints, including x, y ≥ 0, of a linear programming problem.')
b('3-mark: maximise Z = 3x + 2y subject to x + y ≤ 4, x ≤ 3, x, y ≥ 0.', 'Corners (0, 0), (3, 0), (3, 1), (0, 4): Z = 0, 9, 11, 8. ' + N('Maximum Z = 11 at (3, 1)'))
b('4-mark: a manufacturer makes tables and chairs. A table needs 4 h of carpentry and 2 h of finishing; a chair needs 2 h and 2 h. Available: 40 h carpentry, 30 h finishing. Profit ₹100 per table, ₹60 per chair. Maximise profit.', 'Maximise Z = 100x + 60y subject to 4x + 2y ≤ 40, 2x + 2y ≤ 30, x, y ≥ 0. Corners: ' + rows_text(table([(4, 2, 40, '<='), (2, 2, 30, '<=')], (100, 60))) + '. ' + N('Maximum ₹1100 at (5, 10)'))
b('4-mark: minimise Z = 4x + 3y subject to x + y ≥ 5, 2x + y ≥ 8, x, y ≥ 0.', 'Corners: ' + rows_text(table([(1, 1, 5, '>='), (2, 1, 8, '>=')], (4, 3))) + '. The region is unbounded but Z grows in every unbounded direction (the half-plane 4x + 3y < 18 misses it): ' + N('minimum Z = 18 at (3, 2)'))
b('Case-based: a farmer has 50 acres and ₹4 000. Wheat costs ₹40/acre and gives ₹200 profit/acre; maize costs ₹100/acre and gives ₹400. How should he plant (fractions of an acre allowed)?', 'Maximise Z = 200x + 400y subject to x + y ≤ 50, 40x + 100y ≤ 4000 (2x + 5y ≤ 200), x, y ≥ 0. Corners: ' + rows_text(table([(1, 1, 50, '<='), (2, 5, 200, '<=')], (200, 400))) + '. ' + N('Maximum ₹50000/3 ≈ ₹16 667 at (50/3, 100/3)'))

print('cards', len(d.cards))
os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
