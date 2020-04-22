altura_salto, qtd_canos = map(lambda i: int(i), input().split())
altura_canos = list(map(lambda i: int(i), input().split()))
ganhou = True

for i in range(qtd_canos - 1):
    diff = abs(altura_canos[i + 1] - altura_canos[i])
    if diff > altura_salto:
        print('GAME OVER')
        ganhou = False
        break

if ganhou:
    print('YOU WIN')
