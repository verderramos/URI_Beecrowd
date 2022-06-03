contin = 0
contout = 0
x = int(input())
for c in range(x):
    z = int(input())
    if 10 <= z <= 20:
        contin += 1
    else:
        contout += 1
print(f'{contin} in')
print(f'{contout} out')
