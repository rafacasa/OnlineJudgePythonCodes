n = []

for i in range(20):
    n.append(int(input()))

for i in range(10):
    n[i], n[19-i] = n[19-i], n[i]

for i, v in enumerate(n):
    print('N[{}] = {}'.format(i, v))
