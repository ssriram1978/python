from collections import defaultdict
from collections import deque
import unittest

class python_default_datastructures():
    def __init__(self,start,end):
        self.dict1=defaultdict(int)
        self.list1 = list(range(1, 10))
        self.list2 = deque()
        self.start=start
        self.end=end
        self.tuple=()

    def perform_default_dict_operations(self):
        self.dict1[4]="Hello"
        self.dict1[3]="Hello2"
        self.dict1[2]="Hello3"
        self.dict1[1]="Hello4"
        print(self.dict1)
        for name,value in self.dict1.items():
            print(name,value)
        list1=sorted(self.dict1,key=lambda x: self.dict1.keys(),reverse=True)
        print(list1)
        list2 = sorted(self.dict1.keys())
        print(list2)
        list3=sorted(self.dict1.values())
        print(list3)

    def perform_stack_operations(self):
        print(self.list1)
        self.list1=self.list1[::-1]
        print(self.list1[0:100])
        while len(self.list1):
            print(self.list1.pop())
        list2=list(range(10,1,-1))
        print(list2)
        list3=[[10,20],[9,31],[8,41],[7,51]]
        print(sorted(list3,key=lambda x: x[0]))
        print(sorted(list3,key=lambda x: x[1]))

    def perform_tuple_operations(self):
        self.tuple=(0,1,2,3,4,5,6,7)
        for index in range(0,len(self.tuple)):
            print(self.tuple[index])


    def perform_queue_operations(self):
        for index in range(self.start,self.end):
            self.list2.append(index)
        print(self.list2)
        while len(self.list2):
            print(self.list2.popleft())

    def perform_string_operation(self):
        string_var="Hello world"
        string_var=string_var.strip(' ')
        print(string_var)
        list_of_char=[ x for x in string_var]
        print(list_of_char)
        string_var2=''.join(list_of_char)
        print(string_var2)

obj=python_default_datastructures(10,20)
#obj.perform_default_dict_operations()
#obj.perform_stack_operations()
#obj.perform_queue_operations()
#obj.perform_queue_operations()
#obj.perform_tuple_operations()
obj.perform_string_operation()

class first_unittest(unittest.TestCase):
    """Testing my class python_default_datastructures."""
    def test_perform_default_dict_operations(self):
        obj = python_default_datastructures(10, 20)
        obj.perform_default_dict_operations()
        self.assertEqual(1,1)

unittest.main()