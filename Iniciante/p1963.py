antigo_valor, novo_valor = map(lambda f: float(f), input().split())

aumento = novo_valor - antigo_valor
porcentagem = (aumento * 100) / antigo_valor

print('{:.2f}%'.format(porcentagem))
