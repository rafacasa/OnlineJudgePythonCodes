import struct
a, b = map(float, input().split())
c, d = map(float, input().split())
a = struct.unpack('f', struct.pack('f', a))[0]
b = struct.unpack('f', struct.pack('f', b))[0]

print('A = {:f}, B = {:f}'.format(a, b))
print('C = {:f}, D = {:f}'.format(c, d))
print('A = {:.1f}, B = {:.1f}'.format(round(a, 1), round(b, 1)))
print('C = {:.1f}, D = {:.1f}'.format(round(c, 1), round(d, 1)))
print('A = {:.2f}, B = {:.2f}'.format(round(a, 2), round(b, 2)))
print('C = {:.2f}, D = {:.2f}'.format(round(c, 2), round(d, 2)))
print('A = {:.3f}, B = {:.3f}'.format(round(a, 3), round(b, 3)))
print('C = {:.3f}, D = {:.3f}'.format(round(c, 3), round(d, 3)))
print('A = {:.3e}, B = {:.3e}'.format(round(a, 3), round(b, 3)).replace('e', 'E'))
print('C = {:.3e}, D = {:.3e}'.format(round(c, 3), round(d, 3)).replace('e', 'E'))
print('A = {:.0f}, B = {:.0f}'.format(a, b))
print('C = {:.0f}, D = {:.0f}'.format(c, d))
