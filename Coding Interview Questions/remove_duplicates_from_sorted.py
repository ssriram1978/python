"""
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
"""

"""
Given that you have a sorted array,
All you need to do is remove the duplicates.
Start a while loop until you reach the end of the array:
    Check if the content of current index is equal to the content of current index +1
        If they match, then, delete the current content.
        Else
        Skip the current content move to the next element in the array.
return the output.
"""

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0:
            print("Invalid arguments")
            return None
        current_index=0
        while current_index < len(nums)-1:
            if nums[current_index] == nums[current_index+1]:
                del nums[current_index]
            else:
                current_index+=1

sol=Solution()
list=[1,1,1,1,2,3,3]
sol.removeDuplicates(list)
print(list)
