'''
Author: francis_bowe 
Date: 2024-07-17 21:50:13
LastEditors: francis_bowe franciscodomingos20155@gmail.com
LastEditTime: 2024-07-17 21:56:30
FilePath: exTomadaDeDecisao/DecisãoComposta.py
Description: primeiro exerccio de decisão composta
'''

nome = input("Digite nome")
idade = int(input("Digite Idade"))

if idade>=65:
    print("o Paciente: " + nome + " tem prioridade")
else:
    print("o Paciente: " + nome + "tem prioridade")