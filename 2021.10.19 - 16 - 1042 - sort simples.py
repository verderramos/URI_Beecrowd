lista = list()
lista1 = list()
a, b, c = input().split()
lista.append(int(a))
lista.append(int(b))
lista.append(int(c))
for c in range(len(lista)):
    lista1.append((lista[c]))
lista.sort()
for c in range(len(lista)):
    print(lista[c])
print()
for c in range(len(lista1)):
    print(lista1[c])
