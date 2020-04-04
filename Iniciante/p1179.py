par = []
impar = []
for i in range(15):
    num = int(input())
    if num % 2 == 0:
        par.append(num)
        if len(par) == 5:
            for j, v in enumerate(par):
                print('par[{}] = {}'.format(j, v))
            par = []
    else:
        impar.append(num)
        if len(impar) == 5:
            for j, v in enumerate(impar):
                print('impar[{}] = {}'.format(j, v))
            impar = []
for j, v in enumerate(impar):
    print('impar[{}] = {}'.format(j, v))
for j, v in enumerate(par):
    print('par[{}] = {}'.format(j, v))
