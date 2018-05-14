import re
from datetime import datetime

"""
function decorators are executed as soon as the module is imported, 
but the decorated functions only run when they are explicitly invoked. 
This highlights the difference between what Pythonistas call import time and run time.
"""
def deco_outer_function(func):
    print("Deco outer function")
    def deco_inner_fn(*args):
        result=0
        result=func(args)
        name=func.__name__
        now = datetime.now()
        format(now, '%H:%M:%S')
        arg_str=str(now)
        arg_str+=','.join(repr(arg) for arg in args)
        print("deco_inner_fn %s %s"%(arg_str,result))
        return result
    return deco_inner_fn

class Solution:

    def __init__(self,value):
        self.value=value
        self.list=[]

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return "Solution:__str__"

    def __len__(self):
        return 1

    def __call__(self,string):
        self.list.append(string)

    @classmethod
    def classmethod(*args):
        print("class method is called." + str(args))
        return args

    @staticmethod
    def statmethod(*args):
        print("static method is called." +str(args))
        return args

    def multiple_args(self,*args,**args2):
        for index in range(len(args)):
            print("word=%s"%(args[index]))

        for name,value in args2:
            print(name,value)

    def re_usage(self,string):
        list=re.split(r'\W+',string)
        print(list)

    def string_to_list(self,string):
        list=string.split(' ')
        print(list)

    def remove_a_substring(self,string,substring):
        m=re.search(substring,string)
        string_output=string[:m.start()]+string[m.end():]
        print(string_output)

    def remove_a_substring2(self,string,substring):
        starting_location=string.find(substring)
        string_output=string[:starting_location]+string[starting_location+len(substring):]
        print(string_output)

    def encode_decode_string(self,string):
        binary=string.encode('utf8')
        print("After invoking encode, binary=%s"%(binary))
        binary2=bytes(string,encoding='utf_8')
        print("After invoking bytes,with encoding set to utf-8, binary2=%s"%(binary2))
        byte_array=bytearray(binary2)
        print("After invoking bytearray on bytes, byte_array=%s"%(byte_array))
        print("After invoking bytearray.decode()-->%s" % (bytearray.decode(byte_array)))


    def print_list(self):
        print(self.list)

    """
    A decorator is a callable that takes another function as argument 
    (the decorated function). 
    The decorator may perform some processing with the decorated function, and
    returns it or replaces it with another function or callable object.
    """
    @deco_outer_function
    def inner_function(self,a=1,b=2,c=3):
        print("Inner function")
        return "Hello"

sol=Solution(100)
print(sol)
print(len(sol))
sol.multiple_args("hello","world","xyz","abc",{"a":1,"b":2})
sol.re_usage("Hello world hello2 hello3")
sol.string_to_list("Hello world hello2 hello3")
sol.remove_a_substring("sriramsridhar@verizon.com","sridhar")
sol.remove_a_substring2("sriramsridhar@verizon.com","sridhar")
sol.encode_decode_string("sriramsridhar@verizon.com")
sol("Hello")
sol("Hello2")
sol("Hello3")
sol.print_list()
sol.inner_function()
print(sol)
sol.statmethod("Hello","Sriram")
sol.classmethod("Hello","Sriram")