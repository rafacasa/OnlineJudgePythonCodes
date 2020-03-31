n = int(input())

numeros = [i for i in range(1, 10001) if i % n == 2]

for num in numeros:
    print(num)
