while True:
    try:
        n, id = [int(i) for i in input().split(" ")]
        qtd = 0

        for i in range(n):
            id_video, jogo = [int(j) for j in input().split(" ")]
            if id_video == id and jogo == 0:
                qtd += 1

        print(qtd)

    except EOFError:
        break
