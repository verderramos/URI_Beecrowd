a = int(input())
ddd = (61, 71, 11, 21, 32, 19, 27, 31)
cid = ('Brasilia', 'Salvador', 'Sao Paulo', 'Rio de Janeiro', 'Juiz de Fora', 'Campinas', 'Vitoria', 'Belo Horizonte')

if a not in ddd:
    print('DDD nao cadastrado')
else:
    x = ddd.index(a)
    print(f'{cid[x]}')
