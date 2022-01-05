from math import factorial


L = [7,5,3,1]

def inverse(L):
    A = L[::-1]
    return A

print(L)
print(inverse(L))

def binaireRecusif(dec):
    if (dec >= 1):
        binaire(dec // 2)
    print(dec % 2, "\t")

def binaireIt(len, dec):
    x = []
    for i in range(len):
        dec //= 2
        x.append(dec % 2)
    return x

def dec(B):
    A = inverse(B)
    s = 0
    for n in range(len(A)):
        s += A[n]*2**n
    return s

print(dec([1,1,0,1]))

x = dec([1, 1, 0, 1, 1, 0, 0])
z = dec([1, 0, 1, 0, 1, 0, 1, 0])

print(x + z)

fact50 = factorial(50)
print(fact50)
fact50Str = str(fact50)
length = len(fact50Str)
print(length)
listebinaire = binaireIt(length, fact50)
print(listebinaire)













