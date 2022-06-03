menor = 0
maior = 0
soma = 0
menores = list()
maiores = list()
plus = list()
while True:
    m, n = input().split()
    m = int(m)
    n = int(n)
    if m <= 0:
        break
    if n <= 0:
        break
    else:
        if m > n:
            maior = m
            menor = n
        else:
            maior = n
            menor = m
    menores.append(menor)
    maiores.append(maior)
    for c in range(menor, maior+1):
        soma += c
    plus.append(soma)
    soma = 0
for c in range(len(plus)):
    for d in range(menores[c], maiores[c]+1):
        print(d, end=' ')
    print(f'Sum={plus[c]}')
