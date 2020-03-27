linha1 = input()
linha2 = input()

peca1 = linha1.split()
peca2 = linha2.split()

valorPeca1 = int(peca1[1]) * float(peca1[2])
valorPeca2 = int(peca2[1]) * float(peca2[2])

total = valorPeca1 + valorPeca2

print('VALOR A PAGAR: R$ {:.2f}'.format(total))
