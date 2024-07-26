respsota ="SIM"

while respsota=="SIM":
    nome = input("Digite o nome do paciente")
    doenca_contagiosa =input("Exite sintomas de doença contagiosa?").upper()
    idade = int (input ("Digite a Idade do Paciente"))

# PRIMEIRO PROBLEMA A SER RESOLVIDO
    while doenca_contagiosa!="SIM" and doenca_contagiosa!="NAO":
        print ("Digite SIM OU NAO")
        doenca_contagiosa =input("Exite sintomas de doença contagiosa?").upper()

    if doenca_contagiosa=="SIM":
        print("Encaminhe o paciente para sala AMARELA")
    else:
        print("Encaminhe o paciente para sala BRANCA")

    # SEGUNDO PROBLEMA A SER RESOLVIDO
    if idade >= 65:
        print("Paciente COM prioridade")
    else:
        genero=input("Digite o gênero do paciente: ").upper()
        if genero=="FEMININO" and idade>10:
            gravidez=input("A paciente está grávida? ").upper()
            if gravidez=="SIM":
                print("Paciente COM prioridade")
            else:
                print("Paciente SEM prioridade")
        else:
            print("Paciente SEM prioridade")
    resposta = input("Degite SIM se deseja continuar").upper()