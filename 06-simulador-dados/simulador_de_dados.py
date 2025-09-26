#Pega algumas funções de certas bibliotecas para realizar operações específicas, choice faz uma escolha dentro de um iterador e trunc reduz um número flutuante ao inteiro mais próximo de zero.
from random import choice
from math import trunc

#Criando uma função para formar dados que utiliza um loop e depende da quantidade de lados dita pelo usuário.
def formar_dado(lados):
    possibilidades = []
    for i in range(1, lados+1):
        possibilidades.append(i)
    return possibilidades

#Criando um dicionário que conterá o nome do dado e as possibilidades.
dados = {}

#Loop de iteração sem condição para o usuário poder executar as suas devidas operações.
while True:
    
    #Uma variável que é usada para ser analisada para fazer diversas operações.
    opção = input('Diga o que quer fazer: \n1-Criar um dado\n2-Rolar um dado\n3-Maior Rolagem\n4-Menor Rolagem\n5-Média\n6-Sair\n:')

    #Analisando cada possível caso de opção: criar um dado, rolar um dado (já existente), maior rolagem de um dado, menor rolagem de um dado, média do dado e sair da operação.
    match opção:
        case '1':
            nome_dado = input('Diga um nome para o seu dado: ')
            n_lados = int(input('Diga quantos lados tem o seu dado: '))
            dados[nome_dado] = formar_dado(n_lados)
            print('Dado criado com sucesso')
        case '2':
            nome_dado = input('Escolha um dado para ser usado: ')
            if nome_dado in dados:
                print(choice(dados[nome_dado]))
                while True:
                    continuar = input('Continuar rolando o dado?(Y/N) ')
                    if continuar == 'Y':
                        print(choice(dados[nome_dado]))
                    elif continuar == 'N':
                        break
                    else:
                        print('Não tem essa opção')
            else:
                print('Digite um nome de um dado pre-existente ou crie um novo dado')
        case '3':
            nome_dado = input('Escolha um dado para verificar: ')
            escolha_1 = choice(dados[nome_dado])
            escolha_2 = choice(dados[nome_dado])
            escolhas = [escolha_1, escolha_2]
            print(max(escolhas))
            print('Opções: ', escolhas)
        case '4':
            nome_dado = input('Escolha um dado para verificar: ')
            escolha_1 = choice(dados[nome_dado])
            escolha_2 = choice(dados[nome_dado])
            escolhas = [escolha_1, escolha_2]
            print(min(escolhas))
            print('Opções: ', escolhas)
        case '5':
            nome_dado = input('Escolha um dado para verificar: ')
            lista = []
            num = 0
            for i in range(len(dados[nome_dado])):
                lista.append(choice(dados[nome_dado]))
                num+=lista[i]
                print(num)
            print('Média de {} rolagens:\n'.format(len(dados[nome_dado])),lista,'\n',trunc((num/len(dados[nome_dado]))))
        case '6':
            print('Saindo do simulador..')
            break