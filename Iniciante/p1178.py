n = []
x = float(input())
n.append(x)
print('N[0] = {:.4f}'.format(x))
for i in range(99):
    n.append(n[i]/2)
    print('N[{}] = {:.4f}'.format(i+1, n[-1]))
