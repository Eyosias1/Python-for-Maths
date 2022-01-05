""" Question 1"""

def code_une(lt):
    alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    note = "not a valid char"
    for i in range(len(alp)):
        if (lt == alp[i]):
            return (i)
    return note
mt = "CESAR"
print(mt)
a = ""
for i in range(len(mt)):
    a += str(code_une(mt[i])) + " "

print(a)

""" question 2 """
def decode_une(c):
    alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(alp)):
        if (alp[c] == alp[i]):
            return alp[c]

print(decode_une(0))
print(decode_une(1))

""" Question 3"""

def code_mot(m):
    return list(map(code_une , m))

mot = "CESAR"
Listecode = (code_mot(mot))
print(Listecode)
 #Erreure
def decode_mot(L):
    mot = ""
    for i in range(len(L)):
        mot += decode_une(L[i])
    return mot
print(decode_mot(Listecode))
def decode_mot1(L):
    return "".join(list(map(decode_une, L)))

print(decode_mot1([2, 4, 18, 0, 17]))

