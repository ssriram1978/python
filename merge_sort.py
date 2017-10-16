class MergeSort :
    def __init__(self,unsorted_array):
        self.mergesort(unsorted_array,0,len(unsorted_array))

    def mergesort(self,unsorted_array,left,right):
        if unsorted_array == None or len(unsorted_array) == 0 or left >= right:
            return None

        mid=((right-left)//2) + left

        if mid <= 0:
            return None
        print("mergesort:invoking mergesort,left=%d, mid=%d"%(left,mid))
        self.mergesort(unsorted_array,left,mid)
        print("mergesort:invoking mergesort,mid=%d, right=%d" % (mid+1, right))
        self.mergesort(unsorted_array,mid+1,right)
        print("mergesort:left=%d,right=%d and mid=%d" % (left, right, mid))
        self.merge(unsorted_array,left,mid,right)

    def merge(self,unsorted_array,left,mid,right):
        if unsorted_array == None or len(unsorted_array) == 0 or left >= right or left >= mid or mid >= right:
            return None

        print("merge:left=%d,right=%d and mid=%d" % (left, right, mid))

        array1=[]
        array2=[]

        for index in range(left,mid,1):
            array1.append(unsorted_array[index])

        for index in range(mid,right,1):
            array2.append(unsorted_array[index])

        print("array1")
        print(array1)

        print("array2")
        print(array2)


        array1_index=0
        array2_index=0
        main_array_index=left

        while array1_index < len(array1) and array2_index < len(array2) and main_array_index < right:
            if array1[array1_index] < array2[array2_index]:
                unsorted_array[main_array_index]=array1[array1_index]
                print("array1[%d]=%d is less than array2[%d]=%d copied %d to mainarray[%d]" %(array1_index,
                                                                                         array1[array1_index],
                                                                                         array2_index,
                                                                                         array2[array2_index],
                                                                                         unsorted_array[main_array_index],
                                                                                         main_array_index))
                array1_index+=1
            else:
                unsorted_array[main_array_index] = array2[array2_index]
                print("array1[%d]==%d is greater than or equal to array2[%d]=%d copied %d to mainarray[%d]" %(array1_index,
                                                                                          array1[array1_index],
                                                                                          array2_index,
                                                                                          array2[array2_index],
                                                                                          unsorted_array[main_array_index],
                                                                                          main_array_index))

                array2_index += 1
            main_array_index += 1

        if array1_index < len(array1):
            for index in range(array1_index,len(array1),1):
                unsorted_array[main_array_index]=array1[index]
                print("copying array1[%d]=%d to mainarray[%d]" % (array1_index,array1[index],main_array_index))
                main_array_index+=1

        if array2_index < len(array2):
            for index in range(array2_index, len(array2), 1):
                unsorted_array[main_array_index] = array2[index]
                print("copying array2[%d]=%d to mainarray[%d]" % (array2_index, array2[index], main_array_index))
                main_array_index += 1

        print("unsorted_array=")
        print(unsorted_array)



unsorted_array=[15,7,13,8,2,19,4,1,16]
heap=MergeSort(unsorted_array)
print(unsorted_array)
