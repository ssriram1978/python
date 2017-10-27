# A Python program to demonstrate working of string template
import string
import math
#from thread import *
import heapq
from collections import *

# List Student stores the name and marks of three students
Student = [('Ram',90), ('Ankit',78), ('Bob',92)]

# We are creating a basic structure to print the name and
# marks of the students.
t = string.Template('Hi $name, you have got $marks marks')

for i in Student:
	print (t.substitute(name = i[0], marks = i[1]))

print(math.log10(1000000))

