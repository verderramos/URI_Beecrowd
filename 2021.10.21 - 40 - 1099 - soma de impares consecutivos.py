impar = 0
impares = list()
maior = 0
menor = 0
n = int(input())
for c in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    if x > y:
        maior = x
        menor = y
    else:
        maior = y
        menor = x
    for d in range(menor+1, maior):
        if d % 2 == 1:
            impar += d
    impares.append(impar)
    impar = 0
for f in range(len(impares)):
    print(impares[f])