class Heap :
    def __init__(self,unsorted_array):
        range_max=len(unsorted_array)//2
        for index in range(0,range_max,1):
            self.heapify(range_max,index,unsorted_array)

        for i in range(len(unsorted_array)-1,0,-1):
            temp=unsorted_array[i]
            unsorted_array[i]=unsorted_array[0]
            unsorted_array[0]=temp
            self.heapify(i,0, unsorted_array)

    def heapify(self,range,index,unsorted_array):
        if(index<0):
            return None

        left_index=index*2 +1
        right_index=index*2 +2

        max=index

        if left_index < range and unsorted_array[max] < unsorted_array[left_index]:
            max=left_index

        if right_index < range and unsorted_array[max] < unsorted_array[right_index]:
            max=right_index

        if max != index:
            temp=unsorted_array[index]
            unsorted_array[index]=unsorted_array[max]
            unsorted_array[max]=temp
            self.heapify(range,max,unsorted_array)

unsorted_array=[5,7,3,8,2,9,4,1,6]
heap=Heap(unsorted_array)
print(unsorted_array)


