"""
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
"""


class Solution:
    def __init__(self):
        self.max_result=0

    def find_second_number(self,nums,max_number):
        #just iterate the list to find the second number which when xored results in a maximum number
        max_result=0
        for number in nums:
            if number != max_number:
                xored_value=number ^ max_number
                if xored_value > max_result:
                    max_result=xored_value
        return max_result


    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #prepare a list that contains the numbers with largest MSB.
        largest_msb_list=[]
        found_largest_msb=False
        for index in range(31,-1,-1):
            mask=1<<index
            for index2 in range(len(nums)):
                if nums[index2]|mask > 0:
                    largest_msb_list.append(nums[index2])
                    found_largest_msb=True
            if found_largest_msb > 0:
                #you found a largest number
                #now your job is to find the right number when x'ored will result in the maximum number
                #note that MSB of the largest is 1. Therefore, you would prefer the right number to have
                #0 so that when 1 ored with 0 results in MSB as 1
                for index2 in range(len(largest_msb_list)):
                    max=self.find_second_number(nums,largest_msb_list[index2])
                    if max >= self.max_result:
                        self.max_result=max

                #break from the for loop that creates the msb mask
                break

        return self.max_result

sol=Solution()
list=[3, 10, 5, 25, 2, 8]
print(sol.findMaximumXOR(list))