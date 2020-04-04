while True:
    n = int(input())

    if n == 0:
        break

    inicio = n if n % 2 == 0 else n + 1
    fim = inicio + 10

    s = 0
    for i in range(inicio, fim, 2):
        s += i
    print(s)
