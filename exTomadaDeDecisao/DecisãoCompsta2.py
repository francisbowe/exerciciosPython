'''
Author: francis_bowe franciscodomingos20155@gmail.com
Date: 2024-07-17 21:57:16
LastEditors: francis_bowe franciscodomingos20155@gmail.com
LastEditTime: 2024-07-17 22:29:35
FilePath: exTomadaDeDecisao/DecisãoCompsta2.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
'''

nome = input("Digite nome")
idade = int(input("Digite Idade"))
doenca_contagiosa = input("Existe supeita de doença contagiosa?").upper()

if idade >= 65 and doenca_contagiosa == "SIM":
    print("o paciente " + nome + " deve ser direcionado para sala *A* com prioridade")
elif idade < 65 and doenca_contagiosa == "SIM":
    print("o paciente " + nome + " deve ser direcionado para sala *A* sem prioridade")
elif idade >= 65 and doenca_contagiosa == "NAO":
    print("o paciente " + nome + "deve ser direcionado para sala *B* com prioridade")
elif idade < 65 and doenca_contagiosa == "NAO":
    print("o paciente" + nome + "deve ser direcionado para sala *B* sem prioridade")