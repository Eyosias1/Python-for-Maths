import numpy as np
import matplotlib.pyplot as plt
import sympy as sm


"""
=================================================================
|                           Question 1                          |
=================================================================
"""
print("\n=============\n| Question 1|\n=============\n")
A = np.array([[6, 2, 8, 0], [3, 0, 1, 8], [7, 4, 0, 3], [2, 6, 7, 0]])
B = np.array([1, 2, 3, 4])
B = B.reshape(4, 1)
A1 = np.linalg.inv(A)
X = A1.dot(B)
print(X)

"""
=================================================================
|                           Question 2                          |
=================================================================
"""
print("\n=============\n| Question 2|\n=============\n")
A2 = np.copy(A)
X2 = np.linalg.solve(A2, B)
print(X2)


"""
=================================================================
|                           Question 3                          |
=================================================================
"""
print("\n=============\n| Question 3|\n=============\n")
x  = []
B = B.reshape(4, )
for i in range(len(A)):
    A3 = np.copy(A)
    A3[:, i] = B
    x = np.hstack((x, np.linalg.det(A3) / np.linalg.det(A)))
x = x.reshape(4, 1)

print(x)