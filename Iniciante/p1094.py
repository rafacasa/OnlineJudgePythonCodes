n = int(input())

cobaias = {
    'coelho': 0,
    'rato': 0,
    'sapo': 0
}

for i in range(n):
    qtd, cobaia = input().split()
    qtd = int(qtd)
    if cobaia == 'C':
        cobaias['coelho'] += qtd
    elif cobaia == 'R':
        cobaias['rato'] += qtd
    else:  # S
        cobaias['sapo'] += qtd

total = sum([q for q in cobaias.values()])

percC = (cobaias['coelho'] / total) * 100
percR = (cobaias['rato'] / total) * 100
percS = (cobaias['sapo'] / total) * 100

print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(cobaias['coelho']))
print('Total de ratos: {}'.format(cobaias['rato']))
print('Total de sapos: {}'.format(cobaias['sapo']))
print('Percentual de coelhos: {:.2f} %'.format(percC))
print('Percentual de ratos: {:.2f} %'.format(percR))
print('Percentual de sapos: {:.2f} %'.format(percS))
