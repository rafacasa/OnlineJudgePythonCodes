n = int(input())
while n > 0:
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(0)
        matriz.append(linha)

    temp = 1
    for i in range(n):
        matriz[0][i] = temp
        temp *= 2

    for j in range(n):
        temp = matriz[0][j] * 2
        for i in range(1, n):
            matriz[i][j] = temp
            temp *= 2

    for linha in matriz:
        string = ''
        for num in linha:
            if n < 3:
                string += '{:->1d} '.format(num)
            elif n < 5:
                string += '{:->2d} '.format(num)
            elif n < 6:
                string += '{:->3d} '.format(num)
            elif n < 8:
                string += '{:->4d} '.format(num)
            elif n < 10:
                string += '{:->5d} '.format(num)
            elif n < 11:
                string += '{:->6d} '.format(num)
            elif n < 13:
                string += '{:->7d} '.format(num)
            elif n < 15:
                string += '{:->8d} '.format(num)
            else:
                string += '{:->9d} '.format(num)

        string = string.strip()
        string = string.replace('-', ' ')
        print(string)
    print()
    n = int(input())
