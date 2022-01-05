

def fibo_liste(n):
    fiblist = []
    n1 = 0
    n2 = 1
    new  = 0
    i = 0
    if (n > 0):
        while ( i <= n):
            new = n1 + n2
            fiblist.append(n1)
            n1 = n2
            n2 = new
            i += 1
    return fiblist

a = fibo_liste(20)
#print(a)

def FiboRec(n):
    if (n >= 0):
        if (n == 0):
            return 0
        elif (n == 1):
            return 1
        else:
            return FiboRec(n - 1) + FiboRec(n - 2)
    else:
        return 0

def FibIt(n):
    n1 = 0
    n2 = 1
    new  = 0
    i = 0
    if (n > 0):
        while ( i < n):
            new = n1 + n2
            n1 = n2
            n2 = new
            i += 1
    return n1


#print(FibIt(19))

sum = 0
for i in range(1000001):
    if (i % 2 == 0):
        sum += 1

print(sum)
#print(sum % 100000007)