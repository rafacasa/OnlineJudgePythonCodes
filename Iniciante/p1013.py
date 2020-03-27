dados = input().split()
a = int(dados[0])
b = int(dados[1])
c = int(dados[2])

maior = (a + b + abs(a - b)) / 2
maior = (c + maior + abs(c - maior)) / 2

print('{:.0f} eh o maior'.format(maior))
