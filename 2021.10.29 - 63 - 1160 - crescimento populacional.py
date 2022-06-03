t = int(input())
for c in range(0, t):
    pa, pb, g1, g2 = map(float, input().split())
    pa = int(pa)
    pb = int(pb)
    anos = 0
    while pa <= pb:
        pa += int((pa * g1) / 100)
        pb += int((pb * g2) / 100)
        anos += 1
        if anos > 100:
            print('Mais de um seculo.')
            break
    if anos <= 100:
        print(f'{anos} anos.')
