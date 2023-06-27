from sys import stdin


def main():
    qtd_estrelas = int(stdin.readline())

    estrela = list(map(int, stdin.readline().split()))
    i = 0
    estrelas_visitadas = [False] * qtd_estrelas

    while 0 <= i < qtd_estrelas:
        qtd_carneiro = estrela[i]

        if qtd_carneiro > 0:
            estrela[i] -= 1

        estrelas_visitadas[i] = True
        if qtd_carneiro % 2 == 0:
            i -= 1
        else:
            i += 1

    soma = 0
    for es in estrelas_visitadas:
        if es:
            soma += 1

    print(soma, sum(estrela))


if __name__ == "__main__":
    main()
