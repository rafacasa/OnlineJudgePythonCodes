par, j1, j2, roubou, acusou = map(int, input().split())

soma = j1 + j2

if roubou:
    if acusou:
        print('Jogador 2 ganha!')
    else:
        print('Jogador 1 ganha!')
else:
    if soma % 2 == 0:
        if par:
            print('Jogador 1 ganha!')
        else:
            print('Jogador 2 ganha!')
    else:
        if par:
            print('Jogador 2 ganha!')
        else:
            print('Jogador 1 ganha!')
