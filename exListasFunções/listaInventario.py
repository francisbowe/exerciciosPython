#criando uma lista de inventario
inventario = []
resposta = "S"

#loop para adicionar itens ao inventario
while resposta == "S":
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: $")))
    inventario.append(int(input("N* Serial: ")))
    inventario.append(input("Departamento: "))
    resposta = input("Deseja adicionar mais um item ao inventario? (S/N): ").upper()

#mostrando o inventario
for elemento in inventario:
    print(elemento)