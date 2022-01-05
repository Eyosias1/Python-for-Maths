

def carre_plus(n):
    b = n*n + 2
    return b
    print("ceci ne s'affichea pas!'")

n = 5
#print(carre_plus(n))

#x = carre_plus(345) + carre_plus(567)
#print(x)

def racines(a, b, c):
    delta = b*b -4*(a)*c
    if (delta < 0):
        return 0
    elif (delta == 0):
        return 1
    else:
        return 2

a = 4
b = -12
c = 9
print(racines(a, b, c))
