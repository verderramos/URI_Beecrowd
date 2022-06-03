a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
D = (b**2)-(4*a*c)
doisa = 2*a
if D < 0 or doisa == 0:
    print('Impossível calcular')
else:
    print(f'R1 = {(((b*-1+D**0.5)/(2*a))):.5f}')
    print(f'R2 = {(((b*-1-D**0.5)/(2*a))):.5f}')
