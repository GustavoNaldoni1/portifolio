#Criando uma função para pegar diversos números de uma vez.

def nums(*args):
    print('Digite seus números para executara as operações')
    return args

#Fazendo um loop sem uma condição específica para o usuário poder fazer todas as operações que quiser (de uma calculadora simples).
while True:
    #O usuário poderá sempre específicar uma operação e um conjunto de números que ele quiser a cada iteração. 
    operação = int(input('Digite o número da sua operação: 1-Soma, 2-Subtração, 3-Multiplicação, 4-Divisão, 5-Sair: '))
    numeros = input('Digite seus números: ')

    num = nums(numeros)

    str_num = str(num[0])

    #Analisando todos os casos da variável operação para realizar todas as devidas operações.
    match operação:
        case 1:
            num = 0
            for stri in str_num.split():
                num+=int(stri)
            print(num)
        case 2:
            num = int(str_num[0])
            lista = str_num.split()
            lista.remove(lista[0])
            for stri in lista:
                    num-=int(stri)
            print(num)
        case 3:
            num = int(str_num[0])
            lista = str_num.split()
            lista.remove(lista[0])
            for stri in lista:
                    num*=int(stri)
            print(num)
        case 4:
            num = int(str_num[0])
            lista = str_num.split()
            lista.remove(lista[0])
            for stri in lista:
                 num/=int(stri)
            print(num)
        #Um caso para sair da calculadora.
        case 5:
              print('Saindo da calculadora...')
              break
        