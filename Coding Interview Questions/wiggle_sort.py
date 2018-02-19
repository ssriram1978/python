"""
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].


"""
"""
Algorithm:
----------
A Simple Solution is to use sorting. First sort the input array, then start reading elements from the end
of the sorted array and start inserting them at locations 1,3,5,7,9,... into the sorted array.

For example, let the input array be {3, 6, 5, 10, 7, 20}. 
After sorting, we get {3, 5, 6, 7, 10, 20}.
Now start reading elements from the end and start inserting them into the sorted array.
20 gets inserted at location 1. {3,20,5,6,7,10}.
Then 10 gets inserted at location 3. {3,20,5,10,6,7}
Then 7 is at index 5 which is at the end of the array, therefore break from the loop.
"""


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums == None or nums == [] or len(nums) == 0:
            return None

        sorted_array=sorted(nums)
        index=1

        while index < len(sorted_array):
            popped_item=sorted_array.pop()
            sorted_array.insert(index,popped_item)
            index+=2

        return sorted_array

sol=Solution()
nums = [3, 5, 2, 1, 6, 4,9,7,8]
print(sol.wiggleSort(nums))