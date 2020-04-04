s = 1
for i in range(1, 20):
    a = 2*i+1
    b = 2**i
    s += a / b
print('{:.2f}'.format(s))
