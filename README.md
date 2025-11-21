
```markdown
# 🔹 Jogo Pedra, Papel e Tesoura com Socket

Um programa em Python que simula o jogo **Pedra, Papel e Tesoura** entre um cliente e um servidor.  
O cliente envia sua jogada e o servidor responde com sua própria escolha e o resultado da partida.

---

## 🚀 Funcionalidades

- Cliente escolhe entre **pedra | papel | tesoura**.  
- Servidor escolhe aleatoriamente sua jogada.  
- Resultado da partida é enviado ao cliente.  
- Tratamento de entradas inválidas.  

---

## 📦 Pré-requisitos

- **Python 3** instalado.  
- Bibliotecas utilizadas:  
  - `socket`  
  - `threading`  
  - `json`  
  - `random`  
  - `time`  

---

## ▶️ Como executar

1. Clone ou baixe este diretório.  
2. No terminal, inicie o servidor:

```bash
python server.py

3. Em outro terminal, inicie o cliente:

python client.py

4. Digite seu nome de usuário e escolha sua jogada:

Escolha entre pedra | papel | tesoura:

5. O servidor responderá com sua jogada e o resultado da partida.
