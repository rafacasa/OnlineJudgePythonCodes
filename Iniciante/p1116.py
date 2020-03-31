qtd = int(input())

for i in range(qtd):
    a, b = input().split()
    a = float(a)
    b = float(b)

    if b == 0:
        print('divisao impossivel')
    else:
        div = a / b
        print('{:.1f}'.format(div))
