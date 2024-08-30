import json
inventario ={}
with open ("inventario_json.json", "r") as arq_json :
    inventario = json.load(arq_json)
opcao = int (input("Digite: \n" + "<1> Para registrar \n" + "<2> Para exibir em arquivo \n :"))

while opcao > 0 and opcao < 3 :
    if opcao == 1:
        resp = "S"
        while resp == "S":
            inventario[input("Digite o numero patrimonial:")] = [
                input("Digite a data da ultima patrimonial: "),
                input("Digite a descricao: "),
                input("Digite o deparatmento: ")
            ]
            resp = input("Deseja adicionar mais um produto? (S/N): ").upper()
        with open("inventario_json.json", "w") as arq_json :
            json.dump(inventario, arq_json)
            print("Json Persistido com Sucesso")
    elif opcao == 2:
        with open ("inventario_json.json", "r") as arq_json :
            resultado = json.load(arq_json)
            for chave, dado in resultado.items():
                print("Data......", dado [0])
                print("Descrição..", dado [1])
                print("Departamento..", dado [2])
                print("---------------------------------")
    opcao = int (input("Digite: \n" + "<1> Para registrar \n" + "<2> Para exibir em arquivo \n :"))