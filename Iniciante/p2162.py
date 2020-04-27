qtd = int(input())
lista_medidas = list(map(int, input().split()))

certo = True

if qtd > 2:
    maior = lista_medidas[0] < lista_medidas[1]

    for i in range(2, qtd):
        if lista_medidas[i - 1] > lista_medidas[i]:
            if not maior:
                certo = False
                break
            maior = False
        elif lista_medidas[i - 1] < lista_medidas[i]:
            if maior:
                certo = False
                break
            maior = True
        else:
            certo = False
elif qtd == 2:
    certo = not lista_medidas[0] == lista_medidas[1]

if certo:
    print(1)
else:
    print(0)
