while True:
    try:
        PI = 3.14
        volume_mel = float(input())
        diametro_cilindro = float(input())
        raio_cilindro = diametro_cilindro / 2

        area = (raio_cilindro ** 2) * PI
        altura = volume_mel / area

        print('ALTURA = {:.2f}'.format(altura))
        print('AREA = {:.2f}'.format(area))

    except EOFError:
        break
