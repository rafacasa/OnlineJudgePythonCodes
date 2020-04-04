idades = []
idade = int(input())
while idade >= 0:
    idades.append(idade)
    idade = int(input())

media = sum(idades) / len(idades)
print('{:.2f}'.format(media))
