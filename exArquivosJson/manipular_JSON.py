from fucoes.funcoes_Json import *

invetario = ler_arquivo ("inventario_json.json")
opcao = chamarMenu()

while opcao > 0 and opcao < 4:
    if opcao == 1:
        print (resgistrar(invetario, "inventario_json.json"))
    elif opcao == 2:
        exibe_arquivo("inventario_json.json")
    opcao = chamarMenu ()