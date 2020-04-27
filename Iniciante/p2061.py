abas, qtd = map(int, input().split())

for i in range(qtd):
    entrada = input()
    if entrada == 'fechou':
        abas += 1
    else:
        abas -= 1

print(abas)
