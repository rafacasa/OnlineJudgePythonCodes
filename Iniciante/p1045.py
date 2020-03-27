dados = input().split()

dados = [float(dados[0]), float(dados[1]), float(dados[2])]
dados.sort(reverse=True)

a, b, c = dados

a2 = a ** 2
c2 = c ** 2
b2 = b ** 2

if a >= (b+c):
    print('NAO FORMA TRIANGULO')
else:
    if a2 == (b2 + c2):
        print('TRIANGULO RETANGULO')
    elif a2 > (b2 + c2):
        print('TRIANGULO OBTUSANGULO')
    else:
        print('TRIANGULO ACUTANGULO')

    if (a == b) and (b == c):
        print('TRIANGULO EQUILATERO')
    elif (a == b) or (b == c) or (a == c):
        print('TRIANGULO ISOSCELES')
