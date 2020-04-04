qtd = int(input())
for temp in range(qtd):
    n = int(input())
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    if s == n:
        print('{} eh perfeito'.format(n))
    else:
        print('{} nao eh perfeito'.format(n))
