import numpy as np
import matplotlib.pyplot as plt
import sympy as sm


#def TapisSirpenski():






def MatAl(niveau):
    car = 3**niveau
    for i in range(niveau):
        if ( i == 0):
            A = np.zeros((1, 1), dtype = int)
        B = A
        C = np.zeros((3**i, 3**i), dtype = int)
        C += 1
        A = np.hstack((A, B))
        A = np.hstack((A, B))
        D = np.hstack((B, C))
        D = np.hstack((D, B))
        A = np.vstack((A, D))
        F = np.hstack((B, B))
        F = np.hstack((F, B))
        A = np.vstack((A, F))
    if niveau == 0:
        A = np.zeros((1, 1), dtype = int)
    plt.matshow(A, cmap='hot')


MatAl(4)

plt.show()

















    # A = np.zeros((1, 1), dtype = int)
    #A =      np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])
    #A = np.vstack((A, [0, 1, 0, 0, 1, 0, 0, 1, 0]))
    #A = np.vstack((A, [0, 0, 0, 0, 0, 0, 0, 0, 0]))
    #A = np.vstack((A, [0, 0, 0, 1, 1, 1, 0, 0, 0]))
    #A = np.vstack((A, [0, 1, 0, 1, 1, 1, 0, 1, 0]))
    #A = np.vstack((A, [0, 0, 0, 1, 1, 1, 0, 0, 0]))
    #A = np.vstack((A, [0, 0, 0, 0, 0, 0, 0, 0, 0]))
    #A = np.vstack((A, [0, 1, 0, 0, 1, 0, 0, 1, 0]))
    #A = np.vstack((A, [0, 0, 0, 0, 0, 0, 0, 0, 0]))

    # A =      np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    # A = np.vstack((A, [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]))
    # A = np.vstack((A, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    # A = np.vstack((A, [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0]))
    # A = np.vstack((A, [0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0]))
    # A = np.vstack((A, [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0]))
    # A = np.vstack((A, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    # A = np.vstack((A, [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]))
    # A = np.vstack((A, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    # A = np.vstack((A, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    # A = np.vstack((A, [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0]))
    # A = np.vstack((A, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    # A = np.vstack((A, [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0]))
    # A = np.vstack((A, [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0]))
    # A = np.vstack((A, [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0]))
    # A = np.vstack((A, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    # A = np.vstack((A, [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0]))
    # A = np.vstack((A, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    # A = np.vstack((A, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    # A = np.vstack((A, [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]))
    # A = np.vstack((A, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    # A = np.vstack((A, [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0]))
    # A = np.vstack((A, [0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0]))
    # A = np.vstack((A, [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0]))
    # A = np.vstack((A, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    # A = np.vstack((A, [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]))
    # A = np.vstack((A, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))





















