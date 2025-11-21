#Pega a palavra do usuário ou frase para a devida verificação.
palavra = input('Digite uma palavra ou frase para a verificação: ')

#Faz um loop para retirar os possíveis espaços da frase.
palíndromo = ''
for letra in palavra:
    if letra != " ":
        palíndromo+=letra

#Faz a devida verificação de palíndromo.
if palíndromo == palíndromo[::-1]:
    print('É palíndromo')
else:
    print('Não é palíndromo')

