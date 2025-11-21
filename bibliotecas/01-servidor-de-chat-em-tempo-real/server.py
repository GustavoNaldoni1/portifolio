# server.py
import socket
import threading
import json
import time

clients = []

#Criando uma função para gerenciar os usuários
def broadcast(msg, conn):
    #Loop de iteração nos clients
    for client in clients:
        #Se o client for diferente da conexão
        if client != conn:
            try:
                #Tenta enviar uma mensagem a ele
                client.send(msg.encode('utf-8'))
            except:
                #Remove a conexão do client
                clients.remove(client)
                
def handle_client(conn, addr):
    print(f"[+] Nova conexão: {addr}")
    while True:
        try:
            msg = conn.recv(1024).decode('utf-8')
            if msg:
                data = json.loads(msg)
                print(f"[{time.strftime('%H:%M:%S')}] {data['user']}: {data['msg']}")
                broadcast(msg, conn)
        except:
            print(f"[-] Conexão perdida: {addr}")
            clients.remove(conn)
            conn.close()
            break

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 5555))
    server.listen()
    print("[*] Servidor iniciado em 127.0.0.1:5555")

    while True:
        conn, addr = server.accept()
        clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
