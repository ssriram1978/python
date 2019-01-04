

class Class1:

    __instance = None

    def __new__(cls, value=10):
        if not Class1.__instance:
            Class1.__instance = object.__new__(cls)
            Class1.__instance.value = value
        return Class1.__instance

    def __init__(self, value=10):
        self.value = value

    def __getattr__(self, name):
        return getattr(self.__instance, name)


    @classmethod
    def print_value(cls):
        print("classmethod: Class1.__instance.value={}.".format(Class1.__instance.value))

    @staticmethod
    def print_value2():
        print("staticmethod: Class1.__instance.value={}.".format(Class1.__instance.value))

if __name__ == "__main__":
    cls_instance = Class1()
    print("instance={},value={}"
          .format(repr(cls_instance),cls_instance.value))
    cls_instance2 = Class1()
    print("instance={},value={}"
          .format(repr(cls_instance2), cls_instance2.value))
    cls_instance.value=20
    print("instance={},value={}"
          .format(repr(cls_instance2), cls_instance2.value))
    Class1.print_value()
    cls_instance.print_value()
    cls_instance2.print_value()
    Class1.print_value2()
    cls_instance.print_value2()
    cls_instance2.print_value2()