# input
n = int(input())

resposta = []
for _ in range(n):
    entrada = input()
    palavra = list(entrada)

    # convertendo a palavra em ASCii
    palavra_ascii = [ord(c) for c in entrada]

    # somando 3 se for letra
    mais3_lista_ascii = []
    for i in range(len(entrada)):
        if palavra[i].isalpha():
            mais3_lista_ascii.append(palavra_ascii[i] + 3)
        else:
            mais3_lista_ascii.append(palavra_ascii[i])

    #convertendo ASCii para letra
    mais3_txt = ''.join(map(chr, mais3_lista_ascii))
    mais3_lista_txt = list(mais3_txt)

    # invertendo a palavra
    mais3_lista_txt.reverse()

    # convertendo a palavra invertida em ASCii
    palavra_ascii_invertida = [ord(c) for c in mais3_lista_txt]

    # subtraindo 1 a partir da metade
    menos1_lista_ascii = []
    for i in range(len(entrada)):
        if i < (len(entrada)//2):
            menos1_lista_ascii.append(palavra_ascii_invertida[i])
        else:
            menos1_lista_ascii.append(palavra_ascii_invertida[i] - 1)

    # convertendo de volta para texto e criando a lista de respostas
    menos1_txt = ''.join(map(chr, menos1_lista_ascii))
    resposta.append(menos1_txt)

# printando a resposta
for i in resposta:
    print(i)
