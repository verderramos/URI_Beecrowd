n = int(input())
for _ in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    if y == 0:
        print('divisao impossivel')
    else:
        print(f'{x/y:.1f}')