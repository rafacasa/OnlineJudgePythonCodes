p1 = input()
p2 = input()
p3 = input()

if p1 == 'vertebrado':
    if p2 == 'mamifero':
        if p3 == 'onivoro':
            print('homem')
        else:
            print('vaca')
    else:
        if p3 == 'onivoro':
            print('pomba')
        else:
            print('aguia')
else:
    if p2 == 'anelideo':
        if p3 == 'onivoro':
            print('minhoca')
        else:
            print('sanguessuga')
    else:
        if p3 == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
