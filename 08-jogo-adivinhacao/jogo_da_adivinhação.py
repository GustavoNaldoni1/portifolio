#Importa uma única função que será usada no código, randint escolhe um número aleatório de a até b.
from random import randint

#Comprimenta o usuário e escolhe um número que nem mesmo o programador sabe.
print('Bem vindo ao jogo de adivinhação!')
num_correto = randint(1, 100)

#Loop de iteração que faz com que o jogo funcione.
while True:
    
    #Número que o usuário digita para verificar se ganhou ou não o jogo.
    num_usuário = int(input('Digite um número de 1 a 100: '))

    #Verificações de quente ou frio a respeito do número do usuário.
    if num_usuário > num_correto:
        print('Menor')
    elif num_usuário < num_correto:
        print('Maior')
    else:
        print('Você ganhou o jogo')
        break