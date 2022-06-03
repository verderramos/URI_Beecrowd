x = int(input())
s = 2
n1 = 0
n2 = 1
r = '0 1'
while s < x:
    r += ' '
    r += str(n1+n2)
    y = n1+n2
    n1 = n2
    n2 = y
    s += 1
print(r)