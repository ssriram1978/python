def binary_search(sorted_list,input):
    isFound=False
    if sorted_list == None or input==None:
        return isFound
    isFound=binary_search_recurse(sorted_list,input,0,len(sorted_list)-1)
    return isFound

def binary_search2(sorted_list,input):
    isFound=False
    if sorted_list == None or input==None:
        return isFound
    isFound=binary_search_non_recurse(sorted_list,input)
    return isFound

def binary_search_recurse(sorted_list,input,start,end):
    if start > end:
        return False
    mid=(start+end)//2
    if sorted_list[mid] == input:
        return True
    elif sorted_list[mid] < input:
        return binary_search_recurse(sorted_list, input, mid+1, end)
    else:
        return binary_search_recurse(sorted_list, input, start, mid-1)

def binary_search_non_recurse(sorted_list,input):
    start=0
    end=len(sorted_list)-1

    while(start <= end):
        mid = (start + end) // 2
        if sorted_list[mid] == input:
            return True
        elif sorted_list[mid] < input:
            start=mid+1
        else:
            end = mid-1

    return False

sorted_list=[2,3,4,5,6,7,8,9]
for index in range(10):
    print("Recursive Search %d returned %s" %(index,str(binary_search(sorted_list,index))))

for index in range(10):
    print("Non Recursive Search %d returned %s" %(index,str(binary_search_non_recurse(sorted_list,index))))
