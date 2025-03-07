#criando a calsse Animal - superclasse
class Animal ():
    def  __init__(self):
        print("Animal criado")
    
    def imprimir(self):
        print("Animal")
    def comer(self):
        print("Comendo")
    def emitir_som(self):
        pass
    
#criando a classe Cachorro - subclasse
class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Objeto Cachorro criado")
    
    def emitir_som(self):
        print("Au Au")

#Criando a classe Gato - subclasse
class Gato(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Objeto Gato criado")
    
    def emitir_som(self):
        print("Miau")

#criando um objectos (instanciando a classe)
rex = Cachorro()
zeze = Gato()
rex.emitir_som()
zeze.emitir_som()
rex.imprimir()
zeze.imprimir()
rex.comer()
zeze.comer()