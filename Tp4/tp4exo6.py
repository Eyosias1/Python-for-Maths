import numpy as np
import matplotlib.pyplot as plt


def getmidpoint(p1, p2):
    xmid = (p1[0] + p2[0]) / 2
    ymid = (p1[1] + p2[1]) / 2
    return [xmid, ymid]



def triangle2():
    p1 = [0, 0]
    p2 = [0.5, 1]
    p3 = [1, 0]
    p4 = [0, 0]
    plt.plot([p1[0], p2[0], p3[0], p4[0]], [p1[1], p2[1], p3[1], p4[1]])
    for i in range(10):
       p1 = getmidpoint(p1, p2)
       p2 = getmidpoint(p2, p3)
       p3 = getmidpoint(p3, p4)
       p4 = p1
       plt.plot([p1[0], p2[0], p3[0], p4[0]], [p1[1], p2[1], p3[1], p4[1]])
    plt.show()

triangle2()
