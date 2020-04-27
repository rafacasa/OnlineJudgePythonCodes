from math import sqrt


def fib(num):
    r5 = sqrt(5)
    p1 = ((1 + r5) / 2) ** num
    p2 = ((1 - r5) / 2) ** num
    return (p1 - p2) / r5


ent = int(input())
print('{:.1f}'.format(fib(ent)))
