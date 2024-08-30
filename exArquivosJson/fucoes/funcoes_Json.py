import json
import os

def chamarMenu ():
    escolha = int (input("Digite: \n" + "<1> Para registrar \n" + "<2> Para exibir em arquivo \n :"))
    return escolha

def ler_arquivo (arquivo):
    if os.path.exists(arquivo) :
        with open (arquivo, "r") as arq_json :
            inventario = json.load(arq_json)
    else :
        inventario = {}
    return inventario

def gravar_arquivo (arquivo, inventario):
    with open (arquivo, "w") as arq_json :
        json.dump(inventario, arq_json)

def resgistrar (dicionario, arquivo):
    resp = "S"
    while resp == "S":
        dicionario[input("Digite o numero patrimonial:")] = [
            input("Digite a data da ultima patrimonial: "),
            input("Digite a descricao: "),
            input("Digite o deparatmento: ")
        ]
        resp = input("Deseja adicionar mais um produto? (S/N): ").upper()
        gravar_arquivo(arquivo, dicionario)
    return "Json gerado!!!!"

def exibe_arquivo (arquivo):
    dicionario = ler_arquivo(arquivo)
    for chave, dado in dicionario.items():
        print("Data......", dado [0])
        print("Descrição..", dado [1])
        print("Departamento..", dado [2])
        print("---------------------------------")
