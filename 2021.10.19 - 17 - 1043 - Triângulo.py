r1, r2, r3 = input().split()
r1 = float(r1)
r2 = float(r2)
r3 = float(r3)
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 >r2:
    print(f'Perimetro = {r1+r2+r3}')
else:
    print(f'Area = {((r1+r2)*r3)/2}')
