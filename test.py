
class test():
    __arg1="static arg"

    def __init__(self, argument):
        self.arg2=argument

    def function1(self, argument2):
        self.arg3=argument2

    def function2(self):
        print(self.__arg1 + self.arg2 + self.arg3)



object=test("Sriram")
object.__arg1="Sriram2"
object.arg2 = "Sridhar"
object.function1("Nithya")
object.function2()


object2=test("Hello")
object2.function1("world")
object2.function2()