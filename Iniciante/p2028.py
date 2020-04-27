caso = 1
while True:
    try:
        num_n = int(input())

        numeros = ['0']

        for i in range(1, num_n + 1):
            for j in range(i):
                numeros.append(str(i))

        qtd_num = len(numeros)
        if qtd_num == 1:
            print('Caso {:d}: 1 numero'.format(caso))
        else:
            print('Caso {:d}: {:d} numeros'.format(caso, qtd_num))

        print(' '.join(numeros))
        print()
        caso += 1
    except EOFError:
        break

