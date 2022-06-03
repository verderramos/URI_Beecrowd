a, b = input().split()
hi, p1, mi, p2, si = input().split()
c, d = input().split()
hf, p3, mf, p4, sf = input().split()
b = int(b)
d = int(d)
hi = int(hi)
mi = int(mi)
si = int(si)
hf = int(hf)
mf = int(mf)
sf = int(sf)
minutoseg = 60
horaseg = minutoseg * 60
diaseg = horaseg * 24
i = si + mi*minutoseg + hi*horaseg + b*diaseg
f = sf + mf*minutoseg + hf*horaseg + d*diaseg
if i < f:
    tempo = f - i
    dias = int(tempo/diaseg)
    tempo = tempo % diaseg
    horas = int(tempo/horaseg)
    tempo = tempo % horaseg
    minutos = int(tempo/minutoseg)
    tempo = tempo % minutoseg
    segundos = tempo
    print(f'{dias} dia(s)')
    print(f'{horas} hora(s)')
    print(f'{minutos} minuto(s)')
    print(f'{segundos} segundo(s)')
