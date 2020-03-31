repete = 1
inter = 0
gremio = 0
empate = 0


while repete == 1:
    placarInter, placarGremio = input().split()
    placarGremio = int(placarGremio)
    placarInter = int(placarInter)

    if placarInter == placarGremio:
        empate += 1
    elif placarInter > placarGremio:
        inter += 1
    else:
        gremio += 1

    print('Novo grenal (1-sim 2-nao)')
    repete = int(input())

total = inter + gremio + empate

print('{} grenais'.format(total))
print('Inter:{}'.format(inter))
print('Gremio:{}'.format(gremio))
print('Empates:{}'.format(empate))

if inter > gremio:
    print('Inter venceu mais')
elif gremio > inter:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')

