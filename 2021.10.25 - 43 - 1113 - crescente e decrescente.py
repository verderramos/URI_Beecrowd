while True:
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a == b:
        break
    if a > b:
        print('Decrescente')
    else:
        print('Crescente')
