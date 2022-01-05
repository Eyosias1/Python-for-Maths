import numpy as np

from sympy import var, sin, cos, pi, pprint, together, apart, simplify, factor, expand, sqrt, Float, evalf, solve, Rational, plot, limit, oo, integrate, diff, log

var('x y z a')
"""
=================================================================
|                           Question 1                          |
=================================================================
"""


print("\n=============\n| Question 1|\n=============\n")
lim = limit(sqrt(x**2 + x) - sqrt(x**2 + 1), x, oo)
print(lim)

lim = limit((1 + (a / (3*n))**(2*n)), n, oo)
print(lim)

"""
=================================================================
|                           Question 2                          |
=================================================================
"""


print("\n=============\n| Question 2|\n=============\n")

f = (x / (1 + sqrt(x)))
#pprint(f)
I = integrate(f, x)
#pprint(I)
d = diff(I, x)
pprint(factor(d))


g = 3*x*sqrt(1 + x**2)
I = integrate(g, x)
pprint("\n")
#pprint(I)
#print("\n")
d = diff(I, x)
pprint(factor(d))

H = sqrt(log(x)) / x
I = integrate(H, (x, 1, 2))
pprint(factor(I))












