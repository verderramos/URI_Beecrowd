x = int(input())
z = x - 1
while z <= x:
    z = int(input())

soma = x
s = 1
i = 2
while soma <= z:
    soma = soma + x + s
    if soma <= z:
        i = i + 1
        s = s + 1
print(i)