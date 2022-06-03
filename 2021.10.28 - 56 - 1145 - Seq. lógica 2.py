x, y = input().split()
x = int(x)
y = int(y)
l = round(y / x)
qt = y - (x * (l - 1))
a = 0
b = 0
while b <= qt:
    for _ in range(1, y+1):
        if a == x-1:
            print(_, end='\n')
            a = 0
            b += 1
        else:
            print(_, end=' ')
            a += 1
            b += 1
