import math

qtd = int(input())

for i in range(qtd):
    # print('################')
    pa, pb, ga, gb = input().split()
    pa = int(pa)
    pb = int(pb)
    ga = float(ga)
    gb = float(gb)
    ga = ga / 100
    gb = gb / 100

    # print('pa={} - ga={:.1f} - pb={} - gb={:.1f}'.format(pa, ga, pb, gb))

    for temp in range(101):
        pa += math.trunc(pa * ga)
        pb += math.trunc(pb * gb)
        # print('pa={} - pb={}'.format(pa, pb))
        if pa > pb:
            break

    if temp + 1 < 101:
        print('{} anos.'.format(temp + 1))
    else:
        print('Mais de 1 seculo.')
