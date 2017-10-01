# A Python program to demonstrate working of string template
import string
import math
from thread import *
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

print("demonstrate heapq functionality")
heap=[]
heapq.heappush(heap,100)
heapq.heappush(heap,200)
heapq.heappush(heap,300)
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))

print("demonstrate stack functionality\n")
stack=[10,20,30]
stack.append(40)
stack.append(50)
print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("demonstrate queue functionality\n")
queue_list=[1,2,3,4,5,6]
queue=deque(queue_list)
queue.append(7)
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

print("demonstrate hashtable\n")
hashtable=[];
hashtable.insert(10,"sriram")
hashtable.insert(20,"sridhar")
print hashtable
