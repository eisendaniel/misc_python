import random


def per(n, c=0):
    if len(str(n)) == 1:
        if c > 4:
            print("MP = ", c)
        return
    c += 1
    product = 1
    for i in str(n):
        product *= int(i)
    per(product, c)


for i in range(0, 100):
    n = random.randint(1000000000, 2000000000)
