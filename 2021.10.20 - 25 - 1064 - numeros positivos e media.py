contap = 0
contan = 0
somapos = 0

for c in range(0, 6):
    a = float(input())
    if a < 0:
        contan += 1
    else:
        contap += 1
        somapos += a
print(f'{contap} valores positivos')
print(f'{somapos/contap:.1f}')
