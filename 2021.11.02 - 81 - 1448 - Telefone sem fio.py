t = input()
t = int(t)
time1 = list()
time2 = list()
for c in range(t):
    f1 = str(input())
    f2 = str(input())
    f3 = str(input())
    for d in range(len(f1)):
        if f1[d] == f2[d]:
            time1.append(1)
        else:
            time1.append(0)
        if f1[d] == f3[d]:
            time2.append(1)
        else:
            time2.append(0)
    print('Instancia {}'.format(c+1))
    d1 = 0
    d2 = 0
    if sum(time1) == sum(time2):
        v = 0
        for e in range(len(time1)):
            if d1 == d2:
                if time1[e] - time2[e] == 1:
                    d1 = 1
                elif time1[e] - time2[e] == -1:
                    d1 = 1
                else:
                    v = 1
            else:
                break
    if sum(time1) > sum(time2) or d1 == 1:
        print('time 1')
    elif sum(time1) < sum(time2) or d2 == 1:
        print('time 2')
    elif sum(time1) == sum(time2) and d1 == 0 and d2 == 0:
        print('empate')
    time1.clear()
    time2.clear()
print()
