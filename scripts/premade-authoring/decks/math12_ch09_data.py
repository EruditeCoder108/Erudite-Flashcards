"""Exercise data for Maths 12 Ch 9 (differential equations). Solutions are verified numerically against the ODE."""
import math

ENV = dict(sin=math.sin, cos=math.cos, tan=math.tan, exp=math.exp, log=math.log, sqrt=math.sqrt, atan=math.atan,
           asin=math.asin, acos=math.acos, pi=math.pi, abs=abs, a=0.7, c=1.3, e=math.e)

ODE = []   # (tag, ode text, solution text, hint, kind, g, sol, points, extra)
# kind 'exp': sol = y(x) with constant c, check y' = g(x, y); points = xs
# kind 'imp': sol = F(x, y) (solution F = const), check -Fx/Fy = g(x, y); points = (x, y) pairs
# extra: optional (x0, y0, F0) initial condition check


def E(tag, ode, sol, hint, g, y, xs=(0.3, 0.6, 0.9), init=None):
    ODE.append((tag, ode, sol, hint, 'exp', g, y, xs, init))


def I(tag, ode, sol, hint, g, F, pts=((0.4, 0.5), (0.7, 0.3), (0.9, 0.8)), init=None):
    ODE.append((tag, ode, sol, hint, 'imp', g, F, pts, init))


def verify():
    bad = []
    for tag, ode, sol, hint, kind, g, S, pts, init in ODE:
        try:
            gg = eval('lambda x, y: ' + g, ENV)
            if kind == 'exp':
                Y = eval('lambda x: ' + S, ENV)
                for x in pts:
                    h = 1e-5
                    d = (Y(x + h) - Y(x - h)) / (2 * h)
                    if abs(d - gg(x, Y(x))) > 1e-4 * (1 + abs(d)):
                        bad.append((tag, x, d, gg(x, Y(x))))
                        break
                if init:
                    x0, y0, _ = init
                    if abs(Y(x0) - y0) > 1e-6:
                        bad.append((tag, 'init', Y(x0), y0))
            else:
                F = eval('lambda x, y: ' + S, ENV)
                for (x, y) in pts:
                    h = 1e-5
                    Fx = (F(x + h, y) - F(x - h, y)) / (2 * h)
                    Fy = (F(x, y + h) - F(x, y - h)) / (2 * h)
                    d = -Fx / Fy
                    if abs(d - gg(x, y)) > 1e-4 * (1 + abs(d)):
                        bad.append((tag, (x, y), d, gg(x, y)))
                        break
                if init:
                    x0, y0, F0 = init
                    if abs(F(x0, y0) - F0) > 1e-6:
                        bad.append((tag, 'init', F(x0, y0), F0))
        except Exception as ex:
            bad.append((tag, 'error', str(ex)))
    return bad


