for i in range(0, 21, 2):
    for j in range(1, 4):
        if i != 0 and i != 10 and i != 20:
            print('I={:.1f} J={:.1f}'.format(i/10, i/10 + j))
        else:
            print('I={:.0f} J={:.0f}'.format(i / 10, i / 10 + j))
