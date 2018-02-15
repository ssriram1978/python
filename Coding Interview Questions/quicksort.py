"""
This is an algorithm that runs at order of(nlogn).
It does not require extra storage and is in place sort and does not require extra memory.
This algorithm can be slower and may run at o(n**2) if you pick the wrong pivot.
Now, the algo goes like this:
pick a pivot which is start+(end-start)//2
start a loop which iterates until left is less than or equal to right
first find a number larger than pivot from the left most position.
start a loop from the end of the array that searches for an element that is smaller than pivot.
    Swap these two numbers.
    Continue this until you break from the loop
Recursively sort the left half and the right half.
"""
def quicksort(unsorted_list):
    if unsorted_list == None:
        return
    quicksort_recurse(unsorted_list,0,len(unsorted_list)-1)

def swap(unsorted_list,index1,index2):
    temp=unsorted_list[index1]
    unsorted_list[index1]=unsorted_list[index2]
    unsorted_list[index2]=temp

def partition(unsorted_list,start,end,pivot):
    while start <= end:
        while unsorted_list[start] < pivot:
            start += 1
        while unsorted_list[end] > pivot:
            end -= 1
        if start <= end:
            swap(unsorted_list, start, end)
            start+=1
            end-=1
    return start

def quicksort_recurse(unsorted_list,start,end):
    if start >= end:
        return
    pivot=unsorted_list[(start+end)//2]
    index=partition(unsorted_list,start,end,pivot)
    quicksort_recurse(unsorted_list,start,index-1)
    quicksort_recurse(unsorted_list,index,end)

unsorted_list=[1,6,3,9,2,4,8,5,7,6]
quicksort(unsorted_list)
print(unsorted_list)