# ---------------------------------------------------------------- Ex 9.3 separable, general solutions
E('Ex 9.3 Q1', 'dy/dx = (1 − cos x)/(1 + cos x)', 'y = 2 tan(x/2) − x + C', '(1 − cos x)/(1 + cos x) = tan²(x/2) = sec²(x/2) − 1', '(1-cos(x))/(1+cos(x))', '2*tan(x/2)-x+c')
E('Ex 9.3 Q2', 'dy/dx = √(4 − y²)  (−2 < y < 2)', 'y = 2 sin(x + C)', 'separate: dy/√(4 − y²) = dx, sin⁻¹(y/2) = x + C', 'sqrt(4-y**2)', '2*sin(x+c)', (-0.6, -0.4, -0.2))
E('Ex 9.3 Q3', 'dy/dx + y = 1  (y ≠ 1)', 'y = 1 + A e^(−x)', 'dy/(1 − y) = dx, −log|1 − y| = x + C', '1-y', '1+c*exp(-x)')
I('Ex 9.3 Q4', 'sec²x tan y dx + sec²y tan x dy = 0', 'tan x tan y = C', 'divide by tan x tan y: sec²x/tan x dx + sec²y/tan y dy = 0', '-(1/cos(x)**2)*tan(y)/(tan(x)*(1/cos(y)**2))', 'tan(x)*tan(y)')
E('Ex 9.3 Q5', '(eˣ + e^(−x)) dy − (eˣ − e^(−x)) dx = 0', 'y = log(eˣ + e^(−x)) + C', 'dy = (eˣ − e^(−x))/(eˣ + e^(−x)) dx', '(exp(x)-exp(-x))/(exp(x)+exp(-x))', 'log(exp(x)+exp(-x))+c')
I('Ex 9.3 Q6', 'dy/dx = (1 + x²)(1 + y²)', 'tan⁻¹y = x + x³/3 + C', 'dy/(1 + y²) = (1 + x²) dx', '(1+x**2)*(1+y**2)', 'atan(y)-x-x**3/3')
E('Ex 9.3 Q7', 'y log y dx − x dy = 0', 'y = e^(Cx)', 'dy/(y log y) = dx/x, log|log y| = log|x| + C', 'y*log(y)/x', 'exp(c*x)', (0.4, 0.8, 1.2))
I('Ex 9.3 Q8', 'x⁵ dy/dx = −y⁵', 'x⁻⁴ + y⁻⁴ = C', 'dy/y⁵ = −dx/x⁵', '-y**5/x**5', 'x**(-4)+y**(-4)')
E('Ex 9.3 Q9', 'dy/dx = sin⁻¹x', 'y = x sin⁻¹x + √(1 − x²) + C', 'integrate sin⁻¹x by parts', 'asin(x)', 'x*asin(x)+sqrt(1-x**2)+c')
I('Ex 9.3 Q10', 'eˣ tan y dx + (1 − eˣ) sec²y dy = 0', 'tan y = C(1 − eˣ)', 'separate: eˣ/(1 − eˣ) dx + sec²y/tan y dy = 0', '-exp(x)*tan(y)/((1-exp(x))*(1/cos(y)**2))', 'tan(y)/(1-exp(x))', ((0.4, 0.5), (0.7, 0.3), (-0.9, 0.8)))

