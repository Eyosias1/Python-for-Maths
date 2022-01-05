import numpy as np
import matplotlib.pyplot as plt
import sympy as sm

"""
=================================================================
|                           Question 1                          |
=================================================================
"""
print("\n=============\n| Question 1|\n=============\n")


L = np.random.randint(0, 2, 100)

print(L)

"""
=================================================================
|                           Question 2                          |
=================================================================
"""

print("\n=============\n| Question 2|\n=============\n")

def CnP(L):
    P = 0
    for i in range(len(L)):
        if L[i] == 1:
            P += 1
    return P

print(CnP(L))

"""
=================================================================
|                           Question 3                          |
=================================================================
"""

print("\n=============\n| Question 3|\n=============\n")



def Pf():
    jeu = 100
    ful = 0
    pil = 0
    L = np.random.randint(0, 2, jeu)
    pil = CnP(L)
    return [pil, L]

print(Pf())

exp = 20000

def countPb():
    sup = 0
    eg = 0
    for i in range(exp):
        Li = Pf()
        if Li[0] >= 53:
            sup += 1
        if Li[0] <= 40:
            eg += 1
        #plt.hist(Li[1], bins=[0.25, 0.5, 0.75, 1])
    #plt.show()
    return [sup, eg]
L = countPb()

print("\nProb (nombre pile > 53) = ", L[0] / exp, "\nProb (nombre pile <= 40) = ", L[1] / exp)


"""
=================================================================
|                           Question 4                          |
=================================================================
"""

print("\n=============\n| Question 4|\n=============\n")


















