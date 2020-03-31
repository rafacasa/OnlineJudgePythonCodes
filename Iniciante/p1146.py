n = int(input())

while n != 0:
    s = ''
    for i in range(1, n+1):
        s += str(i)
        s += ' '
    s = s.strip()
    print(s)
    n = int(input())
