from socket import *

server = "127.0.0.1"
port = 43210

obj_socket = socket(AF_INET, SOCK_DGRAM) #criando um socket com protocolo UDP
obj_socket.bind((server, port)) #vinculando o socket ao endereco e porta
print("Server pronto....")
try:
    while True:
        dados, origem = obj_socket.recvfrom(65535) #recebendo os dados 65535 limite de bytes
        print("Origem..........:", origem)
        print("Dados recebidos.:", dados.decode()) #decode exibe os dados em bytes no formato string
        resposta = input("Digite a resposta: ")
        obj_socket.sendto(resposta.encode(), origem) #enviando a resposta, encode convert string to bytes
finally:
    obj_socket.close() #fechando o socket

# The server code is similar to the client code, but it uses the bind() method to bind the socket to an address and port.