n = int(input())
medias = list()
for c in range(0, n):
    x, y, z = input().split()
    x = float(x)
    y = float(y)
    z = float(z)
    m = (((x * 2) + (y * 3) + (z * 5))/10)
    medias.append(m)
for c in range(len(medias)):
    print(f'{medias[c]:.1f}')
