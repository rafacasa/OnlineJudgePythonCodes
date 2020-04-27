from datetime import datetime, timedelta

while True:
    try:
        dt = datetime.strptime(input(), '%H:%M')

        hora = timedelta(hours=1)
        dt2 = datetime.strptime('8:00', '%H:%M')
        dt = dt + hora
        atraso = dt - dt2
        if dt > dt2:
            print('Atraso maximo:', atraso.seconds // 60)
        else:
            print('Atraso maximo: 0')
    except EOFError:
        break
