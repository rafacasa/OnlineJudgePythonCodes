n = []

t = int(input())
i = 0
while True:
    for j in range(t):
        n.append(j)
        print('N[{}] = {}'.format(i, j))
        i += 1
        if i == 1000:
            break
    if i == 1000:
        break
