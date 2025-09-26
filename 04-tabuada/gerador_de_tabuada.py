#Pega o número do usuário e verifica se o número está em um caso em que não precisa fazer um arquivo específico.
numero = int(input('Digite um número para calcular a tabuada: '))
if numero == 0 or numero == 1 or numero == -1:
    print('Tabuada de zero é tudo zero \n Tabuada de 1 são todos os números que multiplicam o 1 e a do -1 também.')
else:  
    #Faz o arquivo específico de uma forma já estilizada.
    with open('tabuada.txt', 'w') as f:
       f.write(f'{'|':>23} {'TABUADA DO NÚMERO'.center(23)}{numero} {'|':>2}\n')
       for i in range(50):
        f.write(f'{'|':>35}{i*numero:>2}{'|':>2}\n')


    