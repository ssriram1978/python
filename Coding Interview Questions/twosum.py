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
with value as a list of all indexes of the elements in the list.

Create an output hash table which is used to mark all the indexes already there in the output list so that
you don't want to add duplicate entries and you don't want to traverse the output list at o(n) to search for
duplicates.

Create an output list that captures all the pairs which add up to the target.

For every element in the input list, do the following
    if the index of the current element is already there in the output hash table, skip the current element.
    
    compute result=target-current_element
    
    check if result is there in the input hash table o(1):
        If you found the element, 
            Get all the indexes of the result from the input hash table.
                Find an index that is not there in the output hash table.
                    If you found an index, then, use this index 
                            1. append the index of the current element 
                            and the index of the result to the output list.
                            2. insert the index of the current element and 
                            the index of the result to the output hash table.
                        
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
        #stores the indexes of the elements already there in the output list
        output_dict=defaultdict(int)
        #stores the indexes of the elements that add up to the target
        output_list=[]
        #stores the input elements in the dictionary where
        #current element in the input list is used as the key
        #current index of the element in the input list is used as the value
        input_dict=defaultdict(list)

        #insert all the elements into input_dict o(n)
        for index in range(len(nums)):
            input_dict[nums[index]].append(index)

        print(input_dict)

        #iterate all elements from the list o(n)
        for index in range(len(nums)):
            element=nums[index]

            if output_dict[index] == 1:
                #skip this element if it is already there in the output list.
                continue

            #element is not found in the dict
            result=target-element

            #find the index of the result from input dict
            indexes_of_result_list=input_dict[result]

            if len(indexes_of_result_list) == 0:
                #no elements found
                continue

            print("possible match is %d and %d"%(element,result)+str(indexes_of_result_list))
            #pick the index that is not there in the output list
            match_found=False
            for value in indexes_of_result_list:
                if value != index and output_dict[value] == 0:
                    match_found=True
                    break

            if match_found==False:
                #all indexes are used up
                continue
            else:
                #store the index of the first number in the output_dict
                output_dict[index]=1
                #store the index of the second number in the output_dict
                output_dict[value]=1
                #append the current element index and result index into output list.
                print("Appending %d %d to output_list"%(index,value))
                output_list.append((index,value))

        return output_list

sol=Solution()
array=[3,2,3,6,0,1,9,6,6,9]
print(sol.twoSum(array,12))