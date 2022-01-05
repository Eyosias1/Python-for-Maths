
from sympy import var, sin, cos, pi, pprint, together, apart, simplify, factor, expand, sqrt

print("Question avant la premiere question\n")
var('x y z')
pprint(x + y + 2*x + z + 1)
"""
==============
| Question 1 |
==============
"""
p = (x - 1)*(x - 2)*(x + 3)
print("\n=============\n| Question 1|\n=============\n")
print(expand(p))

"""
==============
| Question 2 |
==============
"""

p = x**3 - 39*x + 70
print("\n=============\n| Question 2|\n=============\n")
pprint(factor(p))

"""
==============
| Question 3 |
==============
"""

p = (1 / (x + 1)) + (1 / y) + (1 / z)
print("\n=============\n| Question 3|\n=============\n")
pprint(together(p))

"""
==============
| Question 4 |
==============
"""

p = (2 * (x**2) + 4*x + 3) / ( (x**3) - 39*x - 70)
print("\n=============\n| Question 4|\n=============\n")
pprint(apart(p))

"""
=================================================================
|                           Question 5                          |
=================================================================
"""

p = cos(x + y) + cos(x - y) + sin(x + y) + sin(x - y)
print("\n=============\n| Question 5|\n=============\n")
pprint(simplify(p))

"""
=================================================================
|                           Question 6                          |
=================================================================
"""

p = 2 * (x**2) -3*x + 1
print("\n=============\n| Question 5|\n=============\n")
pprint(p.subs(x , 5))
pprint(p.subs(x, y + 1) - p.subs(x, y - 1))


"""
=================================================================
|                           Question 7                          |
=================================================================
"""

p = sqrt(10)
x = pi.evalf(10)
print("\n=============\n| Question 7|\n=============\n")
pprint(p.evalf())
pprint((x**2 + x + 1).evalf())










