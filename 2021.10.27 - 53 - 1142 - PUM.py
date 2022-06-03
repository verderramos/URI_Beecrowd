x = int(input())
linha = 0
d = 0
while linha < x:
    for c in range(1, x+1):
        linha += 1
        print(f'{c+d} {c+d+1} {c+d+2} PUM')
        d += 3
