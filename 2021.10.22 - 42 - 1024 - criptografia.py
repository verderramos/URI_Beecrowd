# variáveis
palavra = list()
pasc = list()
mais3 = list()
mais3txt = list()
word = ''
lm3txt = list()
parte3 = list()
parte4 = list()
resp = list()
resposta = list()
final = ''
# input
n = int(input())
for a in range(n):
    p = str(input())
    for y in range(len(p)):
# criando lista de palavras
        palavra.append(p[y])
    word = p
# convertendo a palavra em ASCii
    pasc = [ord(c) for c in word]
# somando 3 se for letra
    for b in range(len(word)):
        if palavra[b].isalpha():
            mais3.append(pasc[b]+3)
        else:
            mais3.append(pasc[b])
#convertendo ASCii para letra
    mais3txt.append(''.join(map(chr, mais3)))
    for c in range(0, len(mais3txt[0])):
        lm3txt.append(mais3txt[0][c])
# invertendo a palavra
    lm3txt.reverse()
# convertendo a palavra invertida em ASCii
    parte3 = [ord(c) for c in lm3txt]
# subtraindo 1 a partir da metade
    for d in range(len(word)):
        if d < (len(word)/2):
            parte4.append(parte3[d])
        else:
            parte4.append(parte3[d]-1)
    resp.clear()
# convertendo de volta para texto e criando a lista de respostas
    resp.append(bytes(parte4).decode())

# limpando todas as variáveis
    palavra.clear()
    pasc.clear()
    mais3.clear()
    mais3txt.clear()
    word = ''
    lm3txt.clear()
    parte3.clear()
    parte4.clear()

# printando a resposta
for i in resp:
    print(f'{i}')
