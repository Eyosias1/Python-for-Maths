
def div(b):
    sum = 0
    for n in range(b):
        if (n%3 == 0 or n%5 == 0):
            sum += n
    return sum

print(div(1000))

print(div(2000) + div(3000))