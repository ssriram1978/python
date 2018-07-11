def reversed_function_usage(input):
    return list(reversed(input))

def sorted_function_usage(input):
    # return sorted(input,key=len) -- sort based upon the length of each element.
    # return sorted(input,reverse=True)
    # return sorted(input,key=lambda x:x[1]) -- used to sort based upon value in a dictionary.
    # return sorted(input,key=itemgetter(1)) -- used to sort based upon value in a dictionary.
    # return sorted(input,key=sorting_algo)  -- where you define def sorting_algo(x): return x[1]
    return sorted(input)

def sort_function_usage(input):
    if type(input) == list:
        input.sort()

print("reversed_function_usage(range(1,10))={}".format(reversed_function_usage(range(1, 10))))
print("reversed_function_usage(\"sriram\")={}".format(reversed_function_usage("sriram")))
print("sorted_function_usage(range(10,-1,-1)={}".format(sorted_function_usage(range(10, -1, -1))))
print("sorted_function_usage(\"sriram\")={}".format(sorted_function_usage("sriram")))
output = list(range(10, -1, -1))
print("function that does not return anything returns {} by default".format(sort_function_usage(output)))
print("sort_function_usage(range(10,-1,-1)={}".format(output))

