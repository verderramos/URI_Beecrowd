i = 0
j = 1
for a in range(0, 3):
    print(f'I={i} J={j+a}')
for c in range(0, 4):
    for b in range(0, 3):
        print(f'I={i+.2:.1f} J={j + b + 0.2:.1f}')
    j += 0.2
    i += 0.2
i = 1
j = 2
for a in range(0, 3):
    print(f'I={i} J={j+a}')
for c in range(0, 4):
    for b in range(0, 3):
        print(f'I={i+.2:.1f} J={j + b + 0.2:.1f}')
    j += 0.2
    i += 0.2
i = 2
j = 3
for a in range(0, 3):
    print(f'I={i} J={j+a}')