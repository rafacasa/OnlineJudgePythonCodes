from sys import stdin


def main():
    qtd_estrelas = int(stdin.readline())

    estrela = list(map(int, stdin.readline().split()))
    i = 0
    estrelas_visitadas = set()

    while True:
        if not 0 <= i < qtd_estrelas:
            break

        qtd_carneiro = estrela[i]

        if qtd_carneiro > 0:
            estrela[i] -= 1

        estrelas_visitadas.add(i + 1)
        if qtd_carneiro % 2 == 0:
            i -= 1
        else:
            i += 1

    print(len(estrelas_visitadas), sum(estrela))


if __name__ == '__main__':
    main()
