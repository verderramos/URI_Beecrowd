contapos = contaneg = contapar = contaimp = 0

for c in range(0, 5):
    a = int(input())
    if a > 0:
        contapos += 1
    if a < 0:
        contaneg += 1
    if a % 2 == 0:
        contapar += 1
    else:
        contaimp += 1
print(f'{contapar} valor(es) par(es)')
print(f'{contaimp} valor(es) impar(es)')
print(f'{contapos} valor(es) positivo(s)')
print(f'{contaneg} valor(es) negativo(s)')
