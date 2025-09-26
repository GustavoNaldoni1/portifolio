#Pega a palavra ou frase do usuário que será analisada.
palavra = input('Digite uma palavra ou frase para ser analisada: ')

#Pega todas as letras do alfabeto já com acentos e também os sinais de pontuação para as estatísticas.
letras = "abcdefghijklmnopqrstuvwxyzáéíóúãõçABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚÃÕÇ"
sinais_de_pontuação = '!,;.?-:'

#Cria um dicionário para ser usado como estatística que guardará o caractere e a quantidade.
estatisticas = {}

#Faz um loop de iteração para cada caracter dentro do input do usuário.
for i in palavra:
    if i in letras:
        estatisticas[i] =  estatisticas.get(i, 0) + 1
    elif i in sinais_de_pontuação:
        estatisticas[i] = estatisticas.get(i, 0) + 1
    else:
        estatisticas['espaços_em_branco'] = estatisticas.get('espaços_em_branco', 0) + 1

#Faz um loop de iteração para ver as estatísticas de cada caractere.
for i in estatisticas.keys():
    print(i, ':', estatisticas[i])