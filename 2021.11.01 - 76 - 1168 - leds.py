v = int(input())
for _ in range(v):
    n = str(input())
    soma = 0
    for i in range(len(n)):
        if n[i] in ('0', '6', '9'):
            soma += 6
        if n[i] in ('1'):
            soma += 2
        if n[i] in ('2', '3', '5'):
            soma += 5
        if n[i] in ('4'):
            soma += 4
        if n[i] in ('7'):
            soma += 3
        if n[i] in ('8'):
            soma += 7
    print(f'{soma} leds')