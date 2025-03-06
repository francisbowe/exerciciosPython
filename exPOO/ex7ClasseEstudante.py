class Estudante():
    def __init__(self,nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota
        print("Construtor chamado para criar objecto desta class")
        
Estudante1 = Estudante('Bowe', 27, 18)
Estudante2 = Estudante('Lisa', 23, 16)

print(Estudante1.nome + " tem " + str(Estudante1.idade) + " anos e obteve " + str(Estudante1.nota) + " valores")
print(Estudante2.nome + " tem " + str(Estudante2.idade) + " anos e obteve " + str(Estudante2.nota) + " valores")