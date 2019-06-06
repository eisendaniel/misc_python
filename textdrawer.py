import random

i = 0
while (i < 1000):
    j = 0
    while (j < 1000):
        print("{}".format(random.randrange(2)), end="")
        j += 1
    print()
    i += 1
