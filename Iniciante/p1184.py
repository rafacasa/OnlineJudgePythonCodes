operacao = input()

matriz = []

for i in range(12):
    linha_lida = []
    for j in range(12):
        linha_lida.append(float(input()))
    matriz.append(linha_lida)

dados = []

for i, linha in enumerate(matriz):
    for j, num in enumerate(linha):
        if i + j > 11:
            dados.append(num)

resultado = 0
if operacao == 'S':
    resultado = sum(dados)
else:
    resultado = sum(dados) / len(dados)
print('{:.1f}'.format(resultado))
