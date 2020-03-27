tempo = int(input())

horas = tempo // 3600
tempo = tempo % 3600

min = tempo // 60
seg = tempo % 60

print('{}:{}:{}'.format(horas, min, seg))
