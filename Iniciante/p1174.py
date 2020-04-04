x = []

for i in range(100):
    x.append(float(input()))

for i, v in enumerate(x):
    if v <= 10:
        print('A[{}] = {:.1f}'.format(i, v))
