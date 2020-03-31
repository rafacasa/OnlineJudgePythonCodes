while True:

    notas = []

    while True:
        nota = float(input())
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print('nota invalida')

        if len(notas) == 2:
            break

    media = sum(notas) / 2

    print('media = {:.2f}'.format(media))
    x = 0
    while not 1 <= x <= 2:
        print('novo calculo (1-sim 2-nao)')
        x = int(input())
    if x == 2:
        break
