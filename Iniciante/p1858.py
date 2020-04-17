qtd = input()
lista = list(map(lambda i: int(i), input().split()))
indice = lista.index(min(lista))
print(indice + 1)
