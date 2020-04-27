hora_saida, tempo_viagem, fuso_destino = map(int, input().split())

hora_chegada = hora_saida + tempo_viagem + fuso_destino

if hora_chegada > 23:
    hora_chegada -= 24

if hora_chegada < 0:
    hora_chegada += 24

print(hora_chegada)
