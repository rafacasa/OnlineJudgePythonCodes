preco = {
    '1001': 1.5,
    '1002': 2.5,
    '1003': 3.5,
    '1004': 4.5,
    '1005': 5.5,
}

qtd = int(input())

total = 0
for i in range(qtd):
    prod, qtd_com = input().split()
    qtd_com = int(qtd_com)
    total += qtd_com * preco[prod]

print('{:.2f}'.format(total))
