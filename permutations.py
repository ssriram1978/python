

def permutations_without_repetition(list_of_numbers,
                            combinations_len):
    combinations = []
    #base case. if the current index exceeds the size of the list, return []
    if combinations_len == 1:
        return ([x] for x in list_of_numbers)
    for index,item in enumerate(list_of_numbers):
        #recurse without the current element
        current_combinations = permutations_without_repetition(list_of_numbers[:index] + \
                                                         list_of_numbers[index+1:],
                                                    combinations_len-1)
        for sub_item in current_combinations:
            combinations.append([item] + sub_item) 
    return combinations

def permutations_of_numbers(list_of_numbers):
    output=[]
    if len(list_of_numbers) == 1:
        return [list_of_numbers]
    for index, item in enumerate(list_of_numbers):
        perm_list = \
            permutations_of_numbers(list_of_numbers[:index] \
                + list_of_numbers[index+1:])
        for sub_item in perm_list:
            output += [[item] + sub_item]
    return output

list_of_numbers=['1','2','3','4','5']
perm = permutations_of_numbers(list_of_numbers)
#print("permutation of {} = {}".format(list_of_numbers,perm))
print("Length of perm = {},5*4*3*2*1={}".format(len(perm),str(5*4*3*2*1)))
for index in range(1,6):
    perm2=[]
    perm2=permutations_without_repetition(list_of_numbers,index)
    print("Permutations of {}  without repetition and picking only {} at a time is len={}."
        .format(list_of_numbers,index,len(list(perm2))))


#print(combinations_of_numbers(list_of_numbers,3))
#print(combinations_of_numbers(list_of_numbers,4))
#print(combinations_of_numbers(list_of_numbers,5))
