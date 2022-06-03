x = int(input())
lista = list()
for c in range(x):
    z = int(input())
    if z == 0:
        lista.append('NULL')
    if z > 0:
        if z % 2 == 0:
            lista.append('EVEN POSITIVE')
        else:
            lista.append('ODD POSITIVE')
    if z < 0:
        if z % 2 == 0:
            lista.append('EVEN NEGATIVE')
        else:
            lista.append('ODD NEGATIVE')
for c in range(len(lista)):
    print(lista[c])
