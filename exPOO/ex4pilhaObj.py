class stack :
    def __init__(self): 
        self.__stack_list = []
    
    def push(self, val):
        self.__stack_list.append(val)
    
    def pop(self): 
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val
class addStack(stack):
    def __init__(self):
        stack.__init__(self)
        self.__sum = 0
    def getSum(self):
        return self.__sum
    def push(self, val):
        self.__sum += val
        stack.push(self, val)
    def pop(self):
        val = stack.pop(self)
        self.__sum -= val
        return val

stack_obj = addStack()
for i in range(5):
    stack_obj.push(i)
print(stack_obj.getSum())
for i in range(5):
    print(stack_obj.pop())
    
#little_stack = stack() 
#another_stack = stack()
#funny_stack = stack()

#little_stack.push(1)
#another_stack.push(little_stack.pop() + 1)
#funny_stack.push(another_stack.pop() - 2)
#print(funny_stack.pop())