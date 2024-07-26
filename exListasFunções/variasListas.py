#exercicio criando e mostrando dados de varias listas
#criando listas
lista_equioamento = []
lista_valor = []
lista_serial = []
lista_deparatmento =[]

#adicionando dados a listas
resposta = "S"
while resposta == "S":
    lista_equioamento.append(input("Digite o nome do equipamento: "))
    lista_valor.append(float(input("Digite o valor do equipamento: $")))
    lista_serial.append(int(input("Digite o número de série do equipamento: ")))
    lista_deparatmento.append(input("Digite o departamento do equipamento: "))
    resposta = input("Deseja adicionar mais um equipamento? (S/N): ").upper()

#mostrando dados das listas
'for elemneto in lista_equioamento, lista_valor, lista_serial, lista_deparatmento:   print(elemneto)'
for indice in range(0, len(lista_equioamento)):
    print(f"Equipamento: {lista_equioamento[indice]}, Valor: ${lista_valor[indice]}, Serial: {lista_serial[indice]}, Departamento: {lista_deparatmento[indice]}")
    
#pesquisar elemento na lista
busca=input("Digite o nome do equipamento que deseja buscar: ")
for indice in range(0,len(lista_equioamento)):
  if busca==lista_equioamento[indice]:
    print("Valor..: ", lista_valor[indice])
    print("Serial.:", lista_serial[indice])