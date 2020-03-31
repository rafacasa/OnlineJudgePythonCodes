n = int(input())

tabuada = [n * i for i in range(1, 11)]

for ind, prod in enumerate(tabuada):
    print('{} x {} = {}'.format(ind+1, n, prod))
