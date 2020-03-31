while True:
    a, b = input().split()
    a = int(a)
    b = int(b)

    if a < b:
        print('Crescente')
    elif b < a:
        print('Decrescente')
    else:
        break
