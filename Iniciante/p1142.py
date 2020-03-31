qtd = int(input())

for i in range(1, qtd + 1):
    temp = i * 4
    a, b, c = list(range(temp - 3, temp))
    print('{} {} {} PUM'.format(a, b, c))
