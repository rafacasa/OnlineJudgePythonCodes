from datetime import datetime

while True:
    try:
        mes, dia = map(int, input().split())

        data = datetime(day=dia, month=mes, year=2016)
        natal = datetime(day=25, month=12, year=2016)

        if data > natal:
            print('Ja passou!')
            continue

        if data == natal:
            print('E natal!')
            continue

        diferenca = natal - data

        dias = diferenca.days

        if dias == 1:
            print('E vespera de natal!')
        else:
            print('Faltam {:d} dias para o natal!'.format(dias))

    except EOFError:
        break

