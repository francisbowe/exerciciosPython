from socket import * #importando todas as funcoes de socket
#TODOS OS DADOS TRANSMITIDOS VIA SOCKET DEVEM ESTAR NO FORMATO BYTES 
server = "127.0.0.1"
port = 43210
obj_socket = socket(AF_INET, SOCK_STREAM) #criando um socket 
obj_socket.bind((server, port)) #vinculando o socket ao endereco e porta
obj_socket.listen(2) #socket fica ouvindo a porta, 2 sigifica o maximo de clientes que podem se conectar
print("Aguardando cliente...")
while True:
    con, cliente = obj_socket.accept() #aceitando a conexao
    print("Conectado com: ", cliente)
    while True:
        msg_recebida = str(con.recv(1024)) #recebendo a mensagem
        print("Recebemos: ", str(msg_recebida)[2:-1]) #[2:-1] para remover b' e ' da mensagem
        msg_enviada = bytes(input("Sua resposta: "), 'utf-8') #enviando a mensagem
        con.send(msg_enviada)
        break
    con.close() #fechando a conexao
