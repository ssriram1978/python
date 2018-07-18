class super:
    def fn1(self):
        print("super fn1")
    def fn2(self):
        print("super fn2")

class derived(super):
    def fn1(self):
        print("derived fn1")
    def fn2(self):
        print("derived fn2")

class derived2(derived):
    def fn3(self):
        print("derived3 fn3")
    def fn2(self):
        print("derived2 fn2")

class base():
    def fn2(self):
        print("base fn2")

class derived3(base,derived):
    def fn3(self):
        print("derived3 fn3")

class derived4(derived,base):
    def fn3(self):
        print("derived4 fn3")


obj=derived2()
obj.fn1()
obj.fn2()

obj2=derived3()
obj2.fn1()
obj2.fn2()

obj3=derived4()
obj3.fn1()
obj3.fn2()
