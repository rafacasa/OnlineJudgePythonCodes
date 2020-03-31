r = 0

bd = {
    1: 0,
    2: 0,
    3: 0
}

while r != 4:
    r = int(input())

    try:
        bd[r] += 1
    except KeyError:
        pass

print('MUITO OBRIGADO')
print('Alcool: {}'.format(bd[1]))
print('Gasolina: {}'.format(bd[2]))
print('Diesel: {}'.format(bd[3]))
