num = input().split()
num = map(lambda n: int(n), num)
num = sorted(num)

if num[0] + num[1] > num[2]:
    print('S')
elif num[1] + num[2] > num[3]:
    print('S')
else:
    print('N')
