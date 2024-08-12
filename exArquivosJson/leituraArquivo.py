with open ("teste.txt", "r") as arquivo :
    conteudo = arquivo.readlines()
print ("Tipo de dados da variável", type(conteudo))
print("Conteúdo do arquivo ", conteudo)