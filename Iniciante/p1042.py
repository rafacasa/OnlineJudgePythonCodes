entrada = input()

dados = entrada.split()

dadosOrdem = dados.copy()
dadosOrdem.sort(key=lambda i: int(i))

print(dadosOrdem[0])
print(dadosOrdem[1])
print(dadosOrdem[2])
print()
print(dados[0])
print(dados[1])
print(dados[2])
