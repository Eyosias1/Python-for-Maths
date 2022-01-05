from time import time

def harmonique(n):
    if (n == 0):
        return 0
    else:
        return harmonique(n -1) + 1 / (n)

print(harmonique(100))
print(harmonique(950))

#non on ne pwut pas faire plus de 1000 recursion car python limite

""" Question 2"""

def fibo_r(n):
    if n < 0:
        return 0
    if (n == 0):
        return 0
    if (n == 1 or n == 2):
        return (1)
    else:
        return (fibo_r(n - 1) + fibo_r(n - 2))
""" (a) """
#t_start = time()
#fibo_r(25)
#t_fin = time()
#print("Temps d'execution %.2f"% (t_fin-t_start), "sec.")

""" (b) """

def calculT():
    for i in range(25, 35):
        t_start = time()
        fibo_r(i)
        t_fin = time()
        print("temps d’execution %.2f" % (t_fin - t_start), "sec.")


calculT()




"""
on a trouver pour fibo(25) = 0.07 sec et fibo(26) = 0.10
le rapport de (0.09 / 0.07) = 1.3
on a trouver pour fibo(28) = 0.28 sec et fibo(27) = 0.16
le rapport de (0.28 / 0.16) = 1.7
on a trouver pour fibo(34) = 4.43 sec et fibo(33) = 2.77
le rapport de (4.43 / 2.77) = 1.6

ainsi on voit que pour trouver fibi(80) on fera 80 - 25 = 55 qui dit que
0.06*1.6^55 = 10109980000.18152
10109980000.18152 / 3600 = 2808327.7778282003
2808327.7778282003 / 24 = 117013.65740950835
117013.65740950835 / 365 = 320.5853627657763 ans

ainsi on voit que pour trouver fibi(80) on fera 120 - 25 = 95 qui dit que
0.06*1.6^95 = 1.4775752323648008e+18
1.4775752323648008e+18 / 3600 = 410437564545778.0
410437564545778.0 / 24 = 17101565189407.416
17101565189407.416 / 365 = 47504347748.353935 ans



"""