usuarios = {}
resp = "S"
email = []

while resp == "S":
    email.append(input("Dgite um e-mail: ").lower())
    resp = input("Deseja adicionar mais um e-mail? (S/N): ").upper()

tupla = list(enumerate(email))
for chave in range(0, len(tupla)):
    print("Email: ", tupla[chave][1])
    usuarios [tupla[chave]]=[input("Digite o nome"), input("Digite o Nivel")]
    
for chave,dado in usuarios.items():
    print("Usuario.:", chave[0])
    print("Email...: ",chave[1])
    print("Nome....: ", dado[0])
    print("Nível...: ", dado[1])