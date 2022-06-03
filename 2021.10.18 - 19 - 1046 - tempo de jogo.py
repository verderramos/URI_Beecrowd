a = input().split()
hi, hf = a
hi = int(a[0])
hf = int(a[1])

if hi < hf:
    h = hf - hi
elif hi > hf:
    h = (24 - hi) + hf
elif hi == hf:
    h = 24

print(f'O JOGO DUROU {h} HORA(S)')
