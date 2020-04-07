a, b = input().split()

a = int(a)
b = int(b)

for r in range(abs(b)):
    temp = (a - r) % b
    if temp == 0:
        break

q = (a - r) // b
print(q, r)
