a, b, c = map(lambda i: int(i), input().split())

if b > a:
    if c <= b:
        print(':(')
    else:
        diff1 = b - a
        diff2 = c - b
        if diff2 >= diff1:
            print(':)')
        else:
            print(':(')
elif a > b:
    if c >= b:
        print(':)')
    else:
        diff1 = a - b
        diff2 = b - c
        if diff2 < diff1:
            print(':)')
        else:
            print(':(')
else:
    if c > b:
        print(':)')
    else:
        print(':(')
