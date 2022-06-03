x, y, z = input().split()
x = float(x)
y = float(y)
z = float(z)
v = list()
v.append(x)
v.append(y)
v.append(z)
v.sort(reverse=True)
a = v[0]
b = v[1]
c = v[2]

if a >= (b + c) or b >= (c + a) or c >= (b + a):
    print('NAO FORMA TRIANGULO')
else:
    if a**2 == b**2 + c**2:
        print('TRIANGULO RETANGULO')
    if a**2 > b**2 + c**2:
        print('TRIANGULO OBTUSANGULO')
    if a**2 < b**2 + c**2:
        print('TRIANGULO ACUTANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    if a == b != c or b == c != a or c == b != a:
        print('TRIANGULO ISOSCELES')
