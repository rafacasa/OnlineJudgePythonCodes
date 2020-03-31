a, *_, n = input().split()

a = int(a)
n = int(n)

soma = sum([a + i for i in range(n)])

print(soma)
