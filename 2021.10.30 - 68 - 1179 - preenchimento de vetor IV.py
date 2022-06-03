par = list()
impar = list()
cont = 0
for _ in range(15):
    x = int(input())
    cont += 1
    if x % 2 == 0:
        par.append(x)
        if len(par) == 5:
            for c in range(len(par)):
                print(f'par[{c}] = {par[c]}')
            par.clear()
    else:
        impar.append(x)
        if len(impar) == 5:
            for d in range(len(impar)):
                print(f'impar[{d}] = {impar[d]}')
            impar.clear()
    if cont == 15:
        for c in range(len(impar)):
            print(f'impar[{c}] = {impar[c]}')
        for d in range(len(par)):
            print(f'par[{d}] = {par[d]}')