x = 1
while x != 0:
    x = int(input())
    if x == 0:
        break
    pares = 0
    soma = 0
    while pares != 5:
        if x % 2 == 0:
            pares += 1
            soma += x
            x = x + 1
        else:
            x = x + 1
    print(soma)