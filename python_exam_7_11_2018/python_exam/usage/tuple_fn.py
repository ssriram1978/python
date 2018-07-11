
tuple1='sriram','sriram2'
print(tuple1)
print(id(tuple1))
tuple1+='sridhar',
print(tuple1)
print(id(tuple1))

for elements in tuple1:
    print(elements)

try:
    tuple1[0]="sriram3"
except:
    print("Invalid operation")

list1=[i for i in "sriram"]
list2=[i for i in "sriram2"]
print(list1,list2)
tuple2=[list1,list2]
print(tuple2[0],tuple2[1])
list1+='3'
print(tuple2[0])