# ---------------------------------------------------------------- Ex 9.3 particular solutions
E('Ex 9.3 Q11', '(x³ + x² + x + 1) dy/dx = 2x² + x; y = 1 when x = 0', 'y = ¼ log[(x + 1)²(x² + 1)³] − ½ tan⁻¹x + 1', '(2x² + x)/((x + 1)(x² + 1)) = 1/(2(x + 1)) + (3x + 1)/(2(x² + 1)) after splitting', '(2*x**2+x)/(x**3+x**2+x+1)', 'log((x+1)**2*(x**2+1)**3)/4-atan(x)/2+1', (0.3, 0.6, 0.9), (0, 1, 0))
E('Ex 9.3 Q12', 'x(x² − 1) dy/dx = 1; y = 0 when x = 2', 'y = ½ log|(x² − 1)/x²| − ½ log(3/4)', '1/(x(x² − 1)) = −1/x + ½/(x − 1) + ½/(x + 1)', '1/(x*(x**2-1))', 'log((x**2-1)/x**2)/2-log(0.75)/2', (1.6, 2.2, 3.1), (2, 0, 0))
E('Ex 9.3 Q13', 'cos(dy/dx) = a (a ∈ R); y = 1 when x = 0', 'cos((y − 1)/x) = a', 'dy/dx = cos⁻¹a is constant, so y = x cos⁻¹a + 1', 'acos(a)', 'x*acos(a)+1', (0.3, 0.6, 0.9), (0, 1, 0))
E('Ex 9.3 Q14', 'dy/dx = y tan x; y = 1 when x = 0', 'y = sec x', 'dy/y = tan x dx, log y = log sec x + C', 'y*tan(x)', '1/cos(x)', (0.3, 0.6, 0.9), (0, 1, 0))
E('Ex 9.3 Q15', 'y′ = eˣ sin x; the curve passes through (0, 0)', '2y − 1 = eˣ(sin x − cos x)', 'y = ∫eˣ sin x dx = eˣ(sin x − cos x)/2 + C, C = ½', 'exp(x)*sin(x)', '(exp(x)*(sin(x)-cos(x))+1)/2', (0.3, 0.6, 0.9), (0, 0, 0))
I('Ex 9.3 Q16', 'xy dy/dx = (x + 2)(y + 2); curve through (1, −1)', 'y − x + 2 = log(x²(y + 2)²)', 'y/(y + 2) dy = (x + 2)/x dx', '(x+2)*(y+2)/(x*y)', 'y-x-log(x**2*(y+2)**2)', ((0.4, 0.5), (0.7, 0.3), (0.9, 0.8)), (1, -1, -2))
I('Ex 9.3 Q17', 'the product of the slope of the tangent and the y-coordinate equals the x-coordinate; curve through (0, −2)', 'y² − x² = 4', 'y dy/dx = x → y dy = x dx', 'x/y', 'y**2-x**2', ((0.4, 0.5), (0.7, 0.3), (0.9, 0.8)), (0, -2, 4))
I('Ex 9.3 Q18', 'the slope at (x, y) is twice the slope of the segment joining it to (−4, −3); curve through (−2, 1)', '(x + 4)² = y + 3', 'dy/dx = 2(y + 3)/(x + 4) → dy/(y + 3) = 2dx/(x + 4)', '2*(y+3)/(x+4)', '(x+4)**2/(y+3)', ((0.4, 0.5), (0.7, 0.3), (0.9, 0.8)), (-2, 1, 1))
# ---------------------------------------------------------------- Ex 9.4 homogeneous
I('Ex 9.4 Q1', '(x² + xy) dy = (x² + y²) dx', '(x − y)² = C x e^(−y/x)', 'y = vx: x dv/dx = (1 − v)/(1 + v)', '(x**2+y**2)/(x**2+x*y)', 'log((x-y)**2/x)+y/x', ((1.5, 0.5), (2.0, 0.7), (2.5, 1.1)))
E('Ex 9.4 Q2', 'y′ = (x + y)/x', 'y = x log|x| + Cx', 'y = vx: x dv/dx = 1', '(x+y)/x', 'x*log(x)+c*x', (0.8, 1.5, 2.1))
I('Ex 9.4 Q3', '(x − y) dy − (x + y) dx = 0', 'tan⁻¹(y/x) = ½ log(x² + y²) + C', 'y = vx: (1 − v)/(1 + v²) dv = dx/x', '(x+y)/(x-y)', 'atan(y/x)-log(x**2+y**2)/2', ((1.5, 0.5), (2.0, 0.7), (2.5, 1.1)))
I('Ex 9.4 Q4', '(x² − y²) dx + 2xy dy = 0', 'x² + y² = Cx', 'y = vx: 2v/(1 + v²) dv = −dx/x', '-(x**2-y**2)/(2*x*y)', '(x**2+y**2)/x', ((1.5, 0.5), (2.0, 0.7), (2.5, 1.1)))
I('Ex 9.4 Q5', 'x² dy/dx = x² − 2y² + xy', '(1/(2√2)) log|(x + √2 y)/(x − √2 y)| = log|x| + C', 'y = vx: x dv/dx = 1 − 2v²', '(x**2-2*y**2+x*y)/x**2', 'log(abs((x+sqrt(2)*y)/(x-sqrt(2)*y)))/(2*sqrt(2))-log(x)', ((2.0, 0.5), (2.5, 0.7), (3.0, 1.1)))
I('Ex 9.4 Q6', 'x dy − y dx = √(x² + y²) dx', 'y + √(x² + y²) = Cx²', 'y = vx: dv/√(1 + v²) = dx/x', '(y+sqrt(x**2+y**2))/x', '(y+sqrt(x**2+y**2))/x**2', ((1.5, 0.5), (2.0, 0.7), (2.5, 1.1)))
I('Ex 9.4 Q7', '{x cos(y/x) + y sin(y/x)} y dx = {y sin(y/x) − x cos(y/x)} x dy', 'xy cos(y/x) = C', 'y = vx: separate (v sin v − cos v)/(v cos v) dv', '(x*cos(y/x)+y*sin(y/x))*y/((y*sin(y/x)-x*cos(y/x))*x)', 'x*y*cos(y/x)', ((1.5, 0.5), (2.0, 0.7), (2.5, 1.1)))
I('Ex 9.4 Q8', 'x dy/dx − y + x sin(y/x) = 0', 'x[1 − cos(y/x)] = C sin(y/x)', 'y = vx: x dv/dx = −sin v, so dv/sin v = −dx/x', '(y-x*sin(y/x))/x', 'x*(1-cos(y/x))/sin(y/x)', ((1.5, 0.5), (2.0, 0.7), (2.5, 1.1)))
I('Ex 9.4 Q9', 'y dx + x log(y/x) dy − 2x dy = 0', 'c y = log|y/x| − 1', 'y = vx: (2 − log v)/(v(log v − 1)) dv = dx/x', 'y/(2*x-x*log(y/x))', '(log(y/x)-1)/y', ((1.5, 0.5), (2.0, 0.7), (2.5, 1.1)))
I('Ex 9.4 Q10', '(1 + e^(x/y)) dx + e^(x/y)(1 − x/y) dy = 0', 'x + y e^(x/y) = C', 'x = vy: dx/dy = v + y dv/dy', '-(1+exp(x/y))/(exp(x/y)*(1-x/y))', 'x+y*exp(x/y)', ((1.5, 0.5), (2.0, 0.7), (2.5, 1.1)))
I('Ex 9.4 Q11', '(x + y) dy + (x − y) dx = 0; y = 1 when x = 1', 'log(x² + y²) + 2 tan⁻¹(y/x) = π/2 + log 2', 'y = vx: (1 + v)/(1 + v²) dv = −dx/x', '-(x-y)/(x+y)', 'log(x**2+y**2)+2*atan(y/x)', ((1.5, 0.5), (2.0, 0.7), (2.5, 1.1)), (1, 1, math.pi / 2 + math.log(2)))
I('Ex 9.4 Q12', 'x² dy + (xy + y²) dx = 0; y = 1 when x = 1', 'y + 2x = 3x²y', 'y = vx: dv/(v(v + 2)) = −dx/x', '-(x*y+y**2)/x**2', '(y+2*x)/(x**2*y)', ((1.5, 0.5), (2.0, 0.7), (2.5, 1.1)), (1, 1, 3))
I('Ex 9.4 Q13', '[x sin²(y/x) − y] dx + x dy = 0; y = π/4 when x = 1', 'cot(y/x) = log|ex|', 'y = vx: dv/sin²v = −dx/x', '(y-x*sin(y/x)**2)/x', '1/tan(y/x)-log(x)', ((1.5, 0.5), (2.0, 0.7), (2.5, 1.1)), (1, math.pi / 4, 1))
I('Ex 9.4 Q14', 'dy/dx − y/x + cosec(y/x) = 0; y = 0 when x = 1', 'cos(y/x) = log|ex|', 'y = vx: x dv/dx = −cosec v', '(y/x)-1/sin(y/x)', 'cos(y/x)-log(x)', ((1.5, 0.5), (2.0, 0.7), (2.5, 1.1)), (1, 0, 1))
E('Ex 9.4 Q15', '2xy + y² − 2x² dy/dx = 0; y = 2 when x = 1', 'y = 2x/(1 − log|x|)', 'y = vx: 2v + v² − 2(v + x dv/dx) = 0 → dv/v² = dx/(2x)', '(2*x*y+y**2)/(2*x**2)', '2*x/(1-log(x))', (0.4, 0.7, 1.0), (1, 2, 0))

