from ftplib import *
import getpass
ftp_activo = False #a varivael esta com valor False pois representa conexao passiva
ftp = FTP('ftp.ibiblio.org') #conectando ao servidor FTP
print(ftp.getwelcome()) #metodo welcome exibe a mensagem de boas vindas
user = input("Username: ")
password = getpass.getpass ("Password: ")
ftp.login(user, password) #metodo login para autenticacao
print("Diretorio atual de trabalho: ", ftp.pwd()) #metodo pwd exibe o diretorio atual
ftp.cwd('pub') #metodo cwd muda o diretorio de trabalho
print("Diretorio corrente: ", ftp.pwd())
ftp.quit()

