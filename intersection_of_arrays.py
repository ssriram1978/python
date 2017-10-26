
def find_match_between_two_continuous_arrays(array1,array2):
    array1_start = array1[0]
    array2_start = array2[0]
    array1_end = array1[len(array1)-1]
    array2_end = array2[len(array2)-1]

    #if array1_start is less than or equal to array2 start and
    #array2 start is less than or equal to array1 end
    if(array1_start<= array2_start and array2_start <= array1_end):
        #if array2 is a subset of array1, just return array2
        if array2_end <= array1_end:
            return array2
        else:
            #copy only the elements from array2 that is in array1
            array3=[]
            for index in range(0,(array1_end-array2_start)+1):
                array3.append(array2[index])
            return array3
    #check if array1 start is greater than array2 start and
    ## array1start is less than or equal to array2 end
    elif (array1_start > array2_start and array1_start <= array2_end):
        #if array1 is a subset of array2 then return array1
        if (array1_end <= array2_end):
            return array1
        else:
            #copy only the elements from array1 that is in array2
            array3 = []
            for index in range(0,(array2_end-array1_start)+1):
                array3.append(array1[index])
            return array3


array2=[3,4,5,6,7,8,9,10]
array1=[1,2]
array3=find_match_between_two_continuous_arrays(array1,array2)
print(array3)


