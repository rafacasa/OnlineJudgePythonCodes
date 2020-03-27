dados = input().split()

qtd = int(dados[1])

if dados[0] == '1':
    valor = 4.00
elif dados[0] == '2':
    valor = 4.50
elif dados[0] == '3':
    valor = 5.00
elif dados[0] == '4':
    valor = 2.00
else:
    valor = 1.50

total = qtd * valor

print('Total: R$ {:.2f}'.format(total))
