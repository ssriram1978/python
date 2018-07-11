
class parent:
    class_global_var = 1

    def __init__(self, *args):
        """
        module documentation:
        This is __init__of parent class.
        """
        print("__class__=%s file_name=%s, method_name=%s is getting invoked." % (
        __class__, __name__, self.__init__.__name__))
        self.__name_mangled_fn(*args)
        self.__hidden_var = "world"

    @staticmethod
    def static_method_invocation():
        print("static method invocation")

    @classmethod
    def class_method_invocation(cls):
        print("class method. cls.var1=%d" % (cls.class_global_var))

    # global, nonlocal keyword variables
    def bad_method_to_change_global_var(self):
        module_global_var = "world"

    # global, nonlocal keyword variables
    def correct_method_to_change_global_module_var(self):
        global module_global_var
        module_global_var = "world"

    def hidden_function(self):
        print("I am hidden and name mangled")

    # assign the hidden function to the hidden variable and invoke this in the constructor.
    __name_mangled_fn = hidden_function

    # nonlocal variables
    def nonlocal_variable_invocation_method(self):
        nonlocal_var = 123
        print("Before invoking nonlocal var1={}".format(nonlocal_var))

        def nonlocalvar_fn():
            nonlocal nonlocal_var
            nonlocal_var = 1000

        nonlocalvar_fn()
        print("After invoking nonlocal var1={}".format(nonlocal_var))

    def pass_by_value_method(self, variable):
        variable = 123

    def __str__(self):
        return "test"

if __name__=="__main__":
    print("********** Invoking a static member fn. test.fn1 ****************")
    parent.static_method_invocation()
    print("************* Invoking object function. obj.fn1 ****************")
    obj = parent()
    obj.static_method_invocation()

    module_global_var= "Hello"
    print("parent.class_global_var={} and module_global_var={}".format(parent.class_global_var, module_global_var))
    obj.bad_method_to_change_global_var()
    print("After obj.bad_method_to_change_global_var(),module_global_var={}".format(module_global_var))
    obj.correct_method_to_change_global_module_var()
    print("After obj.correct_method_to_change_global_module_var(),module_global_var={}".format(module_global_var))
    parent.class_global_var=100
    print("After changing the global variable in parent,class_global_var={},obj.class_global_var={}".format(parent.class_global_var,obj.class_global_var))


    print("************ Demonstrating nonlocal_variable_invocation_method. *************")
    obj.nonlocal_variable_invocation_method()
    print("Demonstrating pass by copy/reference")
    variable1 = 12
    print("Before invoking obj.pass_by_value_method, variable1={}".format(variable1))
    obj.pass_by_value_method(variable1)
    print("After invoking obj.pass_by_value_method, variable1={}".format(variable1))

    # data attributes - instance variables because each object has its own namespace.
    obj2 = parent()
    obj2.x = "123"
    obj.y = "345"
    print("Adding new instance variables obj2.x={}".format(obj2.x))
    print("Adding new instance variables obj.y={}".format(obj.y))


    print("**************** Demonstrating parent.class_method_invocation() *****************")
    parent.class_method_invocation()

    print("**************** Demonstrating obj.class_method_invocation() *****************")
    obj.class_method_invocation()

    print("**************** Demonstrating how hidden variables in an object cannot be accessed.) *****************")
    try:
        print("obj.__hidden_var={}".format(obj.__hidden_var))
    except AttributeError:
        print("This is a demo of how hidden variables \"print(obj.__hidden_var)\" in an object cannot  be accessed.")
    finally:
        print("Finally do the cleanup")

    print("type ******** type(obj)={}".format(type(obj)))

    print("isinstance ******** isinstance(obj,test)={}".format(isinstance(obj, parent)))
    print("isinstance ******** isinstance(obj2,test)={}".format(isinstance(obj2, parent)))

    print("issubclass ******** issubclass(test,test)={}".format(issubclass(parent, parent)))

    print("issubclass ******** hasattr(obj,'var1')={}".format(hasattr(obj, 'var1')))
    print("issubclass ******** hasattr(obj,'fn2')={}".format(hasattr(obj, 'fn2')))
    print("type ******** type(obj.fn2)={}".format(type(obj.class_method_invocation)))

    print("********** Demonstrating how to use __str__:print(obj)")
    print(obj)
    print("********** Demonstrating how to use __str__:print(parent)")
    print(parent)

    print("---------Parent class variables.---------------")
    print("Printing test.__dict__={}".format(parent.__dict__))
    print("Printing test.__module__={}".format(parent.__module__))
    print("Printing test.__bases__={}".format(parent.__bases__))
    print("---------Printing object variables.---------------")
    print("Printing obj.__dict__={}".format(obj.__dict__))
    print("Printing obj.__module__={}".format(obj.__module__))
    # print("Printing obj.__bases__={}".format(obj.__bases__))
