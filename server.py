#Importando as bibliotecas necessárias:
import socket
import random
import json
import time
import threading
  
inputs = ["pedra", "papel", "tesoura"]
ganhar = {

    "pedra":"tesoura",
    "papel":"pedra",
    "tesoura":"papel"
}

def handle_client(conn, addr):
    print(f"[+] Nova conexão: {addr}")
    while True:
        try:
            msg = conn.recv(1024).decode('utf-8')
            if msg:
                data = json.loads(msg)
                if data['msg'].lower() not in inputs:
                    print('Servidor recebeu informações erradas')
                    continue

                print(f"[{time.strftime('%H:%M:%S')}] {data['user']} escolheu: {data['msg']}")

                res =  random.choice(inputs)
                print(f"[{time.strftime('%H:%M:%S')}] Servidor escolheu: {res}")

                if ganhar[res] == data['msg']:
                    
                    print(f"[{time.strftime('%H:%M:%S')}] Servidor ganhou o jogo!")

                elif ganhar[data['msg']] == res:
                    print(f"[{time.strftime('%H:%M:%S')}] Usuário ganhou o jogo!")

                
                else:
                    print(f"[{time.strftime('%H:%M:%S')}] Servidor e usuário escolheram as mesmas coisas!")
                
                resultado = {"user":"Servidor", "msg":f"O servidor escolheu {res}"}
                conn.send(json.dumps(resultado).encode('utf-8'))
        except:
            print(f"[-] Conexão perdida: {addr}")
            conn.close()
            break

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 5555))
    server.listen()
    print("[*] Servidor iniciado em 127.0.0.1:5555")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
     


if __name__ == "__main__":
    start_server()