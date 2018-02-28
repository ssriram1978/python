"""
Given an array of n integers where n > 1, nums,
return an array output such that output[i] is equal to the
product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity?
(Note: The output array does not count as extra space for the purpose of space complexity analysis.)

"""

"""
Define a left array which multiplies all the elements before the current element.
Define a right array which multiplies all the elements after the current element.
Multiply left array and right array which results in the desired output.
"""

class Solution(object):
    def prepare_left_array(self,nums):
        left_array=[0]*len(nums)
        product=0
        for index in range(len(nums)):
            element=nums[index]
            if index == 0:
                #skip this element.
                product=element
                left_array[index]=1
            else:
                left_array[index]=product
                product*=element
        return left_array

    def prepare_right_array(self,nums):
        right_array=[0]*len(nums)
        product=0
        for index in range(len(nums)-1,-1,-1):
            element=nums[index]
            if index == len(nums)-1:
                #skip this element
                product=element
                right_array[index]=1
            else:
                right_array[index]=product
                product*=element
        return right_array

    def prepare_output(self,left_array,right_array):
        output_array=[0]*len(left_array)
        for index in range(len(left_array)):
            output_array[index]=left_array[index]*right_array[index]
        return output_array

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_array=self.prepare_left_array(nums)
        right_array=self.prepare_right_array(nums)
        output=self.prepare_output(left_array,right_array)
        return output

sol=Solution()
input=[1,2,3,4]
print(sol.productExceptSelf(input))
