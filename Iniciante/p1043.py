dados = input().split()

a, b, c = dados

a = float(a)
b = float(b)
c = float(c)

if a < b+c and b < a+c and c < a+b:
    prim = a + b + c
    print('Perimetro = {:.1f}'.format(prim))
else:
    area = ((a+b) * c) / 2
    print('Area = {:.1f}'.format(area))
