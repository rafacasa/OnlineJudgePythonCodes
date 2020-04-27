from math import log


def min(num):
    return num / log(num)


def max(num):
    return 1.25506 * min(num)


numero = int(input())
menor = min(numero)
maior = max(numero)

print('{:.1f} {:.1f}'.format(menor, maior))
