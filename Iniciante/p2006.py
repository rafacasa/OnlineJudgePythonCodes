certo = int(input())

chutes = map(int, input().split())

acertos = 0

for chute in chutes:
    if chute == certo:
        acertos += 1

print(acertos)
