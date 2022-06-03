i = int(input())
print(f'{i//365} ano(s)')
print(f'{(i % 365)//30} mes(es)')
print(f'{((i % 365)%30)} dia(s)')