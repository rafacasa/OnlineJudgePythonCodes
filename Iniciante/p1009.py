nome = input()
salBase = float(input())
vendas = float(input())

comissao = 0.15 * vendas

salario = salBase + comissao

print('TOTAL = R$ {:.2f}'.format(salario))
