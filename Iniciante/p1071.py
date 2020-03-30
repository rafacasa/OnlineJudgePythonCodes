a = int(input())
b = int(input())

if b < a:
    b, a = a, b

soma = sum([i for i in range(a+1, b) if i % 2 == 1])

print(soma)
