T = str(input())
lin1 = []
lin2 = []
lin3 = []
lin4 = []
lin5 = []
lin6 = []
lin7 = []
lin8 = []
lin9 = []
lin10 = []
lin11 = []
lin12 = []
dados = [lin1[:], lin2[:], lin3[:], lin4[:], lin5[:], lin6[:], lin7[:], lin8[:], lin9[:], lin10[:], lin11[:], lin12[:]]

for c in range(len(dados)):
    for d in range(0, len(dados)):
        dados[c].append(float(input()))
inuteis = list()
uteis = list()
for l in range(0, len(dados)):
    for c in range(0, len(dados)):
        if c < len(dados) - l - 1:
            uteis.append(dados[l][c])
        else:
            inuteis.append(dados[l][c])
if T == 's':
    print(f'{sum(uteis):.1f}')
else:
    print(f'{(sum(uteis)/len(uteis)):.1f}')