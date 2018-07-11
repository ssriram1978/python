
def map_function_usage(start, end):
    list1 = [x for x in range(start, end)]
    list2 = [x ** 2 for x in range(start, end)]
    return list(map(lambda x, y: x + y, list1, list2))


def filter_function_usage(start, end, list_to_exclude):
    return list(filter(lambda x: x not in list_to_exclude, [x for x in range(start, end)]))


def reduce_function_usage(start, end):
    import functools
    return functools.reduce(lambda x, y: x * y, range(start, end))


print("map_function_usage(2,5)={}".format(map_function_usage(2, 5)))
print("filter_function_usage(1,10,[2,4,8])={}".format(filter_function_usage(1, 10, [2, 4, 8])))
print("reduce_function_usage(1,10)={}".format(reduce_function_usage(1, 10)))
