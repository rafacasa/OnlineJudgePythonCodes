qtd = int(input())

for i in range(qtd):
    palavra = input()
    tamanho = len(palavra)
    tempo = tamanho / 100
    print('{:.2f}'.format(tempo))
