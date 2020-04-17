while True:
    try:
        # Lê o tamanho da matriz
        tamanho = int(input())

        inicio_interna = tamanho // 3
        fim_interna = tamanho - inicio_interna

        # Cria a matriz e inicia com 1 na parte interna e 0 no resto (poder entrar em qualquer posicao com []
        matriz = []
        for i in range(tamanho):
            linha = []
            for j in range(tamanho):
                if inicio_interna <= i < fim_interna and inicio_interna <= j < fim_interna:
                    linha.append(1)
                else:
                    linha.append(0)
            matriz.append(linha)

        # Coloca o 4 no meio da matriz
        matriz[tamanho//2][tamanho//2] = 4

        for i in range(tamanho):
            for j in range(tamanho):
                if matriz[i][j] == 1 or matriz[i][j] == 4:
                    continue
                if i == j:
                    matriz[i][j] = 2
                    continue
                if i + j == tamanho-1:
                    matriz[i][j] = 3

        for linha in matriz:
            string = ''
            for num in linha:
                string += str(num)
            print(string)
        print()
    except EOFError:
        break
