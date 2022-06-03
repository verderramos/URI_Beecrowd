x = 1
cont = 0
while x != 0:
    x = int(input())
    r = ''
    if x == 0:
        break
    else:
        for _ in range(1, x+1):
            cont += 1
            r += str(_) + ' '
        print(r[:-1])