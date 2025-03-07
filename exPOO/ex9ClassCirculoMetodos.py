class Circulo ():
    pi = 3.14
    def __init__(self, raio = 5):
        self.raio = raio
        
    #metodo para calcular a area
    def area(self):
        return (self.raio * self.raio) * Circulo.pi
    #metodo para alterar o raio
    def setRaio(self, novo_raio):
        self.raio = novo_raio
        
    #metodo para obter o raio
    def getRaio(self):
        return self.raio

#instanciando a classe
circ = Circulo()
#print("O raio é: ", circ.getRaio())
circ1 = Circulo(7)
print("O raio é: ", circ1.getRaio())
print("A area é: ", circ1.area())
