x = float(input())
N = list()
N.append(x)
for c in range(0, 99):
    N.append((N[c])/2)
for _ in range(len(N)):
    print(f'N[{_}] = {N[_]:.4f}')