# ---------------------------------------------------------------- Ex 9.5 linear
E('Ex 9.5 Q1', 'dy/dx + 2y = sin x', 'y = (2 sin x − cos x)/5 + C e^(−2x)', 'IF = e^(2x)', 'sin(x)-2*y', '(2*sin(x)-cos(x))/5+c*exp(-2*x)')
E('Ex 9.5 Q2', 'dy/dx + 3y = e^(−2x)', 'y = e^(−2x) + C e^(−3x)', 'IF = e^(3x)', 'exp(-2*x)-3*y', 'exp(-2*x)+c*exp(-3*x)')
E('Ex 9.5 Q3', 'dy/dx + y/x = x²', 'xy = x⁴/4 + C', 'IF = x', 'x**2-y/x', '(x**4/4+c)/x', (0.8, 1.5, 2.1))
E('Ex 9.5 Q4', 'dy/dx + (sec x) y = tan x  (0 ≤ x < π/2)', 'y(sec x + tan x) = sec x + tan x − x + C', 'IF = sec x + tan x', 'tan(x)-y/cos(x)', '(1/cos(x)+tan(x)-x+c)/(1/cos(x)+tan(x))')
E('Ex 9.5 Q5', 'cos²x dy/dx + y = tan x  (0 ≤ x < π/2)', 'y = tan x − 1 + C e^(−tan x)', 'divide: dy/dx + sec²x y = tan x sec²x; IF = e^(tan x)', '(tan(x)-y)/cos(x)**2', 'tan(x)-1+c*exp(-tan(x))')
E('Ex 9.5 Q6', 'x dy/dx + 2y = x² log x', 'y = (x²/16)(4 log x − 1) + C x⁻²', 'IF = x²', '(x**2*log(x)-2*y)/x', 'x**2*(4*log(x)-1)/16+c/x**2', (0.8, 1.5, 2.1))
E('Ex 9.5 Q7', 'x log x dy/dx + y = (2/x) log x', 'y log x = −(2/x)(1 + log x) + C', 'IF = log x', '(2*log(x)/x-y)/(x*log(x))', '(-2*(1+log(x))/x+c)/log(x)', (1.6, 2.2, 3.1))
E('Ex 9.5 Q8', '(1 + x²) dy + 2xy dx = cot x dx  (x ≠ 0)', 'y = (log|sin x| + C)/(1 + x²)', 'IF = 1 + x²', '(1/tan(x)-2*x*y)/(1+x**2)', '(log(sin(x))+c)/(1+x**2)')
E('Ex 9.5 Q9', 'x dy/dx + y − x + xy cot x = 0  (x ≠ 0)', 'y = 1/x − cot x + C/(x sin x)', 'y′ + (1/x + cot x)y = 1, IF = x sin x', '1-y*(1/x+1/tan(x))', '1/x-1/tan(x)+c/(x*sin(x))', (0.8, 1.5, 2.1))
I('Ex 9.5 Q10', '(x + y) dy/dx = 1', 'x + y + 1 = C e^y', 'dx/dy − x = y: IF = e^(−y)', '1/(x+y)', '(x+y+1)/exp(y)', ((0.4, 0.5), (0.7, 0.3), (0.9, 0.8)))
I('Ex 9.5 Q11', 'y dx + (x − y²) dy = 0', 'x = y²/3 + C/y', 'dx/dy + x/y = y: IF = y', '-y/(x-y**2)', '(x-y**2/3)*y', ((0.4, 0.5), (0.7, 0.3), (0.9, 0.8)))
I('Ex 9.5 Q12', '(x + 3y²) dy/dx = y', 'x = 3y² + Cy', 'dx/dy − x/y = 3y: IF = 1/y', 'y/(x+3*y**2)', '(x-3*y**2)/y', ((0.4, 0.5), (0.7, 0.3), (0.9, 0.8)))
E('Ex 9.5 Q13', 'dy/dx + 2y tan x = sin x; y = 0 when x = π/3', 'y = cos x − 2cos²x', 'IF = sec²x; y sec²x = sec x + C', 'sin(x)-2*y*tan(x)', 'cos(x)-2*cos(x)**2', (0.3, 0.6, 0.9), (math.pi / 3, 0, 0))
E('Ex 9.5 Q14', '(1 + x²) dy/dx + 2xy = 1/(1 + x²); y = 0 when x = 1', 'y(1 + x²) = tan⁻¹x − π/4', 'd/dx[(1 + x²) y] = 1/(1 + x²)', '(1/(1+x**2)-2*x*y)/(1+x**2)', '(atan(x)-pi/4)/(1+x**2)', (0.3, 0.6, 0.9), (1, 0, 0))
E('Ex 9.5 Q15', 'dy/dx − 3y cot x = sin 2x; y = 2 when x = π/2', 'y = 4 sin³x − 2 sin²x', 'IF = 1/sin³x; y/sin³x = ∫2 cos x/sin²x dx', 'sin(2*x)+3*y/tan(x)', '4*sin(x)**3-2*sin(x)**2', (0.3, 0.6, 0.9), (math.pi / 2, 2, 0))
E('Ex 9.5 Q16', 'the slope of the tangent at (x, y) equals the sum of the coordinates; curve through the origin', 'x + y + 1 = eˣ', 'dy/dx − y = x: IF = e^(−x)', 'x+y', 'exp(x)-x-1', (0.3, 0.6, 0.9), (0, 0, 0))
E('Ex 9.5 Q17', 'x + y exceeds the magnitude of the slope by 5; curve through (0, 2)', 'y = 4 − x − 2eˣ', 'y′ = x + y − 5: y′ − y = x − 5', 'x+y-5', '4-x-2*exp(x)', (0.3, 0.6, 0.9), (0, 2, 0))

