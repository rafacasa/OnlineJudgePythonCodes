import struct
a, b, c, *d = input().split(' ')
b = float(b)
b = struct.unpack('f', struct.pack('f', b))[0]
d = ' '.join(d)
print('{:s}{:f}{:s}{:s}'.format(a, b, c, d))
print('{:s}\t{:f}\t{:s}\t{:s}'.format(a, b, c, d))
print('{: >10s}{: >10f}{: >10s}{: >10s}'.format(a, b, c, d))
