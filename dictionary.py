from operator import itemgetter,attrgetter,methodcaller
from collections import *
from functools import cmp_to_key

def compare(a,b):
    if a < b :
        return a
    else:
        return b

dict={}

dict["f"]="q"
dict["c"]="z"
dict["s"]="c"
dict["d"]="w"

print("original dict=")
print(dict)

sorted_dict_key=sorted(dict.items(),key=itemgetter(0),reverse=True)
print("sorted by key=")
print(sorted_dict_key)

sorted_dict_value=sorted(dict.items(),key=itemgetter(1),reverse=True)
print("sorted by value")
print(sorted_dict_value)

#sorted_dict_by_func=sorted(dict.items(),key=methodcaller(compare),reverse=True)

sorted_dict_by_func=sorted(dict.items(),key=cmp_to_key(compare),reverse=True)
print("sorted by function")
print(sorted_dict_by_func)
