p = 0
i = 0
po = 0
n = 0
for a in range(5):
    b = int(input())
    if b % 2 == 0:
        p += 1
    else:
        i += 1

    if b > 0:
        po += 1
    if b < 0:
        n += 1

print('{} valor(es) par(es)'.format(p))
print('{} valor(es) impar(es)'.format(i))
print('{} valor(es) positivo(s)'.format(po))
print('{} valor(es) negativo(s)'.format(n))
