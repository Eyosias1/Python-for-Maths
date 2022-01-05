import numpy as np
import matplotlib.pyplot as plt
""" Question 1 et 2 """
def pussance():
    x = np.linspace(0, 1, 200)
    range = np.arange(0.3, 2, 0.2)#on fait comme sa carrangefonctionneavecdesentier
    y = 0
    for i in range:
        y = x**i
        plt.plot(x, y, label = "t = %1.1f" %i)
    plt.legend(loc = 0)
    plt.title("Courbe de x puissance t")
    plt.show()

pussance()

""" Question 3 """
def pussance2():
    x = np.linspace(0, 1, 200)
    range = np.arange(0.4, 3, 0.01)
    y = 0
    k = 1
    for i in range:
        y = x**i
        #plt.plot(x, y, color = plt.cm.hsv(k))
        #plt.plot(x, y, color = plt.cm.hot(k))
        #plt.plot(x, y, color = plt.cm.jet(k))
        #plt.plot(x, y, color = plt.cm.winter(k))
        k += 1
    plt.title("Courbe de x puissance t")
    plt.show()

plt.figure()
pussance2()
