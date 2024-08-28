from fucoes.funcoes_Arquivo import *

inventario = {}
option = showMenu ()

while option > 0 and option < 5 :
    if option == 1:
        register(inventario)
    elif option == 2:
        saveInventory(inventario)
    elif option == 3:
        result = loadInventory()
        #vai apresentar todos os dados do inventario
        #menos o id será cortado no 1º ;
        for line in result:
            list = line.split(";")
            print("Data......", list[1])
            print("Descrição..", list[2])
            print("Departamento..", list[3])
            print("---------------------------------")
    elif option == 4:
        patrimonial = input("Digite o nºs Patrimonial para pesquisar: ")
        searchInventory(inventario,patrimonial)

    option = showMenu ()


