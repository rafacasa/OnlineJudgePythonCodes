dados = input().split()

a = int(dados[0])
b = int(dados[1])

if b > a:
    a, b = b, a

if a % b == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
