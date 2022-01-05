

import numpy as np

from sympy import var, sin, cos, pi, pprint, together, apart, simplify, factor, expand, sqrt, Float, evalf, solve, Rational

var('x y z')

"""
=================================================================
|                           Question 1                          |
=================================================================
"""


print("\n=============\n| Question 1|\n=============\n")
p = ( 3 * (x**3)) - ( (7 * (x**2) ) / 2) - (x / 2) + 1
s = solve(p, x)
pprint(p)
print("\nles solution de cette equation sont\n")
pprint(s)
print("\non verifiant avec subs si on trouve 0 c'est que c'est bon\n")
pprint(p.subs(x, Rational(2 , 3)))


"""
=================================================================
|                           Question 2                          |
=================================================================
"""
print("\n=============\n| Question 2|\n=============\n")
expr1 = 0*x +  2*y + 5*z -3
expr2 = -3*x + 2*y -1*z +1
expr3 = -1*x + 2*y + 2*z -5

s = solve([expr1, expr2, expr3], [x, y, z])
print(s[x], s[y], s[z])

