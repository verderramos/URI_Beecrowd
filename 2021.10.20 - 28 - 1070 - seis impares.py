a = int(input())
x = 0
impar = list()
cont = 0
if a % 2 == 0:
    x = a + 1
else:
    x = a
while True:
    impar.append(x)
    cont += 1
    x = x + 2
    if cont == 6:
        break
for c in range(0, len(impar)):
    print(impar[c])
