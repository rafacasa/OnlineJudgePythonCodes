qtd = int(input())

for i in range(qtd):
    j1 = input()
    j2 = input()
    if j1 == 'ataque':
        if j2 == 'ataque':
            print('Aniquilacao mutua')
            continue
        else:
            print('Jogador 1 venceu')
            continue
    if j1 == 'pedra':
        if j2 == 'ataque':
            print('Jogador 2 venceu')
            continue
        if j2 == 'pedra':
            print('Sem ganhador')
            continue
        if j2 == 'papel':
            print('Jogador 1 venceu')
            continue
    if j1 == 'papel':
        if j2 == 'papel':
            print('Ambos venceram')
            continue
        else:
            print('Jogador 2 venceu')
            continue
