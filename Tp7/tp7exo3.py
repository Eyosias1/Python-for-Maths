import numpy as np
import matplotlib.pyplot as plt
import sympy as sm


"""
=================================================================
|                           Question 1                          |
=================================================================
"""
print("\n=============\n| Question 1|\n=============\n")

def bern(a, b, p):
    r = np.random.rand()
    if (r  <= p):
        return b
    else:
        return a

print(bern(-1, 1, 0.6))

L = []


"""
=================================================================
|                           Question 2                          |
=================================================================
"""
print("\n=============\n| Question 2|\n=============\n")
for i in range(100):
    L.append(bern(-1, 1, 0.3))

plt.hist(L, bins = [-1, -0.5, 0.5, 1])
plt.show()