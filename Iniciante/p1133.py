a = int(input())
b = int(input())

if b < a:
    b, a = a, b

exibir = [i for i in range(a+1, b) if i % 5 == 2 or i % 5 == 3]

for i in exibir:
    print(i)
