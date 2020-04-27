qtd = 1
while qtd > 0:
    qtd = int(input())
    for i in range(qtd):
        pessoas = int(input())
        if pessoas % 2 == 0:
            pontas = 2
            meio = pessoas - 2
        else:
            pontas = 1
            meio = pessoas - 1

        pedidos = pontas + (meio * 2)
        print(pedidos)
