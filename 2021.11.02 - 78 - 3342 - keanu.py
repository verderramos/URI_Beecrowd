n = int(input())
casas = n**2
if n % 2 == 0:
    cb = casas//2
    cp = casas//2
    print(f'{int(cb)} casas brancas e {int(cp)} casas pretas')
else:
    cb = (casas//2)+1
    cp = (casas//2)
    print(f'{int(cb)} casas brancas e {int(cp)} casas pretas')