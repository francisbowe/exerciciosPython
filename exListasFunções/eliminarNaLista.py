#Algoritmo que mostra a depreciação de todos os protudos

impressora = []
serial = []
valor = []

resposta = "S"
#adicionando dados a listas
while resposta == "S":
    impressora.append(input("Digite o nome da impressora: "))
    serial.append(int(input("Digite o numero de serie: ")))
    valor.append(float(input("Digite o valor do produto: $")))
    resposta = input("Deseja adicionar mais um produto? (S/N): ").upper()

#mostrando dados das listas
for indice in range (0, len(impressora)):
    print("Equipamentos..: ", (indice+1))
    print("Nome da Impressora..: ", impressora[indice])
    print("Número de Série..: ", serial[indice])
    print("Valor do Produto..: $", valor[indice])
    print("---------------------------------")

#eliminar um elemento na lista
indice_apagar = input("Qual indice deseja apagar? ")
for indice in range (0, len(impressora)):
    if impressora[indice] == indice_apagar :
        del impressora[indice]
        del serial[indice]
        del valor[indice]
        break

#mostrando dados das listas após exclusão
print("\nDados após exclusão:")
for indice in range (0, len(impressora)):
    print("Equipamentos..: ", (indice+1))
    print("Nome da Impressora..: ", impressora[indice])
    print("Número de Série..: ", serial[indice])
    print("Valor do Produto..: $", valor[indice])
    print("---------------------------------")