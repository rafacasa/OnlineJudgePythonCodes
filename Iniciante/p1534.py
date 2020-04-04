while True:
    try:
        n = int(input())
        matriz = []
        for i in range(n):
            linha = []
            for j in range(n):
                linha.append(0)
            matriz.append(linha)

        pos1 = 0
        pos2 = n - 1

        for c in range(n):
            for i in range(n):
                if i == pos2:
                    matriz[c][i] = 2
                elif i == pos1:
                    matriz[c][i] = 1
                else:
                    matriz[c][i] = 3
            pos1 += 1
            pos2 -= 1

        for linha in matriz:
            string = ''
            for num in linha:
                string += '{}'.format(num)
            string = string.strip()
            print(string)

    except EOFError:
        break
