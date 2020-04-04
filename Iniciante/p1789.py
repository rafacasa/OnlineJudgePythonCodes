while True:
    try:
        n = int(input())
        lesmas = input().split()
        lesmas = map(lambda num: int(num), lesmas)
        lesmas = sorted(lesmas)
        rapida = lesmas[-1]
        if rapida >= 20:
            print('3')
        elif rapida >= 10:
            print('2')
        else:
            print('1')
    except EOFError:
        break
