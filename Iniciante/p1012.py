dados = input().split()
a = float(dados[0])
b = float(dados[1])
c = float(dados[2])

triangulo = (a * c) / 2
quadrado = b ** 2
retangulo = a * b
circulo = (c ** 2) * 3.14159
trapezio = ((a + b) * c) / 2

print('TRIANGULO: {:.3f}'.format(triangulo))
print('CIRCULO: {:.3f}'.format(circulo))
print('TRAPEZIO: {:.3f}'.format(trapezio))
print('QUADRADO: {:.3f}'.format(quadrado))
print('RETANGULO: {:.3f}'.format(retangulo))
