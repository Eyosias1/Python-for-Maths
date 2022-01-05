import numpy as np

from sympy import var, sin, cos, pi, pprint, together, apart, simplify, factor, expand, sqrt, Float, evalf, solve, Rational, plot, limit, oo, integrate, diff, log


var('x y z a n')
"""
=================================================================
|                           Question 1                          |
=================================================================
"""
print("\n=============\n| Question 1|\n=============\n")

I = (x**(n - 1)) / (a + x)
vn = integrate(I, (x , 0, 1))
pprint(vn)
print("Le resulta n'est pas intelligible ")
"""
=================================================================
|                           Question 2                         |
=================================================================
"""
print("\n=============\n| Question 2|\n=============\n")
I = (x**(n-1)) / (a + x)
I = I.subs(n, 40)
vn = integrate(I, (x , 0, 1))
pprint(v40)
"""
=================================================================
|                           Question 3                         |
=================================================================
"""
print("\n=============\n| Question 3|\n=============\n")


I = (x**(n-1)) / (a + x)
I = I.subs(n, 40)
vn = integrate(I, (x , 0, 1))
vn = vn.subs(a, 3)
print("%0.20f "%vn.evalf(500))


print("en comparaison avec 0.006288571542029066 et %0.20f on trouve quelle est precise jusqu'a 10 chiffres apres la virgules "%vn.evalf(500))


