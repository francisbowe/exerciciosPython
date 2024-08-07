ips = {}
resp = "S"
while resp == "S":
    ips[(input("Digite os dois primeiros Octetos: "), input("Digite os dois ultimos octectos: "))]= input("Nome da maquina: ")
    resp = input("Deseja adicionar mais uma maquina? (S/N): ").upper()

print ("Exibindo IP's: ")
for ip in ips.keys():
    print(f"{ip[0]}.{ip[1]} {ips[ip]}")  #

print ("Exibindo máquinas com mesmo endereço: ")
pesquisa = input("Digite dois ultimos octetos: ")
for ip, nome in ips.items():
    print("Máquinas no mesmo endereço (redes diferentes")
    if (ip[1] == pesquisa):
        print(f"{ip[0]}.{ip[1]} {nome}")
print("Máquinas que compoem estações de uma rede")
rede = input("Digite os dois primeiros octectos")
for ip, nome in ips.items():
    print("Maquinas na mesma estações")
    if (ip[0] == rede):
        print(f"{ip[0]}.{ip[1]} {nome}")