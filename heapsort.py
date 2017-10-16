class Heap :
    def __init__(self,unsorted_array):
        array_len=len(unsorted_array)
        range_max=array_len//2
        for index in range(range_max-1,-1,-1):
            self.heapify(array_len,index,unsorted_array)

        for i in range(array_len-1,-1,-1):
            temp=unsorted_array[i]
            unsorted_array[i]=unsorted_array[0]
            unsorted_array[0]=temp
            self.heapify(i,0, unsorted_array)

    def heapify(self,range,index,unsorted_array):

        left_index=index*2+1
        right_index=index*2+2

        max=index

        if left_index < range and unsorted_array[left_index] > unsorted_array[max]:
            max=left_index

        if right_index < range and unsorted_array[right_index] > unsorted_array[max]:
            max = right_index

        if max != index:
            temp=unsorted_array[index]
            unsorted_array[index]=unsorted_array[max]
            unsorted_array[max]=temp
            self.heapify(range,max,unsorted_array)

    @staticmethod
    def merge(array1,array2):
        if array1==None or len(array1) == 0:
            return array2

        if array2 == None or len(array2) == 0:
                return array1

        array3=[]

        array1_index=0
        array2_index=0

        while(array1_index < len(array1) and array2_index < len(array2)):
            if(array1[array1_index] < array2[array2_index]):
                array3.append(array1[array1_index])
                array1_index+=1
            else:
                array3.append(array2[array2_index])
                array2_index+=1
        if array1_index < len(array1):
            for index in range(array1_index,len(array1),1):
                array3.append(array1[index])
        elif array2_index < len(array2):
            for index in range(array2_index,len(array2),1):
                array3.append(array2[index])

        return array3


unsorted_array=[15,7,13,8,2,19,4,1,16]
heap=Heap(unsorted_array)
print(unsorted_array)
unsorted_array2=[8,9,3,11,12,16,5,14,7]
heap2=Heap(unsorted_array2)
print(unsorted_array2)
array3=Heap.merge(unsorted_array,unsorted_array2)
print(array3)

