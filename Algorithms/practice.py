import this

message = "hello world {} {}".format("Manish", "Sriram")
print(message.swapcase())
message += ' sriram\n '
print(message)
list = ['toy', 'sriram', 'sridhar', '12']
print(list[2])
# list.extend(10)
print(list)
list.sort()
print(list)

for word in list:
    if (word == 'sriram'):
        print(word.capitalize())
        print(word == 'sriram')
    else:
        print(word)

print(list[0:2])

list2 = list[2:]
print(list2)
tuple = ('home', 'work', 'vacation', 14)
print(tuple)
if ('work' in tuple and 14 in tuple and 'Work' not in tuple):
    canprint = True
    print("'work' in tuple and 14 in tuple and 'work'not in tuple." + canprint.__str__())

items = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}

for key, value in items.items():
    print("key=" + key + "value=" + value + "\n")

# message=""
# while message != "quit" :
#    message = input("Enter a message. Type quit to quit");

# dictionary={}
# poll=True
# while poll:
#    name=input("Enter your name")
#    value=input("Enter your value")
#    dictionary[name]=value
#    do_continue=input("Do you want to continue? Type no to quit")
#    if(do_continue =="no"):
#        poll=False


# print(dictionary.items())

items2 = {}


def function(items, copied_item, **name_value_pair):
    for name, value in items.items():
        print(name + value)
        copied_item[name] = value
        # items.popitem()
    for name, value in name_value_pair.items():
        print(name + value)
        copied_item[name] = value


function(items, items2, name='ss', name2='ss2')

print(items2)

# for name,value in items.items():
#    print("items2.items=" + items2.keys() + items2.values())
