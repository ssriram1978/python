def decorator(inner_fn):
    def deco_fn(*args,**kwargs):
        print("Do something before invoking inner fn\n")
        inner_fn(args,kwargs)
        print("Do something after invoking inner_fn")
    return deco_fn

@decorator
def decorator_method_invocation(self, *args, **kwargs):
    print("iterating args...\n")
    for arg in args:
        print(arg, end=" ")
    print("\n All done iterating args in fn3")
    for name, value in kwargs:
        print("name=%s and value=%s\n" % (name, value))


dict1 = {"1": "sriram", "2": "sridhar"}
decorator_method_invocation(1, 2, 3, **dict1)

