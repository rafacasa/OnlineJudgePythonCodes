x1, y1, x2, y2 = [int(i) for i in input().split(" ")]
fazenda = 1

while x1 != 0 and y1 != 0 and x2 != 0 and y2 != 0:
    qtd_meteoros = int(input())
    qtd_acertos = 0

    for i in range(qtd_meteoros):
        x_met, y_met = [int(j) for j in input().strip().split(" ")]

        if x1 <= x_met <= x2 and y2 <= y_met <= y1:
            qtd_acertos += 1

    print(f"Teste {fazenda}")
    print(f"{qtd_acertos}")
    fazenda += 1
    x1, y1, x2, y2 = [int(i) for i in input().split(" ")]
