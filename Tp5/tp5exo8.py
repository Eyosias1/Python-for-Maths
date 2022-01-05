import numpy as np

from sympy import var, sin, cos, pi, pprint, together, apart, simplify, factor, expand, sqrt, Float, evalf, solve, Rational, plot, limit, oo, integrate, diff, log,plot


var('x y z a n')
"""
=================================================================
|                           Question 1                          |
=================================================================
"""
print("\n=============\n| Question 1|\n=============\n")


f = 1 / 2 *x**2 + x - 1
pprint(diff(f, x))

y = diff(f, x).subs(x, 2) * (x - 2) + f.subs(x, 2)
print(y)


plot(f, y, (x, -4, 4))
