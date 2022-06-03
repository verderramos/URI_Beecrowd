n = int(input())
x = list(map(int, input().split()))
pos = 0
menor = x[0]
for c in range(len(x)):
    if x[c] < menor:
        menor = x[c]
        pos = c
print(f'Menor valor: {menor}')
print(f'Posicao: {pos}')