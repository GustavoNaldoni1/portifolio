#Criando as funções que serão usadas no loop de iteração para converter as temperaturas. Note que reverse é uma variável que possibilita a operação contrária da conversão.
def celsius_kelvin(temp, reverse=False):
    if reverse:
        print(f'{temp-273.15} Celsius')      
    else:
        print(f'{temp+273.15} Kelvins')
        
def celsius_fahrenheit(temp, reverse=False):
    if reverse:
        print(f'{(temp-32)/1.8} Fahrenheit')
    else:
        print(f'{(temp*1.8)+32} Celsius')

def fahrenheit_kelvin(temp,reverse=False):
    if reverse:
        print(f'{((temp+32)/1.8)+273.15}')
    else:
        print(f'{(1.8*(temp-273.15))+32}')

#Criando o loop de iteração que será usado para fazer as devidas conversões.
while True:
    #O usuário sempre poderá estabelecer uma temperatura e a sua conversão a cada iteração do loop.
    temperatura = float(input('Digite sua temperatura: '))
    opção = input('Digite sua opção: \n1-Celsius-Kelvin, \n2-Celsius-Fahrenheit, \n3-Fahrenheit-Kelvin, \n4-Kelvin-Celsius, \n5-Kelvin-Fahrenheit, \n6-Fahrenheit-Celsius, \n7-Sair: ')

    #Uma análise de todos os possíveis casos de conversão.
    match opção:
        case '1':
            celsius_kelvin(temperatura)
        case '2':
            celsius_fahrenheit(temperatura)
        case '3':
            fahrenheit_kelvin(temperatura)
        case '4':
            celsius_kelvin(temperatura, reverse=True)
        case '5':
            fahrenheit_kelvin(temperatura, reverse=True)
        case '6':
            celsius_fahrenheit(temperatura, reverse=True)
        #Um caso para sair do loop e encerrar a operação.
        case '7':
            print('Saindo do conversor')
            break
