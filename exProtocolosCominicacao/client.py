from socket import *

server = "127.0.0.1"
port = 43210

while True:
    
    obj_socket = socket(AF_INET, SOCK_STREAM) #criando um socket
    obj_socket.connect((server, port)) #conectando o socket ao endereco e porta
    msg = bytes(input("Digite algo: "), 'utf-8') #transformando a mensagem em bytes
    obj_socket.send(msg) #enviando a mensagem
    msg_resposta = obj_socket.recv(1024) #recebendo a mensagem
    print("Resposta do servidor: ", str (msg_resposta)[2:-1]) #[2:-1] para remover b' e ' da mensagem
    if str(msg)[2:-1].upper() == "SAIR":
        break
obj_socket.close() #fechando o socket

# The client code is similar to the server code, but it uses the connect() method to connect to the server.