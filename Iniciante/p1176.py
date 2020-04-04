fib = [0, 1]

for i in range(2, 61):
    fib.append(fib[i-1] + fib[i-2])

qtd = int(input())

for i in range(qtd):
    n = int(input())
    print('Fib({}) = {}'.format(n, fib[n]))
