x = int(input())
for c in range(x):
    a, b = map(int, input().split())
    impares = 0
    soma = 0
    while impares != b:
        if a % 2 == 0:
            a += 1
        else:
            soma += a
            impares += 1
            a += 1
    print(soma)
