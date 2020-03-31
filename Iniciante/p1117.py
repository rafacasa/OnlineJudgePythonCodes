notas = []

while True:
    nota = float(input())
    if 0 <= nota <= 10:
        notas.append(nota)
    else:
        print('nota invalida')

    if len(notas) == 2:
        break

media = sum(notas) / 2

print('media = {:.2f}'.format(media))
