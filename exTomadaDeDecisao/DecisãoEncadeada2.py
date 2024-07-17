'''
Author: francis_bowe franciscodomingos20155@gmail.com
Date: 2024-07-17 23:05:07
LastEditors: francis_bowe franciscodomingos20155@gmail.com
LastEditTime: 2024-07-17 23:36:48
FilePath: exTomadaDeDecisao/DecisãoEncadeada2.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
'''

nome = input("Digite Nome")
idade = int (input("Digite idade"))
doenca_contagiosa = input("Exite supeita se doença contagiosa?").upper()

#Primeiro problema a ser resolvido

if doenca_contagiosa == "SIM":
    print("Para sala A")
elif doenca_contagiosa == "NAO":
    print("Para sala B")
else:
    print("Responda sobre doença conatgiosa com SIM/NAO")
    
#Segundo Problema a ser resolvido
if idade >= 65:
    print("Com Prioridade")
else:
    genero = input("Digite Genero").upper()
    if genero == "F" and idade > 10:
        gravidez = input("Está gravida?").upper()
        if gravidez == "SIM":
            print("com Prioridade")
        else:
            print("sem Prioridade")
    else:
        print("Sem Prioridade")