qtd_num = int(input())
lista_num = map(int, input().split())

multiplo_2 = 0
multiplo_3 = 0
multiplo_4 = 0
multiplo_5 = 0

for i in lista_num:
    if i % 2 == 0:
        multiplo_2 += 1
    if i % 3 == 0:
        multiplo_3 += 1
    if i % 4 == 0:
        multiplo_4 += 1
    if i % 5 == 0:
        multiplo_5 += 1

print('{:d} Multiplo(s) de 2'.format(multiplo_2))
print('{:d} Multiplo(s) de 3'.format(multiplo_3))
print('{:d} Multiplo(s) de 4'.format(multiplo_4))
print('{:d} Multiplo(s) de 5'.format(multiplo_5))
