n = int(input())
total = coelhos = ratos = sapos = 0
for c in range(n):
    q, t = input().split()
    q = int(q)
    t = str(t).upper()
    total += q
    if t == 'S':
        sapos += q
    if t == 'R':
        ratos += q
    if t == 'C':
        coelhos += q
print(f'Total: {total} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print(f'Percentual de coelhos: {(coelhos/total)*100:.2f} %')
print(f'Percentual de ratos: {(ratos/total)*100:.2f} %')
print(f'Percentual de sapos: {(sapos/total)*100:.2f} %')
