x = int(input())
for c in range(x):
    n = str(input())
    dificil = ''
    for l in n:
        if l not in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
            dificil += '1'
        else:
            dificil += '0'
    if '111' in dificil:
        print(f'{n} nao eh facil')
    else:
        print(f'{n} eh facil')
