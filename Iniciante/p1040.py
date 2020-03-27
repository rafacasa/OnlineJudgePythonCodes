dados = input().split()

a, b, c, d = dados

a = float(a)
b = float(b)
c = float(c)
d = float(d)

media = (2*a + 3*b + 4*c + d) / 10

print('Media: {:.1f}'.format(media))

if media >= 7:
    print('Aluno aprovado.')
elif media < 5:
    print('Aluno reprovado.')
else:
    notaExame = float(input())
    media = (media + notaExame) / 2
    print('Aluno em exame.')
    print('Nota do exame: {:.1f}'.format(notaExame))
    if media >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(media))
