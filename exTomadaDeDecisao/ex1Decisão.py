'''
Author: francis_bowe franciscodomingos20155@gmail.com
Date: 2024-07-17 23:46:15
LastEditors: francis_bowe franciscodomingos20155@gmail.com
LastEditTime: 2024-07-18 00:04:37
FilePath: exTomadaDeDecisao/ex1Decisão.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
'''

nivel_acesso = input("Digite o nivel de acesso").upper()


if nivel_acesso == "ADM" or nivel_acesso == "USR":
    genero = input("Digite o genero").upper()
    if nivel_acesso == "ADM":
        if genero == "F":
            print("Ola Adminstradora")
        else:
         print("Ola Adminstrador")
    else:
        if genero == "F":
            print("Ola Usuaria")
        else:
            print("Ola Usuario")
elif nivel_acesso == "GUEST":
    print("Ola visitante")
else:
    print("ola desconhecido")
    