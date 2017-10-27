class Heap :
    def __init__(self,unsorted_array):
        array_len=len(unsorted_array)

        #find the mid point of the array
        range_max=(array_len-1)//2

        #prepare a max heap data structure from the mid point to the beginning of the array.
        for index in range(range_max,-1,-1):
            self.heapify(array_len,index,unsorted_array)

        #pop all the items from the end to the first element at 0th location.
        for i in range(array_len-1,-1,-1):
            #take a copy of the element at the current location
            temp=unsorted_array[i]
            #swap the current location with the element at location 0
            unsorted_array[i]=unsorted_array[0]
            #overwrite the location of the element at 0th location with the copied element.
            unsorted_array[0]=temp
            #invoke the max heap algorithm from current index to index 0.
            self.heapify(i,0, unsorted_array)

    def heapify(self,range,index,unsorted_array):
        #left node is current node times two plus one.
        left_index=index*2+1
        #right node is current node times two plus two.
        right_index=index*2+2

        #assume that maximum number is at the current index.
        max=index

        #find out if the left node is greater than current node
        if left_index < range and unsorted_array[left_index] > unsorted_array[max]:
            #assume left node is the max
            max=left_index

        #find out if the right node is greater than the max node.
        if right_index < range and unsorted_array[right_index] > unsorted_array[max]:
            #you found out that right node is the max node.
            max = right_index

        #if the max node that was previously assumed to tbe the current index is not eual to the current
        #node, then swap it.
        if max != index:
            temp=unsorted_array[index]
            unsorted_array[index]=unsorted_array[max]
            unsorted_array[max]=temp
            #recursively do the above said heapify algo from the node that was found to be max to the current node.
            #this is done because we want to bubble up the max node among the children of the max node.
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

def binary_search(input_num,sorted_array,start,end):
    if input_num == None:
        return -1
    if sorted_array == None or len(sorted_array) == 0:
        return -1
    if start > end :
        return -1

    mid=(start+end)//2
    if sorted_array[mid] == input_num:
        return 1
    elif sorted_array[mid] > input_num:
        return binary_search(input_num,sorted_array,start,mid-1)
    else:
        return binary_search(input_num, sorted_array, mid+1,end)

for index in range(len(array3)):
    print("search for %d in the sorted_array returned %d" %(array3[index],
                                                            binary_search(array3[index],array3,0,len(array3)-1)))

print("search for 20 in the sorted_array returned %d" %(binary_search(20,array3,0,len(array3)-1)))