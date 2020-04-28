a = int(input())
b = int(input())
c = int(input())

print('A = {:d}, B = {:d}, C = {:d}'.format(a, b, c))
print('A = {: >10d}, B = {: >10d}, C = {: >10d}'.format(a, b, c))
print('A = {:s}, B = {:s}, C = {:s}'.format(str(a).zfill(10), str(b).zfill(10), str(c).zfill(10)))
print('A = {: <10d}, B = {: <10d}, C = {: <10d}'.format(a, b, c))


# 1234
# 12
# 123
