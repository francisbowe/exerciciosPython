class Livro ():
    def __init__(self, titulo, isbn):
        #atributos sao propriedads
        self.titulo =titulo
        self.isbn =isbn
        print("Construtor chamado para criar objecto desta class")
    #metodos sao funcao que executam acoes nos objectos da classe
    def imprime(self):
        print("Foi criado o livro %s e ISBN %d" %(self.titulo, self.isbn))

Livro1 = Livro("O Poder do Habito", 1234)

Livro1.imprime()