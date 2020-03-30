p = 0
s = 0
for i in range(6):
    n = float(input())
    if n > 0:
        p += 1
        s += n

print('{} valores positivos'.format(p))
media = s/p
print('{:.1f}'.format(media))
