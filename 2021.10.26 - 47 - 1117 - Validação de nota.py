notas = list()
while True:
    x = float(input())
    if 0.0 <= x <= 10.0:
        notas.append(x)
        if len(notas) == 2:
            print(f'media = {sum(notas)/2:.2f}')
            break
    else:
        print('nota invalida')