a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
maiorab = ((a+b+abs(a-b))/2)
maior = int(maiorab)
if maior > c:
    print(f'{maior} eh o maior')
else:
    print(f'{c} eh o maior')
