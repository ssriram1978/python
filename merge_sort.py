class MergeSort :
    def __init__(self,unsorted_array):
        self.mergesort(unsorted_array,0,(len(unsorted_array)-1))

    def mergesort(self,unsorted_array,left,right):
        if left < right:
            mid=(left+(right-1))//2
            self.mergesort(unsorted_array,left,mid)
            self.mergesort(unsorted_array,mid+1,right)
            self.merge(unsorted_array,left,mid,right)

    def merge(self,unsorted_array,left,mid,right):
        array1_len=mid-left+1
        array2_len=right-mid

        array1=[0] * (array1_len)
        array2=[0] * (array2_len)

        for index in range(0,array1_len):
            array1[index]= unsorted_array[left+index]

        for index in range(0,array2_len):
            array2[index]= unsorted_array[mid+1+index]

        array1_index=0
        array2_index=0
        main_array_index=left

        while array1_index < array1_len and array2_index < array2_len:
            if array1[array1_index] < array2[array2_index]:
                unsorted_array[main_array_index]=array1[array1_index]
                array1_index+=1
            else:
                unsorted_array[main_array_index] = array2[array2_index]
                array2_index += 1
            main_array_index += 1

        while array1_index < array1_len:
            unsorted_array[main_array_index]=array1[array1_index]
            main_array_index+=1
            array1_index+=1

        while array2_index < array2_len:
            unsorted_array[main_array_index]=array2[array2_index]
            main_array_index+=1
            array2_index+=1

unsorted_array=[15,7,13,8,2,19,4,1,16]
heap=MergeSort(unsorted_array)
print(unsorted_array)
