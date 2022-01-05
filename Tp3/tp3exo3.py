def pgcd(a, b):
    re = 0
    if b == 0:
        return a
    while (b > 0):
        re = a % b
        a = b
        b = re
    return (a)

""" Question 1"""
l = []
for i in range(26):
    if pgcd(i, 26) == 1:
        l.append(i)
print(l)

""" Question 2"""





def code_une(lt):
    alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    note = "not a valid char"
    for i in range(len(alp)):
        if (lt == alp[i]):
            return (i)
    return note

def decode_mot(L):
    mot = ""
    for i in range(len(L)):
        mot += decode_une(L[i])
    return mot

def decode_une(c):
    alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(alp)):
        if (alp[c] == alp[i]):
            return alp[c]

def affine(mot, a, b):
    L = []
    for i in range(len(mot)):
        L.append(code_une(mot[i]))
    for i in range(len(L)):
        L[i] = (L[i]*a + b) % 26
    mot = decode_mot(L)
    return mot


mot = "CONFIDENTIEL"

mot = affine(mot, 5, 7)
print(mot)
""" Question 3"""
def inverse(a):
    for i in range(26):
        if ((a * i ) % 26 == 1):
            return i
    return 0

#for i in range(26):
 #   if (inverse(i) == 0):
  #      print(i,"* x n'est pas inversible avec modulo 26")


""" Question 4"""

def de_affine(mot, a, b):
    L = []
    c = inverse(a)
    for i in range(len(mot)):
        L.append(code_une(mot[i]))
    for i in range(len(L)):
        L[i] = (c * (L[i] - b)) % 26
    text = decode_mot(L)
    return text

""" Question """
mot = de_affine(mot, 5, 7)
print(mot)

""" facultatif """

def affinePh(mot, a, b):
    c = ""
    tmp = ""
    for i in range(len(mot)):
        if (mot[i] != " "):
            tmp += mot[i]
        else:
            tmp = affine(tmp, a, b)
            print(tmp)
            c += tmp
            c += " "
            tmp = ""
    c += affine(tmp, a, b)
    return c


def DEaffinePh(mot, a, b):
    c = ""
    tmp = ""
    for i in range(len(mot)):
        if (mot[i] != " "):
            tmp += mot[i]
        else:
            tmp = de_affine(tmp, a, b)
            c += tmp
            c += " "
            tmp = ""
    c += de_affine(tmp, a, b)
    return c


mot = "CONFIDENTIEL YACINE"
mot = affinePh(mot, 5, 7)
mot = DEaffinePh(mot, 5, 7)



""" Question 6 """

mot = "KYBIX"

#for a in range(10):
 #    for b in range(10):
  #       if a % 2 != 0:
           # print(DEaffinePh(mot, a, b))
""" la reponse est BRAVO """

""" QUESTION 7 """

mot = "LP NVP UJVR YCJAVXRJUR L PRG AP QH LJFYCPIPURXJU"

for i in range(173):
    print(DEaffinePh(mot, a, i))














