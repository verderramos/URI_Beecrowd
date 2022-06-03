x = int(input())
y = int(input())
maior = 0
menor = 0
if x > y:
    maior = x
    menor = y
else:
    menor = x
    maior = y
soma = 0

for c in range(menor, maior+1):
    if c % 13 != 0:
        soma += c
print(soma)