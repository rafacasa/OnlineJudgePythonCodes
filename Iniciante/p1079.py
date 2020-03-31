qtd = int(input())

for i in range(qtd):
    a, b, c = input().split()
    a = float(a)
    b = float(b)
    c = float(c)

    media = (2*a + 3*b + 5*c)/10

    print('{:.1f}'.format(media))
