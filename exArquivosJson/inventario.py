inventario = {}
option = int ( input("Digite: " + "<1> Para registrar activo \n" + "<2> Para persistir em arquivo \n" + "<3>  Para exibir activos aramazenados \n :"))

while option > 0 and option < 4 :
    if option == 1:
        resp = "S"
        while resp == "S":
            inventario[input("Digite o numero patrimonial: ")] = [
                input("Digite a data da ultima patrimonial: "),
                input("Digite a descricao: "),
                input("Digite o deparatmento: ")
            ]
            resp = input("Digite <S> para continuar.").upper()
    elif option == 2:
        with open("inventario.csv", "a") as inv:
            for chave, valor in inventario.items():
                inv.write(chave + ";" + valor [0] + ";" + valor [1] + ";" +valor[2]+"")
                print("Persistido com sucesso!")
    elif option == 3:
        with open("inventario.csv", "r") as inv:
            print(inv.readlines())
    option = int( input("Digite: " "<1> Para registrar activo \n" "<2> Para persistir em arquivo \n" "<3>  Para exibir activos aramazenados \n :"))
chave = input("Digite o numero patrimonial para pesquisar: ")

