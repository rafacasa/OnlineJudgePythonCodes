x = int(input())
z = -99999999
while z <= x:
    z = int(input())

soma = x
qtd = 1

while True:
    if soma > z:
        break
    else:
        soma += x + qtd
        qtd += 1

print(qtd)