# ---------------------------------------------------------------- Miscellaneous
I('Misc Q4', 'dy/dx + √((1 − y²)/(1 − x²)) = 0', 'sin⁻¹x + sin⁻¹y = C', 'dy/√(1 − y²) + dx/√(1 − x²) = 0', '-sqrt((1-y**2)/(1-x**2))', 'asin(x)+asin(y)')
I('Misc Q5', 'dy/dx + (y² + y + 1)/(x² + x + 1) = 0', '(x + y + 1) = A(1 − x − y − 2xy)', 'dy/(y² + y + 1) + dx/(x² + x + 1) = 0; tan⁻¹ addition formula', '-(y**2+y+1)/(x**2+x+1)', '(x+y+1)/(1-x-y-2*x*y)', ((0.4, 0.5), (0.7, 0.3), (0.9, 0.8)))
I('Misc Q6', 'sin x cos y dx + cos x sin y dy = 0; curve through (0, π/4)', 'cos y = sec x/√2', 'the left side is −d(cos x cos y)', '-sin(x)*cos(y)/(cos(x)*sin(y))', 'cos(x)*cos(y)', ((0.4, 0.5), (0.7, 0.3), (0.9, 0.8)), (0, math.pi / 4, 1 / math.sqrt(2)))
I('Misc Q7', '(1 + e^(2x)) dy + (1 + y²) eˣ dx = 0; y = 1 when x = 0', 'tan⁻¹y + tan⁻¹(eˣ) = π/2', 'dy/(1 + y²) = −eˣ dx/(1 + e^(2x))', '-(1+y**2)*exp(x)/(1+exp(2*x))', 'atan(y)+atan(exp(x))', ((0.4, 0.5), (0.7, 0.3), (0.9, 0.8)), (0, 1, math.pi / 2))
I('Misc Q8', 'y e^(x/y) dx = (x e^(x/y) + y²) dy  (y ≠ 0)', 'e^(x/y) = y + C', 'x = vy: e^v dv = dy', 'y*exp(x/y)/(x*exp(x/y)+y**2)', 'exp(x/y)-y', ((1.5, 0.5), (2.0, 0.7), (2.5, 1.1)))
I('Misc Q9', '(x − y)(dx + dy) = dx − dy; y = −1 when x = 0', 'log|x − y| = x + y + 1', 'with t = x − y the equation becomes dy/dx = (1 − t)/(1 + t); integrate in t', '(1-(x-y))/(1+(x-y))*1', 'log(abs(x-y))-x-y', ((1.5, 0.5), (2.0, 0.7), (2.5, 1.1)), (0, -1, 1))
I('Misc Q10', '[e^(−2√x)/√x − y/√x] dx/dy = 1  (x ≠ 0)', 'y e^(2√x) = 2√x + C', 'dy/dx + y/√x = e^(−2√x)/√x; IF = e^(2√x)', '(exp(-2*sqrt(x))-y)/sqrt(x)', 'y*exp(2*sqrt(x))-2*sqrt(x)', ((1.5, 0.5), (2.0, 0.7), (2.5, 1.1)))
E('Misc Q11', 'dy/dx + y cot x = 4x cosec x; y = 0 when x = π/2', 'y sin x = 2x² − π²/2', 'IF = sin x', '4*x/sin(x)-y/tan(x)', '(2*x**2-pi**2/2)/sin(x)', (0.5, 1.0, 1.4), (math.pi / 2, 0, 0))
E('Misc Q12', '(x + 1) dy/dx = 2e^(−y) − 1; y = 0 when x = 0', 'y = log|(2x + 1)/(x + 1)|', 'e^y dy/(2 − e^y) = dx/(x + 1)', '(2*exp(-y)-1)/(x+1)', 'log((2*x+1)/(x+1))', (0.3, 0.6, 0.9), (0, 0, 0))
I('Misc Q13', 'y dx − x dy = 0', 'y = Cx  (equivalently x = C₁y)', 'dy/y = dx/x', 'y/x', 'y/x', ((1.5, 0.5), (2.0, 0.7), (2.5, 1.1)))
I('Misc Q15', 'eˣ dy + (y eˣ + 2x) dx = 0', 'y eˣ + x² = C', 'the left side is d(y eˣ + x²)', '-(y*exp(x)+2*x)/exp(x)', 'y*exp(x)+x**2', ((0.4, 0.5), (0.7, 0.3), (0.9, 0.8)))

if __name__ == '__main__':
    print(len(ODE), 'entries', 'bad:', verify())
