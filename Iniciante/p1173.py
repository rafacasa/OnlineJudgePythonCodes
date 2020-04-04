n = int(input())
x = [n]

for i in range(1, 10):
    x.append(2 * x[i - 1])

for i, v in enumerate(x):
    print('N[{}] = {}'.format(i, v))
