from funcoes.indentificadoresFunções import *
minhaLista=[]

# Adicionando valores a lista
print("Adicionando")
preencherInventario(minhaLista)
# Mostrando o inventario
print("Exibindo")
mostrarInventario(minhaLista)
# Localizando um item na lista
print("Localizando")
localizarPorNome(minhaLista)
# Depreciando um item na lista
print("Depreciando")
depreciarPorNome(minhaLista, 20)
# Excluindo um item da lista
print("Excluindo")
print(excluirPorSerial(minhaLista))
# Resumindo valores
print("Resumindo")
resumirValores(minhaLista)

print("Fim")

# Para testar as funções, basta chamar as funções passando a lista como argumento.