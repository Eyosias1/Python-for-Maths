import numpy as np
import matplotlib.pyplot as plt


A = np.array([[1, 2] , [3, 4]])
B = np.array([[2, -1] , [2, 7]])
C = np.array([[1, 1, 1, 1] , [2, 2, 2, 2]])
x = np.array([[1] , [-2]])
y = np.array([3, 1, -0.5])
z = np.array([7, 7])
D = np.zeros((10, 20), dtype=int)
E = np.array([7, 7, 7, 7, 7, 7, 7])
I = np.diag([1, 1, 1, 1, 1, 1, 1, 1])

u = np.linspace(1, 100, 100, dtype=int)

L = np.diag(u)

v2 = np.linspace(2, 2, 100, dtype=int)
v1 = np.linspace(-1, -1, 99, dtype=int)

M = np.diag(v2)+np.diag(v1, -1)+np.diag(v1, 1)

print(A + B)
print('\n')
print(A.dot(B))
print('\n')
G = A*B
print(G)
print('\n')
print(A.dot(C))
print('\n')
print(A.dot(x))
print('\n')
print(10 *C)
print('\n')
print(z.dot(C))
print('\n')
print(x + z)
print('\n')
print(np.vdot(x, z))
print('\n')
A = A - np.array([[0, 0] , [0, 4]])
print(A)
C[1][0] = 4
C[1][1] = 3
C[1][2] = 2
C[1][3] = 1
#C = C + np.array([[3, 2, 1, 0], [0, 0, 0, 0]]) deuxieme methode
print('\n', C)
F = np.array([[C[0][0], C[1][0]], [C[0][1], C[1][0]]] )
F = F.T
print('\n', F)
print('\n', np.linalg.matrix_power(A, 10))

