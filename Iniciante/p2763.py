dados = input().split('.')
temp = dados[-1]
dados.remove(temp)
dados.extend(temp.split('-'))
for i in dados:
    print(i)
