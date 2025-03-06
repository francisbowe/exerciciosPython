class Algoritmo ():
    def __init__(self, tipo_algo):
        self.tipo = tipo_algo
        print("Construtor chamado para criar objecto desta class")
    
#crando um objecto a partir da classe
algo1 = Algoritmo(tipo_algo='Busca em Largura')
print(algo1.tipo)
algo2 = Algoritmo(tipo_algo='Deep Learning')
print(algo2.tipo)

#atribuindo objecto a partir da classe
algo1.tipo
algo2.tipo