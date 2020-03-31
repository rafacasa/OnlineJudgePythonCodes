lista = []

for i in range(100):
    numero = int(input())
    lista.append(numero)

maximo = max(lista)
indice = lista.index(maximo) + 1

print(maximo)
print(indice)
