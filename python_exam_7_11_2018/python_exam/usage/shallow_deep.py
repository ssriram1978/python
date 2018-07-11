
from Lib import copy

def demo_shallow_deep():
    string1 = "sriram"
    string2 = "sridhar"
    list2 = [string1, string2]
    print("id(list2)={},id(list2[0])={},id(list2[1])={}".format(id(list2), id(list2[0]), id(list2[1])))
    list3 = list2
    print("id(list3)={},id(list3[0])={},id(list3[1])={}".format(id(list3), id(list3[0]), id(list3[1])))
    list4 = list2[:]
    print("id(list4)={},id(list4[0])={},id(list4[1])={}".format(id(list4), id(list4[0]), id(list4[1])))
    list5 = copy.copy(list2)
    print("id(list5)={},id(list5[0])={},id(list5[1])={}".format(id(list5), id(list5[0]), id(list5[1])))
    list6 = copy.deepcopy(list2)
    print("id(list6)={},id(list6[0])={},id(list6[1])={}".format(id(list6), id(list6[0]), id(list6[1])))

    dict1 = {"name1": "value1", "name2": "value2", "name3": "value3"}
    print("id(dict1)={}".format(id(dict1)), end=" ")
    for name, value in dict1.items():
        print("id(name) in dict1={}.".format(id(name)), end=" ")
        print("id(value) in dict1={}.".format(id(value)), end=" ")
    print("\n")
    dict2 = dict1
    print("id(dict2)={}".format(id(dict2)), end=" ")
    for name, value in dict2.items():
        print("id(name) in dict2={}.".format(id(name)), end=" ")
        print("id(value) in dict2={}.".format(id(value)), end=" ")
    print("\n")
    dict3 = copy.copy(dict1)
    print("id(dict3)={}".format(id(dict3)), end=" ")
    for name, value in dict3.items():
        print("id(name) in dict3={}.".format(id(name)), end=" ")
        print("id(value) in dict3={}.".format(id(value)), end=" ")
    print("\n")
    dict4 = copy.deepcopy(dict1)
    print("id(dict4)={}".format(id(dict4)), end=" ")
    for name, value in dict4.items():
        print("id(name) in dict4={}.".format(id(name)), end=" ")
        print("id(value) in dict4={}.".format(id(value)), end=" ")
    print("\n")


print("****************Demonstrating shallow/deep copy **************")
demo_shallow_deep()
