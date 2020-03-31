n = int(input())

seq = [0, 1]

if n == 1:
    print(0)
elif n == 2:
    print(0, 1)
else:
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])

    s = ''
    for i in seq:
        s += str(i)
        s += ' '

    s = s.strip()
    print(s)
