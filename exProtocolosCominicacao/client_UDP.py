from socket import *

server = "127.0.0.1"
port = 43210

obj_socket = socket(AF_INET, SOCK_DGRAM) #criando um socket com protocolo UDP

out = ""
while out != "X":
    msg = input("Digite algo: ")
    obj_socket.sendto(msg.encode(), (server, port)) #enviando a mensagem
    dados, origem = obj_socket.recvfrom(65535) #recebendo os dados 65535 limite de bytes
    print("Reposta Server: ", dados.decode()) #decode exibe os dados em bytes no formato string
    out = input("Digite X para sair: ").upper()
obj_socket.close() #fechando o socket