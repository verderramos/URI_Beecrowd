x = int(input())
for c in range(1, x+1):
    a, b = map(int, input().split())
    impares = list()
    while len(impares) < b:
        if a % 2 != 0:
            impares.append(a)
            a += 1
        else:
            a += 1
    print(sum(impares))
