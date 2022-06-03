x = int(input())
y = int(input())
if x > y:
    maior = x
    menor = y
else:
    maior = y
    menor = x
for n in range(menor+1, maior):
    if n % 5 == 2 or n % 5 == 3:
        print(n)
