n_coluna = int(input())
operacao = input()

matriz = []

for i in range(12):
    linha_lida = []
    for j in range(12):
        linha_lida.append(float(input()))
    matriz.append(linha_lida)

coluna = []

for linha in matriz:
    coluna.append(linha[n_coluna])

if operacao == 'S':
    soma = sum(coluna)
    print('{:.1f}'.format(soma))
elif operacao == 'M':
    media = sum(coluna) / 12
    print('{:.1f}'.format(media))
