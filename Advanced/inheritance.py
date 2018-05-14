from collections import namedtuple
from collections import _itemgetter
import re
import sys


class Animal:

    def create(self,name):
        """Abstract method"""

class Dog(Animal):
    def __init__(self):
        self.name=""

    def create(self,name):
        self.name=name
        return "Dog" + str(name)


class Cat(Animal):
    def __init__(self):
        self.name = ""

    def create(self, name):
        self.name = name
        print("Cat %s" % (name))

animal=Dog()
animal.create("Hello")
mapped=map(animal.create,(range(11)))
print(mapped)
list_map=list(mapped)
print(list_map)
print(animal.create.__globals__)

nt=namedtuple('nt','x y')
a=nt(1,2)
print(a.x,a.y)
nt_list=[nt(i,j) for i in range(10) for j in range(20)]
print(nt_list)
for value in nt_list:
    print(value.x,value.y)

s = 'bicycle'
print(s[::3])
print(s[::-1])
print(s[::-2])

first_slice=slice(0,2)
second_slice=slice(2,5)
third_slice=slice(5,7)
print(s[first_slice],s[second_slice],s[third_slice])

tt=frozenset([1,2,3,4])
print(tt,str(hash(tt)))

index={}
WORD_RE=re.compile('\w+')
with open(sys.argv[1],encoding='utf-8') as fp:
    for line_no,line in enumerate(fp,1):
        for match in WORD_RE.finditer(line):
            word=match.group()
            index[word]+=1
for word in sorted(index,key=str.upper):
    print(word,index[word])



