import numpy as np

from sympy import var, sin, cos, pi, pprint, together, apart, simplify, factor, expand, sqrt, Float, evalf, solve, Rational, plot

var('x y z a b c h u v w')
"""
=================================================================
|                           Question 1                          |
=================================================================
"""


print("\n=============\n| Question 1|\n=============\n")

p  = a*x**2 + b*x + c

exp1 = p.subs(x, 0) - u


exp2 = p.subs(x, h/2) - v



exp3 = p.subs(x, h) - w

s = solve([exp1, exp2, exp3], [a, b, c])
print(s)

"""
=================================================================
|                           Question 2                          |
=================================================================
"""


print("\n=============\n| Question 2|\n=============\n")

p = p.subs(s)
print(p)

"""
=================================================================
|                           Question 3                          |
=================================================================
"""


print("\n=============\n| Question 3|\n=============\n")


#p = p.subs([u, v, w, h], [0, 2, 1, 2])
p = p.subs(u, 0)
p = p.subs(v, 2)
p = p.subs(w, 1)
p = p.subs(h, 2)


pprint(p)
plot(p, (x, 0, 2))
