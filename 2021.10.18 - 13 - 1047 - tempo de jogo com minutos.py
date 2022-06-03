a = input().split()
hi, mi, hf, mf = a
hi = int(a[0])
mi = int(a[1])
hf = int(a[2])
mf = int(a[3])

if hi < hf:
    h = hf - hi
    if mi < mf:
        m = mf - mi
    elif mi > mf:
        h = h - 1
        m = (60 - mi) + mf
    elif mi == mf:
        m = 0
elif hi > hf:
    h = (24 - hi) + hf
    if mi < mf:
        m = mf - mi
    elif mi > mf:
        h = h - 1
        m = (60 - mi) + mf
    elif mi == mf:
        m = 0
elif hi == hf:
    if mi < mf:
        m = mf - mi
        h = 0
    elif mi > mf:
        m = (60 - mi) + mf
        h = 23
    elif mi == mf:
        h = 24
        m = 0
print(f'O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)')
