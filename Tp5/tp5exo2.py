
import numpy as np

from sympy import var, sin, cos, pi, pprint, together, apart, simplify, factor, expand, sqrt, Float, evalf



def suite(n):
    xo = Float(0.23)
    for z in range(n):
        xo =  (4*(xo)*(1 - xo)).evalf(500)
    return xo

def suite1(x):
    yo = Float(0.23)
    for z in range(x):
        yo = (4*(yo) - 4*(yo*yo)).evalf(500)
    return yo

def suite2(n):
    xo = 0.23
    for z in range(n):
        xo =  (4*(xo)*(1 - xo))
    return xo

def suite3(x):
    yo = 0.23
    for z in range(x):
        yo = 4*(yo) - 4*(yo*yo)
    return yo

L = np.arange(10, 70, 10)
"""
=================================================================
|                           Question 0                          |
=================================================================
"""

print("\n=============\n| Question 0|\n=============\n")
for i in range(len(L)):
    print("%1.20f" %(suite(L[i])), "%1.20f" %suite1(L[i]))

print("\n On retrouve que avec les meme precission\n les deux formoules developper et non dev\n donnes excatement les meme resultat ")

"""
=================================================================
|                           Question 1                          |
=================================================================
"""

print("\n=============\n| Question 1|\n=============\n")
for i in range(len(L)):
    print("%1.20f" %(suite(L[i])), "%1.20f" %suite2(L[i]))
print("\n On trouve que avec la fonction avec precission\n et celle qui n a pas donne des resultat presque les \n meme au debut avec une legere difference \n et ensuite a u 60 c'est plus les meme resutat ")


"""
=================================================================
|                           Question 2                          |
=================================================================
"""

print("\n=============\n| Question 2|\n=============\n")
for i in range(len(L)):
    print("%1.20f" %(suite(L[i])), "%1.20f" %suite3(L[i]))
print("\n On trouve le meme cas dans\n cette question pour la \n fonction avec une formule devopper")





