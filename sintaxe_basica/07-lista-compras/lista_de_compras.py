#Faz um dicionário que guardará o nome do item e a quantidade dele e faz um comprimento ao usuário.
lista_compras = {}
print('Bem vindo ao sistema de lista de compras!')

#Loop de iteração que é usado para adicionar, remover ou listar itens da lista de compras. Note que não têm uma condição ou seja o usuário poderá executar ações até a hora de devidamente querer sair.
while True:

    #Input que será usado para analisar e fazer todas as operações na lista de compras.
    opções = input('Digite a opção que desejar:\n1-Adicionar\n2-Remover\n3-Listar\n4-Sair: ')

    #Analisando todas as operações que são possíveis dentro do sistema.
    match opções:
        case '1':
            item = input('Digite o item que deseja adicionar: ')
            quantidade = input('Digite a quantidade desse item que deseja adicionar: ')

            lista_compras[item] = quantidade

            print(f'Item {item} adicionado com sucesso na lista de compras!')
        case '2':
            item = input('Digite o item que deseja adicionar: ')

            if item in lista_compras:
                lista_compras.pop(item)
                print(f'Item {item} removido com sucesso da lista de compras!')
            else:
                print('Não há itens para excluir')
        case '3':
            print('Listando itens')

            if len(lista_compras) > 0:
                for i in lista_compras.keys():
                    print(i,lista_compras[i])
                    print('Todos os itens listados com sucesso')
            else:
                print('Não há itens para listar')

        #Caso de saída também gera um arquivo para o usuário guardar a sua lista de compras.
        case '4':
            print('Saindo do sistema de lista de compras!')
            if len(lista_compras) > 0:
                with open('compras.txt', 'w') as f:
                    f.write('LISTA DE COMPRAS\n')
                    for i in lista_compras.keys():
                        f.write(i + ' ' + lista_compras[i])
            break