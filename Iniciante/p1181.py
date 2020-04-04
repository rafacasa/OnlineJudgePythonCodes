linha = int(input())
operacao = input()

matriz = []

for i in range(12):
    linha_lida = []
    for j in range(12):
        linha_lida.append(float(input()))
    matriz.append(linha_lida)

if operacao == 'S':
    soma = sum(matriz[linha])
    print('{:.1f}'.format(soma))
elif operacao == 'M':
    media = sum(matriz[linha]) / 12
    print('{:.1f}'.format(media))
