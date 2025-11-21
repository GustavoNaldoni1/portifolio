#Loop de iteração usado para criar o sistema de contador e variável para incrementar o número de arquivos de relatório.
n=1
while True:
    #Variáveis importantes que serão usadas ao decorrer da operação, o primerio é um input para pegar a palavra ou frase do usuário, o segundo é para dividir as palavras em uma lista e o terceiro é um número para incrementar para cada palavra para fazer o relatório.
    palavra = input('Digite sua palavra ou frase: ')
    palavra_lista = palavra.split()
    count = 0

    #Loop para contar as palavras.
    for i in palavra_lista:
        count+=1

    #Abrindo um arquivo para realizar um relatório. Note que nunca teremos um relatório com a mesma sequência de palavras ou frases, por conta do número n. Nesse relatório contém a quantidade de palavras, a maior palavra e a menor palavra dita pelo usuário.
    with open('relatório{}.txt'.format(n), 'w') as f:
        f.write('Quantidade de palavras: {}\n'.format(count))
        f.write('Maior palavra: {}\n'.format(max(palavra_lista, key=len)))
        f.write('Menor palavra: {}'.format(min(palavra_lista, key=len)))
        n+=1

    #Um input para verificar se o usuário quer continuar verificando e propriamente a verificação.
    sair = input('Deseja sair do contador?(Y/N)')
    if sair == 'Y':
        print('Saindo do contador')
        break
    else:
        continue