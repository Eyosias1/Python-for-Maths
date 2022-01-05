

def pgcd(a, b):
    re = 0
    if b == 0:
        return a
    while (b > 0):
        re = a % b
        a = b
        b = re
    return (a)

#print(pgcd(1, 1))

def phi(n):
    num = 1
    for i in range(2, n + 1):
        if (pgcd(i, n) == 1):
            num += 1
    return num

#print(phi(10))

#derniere question suffit de repeter phi(30) on cherche le nombre de fraction irreductibe
#Une fraction a / b est irréductible si a et b sont premiers entre eux.
#du coup comme on connait b il suffit de trouver a
# et la fonction phi trouve a et renvoie le nombre de fraction irreductible

#print(phi(30))

def farey(n):
    fn = 1
    somphi = 0
    if n > 1:
        for i in range(1, n + 1):
            somphi += phi(i)
    if (somphi == 0):
        somphi += 1
    fn += somphi
    return fn

#wikipedia dit pour calculer la somme de farey(n)
#il suffit de faire fn = 1 + sommedePhi(m) allant de 1 a m inclus

#for i in range(1, 4):
    print(farey(4))

#//////////////////////

def farey2(n):
    fn = 1
    count = n
    value = [0]
    x = farey(n)
    for i in range(1, x):
        if ( i == x - 1):
            value.append(1)
        elif (fn / count) > 1 / 2:
            fn += 1
            count = fn + 1
            value.append(fn / count)
        else:
            value.append(fn / count)
            count -= 1
    print(x, count, fn)
    return value

#print(farey2)

#print(farey2(4))


def farey3(n):
    print(0 ,"/",  1)
    for i in range(1, n + 1):
        for j in range(1, i):
            if (pgcd(i, j) == 1):
                print(j ,"/", i)
    print(1 ,"/", 1)

#for i in range(10, 30):
 #   farey3(i)















