
def combination_without_repetition(list_of_numbers,
                            combinations_length):
    combinations = []
    #base case. if the current index exceeds the size of the list, return []
    if combinations_length == 1:
        return ([x] for x in list_of_numbers)
    combinations_dict = {}
    for index,item in enumerate(list_of_numbers):
        #recurse without the current element
        current_combinations = combination_without_repetition(list_of_numbers[:index] + \
                                                         list_of_numbers[index+1:],
                                                    combinations_length-1)
        for sub_item in current_combinations:
            key = str(sorted([item] + sub_item))
            if key not in combinations_dict:
                combinations.append([item] + sub_item) 
                combinations_dict[key] = 1
    return combinations
    
def permutations_without_repetition(list_of_numbers,
                            permutations_length):
    permutations = []
    #base case. if the current index exceeds the size of the list, return []
    if permutations_length == 1:
        return ([x] for x in list_of_numbers)
    for index,item in enumerate(list_of_numbers):
        #recurse without the current element
        current_permutations = permutations_without_repetition(list_of_numbers[:index] + \
                                                         list_of_numbers[index+1:],
                                                    permutations_length-1)
        for sub_item in current_permutations:
            permutations.append([item] + sub_item) 
    return permutations

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
    print("Permutations n!/(n-r)! of {}  without repetition and picking only {} at a time is len={}."
        .format(list_of_numbers,index,len(list(perm2))))

for index in range(1,6):
    comb=[]
    comb=combination_without_repetition(list_of_numbers,index)
    print("Combinations n!/(r! * (n-r)!) of {}  without repetition and picking only {} at a time is len={}."
        .format(list_of_numbers,index,len(list(comb))))

#print(permutations_of_numbers(list_of_numbers,3))
#print(permutations_of_numbers(list_of_numbers,4))
#print(permutations_of_numbers(list_of_numbers,5))
