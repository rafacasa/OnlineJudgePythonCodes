qtd = int(input())

for i in range(qtd):
    hora, minuto, abriu = map(int, input().split())
    hora = str(hora).zfill(2)
    minuto = str(minuto).zfill(2)
    if abriu:
        print('{:s}:{:s} - A porta abriu!'.format(hora, minuto))
    else:
        print('{:s}:{:s} - A porta fechou!'.format(hora, minuto))
