from parent_child.parent import parent

class child(parent):
    class_global_var = 100

    def __init__(self):
        """
        module documentation:
        This is __init__of child class.
        """
        print("__class__=%s file_name=%s, method_name=%s is getting invoked." % (
        __class__, __name__, self.__init__.__name__))

        self.name = "xyz"

    def getname_defined_locally_in_this_instance(self):
        return self.name

    def bad_method_to_change_global_var(self):
        print("Demonstrating virtual method")

    def __str__(self):
        return "test2"


print("Invoking classmethod defined in the parent class which access child class variable.")
obj3 = child()
obj3.class_method_invocation()
obj3.bad_method_to_change_global_var()
print("********** Demonstrating how to use __str__: print(obj3)")
print(obj3)
print("isinstance ******** isinstance(obj3,test)={}".format(isinstance(obj3, parent)))
print("issubclass ******** issubclass(test2,test)={}".format(issubclass(child, parent)))
print("issubclass ******** issubclass(test,test2)={}".format(issubclass(parent, child)))
print("isinstance ******** isinstance(obj,test2)={}".format(isinstance(obj3, child)))
