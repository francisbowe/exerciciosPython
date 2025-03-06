#criando a classe
class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        
    def dados(self):
        print("Funcionario %s tem salario de %d" %(self.nome, self.salario))

fun1 = Funcionario("Bowe", 1000)
fun1.dados()
fun2 = Funcionario("Lisa", 2000)
fun2.dados()