




def suite(n):
    xo = 0.23
    for z in range(n):
        xo =  4*(xo)*(1 - xo)
    return xo

n = 10
z = 60
value = suite(n)
value2 = suite(z)
print(value)
print(value2)

def suite2(x):
    yo = 0.23
    for z in range(x):
        yo = 4*(yo) - 4*(yo*yo)
    return yo


value = suite2(n)
value1 = suite2(z)
print(value)
print(value1)


# on n'obtient pas les memes resultat. je suppose qu'il vient de la precision de chaque ordinateur
# on ne peut pas choisir car les 2 sont mathematiquement juste du coup on ne peut pas determiner