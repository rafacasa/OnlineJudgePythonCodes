qtd = int(input())
for temp in range(qtd):
    n = int(input())
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    if s == 1:
        print('{} eh primo'.format(n))
    else:
        print('{} nao eh primo'.format(n))
