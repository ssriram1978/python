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
    def findPivot(self, nums):
        start=0
        end=len(nums)-1
        pivot=-1
        while start < end:
            mid=start+(end-start)//2
            if nums[mid] > nums[mid+1]:
                #you found the pivot
                pivot=mid
                break
            elif nums[mid] < nums[mid-1]:
                #you found the pivot
                pivot=mid-1
                break
            if nums[start] >= nums[mid]:
                end=mid-1
            elif nums[end] <= nums[mid]:
                start=mid+1
        return pivot

    def PerformBinarySearch(self,nums,start,end,target):
        foundElement=False
        while start < end:
            mid=start+(end-start)//2
            if target == nums[mid]:
                foundElement=True
                break
            if target > nums[mid]:
                start=mid+1
            else:
                end=mid-1
        return foundElement

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if type(target) != int or nums==None or len(nums)==0:
            return None
        start=0
        end=len(nums)-1
        found=False
        pivot=self.findPivot(nums)
        if pivot==-1:
            #no pivot found
            #do a regular Binary Search
            found=self.PerformBinarySearch(nums,target,start,end)
        else:
            print("Found pivot=%d"%(nums[pivot]))
            if target==nums[pivot]:
                found=True
            elif target < nums[pivot] and target >= nums[0]:
                found=self.PerformBinarySearch(nums,start,pivot-1,target)
            elif target >= nums[pivot+1] and target <= nums[len(nums)-1]:
                found = self.PerformBinarySearch(nums, pivot+1, len(nums)-1,target)
        return found


sol=Solution()
pivoted_array=[4,5,6,7,0,1,2]
print(sol.search(pivoted_array,1))
