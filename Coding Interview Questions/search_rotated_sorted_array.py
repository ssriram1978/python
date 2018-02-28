"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""

"""
1. First find the pivot point.
    In order to find the pivot point, perform a binary search with the following condition:
    Start a while loop with the condition while start < end:
    mid=start+(end-start)//2
    if array[mid] > arr[mid+1]:
        you found the pivot point. (mid)
        return it.
    else if array[mid] < arr[mid-1]:
        you found the pivot point. (mid-1)
        return it
    If you found that array[start] is greater than array[mid],
        then the pivot has to be between start and mid
            end=mid-1
    Else if you found that array[mid] is less than array[end]
        then the pivot has to be between mid and end.
        start=mid+1
    If you did not find any pivot, then, return -1
    
2. If you did not find any pivot, then 
        Perform Binary search on the whole array O(logn).
   Else:
        If target is equal to the content located at pivot,
            then return True.
        If the target value is greater than the content located at pivot
            If so, Perform Binary search with start=0 end=pivot-1.
            Else:
                Perform Binary search with start=pivot+1,end=len(array)-1
If you found the element, return True else return False
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
