dados = input().split()

horaInicio = int(dados[0])
minutoInicio = int(dados[1])
horaFim = int(dados[2])
minutoFim = int(dados[3])

if horaInicio == horaFim and minutoInicio == minutoFim:
    horas = 24
    minutos = 0
elif (horaInicio > horaFim) or (horaInicio == horaFim and minutoInicio > minutoFim):
    inicio = minutoInicio + (horaInicio * 60)
    fim = minutoFim + (horaFim * 60)

    duracao = ((24*60) - inicio) + fim

    horas = duracao // 60
    minutos = duracao % 60
else:
    inicio = minutoInicio + (horaInicio * 60)
    fim = minutoFim + (horaFim * 60)

    duracao = fim - inicio

    horas = duracao // 60
    minutos = duracao % 60

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))
