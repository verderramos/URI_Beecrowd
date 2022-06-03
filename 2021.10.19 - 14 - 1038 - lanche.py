A, B = input().split()
A = int(A)
B = int(B)

if A == 1:
    print(f'Total: R$ {B * 4.00:.2f}')
elif A == 2:
    print(f'Total: R$ {B * 4.50:.2f}')
elif A == 3:
    print(f'Total: R$ {B * 5.00:.2f}')
elif A == 4:
    print(f'Total: R$ {B * 2.00:.2f}')
elif A == 5:
    print(f'Total: R$ {B * 1.50:.2f}')
