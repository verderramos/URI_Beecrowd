a = float(input())
rreaj = 0
reajperc = 0
nsal = 0
if a > 2000.00:
    reajperc = 4
    rreaj = (a * (reajperc / 100))
    nsal = a + rreaj
if a <= 2000.00:
    reajperc = 7
    rreaj = (a * (reajperc / 100))
    nsal = a + rreaj
if a <= 1200.00:
    reajperc = 10
    rreaj = (a * (reajperc / 100))
    nsal = a + rreaj
if a <= 800.00:
    reajperc = 12
    rreaj = (a * (reajperc / 100))
    nsal = a + rreaj
if a <= 400.00:
    reajperc = 15
    rreaj = (a * (reajperc/100))
    nsal = a + rreaj
print(f'Novo salario: {nsal:.2f}')
print(f'Reajuste ganho: {rreaj:.2f}')
print(f'Em percentual: {reajperc} %')
