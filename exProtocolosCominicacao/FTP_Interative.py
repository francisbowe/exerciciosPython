import os
import getpass
from ftplib import *
ftp_activo = True # a variável está com valor False para representar conexão passiva
ftp = FTP(input('Digite o FTP que se desja conecatar: ')) # conectando ao servidor FTP
print(ftp.getwelcome())
user = input('Digite o usuário: ')
password = getpass.getpass('Digite a senha: ')
ftp.login(user, password)
print("Conexao sucedida \n Diretório atual: ", ftp.pwd())

menu = "1"
while menu == "1" or menu=="2" or menu=="3":
    menu = input("Digite uma opcao desejada: /n <1> Para listar os arquivos /n <2> Para definir directorio /n <3> Para baixar arquivo /n")
    if menu == "1":
        print(ftp.dir())
    elif menu == "2":
        ftp.cwd(input("Digite o directorio que deseja acessar: "))
        print("Diretorio atual: ", ftp.pwd())
    elif menu == "3":
        tipo = input("Digite o tipo de arquivo que deseja baixar: /n <1> Binario  /n <2> ASCII  /n")
        if tipo == "1":
            with open(input("Dgite nome de aequivo: "), "wb") as arq:
                ftp.retrbinary('RETR ' + input("Digite o nome do arquivo de origem: "), arq.write)
        else:
            with open(input("Dgite nome de aequivo: "), "w") as arq:
                def escreverLinha(data):
                    arq.write(data)
                    arq.write(os.linesep)
                ftp.retrlines('RETR ' + input("Digite o nome do arquivo de origem: "), escreverLinha)
        print("Arquivo baixado com sucesso")
ftp.quit()
