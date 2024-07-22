
resposta="SIM"
while resposta == "SIM":
    nivel = input("Digite o nivel de acesso: ").upper()
    if nivel == "ADM" or nivel == "USR":
        genero = input("Digite o seu geneo")
        if nivel == "ADM":
            if genero == "f":
                print ("Ola adminstradora")
            else:
                print ("Ola Adminstrador")
        else:
            if genero == "f":
                print ("Ola usuaria")
            else:
                print ("ola usuario")
    elif nivel == "GUEST":
        print("Ola visita")
    else:
        print("Ola descilhencido")
    resposta= input("Digite SIM para continuar: ").upper()
    