qtd_testes = int(input())

for i in range(qtd_testes):
    qtd_anos = int(input())
    if qtd_anos < 2015:
        ano = 2015 - qtd_anos
        dc = True
    else:
        ano = qtd_anos - 2014
        dc = False
    ano_str = str(ano)
    ano_str += ' '
    ano_str += 'D.C.' if dc else 'A.C.'
    print(ano_str)
