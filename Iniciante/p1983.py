qtd_alunos = int(input())

maior_nota = 0
aluno_maior_nota = ''

for i in range(qtd_alunos):
    aluno, nota = input().split()
    nota = float(nota)

    if nota > maior_nota:
        maior_nota = nota
        aluno_maior_nota = aluno

if maior_nota >= 8:
    print(aluno_maior_nota)
else:
    print('Minimum note not reached')
