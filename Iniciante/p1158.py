qtd = int(input())

for temp in range(qtd):
    x, y = input().split()
    x = int(x)
    y = int(y)

    inicio = x if x % 2 == 1 else x + 1
    fim = inicio + y * 2

    soma = 0
    for i in range(inicio, fim, 2):
        soma += i
    print(soma)
