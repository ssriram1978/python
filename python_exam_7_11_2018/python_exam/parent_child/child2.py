class Stack:
    __stack=[]
    def __init__(self):
        pass

    def push(self,val):
        Stack.__stack.append(val)

    def pop(self):
        return Stack.__stack.pop()


class DerivedStack(Stack):
    def __init__(self):
        self.__sum=0

    def push(self,val):
        self.__sum+=val
        Stack.push(self,val)

    def pop(self):
        val=Stack.pop(self)
        self.__sum-=val
        return val

    def sum(self):
        return self.__sum

obj=DerivedStack()
for index in range(10):
    obj.push(index)

print("sum={}".format(obj.sum()))

for index in range(10):
    obj.pop()

print("sum={}".format(obj.sum()))

class Stack2:
    def __init__(self):
        self.__stack=[]
    
    def push(self,val):
        self.__stack.append(val)

    def pop(self):
        return self.__stack.pop()

class DerivedStack2(Stack2):
    def __init__(self):
        super().__init__()
        self.__sum=0

    def push(self,val):
        self.__sum+=val
        Stack.push(self,val)

    def pop(self):
        val=Stack.pop(self)
        self.__sum-=val
        return val

    def sum(self):
        return self.__sum

obj=DerivedStack2()
for index in range(10):
    obj.push(index)

print("sum={}".format(obj.sum()))

for index in range(10):
    obj.pop()

print("sum={}".format(obj.sum()))
