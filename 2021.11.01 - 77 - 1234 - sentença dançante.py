try:
    while True:
        s = str(input())
        x = 10
        resposta = ''
        for c in range(len(s)):
            if s[c] == ' ':
                resposta += ' '
            elif x > 0:
                resposta += s[c].upper()
                x = x * -1
            else:
                resposta += s[c].lower()
                x = x * -1
        print(resposta)
except EOFError:
    quit()
