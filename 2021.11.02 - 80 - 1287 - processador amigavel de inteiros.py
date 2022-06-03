def lendotudo(entrada):
    inteiro = ''
    numeros = '0123456789'
    teste = 0
    for l in entrada:
        if l in numeros:
            inteiro += l
        else:
            if l == 'l':
                inteiro += '1'
            elif l == 'o' or l == 'O':
                inteiro += '0'
            elif l != ',' and l != ' ':
                teste = 1
                break
    try:
        inteiro = int(inteiro)
        if inteiro > 2147483647:
            teste = 1
    except ValueError:
        inteiro = 'error'
    if teste:
        inteiro = 'error'
    return inteiro
while True:
    try:
        entrada = input()
        entrada = lendotudo(entrada)
        print(entrada)
    except EOFError:
        break