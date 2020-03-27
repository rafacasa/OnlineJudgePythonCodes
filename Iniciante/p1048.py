from builtins import print

salario = float(input())

if salario <= 400:
    perc = 0.15
elif salario <= 800:
    perc = 0.12
elif salario <= 1200:
    perc = 0.1
elif salario <= 2000:
    perc = 0.07
else:
    perc = 0.04

reaj = salario * perc
salario += reaj

print('Novo salario: {:.2f}'.format(salario))
print('Reajuste ganho: {:.2f}'.format(reaj))
print('Em percentual: {:.0f} %'.format(perc*100))
