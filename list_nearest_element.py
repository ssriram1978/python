"""
Given an array of numbers and an index i, return the index 
of the nearest larger number of the number at index i, 
where distance is measured in array indices.

For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

If two distances to larger numbers are the equal, 
then return any one of them. 
If the array at i doesn't have a nearest larger integer, then return null.

Follow-up: If you can preprocess the array, can you do this in constant time?
"""


def find_nearest_larger_integer(input_list, element):
    nearest_largest = None
    dict_of_item_index = {}
    if element not in input_list:
        return None
    #store all the item and its index in a dictionary. O(n)
    for index, item in enumerate(input_list):
        dict_of_item_index[item] = index
    print("dict_of_item_index={}.".format(dict_of_item_index))
    #get the keys and sort them. O(nlogn)
    sorted_keys = sorted(dict_of_item_index.keys())
    print("Sorted keys = {}".format(sorted_keys))
    #binary search and find the item in the sorted keys O(logn)
    item_index = sorted_keys.index(element)
    print("element index = {}.".format(item_index))
    #return None if you can't find the item in the list.
    if item_index == len(sorted_keys)-1:
        return None
    nearest_largest = abs(dict_of_item_index[sorted_keys[item_index+1]] \
        - dict_of_item_index[item])
    return nearest_largest


input_list = [4,1,3,5,6]

print("find_nearest_larger_integer returned {}"
.format(find_nearest_larger_integer(input_list,4)))