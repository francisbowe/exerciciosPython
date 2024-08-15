def showMenu ():
    option = int(input("Digite: \n" + "<1> Para registrar \n" + "<2> Para persistir em arquivo\n" + "<3> Para exibir os activos armazenados \n " + "<4> Digite nº Patrimonial para pesquisar \n :"))
    return option
def register (inventory):
    resp = "S"
    while resp == "S":
        inventory[input("Digite o numero patrimonial: ")] = [
            input("Digite a data da ultima patrimonial: "),
            input("Digite a descricao: "),
            input("Digite o deparatmento: ")
        ]
        resp = input("Deseja adicionar mais um produto? (S/N): ").upper()
def saveInventory (inventory):
    with open("inventario.csv", "a") as file:
        for patrimonial, data in inventory.items():
            file.write(f"{patrimonial};{data[0]};{data[1]};{data[2]}\n")
    return "Persistido com Sucesso"
def loadInventory ():
    with open("inventario.csv", "r") as file:
        line = file.readlines()
    return line
def searchInventory (inventory, patrimonial):
    lists = inventory.get(patrimonial)
    if lists is not None:
        print("Nome...........: " + lists[1])
        print("Ultima data..: " + lists[0])
        print("Descrição....: " + lists[1])
        print("Departamento..: " + lists[2])