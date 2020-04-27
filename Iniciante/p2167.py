qtd = int(input())

lista = list(map(int, input().split()))
temp = 0
if qtd > 1:
    for i in range(1, qtd):
        if lista[i] < lista[i - 1]:
            temp = i + 1
            break

print(temp)
