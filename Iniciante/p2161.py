rep = int(input())

resp = 3
denom = 0

for i in range(rep):
    if denom:
        temp = 1 / denom
    else:
        temp = 0
    denom = temp + 6

if denom:
    resp = resp + (1 / denom)

print('{:.10f}'.format(resp))
