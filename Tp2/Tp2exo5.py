
def pgcd(a, b):
    re = 0
    if b == 0:
        return a
    while (b > 0):
        re = a % b
        a = b
        b = re
    return (a)

print(pgcd(495, 275))
print(pgcd(10, 2))

