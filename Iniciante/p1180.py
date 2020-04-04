n = int(input())
lista = input().split()

lista = list(map(lambda i: int(i), lista))

menor = min(lista)
ind = lista.index(menor)

print('Menor valor: {}'.format(menor))
print('Posicao: {}'.format(ind))
