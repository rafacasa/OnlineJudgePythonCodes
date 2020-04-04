x = []
for i in range(10):
    v = int(input())
    if v <= 0:
        valor = 1
    else:
        valor = v
    x.append(valor)

for i, v in enumerate(x):
    print('X[{}] = {}'.format(i, v))
