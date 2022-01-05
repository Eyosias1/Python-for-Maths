def code_une(lt):
    alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(alp)):
        if (lt == alp[i]):
            return (i)
    return -1

def cesar(ph, dec):
    alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ph2 = ""
    for i in range(len(ph)):
        if (ph[i] == " "):
            ph2 += " "
        else:
            ph2 += alp[(code_une(ph[i]) + dec) % 26]
    return ph2


""" Question 2"""


def decesar(m, dec):
    alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ph = ""
    for i in range(len(m)):
        if (m[i] == " "):
            ph += " "
        else:
            ph += alp[(code_une(m[i]) - dec) % 26]
    return ph


ph = "YACINE"
print(cesar(ph, 1))
ph2 = "ZBDJOF"
print(decesar(ph2, 1))
phrase = "CE MESSAGE EST CONFIDENTIEL"
print(cesar(phrase,10))
phraseDecrypte = "MO WOCCKQO OCD MYXPSNOXDSOV"
print(decesar(phraseDecrypte, 10))


Decrypter = "KYV RIK FW GIFXIRDDZEX ZJ KYV RIK FW FIXREZQZEX TFDGCVOZKP"
for i in range(51):
    print(decesar(Decrypter, i))

""" la reponse est THE ART OF PROGRAMMING IS THE ART OF ORGANIZING COMPLEXITY"""