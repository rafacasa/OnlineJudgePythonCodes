centenas = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
dezenas = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
unidades = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

numero_string = input()
numero_original = int(numero_string)

if numero_original >= 100:
    c = numero_string[0]
    d = numero_string[1]
    u = numero_string[2]
elif numero_original >= 10:
    c = '0'
    d = numero_string[0]
    u = numero_string[1]
else:
    c = '0'
    d = '0'
    u = numero_string[0]

romano = ''
romano += centenas[int(c)]
romano += dezenas[int(d)]
romano += unidades[int(u)]

print(romano)
