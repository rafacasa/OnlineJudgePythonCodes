valor = int(input())

n100 = valor // 100
nvalor = valor - n100 * 100
n50 = nvalor // 50
nvalor = nvalor - n50 * 50
n20 = nvalor // 20
nvalor = nvalor - n20 * 20
n10 = nvalor // 10
nvalor = nvalor - n10 * 10
n5 = nvalor // 5
nvalor = nvalor - n5 * 5
n2 = nvalor // 2
n1 = nvalor - n2 * 2

print(valor)
print('{} nota(s) de R$ 100,00'.format(n100))
print('{} nota(s) de R$ 50,00'.format(n50))
print('{} nota(s) de R$ 20,00'.format(n20))
print('{} nota(s) de R$ 10,00'.format(n10))
print('{} nota(s) de R$ 5,00'.format(n5))
print('{} nota(s) de R$ 2,00'.format(n2))
print('{} nota(s) de R$ 1,00'.format(n1))