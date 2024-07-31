inventario = []
resposta = "S"
while resposta == "S":
    equipamento = [input("Equipamento..: "), float(input("Valor..: ")), int(input("Serial..: ")), input("Departamento")]
    inventario.append(equipamento)
    resposta = input("Deseja adicionar mais um item ao inventario? (S/N): ").upper()

for elemento in inventario:
    print("Nome..: ", elemento[0])
    print("Valor..: $", elemento[1])
    print("Serial..: ", elemento[2])
    print("Departamento..: ", elemento[3])
    print("---------------------------------")

#pesquisar elemento na lista
busca = input("Digite o nome do equipamento que deseja buscar: ")
for elemento in inventario:
    if busca == elemento[0]:
        print("Valor..: $", elemento[1])
        print("Serial..: ", elemento[2])

#elemento a ser depreciado

depreciacao = input("Digite o nome do equipamento que será depreciado: ")
for elemento in inventario:
    if depreciacao == elemento[0]:
        print("Valor actual..: ", elemento[1])
        elemento[1] = elemento[1] * 0.9
        print("Valor de Depreciacao..: ", elemento[1])

#elemento a ser excluido
serial = int(input ("Digite o serial do equipamento a ser excluido: "))
for elemento in inventario:
    if elemento[2] == serial:
        inventario.remove(elemento)
        print("Equipamento excluido com sucesso")

#atualizar inventario
print("\nInventario Atualizado:")
for elemento in inventario:
    print("Nome..: ", elemento[0])
    print("Valor..: $", elemento[1])
    print("Serial..: ", elemento[2])
    print("Departamento..: ", elemento[3])
    print("---------------------------------")

valores=[]
for elemento in inventario:
  valores.append(elemento[1])
if len(valores)>0:
  print("O equipamento mais caro custa: ", max(valores))
  print("O equipamento mais barato custa: ", min(valores))
  print("O total de equipamentos é de: ", sum(valores))