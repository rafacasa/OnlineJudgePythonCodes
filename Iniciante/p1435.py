n = int(input())
while n > 0:
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(0)
        matriz.append(linha)

    meio = n // 2
    a = meio + 1

    matriz[meio][meio] = a

    esquerda = 0
    cima = 0
    direita = n - 1
    baixo = n - 1

    for valor in range(1, a):
        for posicao in range(esquerda, direita + 1):
            matriz[cima][posicao] = valor
            matriz[baixo][posicao] = valor

        for posicao in range(cima + 1, baixo):
            matriz[posicao][esquerda] = valor
            matriz[posicao][direita] = valor

        cima += 1
        esquerda += 1
        direita -= 1
        baixo -= 1

    for linha in matriz:
        string = ''
        for num in linha:
            string += '{:->3d} '.format(num)
        string = string.strip()
        string = string.replace('-', ' ')
        print(string)
    print()
    n = int(input())

