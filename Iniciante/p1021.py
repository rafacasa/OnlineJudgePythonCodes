valor = float(input())

valor *= 100

n100 = valor // 10000
valor = valor % 10000
n50 = valor // 5000
valor = valor % 5000
n20 = valor // 2000
valor = valor % 2000
n10 = valor // 1000
valor = valor % 1000
n5 = valor // 500
valor = valor % 500
n2 = valor // 200
valor = valor % 200
m1 = valor // 100
valor = valor % 100
m50 = valor // 50
valor = valor % 50
m25 = valor // 25
valor = valor % 25
m10 = valor // 10
valor = valor % 10
m5 = valor // 5
m01 = valor % 5

print('NOTAS:')
print('{:.0f} nota(s) de R$ 100.00'.format(n100))
print('{:.0f} nota(s) de R$ 50.00'.format(n50))
print('{:.0f} nota(s) de R$ 20.00'.format(n20))
print('{:.0f} nota(s) de R$ 10.00'.format(n10))
print('{:.0f} nota(s) de R$ 5.00'.format(n5))
print('{:.0f} nota(s) de R$ 2.00'.format(n2))

print('MOEDAS:')
print('{:.0f} moeda(s) de R$ 1.00'.format(m1))
print('{:.0f} moeda(s) de R$ 0.50'.format(m50))
print('{:.0f} moeda(s) de R$ 0.25'.format(m25))
print('{:.0f} moeda(s) de R$ 0.10'.format(m10))
print('{:.0f} moeda(s) de R$ 0.05'.format(m5))
print('{:.0f} moeda(s) de R$ 0.01'.format(m01))
