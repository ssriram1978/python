"""
o(nlogn)
It uses extra memory to merge two arrays.
Given an unsorted array, invoke a recursive function that takes in start and end of the array.
mid = start + (end-start//2)
sort(array, start, mid)
sort(array, mid+1, end)
merge(array,start,mid,end)

in merge function:
set the left array start and end, right array start and end.
create a temp list that stores the elements from both the arrays in a sorted order.
After iterating over the two arrays, pop elements from temp array and overwrite the main unsorted array.
"""

from collections import deque

def mergesort(unsorted_list):
    if unsorted_list == None:
        return None
    mergesort_recurse(unsorted_list,0,len(unsorted_list)-1)

def merge(unsorted_list,start,mid,end):
    left_start=start
    left_end=mid
    right_start=mid+1
    right_end=end
    temp_list=deque()

    while left_start <= left_end and right_start <= right_end:
        if unsorted_list[left_start] <= unsorted_list[right_start]:
            temp_list.append(unsorted_list[left_start])
            left_start+=1
        else:
            temp_list.append(unsorted_list[right_start])
            right_start+=1
    while left_start <= left_end:
        temp_list.append(unsorted_list[left_start])
        left_start+=1
    while right_start <= right_end:
        temp_list.append(unsorted_list[right_start])
        right_start+=1

    for index in range(start,end+1):
        unsorted_list[index]=temp_list.popleft()

def mergesort_recurse(unsorted_list,start,end):
    if start >= end:
        return
    mid=start + (end-start)//2
    mergesort_recurse(unsorted_list,start,mid)
    mergesort_recurse(unsorted_list,mid+1,end)
    merge(unsorted_list,start,mid,end)

unsorted_list=[1,6,3,9,2,4,8,5,7,6]
mergesort(unsorted_list)
print(unsorted_list)
