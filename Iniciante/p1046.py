dados = input().split()

inicio = int(dados[0])
fim = int(dados[1])

if inicio == fim:
    duracao = 24
elif inicio > fim:
    duracao = (24 - inicio) + fim
else:
    duracao = fim - inicio

print('O JOGO DUROU {} HORA(S)'.format(duracao))
