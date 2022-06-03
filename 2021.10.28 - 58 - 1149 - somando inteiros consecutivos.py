x = list(map(int, input().split()))
i = 1
r = 0
while x[i] <= 0:
    if x[i] <= 0:
        i = i + 1
    if x[i] > 0:
        break
for _ in range(0, x[i]):
    r += x[0] + _
print(r)