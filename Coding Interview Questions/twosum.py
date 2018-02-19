"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""
"""
Algorithm:
----------
Insert all the input elements into an input hash table.o(n)
Create an output hash table.
Create an output list.

For every element in the input list, do the following
    if the current element is already there in the output hash table, skip the current element
    
    compute result=target-current_element
    
    check if result is there in the input hash table o(1):
        if you found the element, then, make sure that this result is not there in the output hash table.o(1)
            After making sure that neither current element nor the result is there in the output hash table,
                append the current element and the result to the output list.
                insert the current element and the result to the output hash table.
return output list
        
"""
from collections import defaultdict

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums == None or nums == []:
            return None

        output_dict=defaultdict(int)
        output_list=[]
        input_dict=defaultdict(int)

        #insert all the elements into input_dict o(n)
        for element in nums:
            value=input_dict[element]
            if value == -1:
                input_dict[element]=1
            else:
                input_dict[element]+=1

        #iterate all elements from the list o(n)
        for element in nums:
            if output_dict[element] == 1:
                #element is already there in the output dict o(1)
                continue

            #element is not found in the dict
            result=target-element

            if result == element and input_dict[result] <= 1:
                #you cannot use the same number more than once
                #there has to be atleast one more repetition of the same number
                continue

            if output_dict[result] == 1:
                #element is already there in the output list o(1)
                continue

            if input_dict[result] >= 1:
                #result is there in the input dict
                #insert current element,value into input dict o(1)
                output_dict[element]=1
                output_dict[result]=1

                #append the current element, result into output list.
                output_list.append((element,result))

        return output_list

sol=Solution()
array=[3,2,3,6,0,1,9,6,6]
print(sol.twoSum(array,12))