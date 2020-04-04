import math
while True:
    entrada = input().split()
    if len(entrada) != 3:
        break

    a = int(entrada[0])
    b = int(entrada[1])
    c = int(entrada[2])

    area_casa = a * b

    porcentagem = c / 100
    area_terreno = area_casa / porcentagem

    lado_terreno = math.trunc(area_terreno ** 0.5)
    print(lado_terreno)


