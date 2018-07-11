from parent_child.child import child
class how_to_use_super(child):
    def __init__(self):
        print("__class__=%s file_name=%s, method_name=%s is getting invoked."%(__class__,__name__,self.__init__.__name__))
        super().__init__()
        print("super().getname()={}".format(super().getname_defined_locally_in_this_instance()))


