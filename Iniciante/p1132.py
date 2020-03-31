a = int(input())
b = int(input())

if b < a:
    b, a = a, b

nao_multiplos_13 = [i for i in range(a, b+1) if i % 13 != 0]

print(sum(nao_multiplos_13))
