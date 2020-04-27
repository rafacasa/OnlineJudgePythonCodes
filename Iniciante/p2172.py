while True:
    multi, xp = map(int, input().split())
    if multi == 0 and xp == 0:
        break
    print(multi * xp)
