import os
from ftplib import *

def escreverLinha(data):
    arq.write(data)
    arq.write(os.linesep)

ftp_activo = True # a variável está com valor True para representar conexão activa
ftp = FTP('ftp.ibiblio.org') # conectando ao servidor FTP
print(ftp.getwelcome()) 
ftp.login()
ftp.set_pasv(ftp_activo)

# Listar arquivos no diretório atual do servidor FTP
ftp.retrlines('LIST')

arquivo = 'README'
with open(arquivo, 'w') as arq:
    ftp.retrlines('RETR README', escreverLinha)
ftp.quit()
print("Arquivo ", arquivo, " criado com sucesso")