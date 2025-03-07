#superclasse - em polimorfismo so usamos o construtor na superclasse
class Veiculo ():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def acelerar(self):
        pass
    def frear(self):
        pass
    
#subclasse carro
class Carro(Veiculo):
    def acelerar(self):
        print("Carro acelerando")
    def frear(self):
        print("Carro freando")
#subclasse moto
class Moto(Veiculo):
    def acelerar(self):
        print("Moto acelerando")
    def frear(self):
        print("Moto freando")
#subclasse aviao
class Aviao(Veiculo):
    def acelerar(self):
        print("Aviao acelerando")
    def frear(self):
        print("Aviao freando")
    def decolar(self):
        print("Aviao decolando")

#criando objetos
lista_veiculos = [Carro("Ford", "Fiesta"), Moto("Honda", "Biz"), Aviao("Boeing", "747")]
for inten in lista_veiculos:
    inten.acelerar()
    inten.frear()
    if isinstance(inten, Aviao):
        inten.decolar()
    print("-------")