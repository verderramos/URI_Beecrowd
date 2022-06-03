# A primeira linha da entrada contém um inteiro T, indicando o número de casos de teste.
# Cada caso de teste contém um único inteiro N (0 ≤ N ≤ 60), correspondente ao N-esimo
# termo da série de Fibonacci.

t = int(input())
num = list()
resp = list()
fibo = list()
for x in range(0, t):
    n = num.append(int(input()))
    for d in range(len(num)):
        fibo.clear()
        fibo.append(0)
        fibo.append(1)
        for c in range(0, num[d]):
            fibo.append(fibo[c]+fibo[c+1])
    resp.append(fibo[num[d]])
for c in range(len(num)):
    print(f'Fib({num[c]}) = {resp[c]}')