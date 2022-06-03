v = float(input())
valor = int(v)
moedas = int(round((v - valor), 2)*100)
n100 = valor // 100
resto100 = (valor % 100)
n50 = resto100 // 50
resto50 = resto100 % 50
n20 = resto50 // 20
resto20 = resto50 % 20
n10 = resto20 // 10
resto10 = resto20 % 10
n5 = resto10 // 5
resto5 = resto10 % 5
n2 = resto5 // 2
resto2 = resto5 % 2
n1 = resto2 // 1
resto1 = (resto2 % 1)
m50 = int(moedas // 50)
resto050 = moedas % 50
m25 = int(resto050 // 25)
resto025 = resto050 % 25
m10 = int(resto025 // 10)
resto010 = (resto025 % 10)
m5 = int(resto010 // 5)
resto005 = (resto010 % 5)
m1 = int(resto005 // 1)
print('NOTAS:')
print(f'{n100} nota(s) de R$ 100.00')
print(f'{n50} nota(s) de R$ 50.00')
print(f'{n20} nota(s) de R$ 20.00')
print(f'{n10} nota(s) de R$ 10.00')
print(f'{n5} nota(s) de R$ 5.00')
print(f'{n2} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{n1} moeda(s) de R$ 1.00')
print(f'{m50} moeda(s) de R$ 0.50')
print(f'{m25} moeda(s) de R$ 0.25')
print(f'{m10} moeda(s) de R$ 0.10')
print(f'{m5} moeda(s) de R$ 0.05')
print(f'{m1} moeda(s) de R$ 0.01')
