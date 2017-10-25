class MergeSort :
    def __init__(self,unsorted_array):
        #indexing start from 0, therefore right is length -1
        self.mergesort(unsorted_array,0,(len(unsorted_array)-1))

    def mergesort(self,unsorted_array,left,right):
        if left < right:
            #mid is left + right /2
            mid=(left+(right))//2
            #merge sort the array left to mid
            self.mergesort(unsorted_array,left,mid)
            #merge sort the array mid+1 to right (mid is already taken into consideration)
            self.mergesort(unsorted_array,mid+1,right)
            #merge both the arrays left and right.
            self.merge(unsorted_array,left,mid,right)

    def merge(self,sorted_array,left,mid,right):
        array1_len=mid-left+1
        array2_len=right-mid

        array1=[0] * (array1_len)
        array2=[0] * (array2_len)

        #prepare array1 from left to mid+1
        for index in range(0,array1_len):
            array1[index]= unsorted_array[left+index]

        #prepare array2 from mid to right
        for index in range(0,array2_len):
            array2[index]= unsorted_array[mid+1+index]

        #initialize array1 index and array2 index.
        array1_index=0
        array2_index=0

        #you are going to starting from left index in the sorted array.
        main_array_index=left

        #make sure not to go past the array1 len and array2 len
        while array1_index < array1_len and array2_index < array2_len:

            if array1[array1_index] < array2[array2_index]:
                #copy the array1 element to the sorted array because it is the smallest.
                sorted_array[main_array_index]=array1[array1_index]
                #bump up the array1 index by 1 to move to the next index.
                array1_index+=1
            else:
                # copy the array2 element to the sorted array because it is the smallest.
                sorted_array[main_array_index] = array2[array2_index]
                # bump up the array2 index by 1 to move to the next index.
                array2_index += 1
            # bump up the main array index by 1 to move to the next index.
            main_array_index += 1

        #copy the remaining elements from array1 to the sorted array.
        while array1_index < array1_len:
            sorted_array[main_array_index]=array1[array1_index]
            main_array_index+=1
            array1_index+=1

        #copy the remaining elements from array2 to the sorted array.
        while array2_index < array2_len:
            sorted_array[main_array_index]=array2[array2_index]
            main_array_index+=1
            array2_index+=1


unsorted_array=[15,7,13,8,2,19,4,1,16]
heap=MergeSort(unsorted_array)
print(unsorted_array)
