import numpy as np
import matplotlib.pyplot as plt
import sympy as sm


"""
=================================================================
|                           Question  1                         |
=================================================================
"""
print("\n=============\n| Question 1|\n=============\n")

def bern(a, b, p):
    r = np.random.rand()
    if (r  <= p):
        return b
    else:
        return a

def marche(n):
    v = []
    for i in range(n):
        v.append(bern(-1, 1, 0.5))
    v = np.array(v)
    v = np.cumsum(v)
    return v

pas = 500
L = marche(pas)
y = np.linspace(0, pas, pas)
plt.plot(y, L)
plt.ylabel("0 to r")
plt.xlabel("left to right")
plt.title('Simuler et visualiser une marche au hasard')
plt.show()

plt.figure()
"""
=================================================================
|                           Question 2                          |
=================================================================
"""
print("\n=============\n| Question 2|\n=============\n")
def superposerGP(n):
    y = np.linspace(0, n, n)
    for i in range(n):
        L = marche(n)
        plt.plot(y, L)
    plt.ylabel("0 to r")
    plt.xlabel("gauche to droite")
    plt.title('Superposer dans un meme graphique')
    plt.show()

superposerGP(500)


plt.figure()
"""
=================================================================
|                           Question 3                          |
=================================================================
"""
print("\n=============\n| Question 3|\n=============\n")
nfoi = 20000
X100 = []
for i in range(nfoi):
    L = marche(100)
    X100.append(L[-1])


plt.hist(X100, bins = np.arange(-50, 50, 1),  color='black', linewidth = 2, density = True, stacked = True)
plt.show()

"""
=================================================================
|                           Question 4                          |
=================================================================
"""
print("\n=============\n| Question 5|\n=============\n")

ro = 10
def formula(x):
    return (1 / (ro * np.sqrt(2 * np.pi)) * np.exp(-x**2 / (2*ro**2)))
bel = [formula(i) for i in range(-50, 50)]
y = bel
x=np.arange(-50, 50, 1)
plt.plot(x, y)
plt.show()


# ce theooreme rappelle la loi biniomiale




