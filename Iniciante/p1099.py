qtd = int(input())

for i in range(qtd):
    a, b = input().split()
    a = int(a)
    b = int(b)
    if b < a:
        b, a = a, b
    impares = [num for num in range(a+1, b) if num % 2 == 1]
    soma = sum(impares)
    print(soma)
