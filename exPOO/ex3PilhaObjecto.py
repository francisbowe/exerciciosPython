class stack :
    def __init__(self): #construtor de um novo objecto
        #self.stack_list = []
        self.__stack_list = [] # __stack_list é um atributo privado __para tornar privado
    
    def push(self, val):
        self.__stack_list.append(val)
    
    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val
        
stack_obj = stack()

stack_obj.push(3)
stack_obj.push(2)
stack_obj.push(1)
print(stack_obj.pop())
print(stack_obj.pop())
print(stack_obj.pop())
         