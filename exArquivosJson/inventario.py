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
        for line in result:
            print(line [line.find(";")+ 1:-1])
    elif option == 4:
        patrimonial = input("Digite o nº Patrimonial para pesquisar: ")
        searchInventory(inventario,patrimonial)

    option = showMenu ()


