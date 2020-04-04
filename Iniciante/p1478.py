n = int(input())
while n > 0:
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(0)
        matriz.append(linha)

    cima = 0
    esquerdo = 0

    for temp in range(n):
        b = 1
        for i in range(esquerdo, n):
            matriz[cima][i] = b
            b += 1

        b = 2
        for i in range(cima + 1, n):
            matriz[i][esquerdo] = b
            b += 1

        cima += 1
        esquerdo += 1

    for linha in matriz:
        string = ''
        for num in linha:
            string += '{:->3d} '.format(num)
        string = string.strip()
        string = string.replace('-', ' ')
        print(string)
    print()
    n = int(input())
