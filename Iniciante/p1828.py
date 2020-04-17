from enum import Enum


class Resposta(Enum):
    pedra = 'pedra'
    papel = 'papel'
    tesoura = 'tesoura'
    lagarto = 'lagarto'
    spock = 'Spock'


testes = int(input())

for i in range(testes):
    sheldon, raj = input().split()
    sheldon = Resposta(sheldon)
    raj = Resposta(raj)
    if sheldon == raj:
        print('Caso #{:d}: De novo!'.format(i + 1))
        continue
    if sheldon == Resposta.papel:
        if raj == Resposta.pedra or raj == Resposta.spock:
            print('Caso #{:d}: Bazinga!'.format(i + 1))
        else:
            print('Caso #{:d}: Raj trapaceou!'.format(i + 1))
        continue
    if sheldon == Resposta.pedra:
        if raj == Resposta.tesoura or raj == Resposta.lagarto:
            print('Caso #{:d}: Bazinga!'.format(i + 1))
        else:
            print('Caso #{:d}: Raj trapaceou!'.format(i + 1))
        continue
    if sheldon == Resposta.spock:
        if raj == Resposta.tesoura or raj == Resposta.pedra:
            print('Caso #{:d}: Bazinga!'.format(i + 1))
        else:
            print('Caso #{:d}: Raj trapaceou!'.format(i + 1))
        continue
    if sheldon == Resposta.lagarto:
        if raj == Resposta.papel or raj == Resposta.spock:
            print('Caso #{:d}: Bazinga!'.format(i + 1))
        else:
            print('Caso #{:d}: Raj trapaceou!'.format(i + 1))
        continue
    if sheldon == Resposta.tesoura:
        if raj == Resposta.papel or raj == Resposta.lagarto:
            print('Caso #{:d}: Bazinga!'.format(i + 1))
        else:
            print('Caso #{:d}: Raj trapaceou!'.format(i + 1))
        continue

