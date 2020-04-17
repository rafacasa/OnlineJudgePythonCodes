n = float(input())
s = '{:.4e}'.format(n).replace('e', 'E')
if s[0] == '-':
    print(s)
else:
    print('+' + s)
