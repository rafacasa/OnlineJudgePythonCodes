n, m = input().split()
n = int(n)
m = int(m)

while n > 0 and m > 0:
    if m < n:
        m, n = n, m

    seq = [i for i in range(n, m+1)]
    soma = sum(seq)
    seq2 = [str(i) for i in seq]
    saida = ' '.join(seq2)
    saida += ' Sum={}'.format(soma)

    print(saida)

    n, m = input().split()
    n = int(n)
    m = int(m)
