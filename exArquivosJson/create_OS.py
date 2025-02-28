import os

texto = "example text created by python \n"
texto += "another line for example \n"
texto += "another line for example 3 \n"

# Cria um arquivo chamado "example.txt"
arquivo = open(os.path.join('example.txt'), 'w')
for line in texto.splitlines():
    arquivo.write(line + '\n')
arquivo.close()

# Lê o conteúdo do arquivo 
arquivo = open('example.txt', 'r')
conteudo =arquivo.read()
arquivo.close()
print(conteudo)
    