import numpy as np

def suiteIn(n):
    if n > 0:
        if n == 1:
            return np.log((1 + 3) / 3)
        else:
            return 1 / (n - 1) - 3*suiteIn(n - 1)
#version iterative
def suiteIn2(n, a):
    vn = np.log((1 + a) / a)
    for x in range(2, n + 1):
        vn = (1 / (x - 1)) - 3*vn
    return vn
a = 3
for n in range(1, 41):
   print("at n=",n,"v=", suiteIn2(n, a))

moyenne = ((1 / (60*(a + 1))) + (1/ (60 * a))) / 2
#print(moyenne)

def suitedown(n, a):
    vn = moyenne
    for x in range(60, n , -1):#la borne est n pas n - 1 car sinon on calcule 39 a la place de 40
        vn = (vn - (1 / (x - 1))) / (-a)
    return vn

print("\n")

for n in range(60, 39, -1):
    print("at n=",n,", v=",suitedown(n, a))