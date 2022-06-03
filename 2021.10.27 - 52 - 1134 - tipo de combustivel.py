G = 0
A = 0
D = 0
x = int(input())
while x not in (1, 4):
    while x != 4:
        x = int(input())
        if x == 3:
            D += 1
        elif x == 2:
            G += 1
        elif x == 1:
            A += 1
    print('MUITO OBRIGADO')
    print(f'Alcool: {A}')
    print(f'Gasolina: {G}')
    print(f'Diesel: {D}')
