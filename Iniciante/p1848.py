soma = 0
pot = [4, 2, 1]
while True:
    try:
        linha = input()
        if linha == 'caw caw':
            print(soma)
            soma = 0
            continue
        for i, olho in enumerate(linha):
            if olho == '*':
                soma += pot[i]
    except EOFError:
        break
