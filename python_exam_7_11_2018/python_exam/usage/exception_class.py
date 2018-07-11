from parent_child.parent import parent

class how_to_define_exception_class(parent, Exception):
    def __init__(self,value):
        self.value=value

    def __str__(self):
        return repr(self.value)

    def __doc__(self):
        return "This class name is test."


print("*********** how to define and use your own exception class.***********")
try:
    raise (how_to_define_exception_class(100))
except how_to_define_exception_class as t:
    print("t={},t.value={}".format(t, t.value))
else:
    print("no except")
finally:
    print("done with except")

print("issubclass ******** issubclass(test3,test)={}".format(issubclass(how_to_define_exception_class, parent)))
