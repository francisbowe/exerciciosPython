def add_number (list):
    resp = "S"
    while resp == "S":
        num = float(input("Digite um número: "))
        list.append(num)
        resp = input("Deseja adicionar mais um número? (S/N): ").upper()
def remove_number (list):
    num_remove = float(input("Digite o número a ser removido: "))
    if num_remove in list:
        list.remove(num_remove)
    else:
        print("Número não encontrado na lista.")
    return "Numero Exculido com sucesso"
def show_list (list):
    print("Elementos da lista:")
    for indice in range (0, len(list)):
        print("Element", (indice +1))
def invert (list):
    list.reverse()
    return list