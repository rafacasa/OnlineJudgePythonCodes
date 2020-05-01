msg_original = input()

qtd_1 = len(msg_original.replace('0', ''))

if qtd_1 % 2 == 0:
    msg = msg_original + '0'
else:
    msg = msg_original + '1'

print(msg)
