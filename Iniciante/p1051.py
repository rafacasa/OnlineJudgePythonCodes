salario = float(input())

ir = 0

if salario <= 2000:
    print('Isento')
else:
    if salario <= 3000:
        ir = (salario - 2000) * 0.08
    else:
        ir = 1000 * 0.08
        if salario <= 4500:
            ir += (salario - 3000) * 0.18
        else:
            ir += 1500 * 0.18
            ir += (salario - 4500) * 0.28
    print('R$ {:.2f}'.format(ir))
