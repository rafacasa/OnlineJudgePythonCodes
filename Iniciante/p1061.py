diaInicio = input()
horarioInicio = input()
diaFim = input()
horarioFim = input()

diaInicio = int(diaInicio.split()[1])
diaFim = int(diaFim.split()[1])

horarioInicio = horarioInicio.split(':')
horaInicio = int(horarioInicio[0].strip())
minInicio = int(horarioInicio[1].strip())
segInicio = int(horarioInicio[2].strip())

horarioFim = horarioFim.split(':')
horaFim = int(horarioFim[0].strip())
minFim = int(horarioFim[1].strip())
segFim = int(horarioFim[2].strip())

totalSegIni = segInicio + (minInicio * 60) + (horaInicio * 3600) + (diaInicio * 86400)
totalSegFim = segFim + (minFim * 60) + (horaFim * 3600) + (diaFim * 86400)

total = totalSegFim - totalSegIni

dias = total // 86400
total %= 86400

horas = total // 3600
total %= 3600

minutos = total // 60

segundos = total % 60

print('{} dia(s)'.format(dias))
print('{} hora(s)'.format(horas))
print('{} minuto(s)'.format(minutos))
print('{} segundo(s)'.format(segundos))

