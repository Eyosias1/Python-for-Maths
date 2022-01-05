import numpy as np

from sympy import var, sin, cos, pi, pprint, together, apart, simplify, factor, expand, sqrt, Float, evalf, solve, Rational, plot, limit, oo, integrate, diff, log


var('x y z a')
"""
=================================================================
|                           Question 1                          |
=================================================================
"""
print("\n=============\n| Question 1|\n=============\n")

f = x*log(sqrt(x**2 + 3)) / sqrt(x**2 + 3)
u = log(sqrt(x**2 + 3))
print("u =" ,u)
v = integrate(dv)
print("v =", v)
dv = x / sqrt(x**2 + 3)
print("v' =" ,dv)
du = diff(u, x)
print("u' =" ,du)




#print(du)
dufoiV = du * v

val = u.subs(x, 1) * v.subs(x, 1)
val2 = u.subs(x, 0) * v.subs(x, 0)

newVal = val - val2
print("[u*v]1 et 0 =", newVal)


I = integrate(dufoiV, (x, 0, 1))
print("integrale u'*v =", I)

res  = newVal - I
print("resultat final = ", res)

