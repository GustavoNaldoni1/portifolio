#Importando as bibliotecas necessárias
import socket
import threading
import json

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

#Função que iniciará o client
def start_client(user):
    #Socket responsável pela conexão
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Conectando o socket ao servidor
    sock.connect(('127.0.0.1', 5555))

    #Criando o thread do usuário
    thread = threading.Thread(target=receive_messages, args=(sock,))

    #Iniciando o thread
    thread.start()

    #Loop de envio de mensagens
    while True:
        #Pegando a mensagem do usuário
        msg = input()

        #Transformando as informações em um objeto
        dados = {'user':user, 'msg':msg}

        #Enviando as mensagens para o usuário
        sock.send(json.dumps(dados).encode('utf-8'))

#Se o nome do arquivo for esse inicia o client
if __name__ == "__main__":
    #Pegando o nome de usuário
    user = input('Digite seu nome de usuário: ')
    start_client(user)