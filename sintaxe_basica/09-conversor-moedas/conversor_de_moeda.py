#Loop de iteração que serve para criar todo o sistema do conversor de moeda.
while True:

    #Inputs que serão usados para converter a moeda, o primeiro é a quantidade não necessariamente em reais e o segundo é a opção que o usuário deseja fazer.
    moeda = float(input('Digite a sua quantidade: '))
    opção = input('Digite o tipo de conversão:\n1-Real-Dólar\n2-Real-Euro\n3-Euro-Dólar\n4-Euro-Real\n5-Dólar-Real\n6-Dólar-Euro\n7-Sair\n:')
    
    #Análise de todas as opções do input opção que o usuário pode converter.
    match opção:
        case '1':
            print(f' {(moeda/5.36):.2f} Dólares')
        case '2':
            print(f' {(moeda/6.26):.2f} Euros')
        case '3':
            print(f' {(moeda*1.17):.2f} Dólares')
        case '4':
            print(f' {(moeda*6.26):.2f} Reais')
        case '5':
            print(f' {(moeda*5.36):.2f} Reais')
        case '6':
            print(f' {(moeda*0.86):.2f} Euros')
        case '7':
            print('Saindo do conversor')
            break