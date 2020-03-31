qtdNumeros, qtdLinhas = input().split()

qtdNumeros = int(qtdNumeros)
qtdLinhas = int(qtdLinhas)

limites = [i+1 for i in range(1, qtdLinhas+1) if i == qtdLinhas or i % qtdNumeros == 0]

for i in limites:
    s = ''
    for j in range(i-qtdNumeros, i):
        s += str(j)
        s += ' '
    s = s.strip()
    print(s)
