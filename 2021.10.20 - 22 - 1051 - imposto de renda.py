r = float(input())
status = 0
if r <= 2000.00:
    status = 'Isento'
if 2000.01 <= r <= 3000.00:
    t8 = (r - 2000) * 0.08
    status = (f'R$ {t8:.2f}')
if 3000.01 <= r <= 4500.00:
    t18 = (999.99 * .08) + ((r - 3000) * 0.18)
    status = (f'R$ {t18:.2f}')
if r > 4500.00:
    t28 = (999.99 * 0.08) + (1499.99 * 0.18) + ((r - 4500) * 0.28)
    status = (f'R$ {t28:.2f}')
print(f'{status}')
