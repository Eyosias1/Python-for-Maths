import numpy as np
import matplotlib.pyplot as plt
import sympy as sm



"""
=================================================================
|                           Question 1                          |
=================================================================
"""
print("\n=============\n| Question 1|\n=============\n")
n = 100
x = np.linspace(-np.pi, np.pi, n)

L = []

for i in range(n):
    L = np.hstack((L, np.power(x , i)))

L = L.reshape(n, n)
L = L.T
print(L)


b = [np.sin(x[i]) for i in range(n)]
print(b, '\n')

a = np.linalg.solve(L, b)
print(a)
"""
=================================================================
|                           Question 2                          |
=================================================================
"""
print("\n=============\n| Question 2|\n=============\n")
t = np.linspace(-np.pi, np.pi, 250)
np.polyval(a[::-1], t)

plt.plot(x, b)
plt.plot(t, np.polyval(a[::-1], t))
plt.show()
