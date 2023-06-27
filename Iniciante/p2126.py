caso = 1

while True:
    try:
        num1 = input()
        num2 = input()

        tam_num1 = len(num1)
        tam_num2 = len(num2)

        qtd = 0
        inicio = 0

        for i in range(tam_num2 - (tam_num1 - 1)):
            if num2[i : i + tam_num1] == num1:
                qtd += 1
                inicio = i + 1

        print(f"Caso #{caso}:")
        if qtd == 0:
            print("Nao existe subsequencia")
        else:
            print(f"Qtd.Subsequencias: {qtd}")
            print(f"Pos: {inicio}")

        print()
        caso += 1

    except EOFError:
        break
