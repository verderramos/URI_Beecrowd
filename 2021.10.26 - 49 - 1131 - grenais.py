jogos = 0
inter = 0
gremio = 0
empate = 0
while True:
    i, g = input().split()
    i = int(i)
    g = int(g)
    jogos += 1
    if i > g:
        inter += 1
    if g > i:
        gremio += 1
    if g == i:
        empate += 1
    print('Novo grenal (1-sim 2-nao)')
    x = int(input())
    while x not in (1, 2):
        print('Novo grenal (1-sim 2-nao)')
        x = int(input())
    if x == 2:
        print(f'{jogos} grenais')
        print(f'Inter:{inter}')
        print(f'Gremio:{gremio}')
        print(f'Empates:{empate}')
        if inter > gremio:
            print('Inter venceu mais')
        if gremio > inter:
            print('Gremio venceu mais')
        if gremio == inter:
            print('Nao houve vencedor')
        break
