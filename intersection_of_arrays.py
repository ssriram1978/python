
def find_match_between_two_continuous_arrays(array1,array2):
    array1_start = array1[0]
    array2_start = array2[0]
    array1_end = array1[len(array1)-1]
    array2_end = array2[len(array2)-1]

    if(array1_start<= array2_start and array2_start <= array1_end):
        if array2_end <= array1_end:
            return array2
        else:
            array3=[]
            for value in array2[0:(array1_end-array2_end)]:
                array3.append(value)
            return array3

    elif (array1_start > array2_start and array1_start <= array2_end):
        if (array1_end <= array2_end):
            return array1
        else:
            array3 = []
            for value in array1[0:(array2_end - array1_end)]:
                array3.append(value)
            return array3


array1=[3,4,5,6,7,8,9,10]
array2=[1,2,3,4]
array3=find_match_between_two_continuous_arrays(array1,array2)
print(array3)


