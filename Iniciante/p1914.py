qtd = int(input())

for i in range(qtd):
    j1, esc1, j2, esc2 = input().split()
    a, b = map(lambda n: int(n), input().split())
    if (a + b) % 2 == 0:
        if esc1 == 'PAR':
            print(j1)
        else:
            print(j2)
    else:
        if esc1 == 'PAR':
            print(j2)
        else:
            print(j1)


