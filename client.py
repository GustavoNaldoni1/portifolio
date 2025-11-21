#Importando as bibliotecas necessárias
import socket
import json
import threading

inputs = ["pedra", "papel", "tesoura"]
#Criando uma função para gerenciar o pedra-papel-tesoura
def jogo():
    msg = input('Escolha entre pedra | papel | tesoura: ')
    #Verificando os inputs de msg
    
    if msg.lower() not in inputs:
        return 0
    #Se ele escolheu certo, retorna a escolha dele
    else:
        return msg
    
#Função para receber mensagens
def receive_messages(sock):
    #Loop para receber mensagens
    while True:
        try:
            #Recebendo as mensagens
            msg = sock.recv(1024).decode('utf-8')

            #Transformando a mensagem em um objeto
            dados = json.loads(msg)

            #Printando as informações
            print(f"{dados['user']}:{dados['msg']}")
        except:
            #Printa para o usuário quando acabou uma conexão
            print("Conexão encerrada pelo servidor")

            #Finaliza a conexão
            sock.close()

            #Quebra o loop
            break

def start_client(user):
    #Criando o socket responsável pela conexão
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Conectando o usuário ao servidor
    sock.connect(('127.0.0.1', 5555))

    #Criando o thread do usuário
    thread = threading.Thread(target=receive_messages, args=(sock,))

    #Iniciando o thread
    thread.start()

    #Loop para pegar as informações do usuário
    while True:
        #Pegando as informações do usuário
        msg = jogo()
        if msg == 0:
            print("Usuário não quis participar do jogo")
            continue
        #Transformando as informações em objeto
        dados = {"user":user, "msg":msg}

        #Enviando ao serivdor
        sock.send(json.dumps(dados).encode('utf-8'))

if __name__ == "__main__":
    user = input("Digite seu nome de usuário: ")
    start_client(user)