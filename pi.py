from math import factorial


def gregleibpi(n):
    p = 4
    d = 3
    for i in range(1, n + 1):
        if i % 2 == 0:
            p += 4 / d
        else:
            p -= 4 / d
        d += 2
    return p


def nilakanthapi(n):
    p = 3
    d = 2
    for i in range(1, n + 1):
        if i % 2:
            p += 4 / (d * (d + 1) * (d + 2))
        else:
            p -= 4 / (d * (d + 1) * (d + 2))
        d += 2
    return p
