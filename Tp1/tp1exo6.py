

def syracuse(n):
    len = 0
    while (n > 1):
        if (n % 2 == 0):
            n //= 2
        else:
            n = (n * 3) + 1
            n //= 2
        len += 1
    if (n == 1):
        len += 1
    return len

#print(syracuse(10))
#print(syracuse(100))

#for i in range(10, 26):
    print(syracuse(i))

max = 0
valeurMax = 0
for i in range(10 , 10000):
    if (max < syracuse(i)):
        max = syracuse(i)
        valeurMax = i

print(max)
print(valeurMax)